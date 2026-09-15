"""Capability profiles for Video Generator tags. P1: load only; no live emit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.video_prompt.schema import repo_root

PROFILES_DIRNAME = "video_profiles"


class ProfileError(ValueError):
    """Capability profile missing or malformed."""


def profiles_dir() -> Path:
    return repo_root() / "spec" / PROFILES_DIRNAME


def _read_profile(path: Path) -> dict[str, Any]:
    """Profiles are JSON documents with a .yaml suffix (JSON is a YAML 1.2 subset)."""
    raw = path.read_text(encoding="utf-8")
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise ProfileError(f"{path.name}: profile must be an object")
    profile_id = str(payload.get("profile_id") or path.stem)
    payload["profile_id"] = profile_id
    identity = payload.get("identity")
    if not isinstance(identity, dict) or not identity.get("mode"):
        raise ProfileError(f"{path.name}: identity.mode is required")
    if "live" not in payload:
        payload["live"] = False
    if "generator_tag" not in payload:
        raise ProfileError(f"{path.name}: generator_tag is required")
    evidence = payload.get("evidence") if isinstance(payload.get("evidence"), dict) else {}
    payload["evidence"] = evidence
    return payload


def load_profiles() -> list[dict[str, Any]]:
    folder = profiles_dir()
    if not folder.is_dir():
        return []
    rows = [_read_profile(path) for path in sorted(folder.glob("*.yaml"))]
    return rows


def load_profile(profile_id: str) -> dict[str, Any]:
    wanted = str(profile_id or "").strip()
    for row in load_profiles():
        if row.get("profile_id") == wanted:
            return row
    raise ProfileError(f"unknown profile {wanted}")


def profile_for_tag(generator_tag: str) -> dict[str, Any] | None:
    tag = str(generator_tag or "").strip()
    matches = [row for row in load_profiles() if row.get("generator_tag") == tag]
    if not matches:
        return None
    live = [row for row in matches if row.get("live") is True]
    return (live or matches)[0]
