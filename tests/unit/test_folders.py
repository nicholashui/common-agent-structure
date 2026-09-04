"""Agent folder listing includes every spec folder; locate survives corrupt siblings."""

from __future__ import annotations

import json
from pathlib import Path

from casops.compose.folders import list_agent_summaries, locate_agent_folder, public_folder_ref


def _write_spec(folder: Path, agent_id: str, role: str = "", va_category: str | None = None) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    payload = {
        "agent_id": agent_id,
        "structure_id": "casops.common_agent.v3",
        "schema_version": "3.0",
        "role": role or agent_id,
    }
    if va_category is not None:
        payload["va_category"] = va_category
    (folder / "agent_spec.json").write_text(json.dumps(payload), encoding="utf-8")
    (folder / "memory").mkdir(exist_ok=True)
    (folder / "memory" / "policy.json").write_text(
        json.dumps({"mode": "none"}),
        encoding="utf-8",
    )


def test_list_agent_summaries_returns_every_spec(tmp_path: Path) -> None:
    for name, agent_id in (("alpha", "pack.alpha"), ("beta", "pack.beta")):
        _write_spec(tmp_path / name, agent_id, name)
    (tmp_path / "skip-me").mkdir()
    rows = list_agent_summaries(tmp_path)
    assert [row["agent_id"] for row in rows] == ["pack.alpha", "pack.beta"]
    assert rows[0]["memory_mode"] == "none"
    assert rows[0]["va_category"] == ""


def test_list_agent_summaries_includes_va_category(tmp_path: Path) -> None:
    _write_spec(tmp_path / "video.director", "video.director", va_category="1-ATL")
    _write_spec(tmp_path / "specials.planner-agent", "specials.planner-agent", va_category=None)
    rows = {row["agent_id"]: row for row in list_agent_summaries(tmp_path)}
    assert rows["video.director"]["va_category"] == "1-ATL"
    assert rows["specials.planner-agent"]["va_category"] == ""


def test_list_agent_summaries_keeps_every_folder_in_a_large_tree(tmp_path: Path) -> None:
    expected: set[str] = set()
    for index in range(60):
        agent_id = f"pack.n{index:04d}"
        _write_spec(tmp_path / agent_id, agent_id)
        expected.add(agent_id)
    listed = {row["agent_id"] for row in list_agent_summaries(tmp_path)}
    assert listed == expected


def test_list_includes_unreadable_spec_folder(tmp_path: Path) -> None:
    _write_spec(tmp_path / "good", "pack.good")
    bad = tmp_path / "broken.agent"
    bad.mkdir()
    (bad / "agent_spec.json").write_text("{", encoding="utf-8")
    listed = {row["agent_id"]: row for row in list_agent_summaries(tmp_path)}
    assert set(listed) == {"pack.good", "broken.agent"}
    assert listed["broken.agent"]["folder"] == "agents/broken.agent"
    assert listed["pack.good"]["folder"] == "agents/good"


def test_public_folder_ref_is_repo_relative(tmp_path: Path) -> None:
    root = tmp_path / "agents"
    folder = root / "video.director"
    folder.mkdir(parents=True)
    assert public_folder_ref(folder, root) == "agents/video.director"


def test_locate_ignores_corrupt_sibling(tmp_path: Path) -> None:
    _write_spec(tmp_path / "_template_v3", "casops.template.baseline_safe")
    broken = tmp_path / "broken.agent"
    broken.mkdir()
    (broken / "agent_spec.json").write_text("{", encoding="utf-8")
    found = locate_agent_folder(tmp_path, "casops.template.baseline_safe")
    assert found == tmp_path / "_template_v3"
    assert locate_agent_folder(tmp_path, "pack.good") is None
