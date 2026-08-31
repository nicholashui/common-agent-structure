"""Deterministic local adapter for CI and baseline_safe (plan §18.3)."""

from __future__ import annotations

from casops.contracts.canonical import sha256_json


class DeterministicAdapter:
    provider = "local_deterministic"

    def complete(self, *, prompt: str, node_id: str) -> dict[str, str]:
        digest = sha256_json({"prompt": prompt, "node_id": node_id})
        return {
            "provider": self.provider,
            "node_id": node_id,
            "text": f"deterministic:{digest[:12]}",
            "digest": digest,
        }
