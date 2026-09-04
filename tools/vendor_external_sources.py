"""Copy sibling external trees into vendor/. Copies, not junctions.

Reads historical sibling checkouts only as a one-time source. After copy,
importers and tests must use vendor/ relative to this repo.
Skips media suffixes the agent importer already ignores.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from reloc import REPO, VENDOR, VENDOR_SWARM_OPS, VENDOR_VA

SKIP_SUFFIXES = {".mp3", ".wav", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".webm"}
SKIP_DIR_NAMES = {".git", "__pycache__", "node_modules", ".venv"}

# Sibling checkouts next to this repo (../common-agent-swarm-ops). Never required at runtime.
SIBLING_SWARM_OPS = REPO.parent / "common-agent-swarm-ops"
SIBLING_VA = REPO.parent / "va-agent-swarm"

TREES: tuple[tuple[str, Path, Path], ...] = (
    ("testcases/api_test", SIBLING_SWARM_OPS / "testcases" / "api_test", VENDOR_SWARM_OPS / "testcases" / "api_test"),
    (
        "business/video/agents",
        SIBLING_SWARM_OPS / "business" / "video" / "agents",
        VENDOR_SWARM_OPS / "business" / "video" / "agents",
    ),
    (
        "business/specials/agents",
        SIBLING_SWARM_OPS / "business" / "specials" / "agents",
        VENDOR_SWARM_OPS / "business" / "specials" / "agents",
    ),
    (
        "docs/special_agents_redesign",
        SIBLING_SWARM_OPS / "docs" / "special_agents_redesign",
        VENDOR_SWARM_OPS / "docs" / "special_agents_redesign",
    ),
    ("va-agent-swarm", SIBLING_VA, VENDOR_VA),
)


def copy_tree(src: Path, dest: Path) -> int:
    copied = 0
    dest.mkdir(parents=True, exist_ok=True)
    for path in src.rglob("*"):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.is_dir():
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        rel = path.relative_to(src)
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied += 1
    return copied


def write_manifest() -> None:
    VENDOR.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema_version": "casops.vendor.v1",
        "note": (
            "Byte copies of external trees this host needs. Not junctions, not git "
            "submodules, not runtime file links. Tools read these relative to the repo root."
        ),
        "trees": [
            {
                "key": key,
                "dest": dest.relative_to(REPO).as_posix(),
                "present": dest.is_dir(),
            }
            for key, _src, dest in TREES
        ],
        "skipped_media_suffixes": sorted(SKIP_SUFFIXES),
    }
    (VENDOR / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    readme = VENDOR / "README.md"
    if not readme.is_file():
        readme.write_text(
            "# Vendor copies\n\n"
            "Self-contained copies of external sources. **Not file links.**\n\n"
            "- `common-agent-swarm-ops/` — api_test cases and pack agent folders used by import tools.\n"
            "- `va-agent-swarm/` — design corpus previously cited by agent user guides (untrusted provenance).\n\n"
            "Refresh (only if a sibling checkout still exists on this machine):\n\n"
            "```powershell\n"
            "python tools/vendor_external_sources.py\n"
            "```\n",
            encoding="utf-8",
        )


def main() -> None:
    write_manifest()
    for key, src, dest in TREES:
        if dest.is_dir() and any(dest.rglob("*")):
            if not src.is_dir():
                print(f"keep {key}: vendor already present, sibling missing")
                continue
        if not src.is_dir():
            if dest.is_dir():
                print(f"keep {key}: sibling missing, using existing vendor copy")
                continue
            raise SystemExit(f"missing source for {key}: {src} (and no vendor copy at {dest})")
        if dest.exists():
            shutil.rmtree(dest)
        n = copy_tree(src, dest)
        print(f"copied {n} files {key} -> {dest.relative_to(REPO).as_posix()}")
    write_manifest()
    print(f"vendor ready under {VENDOR.relative_to(REPO).as_posix()}")


if __name__ == "__main__":
    main()
