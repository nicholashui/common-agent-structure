"""Attach bibliographic reference books from spec/book_of_knowledge.md by agent id.

Entries are provenance records only. They do not enable network, RAG, T3,
plugins, memory writes, or production activation.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ORIGIN = "spec/book_of_knowledge.md"
KIND = "reference_book"
NOTE = (
    "Bibliographic references from spec/book_of_knowledge.md. "
    "Does not enable network, RAG, T3, plugins, or memory writes."
)

ROW_RE = re.compile(
    r"^\|\s*`(?P<agent_id>[a-z0-9][a-z0-9._-]*)`\s*\|(?P<books>.+)\|\s*(?P<count>\d+)\s*\|?\s*$",
    re.MULTILINE,
)
BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
LANG_RE = re.compile(r"^(EN|ZH)\s*[:：]\s*", re.IGNORECASE)
ISBN_RE = re.compile(r"ISBN-13\s+(\d{13})", re.IGNORECASE)
ISBN_TAIL_RE = re.compile(r"[,，]?\s*ISBN-13\s+(\d{13})\s*$", re.IGNORECASE)
EDITION_NOTE_RE = re.compile(r"\s+[—–-]\s+check latest ed\.?\s*$", re.IGNORECASE)
FW_AUTHOR_RE = re.compile(r"^(.*)（([^）]+)）\s*$")


@dataclass(frozen=True)
class AttachReport:
    parsed_agents: int
    written: tuple[str, ...]
    missing_folders: tuple[str, ...]
    skipped_unlisted: tuple[str, ...]
    book_count: int
    count_mismatches: tuple[tuple[str, int, int], ...]


def parse_book_of_knowledge(text: str) -> dict[str, list[dict[str, str]]]:
    """Parse markdown tables into `{agent_id: [source, ...]}` preserving row order."""
    catalog: dict[str, list[dict[str, str]]] = {}
    for match in ROW_RE.finditer(text):
        agent_id = match.group("agent_id")
        cell = match.group("books").strip().rstrip("|").strip()
        books = _parse_book_cell(cell)
        if not books:
            continue
        catalog[agent_id] = books
    return catalog


def parse_book_of_knowledge_path(path: Path) -> dict[str, list[dict[str, str]]]:
    return parse_book_of_knowledge(path.read_text(encoding="utf-8"))


def attach_book_of_knowledge(
    book_path: Path,
    agents_root: Path,
    *,
    missing_ok: bool = False,
) -> AttachReport:
    """Write matched reference books into each agent's sources/PROVENANCE.json."""
    if not book_path.is_file():
        if missing_ok:
            return AttachReport(0, (), (), (), 0, ())
        raise FileNotFoundError(book_path)
    catalog = parse_book_of_knowledge_path(book_path)
    mismatches: list[tuple[str, int, int]] = []
    text = book_path.read_text(encoding="utf-8")
    for match in ROW_RE.finditer(text):
        agent_id = match.group("agent_id")
        declared = int(match.group("count"))
        actual = len(catalog.get(agent_id, []))
        if declared != actual:
            mismatches.append((agent_id, declared, actual))

    written: list[str] = []
    missing: list[str] = []
    for agent_id, books in catalog.items():
        folder = agents_root / agent_id
        provenance_path = folder / "sources" / "PROVENANCE.json"
        if not folder.is_dir() or not provenance_path.is_file():
            missing.append(agent_id)
            continue
        _write_sources(provenance_path, books)
        written.append(agent_id)

    skipped = _unlisted_agent_folders(agents_root, set(catalog))
    return AttachReport(
        parsed_agents=len(catalog),
        written=tuple(sorted(written)),
        missing_folders=tuple(sorted(missing)),
        skipped_unlisted=tuple(sorted(skipped)),
        book_count=sum(len(v) for v in catalog.values()),
        count_mismatches=tuple(mismatches),
    )


def _parse_book_cell(cell: str) -> list[dict[str, str]]:
    parts = [p.strip().strip("\u3000").strip() for p in BR_RE.split(cell)]
    books: list[dict[str, str]] = []
    seen: set[str] = set()
    for part in parts:
        if not part:
            continue
        item = parse_book_entry(part)
        isbn = item["isbn13"]
        if isbn in seen:
            continue
        seen.add(isbn)
        books.append(item)
    return books


def parse_book_entry(raw: str) -> dict[str, str]:
    text = raw.strip().strip("\u3000").strip()
    lang_match = LANG_RE.match(text)
    language = lang_match.group(1).upper() if lang_match else "EN"
    rest = text[lang_match.end() :] if lang_match else text
    isbn_match = ISBN_TAIL_RE.search(rest) or ISBN_RE.search(rest)
    if isbn_match is None:
        raise ValueError(f"book entry missing ISBN-13: {text[:120]}")
    isbn13 = isbn_match.group(1)
    title_part = rest[: isbn_match.start()].strip().rstrip(" ,，").strip()
    title_part = EDITION_NOTE_RE.sub("", title_part).strip()
    title, author = _split_title_author(title_part)
    item: dict[str, str] = {
        "kind": KIND,
        "language": language,
        "title": title or text,
    }
    if author:
        item["author"] = author
    item["isbn13"] = isbn13
    item["origin"] = ORIGIN
    item["citation"] = text
    return item


def _split_title_author(title_part: str) -> tuple[str, str | None]:
    fw = FW_AUTHOR_RE.match(title_part)
    if fw and fw.group(1).strip():
        return fw.group(1).strip().rstrip(" ,，").strip(), fw.group(2).strip()
    if not title_part.endswith(")"):
        return title_part, None
    depth = 0
    for index in range(len(title_part) - 1, -1, -1):
        char = title_part[index]
        if char == ")":
            depth += 1
        elif char == "(":
            depth -= 1
            if depth == 0:
                author = title_part[index + 1 : -1].strip()
                title = title_part[:index].strip().rstrip(" ,，").strip()
                if title and author:
                    return title, author
                break
    return title_part, None


def _write_sources(path: Path, books: list[dict[str, str]]) -> None:
    payload: dict[str, Any] = {"schema_version": "3.0", "sources": []}
    if path.is_file():
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            loaded = None
        if isinstance(loaded, dict):
            payload.update(loaded)
    existing = payload.get("sources")
    kept: list[Any] = []
    if isinstance(existing, list):
        for item in existing:
            if isinstance(item, dict) and item.get("origin") == ORIGIN:
                continue
            kept.append(item)
    payload["schema_version"] = "3.0"
    payload["sources"] = kept + books
    payload["reference_book_origin"] = ORIGIN
    payload["reference_book_note"] = NOTE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _unlisted_agent_folders(agents_root: Path, listed: set[str]) -> list[str]:
    skipped: list[str] = []
    if not agents_root.is_dir():
        return skipped
    for child in agents_root.iterdir():
        if not child.is_dir() or not (child / "agent_spec.json").is_file():
            continue
        if child.name not in listed:
            skipped.append(child.name)
    return skipped
