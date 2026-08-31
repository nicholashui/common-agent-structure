"""Generated error catalogue and codes."""

from casops.errors.catalogue import CATALOGUE_FIELDS, load_catalogue

__all__ = ["CATALOGUE_FIELDS", "ErrorCode", "load_catalogue"]


def __getattr__(name: str):
    if name == "ErrorCode":
        from casops.errors.codes import ErrorCode

        return ErrorCode
    raise AttributeError(name)
