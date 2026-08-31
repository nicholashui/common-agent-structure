"""Trainer-bridge health."""

from __future__ import annotations

from fastapi.testclient import TestClient

from casops.improvement.app import create_trainer_app


def test_trainer_health() -> None:
    client = TestClient(create_trainer_app())
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["service"] == "trainer-bridge"
    assert body["gradient_updates_in_serving"] == 0
