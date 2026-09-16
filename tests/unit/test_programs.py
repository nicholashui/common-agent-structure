from pathlib import Path

import pytest

from casops.errors.exceptions import CasopsError
from casops.programs import list_programs, normalize_code, read_program, write_program


def test_normalize_code_lowercase_no_spaces() -> None:
    assert normalize_code("SpringLaunch") == "springlaunch"
    assert normalize_code("spring launch") == "springlaunch"
    with pytest.raises(CasopsError):
        normalize_code("")
    with pytest.raises(CasopsError):
        normalize_code("1bad")
    with pytest.raises(CasopsError):
        normalize_code("../escape")


def test_write_and_list_program(tmp_path: Path) -> None:
    root = tmp_path / "program"
    dry = write_program(root, {"code": "alpha", "name": "Alpha"}, dry_run=True, create=True)
    assert dry["dry_run"] is True
    assert dry["saved"] is False
    assert not (root / "alpha" / "program.json").is_file()
    saved = write_program(root, {"code": "Alpha One", "name": "Alpha One"}, dry_run=False, create=True)
    assert saved["id"] == "alphaone"
    assert saved["code"] == "alphaone"
    assert saved["name"] == "Alpha One"
    assert saved["folder"] == "program/alphaone"
    assert (root / "alphaone" / "program.json").is_file()
    rows = list_programs(root)
    assert rows[0]["id"] == "alphaone"
    loaded = read_program(root, "alphaone")
    assert loaded["name"] == "Alpha One"


def test_duplicate_program_rejected(tmp_path: Path) -> None:
    root = tmp_path / "program"
    write_program(root, {"code": "beta", "name": "Beta"}, dry_run=False, create=True)
    with pytest.raises(CasopsError):
        write_program(root, {"code": "beta", "name": "Beta 2"}, dry_run=False, create=True)
