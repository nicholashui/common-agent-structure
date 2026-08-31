"""ErrorCode enum generated from errors/catalogue.json. Do not hand-edit members."""

from __future__ import annotations

from enum import Enum

from casops.errors.catalogue import load_catalogue


def _build() -> type[Enum]:
    members = {entry["code"]: entry["code"] for entry in load_catalogue()["codes"]}
    return Enum("ErrorCode", members, type=str)


def __getattr__(name: str) -> object:
    if name == "ErrorCode":
        value = _build()
        globals()["ErrorCode"] = value
        return value
    raise AttributeError(name)
