"""Grok projection is one-way, empty tools/skills, auto_update false."""

from __future__ import annotations

import json
import tomllib
from pathlib import Path

from casops.acp.project import (
    AMBIENT_MCP,
    grok_home_config_text,
    prepare_grok_home,
    project_agent,
    sanitize_grok_env,
    write_binding,
)
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
    assert "enabled = []" in config
    assert "mcp-search" in config
    grok_home_cfg = Path(result["home"]) / "grok-home" / "config.toml"
    assert grok_home_cfg.is_file()
    home_text = grok_home_cfg.read_text(encoding="utf-8")
    assert "official_marketplace_auto_installed = false" in home_text
    assert "mcp-search" in home_text
    lock = json.loads(Path(result["lock"]).read_text(encoding="utf-8"))
    assert lock["auto_update"] is False
    assert lock["files"]["profile.md"]


def test_sanitize_grok_env_drops_plugin_roots() -> None:
    cleaned = sanitize_grok_env(
        {"PATH": "/bin", "CLAUDE_PLUGIN_ROOT": "C:/leak", "PLUGIN_ROOT": "C:/leak", "GROK_HOME": "keep"}
    )
    assert "CLAUDE_PLUGIN_ROOT" not in cleaned
    assert "PLUGIN_ROOT" not in cleaned
    assert cleaned["GROK_HOME"] == "keep"
    assert cleaned["PATH"] == "/bin"


def test_prepare_grok_home_rewrites_config(tmp_path: Path) -> None:
    grok_home = tmp_path / "grok-home"
    grok_home.mkdir()
    (grok_home / "config.toml").write_text("[marketplace]\nofficial_marketplace_auto_installed = true\n", encoding="utf-8")
    path = prepare_grok_home(grok_home)
    text = path.read_text(encoding="utf-8")
    assert "official_marketplace_auto_installed = false" in text
    assert "enabled = []" in text
    parsed = tomllib.loads(text)
    assert parsed.get("disabled_mcp_servers") == list(AMBIENT_MCP)
    assert "mcp-search" in parsed["disabled_mcp_servers"]
    skills = parsed.get("skills") if isinstance(parsed.get("skills"), dict) else {}
    plugins = parsed.get("plugins") if isinstance(parsed.get("plugins"), dict) else {}
    assert "disabled_mcp_servers" not in skills
    assert "disabled_mcp_servers" not in plugins


def test_grok_home_config_disabled_mcp_is_root_key() -> None:
    parsed = tomllib.loads(grok_home_config_text())
    assert parsed.get("disabled_mcp_servers") == list(AMBIENT_MCP)
    skills = parsed.get("skills") if isinstance(parsed.get("skills"), dict) else {}
    assert "disabled_mcp_servers" not in skills


def test_projected_config_toml_disabled_mcp_is_root_key(tmp_path: Path) -> None:
    folder = REPO / "agents" / "video.director"
    result = project_agent(folder, home_root=tmp_path, compose_hash="test")
    overlay = tomllib.loads(Path(result["config"]).read_text(encoding="utf-8"))
    home = tomllib.loads((Path(result["home"]) / "grok-home" / "config.toml").read_text(encoding="utf-8"))
    assert overlay.get("disabled_mcp_servers") == list(AMBIENT_MCP)
    assert home.get("disabled_mcp_servers") == list(AMBIENT_MCP)
    overlay_plugins = overlay.get("plugins") if isinstance(overlay.get("plugins"), dict) else {}
    assert "disabled_mcp_servers" not in overlay_plugins


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
