"""ISSUE-0009 P4: adapter compile. Canonical stays CONTROL; vendors get a dialect package."""

from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path
from typing import Any

from casops.video_prompt.dialects import GUIDE_BY_TAG, dialect_prompts
from casops.video_prompt.profiles import ProfileError, load_profile, profile_for_tag
from casops.video_prompt.schema import ClipSchemaError, validate_clip

COMPILER_VERSION = "casops.video_prompt.compile.v1"
PROMPT_CHAR_CAP = 4500
GROK_I2V_PROFILE = "xai.grok-imagine-video-1.5.i2v"
GROK_STILL_PROFILE = "xai.grok-imagine-image-2.0.still"
GROK_LIVE_TAGS = frozenset({"grok-imagine", "grok-image"})

# House hair-off-lips lines compiled from constraints (not a generate-time magic string).
HOUSE_HAIR_OFF_LIPS = (
    "Hair stays off the lips.",
    "No hair in the mouth.",
    "Do not put hair in the mouth.",
    "Do not chew or eat hair.",
    "Do not hook a strand with the lip.",
)

_WORD_RE = re.compile(r"[^a-z0-9]+")


def _norm(text: str) -> str:
    return _WORD_RE.sub("", (text or "").lower())


def _fmt_s(value: Any) -> str:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value or "0")
    if number.is_integer():
        return str(int(number))
    return str(number)


def _first_shot(clip: dict[str, Any]) -> dict[str, Any]:
    creative = clip.get("creative") if isinstance(clip.get("creative"), dict) else {}
    shots = creative.get("shots") if isinstance(creative.get("shots"), list) else []
    first = shots[0] if shots and isinstance(shots[0], dict) else {}
    return first


def _first_subject(shot: dict[str, Any]) -> dict[str, Any]:
    subjects = shot.get("subjects") if isinstance(shot.get("subjects"), list) else []
    first = subjects[0] if subjects and isinstance(subjects[0], dict) else {}
    return first


def _join(*parts: Any) -> str:
    return "\n".join(str(item).strip() for item in parts if str(item or "").strip())


def _mentions_hair_mouth(text: str) -> bool:
    low = (text or "").lower()
    return "hair" in low and any(token in low for token in ("mouth", "lip", "teeth", "chew", "eat"))


def _forbid_list(clip: dict[str, Any]) -> list[str]:
    constraints = clip.get("constraints") if isinstance(clip.get("constraints"), dict) else {}
    raw = constraints.get("forbid") if isinstance(constraints.get("forbid"), list) else []
    return [str(item).strip() for item in raw if str(item).strip()]


def _constraint_bucket(clip: dict[str, Any], key: str) -> list[str]:
    constraints = clip.get("constraints") if isinstance(clip.get("constraints"), dict) else {}
    raw = constraints.get(key) if isinstance(constraints.get(key), list) else []
    return [str(item).strip() for item in raw if str(item).strip()]


def _already_has(line: str, lines: list[str]) -> bool:
    needle = _norm(line)
    if not needle:
        return True
    for item in lines:
        other = _norm(item)
        if not other:
            continue
        if needle == other:
            return True
        if len(needle) >= 12 and len(other) >= 12 and (needle in other or other in needle):
            return True
    return False


def _unique_lines(*groups: list[str]) -> list[str]:
    out: list[str] = []
    for group in groups:
        for item in group:
            if item and not _already_has(item, out):
                out.append(item)
    return out


def constraint_lines(clip: dict[str, Any]) -> tuple[list[str], str]:
    """Compile hair-off-lips from constraints.forbid; fill house lines only if missing."""
    forbid = _forbid_list(clip)
    hair = [item for item in forbid if _mentions_hair_mouth(item)]
    source = "constraints.forbid" if hair else "constraints.forbid+house"
    lines = list(hair)
    for house in HOUSE_HAIR_OFF_LIPS:
        if not _already_has(house, lines):
            lines.append(house)
    return lines, source


def _beats_text(shot: dict[str, Any]) -> str:
    action = shot.get("action") if isinstance(shot.get("action"), dict) else {}
    beats = action.get("beats") if isinstance(action.get("beats"), list) else []
    lines: list[str] = []
    for beat in beats:
        if not isinstance(beat, dict):
            continue
        body = str(beat.get("action") or "").strip()
        if beat.get("start_s") is None or beat.get("end_s") is None:
            if body:
                lines.append(body)
            continue
        lines.append(f"{_fmt_s(beat.get('start_s'))}–{_fmt_s(beat.get('end_s'))}s | {body}".strip())
    if lines:
        return "\n".join(lines)
    return str(action.get("prose") or "").strip()


def _coverage_row(requirement: str, disposition: str, path: str, implementation: str = "") -> dict[str, str]:
    row = {"requirement": requirement, "disposition": disposition, "path": path}
    if implementation:
        row["implementation"] = implementation
    return row


def _diagnostic(
    *,
    code: str,
    severity: str,
    path: str,
    message: str,
    proposal: dict[str, Any] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {"code": code, "severity": severity, "path": path, "message": message}
    if proposal:
        row["proposal"] = proposal
    return row


def _duration_s(clip: dict[str, Any]) -> int:
    generation = clip.get("generation") if isinstance(clip.get("generation"), dict) else {}
    try:
        value = int(round(float(generation.get("duration_s") or 10)))
    except (TypeError, ValueError):
        value = 10
    return max(1, min(15, value))


def _aspect(clip: dict[str, Any]) -> str:
    generation = clip.get("generation") if isinstance(clip.get("generation"), dict) else {}
    aspect = str(generation.get("aspect_ratio") or "").strip()
    return aspect or "9:16"


def _cap(text: str) -> str:
    return (text or "").strip()[:PROMPT_CHAR_CAP]


def _empty_package(
    *,
    clip: dict[str, Any],
    profile: dict[str, Any],
    status: str,
    diagnostics: list[dict[str, Any]],
    coverage: list[dict[str, str]],
) -> dict[str, Any]:
    return {
        "status": status,
        "compiler_version": COMPILER_VERSION,
        "profile_id": str(profile.get("profile_id") or ""),
        "generator_tag": str(profile.get("generator_tag") or ""),
        "live": bool(profile.get("live")),
        "mode": str((profile.get("identity") or {}).get("mode") or ""),
        "clip_id": str(clip.get("clip_id") or ""),
        "prompt": {"still": "", "motion": ""},
        "request": {},
        "bindings": [],
        "delivery_tasks": [],
        "diagnostics": diagnostics,
        "coverage": coverage,
        "proposal": {
            "live": False,
            "message": "Host has not activated this engine. Fail-closed. No pretend request.",
        },
    }


def _compile_grok(clip: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    shot = _first_shot(clip)
    subject = _first_subject(shot)
    scene = subject.get("scene_state") if isinstance(subject.get("scene_state"), dict) else {}
    lighting = shot.get("lighting") if isinstance(shot.get("lighting"), dict) else {}
    look = shot.get("look") if isinstance(shot.get("look"), dict) else {}
    camera = shot.get("camera") if isinstance(shot.get("camera"), dict) else {}
    creative = clip.get("creative") if isinstance(clip.get("creative"), dict) else {}
    audio = creative.get("audio") if isinstance(creative.get("audio"), dict) else {}
    casops = {}
    extensions = clip.get("extensions") if isinstance(clip.get("extensions"), dict) else {}
    if isinstance(extensions.get("casops"), dict):
        casops = extensions["casops"]

    identity = str(subject.get("identity") or casops.get("subject_prose") or "").strip()
    anchors = subject.get("anchors") if isinstance(subject.get("anchors"), dict) else {}
    hair = str(subject.get("hair") or anchors.get("hair") or casops.get("hair_prose") or "").strip()
    skin = str(subject.get("skin") or anchors.get("skin") or casops.get("skin_prose") or "").strip()
    makeup = str(scene.get("makeup") or casops.get("makeup_prose") or "").strip()
    light = str(lighting.get("key") or look.get("medium") or casops.get("light_prose") or "").strip()
    look_text = str(look.get("medium") or "").strip()
    if look_text and look_text != light:
        light = _join(light, look_text)
    frame = str(casops.get("frame_prose") or "").strip()
    camera_text = str(camera.get("movement") or camera.get("framing") or casops.get("camera_prose") or "").strip()
    audio_text = str(audio.get("prose") or casops.get("sound_prose") or "").strip()
    beats = _beats_text(shot) or str(casops.get("coverage_prose") or "").strip()
    forbid = _forbid_list(clip)
    hard = _constraint_bucket(clip, "hard")
    acceptance = _constraint_bucket(clip, "acceptance")
    hair_lines, hair_source = constraint_lines(clip)
    aspect = _aspect(clip)
    duration = _duration_s(clip)
    tag = str(profile.get("generator_tag") or "")
    mode = str((profile.get("identity") or {}).get("mode") or "")
    still_only = tag == "grok-image" or mode == "still"
    constraint_text = "\n".join(_unique_lines(hair_lines, hard, forbid, acceptance))
    dialect = dialect_prompts(clip, tag, constraints=constraint_text)
    still = _cap(dialect.get("still") or "")
    motion = "" if still_only else _cap(dialect.get("motion") or "")

    still_request = {
        "model": "grok-imagine-image-2.0",
        "prompt": still,
        "n": 1,
        "aspect_ratio": aspect,
        "resolution": "2k",
    }
    request: dict[str, Any] = {"still": still_request}
    if not still_only:
        request["video"] = {
            "model": "grok-imagine-video-1.5",
            "prompt": motion,
            "aspect_ratio": aspect,
            "duration": duration,
            "resolution": "1080p",
        }

    coverage = [
        _coverage_row("generation.duration_s", "not_applicable" if still_only else "exact", "generation.duration_s"),
        _coverage_row("generation.aspect_ratio", "exact", "generation.aspect_ratio"),
        _coverage_row("subjects.identity", "prompted", "creative.shots.subjects.identity"),
        _coverage_row("subjects.anchors", "prompted" if (hair or skin) else "not_applicable", "creative.shots.subjects.anchors"),
        _coverage_row("constraints.hard", "prompted" if hard else "not_applicable", "constraints.hard"),
        _coverage_row("lighting", "prompted", "creative.shots.lighting"),
        _coverage_row("look", "prompted", "creative.shots.look"),
        _coverage_row("action.beats", "not_applicable" if still_only else "prompted", "creative.shots.action.beats"),
        _coverage_row("camera", "not_applicable" if still_only else "prompted", "creative.shots.camera"),
        _coverage_row("audio", "not_applicable" if still_only else "prompted", "creative.audio"),
        _coverage_row("hair-off-lips", "prompted", hair_source, "compiled into still and motion"),
        _coverage_row(
            "starting_image",
            "not_applicable" if still_only else "post",
            "assets",
            "bound after Image 2.0 still" if not still_only else "still has no video binding",
        ),
    ]
    diagnostics: list[dict[str, Any]] = []
    if hair_source.endswith("+house"):
        diagnostics.append(
            _diagnostic(
                code="CONSTRAINT_HAIR_OFF_LIPS_HOUSE",
                severity="info",
                path="constraints.forbid",
                message="Hair-off-lips was not in constraints.forbid; compiled from the house constraint list.",
            )
        )
    bindings: list[dict[str, Any]] = []
    delivery_tasks: list[dict[str, Any]] = []
    if not still_only:
        bindings.append({"role": "starting_image", "status": "pending", "path": "request.video.image"})
        delivery_tasks.append({"task": "bind_starting_image", "disposition": "post"})

    return {
        "status": "ok",
        "compiler_version": COMPILER_VERSION,
        "profile_id": str(profile.get("profile_id") or ""),
        "generator_tag": tag,
        "live": True,
        "mode": mode or ("still" if still_only else "image_to_video"),
        "clip_id": str(clip.get("clip_id") or ""),
        "prompt": {"still": still, "motion": motion},
        "request": request,
        "bindings": bindings,
        "delivery_tasks": delivery_tasks,
        "diagnostics": diagnostics,
        "coverage": coverage,
        "proposal": None,
        "guide": GUIDE_BY_TAG.get(tag),
    }


def compile_clip(canonical: dict[str, Any], profile_id: str | None = None) -> dict[str, Any]:
    """Compile a v2 clip into a vendor package. Does not call a vendor. Does not read sample/."""
    clip = deepcopy(canonical) if isinstance(canonical, dict) else {}
    try:
        clip = validate_clip(clip)
    except ClipSchemaError:
        pass
    wanted = str(profile_id or (clip.get("target") or {}).get("profile_id") or "").strip()
    try:
        profile = load_profile(wanted) if wanted else None
    except ProfileError:
        profile = None
    if profile is None and wanted:
        profile = profile_for_tag(wanted)
    if profile is None:
        fake = {"profile_id": wanted, "generator_tag": wanted, "live": False, "identity": {"mode": "unknown"}}
        return _empty_package(
            clip=clip,
            profile=fake,
            status="blocked",
            diagnostics=[
                _diagnostic(
                    code="CAPABILITY_PROFILE_UNKNOWN",
                    severity="error",
                    path="target.profile_id",
                    message=f"No capability profile for {wanted or '(missing)'}.",
                    proposal={"live": False},
                )
            ],
            coverage=[_coverage_row("live emit", "unsupported", "target.profile_id")],
        )
    tag = str(profile.get("generator_tag") or "")
    if not profile.get("live") or tag not in GROK_LIVE_TAGS:
        hair_lines, _src = constraint_lines(clip)
        hard = _constraint_bucket(clip, "hard")
        forbid = _forbid_list(clip)
        acceptance = _constraint_bucket(clip, "acceptance")
        dialect = dialect_prompts(
            clip,
            tag,
            constraints="\n".join(_unique_lines(hair_lines, hard, forbid, acceptance)),
        )
        pkg = _empty_package(
            clip=clip,
            profile=profile,
            status="blocked",
            diagnostics=[
                _diagnostic(
                    code="CAPABILITY_PROFILE_NOT_LIVE",
                    severity="error",
                    path="target.profile_id",
                    message=(
                        f"{profile.get('profile_id')} ({tag}) is not a live compiler target. "
                        "Fail-closed. Dialect prompt is operator preview only. Do not emit a pretend request."
                    ),
                    proposal={"live": False, "activate": False},
                )
            ],
            coverage=[_coverage_row("live emit", "unsupported", "target.profile_id")],
        )
        pkg["prompt"] = {"still": dialect.get("still") or "", "motion": dialect.get("motion") or ""}
        pkg["guide"] = GUIDE_BY_TAG.get(tag)
        return pkg
    return _compile_grok(clip, profile)


def write_compiled_package(folder: Path, compiled: dict[str, Any]) -> Path:
    """Persist spec §8.7 package under output/compiled/<engine>/. Never sample/."""
    dest = Path(folder)
    if "sample" in dest.parts:
        raise ValueError("sample/ is read-only")
    dest.mkdir(parents=True, exist_ok=True)
    prompt = compiled.get("prompt") if isinstance(compiled.get("prompt"), dict) else {}
    prompt_text = _join(
        "## still",
        str(prompt.get("still") or ""),
        "",
        "## motion",
        str(prompt.get("motion") or ""),
    )
    (dest / "compiled.prompt.txt").write_text(prompt_text + "\n", encoding="utf-8")
    (dest / "compiled.request.json").write_text(
        json.dumps(compiled.get("request") or {}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (dest / "compiled.asset_bindings.json").write_text(
        json.dumps(compiled.get("bindings") or [], indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (dest / "compiled.delivery_tasks.json").write_text(
        json.dumps(compiled.get("delivery_tasks") or [], indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (dest / "compiled.diagnostics.json").write_text(
        json.dumps(
            {
                "status": compiled.get("status"),
                "diagnostics": compiled.get("diagnostics") or [],
                "coverage": compiled.get("coverage") or [],
                "proposal": compiled.get("proposal"),
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    (dest / "compiled.manifest.json").write_text(
        json.dumps(
            {
                "compiler_version": compiled.get("compiler_version") or COMPILER_VERSION,
                "profile_id": compiled.get("profile_id"),
                "generator_tag": compiled.get("generator_tag"),
                "status": compiled.get("status"),
                "clip_id": compiled.get("clip_id"),
                "live": compiled.get("live"),
                "mode": compiled.get("mode"),
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    return dest


def apply_runtime_config(compiled: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    """Overlay operator generate-time duration/aspect/resolution onto compiled request fields."""
    out = deepcopy(compiled)
    request = out.get("request") if isinstance(out.get("request"), dict) else {}
    still = request.get("still") if isinstance(request.get("still"), dict) else None
    video = request.get("video") if isinstance(request.get("video"), dict) else None
    if still:
        if config.get("aspect_ratio"):
            still["aspect_ratio"] = str(config["aspect_ratio"])
        if config.get("image_resolution"):
            still["resolution"] = str(config["image_resolution"])
        if config.get("image_model"):
            still["model"] = str(config["image_model"])
    if video:
        if config.get("aspect_ratio"):
            video["aspect_ratio"] = str(config["aspect_ratio"])
        if config.get("duration") not in (None, ""):
            try:
                video["duration"] = max(1, min(15, int(config["duration"])))
            except (TypeError, ValueError):
                pass
        if config.get("resolution"):
            video["resolution"] = str(config["resolution"])
        if config.get("video_model"):
            video["model"] = str(config["video_model"])
    out["request"] = request
    return out


def compiled_snapshot(compiled: dict[str, Any]) -> dict[str, Any]:
    """Dry-run payload: compile result without vendor bytes."""
    prompt = compiled.get("prompt") if isinstance(compiled.get("prompt"), dict) else {}
    return {
        "status": compiled.get("status"),
        "compiler_version": compiled.get("compiler_version"),
        "profile_id": compiled.get("profile_id"),
        "generator_tag": compiled.get("generator_tag"),
        "live": compiled.get("live"),
        "mode": compiled.get("mode"),
        "prompt": {"still": prompt.get("still") or "", "motion": prompt.get("motion") or ""},
        "request": compiled.get("request") or {},
        "coverage": compiled.get("coverage") or [],
        "diagnostics": compiled.get("diagnostics") or [],
        "proposal": compiled.get("proposal"),
        "guide": compiled.get("guide"),
    }
