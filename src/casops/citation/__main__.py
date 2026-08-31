"""python -m casops.citation — execute CIT-GATE-001 against live sources."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from casops.citation.audit import run_audit, write_audit

REPO = Path(__file__).resolve().parents[3]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="casops-citation")
    parser.add_argument(
        "--out",
        type=Path,
        default=REPO / "evals" / "reports" / "citation-audit" / "citation-audit.json",
    )
    parser.add_argument("--verified-by", default="casops-citation-auditor")
    args = parser.parse_args(argv)
    document = run_audit(verified_by=args.verified_by, now=datetime.now(timezone.utc))
    write_audit(document, args.out)
    committed = REPO / "docs" / "citation" / "citation-audit.json"
    write_audit(document, committed)
    print(args.out)
    print(f"cleared={document['cleared']} blocking={len(document['blocking'])} total={document['counts']['total']}")
    return 0 if document["cleared"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
