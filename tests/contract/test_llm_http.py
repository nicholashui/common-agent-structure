"""LLM companion routes: mutation contract, no secrets, dry-run does not persist."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from casops.api.apps import create_control_plane
from casops.runtime.llm import LlmRouter, LlmSettings

REPO = Path(__file__).resolve().parents[2]
MUTATION = {
    "x-casops-actor": "human_operator",
    "x-casops-reason": "set default llm",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "false",
}


def _client(tmp_path: Path, monkeypatch) -> TestClient:
    monkeypatch.setenv("DEFAULT_LLM", "local_deterministic")
    monkeypatch.setenv("CASOPS_LLM_SETTINGS", str(tmp_path / "llm-settings.json"))
    llm = LlmRouter(settings=LlmSettings.load(tmp_path / "llm-settings.json"))
    return TestClient(create_control_plane(agents_root=REPO / "agents", llm=llm))


def test_providers_endpoint_lists_local_and_hides_keys(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-live-secret")
    client = _client(tmp_path, monkeypatch)
    body = client.get("/api/v3/llm/providers").json()
    ids = [item["id"] for item in body["providers"]]
    assert "local_deterministic" in ids
    assert "openai" in ids
    assert "sk-live-secret" not in str(body)


def test_set_default_llm_requires_mutation_headers(tmp_path: Path, monkeypatch) -> None:
    client = _client(tmp_path, monkeypatch)
    response = client.post("/api/v3/llm/settings", json={"default_llm": "local_deterministic"})
    assert response.status_code != 200
    assert response.json()["error"]["code"] == "IMP_UNSIGNED"


def test_dry_run_does_not_persist_default(tmp_path: Path, monkeypatch) -> None:
    client = _client(tmp_path, monkeypatch)
    headers = dict(MUTATION)
    headers["x-casops-dry-run"] = "true"
    response = client.post("/api/v3/llm/settings", json={"default_llm": "openai"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["saved"] is False
    assert response.json()["dry_run"] is True
    saved = client.get("/api/v3/llm/settings").json()
    assert saved["default_source"] == "DEFAULT_LLM"
    assert saved["default_llm"] == "local_deterministic"


def test_operator_sets_default_and_agent_override(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    client = _client(tmp_path, monkeypatch)
    fleet = client.post(
        "/api/v3/llm/settings",
        json={"default_llm": "openai"},
        headers=MUTATION,
    )
    assert fleet.status_code == 200
    assert fleet.json()["saved"] is True
    assert fleet.json()["default_llm"] == "openai"
    agent = "casops.template.baseline_safe"
    override = client.post(
        f"/api/v3/agents/{agent}/llm",
        json={"provider": "local_deterministic"},
        headers=MUTATION,
    )
    assert override.status_code == 200
    assert override.json()["provider"] == "local_deterministic"
    assert override.json()["override"] == "local_deterministic"
    view = client.get(f"/api/v3/agents/{agent}/llm").json()
    assert view["provider"] == "local_deterministic"
    assert view["default_llm"] == "openai"


def test_agent_runtime_cannot_change_llm(tmp_path: Path, monkeypatch) -> None:
    client = _client(tmp_path, monkeypatch)
    headers = dict(MUTATION)
    headers["x-casops-actor"] = "agent_runtime"
    response = client.post("/api/v3/llm/settings", json={"default_llm": "openai"}, headers=headers)
    assert response.status_code != 200
    assert response.json()["error"]["code"] == "IMP_SELF_APPROVAL"
