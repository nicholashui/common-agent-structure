"""Memory and consolidation health probes."""

from __future__ import annotations

from fastapi.testclient import TestClient

from casops.memory.app import create_consolidation_app, create_memory_service_app
from casops.memory.store import ConsolidationWorker, MemoryService


def test_memory_health() -> None:
    client = TestClient(create_memory_service_app())
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "memory-service"


def test_consolidation_health_offline() -> None:
    worker = ConsolidationWorker(MemoryService())
    client = TestClient(create_consolidation_app(worker))
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["service"] == "consolidation-worker"
    assert body["ran_on_serving_path"] is False
