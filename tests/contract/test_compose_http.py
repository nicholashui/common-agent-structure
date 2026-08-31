"""Compose preview HTTP (spec §19)."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.api.apps import create_compose_app, create_control_plane

REPO = Path(__file__).resolve().parents[2]


def test_compose_preview_on_template() -> None:
    client = TestClient(create_compose_app(agents_root=REPO / "agents"))
    response = client.post("/api/v3/agents/casops.template.baseline_safe/compose-preview")
    assert response.status_code == 200
    body = response.json()
    assert len(body["compose_hash"]) == 64
    assert body["mro"][0] == "casops.template.baseline_safe"


def test_control_plane_exposes_only_api_v3_public_paths() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    paths = spec["paths"]
    assert all(path.startswith("/api/v3") for path in paths)
    assert "/api/v3/agents/{agent_id}/compose-preview" in paths
    assert "/api/v3/agents/{agent_id}/corrigibility/attestation" in paths
    assert "/internal/v1/reference" not in paths
