"""Scoped cache tiers T0–T3."""

from casops.cache.manager import (
    FALSE_REUSE_LIMIT,
    CacheManager,
    CacheScope,
    EquivalenceVerifier,
    false_reuse_harness,
)

__all__ = [
    "FALSE_REUSE_LIMIT",
    "CacheManager",
    "CacheScope",
    "EquivalenceVerifier",
    "false_reuse_harness",
]
