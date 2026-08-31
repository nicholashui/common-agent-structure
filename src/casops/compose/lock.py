"""Compose lock document (spec §6.6)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from casops.contracts.canonical import sha256_file, sha256_json


def _file_hash(folder: Path, relative: str) -> str:
    path = folder / relative
    if path.is_file():
        return sha256_file(path)
    return ""


def _ref_hash(folder: Path, reference: str | None) -> str:
    if not reference:
        return ""
    path = folder / reference
    if path.is_file():
        return sha256_file(path)
    return sha256_json({"ref": reference})


def _regression_digest(folder: Path) -> str:
    directory = folder / "evals" / "regression"
    names = sorted(
        path.name
        for path in directory.iterdir()
        if path.is_file() and path.name != ".gitkeep"
    ) if directory.is_dir() else []
    return sha256_json({"fixtures": names})


def build_compose_lock(
    *,
    agent_id: str,
    folder: Path,
    mro: list[str],
    folders: dict[str, Path],
    merged: dict[str, Any],
    skill_resolution: dict[str, Any],
    corrigibility_digest: str,
    verified_capability_matrix: dict[str, Any] | None = None,
) -> dict[str, Any]:
    parent_hashes = [
        {
            "agent_id": parent_id,
            "hash": _file_hash(folders[parent_id], "agent_spec.json"),
        }
        for parent_id in mro[1:]
    ]
    body = {
        "schema_version": "3.0",
        "agent_id": agent_id,
        "child_hash": _file_hash(folder, "agent_spec.json"),
        "parent_hashes": parent_hashes,
        "mro": mro,
        "prompt_hashes": {
            "primary": _ref_hash(folder, merged.get("prompt_reference")),
        },
        "rubric_hashes": {
            "primary": _ref_hash(folder, merged.get("rubric_reference")),
        },
        "skill_resolution": skill_resolution,
        "cache_policy_hash": _file_hash(folder, "runtime/cache.json"),
        "context_policy_hash": _file_hash(folder, "runtime/context.json"),
        "compute_controller_hash": _file_hash(folder, "runtime/compute_controller.json"),
        "verified_capability_matrix": verified_capability_matrix or {},
        "tokenizer_digest": "",
        "chat_template_digest": "",
        "protocol_versions": {},
        "adapter_versions": {},
        "otel_schema_url": "",
        "plugin_digests": {},
        "isolation_tier_map": {},
        "plugin_sbom_digests": {},
        "memory_policy_hash": _file_hash(folder, "memory/policy.json"),
        "memory_hierarchy_hash": _file_hash(folder, "memory/hierarchy.json"),
        "memory_security_hash": _file_hash(folder, "memory/security.json"),
        "unlearning_hash": _file_hash(folder, "memory/unlearning.json"),
        "verifier_set_hash": _file_hash(folder, "improvement/verifiers.json"),
        "safety_hash": _file_hash(folder, "safety/policy.json"),
        "termination_hash": _file_hash(folder, "safety/termination.json"),
        "corrigibility_invariant_digest": corrigibility_digest,
        "analysis_plan_hash": _file_hash(folder, "evals/analysis_plan.json"),
        "regression_fixture_set_digest": _regression_digest(folder),
        "merged": merged,
    }
    compose_hash = sha256_json(body)
    return {**body, "compose_hash": compose_hash}
