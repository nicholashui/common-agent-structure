"""Governed T0–T3 cache. T3 is off until an independent verifier and false-reuse gate pass."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from casops.contracts.canonical import sha256_json
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

FALSE_REUSE_LIMIT = 0.005
TIERS = ("T0", "T1", "T2", "T3")


@dataclass(frozen=True)
class CacheScope:
    agent_id: str
    tenant: str
    subject: str
    sensitivity: str = "default"
    approval_epoch: str = "0"
    model_revision: str = "local_deterministic"
    tokenizer_digest: str = ""
    template_digest: str = ""
    policy_digest: str = ""
    capability_scope: str = ""


def exact_key(scope: CacheScope, payload: Any) -> str:
    return sha256_json(
        {
            "agent": scope.agent_id,
            "tenant": scope.tenant,
            "subject": scope.subject,
            "sensitivity": scope.sensitivity,
            "approval": scope.approval_epoch,
            "model": scope.model_revision,
            "tokenizer": scope.tokenizer_digest,
            "template": scope.template_digest,
            "policy": scope.policy_digest,
            "capability": scope.capability_scope,
            "payload": payload,
        }
    )


def semantic_signature(text: str) -> str:
    tokens = tuple(sorted({part.lower() for part in text.split() if part}))
    return sha256_json({"tokens": tokens})


@dataclass
class CacheEntry:
    tier: str
    key: str
    value: Any
    scope: CacheScope
    memory_ids: tuple[str, ...] = ()


class EquivalenceVerifier:
    """Independent of the cache lookup path. Compares cached vs uncached outputs."""

    def equivalent(self, cached: Any, uncached: Any) -> bool:
        return cached == uncached


class CacheManager:
    def __init__(self) -> None:
        self._entries: dict[str, CacheEntry] = {}
        self.enabled_tiers: set[str] = {"T0"}
        self.t3_enabled = False
        self.telemetry: dict[str, int] = {
            "hits": 0,
            "misses": 0,
            "invalidations": 0,
            "evictions": 0,
            "scope_rejections": 0,
        }
        self.verifier: EquivalenceVerifier | None = None
        self.false_reuse_rate: float | None = None

    def stats(self, agent_id: str | None = None) -> dict[str, Any]:
        del agent_id
        return {
            "entries": len(self._entries),
            "tiers": sorted(self.enabled_tiers),
            "t3_enabled": self.t3_enabled,
            "telemetry": dict(self.telemetry),
            "false_reuse_rate": self.false_reuse_rate,
        }

    def enable_t3(self, *, verifier: EquivalenceVerifier, false_reuse_rate: float) -> None:
        if false_reuse_rate > FALSE_REUSE_LIMIT:
            raise CasopsError(ErrorCode.CACHE_SEMANTIC_REUSE)
        self.verifier = verifier
        self.false_reuse_rate = false_reuse_rate
        self.t3_enabled = True
        self.enabled_tiers.add("T3")

    def disable_t3(self) -> None:
        self.t3_enabled = False
        self.enabled_tiers.discard("T3")
        self._purge_tier("T3")

    def put(
        self,
        *,
        tier: str,
        scope: CacheScope,
        payload: Any,
        value: Any,
        memory_ids: tuple[str, ...] = (),
        probe: bool = False,
    ) -> str:
        if tier not in TIERS:
            raise CasopsError(ErrorCode.CACHE_INVALIDATION)
        if tier == "T3" and not self.t3_enabled and not probe:
            raise CasopsError(ErrorCode.CACHE_SEMANTIC_REUSE)
        if tier not in self.enabled_tiers and tier != "T3":
            self.enabled_tiers.add(tier)
        key = semantic_signature(str(payload)) if tier == "T3" else exact_key(scope, payload)
        slot = f"{tier}:{scope.agent_id}:{scope.tenant}:{scope.subject}:{key}"
        self._entries[slot] = CacheEntry(tier=tier, key=key, value=value, scope=scope, memory_ids=memory_ids)
        return slot

    def get(self, *, tier: str, scope: CacheScope, payload: Any, probe: bool = False) -> Any | None:
        if tier == "T3" and not self.t3_enabled and not probe:
            self.telemetry["misses"] += 1
            return None
        key = semantic_signature(str(payload)) if tier == "T3" else exact_key(scope, payload)
        slot = f"{tier}:{scope.agent_id}:{scope.tenant}:{scope.subject}:{key}"
        entry = self._entries.get(slot)
        if entry is None:
            self.telemetry["misses"] += 1
            return None
        if not _same_scope(entry.scope, scope):
            self.telemetry["scope_rejections"] += 1
            self.purge()
            raise CasopsError(ErrorCode.PERF_CACHE_SCOPE)
        self.telemetry["hits"] += 1
        return entry.value

    def lookup_across_scope(self, *, tier: str, from_scope: CacheScope, to_scope: CacheScope, payload: Any) -> None:
        """Attempt a cross-boundary reuse — must abort and purge."""
        key = semantic_signature(str(payload)) if tier == "T3" else exact_key(from_scope, payload)
        slot = f"{tier}:{from_scope.agent_id}:{from_scope.tenant}:{from_scope.subject}:{key}"
        entry = self._entries.get(slot)
        if entry is None:
            return
        if not _same_scope(entry.scope, to_scope):
            self.telemetry["scope_rejections"] += 1
            self.purge()
            raise CasopsError(ErrorCode.PERF_CACHE_SCOPE)

    def invalidate_dependency(self, *, policy_digest: str | None = None) -> None:
        if policy_digest is None:
            self.purge()
            return
        remove = [slot for slot, entry in self._entries.items() if entry.scope.policy_digest != policy_digest]
        for slot in remove:
            del self._entries[slot]
            self.telemetry["invalidations"] += 1

    def on_memory_delete(self, memory_id: str) -> None:
        remove = [slot for slot, entry in self._entries.items() if memory_id in entry.memory_ids]
        for slot in remove:
            del self._entries[slot]
            self.telemetry["invalidations"] += 1

    def purge(self) -> None:
        n = len(self._entries)
        self._entries.clear()
        self.telemetry["invalidations"] += n
        self.telemetry["evictions"] += n

    def _purge_tier(self, tier: str) -> None:
        remove = [slot for slot, entry in self._entries.items() if entry.tier == tier]
        for slot in remove:
            del self._entries[slot]
            self.telemetry["evictions"] += 1

    def clear(self) -> None:
        self.purge()


def _same_scope(stored: CacheScope, requested: CacheScope) -> bool:
    return (
        stored.agent_id == requested.agent_id
        and stored.tenant == requested.tenant
        and stored.subject == requested.subject
        and stored.sensitivity == requested.sensitivity
        and stored.approval_epoch == requested.approval_epoch
        and stored.model_revision == requested.model_revision
        and stored.tokenizer_digest == requested.tokenizer_digest
        and stored.template_digest == requested.template_digest
        and stored.policy_digest == requested.policy_digest
        and stored.capability_scope == requested.capability_scope
    )


def false_reuse_harness(
    manager: CacheManager,
    pairs: list[tuple[str, str, bool]],
    *,
    scope: CacheScope,
) -> float:
    """Independent false-reuse measurement. ``pairs`` are (cached_payload, probe, should_hit)."""
    if not pairs:
        return 0.0
    false = 0
    for cached_payload, probe, should_hit in pairs:
        manager.put(tier="T3", scope=scope, payload=cached_payload, value={"text": cached_payload}, probe=True)
        hit = manager.get(tier="T3", scope=scope, payload=probe, probe=True) is not None
        if hit and not should_hit:
            false += 1
        manager._purge_tier("T3")
    return false / len(pairs)
