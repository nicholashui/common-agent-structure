"""Runtime-service health and template execution via shipped factory."""

from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from casops.corrigibility.store import InvariantStore
from casops.runtime.app import create_runtime_service_app
from casops.runtime.executor import Runtime
from casops.runtime.llm import LlmRouter, LlmSettings

REPO = Path(__file__).resolve().parents[2]


def test_health_and_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "local_deterministic")
    llm = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json", default_llm="local_deterministic"))
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults(), llm=llm)
    client = TestClient(create_runtime_service_app(agents_root=REPO / "agents", runtime=runtime))
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
