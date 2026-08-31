"""Minimal guest process environment: OS loader vars only, no production secrets."""

from __future__ import annotations

import os
from pathlib import Path

_KEEP = frozenset(
    {
        "PATH",
        "PATHEXT",
        "SYSTEMROOT",
        "WINDIR",
        "SYSTEMDRIVE",
        "COMSPEC",
        "PROCESSOR_ARCHITECTURE",
        "PROCESSOR_ARCHITEW6432",
        "PROCESSOR_IDENTIFIER",
        "NUMBER_OF_PROCESSORS",
        "TEMP",
        "TMP",
        "TMPDIR",
        "HOME",
        "USERPROFILE",
        "HOMEDRIVE",
        "HOMEPATH",
        "PROGRAMDATA",
        "PROGRAMFILES",
        "PROGRAMFILES(X86)",
        "PYTHONHOME",
        "PYTHONIOENCODING",
        "PYTHONUTF8",
        "PYTHONDONTWRITEBYTECODE",
        "SYSTEMDRIVE",
    }
)

_SECRET_NEEDLES = ("SECRET", "TOKEN", "PASSWORD", "CREDENTIAL", "API_KEY", "ACCESS_KEY")


def guest_env(*, pythonpath: Path, sandbox: str) -> dict[str, str]:
    env: dict[str, str] = {}
    for key, value in os.environ.items():
        upper = key.upper()
        if upper in _KEEP or upper.startswith("PYTHON"):
            if any(needle in upper for needle in _SECRET_NEEDLES):
                continue
            env[key] = value
    env["PYTHONPATH"] = str(pythonpath)
    env["PYTHONIOENCODING"] = "utf-8"
    env["CASOPS_SANDBOX"] = sandbox
    env.pop("AWS_SECRET_ACCESS_KEY", None)
    env.pop("AWS_ACCESS_KEY_ID", None)
    env.pop("CASOPS_HOST_KEY", None)
    env.pop("CASOPS_PRODUCTION_CREDENTIAL", None)
    env.pop("OPENAI_API_KEY", None)
    return env
