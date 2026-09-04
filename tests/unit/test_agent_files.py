"""Confined agent config-folder listing and writes."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from casops.compose.files import (
    CONFIG_FOLDERS,
    confined_path,
    host_owned,
    list_config_files,
    normalize_rel,
    read_config_file,
    write_config_file,
)
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def _agent(tmp_path: Path) -> Path:
    folder = tmp_path / "demo.agent"
    (folder / "prompts").mkdir(parents=True)
    (folder / "prompts" / "primary.md").write_text("# hello\n", encoding="utf-8")
    (folder / "identity").mkdir()
    (folder / "identity" / "persona.json").write_text('{"role": "demo"}\n', encoding="utf-8")
    (folder / "corrigibility").mkdir()
    (folder / "corrigibility" / "attestation.json").write_text('{"status": "host"}\n', encoding="utf-8")
    (folder / "corrigibility" / "invariants.json").write_text('{"invariants": []}\n', encoding="utf-8")
    (folder / "memory").mkdir()
    (folder / "memory" / "policy.json").write_text('{"mode": "none"}\n', encoding="utf-8")
    return folder


def test_config_folders_are_the_sixteen() -> None:
    assert CONFIG_FOLDERS == (
        "corrigibility",
        "docs",
        "evals",
        "identity",
        "improvement",
        "inheritance",
        "memory",
        "observability",
        "plugins",
        "prompts",
        "protocols",
        "rubrics",
        "runtime",
        "safety",
        "skills",
        "sources",
    )


def test_list_includes_every_folder_even_when_missing(tmp_path: Path) -> None:
    folder = _agent(tmp_path)
    body = list_config_files(folder, "demo.agent")
    names = [row["name"] for row in body["folders"]]
    assert names == list(CONFIG_FOLDERS)
    prompts = next(row for row in body["folders"] if row["name"] == "prompts")
    assert prompts["present"] is True
    assert any(item["path"] == "prompts/primary.md" and item["writable"] is True for item in prompts["files"])
    docs = next(row for row in body["folders"] if row["name"] == "docs")
    assert docs["present"] is False
    attestation = next(
        item
        for row in body["folders"]
        if row["name"] == "corrigibility"
        for item in row["files"]
        if item["path"] == "corrigibility/attestation.json"
    )
    assert attestation["writable"] is False


def test_normalize_rejects_escape() -> None:
    with pytest.raises(CasopsError) as escaped:
        normalize_rel("../secrets.txt")
    assert escaped.value.code == ErrorCode.SAF_EXFILTRATION
    with pytest.raises(CasopsError) as unknown:
        normalize_rel("agent_spec.json")
    assert unknown.value.code == ErrorCode.INH_SURFACE_UNKNOWN


def test_confined_path_stays_inside(tmp_path: Path) -> None:
    folder = _agent(tmp_path)
    path = confined_path(folder, "prompts/primary.md")
    assert path == (folder / "prompts" / "primary.md").resolve()


def test_read_and_write_roundtrip(tmp_path: Path) -> None:
    folder = _agent(tmp_path)
    before = read_config_file(folder, "demo.agent", "prompts/primary.md")
    assert before["content"] == "# hello\n"
    assert before["writable"] is True
    preview = write_config_file(folder, "demo.agent", "prompts/primary.md", "# next\n", dry_run=True)
    assert preview["saved"] is False
    assert (folder / "prompts" / "primary.md").read_text(encoding="utf-8") == "# hello\n"
    saved = write_config_file(folder, "demo.agent", "prompts/primary.md", "# next\n", dry_run=False)
    assert saved["saved"] is True
    assert (folder / "prompts" / "primary.md").read_text(encoding="utf-8") == "# next\n"


def test_host_owned_attestation_cannot_write(tmp_path: Path) -> None:
    folder = _agent(tmp_path)
    assert host_owned("corrigibility/attestation.json") is True
    with pytest.raises(CasopsError) as exc:
        write_config_file(folder, "demo.agent", "corrigibility/attestation.json", "{}", dry_run=False)
    assert exc.value.code == ErrorCode.IMP_CORRIGIBILITY
    assert json.loads((folder / "corrigibility" / "attestation.json").read_text(encoding="utf-8"))["status"] == "host"


def test_invalid_json_rejected(tmp_path: Path) -> None:
    folder = _agent(tmp_path)
    with pytest.raises(CasopsError) as exc:
        write_config_file(folder, "demo.agent", "identity/persona.json", "{not json", dry_run=True)
    assert exc.value.code == ErrorCode.CMP_JSON_SCHEMA_PROFILE
