"""Runtime-service health and template execution via shipped factory."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.runtime.app import create_runtime_service_app

REPO = Path(__file__).resolve().parents[2]


def test_health_and_run() -> None:
    client = TestClient(create_runtime_service_app(agents_root=REPO / "agents"))
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "ok"
    response = client.post(
        "/internal/v1/runs",
        json={"agent_id": "casops.template.baseline_safe"},
        headers={"x-casops-actor": "host_service"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["containment_stop"] is None
    roots = [span for span in body["trace"]["spans"] if span["parent_id"] is None]
    assert len(roots) == 1
    assert body["memory_writes"] == []
