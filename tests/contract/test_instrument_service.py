"""Instrument-registry-service health and persistence."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.corrigibility.signing import HostSigner
from casops.instruments.app import create_instrument_service_app
from casops.instruments.registry import InstrumentRegistry


def test_health_lists_instruments(tmp_path: Path) -> None:
    key = tmp_path / "k.pem"
    HostSigner.generate().save(key)
    registry = InstrumentRegistry.open(data_dir=tmp_path / "data", key_path=key)
    client = TestClient(create_instrument_service_app(registry))
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["unqualified"] is True
    assert "INS-01" in body["instruments"]
    record = client.get("/internal/v1/instruments/INS-01").json()
    assert record["status"] == "UNQUALIFIED"
    assert record["may_gate"] is False
    assert record["signature"]
