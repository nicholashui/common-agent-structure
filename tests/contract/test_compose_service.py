"""Compose-service internal HTTP contract."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.compose.app import create_compose_service_app
from casops.corrigibility.store import InvariantStore

REPO = Path(__file__).resolve().parents[2]


def test_service_has_no_public_api_v3_routes() -> None:
    app = create_compose_service_app(
        agents_root=REPO / "agents",
        store=InvariantStore.with_host_defaults(),
    )
    client = TestClient(app)
    spec = client.get("/openapi.json").json()
    public = [path for path in spec["paths"] if str(path).startswith("/api/")]
    assert public == []
    assert "/internal/v1/compose-preview" in spec["paths"]
    assert "/health" in spec["paths"]


def test_internal_preview_is_side_effect_free() -> None:
    app = create_compose_service_app(
        agents_root=REPO / "agents",
        store=InvariantStore.with_host_defaults(),
    )
    client = TestClient(app)
    response = client.post(
        "/internal/v1/compose-preview",
        json={"agent_id": "casops.template.baseline_safe"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["wrote_locks"] is False
    assert body["mro"][0] == "casops.template.baseline_safe"
    assert "child_hash" in body["lock"]
    assert not (REPO / "agents" / "_template_v3" / "generated").exists()
