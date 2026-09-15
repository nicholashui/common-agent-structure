import base64
from pathlib import Path

import httpx
import pytest

import casops.project_generate as project_generate
from casops.project_comms import GOLD_BODY_PROBE, append_comm, save_comms
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.project_generate import (
    MAX_DOWNLOAD_BYTES,
    _http_get_bytes,
    allowed_imagine_download_url,
    default_video_config,
    generate_project_media,
    generator_catalog,
    motion_prompt,
    resolve_download_redirect,
    safe_output_file,
    still_prompt,
)
from casops.projects import write_project


REPO = Path(__file__).resolve().parents[2]


def _project(root: Path, text: str) -> None:
    folder = root / "asain-beauty"
    write_project(
        root,
        {
            "schema_version": "casops.project.v1",
            "id": "asain-beauty",
            "name": "asain-beauty",
            "title": "Asain Beauty",
            "brief": "Short vertical beauty clip. Adult East Asian woman.",
            "graph": {"nodes": [], "edges": []},
        },
        dry_run=False,
        create=True,
    )
    out = folder / "output"
    out.mkdir()
    (out / "asain-beauty-prompt.txt").write_text(text, encoding="utf-8")
    save_comms(
        root,
        "asain-beauty",
        {"items": [], "decisions": [{"id": "dec-01", "agent_id": "video.promptengineer"}]},
        dry_run=False,
    )


def test_prompts_are_still_then_motion() -> None:
    text = (
        "Frame\n15-second, 9:16 vertical.\n\n"
        "Subject\nAdult East Asian woman. mole under left eye.\n\n"
        "Coverage / performance\n0–3s smash. 3–6s macro.\n\n"
        "Camera lock\nNo orbit.\n\n"
        "Sound\nRoom tone.\n"
    )
    still = still_prompt(text)
    motion = motion_prompt(text)
    assert "Do not animate" in still
    assert "Adult East Asian woman" in still
    assert "Hold the composition" in motion
    assert "0–3s smash" in motion
    assert "Hair stays off the lips" in still
    assert "Do not put hair in the mouth" in motion
    assert "Do not chew or eat hair" in motion
    assert GOLD_BODY_PROBE not in still
    assert GOLD_BODY_PROBE not in motion


def test_catalog_has_grok_and_declared_tags() -> None:
    rows = generator_catalog(configured=True)
    ids = [row["id"] for row in rows]
    assert ids[0] == "grok-imagine"
    assert "grok-image" in ids
    for extra in ("kling", "veo", "seedance", "sora", "runway", "luma", "pika", "hailuo", "wan", "ltx", "gpt-image"):
        assert extra in ids
    grok = next(row for row in rows if row["id"] == "grok-imagine")
    assert grok["live"] is True and grok["configured"] is True
    kling = next(row for row in rows if row["id"] == "kling")
    assert kling["live"] is False and kling["configured"] is False


def test_safe_clip_path_allows_clips_subdir(tmp_path: Path) -> None:
    from casops.project_generate import _safe_output_clip_path

    nested = tmp_path / "asain-beauty" / "output" / "clips"
    nested.mkdir(parents=True)
    (nested / "CLIP.asain-beauty.001-canonical.yaml").write_text("{}", encoding="utf-8")
    path = _safe_output_clip_path(tmp_path, "asain-beauty", "clips/CLIP.asain-beauty.001-canonical.yaml")
    assert path is not None and path.is_file()
    assert _safe_output_clip_path(tmp_path, "asain-beauty", "sample/asain-beauty-prompt.txt") is None
    assert _safe_output_clip_path(tmp_path, "asain-beauty", "../secret.yaml") is None


def test_safe_output_rejects_sample(tmp_path: Path) -> None:
    with pytest.raises(Exception):
        safe_output_file(tmp_path, "asain-beauty", "../sample/asain-beauty-prompt.txt")
    with pytest.raises(Exception):
        safe_output_file(tmp_path, "asain-beauty", "foo/bar.mp4")


def test_safe_output_file_does_not_mkdir(tmp_path: Path) -> None:
    path = safe_output_file(tmp_path, "asain-beauty", "clip.mp4")
    assert path.name == "clip.mp4"
    assert not (tmp_path / "asain-beauty" / "output").exists()


def test_download_host_allowlist() -> None:
    assert allowed_imagine_download_url("https://vidgen.x.ai/clip.mp4") is True
    assert allowed_imagine_download_url("https://x.ai/v") is True
    assert allowed_imagine_download_url("https://evilx.ai/clip.mp4") is False
    assert allowed_imagine_download_url("https://evil.example/clip.mp4") is False
    assert allowed_imagine_download_url("http://169.254.169.254/latest") is False
    assert allowed_imagine_download_url("javascript:alert(1)") is False


def test_redirect_off_host_is_exfil() -> None:
    with pytest.raises(CasopsError) as exc:
        resolve_download_redirect("https://vidgen.x.ai/a", "https://127.0.0.1/x")
    assert exc.value.code == ErrorCode.SAF_EXFILTRATION
    joined = resolve_download_redirect("https://api.x.ai/a", "/cdn/clip.mp4")
    assert joined.startswith("https://api.x.ai/")
    assert "clip.mp4" in joined


def test_dry_run_does_not_call_imagine(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "xai-test")
    _project(tmp_path, "Frame\n9:16\n")
    calls = {"n": 0}

    def boom(*_args, **_kwargs):
        calls["n"] += 1
        raise AssertionError("network")

    result = generate_project_media(
        tmp_path,
        "asain-beauty",
        engine="grok-imagine",
        dry_run=True,
        post_json=boom,
        get_json=boom,
        get_bytes=boom,
    )
    assert result["error"] == "dry_run"
    assert calls["n"] == 0
    assert not (tmp_path / "asain-beauty" / "output" / "asain-beauty.mp4").exists()


def test_kling_is_fail_closed(tmp_path: Path) -> None:
    _project(tmp_path, "Frame\n9:16\n")
    result = generate_project_media(tmp_path, "asain-beauty", engine="kling", dry_run=False)
    assert result["live"] is False
    assert result["error"] == "engine_not_activated"
    items = result["comms"]["items"]
    assert items[-1]["kind"] == "generated_media"
    assert items[-1]["live"] is False
    assert result["comms"]["decisions"][0]["id"] == "dec-01"


def test_grok_imagine_saves_video(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "xai-test")
    _project(tmp_path, "Frame\n15-second, 9:16\n\nSubject\nmole under left eye\n\nCoverage / performance\nmacro crawl\n")
    jpeg = base64.b64encode(b"JPEGDATA").decode()

    def post_json(url, headers, payload, timeout):
        assert headers["Authorization"].startswith("Bearer ")
        if url.endswith("/images/generations"):
            assert payload["aspect_ratio"] == "9:16"
            return {"data": [{"b64_json": jpeg}]}
        if url.endswith("/videos/generations"):
            assert payload["image"]["url"].startswith("data:image/")
            assert "Hold the composition" in payload["prompt"]
            return {"request_id": "vid-1"}
        raise AssertionError(url)

    def get_json(url, headers, timeout):
        assert url.endswith("/videos/vid-1")
        return {"status": "done", "video": {"url": "https://vidgen.x.ai/clip.mp4", "duration": 10}}

    def get_bytes(url, headers, timeout):
        return b"MP4DATA"

    result = generate_project_media(
        tmp_path,
        "asain-beauty",
        engine="grok-imagine",
        config={"duration": 10, "resolution": "1080p", "mode": "i2v"},
        dry_run=False,
        post_json=post_json,
        get_json=get_json,
        get_bytes=get_bytes,
        sleep=lambda _s: None,
    )
    video = tmp_path / "asain-beauty" / "output" / "asain-beauty.mp4"
    still = tmp_path / "asain-beauty" / "output" / "asain-beauty-still.jpg"
    assert video.read_bytes() == b"MP4DATA"
    assert still.read_bytes() == b"JPEGDATA"
    assert result["live"] is True
    item = result["comms"]["items"][-1]
    assert item["kind"] == "generated_media"
    assert item["from"] == "video.promptengineer"
    assert item["media"]["kind"] == "video"
    assert "video.continuity" in item["agents"]
    assert GOLD_BODY_PROBE not in item["text"]
    assert not (tmp_path / "asain-beauty" / "sample").exists()
    assert item["media"]["url"].startswith("/api/v3/projects/asain-beauty/output/file?name=")


def test_imagine_download_rejects_off_host(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "xai-test")
    _project(tmp_path, "Frame\n9:16\n\nSubject\nmole\n")
    jpeg = base64.b64encode(b"JPEGDATA").decode()

    def post_json(url, headers, payload, timeout):
        if url.endswith("/images/generations"):
            return {"data": [{"b64_json": jpeg}]}
        if url.endswith("/videos/generations"):
            return {"request_id": "vid-evil"}
        raise AssertionError(url)

    def get_json(url, headers, timeout):
        return {"status": "done", "video": {"url": "https://evil.example/clip.mp4"}}

    def get_bytes(url, headers, timeout):
        raise AssertionError("must not fetch off-host")

    with pytest.raises(CasopsError) as exc:
        generate_project_media(
            tmp_path,
            "asain-beauty",
            engine="grok-imagine",
            dry_run=False,
            post_json=post_json,
            get_json=get_json,
            get_bytes=get_bytes,
            sleep=lambda _s: None,
        )
    assert exc.value.code == ErrorCode.SAF_EXFILTRATION
    assert not (tmp_path / "asain-beauty" / "output" / "asain-beauty.mp4").exists()


def test_imagine_download_rejects_oversize(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "xai-test")
    _project(tmp_path, "Frame\n9:16\n\nSubject\nmole\n")
    jpeg = base64.b64encode(b"JPEGDATA").decode()

    def post_json(url, headers, payload, timeout):
        if url.endswith("/images/generations"):
            return {"data": [{"b64_json": jpeg}]}
        if url.endswith("/videos/generations"):
            return {"request_id": "vid-big"}
        raise AssertionError(url)

    def get_json(url, headers, timeout):
        return {"status": "done", "video": {"url": "https://vidgen.x.ai/clip.mp4"}}

    def get_bytes(url, headers, timeout):
        return b"x" * (MAX_DOWNLOAD_BYTES + 1)

    with pytest.raises(CasopsError) as exc:
        generate_project_media(
            tmp_path,
            "asain-beauty",
            engine="grok-imagine",
            dry_run=False,
            post_json=post_json,
            get_json=get_json,
            get_bytes=get_bytes,
            sleep=lambda _s: None,
        )
    assert exc.value.code == ErrorCode.PERF_ROUTE_UNAVAILABLE
    assert not (tmp_path / "asain-beauty" / "output" / "asain-beauty.mp4").exists()


def test_http_get_bytes_refuses_oversize_content_length() -> None:
    reads = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        def body():
            reads["n"] += 1
            yield b"x" * 32

        return httpx.Response(
            200,
            headers={"Content-Length": str(MAX_DOWNLOAD_BYTES + 8)},
            content=body(),
        )

    transport = httpx.MockTransport(handler)
    with httpx.Client(transport=transport, follow_redirects=False) as client:
        with pytest.raises(CasopsError) as exc:
            _http_get_bytes("https://vidgen.x.ai/clip.mp4", {}, 5.0, client=client)
    assert exc.value.code == ErrorCode.PERF_ROUTE_UNAVAILABLE
    assert "too large" in exc.value.operator_message
    assert reads["n"] == 0


def test_http_get_bytes_stream_aborts_without_content_length(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(project_generate, "MAX_DOWNLOAD_BYTES", 64)
    sent = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        def body():
            for _ in range(40):
                sent["n"] += 16
                yield b"x" * 16

        return httpx.Response(200, content=body())

    transport = httpx.MockTransport(handler)
    with httpx.Client(transport=transport, follow_redirects=False) as client:
        with pytest.raises(CasopsError) as exc:
            _http_get_bytes("https://vidgen.x.ai/clip.mp4", {}, 5.0, client=client)
    assert exc.value.code == ErrorCode.PERF_ROUTE_UNAVAILABLE
    assert sent["n"] > 64
    assert sent["n"] < 16 * 40


def test_http_get_bytes_returns_bounded_body() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"MP4DATA")

    transport = httpx.MockTransport(handler)
    with httpx.Client(transport=transport, follow_redirects=False) as client:
        raw = _http_get_bytes("https://vidgen.x.ai/clip.mp4", {}, 5.0, client=client)
    assert raw == b"MP4DATA"
