"""Corrigibility HTTP surface: public GET + agent cannot write the reference."""

from __future__ import annotations

from fastapi.testclient import TestClient

from casops.api.apps import create_corrigibility_app
from casops.corrigibility.store import InvariantStore


def test_public_attestation_route() -> None:
    client = TestClient(create_corrigibility_app())
    response = client.get("/api/v3/agents/casops.template.baseline_safe/corrigibility/attestation")
    assert response.status_code == 200
    assert response.json()["digest"]


def test_agent_put_reference_is_forbidden() -> None:
    store = InvariantStore.with_host_defaults()
    original = store.reference_digest()
    client = TestClient(create_corrigibility_app(store))
    response = client.put(
        "/internal/v1/reference",
        json={"invariants": []},
        headers={"x-casops-actor": "agent_runtime"},
    )
    assert response.status_code == 503
    assert response.json()["error"]["code"] == "IMP_CORRIGIBILITY"
    assert store.reference_digest() == original


def test_host_attest_mismatch_containment() -> None:
    client = TestClient(create_corrigibility_app())
    response = client.post(
        "/internal/v1/attest",
        json={"presented_digest": "0" * 64},
        headers={"x-casops-actor": "host_service"},
    )
    assert response.status_code == 503
    assert response.json()["error"]["containment_required"] is True
