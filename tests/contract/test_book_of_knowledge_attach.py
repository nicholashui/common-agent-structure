"""Every video.* and specials.* folder carries Book of Knowledge references."""

from __future__ import annotations

import json
from pathlib import Path

from casops.registry.book_of_knowledge import ORIGIN, parse_book_of_knowledge_path

REPO = Path(__file__).resolve().parents[2]
BOOK = REPO / "spec" / "book_of_knowledge.md"
AGENTS = REPO / "agents"
UNLISTED = {"_template_v3", "common.health"}


def test_book_of_knowledge_covers_specials_and_video_packs() -> None:
    catalog = parse_book_of_knowledge_path(BOOK)
    specials = sorted(k for k in catalog if k.startswith("specials."))
    video = sorted(k for k in catalog if k.startswith("video."))
    assert len(specials) == 19
    assert len(video) == 114
    assert len(catalog) == 133
    for agent_id, books in catalog.items():
        assert books, agent_id
        isbns = [item["isbn13"] for item in books]
        assert len(isbns) == len(set(isbns)), agent_id
        for item in books:
            assert item["kind"] == "reference_book"
            assert item["language"] in {"EN", "ZH"}
            assert item["title"]
            assert len(item["isbn13"]) == 13
            assert item["isbn13"].isdigit()
            assert item["origin"] == ORIGIN


def test_each_listed_agent_folder_has_matching_reference_books() -> None:
    catalog = parse_book_of_knowledge_path(BOOK)
    for agent_id, books in catalog.items():
        folder = AGENTS / agent_id
        path = folder / "sources" / "PROVENANCE.json"
        assert folder.is_dir(), agent_id
        payload = json.loads(path.read_text(encoding="utf-8"))
        attached = [
            item
            for item in payload.get("sources") or []
            if isinstance(item, dict) and item.get("origin") == ORIGIN
        ]
        expected = [item["isbn13"] for item in books]
        actual = [item["isbn13"] for item in attached]
        assert actual == expected, agent_id
        assert payload.get("imported_from") or payload.get("note")
        spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
        assert spec["model_policy"]["network_access"] is False
        assert spec["production_activation_requested"] is False


def test_unlisted_agents_do_not_receive_book_rows() -> None:
    for name in UNLISTED:
        payload = json.loads(
            (AGENTS / name / "sources" / "PROVENANCE.json").read_text(encoding="utf-8")
        )
        books = [
            item
            for item in payload.get("sources") or []
            if isinstance(item, dict) and item.get("origin") == ORIGIN
        ]
        assert books == [], name


def test_known_titles_land_on_matching_ids() -> None:
    catalog = parse_book_of_knowledge_path(BOOK)
    autotelic = {item["isbn13"] for item in catalog["specials.autotelic-agent"]}
    assert "9780374533557" in autotelic  # Thinking, Fast and Slow
    screenwriter = {item["isbn13"] for item in catalog["video.screenwriter"]}
    assert "9780060391683" in screenwriter  # Story (McKee)
    planner = json.loads(
        (AGENTS / "specials.planner-agent" / "sources" / "PROVENANCE.json").read_text(
            encoding="utf-8"
        )
    )
    titles = {item.get("title") for item in planner["sources"]}
    assert "The Mythical Man-Month" in titles
