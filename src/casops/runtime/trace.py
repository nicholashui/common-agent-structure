"""Exactly one root trace per run."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from casops.contracts.canonical import sha256_json


@dataclass
class Span:
    span_id: str
    parent_id: str | None
    name: str
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass
class Trace:
    root_id: str
    spans: list[Span] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "root_trace_id": self.root_id,
            "spans": [
                {
                    "span_id": span.span_id,
                    "parent_id": span.parent_id,
                    "name": span.name,
                    "attributes": span.attributes,
                }
                for span in self.spans
            ],
        }


def start_run_trace(run_id: str) -> Trace:
    root = f"tr_{sha256_json({'run': run_id})[:16]}"
    trace = Trace(root_id=root)
    trace.spans.append(Span(span_id=root, parent_id=None, name="run.root"))
    return trace


def add_child(trace: Trace, *, name: str, attributes: dict[str, Any] | None = None) -> Span:
    span_id = f"sp_{sha256_json({'root': trace.root_id, 'name': name, 'n': len(trace.spans)})[:16]}"
    span = Span(
        span_id=span_id,
        parent_id=trace.root_id,
        name=name,
        attributes=attributes or {},
    )
    trace.spans.append(span)
    return span
