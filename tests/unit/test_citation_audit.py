"""CIT-GATE-001/002: live-source audit, no backdating, no false accepts."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from casops.citation.audit import run_audit, titles_match
from casops.citation.inventory import spec_references
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def _arxiv_xml(arxiv_id: str, title: str, published: str = "2025-07-28T00:00:00Z") -> bytes:
    return f"""<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/{arxiv_id}</id>
    <title>{title}</title>
    <published>{published}</published>
    <author><name>Ada Lovelace</name></author>
    <summary>Abstract text without the withdrawn SWE-bench numbers.</summary>
  </entry>
</feed>
""".encode()


def test_inventory_covers_d_c_and_k_markers() -> None:
    refs = spec_references()
    markers = {item["marker_before"] for item in refs}
    assert markers == {"D", "C", "K"}
    assert len(refs) >= 55


def test_titles_match_allows_subtitle_extension() -> None:
    assert titles_match(
        "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve",
        "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence",
    )


def test_audit_accepts_matching_arxiv_and_blocks_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    def fetcher(url: str) -> bytes:
        if "2507.21046" in url:
            return _arxiv_xml(
                "2507.21046",
                "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve",
            )
        if "export.arxiv.org" in url:
            return b"""<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns="http://www.w3.org/2005/Atom"></feed>
"""
        return b"<html><title>Trace Context</title></html>"

    now = datetime(2026, 8, 31, tzinfo=timezone.utc)
    document = run_audit(fetcher=fetcher, now=now, verified_by="test", document_date="2026-08-31")
    by_id = {item["reference_id"]: item for item in document["entries"]}
    assert by_id["ref-010"]["status"] == "accepted"
    assert by_id["ref-010"]["marker_after"] == "A"
    assert by_id["ref-001"]["status"] == "unverified"
    assert document["audit_date"] == "2026-08-31"
    assert document["cit_gate_002"] == "ok"
    # Missing live sources stay unverified, not silently accepted as [A].
    assert by_id["ref-001"]["marker_after"] != "A"
    assert document["cleared"] is False


def test_cit_gate_002_rejects_backdated_verification() -> None:
    now = datetime(2026, 8, 1, tzinfo=timezone.utc)
    with pytest.raises(CasopsError) as raised:
        run_audit(fetcher=lambda _url: b"", now=now, document_date="2026-08-31")
    assert raised.value.code == ErrorCode.CIT_MISMATCH
