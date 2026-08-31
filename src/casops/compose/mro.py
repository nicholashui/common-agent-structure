"""MRO resolver (spec §6.1)."""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path

from casops.compose.folders import locate_agent_folder
from casops.compose.surfaces import LEGAL_INHERITED_SURFACES
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

LocateFn = Callable[[str], Path | None]


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _parents(folder: Path) -> list[dict]:
    payload = _load_json(folder / "inheritance" / "parents.json")
    parents = list(payload.get("parents") or [])
    if len(parents) > 8:
        raise CasopsError(ErrorCode.INH_PARENT_LIMIT)
    for parent in parents:
        for surface in parent.get("surfaces") or []:
            if surface not in LEGAL_INHERITED_SURFACES:
                raise CasopsError(ErrorCode.INH_SURFACE_UNKNOWN)
    return sorted(
        parents,
        key=lambda item: (int(item.get("priority", 0)), str(item.get("agent_id", ""))),
    )


def resolve_mro(
    child_dir: Path,
    agents_root: Path,
    *,
    locate: LocateFn | None = None,
) -> list[str]:
    def default_locate(agent_id: str) -> Path | None:
        return locate_agent_folder(agents_root, agent_id)

    find = locate or default_locate
    order: list[str] = []
    seen: set[str] = set()
    visiting: set[str] = set()

    def walk(folder: Path, depth: int) -> None:
        spec_path = folder / "agent_spec.json"
        spec_md = folder / "SPEC.md"
        if not spec_path.is_file() or not spec_md.is_file():
            raise CasopsError(ErrorCode.INH_PARENT_MISSING)
        spec = _load_json(spec_path)
        agent_id = spec["agent_id"]
        structure = spec.get("structure_id")
        if structure not in {None, "casops.common_agent.v3"}:
            raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH)
        if depth > 3:
            raise CasopsError(ErrorCode.INH_DEPTH)
        if agent_id in visiting:
            raise CasopsError(ErrorCode.INH_CYCLE)
        if agent_id in seen:
            return
        visiting.add(agent_id)
        order.append(agent_id)
        seen.add(agent_id)
        for parent in _parents(folder):
            parent_id = str(parent["agent_id"])
            if parent_id == agent_id:
                raise CasopsError(ErrorCode.INH_SELF_PARENT)
            parent_dir = find(parent_id)
            if parent_dir is None or not parent_dir.is_dir():
                raise CasopsError(ErrorCode.INH_PARENT_MISSING)
            walk(parent_dir, depth + 1)
        visiting.remove(agent_id)

    walk(child_dir, 0)
    return order
