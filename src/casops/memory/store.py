"""Typed memory with tenant/subject isolation and deletion probes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


@dataclass
class MemoryRecord:
    memory_id: str
    tenant: str
    subject: str
    text: str
    tombstoned: bool = False
    indexes: list[str] = field(default_factory=list)
    embeddings: list[str] = field(default_factory=list)
    summaries: list[str] = field(default_factory=list)
    graph_edges: list[str] = field(default_factory=list)
    cache_entries: list[str] = field(default_factory=list)
    consolidated: list[str] = field(default_factory=list)
    flagged: list[str] = field(default_factory=list)


class MemoryService:
    def __init__(self) -> None:
        self._records: dict[str, MemoryRecord] = {}
        self._serving = True

    def write_candidate(
        self,
        *,
        tenant: str,
        subject: str,
        text: str,
        mode: str = "working",
    ) -> MemoryRecord:
        if mode in {"none", "disabled"}:
            raise CasopsError(ErrorCode.MEM_TRUST_TIER, detail="memory writes forbidden in this mode")
        record = MemoryRecord(
            memory_id=str(uuid4()),
            tenant=tenant,
            subject=subject,
            text=text,
            indexes=[text],
            embeddings=[text],
            summaries=[],
            graph_edges=[],
            cache_entries=[],
            consolidated=[],
            flagged=[],
        )
        self._records[record.memory_id] = record
        return record

    def _require_scope(self, record: MemoryRecord, *, tenant: str, subject: str) -> None:
        if record.tenant != tenant or record.subject != subject:
            raise CasopsError(ErrorCode.MEM_SCOPE)

    def query(self, *, tenant: str, subject: str, text: str | None = None) -> list[MemoryRecord]:
        hits = []
        for record in self._records.values():
            if record.tombstoned:
                continue
            if record.tenant != tenant or record.subject != subject:
                continue
            if text is None or text in record.text:
                hits.append(record)
        return hits

    def scoped_query(self, *, tenant: str, subject: str, text: str | None = None) -> list[dict[str, Any]]:
        hits = []
        for record in self._records.values():
            if record.tombstoned:
                continue
            if record.tenant != tenant or record.subject != subject:
                continue
            if text is None or text in record.text:
                hits.append({"memory_id": record.memory_id, "text": record.text})
        return hits

    def delete(self, memory_id: str, *, tenant: str, subject: str) -> None:
        record = self._records[memory_id]
        self._require_scope(record, tenant=tenant, subject=subject)
        record.tombstoned = True
        record.indexes.clear()
        record.embeddings.clear()
        record.summaries.clear()
        record.graph_edges.clear()
        record.cache_entries.clear()
        record.consolidated.clear()
        record.flagged.clear()
        record.text = ""

    def verify_deletion(self, memory_id: str, *, tenant: str, subject: str) -> dict[str, Any]:
        record = self._records[memory_id]
        self._require_scope(record, tenant=tenant, subject=subject)
        residual = {
            "lexical": record.indexes,
            "dense": record.embeddings,
            "graph": record.graph_edges,
            "cache": record.cache_entries,
            "summaries": record.summaries,
            "consolidated": record.consolidated,
            "flagged": record.flagged,
            "text": record.text,
        }
        if any(residual.values()):
            raise CasopsError(ErrorCode.MEM_DELETE_INCOMPLETE)
        return {"memory_id": memory_id, "absent": True, "paths": residual}


class ConsolidationWorker:
    def __init__(self, memory: MemoryService) -> None:
        self.memory = memory
        self.queue: list[dict[str, Any]] = []
        self.ran_on_serving_path = False

    def enqueue(self, job: dict[str, Any]) -> None:
        """Serving-path entry: queue work, never drain."""
        self.queue.append(job)

    def run_offline(self) -> list[dict[str, Any]]:
        """Worker-only drain. Must not be called from serving HTTP handlers."""
        done = list(self.queue)
        self.queue.clear()
        self.ran_on_serving_path = False
        return done
