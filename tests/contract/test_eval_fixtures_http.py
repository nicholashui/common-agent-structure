"""GET /api/v3/agents/{id}/evals/fixtures is a companion read of CHARACTERIZATION cases."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.api.apps import create_control_plane
from casops.api.control import COMPANION_V3_PATHS, SPEC_V3_PATHS

REPO = Path(__file__).resolve().parents[2]
PATH = "/api/v3/agents/{agent_id}/evals/fixtures"


def test_eval_fixtures_companion_in_openapi() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    assert ("GET", PATH) in COMPANION_V3_PATHS
    assert PATH in spec["paths"]
    assert spec["paths"][PATH].get("get")
    assert ("GET", PATH) not in SPEC_V3_PATHS


def test_eval_fixtures_http_lists_characterization_cases() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    for agent_id in ("video.director", "specials.intent-analysis-agent", "common.health"):
        response = client.get(f"/api/v3/agents/{agent_id}/evals/fixtures")
        assert response.status_code == 200
        body = response.json()
        assert body["agent_id"] == agent_id
        assert body["honesty"] == "CHARACTERIZATION"
        assert body.get("pass") is not True
        assert "NOT_RUN" in body["note"] or "CHARACTERIZATION" in body["note"]
        ids = {item["id"] for item in body["fixtures"]}
        assert "chat-tc1" in ids
        assert "run-tc1" in ids
        chat = next(item for item in body["fixtures"] if item["id"] == "chat-tc1")
        assert chat["path"] == "chat"
        assert chat["honesty"] == "CHARACTERIZATION"
        assert str(chat["input"]["message"]).strip()
        assert chat["expect"]["memory_writes"] == []
        assert chat["expect"]["plugins_executed"] is False
        assert chat["expect"]["t3_enabled"] is False


def test_eval_fixtures_http_every_loaded_agent() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    listed = client.get("/api/v3/agents").json()["agents"]
    assert listed
    missing: list[str] = []
    for row in listed:
        agent_id = row["agent_id"]
        body = client.get(f"/api/v3/agents/{agent_id}/evals/fixtures").json()
        if body["honesty"] != "CHARACTERIZATION":
            missing.append(f"{agent_id}:honesty")
        if body.get("pass") is True:
            missing.append(f"{agent_id}:pass")
        chats = [item for item in body["fixtures"] if item.get("path") == "chat"]
        runs = [item for item in body["fixtures"] if item.get("path") == "run"]
        if not chats:
            missing.append(f"{agent_id}:no chat")
        if not runs:
            missing.append(f"{agent_id}:no run")
    assert missing == []


def test_eval_fixtures_missing_agent_is_not_200() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.get("/api/v3/agents/does.not.exist/evals/fixtures")
    assert response.status_code != 200
