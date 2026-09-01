"""Host-owned health snapshot for observe transforms (common.health)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.contracts.canonical import sha256_json
from casops.corrigibility.store import InvariantStore
from casops.registry.folder import validate_required_files


def observe_health(
    *,
    folder: Path,
    spec: dict[str, Any],
    store: InvariantStore,
    node_id: str = "health_1",
) -> dict[str, Any]:
    memory = json.loads((folder / "memory" / "policy.json").read_text(encoding="utf-8"))
    plugins = json.loads((folder / "plugins" / "registry.json").read_text(encoding="utf-8"))
    cache = json.loads((folder / "runtime" / "cache.json").read_text(encoding="utf-8"))
    check = validate_required_files(folder)
    record = store.reference()
    plugin_list = list(plugins.get("plugins") or [])
    payload = {
        "status": "ok" if check.ok else "degraded",
        "service": "control-plane",
        "agent_id": spec.get("agent_id"),
        "role": spec.get("role"),
        "structure_id": spec.get("structure_id"),
        "schema_version": spec.get("schema_version"),
        "folder": str(folder),
        "folder_ok": check.ok,
        "folder_missing": check.missing,
        "production_activation_requested": bool(spec.get("production_activation_requested")),
        "network_access": bool((spec.get("model_policy") or {}).get("network_access")),
        "memory_mode": memory.get("mode"),
        "plugins": len(plugin_list),
        "cache_tiers": list(cache.get("tiers") or []),
        "t3_enabled": bool(cache.get("t3_enabled")),
        "attestation": {
            "status": "host_reference",
            "invariant_set_id": record.invariant_set_id,
            "digest": record.digest,
        },
        "containment_stop": None,
        "notes": [
            "Host-filled snapshot. The agent folder cannot rewrite attestation.",
            "Not an eval pass and not production certification.",
        ],
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    return {
        "provider": "host_observe",
        "node_id": node_id,
        "text": text,
        "digest": sha256_json(payload),
        "health": payload,
    }
