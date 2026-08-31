"""Compose algorithm (spec §17.1). Step 2 is invariant attestation."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from casops.artifacts.atomic import atomic_write
from casops.auth.actors import ActorClass
from casops.compose.fixtures import check_fixture_monotonicity
from casops.compose.folders import locate_agent_folder
from casops.compose.identity import validate_identity
from casops.compose.lock import build_compose_lock
from casops.compose.merge import merge_specs
from casops.compose.mro import resolve_mro
from casops.capabilities.conformance import verify_folder
from casops.compose.skills import resolve_skills
from casops.plugins.validate import validate_registry
from casops.contracts.canonical import canonical_dumps, sha256_json
from casops.corrigibility.checkpoints import Checkpoint
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.registry.folder import validate_required_files

LOCK_NAMES = (
    "compose.lock.json",
    "capabilities.lock.json",
    "benchmark-baseline.json",
    "compatibility-matrix.lock.json",
    "context-budget.lock.json",
)


@dataclass
class ComposeResult:
    steps: list[str] = field(default_factory=list)
    compose_hash: str = ""
    mro: list[str] = field(default_factory=list)
    lock: dict[str, Any] = field(default_factory=dict)
    findings: list[str] = field(default_factory=list)
    errors: list[dict[str, str]] = field(default_factory=list)
    wrote_locks: bool = False


class Composer:
    def __init__(self, *, agents_root: Path, store: InvariantStore) -> None:
        self.agents_root = agents_root
        self.store = store

    def preview(self, agent_id: str) -> ComposeResult:
        return self._run(agent_id, persist=False)

    def compose(self, agent_id: str, *, actor: ActorClass) -> ComposeResult:
        del actor
        return self._run(agent_id, persist=True)

    def resolve_folder(self, agent_id: str) -> Path:
        located = locate_agent_folder(self.agents_root, agent_id)
        if located is None:
            raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail=f"unknown agent_id {agent_id}")
        return located

    def _run(self, agent_id: str, persist: bool) -> ComposeResult:
        result = ComposeResult()
        folder = self.resolve_folder(agent_id)

        result.steps.append("validate_folder")
        check = validate_required_files(folder)
        if not check.ok:
            raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail=f"missing {check.missing}")
        result.findings.append("folder validated")

        result.steps.append("attest_invariants")
        presented = _folder_invariant_digest(folder)
        self.store.attest(
            actor=ActorClass.host_service,
            presented_digest=presented,
            checkpoint=Checkpoint.compose,
            agent_id=agent_id,
        )
        result.findings.append("invariants attested")

        result.steps.append("validate_identity")
        validate_identity(folder)

        result.steps.append("resolve_mro")
        result.mro = resolve_mro(
            folder,
            self.agents_root,
            locate=lambda item: locate_agent_folder(self.agents_root, item),
        )
        folders = {item: self.resolve_folder(item) for item in result.mro}
        parent_folders = [folders[item] for item in result.mro[1:]]
        result.findings.append("mro=" + ",".join(result.mro))

        result.steps.append("merge")
        specs = [_load_spec(folders[item]) for item in result.mro]
        merged = merge_specs(specs[0], specs[1:])

        result.steps.append("resolve_skills")
        skills = resolve_skills([folders[item] for item in result.mro])

        result.steps.append("fixture_monotonicity")
        check_fixture_monotonicity(folder, parent_folders)

        result.steps.append("verify_capabilities")
        matrix = verify_folder(folder)
        result.findings.append("capabilities=" + str(matrix.get("production_bindable")))

        result.steps.append("validate_plugins")
        plugins = validate_registry(folder)
        result.findings.append(f"plugins_validated={plugins['count']}")

        result.lock = build_compose_lock(
            agent_id=agent_id,
            folder=folder,
            mro=result.mro,
            folders=folders,
            merged=merged,
            skill_resolution=skills,
            corrigibility_digest=presented,
            verified_capability_matrix=matrix,
        )
        result.compose_hash = result.lock["compose_hash"]

        if persist:
            generated = folder / "generated"
            written: list[Path] = []
            try:
                for name in LOCK_NAMES:
                    payload = (
                        result.lock
                        if name == "compose.lock.json"
                        else {
                            "schema_version": "3.0",
                            "agent_id": agent_id,
                            "compose_hash": result.compose_hash,
                        }
                    )
                    path = generated / name
                    atomic_write(path, canonical_dumps(payload) + "\n")
                    written.append(path)
            except Exception:
                for path in written:
                    if path.exists():
                        path.unlink()
                raise
            result.wrote_locks = True
            result.findings.append("locks written atomically")
        else:
            result.findings.append("preview: no locks written")
        return result


def _load_spec(folder: Path) -> dict[str, Any]:
    return json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))


def _folder_invariant_digest(folder: Path) -> str:
    payload = json.loads((folder / "corrigibility" / "invariants.json").read_text(encoding="utf-8"))
    return sha256_json({"invariants": payload.get("invariants")})
