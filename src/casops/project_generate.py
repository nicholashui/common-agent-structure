"""Operator-gated video generation from a project's assembled instruction.

Grok Imagine (Image 2.0 still, then Video 1.5 I2V) is the live engine.
Other tags stay fail-closed. sample/ is never written.
"""

from __future__ import annotations

import os
import re
import time
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.project_comms import append_comm, output_prompt_path, read_output
from casops.projects import normalize_slug, read_project
from casops.runtime.llm import PROVIDER_CATALOG

GENERATOR_TAGS: list[dict[str, Any]] = [
    {
        "id": "grok-imagine",
        "label": "Grok Imagine",
        "engine": "grok-imagine",
        "live": True,
        "why": "Still with grok-imagine-image-2.0, then grok-imagine-video-1.5 I2V.",
    },
    {
        "id": "grok-image",
        "label": "Grok Image",
        "engine": "grok-image",
        "live": True,
        "why": "Still only: grok-imagine-image-2.0, 9:16, no motion.",
    },
    {
        "id": "kling",
        "label": "Kling 3.0",
        "engine": "kling",
        "live": False,
        "why": "Declared tag. Host has not activated Kling.",
    },
    {
        "id": "veo",
        "label": "Veo 3.1",
        "engine": "veo",
        "live": False,
        "why": "Declared tag. Host has not activated Veo.",
    },
    {
        "id": "seedance",
        "label": "Seedance 2.0",
        "engine": "seedance",
        "live": False,
        "why": "Declared tag. Host has not activated Seedance.",
    },
    {
        "id": "sora",
        "label": "Sora 2",
        "engine": "sora",
        "live": False,
        "why": "Declared tag. Host has not activated Sora.",
    },
    {
        "id": "runway",
        "label": "Runway Gen-4",
        "engine": "runway",
        "live": False,
        "why": "Declared tag. Host has not activated Runway.",
    },
    {
        "id": "luma",
        "label": "Luma Ray 3",
        "engine": "luma",
        "live": False,
        "why": "Declared tag. Host has not activated Luma.",
    },
    {
        "id": "pika",
        "label": "Pika 2.2",
        "engine": "pika",
        "live": False,
        "why": "Declared tag. Host has not activated Pika.",
    },
    {
        "id": "hailuo",
        "label": "Hailuo 02",
        "engine": "hailuo",
        "live": False,
        "why": "Declared tag. Host has not activated Hailuo.",
    },
    {
        "id": "wan",
        "label": "Wan 2.2",
        "engine": "wan",
        "live": False,
        "why": "Declared tag. Host has not activated Wan.",
    },
]

LOCK_AGENTS = [
    "video.promptengineer",
    "video.creativedirector",
    "video.director",
    "video.cinematographer",
    "video.mua_makeup",
    "video.cameraoperator",
    "video.continuity",
    "video.critic",
]

_FILE_SAFE = re.compile(r"^[A-Za-z0-9._-]+$")
_HEADING = re.compile(r"^(?:#{1,3}\s*)?([A-Za-z0-9].+?)\s*$")
MAX_DOWNLOAD_BYTES = 64 * 1024 * 1024
_REDIRECT_STATUSES = {301, 302, 303, 307, 308}

PostJson = Callable[[str, dict[str, str], dict[str, Any], float], dict[str, Any]]
GetJson = Callable[[str, dict[str, str], float], dict[str, Any]]
GetBytes = Callable[[str, dict[str, str], float], bytes]


def _http_post_json(url: str, headers: dict[str, str], payload: dict[str, Any], timeout: float) -> dict[str, Any]:
    import httpx

    response = httpx.post(url, headers=headers, json=payload, timeout=timeout)
    try:
        body = response.json()
    except Exception:
        body = {"error": response.text[:400]}
    if response.status_code >= 400:
        detail = ""
        if isinstance(body, dict):
            err = body.get("error")
            if isinstance(err, dict):
                detail = str(err.get("message") or err.get("code") or "")
            elif err:
                detail = str(err)
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail=detail or f"Imagine HTTP {response.status_code}")
    if not isinstance(body, dict):
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="Imagine response was not an object")
    return body


def _http_get_json(url: str, headers: dict[str, str], timeout: float) -> dict[str, Any]:
    import httpx

    response = httpx.get(url, headers=headers, timeout=timeout)
    try:
        body = response.json()
    except Exception:
        body = {"error": response.text[:400]}
    if response.status_code >= 400:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail=f"Imagine poll HTTP {response.status_code}")
    if not isinstance(body, dict):
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="Imagine poll was not an object")
    return body


def allowed_imagine_download_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"https", "http"}:
        return False
    host = (parsed.hostname or "").lower().rstrip(".")
    if not host or parsed.username or parsed.password:
        return False
    return host == "x.ai" or host.endswith(".x.ai")


def resolve_download_redirect(current: str, location: str) -> str:
    from urllib.parse import urljoin

    nxt = urljoin(current, location or "")
    if not allowed_imagine_download_url(nxt):
        raise CasopsError(ErrorCode.SAF_EXFILTRATION, detail="download redirect host not allowed")
    return nxt


def _declared_download_size(headers: Any) -> int | None:
    raw = ""
    if headers is None:
        return None
    getter = getattr(headers, "get", None)
    if callable(getter):
        raw = str(getter("content-length") or getter("Content-Length") or "")
    elif isinstance(headers, dict):
        raw = str(headers.get("content-length") or headers.get("Content-Length") or "")
    if not raw.strip():
        return None
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return None
    return value if value >= 0 else None


def _http_get_bytes(url: str, headers: dict[str, str], timeout: float, *, client: Any = None) -> bytes:
    import httpx

    current = url
    own = client is None
    session = client or httpx.Client(timeout=timeout, follow_redirects=False)
    try:
        for _ in range(6):
            if not allowed_imagine_download_url(current):
                raise CasopsError(ErrorCode.SAF_EXFILTRATION, detail="download host not allowed")
            with session.stream("GET", current, headers=headers) as response:
                if response.status_code in _REDIRECT_STATUSES:
                    current = resolve_download_redirect(current, response.headers.get("location") or "")
                    continue
                response.raise_for_status()
                declared = _declared_download_size(response.headers)
                if declared is not None and declared > MAX_DOWNLOAD_BYTES:
                    raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="download too large")
                chunks: list[bytes] = []
                total = 0
                for chunk in response.iter_bytes():
                    if not chunk:
                        continue
                    total += len(chunk)
                    if total > MAX_DOWNLOAD_BYTES:
                        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="download too large")
                    chunks.append(chunk)
                return b"".join(chunks)
    finally:
        if own:
            session.close()
    raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="download redirected too many times")


def generator_catalog(*, configured: bool) -> list[dict[str, Any]]:
    rows = []
    for item in GENERATOR_TAGS:
        row = dict(item)
        row["configured"] = bool(configured) if item["live"] else False
        rows.append(row)
    return rows


def default_video_config(instruction: str = "") -> dict[str, Any]:
    text = instruction or ""
    duration = 15 if "15-second" in text or "15s" in text else 10
    aspect = "9:16" if "9:16" in text else "9:16"
    return {
        "engine": "grok-imagine",
        "mode": "i2v",
        "aspect_ratio": aspect,
        "duration": duration,
        "resolution": "1080p",
        "image_model": "grok-imagine-image-2.0",
        "video_model": "grok-imagine-video-1.5",
        "image_resolution": "2k",
    }


def _sections(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    current = ""
    buf: list[str] = []

    def flush() -> None:
        nonlocal current, buf
        if current:
            found[current] = "\n".join(buf).strip()
        buf = []

    for line in (text or "").splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("•") and len(stripped) < 80:
            key = stripped.lstrip("#").strip()
            if key in {
                "Creative direction",
                "Frame",
                "Subject",
                "Hair",
                "Makeup",
                "Skin",
                "Light",
                "Coverage / performance",
                "Camera lock",
                "Sound, if the model supports native audio",
                "Sound",
                "Negatives",
            } or (" | " in key and key[:1].isdigit()):
                flush()
                current = "Sound" if key.startswith("Sound") else key
                continue
        buf.append(line)
    flush()
    return found


def still_prompt(instruction: str) -> str:
    parts = _sections(instruction)
    chunks = [
        "Photoreal still, 9:16 vertical phone-macro close-up. Locked adult identity. Do not animate.",
        parts.get("Frame", ""),
        parts.get("Subject", ""),
        parts.get("Hair", ""),
        parts.get("Makeup", ""),
        parts.get("Skin", ""),
        parts.get("Light", ""),
        parts.get("Negatives", ""),
    ]
    text = "\n".join(item for item in chunks if item).strip()
    if "Hair stays off the lips" not in text:
        text = (text + "\nHair stays off the lips. No hair in the mouth.").strip()
    return text[:4500]


def motion_prompt(instruction: str) -> str:
    parts = _sections(instruction)
    beats = parts.get("Coverage / performance") or "\n".join(
        parts.get(key, "") for key in list(parts) if key[:1].isdigit()
    )
    chunks = [
        "Animate this locked still. Keep the same adult identity, moles, hair, makeup, and light. Motion and sound only. Do not re-describe the face.",
        beats,
        parts.get("Camera lock", ""),
        parts.get("Sound", ""),
        "Hair stays off the lips. Do not put hair in the mouth. Do not chew or eat hair. Do not hook a strand with the lip.",
    ]
    text = "\n".join(item for item in chunks if item).strip()
    return text[:4500]


def output_dir(root: Path, slug: str, *, create: bool = True) -> Path:
    folder = Path(root) / slug / "output"
    if "sample" in folder.parts:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="sample/ is read-only")
    if create:
        folder.mkdir(parents=True, exist_ok=True)
    return folder


def safe_output_file(root: Path, slug: str, name: str) -> Path:
    normalize_slug(slug)
    if not _FILE_SAFE.match(name) or ".." in name or "/" in name or "\\" in name:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="bad output filename")
    path = output_dir(root, slug, create=False) / name
    if "sample" in path.parts:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="sample/ is read-only")
    return path


def list_output_media(root: Path, slug: str) -> list[dict[str, str]]:
    folder = Path(root) / slug / "output"
    if not folder.is_dir():
        return []
    rows: list[dict[str, str]] = []
    for path in sorted(folder.iterdir()):
        if not path.is_file() or not _FILE_SAFE.match(path.name):
            continue
        suffix = path.suffix.lower()
        if suffix in {".mp4", ".webm"}:
            kind = "video"
        elif suffix in {".jpg", ".jpeg", ".png", ".webp"}:
            kind = "image"
        else:
            continue
        rows.append(
            {
                "name": path.name,
                "kind": kind,
                "path": f"project/{slug}/output/{path.name}",
                "url": f"/api/v3/projects/{slug}/output/file?name={path.name}",
            }
        )
    return rows


def _xai_auth() -> tuple[str, str]:
    spec = PROVIDER_CATALOG["xai"]
    key = os.environ.get(spec["key_env"], "").strip()
    base = (os.environ.get(spec.get("base_env", ""), "") or spec.get("default_base") or "").rstrip("/")
    if not key:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="XAI_API_KEY is not configured")
    return key, base


def _headers(key: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def _data_url(path: Path) -> str:
    raw = path.read_bytes()
    suffix = path.suffix.lower()
    mime = {".png": "image/png", ".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}.get(suffix, "image/jpeg")
    import base64

    return f"data:{mime};base64," + base64.b64encode(raw).decode("ascii")


def _save_url(
    url: str,
    dest: Path,
    headers: dict[str, str],
    get_bytes: GetBytes,
) -> None:
    if not allowed_imagine_download_url(url):
        raise CasopsError(ErrorCode.SAF_EXFILTRATION, detail="download host not allowed")
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower().rstrip(".")
    auth: dict[str, str] = {}
    if host == "x.ai" or host.endswith(".x.ai"):
        auth = {"Authorization": headers.get("Authorization", "")}
    raw = get_bytes(url, auth, 120.0)
    if len(raw) > MAX_DOWNLOAD_BYTES:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="download too large")
    dest.write_bytes(raw)


def _generate_still(
    *,
    prompt: str,
    config: dict[str, Any],
    dest: Path,
    key: str,
    base: str,
    post_json: PostJson,
    get_bytes: GetBytes,
) -> str:
    body = post_json(
        f"{base}/images/generations",
        _headers(key),
        {
            "model": str(config.get("image_model") or "grok-imagine-image-2.0"),
            "prompt": prompt,
            "n": 1,
            "aspect_ratio": str(config.get("aspect_ratio") or "9:16"),
            "resolution": str(config.get("image_resolution") or "2k"),
        },
        120.0,
    )
    data = body.get("data") if isinstance(body.get("data"), list) else []
    first = data[0] if data and isinstance(data[0], dict) else {}
    b64 = str(first.get("b64_json") or "")
    url = str(first.get("url") or "")
    if b64:
        import base64

        dest.write_bytes(base64.b64decode(b64))
        return url
    if not url:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="Imagine image returned no url")
    _save_url(url, dest, _headers(key), get_bytes)
    return url


def _generate_video(
    *,
    prompt: str,
    config: dict[str, Any],
    image_path: Path | None,
    dest: Path,
    key: str,
    base: str,
    post_json: PostJson,
    get_json: GetJson,
    get_bytes: GetBytes,
    sleep: Callable[[float], None] = time.sleep,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": str(config.get("video_model") or "grok-imagine-video-1.5"),
        "prompt": prompt,
        "aspect_ratio": str(config.get("aspect_ratio") or "9:16"),
        "duration": int(config.get("duration") or 10),
        "resolution": str(config.get("resolution") or "1080p"),
    }
    if image_path is not None and image_path.is_file():
        payload["image"] = {"url": _data_url(image_path)}
    body = post_json(f"{base}/videos/generations", _headers(key), payload, 60.0)
    request_id = str(body.get("request_id") or "")
    if not request_id:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="Imagine video returned no request_id")
    deadline = time.time() + 180
    result: dict[str, Any] = {}
    while time.time() < deadline:
        result = get_json(f"{base}/videos/{request_id}", _headers(key), 30.0)
        status = str(result.get("status") or "")
        if status == "done":
            break
        if status == "failed":
            err = result.get("error") if isinstance(result.get("error"), dict) else {}
            raise CasopsError(
                ErrorCode.PERF_ROUTE_UNAVAILABLE,
                detail=str(err.get("message") or "Imagine video failed"),
            )
        sleep(2.0)
    else:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="Imagine video timed out")
    video = result.get("video") if isinstance(result.get("video"), dict) else {}
    url = str(video.get("url") or "")
    if not url:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="Imagine video returned no url")
    _save_url(url, dest, _headers(key), get_bytes)
    return {"request_id": request_id, "url": url, "duration": video.get("duration")}


def generate_project_media(
    root: Path,
    slug: str,
    *,
    engine: str,
    config: dict[str, Any] | None = None,
    dry_run: bool,
    post_json: PostJson = _http_post_json,
    get_json: GetJson = _http_get_json,
    get_bytes: GetBytes = _http_get_bytes,
    sleep: Callable[[float], None] = time.sleep,
) -> dict[str, Any]:
    normalize_slug(slug)
    read_project(root, slug)
    instruction = str(read_output(root, slug).get("text") or "")
    if not instruction.strip():
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="no assembled instruction in output/")
    tag = next((item for item in GENERATOR_TAGS if item["id"] == engine or item["engine"] == engine), None)
    if tag is None:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail=f"unknown generator {engine}")
    merged = default_video_config(instruction)
    if isinstance(config, dict):
        for key in ("mode", "aspect_ratio", "duration", "resolution", "image_model", "video_model", "image_resolution"):
            if config.get(key) not in (None, ""):
                merged[key] = config[key]
    try:
        merged["duration"] = max(1, min(15, int(merged["duration"])))
    except (TypeError, ValueError):
        merged["duration"] = 10
    if dry_run:
        return {
            "honesty": "CHARACTERIZATION",
            "engine": tag["id"],
            "live": False,
            "error": "dry_run",
            "note": "Dry-run is on. Uncheck Dry-run in the header to submit to Grok Imagine.",
            "media": [],
        }
    if not tag["live"]:
        saved = append_comm(
            root,
            slug,
            {
                "node_id": "output-prompt",
                "from": "video.promptengineer",
                "to": "human_operator",
                "kind": "generated_media",
                "text": (
                    f"{tag['label']} is a declared generator tag only. "
                    "Host has not activated this engine. Fail-closed. "
                    f"Lock agents: {', '.join(LOCK_AGENTS)}."
                ),
                "live": False,
                "provider": tag["id"],
                "error": "engine_not_activated",
                "agents": LOCK_AGENTS,
            },
            dry_run=False,
        )
        return {
            "honesty": "CHARACTERIZATION",
            "engine": tag["id"],
            "live": False,
            "error": "engine_not_activated",
            "comms": saved,
            "media": [],
        }

    key, base = _xai_auth()
    folder = output_dir(root, slug)
    still_path = folder / f"{slug}-still.jpg"
    video_path = folder / f"{slug}.mp4"
    media: list[dict[str, str]] = []
    note_parts = [f"Lock agents: {', '.join(LOCK_AGENTS)}."]
    mode = str(merged.get("mode") or "i2v")
    if tag["id"] == "grok-image" or (tag["id"] == "grok-imagine" and mode != "t2v"):
        _generate_still(
            prompt=still_prompt(instruction),
            config=merged,
            dest=still_path,
            key=key,
            base=base,
            post_json=post_json,
            get_bytes=get_bytes,
        )
        media.append(
            {
                "name": still_path.name,
                "kind": "image",
                "path": f"project/{slug}/output/{still_path.name}",
                "url": f"/api/v3/projects/{slug}/output/file?name={still_path.name}",
            }
        )
        note_parts.append(f"Still saved {still_path.name}.")
    if tag["id"] == "grok-image":
        text = "Grok Image rendered the locked still. " + " ".join(note_parts)
    elif tag["id"] == "grok-imagine":
        image_path = still_path if still_path.is_file() and mode != "t2v" else None
        _generate_video(
            prompt=motion_prompt(instruction) if image_path is not None else instruction[:4500],
            config=merged,
            image_path=image_path,
            dest=video_path,
            key=key,
            base=base,
            post_json=post_json,
            get_json=get_json,
            get_bytes=get_bytes,
            sleep=sleep,
        )
        poster = f"/api/v3/projects/{slug}/output/file?name={still_path.name}" if still_path.is_file() else ""
        clip = {
            "name": video_path.name,
            "kind": "video",
            "path": f"project/{slug}/output/{video_path.name}",
            "url": f"/api/v3/projects/{slug}/output/file?name={video_path.name}",
        }
        if poster:
            clip["poster"] = poster
        media.append(clip)
        kind_label = "I2V" if image_path is not None else "T2V"
        text = (
            f"Grok Imagine rendered the clip ({merged['duration']}s {merged['aspect_ratio']} {merged['resolution']} {kind_label}). "
            + " ".join(note_parts)
            + f" Video saved {video_path.name}."
        )
    else:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="engine not activated")

    primary = next((item for item in media if item["kind"] == "video"), media[0] if media else None)
    saved = append_comm(
        root,
        slug,
        {
            "node_id": "output-prompt",
            "from": "video.promptengineer",
            "to": "human_operator",
            "kind": "generated_media",
            "text": text,
            "live": True,
            "provider": tag["id"],
            "agents": LOCK_AGENTS,
            "media": primary,
        },
        dry_run=False,
    )
    return {
        "honesty": "CHARACTERIZATION",
        "engine": tag["id"],
        "live": True,
        "config": merged,
        "media": media,
        "comms": saved,
        "note": "Not an eval PASS. sample/ was not written.",
    }
