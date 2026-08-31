"""Real I1–I3 isolation: WASM capabilities, no ambient network, no host FS, allow-listed egress."""

from __future__ import annotations

from pathlib import Path

import pytest

from casops.auth.handles import HandleBroker
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.plugins.i1_wasm import CAP_WAT, IDENTITY_WAT, I1Runtime
from casops.plugins.i2_process import I2Runtime
from casops.plugins.i3_guest import I3Runtime
from casops.plugins.runtime import execute_plugin
from casops.plugins.validate import validate_manifest


def test_i1_wasm_transform_and_capability_handle() -> None:
    payload = b"abcd"
    identity = I1Runtime().run(IDENTITY_WAT, payload)
    assert identity.output == payload
    assert identity.mechanism == "wasmtime"
    broker = HandleBroker()
    handle = broker.mint(audience="plugin", scope="transform")
    capped = I1Runtime(broker).run(CAP_WAT, payload, handle=handle)
    assert capped.output == payload
    with pytest.raises(CasopsError):
        broker.verify(handle, audience="plugin", scope="transform")


def test_i1_wasi_import_fails_closed() -> None:
    wat = '(module (import "wasi_snapshot_preview1" "fd_write" (func (param i32 i32 i32 i32) (result i32))))'
    with pytest.raises(CasopsError) as raised:
        I1Runtime().run(wat, b"x")
    assert raised.value.code == ErrorCode.PLG_ISOLATION_TIER


def test_i2_process_has_no_ambient_network_or_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "should-not-leak")
    runtime = I2Runtime()
    result = runtime.run(IDENTITY_WAT, b"hello")
    assert result.executed is True
    assert result.output == b"hello"
    probe = runtime.probe_network("example.com", 443)
    assert probe["connected"] is False
    assert runtime.probe_env("AWS_SECRET_ACCESS_KEY") is None


def test_i3_cannot_read_host_fs_and_egress_is_allowlisted(tmp_path: Path) -> None:
    secret = tmp_path / "host-secret.txt"
    secret.write_text("credential", encoding="utf-8")
    sandbox = tmp_path / "sandbox"
    allowed = tmp_path / "sandbox" / "note.txt"
    runtime = I3Runtime(
        sandbox,
        allowlist={"example.test"},
        fixtures={"https://example.test/ok": b"proxied"},
    )
    allowed.parent.mkdir(parents=True, exist_ok=True)
    allowed.write_text("inside", encoding="utf-8")
    executed = runtime.run(IDENTITY_WAT, b"wasm")
    assert executed.mechanism == "isolated_guest"
    assert executed.output == b"wasm"
    denied = runtime.probe_fs(str(secret))
    assert denied.get("ok") is False
    inside = runtime.probe_fs(str(allowed))
    assert inside.get("ok") is True
    assert runtime.probe_network("8.8.8.8", 53)["connected"] is False
    ok = runtime.egress("https://example.test/ok")
    assert ok.get("ok") is True
    blocked = runtime.egress("https://evil.test/x")
    assert blocked.get("ok") is False


def test_third_party_cannot_run_below_i2() -> None:
    with pytest.raises(CasopsError) as raised:
        validate_manifest({"id": "ext", "isolation": "I1", "origin": "third_party", "signed": False})
    assert raised.value.code == ErrorCode.PLG_ISOLATION_TIER
    assert validate_manifest({"id": "ext", "isolation": "I2", "origin": "third_party", "signed": False})["executed"] is False


def test_network_plugin_requires_i3() -> None:
    with pytest.raises(CasopsError) as raised:
        validate_manifest({"id": "net", "isolation": "I2", "permissions": {"network": True}})
    assert raised.value.code == ErrorCode.PLG_ISOLATION_TIER
    assert validate_manifest({"id": "net", "isolation": "I3", "permissions": {"network": True}})["isolation"] == "I3"


def test_execute_plugin_does_not_silent_downgrade(tmp_path: Path) -> None:
    out = execute_plugin({"id": "p", "isolation": "I1"}, b"zz")
    assert out["tier"] == "I1"
    with pytest.raises(CasopsError):
        execute_plugin({"id": "p", "isolation": "I3"}, b"zz")
    out3 = execute_plugin({"id": "p", "isolation": "I3"}, b"zz", sandbox=tmp_path / "i3")
    assert out3["tier"] == "I3"
    assert out3["mechanism"] == "isolated_guest"
