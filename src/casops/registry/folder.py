"""Agent folder required-file matrix (spec §5.2)."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ALWAYS_REQUIRED_FILES: tuple[str, ...] = (
    "README.md",
    "SPEC.md",
    "agent_spec.json",
    "sources/PROVENANCE.json",
    "inheritance/parents.json",
    "skills/toggles.json",
    "runtime/execution.json",
    "runtime/backends.json",
    "runtime/routing.json",
    "runtime/cache.json",
    "runtime/context.json",
    "runtime/compute_controller.json",
    "protocols/compatibility.json",
    "protocols/capability_assertions.json",
    "observability/telemetry.json",
    "observability/redaction.json",
    "observability/sampling.json",
    "plugins/registry.json",
    "memory/policy.json",
    "improvement/policy.json",
    "safety/policy.json",
    "safety/termination.json",
    "corrigibility/invariants.json",
    "evals/benchmarks.json",
)

ALWAYS_REQUIRED_DIRS: tuple[str, ...] = ("evals/regression",)


@dataclass
class FolderCheck:
    ok: bool
    missing: list[str] = field(default_factory=list)


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def validate_required_files(agent_dir: Path) -> FolderCheck:
    missing: list[str] = []
    if not agent_dir.is_dir():
        missing.extend(ALWAYS_REQUIRED_FILES)
        missing.extend(f"{item}/" for item in ALWAYS_REQUIRED_DIRS)
        return FolderCheck(ok=False, missing=missing)

    for relative in ALWAYS_REQUIRED_FILES:
        if not (agent_dir / relative).is_file():
            missing.append(relative)
    for relative in ALWAYS_REQUIRED_DIRS:
        if not (agent_dir / relative).is_dir():
            missing.append(f"{relative}/")

    plugins = _read_json(agent_dir / "plugins" / "registry.json")
    if plugins and plugins.get("plugins"):
        if not (agent_dir / "plugins" / "isolation.json").is_file():
            missing.append("plugins/isolation.json")

    memory = _read_json(agent_dir / "memory" / "policy.json")
    if memory and memory.get("mode") not in {None, "none", "disabled"}:
        for extra in ("memory/hierarchy.json", "memory/security.json", "memory/unlearning.json"):
            if not (agent_dir / extra).is_file():
                missing.append(extra)

    improvement = _read_json(agent_dir / "improvement" / "policy.json")
    if improvement and improvement.get("mode") not in {None, "disabled"}:
        if not (agent_dir / "improvement" / "verifiers.json").is_file():
            missing.append("improvement/verifiers.json")

    persona = _read_json(agent_dir / "identity" / "persona.json")
    identity_mode = (persona or {}).get("mode", "grounded")
    if identity_mode != "grounded" and not (agent_dir / "identity" / "DISCLOSURE.md").is_file():
        missing.append("identity/DISCLOSURE.md")

    # unique, stable order
    ordered: list[str] = []
    for item in missing:
        if item not in ordered:
            ordered.append(item)
    return FolderCheck(ok=not ordered, missing=ordered)
