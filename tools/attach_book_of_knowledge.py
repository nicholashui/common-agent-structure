"""Attach Book of Knowledge titles onto matching agent folders.

Usage:
  python tools/attach_book_of_knowledge.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from casops.registry.book_of_knowledge import attach_book_of_knowledge  # noqa: E402

DEFAULT_BOOK = REPO / "spec" / "book_of_knowledge.md"
DEFAULT_AGENTS = REPO / "agents"


def main() -> int:
    report = attach_book_of_knowledge(DEFAULT_BOOK, DEFAULT_AGENTS)
    print(
        f"parsed {report.parsed_agents} agents / {report.book_count} titles from {DEFAULT_BOOK}"
    )
    print(f"wrote sources for {len(report.written)} folders")
    if report.missing_folders:
        print("missing folders:", ", ".join(report.missing_folders))
    if report.skipped_unlisted:
        print("unlisted (unchanged):", ", ".join(report.skipped_unlisted))
    if report.count_mismatches:
        print("count mismatches:", report.count_mismatches)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
