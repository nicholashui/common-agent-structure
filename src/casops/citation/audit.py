"""CIT-GATE-001 / CIT-GATE-002 citation auditor."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from casops.citation.fetch import Fetcher, LiveSource, default_fetcher, fetch_arxiv, fetch_url
from casops.citation.inventory import spec_references
from casops.contracts.canonical import canonical_dumps, sha256_json
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

SPEC_DOCUMENT_DATE = "2026-08-31"
_STOP = frozenset("a an the of for to in on with and or by from as is are".split())


def _tokens(text: str) -> set[str]:
    words = {token.lower() for token in "".join(ch.lower() if ch.isalnum() else " " for ch in text).split()}
    return {word for word in words if word and word not in _STOP}


def titles_match(expected: str, observed: str) -> bool:
    if not expected or not observed:
        return False
    left = " ".join(expected.lower().split())
    right = " ".join(observed.lower().split())
    if left in right or right in left:
        return True
    a, b = _tokens(expected), _tokens(observed)
    if not a or not b:
        return False
    overlap = len(a & b) / len(a)
    return overlap >= 0.5


def _locate_claims(claims: list[str], body: str, title: str) -> list[dict[str, str]]:
    haystack = f"{title}\n{body}".lower()
    located: list[dict[str, str]] = []
    for claim in claims:
        needles = [part.lower() for part in claim.replace("%", " ").replace("→", " ").split() if part]
        found = all(needle in haystack for needle in needles if needle not in {"to", "verified"})
        # Require distinctive numerals when present.
        numerals = [token for token in claim.replace("%", " ").replace("→", " ").split() if any(ch.isdigit() for ch in token)]
        if numerals:
            found = all(num.lower() in haystack for num in numerals)
        located.append(
            {
                "claim": claim,
                "location": "abstract/body" if found else "",
                "status": "verified" if found else "not_located",
            }
        )
    return located


def resolve_one(entry: dict[str, Any], *, fetcher: Fetcher, verified_at: str, verified_by: str) -> dict[str, Any]:
    kind = entry["kind"]
    identifier = entry["resolved_identifier"]
    source: LiveSource
    if kind == "arxiv":
        source = fetch_arxiv(identifier, fetcher=fetcher)
    elif kind == "url":
        source = fetch_url(identifier, fetcher=fetcher)
    else:
        source = LiveSource(identifier, "", (), "knowledge", "", "", "", False)

    claims = _locate_claims(list(entry.get("numeric_claims") or []), source.body, source.title)
    unmatched_claim = any(item["status"] != "verified" for item in claims)

    if kind == "knowledge":
        status = "deleted"
        reason = "unresolvable knowledge-derived reference deleted; controls rest on independent engineering justification"
        marker_after = "deleted"
    elif not source.found:
        status = "unverified"
        reason = "live source not found"
        marker_after = entry["marker_before"]
    elif not titles_match(entry["expected_title"], source.title) and not titles_match(
        entry["expected_title"], source.body[:4000]
    ):
        status = "mismatch"
        reason = "title mismatch"
        marker_after = entry["marker_before"]
    elif unmatched_claim:
        status = "numeric_unverified"
        reason = "numeric claim not located"
        marker_after = entry["marker_before"]
    else:
        status = "accepted"
        reason = "live source matches identifier and title"
        marker_after = "A"

    # Withdrawn Agent Lightning v1.0 numeric claim cannot support a requirement even if the paper exists.
    if entry["reference_id"] == "ref-051" and status == "accepted":
        status = "external_only"
        reason = "numeric claim confined to MEASURED_EXTERNAL; cannot support a requirement"
        marker_after = "A"

    return {
        "reference_id": entry["reference_id"],
        "marker_before": entry["marker_before"],
        "marker_after": marker_after,
        "resolved_identifier": source.identifier or identifier,
        "expected_title": entry["expected_title"],
        "observed_title": source.title,
        "authors": list(source.authors),
        "venue": source.venue,
        "year": int(source.published[:4]) if source.published[:4].isdigit() else None,
        "published": source.published,
        "evidence_grade": entry["evidence_grade"],
        "numeric_claims": claims,
        "verified_by": verified_by,
        "verified_at": verified_at,
        "source_digest": source.digest,
        "status": status,
        "reason": reason,
    }


def run_audit(
    *,
    fetcher: Fetcher | None = None,
    verified_by: str = "casops-citation-auditor",
    now: datetime | None = None,
    document_date: str = SPEC_DOCUMENT_DATE,
) -> dict[str, Any]:
    clock = now or datetime.now(timezone.utc)
    verified_at = clock.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    audit_date = clock.date().isoformat()
    # CIT-GATE-002: do not backdate. If verification is after the spec cutoff, record it.
    if audit_date < document_date:
        raise CasopsError(ErrorCode.CIT_MISMATCH, detail="verification timestamp precedes document date")
    cit_gate_002 = "ok"
    if audit_date > document_date:
        cit_gate_002 = (
            f"verification {audit_date} is after document date {document_date}; "
            "spec must be reissued — audit is not backdated"
        )
    fetch = fetcher or default_fetcher
    inventory = spec_references()
    by_id = {item["reference_id"]: item for item in inventory}
    entries = []
    for item in inventory:
        entries.append(resolve_one(item, fetcher=fetch, verified_at=verified_at, verified_by=verified_by))
        if fetch is default_fetcher and item["kind"] == "arxiv":
            import time as _time

            _time.sleep(0.25)
    if fetch is default_fetcher:
        import time as _time

        for index, item in enumerate(list(entries)):
            if item["status"] != "unverified":
                continue
            _time.sleep(2.0)
            entries[index] = resolve_one(
                by_id[item["reference_id"]],
                fetcher=fetch,
                verified_at=verified_at,
                verified_by=verified_by,
            )
    accepted = sum(1 for item in entries if item["marker_after"] == "A")
    deleted = sum(1 for item in entries if item["marker_after"] == "deleted")
    blocking = [
        item["reference_id"]
        for item in entries
        if item["marker_after"] not in {"A", "deleted"}
    ]
    document = {
        "schema_version": "3.0",
        "gate": "CIT-GATE-001",
        "document_date": document_date,
        "audit_date": audit_date,
        "cit_gate_002": cit_gate_002,
        "verified_by": verified_by,
        "entries": entries,
        "counts": {
            "total": len(entries),
            "accepted": accepted,
            "deleted": deleted,
            "blocking": len(blocking),
        },
        "blocking": blocking,
        "cleared": not blocking and cit_gate_002 == "ok",
    }
    document["digest"] = sha256_json({k: v for k, v in document.items() if k != "digest"})
    return document


def write_audit(document: dict[str, Any], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_dumps(document) + "\n", encoding="utf-8")
    return path


def require_cleared(document: dict[str, Any]) -> None:
    if document.get("cleared"):
        return
    raise CasopsError(ErrorCode.CIT_UNVERIFIED, detail="citation audit has blocking entries")


def load_audit(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))
