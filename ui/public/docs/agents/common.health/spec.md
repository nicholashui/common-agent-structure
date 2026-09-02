# common.health — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/common.health/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "common.health",
  "status": "registered",
  "role": "HostHealthObserver",
  "allowed_tools": [],
  "allowed_plugins": [],
  "model_policy": {
    "provider": "local_deterministic",
    "model_id": "local-deterministic-v1",
    "network_access": false,
    "routing_allowed": false
  },
  "budget_policy": {
    "max_input_tokens": 2048,
    "max_output_tokens": 512,
    "max_model_calls": 0,
    "max_tool_requests": 0,
    "max_job_ms": 15000,
    "max_cost_units": 1.0,
    "max_peer_hops": 0
  },
  "prompt_reference": "prompts/primary.md",
  "rubric_reference": "rubrics/primary.md",
  "critique_edges": {
    "inputs": [],
    "outputs": []
  },
  "max_refinement_count": 0,
  "production_activation_requested": false,
  "does_not_own": [
    "Credentials",
    "Silent production activation",
    "Another agent's exclusive craft output without handoff",
    "Automatic promotion of self-generated artifacts",
    "Modification of safety, telemetry, gates, permissions, or corrigibility",
    "Self-granting tools, plugins, network, or isolation downgrades"
  ],
  "inheritance_ref": "inheritance/parents.json",
  "identity_ref": "identity/",
  "skills_ref": "skills/bindings.json",
  "toggles_ref": "skills/toggles.json",
  "runtime_ref": "runtime/execution.json",
  "context_ref": "runtime/context.json",
  "compute_controller_ref": "runtime/compute_controller.json",
  "backends_ref": "runtime/backends.json",
  "cache_ref": "runtime/cache.json",
  "protocols_ref": "protocols/compatibility.json",
  "capability_assertions_ref": "protocols/capability_assertions.json",
  "observability_ref": "observability/telemetry.json",
  "sampling_ref": "observability/sampling.json",
  "plugins_ref": "plugins/registry.json",
  "isolation_ref": "plugins/isolation.json",
  "memory_ref": "memory/policy.json",
  "memory_hierarchy_ref": "memory/hierarchy.json",
  "memory_security_ref": "memory/security.json",
  "improvement_ref": "improvement/policy.json",
  "verifiers_ref": "improvement/verifiers.json",
  "safety_ref": "safety/policy.json",
  "termination_ref": "safety/termination.json",
  "corrigibility_ref": "corrigibility/invariants.json",
  "evals_ref": "evals/benchmarks.json",
  "analysis_plan_ref": "evals/analysis_plan.json"
}
```

## Folder specification (`SPEC.md`)

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

## Prompts

### `prompts/primary.md`

You are common.health, a baseline-safe host-health observer.
Do not invent metrics. Report only host-filled snapshot fields.
Do not request network, tools, plugins, or memory writes.
Do not treat this snapshot as an eval pass or production certification.

## Rubrics

### `rubrics/primary.md`

Success: emit a bounded JSON health snapshot with status ok or degraded, no network, no memory writes, no production claim.

## Sources

### `sources/MAPPING.md`

No external source mapping.

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [],
  "note": "Sample derived from agents/_template_v3. Health facts are host-filled at run, not sourced externally."
}
```
