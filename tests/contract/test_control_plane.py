"""Control-plane: every spec §19 path, mutation contract, agent cannot approve."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.api.apps import create_control_plane
from casops.api.control import SPEC_V3_PATHS

REPO = Path(__file__).resolve().parents[2]
AGENT = "casops.template.baseline_safe"
MUTATION = {
    "x-casops-actor": "host_service",
    "x-casops-reason": "test",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "true",
}


def test_openapi_contains_every_spec_v3_path() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    paths = spec["paths"]
    assert all(path.startswith("/api/v3") for path in paths)
    for _method, path in SPEC_V3_PATHS:
        assert path in paths, path


def test_mutation_without_contract_is_not_200() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.post(f"/api/v3/agents/{AGENT}/compose-preview")
    assert response.status_code != 200
    assert response.json()["error"]["code"] == "IMP_UNSIGNED"


def test_compose_preview_with_contract_returns_hash() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.post(f"/api/v3/agents/{AGENT}/compose-preview", headers=MUTATION)
    assert response.status_code == 200
    body = response.json()
    assert body["agent_id"] == AGENT
    assert len(body["compose_hash"]) == 64


def test_serving_consolidate_enqueues_and_does_not_drain() -> None:
    from casops.memory.store import ConsolidationWorker, MemoryService

    memory = MemoryService()
    worker = ConsolidationWorker(memory)
    client = TestClient(
        create_control_plane(agents_root=REPO / "agents", memory=memory, consolidator=worker)
    )
    response = client.post(f"/api/v3/agents/{AGENT}/memory/consolidate", headers=MUTATION)
    assert response.status_code == 200
    body = response.json()
    assert body["queued"] is True
    assert body["queue_depth"] == 1
    assert len(worker.queue) == 1
    drained = worker.run_offline()
    assert len(drained) == 1
    assert worker.queue == []


def test_agent_runtime_cannot_approve() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    headers = dict(MUTATION)
    headers["x-casops-actor"] = "agent_runtime"
    response = client.post(
        f"/api/v3/agents/{AGENT}/improvement/candidates/c1/approve",
        headers=headers,
    )
    assert response.status_code != 200
    assert response.json()["error"]["code"] in {"IMP_SELF_APPROVAL"}
