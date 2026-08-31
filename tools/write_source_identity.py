"""WP-001: record canonical source path and SHA-256 digest."""

from __future__ import annotations

import json
from pathlib import Path

from casops.contracts.canonical import sha256_file

REPO = Path(__file__).resolve().parents[1]


def main() -> None:
    source = REPO / "common_agent_structure.md"
    document = {
        "canonical_path": "common_agent_structure.md",
        "document_id": "CASOPS-FS-COMMON-AGENT-STRUCTURE-V3A",
        "internal_title": "common_agent_structure.v3a.md",
        "attachment_filename": "common_agent_structure.md",
        "filename_title_discrepancy": True,
        "sha256": sha256_file(source),
    }
    out = REPO / "docs" / "citation" / "source-identity.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out} sha256={document['sha256']}")


if __name__ == "__main__":
    main()
