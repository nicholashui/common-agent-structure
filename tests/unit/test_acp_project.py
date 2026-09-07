"""Grok projection is one-way, empty tools/skills, auto_update false."""

from __future__ import annotations

import json
from pathlib import Path

from casops.acp.project import project_agent, write_binding
from casops.compose.folders import list_agent_ids, locate_agent_folder

REPO = Path(__file__).resolve().parents[2]


def test_project_director_profile_pins_identity_and_empty_tools(tmp_path: Path) -> None:
    folder = REPO / "agents" / "video.director"
    result = project_agent(folder, home_root=tmp_path, compose_hash="test")
    assert result["agent_id"] == "video.director"
    assert result["tools"] == []
    profile = Path(result["profile"]).read_text(encoding="utf-8")
    assert "name: video.director" in profile
    assert "tools: []" in profile
    assert "skills: []" in profile
    assert "DO NOT EDIT" in profile
    assert "INV-05" in profile
    assert "Sora 2 API" not in profile
    config = Path(result["config"]).read_text(encoding="utf-8")
    assert "auto_update = false" in config
    lock = json.loads(Path(result["lock"]).read_text(encoding="utf-8"))
    assert lock["auto_update"] is False
    assert lock["files"]["profile.md"]


def test_write_binding_sets_agent_id(tmp_path: Path) -> None:
    folder = tmp_path / "demo.agent"
    (folder / "protocols").mkdir(parents=True)
    path = write_binding(folder, "demo.agent")
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["agent_id"] == "demo.agent"
    assert payload["protocol"]["requested_version"] == 1
    assert (folder / "safety" / "egress.json").is_file()


def test_project_all_scanned_agents_empty_tools(tmp_path: Path) -> None:
    agents_root = REPO / "agents"
    ids = list_agent_ids(agents_root)
    scanned = [path.name for path in sorted(agents_root.iterdir()) if (path / "agent_spec.json").is_file()]
    assert ids
    assert len(ids) == len(scanned)
    for agent_id in ids:
        folder = locate_agent_folder(agents_root, agent_id)
        assert folder is not None
        result = project_agent(folder, home_root=tmp_path)
        assert result["tools"] == []
        profile = Path(result["profile"]).read_text(encoding="utf-8")
        assert "tools: []" in profile
        assert "skills: []" in profile
        assert "DO NOT EDIT" in profile
        config = Path(result["config"]).read_text(encoding="utf-8")
        assert "auto_update = false" in config
