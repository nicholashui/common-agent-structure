"""Compose capability matrix for the template agent."""

from __future__ import annotations

from pathlib import Path

from casops.capabilities.conformance import CapabilityStatus, verify_folder
from casops.compose.engine import Composer
from casops.corrigibility.store import InvariantStore

REPO = Path(__file__).resolve().parents[2]


def test_template_local_deterministic_is_verified() -> None:
    matrix = verify_folder(REPO / "agents" / "_template_v3")
    statuses = {item["capability"]: item["status"] for item in matrix["matrix"]}
    assert statuses["model.local_deterministic"] == CapabilityStatus.VERIFIED.value


def test_preview_lock_contains_capability_matrix() -> None:
    composer = Composer(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults())
    result = composer.preview("casops.template.baseline_safe")
    matrix = result.lock["verified_capability_matrix"]
    assert matrix["matrix"]
    assert "verify_capabilities" in result.steps
    assert "validate_plugins" in result.steps
