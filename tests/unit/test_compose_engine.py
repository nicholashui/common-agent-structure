"""Compose algorithm: attest at step 2, deterministic compose_hash, no partial locks."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from casops.auth.actors import ActorClass
from casops.compose.engine import Composer
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

REPO = Path(__file__).resolve().parents[2]
TEMPLATE = REPO / "agents" / "_template_v3"


def test_attestation_runs_before_mro(tmp_path: Path) -> None:
    target = tmp_path / "casops.template.baseline_safe"
    shutil.copytree(TEMPLATE, target)
    steps: list[str] = []
    store = InvariantStore.with_host_defaults()
    original_attest = store.attest

    def tracking_attest(**kwargs):
        steps.append("attest_invariants")
        return original_attest(**kwargs)

    store.attest = tracking_attest  # type: ignore[method-assign]
    composer = Composer(agents_root=tmp_path, store=store)
    result = composer.preview("casops.template.baseline_safe")
    assert result.steps[0] == "validate_folder"
    assert result.steps[1] == "attest_invariants"
    assert steps == ["attest_invariants"]
    assert "resolve_mro" in result.steps
    assert result.steps.index("attest_invariants") < result.steps.index("resolve_mro")


def test_repeated_preview_yields_identical_compose_hash(tmp_path: Path) -> None:
    target = tmp_path / "casops.template.baseline_safe"
    shutil.copytree(TEMPLATE, target)
    composer = Composer(agents_root=tmp_path, store=InvariantStore.with_host_defaults())
    first = composer.preview("casops.template.baseline_safe")
    second = composer.preview("casops.template.baseline_safe")
    assert first.compose_hash == second.compose_hash
    assert len(first.compose_hash) == 64


def test_cycle_writes_no_locks(tmp_path: Path) -> None:
    shutil.copytree(TEMPLATE, tmp_path / "a")
    shutil.copytree(TEMPLATE, tmp_path / "b")
    for agent_id, parent in (("a", "b"), ("b", "a")):
        spec_path = tmp_path / agent_id / "agent_spec.json"
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        spec["agent_id"] = agent_id
        spec_path.write_text(json.dumps(spec, indent=2), encoding="utf-8")
        parents = tmp_path / agent_id / "inheritance" / "parents.json"
        parents.write_text(json.dumps({"parents": [{"agent_id": parent, "priority": 0}]}), encoding="utf-8")
    composer = Composer(agents_root=tmp_path, store=InvariantStore.with_host_defaults())
    with pytest.raises(CasopsError) as raised:
        composer.compose("a", actor=ActorClass.host_service)
    assert raised.value.code == ErrorCode.INH_CYCLE
    assert not (tmp_path / "a" / "generated" / "compose.lock.json").exists()


def test_mismatch_attestation_does_not_continue(tmp_path: Path) -> None:
    target = tmp_path / "casops.template.baseline_safe"
    shutil.copytree(TEMPLATE, target)
    store = InvariantStore.with_host_defaults()

    def bad_attest(**kwargs):
        raise CasopsError(ErrorCode.IMP_CORRIGIBILITY)

    store.attest = bad_attest  # type: ignore[method-assign]
    composer = Composer(agents_root=tmp_path, store=store)
    with pytest.raises(CasopsError) as raised:
        composer.preview("casops.template.baseline_safe")
    assert raised.value.code == ErrorCode.IMP_CORRIGIBILITY
    assert raised.value.containment_required is True
