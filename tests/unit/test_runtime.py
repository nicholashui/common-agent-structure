"""baseline_safe runtime: one root trace, safety gate, no memory writes."""

from __future__ import annotations

import threading
from pathlib import Path

import pytest

from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.runtime.dag import compile_dag
from casops.runtime.executor import Runtime

REPO = Path(__file__).resolve().parents[2]


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


def test_template_run_has_one_root_trace_and_no_memory_write() -> None:
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults())
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


def test_cancellation_at_node_boundary() -> None:
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults())
    cancel = threading.Event()
    cancel.set()
    with pytest.raises(CasopsError) as raised:
        runtime.execute("casops.template.baseline_safe", cancel=cancel)
    assert raised.value.code == ErrorCode.SAF_TERMINATION
