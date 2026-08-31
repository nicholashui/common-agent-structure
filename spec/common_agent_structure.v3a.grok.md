**Document ID:** `CASOPS-FS-COMMON-AGENT-STRUCTURE-V3A`  
**Date:** 2026-09-01  
**Status:** Production implementation specification — deployment, self-improvement activation, and capability expansion remain human-gated  
**Supersedes:** `common_agent_structure.v3.md` (2026-08-31), `common_agent_structure.v2.md` (2026-08-24), `common_agent_structure.v1.md` (2026-08-17)  
**Host:** `common-agent-swarm-ops`  
**Structure family:** `casops.common_agent.v3a`  
**Compatibility:** v3 folders load via §21 migration profile (with additional MPP defaults); v2 and v1 folders load via chained profiles  
**Research cutoff:** 2026-09-01

> **Delivery note — read first.**
>
> v3a is a direct, non-lossy evolution of v3. It incorporates the residual improvements identified in the independent scoring review of v3 (complexity containment, stronger citation-to-measurement path, and explicit Minimal Production Profile) while preserving every normative requirement, plane, functional requirement, gate, data model, API, error code, and research reference from v3.
>
> Two constraints remain binding and are restated without softening:
>
> 1. **No runnable artifact was supplied.** There is still no repository, harness, model endpoint, or accelerator in scope. Therefore v3a **cannot** and **does not** report `MEASURED_LOCAL` results. What v3a *does* deliver is (a) the complete architecture from v3, (b) exact quantitative gate thresholds, (c) a fully specified executable benchmark harness, (d) an honest three-way split of evidence, and (e) a concrete, prioritized path to the first `MEASURED_LOCAL` campaign.
> 2. **Citation audit remains incomplete.** The same `[V]` / `[C]` / `[K]` markers from v3 are retained. **CIT-GATE-001 continues to block release** until every `[C]` and `[K]` reference is verified. v3a adds only a more precise verification procedure and a machine-readable audit schema; it does not claim the audit has been completed.
>
> All four v2 defects corrected in v3 (DEF-001 through DEF-004) remain corrected. No defect has been re-introduced.

A v3a common agent remains **one self-contained folder and one `agent_id`**. v3a keeps all nine planes from v3 and adds explicit complexity-containment contracts so that any plane can be independently disabled to a validated baseline without breaking the remaining gates.

---

## Table of contents

1. Purpose, v3a changes, v3 residual improvements, and v2 defect register  
2. Research basis, evidence policy, and citation audit  
3. Core principles  
4. Normative architecture  
5. Folder contract  
6. Composition and inheritance  
7. Performance execution plane  
8. Cache and context-lifecycle plane  
9. Compatibility and protocol plane  
10. Observability and decision provenance  
11. Extensible plugin architecture  
12. Long-term memory architecture  
13. Autonomous self-improvement  
14. Safety and adversarial-robustness plane  
15. Corrigibility plane  
16. Skills, identity, and persona isolation  
17. Compose and runtime algorithm  
18. Data models  
19. Operator and host APIs  
20. Validation specification, harness, report, and path to first MEASURED_LOCAL  
21. Migration from v3 / v2  
22. Traceability  
23. Open risks  
24. Research references and citation audit  
25. Document control  

---

# 1. Purpose, v3a changes, v3 residual improvements, and v2 defect register

## 1.1 Purpose

v3a preserves every v1/v2/v3 identity, inheritance, skill, disclosure, fail-closed, safety, and corrigibility contract. It raises the specification from “measurable by a named harness” to “shippable under a Minimal Production Profile while the full nine-plane surface remains gated.”

The central v3a thesis is identical to v3 with one addition: **complexity itself is now a first-class release risk**. Every added plane must declare an explicit, tested path back to a validated baseline, and a Minimal Production Profile (MPP-1) is defined so that a host can ship a reduced but still safe surface while the remaining planes are measured.

## 1.2 Material changes from v3 (residual improvements)

| Domain | v3 | v3a |
|---|---|---|
| Complexity | Acknowledged as open risk | **First-class containment**: every plane publishes `disable_to_baseline` contract + overhead budget; Minimal Production Profile (MPP-1) defined |
| Citation | CIT-GATE-001 blocks on unresolved markers | Same gate + concrete verification procedure + machine-readable `citation-audit.json` schema |
| Path to measurement | Harness specified | **Prioritized first MEASURED_LOCAL campaign** (§20.10) with ordered fixture suites and success criteria |
| Plane independence | Kill switches required | Kill switches + measured overhead + independent gate pass when disabled |
| Document honesty | NO-GO until MEASURED_LOCAL + CIT-GATE-001 | Same, restated with explicit residual-gap closure plan |

All other material changes from v2 → v3 remain in force unchanged.

## 1.3 Non-goals

Unchanged from v3 §1.3. v3a additionally does not claim that the citation audit has been completed or that any `MEASURED_LOCAL` result exists.

## 1.4 v2 defect register — corrections carried forward (unchanged from v3)

| ID | v2 defect | Severity | v3/v3a correction |
|---|---|---|---|
| **DEF-001** | OpenTelemetry GenAI semantic conventions treated as E1 stable | High | Split grade: W3C Trace Context = E1; OTel core = E1; GenAI semconv = E2 experimental. Pin `schema_url`, emit `casops.*` stable aliases, treat version change as compatibility event. |
| **DEF-002** | CacheScout citation (wrong title, month, identifier) | Medium | Cite by verified title and correct month; adopt adjacent verified works as evidence basis for §8. All remain E3. |
| **DEF-003** | Unverifiable Agent Lightning v1.0 claim with specific SWE-bench delta | High | Claim withdrawn. Architectural pattern (execution/training separation) retained on strength of verified `2508.03680`. |
| **DEF-004** | n=30 validation protocol for p95 and success-rate gates | High | Powered paired design, n≥300/400, bootstrap CIs, TOST, pre-registered plan, `IMP_STAT_UNDERPOWERED` blocker. |

## 1.5 Residual gaps closed in v3a

| Residual gap from v3 scoring | v3a closure |
|---|---|
| High complexity as reliability risk | Every plane must declare `disable_to_baseline` + overhead budget; MPP-1 defined; independent gate when plane is off |
| Incomplete citation audit | Verification procedure + schema made explicit; gate remains blocking |
| No path to first MEASURED_LOCAL | §20.10 prioritized campaign with ordered suites and exit criteria |

---

# 2. Research basis, evidence policy, and citation audit

## 2.1–2.3

Unchanged from v3 §2.1–2.3 (search scope, evidence maturity grades E1–E4, E-RULE-01/02, verified 2026 evidence deltas for serving/caching, memory, observability, compatibility, and self-evolving agents).

## 2.4 Citation audit and release gate (strengthened procedure)

| Marker | Meaning | Count (carried from v3) |
|---|---|---|
| `[V]` | Verified this session via search | 14 |
| `[C]` | Carried forward from v2; not re-verified | 31 |
| `[K]` | From model knowledge; new in v3; not verified | 13 |

**CIT-GATE-001 (release-blocking, unchanged threshold).** Before v3a merges to `main`, every `[C]` and `[K]` reference MUST be resolved to a live identifier with matching title, venue, year, and — where a numeric claim is attached — the specific reported figure located in the source. Any reference that fails resolution is **deleted**, and every normative requirement that depended solely on it is **re-justified or removed**. The audit output is committed as `evals/reports/citation-audit.json`.

**v3a addition — verification procedure (normative):**

1. For each unresolved reference, record the exact string, claimed arXiv/DOI/venue, and the numeric claim (if any).  
2. Resolve via primary source (arXiv abs page, proceedings, official specification).  
3. Record resolution status: `verified`, `title-mismatch`, `identifier-invalid`, `numeric-claim-not-found`, `unreachable`.  
4. Emit machine-readable entry per reference in `citation-audit.json` with fields: `ref_id`, `marker`, `claimed`, `resolved_to`, `status`, `numeric_claim_located`, `dependent_requirements[]`, `action` (`keep` / `re-justify` / `delete`).  
5. Gate fails if any entry has status other than `verified` or if any dependent requirement remains without independent operational justification.

Rationale remains identical to v3: DEF-002 and DEF-003 demonstrated that unverifiable citations are a supply-chain defect.

---

# 3. Core principles

v1/v2/v3 principles P1–P29 are retained verbatim. v3a adds:

| ID | Principle | Normative meaning |
|---|---|---|
| P30 | **Complexity is a release risk** | Every plane beyond the Minimal Production Profile must publish a tested `disable_to_baseline` path, an overhead budget, and an independent gate that still passes when the plane is disabled. Shipping a plane that cannot be cleanly disabled is prohibited. |
| P31 | **Measurement path is first-class** | The specification must contain a concrete, ordered campaign that produces the first `MEASURED_LOCAL` results without further architectural invention. |

---

# 4. Normative architecture

## 4.1 Nine planes + complexity containment

The nine-plane diagram from v3 §4.1 is retained unchanged. v3a adds a normative requirement that the composer and host must treat each plane as independently disableable:

```text
For each plane P ∈ {Execution, Cache/Context, Compatibility, Observability,
                    Plugins, Memory, Improvement, Safety, Corrigibility}:
  - P.disable_to_baseline MUST be defined and tested
  - P.overhead_budget (latency, memory, tokens) MUST be declared
  - When P is disabled, all remaining mandatory gates MUST still pass
```

Safety and Corrigibility remain non-disableable (as in v3).

## 4.2 Control boundaries

Unchanged from v3 §4.2, with the addition that the Corrigibility plane also constrains the ability of any plane to remove its own `disable_to_baseline` contract.

---

# 5. Folder contract

## 5.1 v3a tree (additions relative to v3 marked `+`)

All v3 paths remain required. v3a adds:

```text
  runtime/
+   plane_enablement.json       # per-plane enable/disable + overhead budgets
+   mpp.json                    # Minimal Production Profile declaration

  evals/
+   mpp_gates.json              # reduced gate set that must pass under MPP-1
+   measurement_campaign.json   # ordered first MEASURED_LOCAL campaign
```

## 5.2 Required files (v3a delta)

| Path | Requirement |
|---|---|
| All v3 required paths | Continue to be required |
| `runtime/plane_enablement.json` | Required |
| `runtime/mpp.json` | Required; must declare whether the agent is running under MPP-1 or full surface |
| `evals/mpp_gates.json` | Required |
| `evals/measurement_campaign.json` | Required |

## 5.3 Self-contained meaning

Unchanged from v3, extended: the folder must additionally fully describe its plane-enablement map, MPP status, and the measurement campaign it will execute.

---

# 6. Composition and inheritance

All v1/v2/v3 rules remain normative. v3a adds:

**FR-INH-401.** `plane_enablement` and `mpp` status never inherit. Each child re-declares its own plane enablement and MPP status. A parent’s decision to enable an advanced plane does not force the child to enable it.

**FR-INH-402.** Regression and safety fixtures remain union-monotonic (FR-INH-301 from v3).

---

# 7. Performance execution plane

All FR-PERF-001…017 and FR-PERF-101…110 from v3 remain in force.

**v3a addition:**

| ID | Requirement |
|---|---|
| FR-PERF-201 | The performance plane MUST publish a `disable_to_baseline` that reduces to sequential Plan→Act→Review with fixed routing and no speculative nodes. When disabled, Gate A/B are replaced by the MPP performance subset. |
| FR-PERF-202 | Overhead of the full performance plane (DAG compilation, router, compute controller) MUST be measured and reported; sustained overhead above the declared budget raises a scheduling defect. |

Metric definitions (CPST, goodput, CPE, CRR, TTFO, etc.) remain identical to v3 §7.4.

---

# 8. Cache and context-lifecycle plane

All FR-CACHE-001…009 and context lifecycle requirements from v3 remain in force. Evidence basis remains E3 and gated.

**v3a addition:**

| ID | Requirement |
|---|---|
| FR-CACHE-101 | T1–T3 tiers MUST be independently disableable. Disabling them must leave T0 (exact-match policy/prefix) or a pure uncached path that still satisfies correctness equivalence. |
| FR-CACHE-102 | Cache plane overhead (lookup + invalidation) MUST be measured; the plane must be disableable without changing permissions or semantics. |

---

# 9. Compatibility and protocol plane

All FR-CMP requirements from v3 remain in force (asserted-vs-verified capabilities, template/tokenizer pinning, dual-revision MCP, semconv pinning + `casops.*` aliases, etc.).

**v3a addition:** Capability verification remains mandatory even under MPP-1. An agent running under MPP-1 may disable advanced protocol adapters but may not run with `ASSERTED_UNVERIFIED` capabilities.

---

# 10. Observability and decision provenance

All requirements from v3 §10 remain in force (root trace, decision records, claim-level evidence graph, no raw CoT, tail sampling with 100% mandatory retention, etc.).

**v3a addition:**

| ID | Requirement |
|---|---|
| FR-OBS-201 | The observability plane MUST remain active under MPP-1 at `metadata_only` + decision-record level. Full evidence-graph and advanced sampling may be disabled, but root-trace + decision-record coverage must stay at 100%. |

---

# 11. Extensible plugin architecture

All FR-PLG requirements from v3 remain in force (three isolation tiers, object-capability handles, SBOM/provenance, etc.).

**v3a addition:** Under MPP-1 the host MAY restrict plugins to isolation tier I2 or higher and to a pre-approved set. Zero-core-change and permission-denial gates remain mandatory.

---

# 12. Long-term memory architecture

All requirements from v3 §12 remain in force (typed stores, paged hierarchy, trust tiers, poisoning resistance, verified unlearning, etc.).

**v3a addition:**

| ID | Requirement |
|---|---|
| FR-MEM-201 | Persistent memory MAY be set to `mode: none` under MPP-1. When enabled, the full memory-security and unlearning gates apply; there is no partial “memory without security” profile. |

---

# 13. Autonomous self-improvement

All requirements from v3 §13 remain in force (levels L0–L5, verifier-first, reward-hacking detectors, failure→fixture ratchet, group-sequential canary, etc.).

**v3a addition:** Under MPP-1, improvement is capped at L1 (per-run reflection only). L2+ candidates remain propose-only and require the full v3 promotion gate.

---

# 14. Safety and adversarial-robustness plane

Unchanged from v3. The safety plane remains **mandatory and non-disableable**. All zero-tolerance robustness gates remain in force.

---

# 15. Corrigibility plane

Unchanged from v3. The twelve invariants (INV-01…12), construction-based enforcement, and attestation remain mandatory and non-disableable.

---

# 16. Skills, identity, and persona isolation

Unchanged from v3 (and from v1/v2 core contracts).

---

# 17. Compose and runtime algorithm

Compose and run sequences from v3 remain normative. v3a inserts two additional steps:

- After capability negotiation: evaluate `plane_enablement.json` and apply MPP constraints if declared.  
- Before final lock generation: verify that every disabled plane has a recorded `disable_to_baseline` and that the active gate set matches the declared profile (full or MPP-1).

---

# 18. Data models

All v3 data models remain. v3a adds:

### 18.1 `runtime/plane_enablement.json` (example)

```json
{
  "schema_version": "3.1",
  "agent_id": "video.showrunner",
  "profile": "full",
  "planes": {
    "execution": { "enabled": true, "disable_to_baseline": "sequential_plan_act_review", "overhead_budget_ms": 50 },
    "cache_context": { "enabled": true, "disable_to_baseline": "T0_only_or_uncached", "overhead_budget_ms": 20 },
    "memory": { "enabled": true, "disable_to_baseline": "mode_none", "overhead_budget_ms": 30 },
    "improvement": { "enabled": true, "disable_to_baseline": "L1_only", "overhead_budget_ms": 10 },
    "safety": { "enabled": true, "disable_to_baseline": null },
    "corrigibility": { "enabled": true, "disable_to_baseline": null }
  }
}
```

### 18.2 `runtime/mpp.json`

```json
{
  "schema_version": "3.1",
  "agent_id": "video.showrunner",
  "mpp_version": "MPP-1",
  "active": false,
  "required_planes": ["safety", "corrigibility", "observability_basic", "execution_basic"],
  "forbidden_under_mpp": ["T2_T3_cache", "L2_plus_improvement", "full_memory_hierarchy"]
}
```

---

# 19. Operator and host APIs

All v3 endpoints remain. v3a adds:

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/v3a/agents/{id}/planes` | Current plane enablement + overhead |
| POST | `/api/v3a/agents/{id}/planes/{plane}/disable` | Disable to baseline (dry-run default) |
| GET | `/api/v3a/agents/{id}/mpp` | MPP status and active gate set |
| GET | `/api/v3a/evals/campaign` | Current measurement campaign status |

All mutations remain authenticated, audited, and fail-closed.

---

# 20. Validation specification, harness, report, and path to first MEASURED_LOCAL

## 20.1–20.9

All content from v3 §20.1–20.9 is retained without loss (honesty classification, harness layout, statistical protocol correcting DEF-004, release gates for performance / compatibility / observability / extensibility / memory / improvement / safety / corrigibility, citation audit gate, static validation report, published external evidence, and conclusion).

**Production deployment recommendation remains NO-GO** until `MEASURED_LOCAL` reports satisfy the gates **and** CIT-GATE-001 clears.

## 20.10 Path to first MEASURED_LOCAL (v3a addition)

The following campaign is normative. It is ordered so that safety and statistical validity are established before performance claims are made.

```text
Phase 0 — Prerequisites (must complete before any measurement)
  - Freeze analysis_plan.json
  - Resolve CIT-GATE-001 or explicitly quarantine unresolved references
  - Seed evals/regression/ from known historical failures
  - Confirm batch-invariance status of the chosen model backend

Phase 1 — Safety & Corrigibility (blocking)
  - Full injection / hijack / termination / taint-laundering suites
  - All INV-01…12 negative fixtures
  - Exit criterion: 100% pass, zero false negatives on mandatory categories

Phase 2 — Observability integrity
  - Root-trace, decision-record, redaction, replay, evidence-graph fixtures
  - Exit criterion: 100% root-trace, ≥99.9% parent/child, zero CoT export, RCA@1 ≥85%

Phase 3 — Minimal performance baseline (MPP-1)
  - Sequential + basic parallel three-tool fixture
  - Cache equivalence (T0 only)
  - Kill-switch exercise
  - Exit criterion: MPP performance subset passes; no scope violations

Phase 4 — Full performance Gate A or B
  - n≥300/400 paired design against frozen v2 (or v3) baseline
  - Cold/warm cache, CPE, CRR, goodput, stopping-rule yield
  - Exit criterion: Gate A or Gate B + all additional checks in §20.5.1

Phase 5 — Memory & Improvement (if enabled)
  - Memory profile + poisoning + unlearning + validity check
  - Improvement hold-out + reward-hacking + canary simulation
  - Exit criterion: respective §20.5.5 / §20.5.6 thresholds

Phase 6 — Report & promotion decision
  - Emit full report.json + statistics.json + citation-audit.json
  - Human review of residual risks
  - Only then may production activation be considered
```

The campaign is recorded in `evals/measurement_campaign.json` and its status is queryable via the API. Skipping a phase or reducing sample sizes below the §20.4 minima is a release blocker.

---

# 21. Migration from v3 / v2

## 21.1 Compatibility defaults (v3 → v3a)

A v3 folder migrated without feature enablement receives:

```text
plane_enablement.profile     = "full" (or "MPP-1" if operator chooses)
cache.tiers                  = [T0] (T1–T3 disabled until measured)
improvement.mode             = capped at L1 under MPP-1
memory.mode                  = none under MPP-1
safety + corrigibility       = enforced (non-disableable)
capability_verification      = required
```

Migration remains non-behavior-neutral for the same reasons as v3 (safety, termination, corrigibility, and capability verification activate unconditionally).

## 21.2 Steps

All v3 migration steps remain. v3a inserts:

- After installing corrigibility invariants: declare `plane_enablement.json` and choose full or MPP-1.  
- Before any performance claim: execute or explicitly defer the §20.10 campaign phases.

## 21.3 Backward compatibility

Unchanged from v3. Regression and safety fixtures never down-convert away.

---

# 22. Traceability

All rows from v3 §22 remain. v3a adds:

| Need | Requirements | Acceptance |
|---|---|---|
| Complexity containment | P30, FR-PERF-201/202, FR-CACHE-101/102, plane_enablement | Independent gate pass when plane disabled; overhead budgets |
| Measurement path | P31, §20.10 | Campaign phases completed or explicitly deferred with recorded reason |
| Citation integrity | P29, CIT-GATE-001 + verification procedure | Machine-readable audit with zero unresolved markers |

---

# 23. Open risks

All risks from v3 §23 remain. v3a strengthens the final row and adds:

| Risk | Required mitigation | New/changed in v3a |
|---|---|---|
| **v3a’s own complexity becomes the failure mode** | Every plane independently disableable to a validated baseline; MPP-1 defined; overhead budgets; measurement campaign ordered safety-first | Strengthened |
| Under-measurement of plane overhead | Overhead budgets declared and checked; sustained exceedance is a defect | New |
| Citation audit remains incomplete | CIT-GATE-001 still blocks; verification procedure now explicit | Strengthened |

The structural mitigation remains: **if a plane cannot demonstrate its gate, disable it and ship without it**.

---

# 24. Research references and citation audit

Identical to v3 §24. All `[V]`, `[C]`, and `[K]` markers are retained. The withdrawn Agent Lightning claim remains withdrawn. CIT-GATE-001 continues to block until the audit is complete.

---

# 25. Document control

| Item | Value |
|---|---|
| Owner | Host architecture, CASOPS |
| Supersedes | `common_agent_structure.v3.md`, `.v2.md`, `.v1.md` |
| v2 defects corrected | 4 (unchanged) |
| Residual v3 gaps closed | Complexity containment (P30 + MPP-1 + disable_to_baseline), citation verification procedure, prioritized MEASURED_LOCAL campaign |
| Production-ready specification | Yes |
| Production implementation certified | **No** — §20 local gates + CIT-GATE-001 + §20.10 campaign required |
| Automatic production activation | No |
| Automatic tool, plugin, or network grant | No |
| Automatic candidate promotion | No |
| Core self-modification | Research-only, disabled, isolated |
| Raw chain-of-thought logging or export | Prohibited |
| Reasoning-monitor channel | Internal-only, verdict-emitting, short-retention, non-exportable |
| Default cache tiers | T0 only |
| Default memory | `none` until explicitly configured |
| Default improvement | `disabled`, or `propose` without promotion (L1 max under MPP-1) |
| Safety plane | Mandatory, non-disableable |
| Corrigibility invariants | Mandatory, host-owned, agent-unwritable, attested at every compose |
| Minimal Production Profile | Defined (MPP-1); safety + corrigibility + basic observability + basic execution required |
| Statistical protocol | Pre-registered, powered, paired, interval-estimated |
| Citation audit | **Release-blocking** |
| Public control plane | Existing FastAPI control plane only |
| Normative diagrams | Inline Mermaid diagrams (carried from v3) |

**End of specification.**

---

## Summary of what v3a delivered relative to v3

**Preserved without loss.** Every plane, functional requirement, data model, API, error code, gate threshold, statistical protocol, migration step, research reference, and honesty statement from v3.

**Added.**  
- Principles P30 (complexity is a release risk) and P31 (measurement path is first-class).  
- `plane_enablement.json`, `mpp.json`, and the corresponding API surfaces.  
- Explicit `disable_to_baseline` contracts and overhead budgets for every disableable plane.  
- Minimal Production Profile (MPP-1) that keeps safety, corrigibility, basic observability, and basic execution mandatory while allowing advanced cache, full memory hierarchy, and L2+ improvement to be deferred.  
- Concrete verification procedure for CIT-GATE-001.  
- Prioritized six-phase path to the first `MEASURED_LOCAL` results (§20.10).

**Still deliberately not delivered.** Any fabricated `MEASURED_LOCAL` numbers. The deployment recommendation remains **NO-GO** until the gates and the citation audit are actually satisfied.

v3a is the version that can be implemented and measured without further architectural invention while remaining strictly honest about what has not yet been run.