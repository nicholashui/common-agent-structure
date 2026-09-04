"""Config, tools, and tests must not hardcode C:\\Project\\... or sibling file links."""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FORBIDDEN = ("C:\\Project\\", "C:/Project/", "C:\\\\Project\\\\")
SCAN_DIRS = ("src", "tests", "scripts", "ui/src", "tools")
SCAN_FILES = ("user_guide.v1.md", "ui/README.md")
ALLOW_FILES = {
    "tools/reloc.py",  # translation table of historical prefixes
    "tools/rewrite_relocatable_paths.py",  # detects historical prefixes
    "tests/contract/test_relocatable_paths.py",
    "issues/issue0004.md",
}


def _iter_scan() -> list[Path]:
    rows: list[Path] = []
    for name in SCAN_DIRS:
        root = REPO / name
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".py", ".ts", ".tsx", ".ps1", ".md", ".json"}:
                continue
            if "__pycache__" in path.parts or "node_modules" in path.parts:
                continue
            rows.append(path)
    for name in SCAN_FILES:
        path = REPO / name
        if path.is_file():
            rows.append(path)
    return rows


def test_vendor_copies_exist_and_are_real_directories() -> None:
    api_test = REPO / "vendor" / "common-agent-swarm-ops" / "testcases" / "api_test"
    video = REPO / "vendor" / "common-agent-swarm-ops" / "business" / "video" / "agents"
    specials = REPO / "vendor" / "common-agent-swarm-ops" / "business" / "specials" / "agents"
    redesign = REPO / "vendor" / "common-agent-swarm-ops" / "docs" / "special_agents_redesign"
    va = REPO / "vendor" / "va-agent-swarm"
    for folder in (api_test, video, specials, redesign, va):
        assert folder.is_dir(), folder
        assert not folder.is_symlink(), folder
    assert (api_test / "video.director" / "cases.json").is_file()
    assert (video / "video.director" / "agent_spec.json").is_file()
    assert any(video.iterdir())
    assert any(specials.iterdir())
    manifest = REPO / "vendor" / "MANIFEST.json"
    assert manifest.is_file()
    text = manifest.read_text(encoding="utf-8")
    assert "C:\\Project\\" not in text
    assert "C:/Project/" not in text


def test_runtime_and_tools_do_not_hardcode_project_drive() -> None:
    hits: list[str] = []
    for path in _iter_scan():
        rel = path.relative_to(REPO).as_posix()
        if rel in ALLOW_FILES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for needle in FORBIDDEN:
            if needle in text:
                hits.append(f"{rel}: {needle}")
                break
    assert hits == []


def test_characterization_provenance_is_repo_relative() -> None:
    bad: list[str] = []
    for spec in (REPO / "agents").glob("*/agent_spec.json"):
        folder = spec.parent
        proven = folder / "evals" / "fixtures" / "provenance.json"
        if proven.is_file():
            text = proven.read_text(encoding="utf-8")
            if "C:\\Project\\" in text or "C:/Project/" in text:
                bad.append(f"{folder.name}:provenance")
        for chat in (folder / "evals" / "fixtures").glob("chat-tc*.json"):
            payload = chat.read_text(encoding="utf-8")
            if "C:\\Project\\" in payload or "C:/Project/" in payload:
                bad.append(f"{folder.name}:{chat.name}")
        background = folder / "identity" / "background.json"
        if background.is_file():
            text = background.read_text(encoding="utf-8")
            if "C:\\Project\\" in text or "C:/Project/" in text:
                bad.append(f"{folder.name}:background")
    assert bad == []
