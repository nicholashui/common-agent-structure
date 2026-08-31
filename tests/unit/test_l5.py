"""L5 research isolation: no production credentials, no production writes, signed rollback."""

from __future__ import annotations

from pathlib import Path

import pytest

from casops.auth.actors import ActorClass
from casops.corrigibility.signing import HostSigner
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.improvement.l5 import PRODUCTION_ENV_KEYS, ResearchIsolation


def _sandbox(tmp_path: Path) -> ResearchIsolation:
    root = tmp_path / "research"
    return ResearchIsolation(
        root=root,
        signer=HostSigner.generate(),
        approved_repos=(root / "writable",),
        production_root=tmp_path / "production",
    )


def test_l5_env_has_no_production_credentials(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "prod-secret")
    monkeypatch.setenv("CASOPS_PROFILE", "research_only")
    box = _sandbox(tmp_path)
    env = box.env()
    for key in PRODUCTION_ENV_KEYS:
        assert key not in env
    assert env["CASOPS_NETWORK"] == "disabled"
    assert env["CASOPS_PROFILE"] == "research_only"


def test_l5_cannot_write_production_or_forbidden_surfaces(tmp_path: Path) -> None:
    box = _sandbox(tmp_path)
    with pytest.raises(CasopsError) as raised:
        box.mutate("corrigibility/invariants.json", b"nope", actor=ActorClass.host_service)
    assert raised.value.code == ErrorCode.IMP_SCOPE
    with pytest.raises(CasopsError):
        box.mutate("..\\production\\agent.py", b"nope", actor=ActorClass.host_service)


def test_l5_mutate_rollback_and_never_promotes(tmp_path: Path) -> None:
    box = _sandbox(tmp_path)
    with pytest.raises(CasopsError) as denied:
        box.mutate("core.py", b"v2", actor=ActorClass.agent_runtime)
    assert denied.value.code == ErrorCode.IMP_SELF_APPROVAL
    record = box.mutate("core.py", b"v2", actor=ActorClass.independent_approver)
    assert (box.root / "writable" / "core.py").read_bytes() == b"v2"
    box.rollback(record, actor=ActorClass.independent_approver)
    assert (box.root / "writable" / "core.py").read_bytes() == b""
    with pytest.raises(CasopsError) as raised:
        box.promote_to_production(actor=ActorClass.independent_approver)
    assert raised.value.code == ErrorCode.IMP_SCOPE


def test_l5_storage_not_shared_with_production(tmp_path: Path) -> None:
    box = _sandbox(tmp_path)
    assert box.shares_storage_with(tmp_path / "production") is False
    assert box.shares_storage_with(box.root) is True
