"""WP-001: canonical source path + SHA-256 digest."""

from __future__ import annotations

import json
from pathlib import Path

from casops.contracts.canonical import sha256_file

REPO = Path(__file__).resolve().parents[2]


def test_source_identity_matches_common_agent_structure_bytes() -> None:
    recorded = json.loads(
        (REPO / "docs" / "citation" / "source-identity.json").read_text(encoding="utf-8")
    )
    source = REPO / "common_agent_structure.md"
    assert recorded["canonical_path"] == "common_agent_structure.md"
    assert recorded["document_id"] == "CASOPS-FS-COMMON-AGENT-STRUCTURE-V3A"
    assert recorded["sha256"] == sha256_file(source)
    assert recorded["filename_title_discrepancy"] is True
    assert recorded["internal_title"] == "common_agent_structure.v3a.md"
