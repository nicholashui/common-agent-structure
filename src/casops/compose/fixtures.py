"""Fixture monotonicity (FR-INH-301)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def _fixture_ids(folder: Path) -> set[str]:
    directory = folder / "evals" / "regression"
    if not directory.is_dir():
        return set()
    return {
        path.name
        for path in directory.iterdir()
        if path.is_file() and path.name != ".gitkeep"
    }


def _waivers(folder: Path) -> set[str]:
    path = folder / "inheritance" / "conflicts.json"
    if not path.is_file():
        return set()
    payload: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    waived: set[str] = set()
    for item in payload.get("waivers") or []:
        if item.get("signed") and item.get("fixture"):
            waived.add(str(item["fixture"]))
    return waived


def check_fixture_monotonicity(child: Path, parent_folders: list[Path]) -> None:
    child_ids = _fixture_ids(child)
    waived = _waivers(child)
    for parent in parent_folders:
        missing = _fixture_ids(parent) - child_ids - waived
        if missing:
            raise CasopsError(ErrorCode.INH_FIXTURE_REMOVAL)
