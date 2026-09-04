"""baseline_safe runtime: admit, compile, attest, execute, seal."""

from __future__ import annotations

import json
import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from casops.auth.actors import ActorClass
from casops.compose.folders import locate_agent_folder
from casops.contracts.canonical import sha256_json
from casops.corrigibility.checkpoints import Checkpoint
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.compose.io import folder_io
from casops.runtime.adapter import DeterministicAdapter
from casops.runtime.chat import build_chat_system, load_prompt, normalize_history, require_message
from casops.runtime.dag import compile_dag
from casops.runtime.health import observe_health
from casops.runtime.llm import LlmRouter, parse_token_count, public_llm_view, resolve_completion_tokens
from casops.runtime.safety import safety_gate
from casops.runtime.trace import add_child, start_run_trace


@dataclass
class RunResult:
    agent_id: str
    root_trace_id: str
    trace: dict[str, Any]
    artifact: dict[str, Any]
    containment_stop: str | None
    memory_writes: list[Any]
    safety: dict[str, Any]
    cancelled: bool
    adapter: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "root_trace_id": self.root_trace_id,
            "trace": self.trace,
            "artifact": self.artifact,
            "containment_stop": self.containment_stop,
            "memory_writes": self.memory_writes,
            "safety": self.safety,
            "cancelled": self.cancelled,
            "adapter": self.adapter,
        }


@dataclass
class Runtime:
    agents_root: Path
    store: InvariantStore
    adapter: DeterministicAdapter = field(default_factory=DeterministicAdapter)
    llm: LlmRouter | None = None
    runs: dict[str, RunResult] = field(default_factory=dict)
    artifacts: dict[str, dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.llm is None:
            self.llm = LlmRouter()
        self.llm.local = self.adapter

    def execute(
        self,
        agent_id: str,
        *,
        cancel: threading.Event | None = None,
        actor: ActorClass = ActorClass.host_service,
    ) -> RunResult:
        del actor
        folder = locate_agent_folder(self.agents_root, agent_id)
        if folder is None:
            raise CasopsError(ErrorCode.INH_PARENT_MISSING)
        spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
        memory_policy = json.loads((folder / "memory" / "policy.json").read_text(encoding="utf-8"))
        safety_policy = json.loads((folder / "safety" / "policy.json").read_text(encoding="utf-8"))
        execution = json.loads((folder / "runtime" / "execution.json").read_text(encoding="utf-8"))
        invariants = json.loads((folder / "corrigibility" / "invariants.json").read_text(encoding="utf-8"))
        presented = sha256_json({"invariants": invariants.get("invariants")})
        self.store.attest(
            actor=ActorClass.host_service,
            presented_digest=presented,
            checkpoint=Checkpoint.run_start,
            agent_id=agent_id,
        )
        dag = compile_dag(execution)
        run_id = sha256_json({"agent": agent_id, "n": len(self.runs)})
        trace = start_run_trace(run_id)
        outputs: list[dict[str, Any]] = []
        cancelled = False
        for node_id in dag.order:
            if cancel is not None and cancel.is_set():
                cancelled = True
                safety_gate(output={}, policy=safety_policy, cancelled=True)
            node = dag.nodes[node_id]
            add_child(trace, name=f"node.{node.kind}", attributes={"node_id": node_id})
            if node.kind == "model":
                prompt = (folder / "prompts" / "primary.md").read_text(encoding="utf-8")
                budget = spec.get("budget_policy") or {}
                max_tokens, _source = resolve_completion_tokens(budget.get("max_output_tokens"))
                router = self.llm or LlmRouter()
                outputs.append(
                    router.complete(
                        agent_id=str(spec.get("agent_id") or agent_id),
                        prompt=prompt,
                        node_id=node_id,
                        max_tokens=max_tokens,
                    )
                )
            elif node.kind == "transform":
                if node.op != "health_snapshot":
                    raise CasopsError(ErrorCode.PERF_PLAN_CYCLE, detail=f"unsupported transform {node.op}")
                outputs.append(
                    observe_health(folder=folder, spec=spec, store=self.store, node_id=node_id)
                )
            elif node.kind == "memory_write":
                if memory_policy.get("mode") in {None, "none", "disabled"}:
                    continue
            elif node.kind == "plugin":
                raise CasopsError(ErrorCode.PLG_ISOLATION_TIER)
        last = outputs[-1] if outputs else {"text": "", "digest": sha256_json({"empty": True})}
        safety = safety_gate(output=last, policy=safety_policy, cancelled=cancelled)
        artifact = {
            "id": f"art_{run_id[:12]}",
            "digest": sha256_json({"outputs": outputs, "agent": agent_id}),
            "sealed": True,
            "text": last.get("text"),
        }
        result = RunResult(
            agent_id=spec.get("agent_id") or agent_id,
            root_trace_id=trace.root_id,
            trace=trace.as_dict(),
            artifact=artifact,
            containment_stop=None,
            memory_writes=[],
            safety=safety,
            cancelled=cancelled,
            adapter=str(last.get("provider") or self.adapter.provider),
        )
        self.runs[result.root_trace_id] = result
        self.artifacts[artifact["id"]] = {
            "artifact": artifact,
            "evidence_graph": {
                "claims": [{"text": last.get("text"), "support": last.get("provider") or "deterministic_adapter"}],
                "unsupported": [],
            },
            "run": result.root_trace_id,
        }
        return result

    def chat(
        self,
        agent_id: str,
        *,
        message: str,
        history: list[Any] | None = None,
    ) -> dict[str, Any]:
        folder = locate_agent_folder(self.agents_root, agent_id)
        if folder is None:
            raise CasopsError(ErrorCode.INH_PARENT_MISSING)
        text = require_message(message)
        spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
        safety_policy = json.loads((folder / "safety" / "policy.json").read_text(encoding="utf-8"))
        io = folder_io(folder, spec=spec, merged=False)
        system, prompt_ref = load_prompt(folder, spec)
        budget = spec.get("budget_policy") or {}
        declared = parse_token_count(budget.get("max_output_tokens"))
        max_tokens, max_tokens_source = resolve_completion_tokens(budget.get("max_output_tokens"))
        router = self.llm or LlmRouter()
        completion = router.complete(
            agent_id=str(spec.get("agent_id") or agent_id),
            prompt=text,
            node_id="chat",
            max_tokens=max_tokens,
            system=build_chat_system(prompt=system, io=io),
            history=normalize_history(history),
        )
        safety = safety_gate(output=completion, policy=safety_policy, cancelled=False)
        return {
            "agent_id": spec.get("agent_id") or agent_id,
            "reply": str(completion.get("text") or ""),
            "provider": str(completion.get("provider") or self.adapter.provider),
            "digest": str(completion.get("digest") or ""),
            "io": io,
            "memory_writes": [],
            "plugins_executed": False,
            "t3_enabled": False,
            "used_prompt_reference": prompt_ref,
            "safety": safety,
            "llm": public_llm_view(
                completion,
                max_tokens=max_tokens,
                max_tokens_source=max_tokens_source,
                declared_max_output_tokens=declared,
            ),
        }
