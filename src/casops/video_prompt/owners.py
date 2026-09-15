"""Agent → canonical path ownership (spec §17.2). Used by P3 overlays; declared in P1."""

from __future__ import annotations

OWNER_PATHS: dict[str, tuple[str, ...]] = {
    "video.creativedirector": ("intent", "creative.continuity"),
    "video.promptengineer": ("generation", "classification", "creative.audio"),
    "video.continuity": ("creative.shots.subjects",),
    "video.mua_makeup": ("creative.shots.subjects.scene_state",),
    "video.cinematographer": ("creative.shots.lighting", "creative.shots.look"),
    "video.director": ("creative.shots.action",),
    "video.cameraoperator": ("creative.shots.camera",),
    "video.critic": ("constraints", "provenance.diagnostics"),
}

# T4 Chat heading → owner + canonical path (spec §17.2). Used by P5 section hops.
HEADING_OWNERS: dict[str, tuple[str, str]] = {
    "Creative direction": ("video.creativedirector", "intent"),
    "Frame": ("video.promptengineer", "generation"),
    "Subject": ("video.continuity", "creative.shots.subjects"),
    "Hair": ("video.continuity", "creative.shots.subjects.anchors"),
    "Skin": ("video.continuity", "creative.shots.subjects.anchors"),
    "Makeup": ("video.mua_makeup", "creative.shots.subjects.scene_state"),
    "Light": ("video.cinematographer", "creative.shots.lighting"),
    "Coverage / performance": ("video.director", "creative.shots.action"),
    "Camera lock": ("video.cameraoperator", "creative.shots.camera"),
    "Sound": ("video.promptengineer", "creative.audio"),
    "Sound, if the model supports native audio": ("video.promptengineer", "creative.audio"),
    "Negatives": ("video.critic", "constraints"),
}


def heading_owner(heading: str) -> tuple[str, str]:
    key = str(heading or "").strip()
    if key in HEADING_OWNERS:
        return HEADING_OWNERS[key]
    if key.startswith("Sound"):
        return ("video.promptengineer", "creative.audio")
    if " | " in key and key[:1].isdigit():
        return ("video.director", "creative.shots.action")
    return ("", "")
