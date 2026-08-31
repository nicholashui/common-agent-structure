"""MRO rules from spec §6.1."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from casops.compose.mro import resolve_mro
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def _agent(root: Path, agent_id: str, parents: list[dict[str, object]]) -> Path:
    folder = root / agent_id
    folder.mkdir(parents=True)
    (folder / "SPEC.md").write_text("spec\n", encoding="utf-8")
    (folder / "agent_spec.json").write_text(
        json.dumps({"schema_version": "3.0", "structure_id": "casops.common_agent.v3", "agent_id": agent_id}),
        encoding="utf-8",
    )
    inh = folder / "inheritance"
    inh.mkdir()
    (inh / "parents.json").write_text(json.dumps({"parents": parents}), encoding="utf-8")
    return folder


def test_child_is_first_and_parents_sort_by_priority_then_id(tmp_path: Path) -> None:
    _agent(tmp_path, "child", [{"agent_id": "p_b", "priority": 1}, {"agent_id": "p_a", "priority": 1}])
    _agent(tmp_path, "p_a", [])
    _agent(tmp_path, "p_b", [])
    order = resolve_mro(tmp_path / "child", tmp_path)
    assert order[0] == "child"
    assert order[1:] == ["p_a", "p_b"]


def test_diamond_collapses(tmp_path: Path) -> None:
    _agent(tmp_path, "child", [{"agent_id": "a", "priority": 0}, {"agent_id": "b", "priority": 1}])
    _agent(tmp_path, "a", [{"agent_id": "shared", "priority": 0}])
    _agent(tmp_path, "b", [{"agent_id": "shared", "priority": 0}])
    _agent(tmp_path, "shared", [])
    order = resolve_mro(tmp_path / "child", tmp_path)
    assert order.count("shared") == 1
    assert order[0] == "child"


def test_cycle_fails_closed(tmp_path: Path) -> None:
    _agent(tmp_path, "a", [{"agent_id": "b", "priority": 0}])
    _agent(tmp_path, "b", [{"agent_id": "a", "priority": 0}])
    with pytest.raises(CasopsError) as raised:
        resolve_mro(tmp_path / "a", tmp_path)
    assert raised.value.code == ErrorCode.INH_CYCLE


def test_parent_limit_fails_closed(tmp_path: Path) -> None:
    parents = [{"agent_id": f"p{i}", "priority": i} for i in range(9)]
    _agent(tmp_path, "child", parents)
    for i in range(9):
        _agent(tmp_path, f"p{i}", [])
    with pytest.raises(CasopsError) as raised:
        resolve_mro(tmp_path / "child", tmp_path)
    assert raised.value.code == ErrorCode.INH_PARENT_LIMIT


def test_depth_limit_fails_closed(tmp_path: Path) -> None:
    _agent(tmp_path, "child", [{"agent_id": "a1", "priority": 0}])
    _agent(tmp_path, "a1", [{"agent_id": "a2", "priority": 0}])
    _agent(tmp_path, "a2", [{"agent_id": "a3", "priority": 0}])
    _agent(tmp_path, "a3", [{"agent_id": "a4", "priority": 0}])
    _agent(tmp_path, "a4", [])
    with pytest.raises(CasopsError) as raised:
        resolve_mro(tmp_path / "child", tmp_path)
    assert raised.value.code == ErrorCode.INH_DEPTH


def test_self_parent_fails_closed(tmp_path: Path) -> None:
    _agent(tmp_path, "loop", [{"agent_id": "loop", "priority": 0}])
    with pytest.raises(CasopsError) as raised:
        resolve_mro(tmp_path / "loop", tmp_path)
    assert raised.value.code == ErrorCode.INH_SELF_PARENT


def test_missing_parent_fails_closed(tmp_path: Path) -> None:
    _agent(tmp_path, "child", [{"agent_id": "ghost", "priority": 0}])
    with pytest.raises(CasopsError) as raised:
        resolve_mro(tmp_path / "child", tmp_path)
    assert raised.value.code == ErrorCode.INH_PARENT_MISSING


def test_unknown_inherited_surface_fails_closed(tmp_path: Path) -> None:
    _agent(
        tmp_path,
        "child",
        [{"agent_id": "base", "priority": 0, "surfaces": ["credentials"]}],
    )
    _agent(tmp_path, "base", [])
    with pytest.raises(CasopsError) as raised:
        resolve_mro(tmp_path / "child", tmp_path)
    assert raised.value.code == ErrorCode.INH_SURFACE_UNKNOWN
