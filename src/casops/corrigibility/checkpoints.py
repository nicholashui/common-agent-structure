"""Attestation checkpoints required by FR-COR-002 and WP-103."""

from __future__ import annotations

from enum import Enum


class Checkpoint(str, Enum):
    compose = "compose"
    run_start = "run_start"
    production_effect = "production_effect"
