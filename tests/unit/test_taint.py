"""Taint survives transform/summary/compaction/consolidation (FR-SAF-002)."""

from casops.safety.taint import Taint


def test_taint_survives_transforms() -> None:
    taint = Taint(frozenset({"untrusted_tool"}))
    assert taint.transform().labels == taint.labels
    assert taint.summarize().labels == taint.labels
    assert taint.compact().labels == taint.labels
    merged = taint.consolidate(Taint(frozenset({"peer"})))
    assert merged.labels == frozenset({"untrusted_tool", "peer"})
