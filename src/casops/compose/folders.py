"""Locate an agent folder by agent_id."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def public_folder_ref(folder: Path, agents_root: Path) -> str:
    """Repo-relative pack location for the public plane, e.g. agents/video.director."""
    try:
        inner = folder.resolve().relative_to(agents_root.resolve()).as_posix()
    except ValueError:
        inner = folder.name
    inner = inner.replace("\\", "/").strip("/")
    if inner.startswith("agents/"):
        return inner
    return f"agents/{inner}" if inner else "agents"


def list_agent_summaries(agents_root: Path) -> list[dict[str, Any]]:
    """Return public-plane summaries for every loadable agent folder."""
    summaries: list[dict[str, Any]] = []
    if not agents_root.is_dir():
        return summaries
    for child in sorted(agents_root.iterdir(), key=lambda path: path.name.lower()):
        if not child.is_dir():
            continue
        spec_path = child / "agent_spec.json"
        if not spec_path.is_file():
            continue
        payload = _read_spec(spec_path)
        summaries.append(
            {
                "agent_id": str(payload.get("agent_id") or child.name),
                "folder": public_folder_ref(child, agents_root),
                "structure_id": str(payload.get("structure_id") or "casops.common_agent.v3"),
                "schema_version": str(payload.get("schema_version") or "3.0"),
                "role": str(payload.get("role") or ""),
                "memory_mode": _memory_mode(child),
                "va_category": _optional_str(payload.get("va_category")),
            }
        )
    return summaries


def _optional_str(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    if text.lower() in {"none", "null"}:
        return ""
    return text


def _read_spec(spec_path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(spec_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(payload, dict):
        return {}
    return payload


def _memory_mode(folder: Path) -> str:
    path = folder / "memory" / "policy.json"
    if not path.is_file():
        return ""
    try:
        policy = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ""
    if not isinstance(policy, dict):
        return ""
    return str(policy.get("mode") or "")


def locate_agent_folder(agents_root: Path, agent_id: str) -> Path | None:
    direct = agents_root / agent_id
    if (direct / "agent_spec.json").is_file():
        return direct
    if not agents_root.is_dir():
        return None
    for child in agents_root.iterdir():
        spec_path = child / "agent_spec.json"
        if not spec_path.is_file():
            continue
        payload = _read_spec(spec_path)
        if payload.get("agent_id") == agent_id:
            return child
    return None
