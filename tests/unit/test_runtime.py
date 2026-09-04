"""baseline_safe runtime: one root trace, safety gate, no memory writes."""

from __future__ import annotations

import threading
import json
from pathlib import Path

import pytest

from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.runtime.dag import compile_dag
from casops.runtime.executor import Runtime
from casops.runtime.llm import LlmRouter, LlmSettings

REPO = Path(__file__).resolve().parents[2]


def _local_runtime(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Runtime:
    monkeypatch.setenv("DEFAULT_LLM", "local_deterministic")
    llm = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json", default_llm="local_deterministic"))
    return Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults(), llm=llm)


def test_cycle_fails_closed() -> None:
    with pytest.raises(CasopsError) as raised:
        compile_dag(
            {
                "ir": "casops.execution_dag.v2",
                "nodes": [
                    {"node_id": "a", "kind": "model", "dependencies": ["b"]},
                    {"node_id": "b", "kind": "model", "dependencies": ["a"]},
                ],
            }
        )
    assert raised.value.code == ErrorCode.PERF_PLAN_CYCLE


def test_template_run_has_one_root_trace_and_no_memory_write(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    runtime = _local_runtime(tmp_path, monkeypatch)
    result = runtime.execute("casops.template.baseline_safe")
    assert result.adapter == "local_deterministic"
    assert result.containment_stop is None
    assert result.memory_writes == []
    roots = [span for span in result.trace["spans"] if span["parent_id"] is None]
    assert len(roots) == 1
    assert roots[0]["span_id"] == result.root_trace_id
    assert result.artifact["sealed"] is True
    assert len(result.artifact["digest"]) == 64
    assert result.safety["passed"] is True


def test_common_health_run_returns_host_snapshot() -> None:
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults())
    result = runtime.execute("common.health")
    assert result.agent_id == "common.health"
    assert result.adapter == "host_observe"
    assert result.containment_stop is None
    assert result.memory_writes == []
    assert result.safety["passed"] is True
    payload = json.loads(result.artifact["text"])
    assert payload["status"] == "ok"
    assert payload["service"] == "control-plane"
    assert payload["agent_id"] == "common.health"
    assert payload["folder_ok"] is True
    assert payload["memory_mode"] == "none"
    assert payload["plugins"] == 0
    assert payload["t3_enabled"] is False
    assert payload["production_activation_requested"] is False
    assert payload["network_access"] is False
    assert payload["containment_stop"] is None
    assert any("eval pass" in note.lower() for note in payload["notes"])


def test_unknown_transform_op_fails_closed_at_execute(tmp_path: Path) -> None:
    import shutil

    src = REPO / "agents" / "common.health"
    dest = tmp_path / "common.health"
    shutil.copytree(src, dest)
    execution = json.loads((dest / "runtime" / "execution.json").read_text(encoding="utf-8"))
    execution["nodes"][0]["op"] = "not_a_real_op"
    (dest / "runtime" / "execution.json").write_text(json.dumps(execution), encoding="utf-8")
    runtime = Runtime(agents_root=tmp_path, store=InvariantStore.with_host_defaults())
    with pytest.raises(CasopsError) as raised:
        runtime.execute("common.health")
    assert raised.value.code == ErrorCode.PERF_PLAN_CYCLE


def test_cancellation_at_node_boundary() -> None:
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults())
    cancel = threading.Event()
    cancel.set()
    with pytest.raises(CasopsError) as raised:
        runtime.execute("casops.template.baseline_safe", cancel=cancel)
    assert raised.value.code == ErrorCode.SAF_TERMINATION


def test_chat_uses_operator_message_and_does_not_record_a_run(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    runtime = _local_runtime(tmp_path, monkeypatch)
    before = len(runtime.runs)
    first = runtime.chat("casops.template.baseline_safe", message="alpha-unique-token")
    second = runtime.chat("casops.template.baseline_safe", message="beta-unique-token")
    assert len(runtime.runs) == before
    assert first["memory_writes"] == []
    assert first["plugins_executed"] is False
    assert first["t3_enabled"] is False
    assert first["provider"] == "local_deterministic"
    assert json.loads(first["reply"])["prompt_sha256"] != json.loads(second["reply"])["prompt_sha256"]


def test_chat_empty_message_fails_closed(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    runtime = _local_runtime(tmp_path, monkeypatch)
    with pytest.raises(CasopsError) as raised:
        runtime.chat("casops.template.baseline_safe", message="  ")
    assert raised.value.code == ErrorCode.CTX_BUDGET


def test_chat_stub_output_budget_uses_host_floor_and_drops_reasoning(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import shutil

    dest = tmp_path / "stub.chat"
    shutil.copytree(REPO / "agents" / "_template_v3", dest)
    spec_path = dest / "agent_spec.json"
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    spec["agent_id"] = "stub.chat"
    spec["budget_policy"]["max_output_tokens"] = 1
    spec_path.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
    captured: dict[str, object] = {}

    def post(url: str, headers: dict[str, str], payload: dict[str, object]) -> dict[str, object]:
        del url, headers
        captured["payload"] = payload
        return {
            "choices": [
                {
                    "finish_reason": "length",
                    "message": {"content": "I", "reasoning_content": "hidden thinking"},
                }
            ]
        }

    monkeypatch.setenv("DEFAULT_LLM", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    llm = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json", default_llm="openai"), post=post)
    runtime = Runtime(agents_root=tmp_path, store=InvariantStore.with_host_defaults(), llm=llm)
    result = runtime.chat("stub.chat", message="what you are thinking?")
    assert captured["payload"]["max_tokens"] == 512
    assert result["reply"] == "I"
    assert "hidden" not in result["reply"]
    assert result["llm"]["truncated"] is True
    assert result["llm"]["max_tokens_source"] == "host_floor"
    assert result["llm"]["declared_max_output_tokens"] == 1
    assert result["llm"]["finish_reason"] == "length"


def test_chat_declared_budget_above_floor_is_honoured(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    captured: dict[str, object] = {}

    def post(url: str, headers: dict[str, str], payload: dict[str, object]) -> dict[str, object]:
        del url, headers
        captured["payload"] = payload
        return {"choices": [{"finish_reason": "stop", "message": {"content": "ok"}}]}

    monkeypatch.setenv("DEFAULT_LLM", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    llm = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json", default_llm="openai"), post=post)
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults(), llm=llm)
    result = runtime.chat("video.director", message="hello from operator")
    assert captured["payload"]["max_tokens"] == 1024
    assert result["reply"] == "ok"
    assert result["llm"]["max_tokens_source"] == "spec"
    assert result["llm"]["truncated"] is False
