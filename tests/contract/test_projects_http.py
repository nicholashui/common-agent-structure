"""Companion /api/v3/projects: mutation, dry-run, no path escape."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.api.control import COMPANION_V3_PATHS, create_control_plane

MUTATION = {
    "x-casops-actor": "human_operator",
    "x-casops-reason": "project test",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "true",
}

LIVE = {**MUTATION, "x-casops-dry-run": "false"}
REPO = Path(__file__).resolve().parents[2]


def _client(tmp_path: Path) -> TestClient:
    return TestClient(create_control_plane(agents_root=REPO / "agents", projects_root=tmp_path / "project"))


def test_projects_companion_in_openapi() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    for method, path in COMPANION_V3_PATHS:
        if "/projects" in path:
            assert path in spec["paths"], path


def test_suggest_and_dry_run_create(tmp_path: Path) -> None:
    client = _client(tmp_path)
    unsigned = client.post("/api/v3/projects/suggest", json={"brief": "safety recap"})
    assert unsigned.status_code == 409
    suggest = client.post(
        "/api/v3/projects/suggest",
        headers=MUTATION,
        json={"title": "Safety recap", "brief": "factory-floor safety recap training", "duration": "3min", "outlets": "web", "risk": "medium"},
    )
    assert suggest.status_code == 200
    body = suggest.json()
    assert body["honesty"] == "CHARACTERIZATION"
    assert body["suggestions"]
    assert body["suggestions"][0]["id"].startswith("video.")
    assert body["llm_used"] is False
    assert len(body["catalog"]) == 17
    assert body["prompt"]
    created = client.post(
        "/api/v3/projects",
        headers=MUTATION,
        json={"name": "safety-recap", "title": "Safety recap", "brief": "training", "sub_workflow_id": "video.template.f"},
    )
    assert created.status_code == 200
    assert created.json()["dry_run"] is True
    assert created.json()["saved"] is False
    assert not (tmp_path / "project" / "safety-recap" / "project.json").is_file()


def test_live_create_and_get(tmp_path: Path) -> None:
    client = _client(tmp_path)
    created = client.post(
        "/api/v3/projects",
        headers=LIVE,
        json={
            "name": "Hook Demo",
            "title": "Hook demo",
            "brief": "tiktok spike",
            "duration": "15s",
            "outlets": "social",
            "risk": "low",
            "sub_workflow_id": "video.template.a",
        },
    )
    assert created.status_code == 200
    payload = created.json()
    assert payload["id"] == "hook-demo"
    assert payload["saved"] is True
    assert payload["graph"]["nodes"][0]["id"] == "create-project"
    assert len(payload["graph"]["nodes"]) == 1
    nxt = client.post(
        "/api/v3/projects/hook-demo/next",
        headers=LIVE,
        json={"from_id": "create-project", "occupied": []},
    )
    assert nxt.status_code == 200
    assert nxt.json()["suggestions"]
    assert nxt.json()["suggestions"][0]["kind"] == "agent"
    listed = client.get("/api/v3/projects").json()["projects"]
    assert any(row["id"] == "hook-demo" for row in listed)
    fetched = client.get("/api/v3/projects/hook-demo")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == "Hook demo"


def test_reject_escape_and_agent_actor(tmp_path: Path) -> None:
    client = _client(tmp_path)
    bad = client.post("/api/v3/projects", headers=LIVE, json={"name": "../secret"})
    assert bad.status_code in {400, 409, 422, 500} or bad.status_code >= 400
    agent = client.post(
        "/api/v3/projects",
        headers={**LIVE, "x-casops-actor": "agent_runtime"},
        json={"name": "from-agent"},
    )
    assert agent.status_code == 409
