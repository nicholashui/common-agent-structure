"""Public plane exposes folder and merged I/O; chat companion accepts a message."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from casops.api.apps import create_control_plane
from casops.api.control import COMPANION_V3_PATHS
from casops.runtime.llm import LlmRouter, LlmSettings

REPO = Path(__file__).resolve().parents[2]
MUTATION = {
    "x-casops-actor": "host_service",
    "x-casops-reason": "test",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "true",
}


def test_structure_exposes_video_director_io() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    body = client.get("/api/v3/agents/video.director/structure").json()
    assert body["agent_id"] == "video.director"
    assert body["folder"] == "agents/video.director"
    assert body["spec_bytes"] > 0
    assert body["io"]["defined"] is True
    assert body["io"]["merged"] is False
    assert "video.critic" in body["io"]["inputs"]
    assert "video.judge" in body["io"]["outputs"]
    assert "video.critic" in body["spec"]["critique_edges"]["inputs"]
    assert body["spec"]["prompt_reference"]


def test_structure_template_declares_empty_io_bus() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    body = client.get("/api/v3/agents/casops.template.baseline_safe/structure").json()
    assert body["io"]["source"] == "critique_edges"
    assert body["io"]["defined"] is False
    assert body["io"]["inputs"] == []
    assert body["io"]["outputs"] == []


def test_resolved_exposes_merged_io() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    body = client.get("/api/v3/agents/video.director/resolved").json()
    assert body["io"]["merged"] is True
    assert "video.critic" in body["io"]["inputs"]
    assert "video.judge" in body["io"]["outputs"]
    assert "mro" in body
    assert len(body["compose_hash"]) == 64


def test_chat_companion_is_public_v3() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    assert ("POST", "/api/v3/agents/{agent_id}/runtime/chat") in COMPANION_V3_PATHS
    assert "/api/v3/agents/{agent_id}/runtime/chat" in spec["paths"]
    assert spec["paths"]["/api/v3/agents/{agent_id}/runtime/chat"].get("post")


def test_chat_requires_mutation_headers(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    client = _chat_client(tmp_path, monkeypatch)
    response = client.post(
        "/api/v3/agents/video.director/runtime/chat",
        json={"message": "hello"},
    )
    assert response.status_code != 200
    assert response.json()["error"]["code"] == "IMP_UNSIGNED"


def test_chat_empty_message_is_rejected(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    client = _chat_client(tmp_path, monkeypatch)
    response = client.post(
        "/api/v3/agents/video.director/runtime/chat",
        headers=MUTATION,
        json={"message": "   "},
    )
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "CTX_BUDGET"


def _chat_client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setenv("DEFAULT_LLM", "local_deterministic")
    monkeypatch.setenv("CASOPS_PROOF_ROOT", str(tmp_path / "proof"))
    llm = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json", default_llm="local_deterministic"))
    return TestClient(create_control_plane(agents_root=REPO / "agents", llm=llm))


def test_chat_returns_reply_without_memory_or_plugins(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    client = _chat_client(tmp_path, monkeypatch)
    response = client.post(
        "/api/v3/agents/video.director/runtime/chat",
        headers=MUTATION,
        json={"message": "alpha-unique-token", "history": []},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["agent_id"] == "video.director"
    assert body["reply"]
    assert body["provider"] == "local_deterministic"
    assert body["memory_writes"] == []
    assert body["plugins_executed"] is False
    assert body["t3_enabled"] is False
    proof = body["proof"]
    assert proof["path_id"] == "chat"
    assert proof["not_a_dag_run"] is True
    assert proof["eval"]["pass"] is not True
    assert proof["eval"]["verdict"] == "NOT_RUN"
    assert proof["io_binding"]["declared_inputs_fetched"] is False
    assert proof["io_binding"]["operator_message"]["status"] == "bound"
    assert "video.critic" in [row["id"] for row in proof["io_binding"]["declared_inputs"]]
    assert proof["observability"]["status"] == "NOT_APPLIED"
    assert proof["observability"]["exporter_wired"] is False
    assert proof["negative"]["network_granted"] is False
    assert proof["spec_applied"]["dag_executed"] is False
    assert body["llm"]["max_tokens_source"] == "spec"
    assert body["llm"]["truncated"] is False
    assert "video.critic" in body["io"]["inputs"]
    context = body["context"]
    assert context["compaction"] == "disabled"
    assert context["skills"] == []
    assert "skills/SKILL.md" in context["omitted"]
    assert "memory" in context["omitted"]
    assert "tools" in context["omitted"]
    names = {row["name"]: row for row in context["segments"]}
    assert names["task"]["tokens"] <= names["task"]["budget"]
    assert names["memory"]["included"] is False
    payload = json.loads(body["reply"])
    other = client.post(
        "/api/v3/agents/video.director/runtime/chat",
        headers=MUTATION,
        json={"message": "beta-unique-token"},
    ).json()
    assert json.loads(other["reply"])["prompt_sha256"] != payload["prompt_sha256"]


def test_chat_accepts_human_text_for_every_sample_agent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    client = _chat_client(tmp_path, monkeypatch)
    for agent_id in ("video.director", "common.health", "casops.template.baseline_safe"):
        response = client.post(
            f"/api/v3/agents/{agent_id}/runtime/chat",
            headers=MUTATION,
            json={"message": "hello, this is a human text message"},
        )
        assert response.status_code == 200, agent_id
        body = response.json()
        assert body["agent_id"] == agent_id
        assert body["reply"]
        assert body["memory_writes"] == []
        assert body["proof"]["path_id"] == "chat"
        assert body["proof"]["io_binding"]["declared_inputs_fetched"] is False
        assert body["proof"]["eval"]["pass"] is not True


def test_chat_proof_every_loaded_agent_is_honest(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    client = _chat_client(tmp_path, monkeypatch)
    listed = client.get("/api/v3/agents").json()["agents"]
    assert listed
    bad: list[str] = []
    for row in listed:
        agent_id = row["agent_id"]
        body = client.post(
            f"/api/v3/agents/{agent_id}/runtime/chat",
            headers=MUTATION,
            json={"message": "issue-0002 proof probe", "history": []},
        ).json()
        proof = body.get("proof") or {}
        if proof.get("path_id") != "chat":
            bad.append(f"{agent_id}:path")
        if proof.get("not_a_dag_run") is not True:
            bad.append(f"{agent_id}:dag")
        if (proof.get("io_binding") or {}).get("declared_inputs_fetched") is not False:
            bad.append(f"{agent_id}:fetched")
        if (proof.get("eval") or {}).get("pass") is True:
            bad.append(f"{agent_id}:eval-pass")
        if (proof.get("observability") or {}).get("status") != "NOT_APPLIED":
            bad.append(f"{agent_id}:obs")
        if (proof.get("negative") or {}).get("plugins_executed") is not False:
            bad.append(f"{agent_id}:plugins")
        record = proof.get("decision_record") or {}
        for key in ("inputs", "actions", "constraints", "codes", "outcomes"):
            if key not in record:
                bad.append(f"{agent_id}:decision.{key}")
                break
    assert bad == []
