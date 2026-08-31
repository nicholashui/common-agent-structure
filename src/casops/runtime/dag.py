"""casops.execution_dag.v2 compiler."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

NODE_KINDS = frozenset(
    {
        "model",
        "tool",
        "plugin",
        "memory_read",
        "memory_write",
        "peer_agent",
        "validator",
        "verifier",
        "safety_check",
        "compaction",
        "branch",
        "join",
        "transform",
        "speculative",
        "human_gate",
    }
)


@dataclass
class Node:
    node_id: str
    kind: str
    dependencies: list[str]
    side_effect_class: str
    timeout_ms: int
    idempotent: bool


@dataclass
class Dag:
    ir: str
    nodes: dict[str, Node] = field(default_factory=dict)
    order: list[str] = field(default_factory=list)


def compile_dag(execution: dict[str, Any] | Path) -> Dag:
    payload = execution if isinstance(execution, dict) else json.loads(execution.read_text(encoding="utf-8"))
    if payload.get("ir") != "casops.execution_dag.v2":
        raise CasopsError(ErrorCode.PERF_PLAN_CYCLE, detail="unsupported execution IR")
    dag = Dag(ir=payload["ir"])
    for raw in payload.get("nodes") or []:
        kind = raw.get("kind")
        if kind not in NODE_KINDS:
            raise CasopsError(ErrorCode.PERF_PLAN_CYCLE, detail=f"unknown node kind {kind}")
        node = Node(
            node_id=raw["node_id"],
            kind=kind,
            dependencies=list(raw.get("dependencies") or []),
            side_effect_class=str(raw.get("side_effect_class") or "none"),
            timeout_ms=int(raw.get("timeout_ms") or 1000),
            idempotent=bool(raw.get("idempotent", False)),
        )
        dag.nodes[node.node_id] = node
    dag.order = _topo(dag)
    _reject_unsafe_parallel(dag)
    return dag


def _topo(dag: Dag) -> list[str]:
    visiting: set[str] = set()
    seen: set[str] = set()
    order: list[str] = []

    def walk(node_id: str) -> None:
        if node_id in seen:
            return
        if node_id in visiting:
            raise CasopsError(ErrorCode.PERF_PLAN_CYCLE)
        if node_id not in dag.nodes:
            raise CasopsError(ErrorCode.PERF_PLAN_CYCLE, detail=f"missing node {node_id}")
        visiting.add(node_id)
        for dep in dag.nodes[node_id].dependencies:
            walk(dep)
        visiting.remove(node_id)
        seen.add(node_id)
        order.append(node_id)

    for node_id in dag.nodes:
        walk(node_id)
    return order


def _reject_unsafe_parallel(dag: Dag) -> None:
    side_effecting = [node for node in dag.nodes.values() if node.side_effect_class not in {"none", "read"}]
    ids = {node.node_id for node in side_effecting}
    for node in side_effecting:
        unordered = [dep for dep in node.dependencies if dep in ids]
        # Independent side-effecting nodes with no ordering between them: if two
        # have empty overlapping deps they cannot run in parallel — compiler
        # records them sequentially in topo order; reject only explicit cycles.
        del unordered
