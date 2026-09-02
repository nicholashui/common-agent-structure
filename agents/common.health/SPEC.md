# common.health

## Mission

Return a sealed **host health snapshot** of this CASOPS control plane and of this agent folder. Operators run it the same way as the template: compose-preview, then `POST /api/v3/agents/common.health/runtime/run`.

## Why this shape

- Smallest useful sample after the template: one DAG node, no tools, no plugins, no memory.
- Health is **host-owned**. The agent folder declares the observe transform; the runtime fills facts. The agent cannot rewrite attestation or claim a production pass.
- Output is JSON text on the sealed artifact (`artifact.text`). It is not eval, not `MEASURED_LOCAL`, and not a green `/health` impersonation of `NOT_RUN` instruments.

## DAG

Single `transform` node `health_1` with `op: health_snapshot`, `side_effect_class: none`.

## Snapshot fields (host-filled)

| Field | Meaning |
|---|---|
| `status` | `ok` if the folder contract is intact, else `degraded` |
| `service` | `control-plane` |
| `agent_id` | `common.health` |
| `folder_ok` / `folder_missing` | spec §5.2 required-file check |
| `production_activation_requested` | always false on this sample |
| `network_access` | false |
| `memory_mode` | `none` |
| `plugins` | 0 |
| `cache_tiers` / `t3_enabled` | from this folder’s cache policy |
| `attestation` | host reference digest / invariant set (not agent-writable) |
| `containment_stop` | null unless a safety gate already stopped the run |

## Out of scope

- OS/hardware probes, live HTTP self-GET of `:18080/health`
- Enabling T3, L5, production activation, or plugins
- Chat / streaming
