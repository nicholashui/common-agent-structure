"""Memory isolation, deletion probes, and offline consolidation."""

from __future__ import annotations

import pytest

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.memory.store import ConsolidationWorker, MemoryService


def test_cross_tenant_query_is_not_returned() -> None:
    memory = MemoryService()
    memory.write_candidate(tenant="t1", subject="s1", text="alpha")
    hits = memory.scoped_query(tenant="t2", subject="s1")
    assert hits == []


def test_mixed_tenant_authorized_query_returns_only_caller_rows() -> None:
    memory = MemoryService()
    first = memory.write_candidate(tenant="t1", subject="s1", text="alpha")
    memory.write_candidate(tenant="t2", subject="s1", text="beta")
    hits = memory.query(tenant="t1", subject="s1")
    assert [row.memory_id for row in hits] == [first.memory_id]
    assert all(row.tenant == "t1" for row in hits)


def test_cross_tenant_delete_raises_mem_scope_and_leaves_record() -> None:
    memory = MemoryService()
    record = memory.write_candidate(tenant="t1", subject="s1", text="secret")
    with pytest.raises(CasopsError) as raised:
        memory.delete(record.memory_id, tenant="t2", subject="s1")
    assert raised.value.code == ErrorCode.MEM_SCOPE
    remaining = memory.query(tenant="t1", subject="s1")
    assert remaining[0].memory_id == record.memory_id
    assert remaining[0].tombstoned is False


def test_delete_then_probe_is_empty() -> None:
    memory = MemoryService()
    record = memory.write_candidate(tenant="t1", subject="s1", text="secret")
    memory.delete(record.memory_id, tenant="t1", subject="s1")
    probe = memory.verify_deletion(record.memory_id, tenant="t1", subject="s1")
    assert probe["absent"] is True
    assert memory.scoped_query(tenant="t1", subject="s1", text="secret") == []


def test_mode_none_forbids_writes() -> None:
    memory = MemoryService()
    with pytest.raises(CasopsError) as raised:
        memory.write_candidate(tenant="t1", subject="s1", text="x", mode="none")
    assert raised.value.code == ErrorCode.MEM_TRUST_TIER


def test_query_write_delete_do_not_drain_queue() -> None:
    memory = MemoryService()
    worker = ConsolidationWorker(memory)
    worker.enqueue({"id": "job-1"})
    record = memory.write_candidate(tenant="t1", subject="s1", text="alpha")
    memory.query(tenant="t1", subject="s1")
    memory.delete(record.memory_id, tenant="t1", subject="s1")
    assert len(worker.queue) == 1
    drained = worker.run_offline()
    assert [job["id"] for job in drained] == ["job-1"]
    assert worker.queue == []
