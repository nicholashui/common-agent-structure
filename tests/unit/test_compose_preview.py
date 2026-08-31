"""Compose preview is a dry run: findings + prospective lock, no lock files."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from casops.auth.actors import ActorClass
from casops.compose.engine import Composer, LOCK_NAMES
from casops.corrigibility.store import InvariantStore

REPO = Path(__file__).resolve().parents[2]
TEMPLATE = REPO / "agents" / "_template_v3"


def _copy_template(tmp_path: Path, name: str = "casops.template.baseline_safe") -> Path:
    target = tmp_path / name
    shutil.copytree(TEMPLATE, target)
    spec_path = target / "agent_spec.json"
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    spec["agent_id"] = name
    spec_path.write_text(json.dumps(spec, indent=2), encoding="utf-8")
    return target


def test_preview_does_not_write_locks(tmp_path: Path) -> None:
    _copy_template(tmp_path)
    composer = Composer(agents_root=tmp_path, store=InvariantStore.with_host_defaults())
    result = composer.preview("casops.template.baseline_safe")
    generated = tmp_path / "casops.template.baseline_safe" / "generated"
    assert not generated.exists()
    assert result.lock["compose_hash"] == result.compose_hash
    for field in (
        "child_hash",
        "parent_hashes",
        "mro",
        "skill_resolution",
        "corrigibility_invariant_digest",
        "compose_hash",
    ):
        assert field in result.lock
    assert result.findings
    assert result.errors == []


def test_compose_writes_all_five_locks_transactionally(tmp_path: Path) -> None:
    _copy_template(tmp_path)
    composer = Composer(agents_root=tmp_path, store=InvariantStore.with_host_defaults())
    composer.compose("casops.template.baseline_safe", actor=ActorClass.host_service)
    generated = tmp_path / "casops.template.baseline_safe" / "generated"
    for name in LOCK_NAMES:
        assert (generated / name).is_file()


def test_input_change_changes_compose_hash(tmp_path: Path) -> None:
    _copy_template(tmp_path)
    composer = Composer(agents_root=tmp_path, store=InvariantStore.with_host_defaults())
    before = composer.preview("casops.template.baseline_safe").compose_hash
    spec_path = tmp_path / "casops.template.baseline_safe" / "agent_spec.json"
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    spec["role"] = "changed"
    spec_path.write_text(json.dumps(spec, indent=2), encoding="utf-8")
    after = composer.preview("casops.template.baseline_safe").compose_hash
    assert before != after
