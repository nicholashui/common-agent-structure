"""Every loaded agent has characterization fixtures; run-tc1 stays offline."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from casops.corrigibility.store import InvariantStore
from casops.runtime.executor import Runtime
from casops.runtime.llm import LlmRouter, LlmSettings

REPO = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((REPO / "schemas" / "eval" / "testcase.schema.json").read_text(encoding="utf-8"))


def _agent_rows() -> list[tuple[str, Path]]:
    rows: list[tuple[str, Path]] = []
    for spec_path in sorted((REPO / "agents").glob("*/agent_spec.json")):
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        agent_id = str(spec.get("agent_id") or spec_path.parent.name)
        rows.append((agent_id, spec_path.parent))
    return rows


def _fixture_files(folder: Path, prefix: str) -> list[Path]:
    return sorted(p for p in (folder / "evals" / "fixtures").glob(f"{prefix}*.json") if p.is_file())


def test_every_loaded_agent_has_chat_and_run_fixtures() -> None:
    rows = _agent_rows()
    assert rows, "no agent folders"
    missing: list[str] = []
    for agent_id, folder in rows:
        chats = _fixture_files(folder, "chat-tc")
        run = folder / "evals" / "fixtures" / "run-tc1.json"
        proven = folder / "evals" / "fixtures" / "provenance.json"
        if len(chats) < 1:
            missing.append(f"{agent_id}:no chat fixtures")
        if not run.is_file():
            missing.append(f"{agent_id}:no run-tc1")
        if not proven.is_file():
            missing.append(f"{agent_id}:no provenance")
    assert missing == []


def test_fixtures_match_schema_and_policy() -> None:
    bad: list[str] = []
    for agent_id, folder in _agent_rows():
        for path in _fixture_files(folder, ""):
            if path.name == "provenance.json" or path.name == ".gitkeep":
                continue
            if path.suffix != ".json":
                continue
            payload = json.loads(path.read_text(encoding="utf-8"))
            try:
                jsonschema.validate(payload, SCHEMA)
            except jsonschema.ValidationError as exc:
                bad.append(f"{agent_id}:{path.name}:{exc.message}")
                continue
            if payload.get("agent_id") != agent_id:
                bad.append(f"{agent_id}:{path.name}:agent_id mismatch")
            expect = payload.get("expect") or {}
            if expect.get("memory_writes") != []:
                bad.append(f"{agent_id}:{path.name}:memory_writes")
            if expect.get("plugins_executed") is not False:
                bad.append(f"{agent_id}:{path.name}:plugins")
            if expect.get("t3_enabled") is not False:
                bad.append(f"{agent_id}:{path.name}:t3")
            if expect.get("network_granted") is not False:
                bad.append(f"{agent_id}:{path.name}:network")
            if payload.get("honesty") not in {"CHARACTERIZATION", "INDICATIVE", "NOT_RUN"}:
                bad.append(f"{agent_id}:{path.name}:honesty")
            if payload.get("path") == "chat":
                message = (payload.get("input") or {}).get("message")
                if not isinstance(message, str) or not message.strip():
                    bad.append(f"{agent_id}:{path.name}:empty chat message")
                if expect.get("io_declared_fetched") is not False:
                    bad.append(f"{agent_id}:{path.name}:declared inputs must stay unbound")
    assert bad == []


def test_benchmarks_list_characterization_fixtures() -> None:
    bad: list[str] = []
    for agent_id, folder in _agent_rows():
        bench = json.loads((folder / "evals" / "benchmarks.json").read_text(encoding="utf-8"))
        rows = bench.get("benchmarks") or []
        ids = {str(item.get("id")) for item in rows if isinstance(item, dict)}
        if "run-tc1" not in ids:
            bad.append(f"{agent_id}:benchmarks missing run-tc1")
        if not any(item.startswith("chat-tc") for item in ids):
            bad.append(f"{agent_id}:benchmarks missing chat-tc")
        note = str(bench.get("note") or "")
        if "NOT_RUN" not in note and "CHARACTERIZATION" not in note:
            bad.append(f"{agent_id}:benchmarks note must stay honest")
        for item in rows:
            if isinstance(item, dict) and item.get("honesty") not in {
                "CHARACTERIZATION",
                "INDICATIVE",
                "NOT_RUN",
            }:
                bad.append(f"{agent_id}:{item.get('id')}:benchmark honesty")
    assert bad == []


def test_run_tc1_execute_all_agents_offline(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "local_deterministic")
    llm = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json", default_llm="local_deterministic"))
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults(), llm=llm)
    failures: list[str] = []
    for agent_id, folder in _agent_rows():
        fixture = json.loads((folder / "evals" / "fixtures" / "run-tc1.json").read_text(encoding="utf-8"))
        result = runtime.execute(agent_id)
        if result.agent_id != agent_id:
            failures.append(f"{agent_id}:got {result.agent_id}")
            continue
        if result.memory_writes:
            failures.append(f"{agent_id}:memory_writes")
        if result.containment_stop is not None:
            failures.append(f"{agent_id}:containment")
        if result.adapter not in {"local_deterministic", "host_observe"}:
            failures.append(f"{agent_id}:adapter {result.adapter}")
        if fixture["expect"]["path_id"] != "run":
            failures.append(f"{agent_id}:fixture path")
    assert failures == []
