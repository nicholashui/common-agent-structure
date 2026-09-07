"""ISSUE-0002 Chat proof: bound operator message, name-only buses, not a DAG run."""

from __future__ import annotations

from pathlib import Path

from casops.runtime.chat import pack_chat_context
from casops.runtime.proof import build_chat_proof, observability_view

REPO = Path(__file__).resolve().parents[2]


def test_observability_is_honest_not_applied() -> None:
    folder = REPO / "agents" / "specials.intent-analysis-agent"
    view = observability_view(folder)
    assert view["status"] == "NOT_APPLIED"
    assert view["exporter_wired"] is False
    assert view["files_present"]["telemetry.json"] is True
    assert view["exporter_declared"] == "otlp"


def test_chat_proof_binds_message_not_declared_buses() -> None:
    folder = REPO / "agents" / "video.director"
    spec = __import__("json").loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    io = {"inputs": ["video.critic"], "outputs": ["video.judge"]}
    packed = pack_chat_context(folder, spec, io, message="hello-operator", history=[])
    proof = build_chat_proof(
        agent_id="video.director",
        folder=folder,
        spec=spec,
        io=io,
        packed=packed,
        completion={"provider": "local_deterministic", "digest": "abc", "finish_reason": "stop", "text": "ok", "content_chars": 2},
        adapter="host_llm",
        max_tokens=1024,
        max_tokens_source="spec",
        message="hello-operator",
        history=[],
    )
    assert proof["path_id"] == "chat"
    assert proof["not_a_dag_run"] is True
    assert proof["eval"]["pass"] is False
    assert proof["eval"]["verdict"] == "NOT_RUN"
    assert proof["io_binding"]["operator_message"]["status"] == "bound"
    assert proof["io_binding"]["declared_inputs_fetched"] is False
    assert proof["io_binding"]["declared_inputs"][0]["id"] == "video.critic"
    assert proof["io_binding"]["declared_inputs"][0]["fetched"] is False
    assert proof["output"]["declared_outputs_produced"] is False
    assert proof["negative"]["plugins_executed"] is False
    assert proof["negative"]["t3_enabled"] is False
    assert proof["negative"]["network_granted"] is False
    assert proof["observability"]["status"] == "NOT_APPLIED"
    assert proof["model"]["folder_model_policy_used_for_routing"] is False
    assert proof["spec_applied"]["packed_system"] is True
    assert proof["spec_applied"]["dag_executed"] is False
    for key in ("inputs", "actions", "constraints", "codes", "outcomes"):
        assert key in proof["decision_record"]
