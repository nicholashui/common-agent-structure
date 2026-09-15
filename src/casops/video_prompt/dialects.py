"""ISSUE-0010: vendor prompt dialects from spec/*_operation_guide.md. Preview text only for fail-closed tags."""

from __future__ import annotations

import re
from typing import Any

GUIDE_BY_TAG: dict[str, str] = {
    "grok-imagine": "spec/grok_imagine_operation_guide.md",
    "grok-image": "spec/grok_imagine_operation_guide.md",
    "seedance": "spec/seedance_operation_guide.md",
    "ltx": "spec/ltx_operation_guide.md",
    "hailuo": "spec/minimax_h3_operation_guide.md",
    "gpt-image": "spec/gpt_image_operation_guide.md",
}

PARAM_LEAK_RE = re.compile(
    r"\b(\d+(?:\.\d+)?\s*-?\s*seconds?\b|9:16|16:9|1:1|4:3|3:2|1080p|720p|480p|4k|8k)\b",
    re.I,
)
WASTE_RE = re.compile(
    r"\b(8k|4k|ultra-detailed|masterpiece|best quality|award-winning|trending on artstation)\b",
    re.I,
)


def strip_param_leaks(text: str) -> str:
    cleaned = PARAM_LEAK_RE.sub("", text or "")
    cleaned = WASTE_RE.sub("", cleaned)
    cleaned = re.sub(r"[ \t]{2,}", " ", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip(" ,;.")


def _first_shot(clip: dict[str, Any]) -> dict[str, Any]:
    creative = clip.get("creative") if isinstance(clip.get("creative"), dict) else {}
    shots = creative.get("shots") if isinstance(creative.get("shots"), list) else []
    return shots[0] if shots and isinstance(shots[0], dict) else {}


def _first_subject(shot: dict[str, Any]) -> dict[str, Any]:
    subjects = shot.get("subjects") if isinstance(shot.get("subjects"), list) else []
    return subjects[0] if subjects and isinstance(subjects[0], dict) else {}


def clip_fields(clip: dict[str, Any]) -> dict[str, str]:
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
    anchors = subject.get("anchors") if isinstance(subject.get("anchors"), dict) else {}
    action = shot.get("action") if isinstance(shot.get("action"), dict) else {}
    beats = action.get("beats") if isinstance(action.get("beats"), list) else []
    beat_lines: list[str] = []
    for beat in beats:
        if not isinstance(beat, dict):
            continue
        body = str(beat.get("action") or "").strip()
        if beat.get("start_s") is None or beat.get("end_s") is None:
            if body:
                beat_lines.append(body)
            continue
        start = beat.get("start_s")
        end = beat.get("end_s")
        beat_lines.append(f"{start}–{end}s | {body}".strip())
    identity = str(subject.get("identity") or casops.get("subject_prose") or "").strip()
    return {
        "identity": identity,
        "identity_lead": identity.split(".")[0].strip() if identity else "",
        "hair": str(subject.get("hair") or anchors.get("hair") or casops.get("hair_prose") or "").strip(),
        "skin": str(subject.get("skin") or anchors.get("skin") or casops.get("skin_prose") or "").strip(),
        "makeup": str(scene.get("makeup") or casops.get("makeup_prose") or "").strip(),
        "light": str(lighting.get("key") or look.get("medium") or casops.get("light_prose") or "").strip(),
        "camera": str(camera.get("movement") or camera.get("framing") or casops.get("camera_prose") or "").strip(),
        "audio": str(audio.get("prose") or casops.get("sound_prose") or "").strip(),
        "beats": "\n".join(beat_lines) or str(action.get("prose") or casops.get("coverage_prose") or "").strip(),
        "frame": str(casops.get("frame_prose") or "").strip(),
    }


def dialect_prompts(clip: dict[str, Any], tag: str, *, constraints: str = "") -> dict[str, str]:
    fields = clip_fields(clip)
    ident = fields["identity"]
    lead = fields["identity_lead"] or ident[:120]
    hair = fields["hair"]
    skin = fields["skin"]
    makeup = fields["makeup"]
    light = fields["light"]
    camera = fields["camera"]
    audio = fields["audio"]
    beats = fields["beats"]
    tag = str(tag or "")
    if tag in {"grok-imagine", "grok-image"}:
        still = "\n".join(
            part
            for part in (
                ident,
                hair,
                makeup,
                skin,
                light,
                "Photoreal still. Locked adult identity. Do not animate.",
                constraints,
            )
            if part
        )
        motion = ""
        if tag == "grok-imagine":
            motion = "\n".join(
                part
                for part in (
                    "Hold the composition, subject identity, colors, and camera angle exactly. Motion and sound only. Do not re-describe the face.",
                    beats,
                    f"Camera: {camera} — only one move." if camera else "Camera: locked.",
                    f"Sound: {audio}" if audio else "",
                    constraints,
                    "Nothing else changes. No new people, no warping, no text overlay.",
                )
                if part
            )
        return {
            "still": strip_param_leaks(still),
            "motion": strip_param_leaks(motion) if tag == "grok-imagine" else "",
        }
    if tag == "seedance":
        still = f"{lead}. {light}".strip()
        motion = "\n".join(
            part
            for part in (
                f"[Subject] {lead}",
                f"[Action]\n{beats}" if beats else "",
                f"[Camera] {camera}" if camera else "[Camera] one locked move",
                f"[Sound] {audio}" if audio else "",
                f"[Keep] identity locked; hair off the lips",
                f"[Exclude] {constraints}" if constraints else "",
            )
            if part
        )
        return {"still": strip_param_leaks(still), "motion": strip_param_leaks(motion)}
    if tag == "ltx":
        still = f"{ident} {light}".strip()
        motion = (
            f"A present-tense shot: {lead}. {beats} {camera} {audio} {light}. "
            "Every sentence implies motion or time. Duration and resolution stay in settings."
        )
        return {"still": strip_param_leaks(still), "motion": strip_param_leaks(motion)}
    if tag == "hailuo":
        still = ident
        motion = "\n".join(
            [
                f"integrated_multimodal_description: [Shot 1] {beats or lead}",
                f"overall_soundscape: {audio or 'room tone'}",
                "non_diegetic_music: none",
            ]
        )
        return {"still": strip_param_leaks(still), "motion": strip_param_leaks(motion)}
    if tag == "gpt-image":
        still = "\n".join(
            part
            for part in (
                "Finished asset: photoreal still, locked adult identity.",
                ident,
                hair,
                makeup,
                skin,
                light,
                constraints,
            )
            if part
        )
        return {"still": strip_param_leaks(still), "motion": ""}
    still = ident
    motion = beats
    return {"still": strip_param_leaks(still), "motion": strip_param_leaks(motion)}
