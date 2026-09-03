"""Fleet UI source uses the list payload; no per-agent fan-out on the home path."""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def test_fleet_page_loads_list_only() -> None:
    src = (REPO / "ui" / "src" / "pages" / "Fleet.tsx").read_text(encoding="utf-8")
    assert "loadFleetList" in src
    assert "summariesToCards" in src
    assert "getAttestation" not in src
    assert "getResolved" not in src
    assert "getMemoryPolicy" not in src


def test_org_chat_page_uses_xyflow_and_group_combobox() -> None:
    src = (REPO / "ui" / "src" / "pages" / "OrgChat.tsx").read_text(encoding="utf-8")
    assert "Agent Group" in src
    assert "ReactFlow" in src
    assert "Background" in src
    assert "Controls" in src
    assert "MiniMap" in src
    assert "orgNode" in src
    assert "@xyflow/react" in src
    assert "nodesForInitialFit" in src
    assert "getAttestation" not in src
    assert "getResolved" not in src
    assert "getMemoryPolicy" not in src
    shell = (REPO / "ui" / "src" / "shell" / "AppShell.tsx").read_text(encoding="utf-8")
    labels = (REPO / "ui" / "src" / "shell" / "nav.ts").read_text(encoding="utf-8")
    assert 'HOME_LABEL = "Agent Swarm"' in labels
    assert 'AGENT_MENU_LABEL = "Agent Profile"' in labels
    start = shell.index("<nav ")
    end = shell.index("</nav>", start)
    nav = shell[start:end]
    home = nav.index("{HOME_LABEL}")
    org = nav.index("Agent Org Chat")
    agent = nav.index("{AGENT_MENU_LABEL}")
    assert org > home
    assert org < agent


def test_agent_switcher_filters_full_id_set() -> None:
    src = (REPO / "ui" / "src" / "shell" / "AgentSwitcher.tsx").read_text(encoding="utf-8")
    assert "filterAgentIds" in src
    assert "collectAgentIds" in src
    assert "<datalist" not in src
