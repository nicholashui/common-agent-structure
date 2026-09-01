"""Control-plane: every spec §19 path, mutation contract, agent cannot approve."""

from __future__ import annotations

import json
from pathlib import Path

from fastapi.testclient import TestClient

from casops.api.apps import create_control_plane
from casops.api.control import COMPANION_V3_PATHS, SPEC_V3_PATHS

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


def test_list_agents_includes_template() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.get("/api/v3/agents")
    assert response.status_code == 200
    body = response.json()
    ids = [item["agent_id"] for item in body["agents"]]
    assert "casops.template.baseline_safe" in ids
    assert "common.health" in ids
    template = next(item for item in body["agents"] if item["agent_id"] == AGENT)
    assert template["structure_id"] == "casops.common_agent.v3"
    assert template["schema_version"] == "3.0"
    assert template["role"] == "BaselineSafeTemplate"
    assert template["memory_mode"] == "none"


def test_list_agents_includes_every_folder() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    listed = {item["agent_id"] for item in client.get("/api/v3/agents").json()["agents"]}
    expected: set[str] = set()
    for child in (REPO / "agents").iterdir():
        spec_path = child / "agent_spec.json"
        if not child.is_dir() or not spec_path.is_file():
            continue
        payload = json.loads(spec_path.read_text(encoding="utf-8"))
        expected.add(str(payload.get("agent_id") or child.name))
    assert listed == expected
    assert "video.director" in listed
    assert "specials.planner-agent" in listed


def test_list_agents_includes_va_category_for_video_director() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    body = client.get("/api/v3/agents").json()
    director = next(item for item in body["agents"] if item["agent_id"] == "video.director")
    assert director["va_category"] == "1-ATL"


def test_list_agents_two_gets_agree_and_match_folder_count() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    first = client.get("/api/v3/agents")
    second = client.get("/api/v3/agents")
    assert first.status_code == 200
    assert second.status_code == 200
    ids_first = [item["agent_id"] for item in first.json()["agents"]]
    ids_second = [item["agent_id"] for item in second.json()["agents"]]
    assert ids_first == ids_second
    folder_count = sum(
        1
        for child in (REPO / "agents").iterdir()
        if child.is_dir() and (child / "agent_spec.json").is_file()
    )
    assert len(ids_first) == folder_count


def test_companion_list_path_is_public_v3() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    for _method, path in COMPANION_V3_PATHS:
        assert path in spec["paths"], path
        assert path.startswith("/api/v3")


def test_cors_preflight_from_vite_origin() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.options(
        "/api/v3/agents",
        headers={
            "Origin": "http://127.0.0.1:5173",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code in {200, 204}
    assert response.headers.get("access-control-allow-origin") == "http://127.0.0.1:5173"


def test_common_health_run_returns_snapshot() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.post(f"/api/v3/agents/common.health/runtime/run", headers=MUTATION)
    assert response.status_code == 200
    body = response.json()
    assert body["agent_id"] == "common.health"
    assert body["adapter"] == "host_observe"
    payload = json.loads(body["artifact"]["text"])
    assert payload["status"] == "ok"
    assert payload["service"] == "control-plane"
    assert payload["agent_id"] == "common.health"


def test_common_health_compose_preview() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.post("/api/v3/agents/common.health/compose-preview", headers=MUTATION)
    assert response.status_code == 200
    body = response.json()
    assert body["agent_id"] == "common.health"
    assert body["wrote_locks"] is False
    assert "common.health" in body["mro"]
    assert "casops.template.baseline_safe" in body["mro"]


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
