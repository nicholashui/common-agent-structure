"""T0–T3 cache: scope isolation, T3 gated enablement, false-reuse harness."""

from __future__ import annotations

import pytest

from casops.cache.manager import (
    FALSE_REUSE_LIMIT,
    CacheManager,
    CacheScope,
    EquivalenceVerifier,
    false_reuse_harness,
)
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def _scope(**kwargs: str) -> CacheScope:
    base = dict(agent_id="a", tenant="t1", subject="s1")
    base.update(kwargs)
    return CacheScope(**base)  # type: ignore[arg-type]


def test_t0_hit_and_cross_tenant_purge() -> None:
    cache = CacheManager()
    scope = _scope()
    cache.put(tier="T0", scope=scope, payload="p", value={"v": 1})
    assert cache.get(tier="T0", scope=scope, payload="p") == {"v": 1}
    with pytest.raises(CasopsError) as raised:
        cache.lookup_across_scope(tier="T0", from_scope=scope, to_scope=_scope(tenant="t2"), payload="p")
    assert raised.value.code == ErrorCode.PERF_CACHE_SCOPE
    assert cache.get(tier="T0", scope=scope, payload="p") is None


def test_t3_disabled_until_harness_and_verifier() -> None:
    cache = CacheManager()
    scope = _scope()
    with pytest.raises(CasopsError) as raised:
        cache.put(tier="T3", scope=scope, payload="alpha beta", value={"v": 1})
    assert raised.value.code == ErrorCode.CACHE_SEMANTIC_REUSE
    pairs = [("alpha beta gamma", "alpha beta gamma", True)] * 598
    rate = false_reuse_harness(cache, pairs, scope=scope)
    assert rate <= FALSE_REUSE_LIMIT
    cache.enable_t3(verifier=EquivalenceVerifier(), false_reuse_rate=rate)
    cache.put(tier="T3", scope=scope, payload="alpha beta gamma", value={"v": 9})
    assert cache.get(tier="T3", scope=scope, payload="gamma beta alpha") == {"v": 9}


def test_t3_false_reuse_blocks_enablement() -> None:
    cache = CacheManager()
    scope = _scope()
    pairs = [("cat sat", "unrelated tokens here", False)] * 20
    rate = false_reuse_harness(cache, pairs, scope=scope)
    with pytest.raises(CasopsError) as raised:
        cache.enable_t3(verifier=EquivalenceVerifier(), false_reuse_rate=0.02)
    assert raised.value.code == ErrorCode.CACHE_SEMANTIC_REUSE
    del rate


def test_memory_delete_invalidates_all_tiers() -> None:
    cache = CacheManager()
    scope = _scope()
    cache.put(tier="T0", scope=scope, payload="x", value=1, memory_ids=("m1",))
    cache.on_memory_delete("m1")
    assert cache.get(tier="T0", scope=scope, payload="x") is None
