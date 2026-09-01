"""Parse and attach Book of Knowledge rows by agent id."""

from __future__ import annotations

import json
from pathlib import Path

from casops.registry.book_of_knowledge import (
    ORIGIN,
    attach_book_of_knowledge,
    parse_book_entry,
    parse_book_of_knowledge,
)

SAMPLE = """# Book of Knowledge

## Specials agents (19)

| Agent | Books (title / author / ISBN-13) | Count |
|-------|----------------------------------|------:|
| `specials.planner-agent` | EN: The Mythical Man-Month (Frederick P. Brooks Jr.), ISBN-13 9780201835953<br>ZH: 人月神话，ISBN-13 9787302154419 | 2 |

## Video agents (114)

| Agent | Books | Count |
|-------|-------|------:|
| `video.director` | EN: Film Art: An Introduction, 12th ed. (Bordwell, Thompson, Smith), ISBN-13 9781259534959<br>EN: Introduction to Information Retrieval, ISBN-13 9780521865715　　　　 | 2 |
| `video.archivemaster` | EN: Reflections: On Cinematography (Roger Deakins) — check latest ed. ISBN-13 9781910593998 | 1 |
"""


def _write_provenance(folder: Path, extra: dict | None = None) -> Path:
    path = folder / "sources" / "PROVENANCE.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"schema_version": "3.0", "sources": [], "imported_from": "src"}
    if extra:
        payload.update(extra)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    (folder / "agent_spec.json").write_text(
        json.dumps({"agent_id": folder.name, "schema_version": "3.0"}),
        encoding="utf-8",
    )
    return path


def test_parse_entry_english_author() -> None:
    item = parse_book_entry(
        "EN: Ways of Seeing (John Berger), ISBN-13 9780140135152"
    )
    assert item["language"] == "EN"
    assert item["title"] == "Ways of Seeing"
    assert item["author"] == "John Berger"
    assert item["isbn13"] == "9780140135152"
    assert item["kind"] == "reference_book"
    assert item["origin"] == ORIGIN


def test_parse_entry_chinese_author_and_bare_title() -> None:
    with_author = parse_book_entry("ZH: 美的历程（李泽厚），ISBN-13 9787108017963")
    assert with_author["language"] == "ZH"
    assert with_author["title"] == "美的历程"
    assert with_author["author"] == "李泽厚"
    bare = parse_book_entry("ZH: 思考，快与慢，ISBN-13 9787508633565")
    assert bare["title"] == "思考，快与慢"
    assert "author" not in bare


def test_parse_entry_strips_edition_note() -> None:
    item = parse_book_entry(
        "EN: Reflections: On Cinematography (Roger Deakins) — check latest ed. ISBN-13 9781910593998"
    )
    assert item["title"] == "Reflections: On Cinematography"
    assert item["author"] == "Roger Deakins"
    assert item["isbn13"] == "9781910593998"


def test_parse_catalog_matches_declared_counts() -> None:
    catalog = parse_book_of_knowledge(SAMPLE)
    assert set(catalog) == {
        "specials.planner-agent",
        "video.director",
        "video.archivemaster",
    }
    assert [b["isbn13"] for b in catalog["specials.planner-agent"]] == [
        "9780201835953",
        "9787302154419",
    ]
    director = catalog["video.director"]
    assert director[0]["author"] == "Bordwell, Thompson, Smith"
    assert "author" not in director[1]
    assert director[1]["title"] == "Introduction to Information Retrieval"


def test_attach_writes_sources_and_preserves_importer_keys(tmp_path: Path) -> None:
    book = tmp_path / "book_of_knowledge.md"
    book.write_text(SAMPLE, encoding="utf-8")
    agents = tmp_path / "agents"
    planner = _write_provenance(
        agents / "specials.planner-agent",
        extra={"note": "Imported into CASOPS as baseline_safe.", "pack_id": "specials"},
    )
    _write_provenance(agents / "video.director")
    _write_provenance(agents / "video.archivemaster")
    health = _write_provenance(
        agents / "common.health", extra={"note": "Sample. No external sources."}
    )

    report = attach_book_of_knowledge(book, agents)
    assert report.parsed_agents == 3
    assert report.written == (
        "specials.planner-agent",
        "video.archivemaster",
        "video.director",
    )
    assert report.skipped_unlisted == ("common.health",)
    assert report.missing_folders == ()
    assert report.count_mismatches == ()

    payload = json.loads(planner.read_text(encoding="utf-8"))
    assert payload["note"] == "Imported into CASOPS as baseline_safe."
    assert payload["pack_id"] == "specials"
    assert payload["imported_from"] == "src"
    assert payload["schema_version"] == "3.0"
    assert len(payload["sources"]) == 2
    assert payload["sources"][0]["isbn13"] == "9780201835953"
    assert payload["reference_book_origin"] == ORIGIN
    health_payload = json.loads(health.read_text(encoding="utf-8"))
    assert health_payload["sources"] == []
    assert "reference_book_origin" not in health_payload

    again = attach_book_of_knowledge(book, agents)
    assert again.written == report.written
    again_payload = json.loads(planner.read_text(encoding="utf-8"))
    assert [s["isbn13"] for s in again_payload["sources"]] == [
        s["isbn13"] for s in payload["sources"]
    ]


def test_attach_skips_missing_folder(tmp_path: Path) -> None:
    book = tmp_path / "book.md"
    book.write_text(SAMPLE, encoding="utf-8")
    agents = tmp_path / "agents"
    agents.mkdir()
    report = attach_book_of_knowledge(book, agents)
    assert set(report.missing_folders) == {
        "specials.planner-agent",
        "video.director",
        "video.archivemaster",
    }
    assert report.written == ()
