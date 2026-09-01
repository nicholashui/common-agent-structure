"""Deterministic local adapter for CI and baseline_safe (plan §18.3)."""

from __future__ import annotations

import json

from casops.contracts.canonical import sha256_json


class DeterministicAdapter:
    provider = "local_deterministic"

    def complete(self, *, prompt: str, node_id: str, agent_id: str = "") -> dict[str, str]:
        digest = sha256_json({"prompt": prompt, "node_id": node_id, "agent_id": agent_id})
        payload = {
            "adapter": self.provider,
            "agent_id": agent_id,
            "node_id": node_id,
            "status": "ready",
            "note": "baseline_safe local_deterministic; no network model.",
            "prompt_sha256": digest,
        }
        return {
            "provider": self.provider,
            "node_id": node_id,
            "text": json.dumps(payload, indent=2, sort_keys=True),
            "digest": digest,
        }
