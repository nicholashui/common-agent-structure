"""Host-owned skill/tool grants. Agent folders cannot self-grant (INV-01)."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

SCHEMA = "casops.host_permission.v1"


def register_path(*, agents_root: Path | None = None, folder: Path | None = None) -> Path | None:
    env = os.environ.get("CASOPS_PERMISSION_REGISTER")
    if env:
        return Path(env)
    if agents_root is not None:
        candidate = agents_root.parent / "permissions" / "register.json"
        return candidate if candidate.is_file() else candidate
    if folder is not None:
        parent = folder.parent
        if parent.name == "agents":
            candidate = parent.parent / "permissions" / "register.json"
            return candidate
    return None


def load_register(path: Path | None) -> dict[str, Any]:
    if path is None or not path.is_file():
        return {"schema_version": SCHEMA, "grants": {}}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"schema_version": SCHEMA, "grants": {}}
    if not isinstance(payload, dict):
        return {"schema_version": SCHEMA, "grants": {}}
    grants = payload.get("grants")
    if not isinstance(grants, dict):
        payload["grants"] = {}
    return payload


def _agent_grant(register: dict[str, Any], agent_id: str) -> dict[str, Any]:
    grants = register.get("grants") if isinstance(register.get("grants"), dict) else {}
    row = grants.get(agent_id)
    return row if isinstance(row, dict) else {}


def skill_granted(agent_id: str, skill_id: str, *, register: dict[str, Any] | None = None) -> bool:
    if not agent_id or not skill_id:
        return False
    row = _agent_grant(register or {}, agent_id)
    skills = row.get("skills") if isinstance(row.get("skills"), list) else []
    return skill_id in {str(item) for item in skills}


def granted_tools(agent_id: str, declared: list[str], *, register: dict[str, Any] | None = None) -> list[str]:
    row = _agent_grant(register or {}, agent_id)
    allowed = {str(item) for item in (row.get("tools") if isinstance(row.get("tools"), list) else [])}
    return [item for item in declared if item in allowed]


def agent_id_from_folder(folder: Path) -> str:
    spec_path = folder / "agent_spec.json"
    if spec_path.is_file():
        try:
            spec = json.loads(spec_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            spec = {}
        if isinstance(spec, dict) and spec.get("agent_id"):
            return str(spec["agent_id"])
    return folder.name
