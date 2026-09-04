"""Repo-relative path helpers. Do not record C:\\Project\\... in config."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VENDOR = REPO / "vendor"
VENDOR_SWARM_OPS = VENDOR / "common-agent-swarm-ops"
VENDOR_VA = VENDOR / "va-agent-swarm"
VENDOR_API_TEST = VENDOR_SWARM_OPS / "testcases" / "api_test"
VENDOR_VIDEO_AGENTS = VENDOR_SWARM_OPS / "business" / "video" / "agents"
VENDOR_SPECIALS_AGENTS = VENDOR_SWARM_OPS / "business" / "specials" / "agents"

HISTORICAL_ROOTS: tuple[tuple[str, str], ...] = (
    (r"C:\Project\common-agent-structure", "."),
    (r"C:/Project/common-agent-structure", "."),
    (r"C:\Project\common-agent-swarm-ops", "vendor/common-agent-swarm-ops"),
    (r"C:/Project/common-agent-swarm-ops", "vendor/common-agent-swarm-ops"),
    (r"C:\Project\va-agent-swarm", "vendor/va-agent-swarm"),
    (r"C:/Project/va-agent-swarm", "vendor/va-agent-swarm"),
)


def repo_posix(path: Path | str, *, root: Path = REPO) -> str:
    raw = Path(path)
    try:
        resolved = raw.resolve()
        base = root.resolve()
        return resolved.relative_to(base).as_posix()
    except (OSError, ValueError):
        text = str(path).replace("\\", "/")
        lowered = text.lower()
        for old, new in HISTORICAL_ROOTS:
            needle = old.replace("\\", "/").lower()
            if lowered.startswith(needle):
                rest = text[len(old) :].lstrip("/\\")
                return f"{new}/{rest}".replace("\\", "/").replace("./", "", 1) if rest else new
        return text


def rewrite_historical_text(text: str) -> str:
    out = text
    for old, new in HISTORICAL_ROOTS:
        out = out.replace(old, new)
        out = out.replace(old.replace("\\", "/"), new)
        out = out.replace(old.replace("\\", "\\\\"), new)
    out = out.replace("vendor/common-agent-swarm-ops\\", "vendor/common-agent-swarm-ops/")
    out = out.replace("vendor/va-agent-swarm\\", "vendor/va-agent-swarm/")
    out = out.replace(".\\", "./")

    def _posix_vendor(match: re.Match[str]) -> str:
        return match.group(0).replace("\\", "/")

    out = re.sub(r"vendor/common-agent-swarm-ops[\\/][^\s`\"']+", _posix_vendor, out)
    out = re.sub(r"vendor/va-agent-swarm[\\/][^\s`\"']+", _posix_vendor, out)
    return out
