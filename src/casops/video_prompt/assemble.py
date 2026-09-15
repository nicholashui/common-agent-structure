"""ISSUE-0009 P2: host-join crafts into a v2 clip object and T4 projection."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from casops.project_instruction import split_continuity_craft
from casops.video_prompt.owners import OWNER_PATHS
from casops.video_prompt.schema import CLIP_SCHEMA_ID, CLIP_SPEC_VERSION, ClipObject, validate_clip

DEFAULT_PROFILE_ID = "xai.grok-imagine-video-1.5.i2v"
PROJECTION_INTRO = (
    "Generate from the locked decisions below. Host-assembled from Chat selections and ASK_HUMAN locks. "
    "sample/ is not a source."
)
SOUND_HEADING = "Sound, if the model supports native audio"
DURATION_RE = re.compile(r"(\d+(?:\.\d+)?)\s*-?\s*seconds?\b", re.I)
DURATION_S_RE = re.compile(r"\b(\d+)\s*s\b", re.I)
ASPECT_RE = re.compile(r"\b(9:16|16:9|1:1|4:3|3:2)\b")
BEAT_RE = re.compile(r"^(\d+(?:\.\d+)?)\s*[–-]\s*(\d+(?:\.\d+)?)\s*s\s*\|\s*(.*)$")


def split_pe_craft(pe_craft: str) -> tuple[str, str]:
    frame, _, sound = (pe_craft or "").partition("\n")
    if not sound.strip():
        return (pe_craft or "").strip(), (pe_craft or "").strip()
    return frame.strip(), sound.strip()


def parse_duration_s(frame: str, fallback: float = 15) -> float:
    match = DURATION_RE.search(frame or "")
    if match:
        return float(match.group(1))
    match = DURATION_S_RE.search(frame or "")
    if match:
        return float(match.group(1))
    return fallback


def parse_aspect_ratio(frame: str) -> str | None:
    match = ASPECT_RE.search(frame or "")
    return match.group(1) if match else None


def parse_beats(text: str, duration_s: float) -> list[dict[str, Any]]:
    beats: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for raw in (text or "").splitlines():
        line = raw.strip()
        match = BEAT_RE.match(line)
        if match:
            if current:
                beats.append(current)
            current = {
                "start_s": float(match.group(1)),
                "end_s": float(match.group(2)),
                "action": match.group(3).strip(),
            }
            continue
        if current and line:
            current["action"] = f"{current['action']} {line}".strip()
    if current:
        beats.append(current)
    if not beats:
        return [{"start_s": 0, "end_s": duration_s, "action": (text or "").strip()}]
    return beats


def parse_forbid(text: str) -> list[str]:
    parts = [item.strip(" .") for item in re.split(r",|\n", text or "") if item.strip()]
    return parts


def parse_constraints(text: str) -> dict[str, list[str]]:
    """Split critic prose into v2 buckets. Forbid stays the Negatives list; hard/acceptance are derived."""
    forbid = parse_forbid(text)
    hard: list[str] = []
    acceptance: list[str] = []
    for item in forbid:
        low = item.lower()
        if low.startswith("must ") or low.startswith("keep "):
            acceptance.append(item)
        elif any(token in low for token in ("hair", "identity", "morph", "mouth", "lip")):
            hard.append(item)
    return {"forbid": forbid, "hard": hard, "soft": [], "acceptance": acceptance}


PROJECTION_HEADINGS = {
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
}


def parse_projection_sections(text: str) -> dict[str, str]:
    """Split a T4 labeled projection into heading → body. Not a generation source."""
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
            if key in PROJECTION_HEADINGS or (" | " in key and key[:1].isdigit()):
                flush()
                current = "Sound" if key.startswith("Sound") else key
                continue
        buf.append(line)
    flush()
    return found


def clip_from_projection(project_id: str, text: str, *, profile_id: str = DEFAULT_PROFILE_ID) -> ClipObject:
    """Bridge T4 operator text into a clip when canonical.yaml is missing. Host compile still owns vendor dialect."""
    parts = parse_projection_sections(text)
    beats = parts.get("Coverage / performance") or "\n".join(
        parts.get(key, "") for key in list(parts) if key[:1].isdigit()
    )
    thesis = parts.get("Creative direction") or ""
    why = ""
    for line in thesis.splitlines():
        if line.strip().upper().startswith("WHY:"):
            why = line.strip()
            break
    return assemble_clip(
        project_id=project_id,
        thesis=thesis,
        why=why,
        frame=parts.get("Frame") or "",
        sound=parts.get("Sound") or "",
        subject=parts.get("Subject") or "",
        hair=parts.get("Hair") or "",
        skin=parts.get("Skin") or "",
        makeup=parts.get("Makeup") or "",
        light=parts.get("Light") or "",
        beats=beats,
        camera=parts.get("Camera lock") or "",
        negatives=parts.get("Negatives") or "",
        profile_id=profile_id,
    )


def assemble_clip(
    *,
    project_id: str,
    thesis: str,
    why: str,
    frame: str,
    sound: str,
    subject: str,
    hair: str,
    skin: str,
    makeup: str,
    light: str,
    beats: str,
    camera: str,
    negatives: str,
    profile_id: str = DEFAULT_PROFILE_ID,
    mode: str = "image_to_video",
) -> ClipObject:
    duration_s = parse_duration_s(frame)
    aspect = parse_aspect_ratio(frame)
    generation: dict[str, Any] = {"duration_s": duration_s}
    if aspect:
        generation["aspect_ratio"] = aspect
    beat_rows = parse_beats(beats, duration_s)
    clip: ClipObject = {
        "schema": CLIP_SCHEMA_ID,
        "spec_version": CLIP_SPEC_VERSION,
        "kind": "clip",
        "clip_id": f"CLIP.{project_id}.001",
        "revision": 1,
        "classification": {
            "prompt_form": "labeled_blocks",
            "input_mode": mode,
            "clip_structure": "single_shot",
            "legacy_tags": ["T4", "T7", "T15"],
        },
        "target": {"profile_id": profile_id, "mode": mode, "profile_revision": 1},
        "generation": generation,
        "delivery": {
            "in_s": 0,
            "out_s": duration_s,
            "timeline_duration_s": duration_s,
            "aspect_ratio": aspect or "",
            "audio_policy": "retain_if_approved",
        },
        "intent": {
            "logline": thesis.strip().rstrip("."),
            "emotion": why.strip(),
        },
        "assets": [],
        "creative": {
            "continuity": {"thesis": thesis.strip()},
            "shots": [
                {
                    "shot_id": f"CLIP.{project_id}.001.A",
                    "start_s": 0,
                    "end_s": duration_s,
                    "subjects": [
                        {
                            "subject_id": "CHAR.LEAD",
                            "identity": subject,
                            "hair": hair,
                            "skin": skin,
                            "anchors": {"hair": hair, "skin": skin},
                            "scene_state": {"makeup": makeup},
                        }
                    ],
                    "lighting": {"key": light},
                    "look": {"medium": light},
                    "camera": {"movement": camera, "framing": camera},
                    "action": {
                        "beats": beat_rows,
                        "prose": beats,
                    },
                }
            ],
            "audio": {"production": "native", "prose": sound},
        },
        "constraints": {**parse_constraints(negatives), "prose": negatives},
        "provenance": {
            "source_brief_id": f"BRIEF.{project_id}",
            "honesty": "CHARACTERIZATION",
        },
        "extensions": {
            "casops": {
                "project_id": project_id,
                "owner_map": {key: list(paths) for key, paths in OWNER_PATHS.items()},
                "thesis": thesis,
                "why": why,
                "frame_prose": frame,
                "sound_prose": sound,
                "subject_prose": subject,
                "hair_prose": hair,
                "skin_prose": skin,
                "makeup_prose": makeup,
                "light_prose": light,
                "coverage_prose": beats,
                "camera_prose": camera,
                "negatives_prose": negatives,
            }
        },
    }
    return validate_clip(clip)


def project_clip(clip: dict[str, Any]) -> str:
    casops = {}
    extensions = clip.get("extensions") if isinstance(clip.get("extensions"), dict) else {}
    if isinstance(extensions.get("casops"), dict):
        casops = extensions["casops"]
    thesis = str(casops.get("thesis") or (clip.get("intent") or {}).get("logline") or "").strip()
    why = str(casops.get("why") or (clip.get("intent") or {}).get("emotion") or "").strip()
    frame = str(casops.get("frame_prose") or "")
    sound = str(casops.get("sound_prose") or frame)
    subject = str(casops.get("subject_prose") or "")
    hair = str(casops.get("hair_prose") or "")
    skin = str(casops.get("skin_prose") or "")
    makeup = str(casops.get("makeup_prose") or "")
    light = str(casops.get("light_prose") or "")
    beats = str(casops.get("coverage_prose") or "")
    camera = str(casops.get("camera_prose") or "")
    negatives = str(casops.get("negatives_prose") or "")
    why_line = why if why.startswith("WHY:") else f"WHY: {why}"
    return "\n".join(
        [
            PROJECTION_INTRO,
            "",
            "Creative direction",
            thesis if thesis.endswith(".") else thesis + ".",
            why_line,
            "",
            "Frame",
            frame,
            "",
            "Subject",
            subject,
            "",
            "Hair",
            hair,
            "",
            "Makeup",
            makeup,
            "",
            "Skin",
            skin,
            "",
            "Light",
            light,
            "",
            "Coverage / performance",
            beats,
            "",
            "Camera lock",
            camera,
            "",
            SOUND_HEADING,
            sound or frame,
            "",
            "Negatives",
            negatives,
            "",
        ]
    )


def dump_canonical(clip: dict[str, Any]) -> str:
    return json.dumps(clip, indent=2, ensure_ascii=False) + "\n"


def write_clip_files(output_dir: Path, slug: str, clip: dict[str, Any]) -> str:
    folder = Path(output_dir)
    folder.mkdir(parents=True, exist_ok=True)
    text = project_clip(clip)
    prompt = folder / f"{slug}-prompt.txt"
    prompt.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
    (folder / f"{slug}-canonical.yaml").write_text(dump_canonical(clip), encoding="utf-8")
    from casops.video_prompt.compile import GROK_I2V_PROFILE, compile_clip, write_compiled_package
    from casops.video_prompt.sequence import sequence_from_clip, write_sequence_file

    clip_id = str(clip.get("clip_id") or f"CLIP.{slug}.001")
    clips_dir = folder / "clips"
    clips_dir.mkdir(parents=True, exist_ok=True)
    clip_rel = f"clips/{clip_id}-canonical.yaml"
    (clips_dir / f"{clip_id}-canonical.yaml").write_text(dump_canonical(clip), encoding="utf-8")
    compiled = compile_clip(clip, GROK_I2V_PROFILE)
    write_sequence_file(folder, slug, sequence_from_clip(clip, slug=slug, path=clip_rel))
    write_compiled_package(folder / "compiled" / "grok-imagine", compiled)
    write_compiled_package(folder / "compiled" / "grok-imagine" / clip_id, compiled)
    return text


def clip_from_walkthrough(
    mod: Any,
    locks: dict[str, str] | None = None,
    cycle_locks: dict[str, str] | None = None,
) -> ClipObject:
    picked = {dec["agent_id"]: mod._chosen_option(dec) for dec in mod.DECISIONS}
    thesis = str(picked["video.creativedirector"]["label"])
    pe_craft = mod._chosen_craft("video.promptengineer", locks)
    frame, sound = split_pe_craft(pe_craft)
    cont = split_continuity_craft(mod._chosen_craft("video.continuity", locks))
    makeup = mod._chosen_craft("video.mua_makeup", locks)
    light = mod._chosen_craft("video.cinematographer", locks)
    beats = mod._chosen_craft("video.director", locks)
    motor = mod._chosen_craft("video.cameraoperator", locks)
    negatives = mod._chosen_craft("video.critic", locks)
    extra_neg = mod._cycle_craft("video.critic", cycle_locks)
    extra_cont = mod._cycle_craft("video.continuity", cycle_locks)
    if extra_neg:
        negatives = "\n".join(part for part in (negatives, extra_neg) if part)
    if extra_cont:
        cont["Subject"] = "\n".join(part for part in (cont["Subject"], extra_cont) if part)
    why = str(getattr(mod, "ASSEMBLE_WHY", "") or "").strip()
    if not why:
        why = "Auto Pilot — intent-analysis read a person, not a product."
    return assemble_clip(
        project_id=str(mod.SLUG),
        thesis=thesis,
        why=why,
        frame=frame,
        sound=sound,
        subject=cont["Subject"],
        hair=cont["Hair"],
        skin=cont["Skin"],
        makeup=makeup,
        light=light,
        beats=beats,
        camera=motor,
        negatives=negatives,
    )
