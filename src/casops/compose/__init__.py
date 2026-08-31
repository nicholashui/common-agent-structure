"""Composer: folder validation, attestation, MRO, merge, locks."""

from casops.compose.engine import Composer, ComposeResult
from casops.compose.merge import merge_specs
from casops.compose.mro import resolve_mro

__all__ = ["Composer", "ComposeResult", "merge_specs", "resolve_mro"]
