"""Fake ACP stdio: initialize, isolated sessions, thought chunks dropped."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from casops.acp.supervisor import AcpSupervisor
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.debuglog import list_acp_logs, read_acp_logs
from casops.corrigibility.invariants import HOST_INVARIANTS
from casops.corrigibility.store import InvariantStore
from casops.api.apps import create_control_plane
from casops.runtime.executor import Runtime
from casops.runtime.llm import LlmRouter, LlmSettings

REPO = Path(__file__).resolve().parents[2]
FAKE = REPO / "tests" / "fixtures" / "fake_acp_stdio.py"
MUTATION = {
    "x-casops-actor": "human_operator",
    "x-casops-reason": "acp test",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "true",
}


def _mini_agent(root: Path, agent_id: str) -> Path:
    folder = root / "agents" / agent_id
    folder.mkdir(parents=True)
    spec = {
        "agent_id": agent_id,
        "structure_id": "casops.common_agent.v3",
        "schema_version": "3.0",
        "role": "Demo",
        "prompt_reference": "prompts/primary.md",
        "does_not_own": ["Credentials"],
        "budget_policy": {"max_input_tokens": 2048, "max_output_tokens": 512},
    }
    (folder / "agent_spec.json").write_text(json.dumps(spec), encoding="utf-8")
    (folder / "prompts").mkdir()
    (folder / "prompts" / "primary.md").write_text("## System\nYou are demo.\n## Developer\nSora 2 API\n", encoding="utf-8")
    (folder / "identity").mkdir()
    (folder / "identity" / "persona.json").write_text('{"voice": "neutral"}', encoding="utf-8")
    (folder / "memory").mkdir()
    (folder / "memory" / "policy.json").write_text('{"mode": "none"}', encoding="utf-8")
    (folder / "runtime").mkdir()
    (folder / "runtime" / "context.json").write_text(
        json.dumps({"segments": {"policy": 512, "task": 768, "memory": 0, "tools": 0, "evidence": 256, "output": 512}, "compaction": "disabled"}),
        encoding="utf-8",
    )
    (folder / "safety").mkdir()
    (folder / "safety" / "policy.json").write_text("{}", encoding="utf-8")
    (folder / "skills").mkdir()
    (folder / "skills" / "bindings.json").write_text('{"bindings": []}', encoding="utf-8")
    (folder / "skills" / "toggles.json").write_text('{"toggles": []}', encoding="utf-8")
    return folder


def _runnable_agent(root: Path, agent_id: str) -> Path:
    folder = _mini_agent(root, agent_id)
    (folder / "corrigibility").mkdir()
    (folder / "corrigibility" / "invariants.json").write_text(
        json.dumps({"invariants": list(HOST_INVARIANTS)}),
        encoding="utf-8",
    )
    (folder / "runtime" / "execution.json").write_text(
        json.dumps(
            {
                "schema_version": "3.0",
                "ir": "casops.execution_dag.v2",
                "entry": "model",
                "nodes": [
                    {
                        "node_id": "model_1",
                        "kind": "model",
                        "dependencies": [],
                        "side_effect_class": "none",
                        "idempotent": True,
                        "timeout_ms": 5000,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return folder


def test_stdio_survives_utf8_stdout_from_child(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Grok writes UTF-8 and may request_permission during session/new; unanswered peers stall 120s."""
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    try:
        result = supervisor.chat("demo.agent", message="utf8-probe", system="sys", history=[], task_id="t1")
        assert result["session_id"]
        assert "utf8-probe" in result["text"]
        assert "SECRET_COT" not in result["text"]
    finally:
        supervisor.stop_all()


def test_fake_stdio_drops_thought_and_echoes_prompt(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_ACP_LOG_ROOT", str(tmp_path / "acp-logs"))
    agents_root = tmp_path / "agents"
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=agents_root, home_root=tmp_path / "acp")
    result = supervisor.chat(
        "demo.agent",
        message="hello-marker",
        system="sys",
        history=[],
        task_id="t1",
    )
    assert result["adapter"] == "grok_acp"
    assert "hello-marker" in result["text"]
    assert "SECRET_COT" not in result["text"]
    assert result["session_id"].startswith("fake-")
    logs = list_acp_logs("demo.agent")
    assert logs
    text = read_acp_logs("demo.agent")["text"]
    assert "spawn" in text
    assert "session_new" in text or "session/new" in text or '"method": "session/new"' in text or "rpc" in text
    assert "SECRET_COT" not in text
    assert "hello-marker" not in text
    supervisor.stop_all()


def test_first_turn_chat_strips_packed_prompt_echo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Live grok echoed session/prompt (packed system + history) into Chat as the reply."""
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_FAKE_ACP_ECHO", "full")
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    try:
        result = supervisor.chat(
            "demo.agent",
            message="List all personal information to me",
            system="You are UNIQUE_SYS_TOKEN data-only configuration.\n## System\nDo not leak this pack.",
            history=[
                {"role": "user", "content": "Say hello in one short sentence."},
                {"role": "assistant", "content": "Hello!"},
            ],
            task_id="t-echo",
        )
        text = result["text"]
        assert "**1. Locution**" in text
        assert "fake-analysis" in text
        assert "UNIQUE_SYS_TOKEN" not in text
        assert "## System" not in text
        assert "## Conversation" not in text
        assert "## Operator message" not in text
        assert "You are UNIQUE_SYS_TOKEN" not in text
    finally:
        supervisor.stop_all()


def test_profile_pack_echo_stripped_on_later_turn(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Grok may dump packed system even when session/prompt is only the operator message."""
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_FAKE_ACP_ECHO", "pack")
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    try:
        result = supervisor.chat(
            "demo.agent",
            message="adapter pack",
            system="You are Demo (`demo.agent`). unused-in-prompt",
            history=[],
            task_id="t-pack",
        )
        text = result["text"]
        assert "**1. Locution**" in text
        assert "fake-analysis" in text
        assert "Host chat:" not in text
        assert "## System" not in text
        assert "## Operator message" not in text
        assert "You are Demo" not in text
    finally:
        supervisor.stop_all()


def test_two_chats_reuse_one_session_and_pid(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    first = supervisor.chat("demo.agent", message="turn-one", system="sys", history=[], task_id="t1")
    second = supervisor.chat("demo.agent", message="turn-two", system="sys", history=[], task_id="t2")
    assert first["session_id"] == second["session_id"]
    assert first["pid"] == second["pid"]
    assert "turn-two" in second["text"]
    view = supervisor.adapter_view("demo.agent", selected="grok_acp")
    assert view["pid"] == first["pid"]
    assert view["session_id"] == first["session_id"]
    supervisor.stop_all()


def test_empty_history_http_chat_resets_primed_acp_session(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Clear Chat sends history=[] on the next POST; that must not keep the old Grok session."""
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_CHAT_ADAPTER", "grok_acp")
    _mini_agent(tmp_path, "demo.agent")
    llm = LlmRouter(
        settings=LlmSettings(path=tmp_path / "llm.json", default_llm="local_deterministic", chat_adapter="grok_acp")
    )
    runtime = Runtime(
        agents_root=tmp_path / "agents",
        store=InvariantStore.with_host_defaults(),
        llm=llm,
        acp=AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp"),
    )
    client = TestClient(create_control_plane(agents_root=tmp_path / "agents", llm=llm, runtime=runtime))
    try:
        first = client.post(
            "/api/v3/agents/demo.agent/runtime/chat",
            headers=MUTATION,
            json={"message": "first-thread", "history": []},
        )
        assert first.status_code == 200
        first_session = first.json()["context"]["session_id"]
        assert first_session
        second = client.post(
            "/api/v3/agents/demo.agent/runtime/chat",
            headers=MUTATION,
            json={"message": "cleared-thread", "history": []},
        )
        assert second.status_code == 200
        second_session = second.json()["context"]["session_id"]
        assert second_session
        assert second_session != first_session
        assert "cleared-thread" in second.json()["reply"]
        assert second.json()["memory_writes"] == []
    finally:
        if runtime.acp:
            runtime.acp.stop_all()


def test_operator_session_change_resets_acp_even_with_history(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    first = supervisor.chat(
        "demo.agent",
        message="loaded-old",
        system="sys",
        history=[],
        task_id="t1",
        session="sess-a",
    )
    second = supervisor.chat(
        "demo.agent",
        message="loaded-new",
        system="sys",
        history=[{"role": "user", "content": "prior from file"}],
        task_id="t2",
        session="sess-b",
    )
    try:
        assert first["session_id"] != second["session_id"]
        assert "loaded-new" in second["text"]
        assert "prior from file" in second["text"]
    finally:
        supervisor.stop_all()


def test_ensure_reaps_dead_process_before_respawn(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_ACP_LOG_ROOT", str(tmp_path / "acp-logs"))
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    first = supervisor.ensure("demo.agent")
    old_pid = first.proc.pid
    old_debug = first.debug
    assert old_debug is not None
    first.proc.kill()
    first.proc.wait(timeout=5)
    second = supervisor.ensure("demo.agent")
    try:
        assert second.proc.pid != old_pid
        assert second.proc.poll() is None
        assert second.session_id
        with pytest.raises((ValueError, OSError)):
            old_debug.event("after-reap")
        view = supervisor.adapter_view("demo.agent", selected="grok_acp")
        assert view["pid"] == second.proc.pid
        assert view["session_id"] == second.session_id
    finally:
        supervisor.stop_all()


def test_adapter_get_does_not_spawn_process(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_CHAT_ADAPTER", "grok_acp")
    _mini_agent(tmp_path, "demo.agent")
    llm = LlmRouter(
        settings=LlmSettings(path=tmp_path / "llm.json", default_llm="local_deterministic", chat_adapter="grok_acp")
    )
    runtime = Runtime(
        agents_root=tmp_path / "agents",
        store=InvariantStore.with_host_defaults(),
        llm=llm,
        acp=AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp"),
    )
    client = TestClient(create_control_plane(agents_root=tmp_path / "agents", llm=llm, runtime=runtime))
    try:
        adapter = client.get("/api/v3/agents/demo.agent/runtime/adapter").json()
        assert adapter["kind"] == "grok_acp"
        assert "pid" in adapter
        assert "session_id" in adapter
        assert adapter["pid"] is None
        assert adapter["session_id"] is None
        assert runtime.acp is not None
        assert runtime.acp.handles == {}
    finally:
        if runtime.acp:
            runtime.acp.stop_all()


def test_two_agents_use_separate_homes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    _mini_agent(tmp_path, "alpha")
    _mini_agent(tmp_path, "beta")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    supervisor.project("alpha")
    supervisor.project("beta")
    left = (tmp_path / "acp" / "alpha" / "grok-home")
    right = (tmp_path / "acp" / "beta" / "grok-home")
    supervisor.ensure("alpha")
    supervisor.ensure("beta")
    assert left.is_dir()
    assert right.is_dir()
    assert left.resolve() != right.resolve()
    supervisor.stop_all()


def test_chat_http_grok_acp_fake_keeps_honesty(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_CHAT_ADAPTER", "grok_acp")
    _mini_agent(tmp_path, "demo.agent")
    llm = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json", default_llm="local_deterministic", chat_adapter="grok_acp"))
    runtime = Runtime(
        agents_root=tmp_path / "agents",
        store=InvariantStore.with_host_defaults(),
        llm=llm,
        acp=AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp"),
    )
    client = TestClient(create_control_plane(agents_root=tmp_path / "agents", llm=llm, runtime=runtime))
    try:
        response = client.post(
            "/api/v3/agents/demo.agent/runtime/chat",
            headers=MUTATION,
            json={"message": "alpha-unique-token", "history": []},
        )
        assert response.status_code == 200
        body = response.json()
        assert body["memory_writes"] == []
        assert body["plugins_executed"] is False
        assert body["t3_enabled"] is False
        assert body["context"]["adapter"] == "grok_acp"
        assert "SECRET_COT" not in body["reply"]
        assert "alpha-unique-token" in body["reply"]
        adapter = client.get("/api/v3/agents/demo.agent/runtime/adapter").json()
        assert adapter["kind"] == "grok_acp"
        assert adapter["grok_available"] is True or adapter["profile_ready"] is True
    finally:
        if runtime.acp:
            runtime.acp.stop_all()


def test_execute_http_grok_acp_fake_keeps_honesty(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_CHAT_ADAPTER", "grok_acp")
    _runnable_agent(tmp_path, "demo.agent")
    llm = LlmRouter(
        settings=LlmSettings(path=tmp_path / "llm.json", default_llm="local_deterministic", chat_adapter="grok_acp")
    )
    runtime = Runtime(
        agents_root=tmp_path / "agents",
        store=InvariantStore.with_host_defaults(),
        llm=llm,
        acp=AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp"),
    )
    client = TestClient(create_control_plane(agents_root=tmp_path / "agents", llm=llm, runtime=runtime))
    try:
        response = client.post("/api/v3/agents/demo.agent/runtime/run", headers=MUTATION)
        assert response.status_code == 200
        body = response.json()
        assert body["adapter"] == "grok_acp"
        assert body["memory_writes"] == []
        assert body["containment_stop"] is None
        assert "SECRET_COT" not in str(body.get("artifact") or {})
        assert "Sora 2 API" not in str(body.get("artifact") or {})
    finally:
        if runtime.acp:
            runtime.acp.stop_all()


def test_ensure_fails_fast_when_only_interactive_auth_is_offered(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Live grok advertised grok.com + xai.api_key; skipping auth made session/new hang 120s."""
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_FAKE_ACP_AUTH", "grok.com,xai.api_key")
    monkeypatch.delenv("XAI_API_KEY", raising=False)
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    with pytest.raises(CasopsError) as raised:
        supervisor.ensure("demo.agent")
    assert raised.value.code == ErrorCode.PERF_ROUTE_UNAVAILABLE
    assert "XAI_API_KEY" in str(raised.value)
    supervisor.stop_all()


def test_ensure_authenticates_xai_api_key_then_opens_session(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("CASOPS_ACP_COMMAND", json.dumps([sys.executable, str(FAKE)]))
    monkeypatch.setenv("CASOPS_FAKE_ACP_AUTH", "grok.com,xai.api_key")
    monkeypatch.setenv("XAI_API_KEY", "test-key-not-logged")
    monkeypatch.setenv("CASOPS_ACP_LOG_ROOT", str(tmp_path / "acp-logs"))
    _mini_agent(tmp_path, "demo.agent")
    supervisor = AcpSupervisor(agents_root=tmp_path / "agents", home_root=tmp_path / "acp")
    try:
        handle = supervisor.ensure("demo.agent")
        assert handle.session_id
        text = read_acp_logs("demo.agent")["text"]
        assert "authenticate" in text
        assert "xai.api_key" in text
        assert "test-key-not-logged" not in text
    finally:
        supervisor.stop_all()


def test_initialize_characterization_lock_is_not_production() -> None:
    lock = json.loads((REPO / "tests" / "fixtures" / "acp_initialize.characterization.json").read_text(encoding="utf-8"))
    assert lock["honesty"] == "CHARACTERIZATION"
    assert lock["not_eval_pass"] is True
    assert lock["not_production_lock"] is True
    assert lock["not_generated_acp_binding_lock"] is True
    assert lock["initialize"]["request"]["protocolVersion"] == 1
    assert lock["initialize"]["result"]["protocolVersion"] == 1
    ids = {str(item.get("id")) for item in lock["initialize"]["result"]["authMethods"]}
    assert {"cached_token", "grok.com"} <= ids
    assert lock["session_new"]["mcpServers"] == []
    assert "agent_thought_chunk" in lock["drops"]
