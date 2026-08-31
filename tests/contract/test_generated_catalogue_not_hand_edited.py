"""Generated catalogue must match spec rows (implementation_plan.md §11.4 check 11)."""

from __future__ import annotations

from casops.contracts.canonical import canonical_dumps
from casops.errors.catalogue import catalogue_document, load_catalogue


def test_committed_catalogue_matches_generated_document() -> None:
    committed = load_catalogue()
    expected = catalogue_document()
    assert canonical_dumps(committed) == canonical_dumps(expected)
