"""Read-only swarm folder listing. Not a v4 outer runner."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

SWARM_ID_RE = __import__("re").compile(r"^[a-z][a-z0-9._-]{0,62}$")


def _root(agents_root: Path) -> Path:
    return Path(agents_root).resolve().parent / "swarms"


def _load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def list_swarms(agents_root: Path) -> dict[str, Any]:
    root = _root(agents_root)
    rows: list[dict[str, Any]] = []
    if root.is_dir():
        for folder in sorted(root.iterdir()):
            if not folder.is_dir():
                continue
            spec = _load_json(folder / "swarm_spec.json")
            roster = _load_json(folder / "roster.json")
            members = roster.get("members") if isinstance(roster.get("members"), list) else []
            rows.append(
                {
                    "swarm_id": spec.get("swarm_id") or folder.name,
                    "status": spec.get("status") or "draft",
                    "pattern": spec.get("pattern") or "",
                    "member_count": len(members),
                    "honesty": "CHARACTERIZATION",
                    "runner": False,
                }
            )
    return {"swarms": rows, "honesty": "CHARACTERIZATION", "note": "Roster listing only. Not a swarm runner."}


def read_swarm(agents_root: Path, swarm_id: str) -> dict[str, Any]:
    if not SWARM_ID_RE.match(swarm_id or ""):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="invalid swarm id")
    folder = _root(agents_root) / swarm_id
    spec = _load_json(folder / "swarm_spec.json")
    if not spec:
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="unknown swarm")
    roster = _load_json(folder / "roster.json")
    graph = _load_json(folder / "graph.json")
    members = roster.get("members") if isinstance(roster.get("members"), list) else []
    member_ids = [str(row.get("agent_id") or "") for row in members if isinstance(row, dict) and row.get("agent_id")]
    return {
        "honesty": "CHARACTERIZATION",
        "runner": False,
        "spec": spec,
        "roster": roster,
        "graph": graph,
        "member_ids": member_ids,
        "note": "Read-only roster for UI ?swarm= filter. POST runtime/run is not implemented.",
    }


def compose_preview(agents_root: Path, swarm_id: str) -> dict[str, Any]:
    payload = read_swarm(agents_root, swarm_id)
    payload["wrote_locks"] = False
    payload["note"] = "compose-preview only. wrote_locks is false. Members were not invoked."
    return payload
