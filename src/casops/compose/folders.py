"""Locate an agent folder by agent_id."""

from __future__ import annotations

import json
from pathlib import Path


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
        payload = json.loads(spec_path.read_text(encoding="utf-8"))
        if payload.get("agent_id") == agent_id:
            return child
    return None
