import json
from pathlib import Path

from casops.project_comms import GOLD_BODY_PROBES, walkthrough_module
from casops.project_generate import generate_project_media
from casops.projects import write_project
from casops.video_prompt.assemble import assemble_clip, clip_from_walkthrough, write_clip_files
from casops.video_prompt.compile import (
    COMPILER_VERSION,
    compile_clip,
    write_compiled_package,
)
from casops.video_prompt.schema import validate_clip


REPO = Path(__file__).resolve().parents[2]
SLUGS = ("asain-beauty", "european-handsome", "japanese-grandma-gta", "hongkong-grandma-gta")


def test_grok_compile_from_canonical_not_sample() -> None:
    clip = clip_from_walkthrough(walkthrough_module("european-handsome"))
    validate_clip(clip)
    compiled = compile_clip(clip, "xai.grok-imagine-video-1.5.i2v")
    still = compiled["prompt"]["still"]
    motion = compiled["prompt"]["motion"]
    identity = clip["creative"]["shots"][0]["subjects"][0]["identity"]
    assert compiled["status"] == "ok"
    assert compiled["live"] is True
    assert compiled["compiler_version"] == COMPILER_VERSION
    assert "Do not animate" in still
    assert identity.split(".")[0] in still
    assert not still.lower().lstrip().startswith("9:16")
    assert compiled.get("guide") == "spec/grok_imagine_operation_guide.md"
    assert "hard, cold sunlight" in still.lower() or "7:20am" in still
    assert "opening smash" not in still.lower()
    assert "Hold the composition" in motion
    assert "opening smash" in motion.lower()
    assert "Hair stays off the lips" in still
    assert "Hair stays off the lips" in motion
    assert "Do not chew or eat hair" in still
    assert "Do not chew or eat hair" in motion
    assert any(row["requirement"] == "hair-off-lips" and row["disposition"] == "prompted" for row in compiled["coverage"])
    assert compiled["request"]["still"]["prompt"] == still
    assert compiled["request"]["video"]["prompt"] == motion
    assert compiled["request"]["video"]["duration"] == 15
    assert compiled["request"]["video"]["aspect_ratio"] == "9:16"
    assert "image" not in compiled["request"]["video"]
    blob = json.dumps(compiled)
    sample = (REPO / "project" / "european-handsome" / "sample" / "european-handsome-prompt.txt").read_text(
        encoding="utf-8"
    )
    for probe in GOLD_BODY_PROBES:
        assert probe not in still
        assert probe not in motion
        assert probe not in blob
    assert still.strip() != sample.strip()
    assert motion.strip() != sample.strip()


def test_four_slugs_compile_without_gold_probes() -> None:
    for slug in SLUGS:
        clip = clip_from_walkthrough(walkthrough_module(slug))
        compiled = compile_clip(clip)
        assert compiled["status"] == "ok"
        text = compiled["prompt"]["still"] + "\n" + compiled["prompt"]["motion"]
        for probe in GOLD_BODY_PROBES:
            assert probe not in text


def test_ltx_compile_is_blocked_not_a_fake_request() -> None:
    clip = clip_from_walkthrough(walkthrough_module("asain-beauty"))
    compiled = compile_clip(clip, "lightricks.ltx-2.stub")
    assert compiled["status"] == "blocked"
    assert compiled["live"] is False
    assert compiled["request"] == {}
    assert compiled["generator_tag"] == "ltx"


def test_seedance_compile_is_blocked_not_a_fake_request() -> None:
    clip = clip_from_walkthrough(walkthrough_module("asain-beauty"))
    compiled = compile_clip(clip, "bytedance.seedance-2.0.stub")
    assert compiled["status"] == "blocked"
    assert compiled["live"] is False
    assert compiled["request"] == {}
    assert compiled["prompt"]["motion"]
    assert compiled["guide"] == "spec/seedance_operation_guide.md"
    assert compiled["diagnostics"][0]["code"] == "CAPABILITY_PROFILE_NOT_LIVE"
    assert any(row["disposition"] == "unsupported" for row in compiled["coverage"])
    assert compiled["proposal"]["live"] is False


def test_write_compiled_package(tmp_path: Path) -> None:
    clip = clip_from_walkthrough(walkthrough_module("european-handsome"))
    compiled = compile_clip(clip)
    dest = write_compiled_package(tmp_path / "compiled" / "grok-imagine", compiled)
    assert (dest / "compiled.prompt.txt").is_file()
    assert (dest / "compiled.request.json").is_file()
    assert (dest / "compiled.diagnostics.json").is_file()
    assert (dest / "compiled.manifest.json").is_file()
    request = json.loads((dest / "compiled.request.json").read_text(encoding="utf-8"))
    assert request["video"]["model"] == "grok-imagine-video-1.5"
    assert "sample" not in dest.parts


def test_generate_dry_run_returns_compile_snapshot(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "xai-test")
    _project(tmp_path, "Frame\n15-second, 9:16\n\nSubject\nmole under left eye\n")
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
    assert result["compiled"]["status"] == "ok"
    assert "Do not animate" in result["compiled"]["prompt"]["still"]
    assert calls["n"] == 0
    assert not (tmp_path / "asain-beauty" / "output" / "compiled").exists()
    assert not (tmp_path / "asain-beauty" / "output" / "asain-beauty.mp4").exists()


def test_generate_uses_canonical_not_t4_text(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "xai-test")
    _project(tmp_path, "Frame\n15-second, 9:16\n\nSubject\nT4-FACE-LOCK-SHOULD-NOT-EMIT\n")
    clip = assemble_clip(
        project_id="asain-beauty",
        thesis="Canonical CONTROL",
        why="WHY: compile from yaml",
        frame="15-second, 9:16 vertical.",
        sound="Room tone.",
        subject="CANONICAL-FACE-LOCK-XYZ adult identity.",
        hair="Hair never crosses the mouth.",
        skin="Real pores.",
        makeup="No makeup.",
        light="Hard 4pm sun.",
        beats="0–3s | smash hold.\n3–6s | macro rake.",
        camera="No orbit.",
        negatives="no hair in the mouth, no chewing or eating hair",
    )
    write_clip_files(tmp_path / "asain-beauty" / "output", "asain-beauty", clip)
    (tmp_path / "asain-beauty" / "output" / "asain-beauty-prompt.txt").write_text(
        "Frame\n15-second, 9:16\n\nSubject\nT4-FACE-LOCK-SHOULD-NOT-EMIT\n",
        encoding="utf-8",
    )
    seen = {"still": "", "motion": ""}

    def post_json(url, headers, payload, timeout):
        if url.endswith("/images/generations"):
            seen["still"] = str(payload.get("prompt") or "")
            return {"data": [{"b64_json": "QQ=="}]}
        if url.endswith("/videos/generations"):
            seen["motion"] = str(payload.get("prompt") or "")
            return {"request_id": "vid-canon"}
        raise AssertionError(url)

    def get_json(url, headers, timeout):
        return {"status": "done", "video": {"url": "https://vidgen.x.ai/clip.mp4", "duration": 15}}

    result = generate_project_media(
        tmp_path,
        "asain-beauty",
        engine="grok-imagine",
        dry_run=False,
        post_json=post_json,
        get_json=get_json,
        get_bytes=lambda *_a, **_k: b"MP4DATA",
        sleep=lambda _s: None,
    )
    assert result["live"] is True
    assert result["clip_source"] == "canonical"
    assert "CANONICAL-FACE-LOCK-XYZ" in seen["still"]
    assert "T4-FACE-LOCK-SHOULD-NOT-EMIT" not in seen["still"]
    assert "Hold the composition" in seen["motion"]
    package = tmp_path / "asain-beauty" / "output" / "compiled" / "grok-imagine" / "compiled.request.json"
    assert package.is_file()
    assert not (tmp_path / "asain-beauty" / "sample").exists()


def test_ltx_generate_still_fail_closed(tmp_path: Path) -> None:
    _project(tmp_path, "Frame\n9:16\n")
    result = generate_project_media(tmp_path, "asain-beauty", engine="ltx", dry_run=False)
    assert result["live"] is False
    assert result["error"] == "engine_not_activated"
    assert result["media"] == []
    assert result["compiled"]["status"] == "blocked"
    assert result["compiled"]["request"] == {}


def test_seedance_generate_still_fail_closed(tmp_path: Path) -> None:
    _project(tmp_path, "Frame\n9:16\n")
    result = generate_project_media(tmp_path, "asain-beauty", engine="seedance", dry_run=False)
    assert result["live"] is False
    assert result["error"] == "engine_not_activated"
    assert result["media"] == []
    assert result["compiled"]["status"] == "blocked"
    assert result["compiled"]["request"] == {}
    diag = tmp_path / "asain-beauty" / "output" / "compiled" / "seedance" / "compiled.diagnostics.json"
    assert diag.is_file()
    payload = json.loads(diag.read_text(encoding="utf-8"))
    assert payload["status"] == "blocked"


def test_read_output_includes_compile_preview() -> None:
    from casops.project_comms import read_output

    payload = read_output(REPO / "project", "european-handsome")
    assert payload["canonical_exists"] is True
    assert payload["compile_note"] == "compiled from canonical v2"
    assert payload["compiled"]["status"] == "ok"
    assert any(row["disposition"] == "prompted" for row in payload["compiled"]["coverage"])
    subject = next(row for row in payload["sections"] if row["heading"] == "Subject")
    assert subject["owner"] == "video.continuity"
    assert subject["path"] == "creative.shots.subjects"
    seedance = read_output(REPO / "project", "european-handsome", engine="seedance")
    assert seedance["compiled"]["status"] == "blocked"
    assert seedance["compiled"]["request"] == {}
    assert any(row["severity"] == "error" for row in seedance["critic_warnings"])


def _project(root: Path, text: str) -> None:
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
    out = root / "asain-beauty" / "output"
    out.mkdir(parents=True, exist_ok=True)
    (out / "asain-beauty-prompt.txt").write_text(text, encoding="utf-8")
