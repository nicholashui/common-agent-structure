# 100% complete (requested host implementation)

CASOPS host implementation status against `implementation_plan.md` §16.2 (eight services), the shared library, public `/api/v3`, and the five items that were previously out of contract.

| | |
|---|---|
| **Requested implementation** | **100%** |
| **Production certification** | **Not claimed** |
| Date | 2026-08-31 |
| Profile reached | `baseline_safe` |
| Tests | `python -m pytest tests -q` — 192 tests, exit 0 |
| Spec | `common_agent_structure.md` (`CASOPS-FS-COMMON-AGENT-STRUCTURE-V3A`) |
| Plan | `implementation_plan.md` (`CASOPS-IP-COMMON-AGENT-STRUCTURE-V3A-002`) |

**All requested coding work is done.** There is no leftover service, API path, or previously excluded item still waiting on implementation.

This host is **not** a production-certified release. Default `casops-eval` remains `NOT_RUN` / `pass: false` while `INS-01…08` are `UNQUALIFIED`. T3 is implemented but off until its harness passes. L5 cannot promote to production. I3 on this Windows host is `isolated_guest`, not Firecracker.

---

## Previously excluded items (now implemented)

| Item | Status | Evidence |
|---|---|---|
| Citation audit `CIT-GATE-001/002` | **Done** | Live auditor `python -m casops.citation`. Artifact `evals/reports/citation-audit/citation-audit.json` (`cleared=true`, 57 accepted, 7 deleted knowledge-only, 0 blocking). Spec date reissued to 2026-08-31. Agent Lightning v1.0 numeric claim is `MEASURED_EXTERNAL` only. |
| Powered confirmatory validation | **Done** | Screening is `INDICATIVE` and cannot pass. Confirmatory is paired at powered `n` (binary floor 400), plan-frozen (`VAL_PLAN_DRIFT`), underpowered → `IMP_STAT_UNDERPOWERED`. Local runs use the deterministic adapter. Unqualified instruments still cannot pass. |
| T3 cache enablement | **Done** | T0–T3 manager, scope keys, deletion invalidation, independent verifier, false-reuse harness (≤0.5%). `enable_t3(...)` is the enable path; default remains off. |
| L5 core self-modification | **Done** | `research_only` isolation: no production credentials, approved repos only, signed rollback. `promote_to_production` → `IMP_SCOPE`. |
| Real I1–I3 sandbox runtimes | **Done** | I1 Wasmtime (no WASI). I2 separate process, no ambient network, secrets stripped. I3 isolated guest: no host FS, allow-listed egress. No silent downgrade. Unsigned/third-party cannot run below I2; network requires I3. |

---

## Services

| Service | Status | Notes |
|---|---|---|
| `corrigibility-invariant-service` | **Done** | Persistence, Ed25519, checkpoints, alerts, projection, Dockerfile. FR-COR-004 cancel honored in runtime. |
| `compose-service` | **Done** | MRO/merge/preview, capability matrix/verify, plugin validate-without-exec. |
| `instrument-registry-service` | **Done** | Signed `INS-01…08` persist across reload. Unqualified instruments cannot gate. |
| `control-plane` | **Done** | All spec §19 `/api/v3` paths. Cache stats from the T0–T3 manager. Mutation contract required. |
| `runtime-service` | **Done** | DAG compile, deterministic adapter, one root trace, safety gate, node-boundary cancel. |
| `memory-service` | **Done** | Tenant/subject scoped query/write/delete/verify. Delete invalidates cache. Cross-tenant → empty / `MEM_SCOPE`. |
| `consolidation-worker` | **Done** | Serving path only enqueues. Drain is worker-only. |
| `trainer-bridge` | **Done** | Trajectory export; unsigned import rejected; no serving-process gradients. |

---

## Public `/api/v3` routes (spec §19)

**35 / 35 unique paths implemented.** Counterfactual replay is `POST …/replay?counterfactual=`. Extra `POST …/runtime/run` executes `baseline_safe`.

Mutations require `x-casops-actor`, `x-casops-reason`, `x-casops-expected-parent`, `x-casops-dry-run`. Missing any is not HTTP 200 (`IMP_UNSIGNED`). `agent_runtime` cannot approve (`IMP_SELF_APPROVAL`).

---

## Shared foundation

| Item | Status |
|---|---|
| `src/casops/` package | Present |
| Error catalogue (93 §20 codes, 12-field contract) | Done |
| Canonical JSON + SHA-256 | Done |
| Source identity digest | Done (refreshed 2026-08-31) |
| `agents/_template_v3/` `baseline_safe` | Done |
| ADR-001…013 | Done |
| Actor matrix (deny-by-default) | Done |
| T0–T3 cache | Done; T3 gated |
| `casops-eval` screening / confirmatory | Done |
| `casops-citation` | Done |
| I1 / I2 / I3 runtimes | Done |
| L5 research isolation | Done |
| Eight service Dockerfiles + `/health` | Done |

---

## Plan phases

| Phase | Intent | Status |
|---|---|---|
| 1 | Host skeleton, catalogue, schemas, template | Done |
| 2 | Trust root | Done |
| 3 | Compose MRO / merge / preview | Done |
| 4 | Runtime to `baseline_safe` | Done |
| 5 | Full control plane | Done |
| 6 | Memory + consolidation | Done |
| 7 | Cache, plugins, improvement, trainer-bridge | Done |
| 8 | Profile verification / release gates | Local confirmatory + citation audit executed. **Not** production certification. |

---

## Not claimed (not leftover coding work)

These are release/ops facts, not unfinished services:

- Instruments `INS-01…08` remain `UNQUALIFIED` → default eval `NOT_RUN`
- No production LLM confirmatory against a frozen v2 model baseline
- T3 is off until the false-reuse harness and verifier pass
- L5 has no production promotion path (by spec)
- I3 on Windows is `isolated_guest`, not Firecracker
- 7 knowledge-only citations were deleted; related controls rest on independent engineering justification
- Automatic production activation is still prohibited

---

## What works today

- Signed host-owned invariant store; mismatch/tamper → containment stop
- Compose preview attests invariants before MRO; writes no locks
- Fail-closed MRO and merge (false-wins, budget minima, tools/plugins never inherit)
- `baseline_safe` run: one root span, sealed artifact, no memory writes
- Memory isolation, offline consolidation, unsigned trainer import rejected
- T3 enablement gated on verifier + false-reuse ≤ 0.5%
- Screening cannot pass; confirmatory is paired, powered, plan-frozen
- I1 WASM; I2 no ambient network; I3 no host FS + allow-listed egress
- L5 research isolation only; cannot promote to production
