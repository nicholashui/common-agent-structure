"""Plugin validation must not execute plugin code."""

from __future__ import annotations

from pathlib import Path

import pytest

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.plugins.validate import validate_manifest, validate_registry

REPO = Path(__file__).resolve().parents[2]


def test_template_registry_validates_without_exec() -> None:
    result = validate_registry(REPO / "agents" / "_template_v3")
    assert result["count"] == 0


def test_python_module_pointer_is_not_imported(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    imported: list[str] = []
    real_import = __import__

    def tracking_import(name, *args, **kwargs):
        imported.append(name)
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr("builtins.__import__", tracking_import)
    payload = {"id": "evil", "isolation": "I0", "module": "this_should_not_be_imported_xyz"}
    result = validate_manifest(payload, folder=tmp_path)
    assert result["executed"] is False
    assert "this_should_not_be_imported_xyz" not in imported


def test_i3_manifest_validates_without_executing() -> None:
    result = validate_manifest({"id": "net", "isolation": "I3", "permissions": {"network": True}})
    assert result["executed"] is False
    assert result["isolation"] == "I3"


def test_manifest_path_outside_agent_folder_is_not_read(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    outside = tmp_path / "secret.json"
    outside.write_text('{"stolen": true}', encoding="utf-8")
    agent = tmp_path / "agent"
    agent.mkdir()
    reads: list[Path] = []
    real_read = Path.read_text

    def tracking_read(self: Path, *args: object, **kwargs: object) -> str:
        reads.append(Path(self).resolve())
        return real_read(self, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", tracking_read)
    with pytest.raises(CasopsError) as raised:
        validate_manifest(
            {"id": "leak", "isolation": "I0", "manifest": "../secret.json"},
            folder=agent,
        )
    assert raised.value.code == ErrorCode.PLG_MANIFEST_INVALID
    assert outside.resolve() not in reads
    with pytest.raises(CasopsError):
        validate_manifest(
            {"id": "abs", "isolation": "I0", "manifest": str(outside)},
            folder=agent,
        )
    assert outside.resolve() not in reads
