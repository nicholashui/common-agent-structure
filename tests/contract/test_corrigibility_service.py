"""Corrigibility-invariant-service HTTP contract (internal plane only)."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.auth.actors import ActorClass
from casops.corrigibility.app import create_corrigibility_service_app
from casops.corrigibility.signing import HostSigner
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode


def _client(tmp_path: Path) -> tuple[TestClient, InvariantStore]:
    key_path = tmp_path / "ed25519.pem"
    HostSigner.generate().save(key_path)
    store = InvariantStore.open(data_dir=tmp_path / "data", key_path=key_path)
    app = create_corrigibility_service_app(store=store)
    return TestClient(app), store


def test_service_has_no_public_api_v3_routes(tmp_path: Path) -> None:
    client, _store = _client(tmp_path)
    spec = client.get("/openapi.json").json()
    public = [path for path in spec["paths"] if str(path).startswith("/api/")]
    assert public == []
    assert "/internal/v1/reference" in spec["paths"]
    assert "/health" in spec["paths"]


def test_health_ok(tmp_path: Path) -> None:
    client, _store = _client(tmp_path)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_host_get_reference_includes_signature(tmp_path: Path) -> None:
    client, store = _client(tmp_path)
    response = client.get(
        "/internal/v1/reference",
        headers={"x-casops-actor": ActorClass.host_service.value},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["digest"] == store.reference_digest()
    assert body["signature"] == store.reference().signature
    assert body["invariant_set_id"] == "casops.host.inv.v1"


def test_agent_cannot_read_or_write_internal_reference(tmp_path: Path) -> None:
    client, store = _client(tmp_path)
    original = store.reference_digest()
    read = client.get(
        "/internal/v1/reference",
        headers={"x-casops-actor": ActorClass.agent_runtime.value},
    )
    write = client.put(
        "/internal/v1/reference",
        json={"invariants": []},
        headers={"x-casops-actor": ActorClass.agent_runtime.value},
    )
    assert read.status_code == 503
    assert write.status_code == 503
    assert read.json()["error"]["code"] == ErrorCode.IMP_CORRIGIBILITY.value
    assert store.reference_digest() == original


def test_attest_mismatch_alerts_and_containment(tmp_path: Path) -> None:
    client, store = _client(tmp_path)
    response = client.post(
        "/internal/v1/attest",
        json={
            "presented_digest": "0" * 64,
            "checkpoint": "run_start",
            "agent_id": "casops.template.baseline_safe",
        },
        headers={"x-casops-actor": ActorClass.host_service.value},
    )
    assert response.status_code == 503
    assert response.json()["error"]["containment_required"] is True
    alerts = client.get(
        "/internal/v1/alerts",
        headers={"x-casops-actor": ActorClass.human_operator.value},
    )
    assert alerts.status_code == 200
    assert alerts.json()["alerts"][-1]["checkpoint"] == "run_start"
