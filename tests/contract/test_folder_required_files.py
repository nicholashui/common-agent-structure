"""Folder contract required-file matrix from spec §5.2."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from casops.registry.folder import validate_required_files

REPO = Path(__file__).resolve().parents[2]
TEMPLATE = REPO / "agents" / "_template_v3"
HEALTH = REPO / "agents" / "common.health"
SCHEMA = REPO / "schemas" / "agent" / "agent_spec.schema.json"

ALWAYS_REQUIRED_FILES = (
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


def test_template_agent_has_all_always_required_files() -> None:
    result = validate_required_files(TEMPLATE)
    assert result.ok, result.missing
    for relative in ALWAYS_REQUIRED_FILES:
        assert (TEMPLATE / relative).is_file(), relative
    assert (TEMPLATE / "evals" / "regression").is_dir()


def test_template_agent_spec_matches_schema() -> None:
    spec = json.loads((TEMPLATE / "agent_spec.json").read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.validate(spec, schema)
    assert spec["schema_version"] == "3.0"
    assert spec["structure_id"] == "casops.common_agent.v3"
    assert spec["model_policy"]["provider"] == "local_deterministic"
    assert spec["model_policy"]["network_access"] is False
    assert spec["production_activation_requested"] is False


def test_template_is_baseline_safe_disabled_modes() -> None:
    memory = json.loads((TEMPLATE / "memory" / "policy.json").read_text(encoding="utf-8"))
    plugins = json.loads((TEMPLATE / "plugins" / "registry.json").read_text(encoding="utf-8"))
    improvement = json.loads(
        (TEMPLATE / "improvement" / "policy.json").read_text(encoding="utf-8")
    )
    compute = json.loads(
        (TEMPLATE / "runtime" / "compute_controller.json").read_text(encoding="utf-8")
    )
    cache = json.loads((TEMPLATE / "runtime" / "cache.json").read_text(encoding="utf-8"))
    assert memory["mode"] == "none"
    assert plugins["plugins"] == []
    assert improvement["mode"] in {"disabled", "propose"}
    assert improvement.get("auto_promote", False) is False
    assert compute["mode"] == "fixed"
    assert cache["tiers"] == ["T0"]


def test_common_health_agent_has_all_always_required_files() -> None:
    result = validate_required_files(HEALTH)
    assert result.ok, result.missing
    spec = json.loads((HEALTH / "agent_spec.json").read_text(encoding="utf-8"))
    jsonschema.validate(spec, json.loads(SCHEMA.read_text(encoding="utf-8")))
    assert spec["agent_id"] == "common.health"
    assert spec["role"] == "HostHealthObserver"
    assert spec["production_activation_requested"] is False
    assert spec["model_policy"]["network_access"] is False
    memory = json.loads((HEALTH / "memory" / "policy.json").read_text(encoding="utf-8"))
    plugins = json.loads((HEALTH / "plugins" / "registry.json").read_text(encoding="utf-8"))
    execution = json.loads((HEALTH / "runtime" / "execution.json").read_text(encoding="utf-8"))
    assert memory["mode"] == "none"
    assert plugins["plugins"] == []
    assert execution["nodes"][0]["kind"] == "transform"
    assert execution["nodes"][0]["op"] == "health_snapshot"


def test_missing_readme_fails_closed() -> None:
    result = validate_required_files(REPO / "does-not-exist")
    assert result.ok is False
    assert "agent_spec.json" in result.missing


@pytest.mark.parametrize("relative", ALWAYS_REQUIRED_FILES)
def test_always_required_path_is_named_in_spec_matrix(relative: str) -> None:
    assert relative in ALWAYS_REQUIRED_FILES
