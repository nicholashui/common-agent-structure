"""Copy per-agent docs into Control UI Help (public/docs/agents/<id>/).

User guide: markdown from agents/<id>/docs.
Spec: merge SPEC.md, agent_spec.json, prompts/, rubrics/, and sources/.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
AGENTS_ROOT = REPO / "agents"
OUT_ROOT = REPO / "ui" / "public" / "docs" / "agents"
TEXT_SUFFIXES = {".md", ".json", ".txt"}
DOC_MD_NAMES = ("user_guide.md", "USER_GUIDE.md", "guide.md")
SOURCE_CLIP = 8_000
EXCERPT_DIRS = {"excerpts", "study"}


def list_agent_folders(agents_root: Path = AGENTS_ROOT) -> list[Path]:
    folders: list[Path] = []
    for child in sorted(agents_root.iterdir()):
        if child.is_dir() and (child / "agent_spec.json").is_file():
            folders.append(child)
    return folders


def agent_id_of(folder: Path) -> str:
    try:
        payload = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        payload = {}
    raw = payload.get("agent_id") if isinstance(payload, dict) else None
    return str(raw or folder.name)


def _read(path: Path, clip: int | None = None) -> str:
    text = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    if clip is not None and len(text) > clip:
        return f"{text[:clip].rstrip()}\n\n…(clipped {len(text) - clip} characters from `{path.name}`)\n"
    return text if text.endswith("\n") else f"{text}\n"


def _fence(language: str, body: str) -> str:
    payload = body.rstrip()
    ticks = "```"
    while ticks in payload:
        ticks += "`"
    return f"{ticks}{language}\n{payload}\n{ticks}\n"


def _iter_files(folder: Path) -> list[Path]:
    if not folder.is_dir():
        return []
    files = [path for path in folder.rglob("*") if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES]
    return sorted(files, key=lambda item: item.as_posix().lower())


def build_userguide(folder: Path) -> str | None:
    docs = folder / "docs"
    if not docs.is_dir():
        return None
    markdown = [path for path in docs.iterdir() if path.is_file() and path.suffix.lower() == ".md"]
    markdown.sort(key=lambda item: (0 if item.name.lower() == "user_guide.md" else 1, item.name.lower()))
    if not markdown:
        return None
    parts = [f"> Copied from `{folder.name}/docs` for Help.\n"]
    if len(markdown) == 1 and markdown[0].name.lower() == "user_guide.md":
        parts.append(_read(markdown[0]))
        return "\n".join(parts).strip() + "\n"
    for path in markdown:
        parts.append(f"## `{path.name}`\n")
        parts.append(_read(path))
    return "\n".join(parts).strip() + "\n"


def _source_clip_for(path: Path, folder: Path) -> int | None:
    try:
        relative = path.relative_to(folder / "sources")
    except ValueError:
        return None
    if relative.parts and relative.parts[0] in EXCERPT_DIRS:
        return SOURCE_CLIP
    return None


def build_spec(folder: Path) -> str:
    agent_id = agent_id_of(folder)
    parts: list[str] = [
        f"# {agent_id} — Spec\n",
        (
            f"> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, "
            f"and `sources/` in `agents/{folder.name}/`.\n"
        ),
    ]
    spec_json = folder / "agent_spec.json"
    if spec_json.is_file():
        parts.append("## Host contract (`agent_spec.json`)\n")
        try:
            payload = json.loads(spec_json.read_text(encoding="utf-8"))
            body = json.dumps(payload, indent=2, ensure_ascii=False)
        except (OSError, json.JSONDecodeError):
            body = _read(spec_json)
        parts.append(_fence("json", body))
    spec_md = folder / "SPEC.md"
    if spec_md.is_file():
        parts.append("## Folder specification (`SPEC.md`)\n")
        parts.append(_read(spec_md))
    for label, sub in (("Prompts", "prompts"), ("Rubrics", "rubrics")):
        files = _iter_files(folder / sub)
        if not files:
            continue
        parts.append(f"## {label}\n")
        for path in files:
            rel = path.relative_to(folder).as_posix()
            parts.append(f"### `{rel}`\n")
            text = _read(path)
            if path.suffix.lower() == ".json":
                parts.append(_fence("json", text))
            elif path.suffix.lower() == ".md":
                parts.append(text)
            else:
                parts.append(_fence("text", text))
    source_files = _iter_files(folder / "sources")
    skip_generic = f"sources/generic/{agent_id}.SPEC.md".lower()
    if source_files:
        parts.append("## Sources\n")
        for path in source_files:
            rel = path.relative_to(folder).as_posix()
            if rel.lower() == skip_generic:
                parts.append(f"### `{rel}`\n")
                parts.append("Omitted here; same document as `SPEC.md` above.\n")
                continue
            clip = _source_clip_for(path, folder)
            parts.append(f"### `{rel}`\n")
            text = _read(path, clip)
            if path.suffix.lower() == ".json":
                parts.append(_fence("json", text))
            elif path.suffix.lower() == ".md":
                parts.append(text)
            else:
                parts.append(_fence("text", text))
    return "\n".join(parts).strip() + "\n"


def write_agent_docs(folder: Path, out_root: Path = OUT_ROOT) -> dict[str, Path]:
    agent_id = agent_id_of(folder)
    dest = out_root / agent_id
    dest.mkdir(parents=True, exist_ok=True)
    written: dict[str, Path] = {}
    spec_text = build_spec(folder)
    spec_path = dest / "spec.md"
    spec_path.write_text(spec_text, encoding="utf-8")
    written["spec"] = spec_path
    guide = build_userguide(folder)
    if guide:
        guide_path = dest / "userguide.md"
        guide_path.write_text(guide, encoding="utf-8")
        written["userguide"] = guide_path
    docs = folder / "docs"
    if docs.is_dir():
        for asset in docs.iterdir():
            if asset.is_file() and asset.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
                target = dest / asset.name
                target.write_bytes(asset.read_bytes())
                written[f"asset:{asset.name}"] = target
    return written


def generate_all(agents_root: Path = AGENTS_ROOT, out_root: Path = OUT_ROOT) -> int:
    count = 0
    for folder in list_agent_folders(agents_root):
        write_agent_docs(folder, out_root)
        count += 1
    return count


def main() -> int:
    count = generate_all()
    print(f"Wrote Help docs for {count} agents under {OUT_ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
