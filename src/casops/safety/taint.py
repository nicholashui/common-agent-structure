"""Taint labels survive transform, summary, compaction, and consolidation (FR-SAF-002)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Taint:
    labels: frozenset[str]

    def transform(self) -> Taint:
        return Taint(self.labels)

    def summarize(self) -> Taint:
        return Taint(self.labels)

    def compact(self) -> Taint:
        return Taint(self.labels)

    def consolidate(self, other: Taint) -> Taint:
        return Taint(self.labels | other.labels)
