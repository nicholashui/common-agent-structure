*Thinking...*

> **Considering document structure**
> 
> I’m looking at the v3 Table of Contents, which has 25 sections and no errors right now. I wonder if I should insert an Error catalogue as section 20 and then shift the validation section to 21. But, I’m questioning whether this would lead to any loss of clarity or if it would make maintaining the numbering easier. It’s definitely worth exploring how to keep everything organized without losing meaning.
> 
> **Considering literature audit**
> 
> I’m thinking about preserving the historical claim since the prior draft marked certain elements, but the current version doesn’t rely on that marker. I wonder if the user expects us to perform a literature audit based on their improvement suggestion. That might involve including a citation gate. Maybe I can browse to verify stable sources that reflect any recent changes or confirmations needed for accuracy. It feels like a good approach for solidifying our claims!
> 
> **Clarifying document details**
> 
> It seems I need to address the current date correction for the draft, which shows an incorrect future date of Aug 31. Also, v3a, dated Aug 24, indicates that all source verifications are still pending, unless there's supporting evidence. Notably, there’s no runnable artifact, and I didn't execute a literature audit this time. While I could mention the lack of browsing due to this being a revision, I’m unsure if it’s necessary to include that in the document. However, honesty remains important to me!
> 
> **Clarifying error catalogues**
> 
> I'm noticing a potential issue where the previous score suggested "restore consolidated error catalogue," but the original summary mentioned an expanded error catalogue, which isn't present. I need to add that detail to ensure clarity moving forward. It's important that my summaries accurately reflect the intended message, so I'll make sure to address this discrepancy. Let's see how we can rectify this to maintain consistency in our documentation!

# `common_agent_structure.v3a.md`

> **Delivery note — read first.**
>
> Four constraints shape this revision:
>
> 1. **No runnable artifact was supplied.** There is no repository, harness implementation, model endpoint, collector, plugin runtime, memory backend, or accelerator in scope. Therefore v3a does **not** report `MEASURED_LOCAL` results. It delivers the complete architecture, quantitative release gates, executable harness contract, migration profile, consolidated error catalogue, and an honest separation of static, external, and unexecuted evidence.
> 2. **The supplied v3 draft was future-dated.** It carried a document date and research cutoff of **2026-08-31**, while this revision is issued on **2026-08-24**. v3a removes that future-dated status. No search, verification, measurement, or event after August 24, 2026 is represented as completed.
> 3. **No committed citation-audit artifact accompanied the supplied drafts.** References marked `[V]` by the unreleased v3 draft are therefore reclassified as `[D]`: *claimed verified by the prior draft, but not accepted as audit-verified by v3a*. `CIT-GATE-001` blocks release until every `[D]`, `[C]`, and `[K]` reference is verified and the audit artifact is committed.
> 4. **v3a is standalone.** Requirements previously incorporated only by phrases such as “retained from v1/v2” are reproduced here. A consolidated error catalogue is restored. Fixed sample sizes are replaced by prospective power calculations, non-inferiority is separated from equivalence testing, and optional optimizer kill switches are distinguished from mandatory-control containment stops.
>
> **No v3 functional requirement has been intentionally removed.** Where v3 contained an inconsistency, v3a retains the underlying control and supplies corrected wording.

---

**Document ID:** `CASOPS-FS-COMMON-AGENT-STRUCTURE-V3A`  
**Date:** `2026-08-24`  
**Status:** Draft production implementation specification — release, deployment, self-improvement activation, and capability expansion remain human-gated and validation-blocked  
**Supersedes when approved:** `common_agent_structure.v2.md`  
**Revises:** unreleased `common_agent_structure.v3.md` draft labelled `2026-08-31`  
**Host:** `common-agent-swarm-ops`  
**Structure family:** `casops.common_agent.v3`  
**Schema version:** `3.0` — v3a is a specification correction and does not require a schema-family bump  
**Compatibility:** v2 folders load through §22; v1 folders load through the v2 profile chained through §22  
**Research cutoff:** `2026-08-24`  
**Citation-audit status:** `BLOCKED`

A v3a common agent remains **one self-contained folder and one `agent_id`**. It has nine first-class planes:

1. execution;
2. compatibility and protocol;
3. observability and decision provenance;
4. extensibility and plugins;
5. long-term memory;
6. autonomous improvement;
7. safety and adversarial robustness;
8. cache and context lifecycle;
9. corrigibility.

---

## Table of contents

1. Purpose, changes, and defect register
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
20. Consolidated error catalogue
21. Validation specification, harness, and report
22. Migration from v2
23. Traceability
24. Open risks
25. Research references and citation audit
26. Document control

---

# 1. Purpose, changes, and defect register

## 1.1 Purpose

v3a preserves the v1/v2 identity, inheritance, skill, disclosure, and fail-closed contracts while providing a complete production implementation specification for:

- task-completion latency, success, cost, and goodput;
- model, tool, protocol, and telemetry interoperability;
- end-to-end operational provenance;
- sandboxed executable extensions;
- typed, persistent, security-governed memory;
- gated autonomous improvement;
- cache and context lifecycle management;
- measured adversarial robustness;
- architecturally enforced corrigibility;
- powered and pre-registered validation.

The central validation thesis remains:

> A specification must define not only what to measure, but how to measure it credibly.

The earlier v2 rule of “at least 30 observations” was inadequate for percentile and binary-rate gates. v3a requires prospective power calculations, paired or blocked task assignment, interval estimates, explicit estimands, and distinct procedures for superiority, non-inferiority, and equivalence.

## 1.2 Material changes

### v2 to v3 architecture

| Domain | v2 | v3a |
|---|---|---|
| Performance | DAG, routing, opportunistic cache | Agent-aware cache scheduling, SLO admission control, goodput/CPE/CRR, adaptive compute and stopping |
| Context | Static segment budgets | Compaction, offload, re-grounding, sub-agent isolation, context-rot testing |
| Compatibility | Declared capability matrix | Asserted-versus-verified capabilities, capability-drift detection, tokenizer/template pinning, schema-profile negotiation |
| Observability | Traces, decision records, replay | Claim-level evidence graph, bounded reasoning monitor, mandatory tail retention, trace-cost budgets, automated RCA |
| Extensibility | Isolated process, digest, signature | I0–I3 isolation, object-capability handles, SBOM, provenance, scanning, ABI contracts |
| Memory | Seven stores, bitemporal records, hybrid retrieval | Paged hierarchy, trust tiers, poisoning resistance, consolidation, verified deletion and unlearning probes |
| Improvement | Propose-only candidates and human gate | Verifier-first objectives, reward-hacking detection, full regression ratchet, group-sequential canaries, immutable ledger |
| Safety | Distributed rules | First-class threat model, taint propagation, injection/hijack/exfiltration and termination gates |
| Corrigibility | Policy-based human gates | Host-owned invariant set unreachable by the agent |
| Validation | Fixed low sample floor and point comparisons | Prospective power, paired design, CIs, superiority/NI/equivalence separation, pre-registration |
| Citations | Inline references | Confidence markers and release-blocking audit |

### Unreleased v3 draft to v3a

| Area | v3 draft issue | v3a correction |
|---|---|---|
| Date integrity | Dated 2026-08-31 before that date occurred | Dated 2026-08-24; no future completion claims |
| Citation state | Prior `[V]` claims had no attached audit artifact | Reclassified to `[D]` until audit evidence is committed |
| Binary sample sizes | `n≥400` implied universal power for a 5pp gate | `n=max(floor, prospectively powered n)` using paired discordance assumptions |
| Statistical terminology | TOST described as the generic NI procedure | One-sided NI testing for NI; TOST only for two-sided equivalence |
| Kill switches | “Every plane disableable” conflicted with mandatory safety/corrigibility | Optional optimizers have baseline kill switches; mandatory controls have fail-stop containment |
| Standalone use | Multiple requirements incorporated only by reference to v1/v2 | Retained requirements reproduced |
| Error handling | Summary promised an expanded catalogue, but no consolidated section existed | Complete §20 added |
| Citation counts | Prior draft reported grouped counts not backed by a machine audit | Counts treated as provisional until `citation-audit.json` normalizes entries |

## 1.3 Non-goals

This specification does not:

- authorize production activation;
- authorize unrestricted network access;
- authorize an agent to grant itself tools, plugins, permissions, or credentials;
- require or export private model chain-of-thought;
- permit the agent to modify its gates, telemetry, safety policy, permissions, or termination conditions;
- treat any preprint as a production baseline without local validation;
- claim bitwise model reproducibility without verified batch-invariant execution;
- claim that deletion from a memory store removes influence already incorporated into model weights;
- create a second public control plane;
- claim that external research gains are CASOPS gains;
- certify an implementation that was not supplied or executed.

## 1.4 Defect register

| ID | Defect | Severity | v3a correction |
|---|---|---:|---|
| `DEF-001` | v2 treated OpenTelemetry GenAI semantic conventions as a stable default contract. | High | GenAI attributes are treated as experimental until audit verifies otherwise. Pin `schema_url`, emit stable `casops.*` aliases, and treat any change as a compatibility event. |
| `DEF-002` | v2 labelled arXiv `2608.14624` as “CacheScout” and assigned an incorrect month/title. | Medium | The disputed label is removed. The identifier and title must be resolved by `CIT-GATE-001` before use. |
| `DEF-003` | v2 attached a specific SWE-bench gain to an unverifiable Agent Lightning identifier. | High | The numeric claim remains withdrawn. Execution/training separation is retained on operational grounds and subject to citation audit. |
| `DEF-004` | v2 used roughly 30 observations for p95 and binary success gates. | High | Replaced by powered, paired validation with minimum percentile floors and prospective binary-rate power calculations. |
| `DEF-005` | The supplied v3 draft was dated seven days in the future. | High | v3a uses August 24, 2026 and forbids representing future verification as complete. |
| `DEF-006` | v3 treated `n≥400` as generally adequate for a 5pp binary gate and used TOST terminology for NI. | High | Binary `n` is power-derived from baseline and paired discordance; NI and equivalence procedures are separated in §21.4. |
| `DEF-007` | v3 said every added plane had a kill switch while declaring safety and corrigibility non-disableable. | Medium | Optional optimizers use kill switches; mandatory controls use containment stops that halt execution rather than bypass controls. |
| `DEF-008` | v3 depended on retained v1/v2 requirements without reproducing them and omitted a consolidated error catalogue. | Medium | Retained normative requirements are inlined and §20 is added. |

---

# 2. Research basis, evidence policy, and citation audit

## 2.1 Search provenance

The supplied drafts report searches across:

- arXiv;
- NeurIPS, ICML, ICLR, PMLR, OpenReview, and ACL Anthology;
- W3C;
- CNCF;
- Linux Foundation;
- official OpenTelemetry, MCP, A2A, and CloudEvents material.

No machine-readable audit proving those searches was attached. v3a preserves the references and architecture but does not accept historical “verified this session” labels as release evidence.

## 2.2 Evidence maturity

| Grade | Meaning | Production treatment |
|---|---|---|
| `E1` | Stable standard or peer-reviewed result with released evaluation | May default on only after local validation |
| `E2` | Peer-reviewed but workload-dependent, or an experimental standard | Feature-gated until local CASOPS gates pass |
| `E3` | Recent preprint or early implementation | Experimental only, explicit flag, fallback, kill switch |
| `E4` | Open-ended self-modification or insufficiently bounded mechanism | Research-only, isolated, disabled in production |

**E-RULE-01.** A feature supported only by E3 evidence must have:

- a validated fallback;
- an independently exercisable optimizer kill switch;
- a runtime budget;
- telemetry;
- no mandatory role on a high-risk execution path.

**E-RULE-02.** External reported deltas:

- are never additive;
- are never represented as CASOPS results;
- must identify the study or be labelled `TARGET`;
- cannot replace local validation.

**E-RULE-03.** Mandatory safety, audit, and corrigibility controls do not receive bypass kill switches. If unavailable, the system enters a containment stop.

## 2.3 Citation-confidence markers

| Marker | Meaning | Release treatment |
|---|---|---|
| `[A]` | Accepted by a committed v3a citation-audit artifact | May support requirements subject to evidence grade |
| `[D]` | Prior unreleased v3 draft claimed verification; v3a has not accepted the audit | Blocked |
| `[C]` | Carried from v2 without a v3a audit | Blocked |
| `[K]` | Model or author knowledge without a v3a audit | Blocked |

The prior draft reported a `14 / 31 / 13` split across verified, carried, and knowledge-derived references. Because the entries were grouped inconsistently and no audit artifact was supplied, those counts are historical metadata, not an accepted v3a inventory.

## 2.4 Evidence basis retained from the supplied draft

### Serving and cache

The draft identifies work on:

- learned agent-execution-aware KV-cache management;
- policy-driven agentic serving;
- workload-aware multi-agent caching.

These motivate §8 but remain E3 and `[D]` until audited. Cache correctness, privacy, and fallback requirements are independently justified by operational engineering.

### Memory

The draft identifies surveys of:

- agent memory mechanisms;
- memory evaluation limitations;
- long-term memory security;
- self-evolving and lifelong agents.

These motivate trust tiers, poisoning tests, evaluation-validity checks, and deletion verification. The controls remain defensible independently of any one citation.

### Observability and compatibility

The draft reports:

- consolidation around OpenTelemetry-based GenAI observability;
- continued GenAI semantic-convention churn;
- rapid explicit MCP revisioning.

v3a therefore pins versions and emits a CASOPS-owned alias layer without assuming the current stability status of any unaudited external convention.

### Self-improvement

The draft organizes improvement by what, when, how, and where evolution occurs. v3a retains that framing while enforcing the decisive boundary: prompts, context, memory, and workflow may produce candidates; permissions, gates, telemetry, safety, and production activation remain unreachable.

## 2.5 Citation audit gate

**CIT-GATE-001 — release-blocking.**

Before merge to `main`, every `[D]`, `[C]`, and `[K]` entry must be resolved to a live source with:

- matching identifier;
- matching title;
- authors;
- venue or repository;
- publication or revision date;
- evidence grade;
- located support for every attached numeric claim;
- audit actor;
- verification timestamp not later than the audit date;
- source digest where legally and technically available.

Output:

```text
evals/reports/<run-id>/citation-audit.json
```

Minimum fields:

```json
{
  "reference_id": "ref-001",
  "marker_before": "D",
  "resolved_identifier": "arXiv:...",
  "expected_title": "...",
  "observed_title": "...",
  "venue": "...",
  "year": 2026,
  "numeric_claims": [
    {
      "claim": "...",
      "location": "page/section/table",
      "status": "verified"
    }
  ],
  "verified_by": "reviewer-id",
  "verified_at": "2026-08-24T00:00:00Z",
  "status": "accepted"
}
```

Unresolvable references are deleted. Requirements depending solely on them must be independently justified or removed.

## 2.6 Date-integrity rule

**CIT-GATE-002.** A source, revision, benchmark result, or verification dated after the document’s audit date must not be represented as completed. Future-dated references may appear only as planned work and cannot support a requirement.

---

# 3. Core principles

| ID | Principle | Normative meaning |
|---|---|---|
| P1 | One identity | One folder remains one `agent_id`. |
| P2 | Child owns mission | Parent content supports but never replaces the child mission. |
| P3 | Safety tightens | Deny lists union, budgets take minima, and false safety booleans win. |
| P4 | Tools never inherit | Tools and executable plugins require child declaration and host approval. |
| P5 | Disabled means absent | Disabled skills and plugins do not enter prompts, tools, memory, cache keys, traces, evidence graphs, or critique. |
| P6 | Persona is presentation | Persona cannot mint facts, permissions, confidence, credentials, trust, or authority. |
| P7 | Evidence over narrative | Provenance records observable evidence, actions, constraints, and outcomes—not claimed private thought. |
| P8 | Optimize job completion | Optimize successful, SLO-meeting work per time and cost, not raw token rate. |
| P9 | Capability negotiation | Runtime behavior depends on verified capabilities, not vendor branding. |
| P10 | Typed extensibility | Every extension has a manifest, typed interfaces, integrity data, permissions, and limits. |
| P11 | Memory is governed data | Persistent memory has source, time, scope, trust, sensitivity, retention, and deletion semantics. |
| P12 | Improvement proposes | The agent may generate candidates; only an external gate may promote them. |
| P13 | Reproducible composition | Every run references immutable compose and capability locks. |
| P14 | Fail closed at trust boundaries | Unknown code, drift, invalid memory, broken provenance, or unauthorized mutation aborts. |
| P15 | Optional acceleration fails safely | Optional optimizer failure may use only a validated semantic-equivalent baseline. |
| P16 | No floating production dependencies | Protocol, adapter, plugin, model, prompt, template, tokenizer, schema, and semconv versions are pinned. |
| P17 | Independent validation | A self-generated candidate cannot promote on its own self-score. |
| P18 | Rollback is mandatory | Every promoted mutable artifact has a previous signed version and tested rollback. |
| P19 | Cache is scheduled | Cache has an owner, scope, budget, key discipline, correctness guard, and telemetry. |
| P20 | Context is a lifecycle | Context is allocated, compacted, offloaded, re-grounded, and verified under policy. |
| P21 | Capabilities are verified | An asserted capability is unavailable until a conformance fixture passes. |
| P22 | Attribution is claim-level | Material output claims link to supporting evidence. |
| P23 | Authority is by handle | Extensions receive narrow object-capability handles, not ambient authority. |
| P24 | Memory is an attack surface | Persistent memory is treated as adversarially reachable. |
| P25 | Every fixed failure becomes permanent | A resolved failure becomes a retained regression fixture. |
| P26 | Verifier before optimizer | No improvement objective is admissible without an independent verifier. |
| P27 | Corrigibility is unreachable by construction | Gates, telemetry, permissions, and termination controls are outside every agent-writable surface. |
| P28 | Statistical honesty | Claims require adequate power, paired design, intervals, declared estimands, and pre-registration. |
| P29 | Citation integrity | An unaudited or unverifiable citation cannot support release. |
| P30 | Fail back or fail stop—never fail open | Optional optimizers fall back; mandatory controls stop execution. |

---

# 4. Normative architecture

## 4.1 Nine planes

```mermaid
flowchart TB
    F["Agent folder<br/>one agent_id"] --> C["Fail-closed composer"]
    C --> L["Immutable compose lock<br/>compose_hash + capability_lock"]

    L --> E["Execution plane<br/>planner / DAG / router / scheduler"]
    L --> CX["Cache + context lifecycle plane"]

    E --> M["Model adapters"]
    E --> T["Tools and plugins"]
    E --> P["Peer agents"]
    E --> R["Memory hierarchy"]
    CX --- E
    CX --- M
    CX --- R

    E --> SAF["Safety plane<br/>injection / hijack / loop guards"]
    SAF --> E

    C --> O["Observability plane"]
    E --> O
    R --> O
    T --> O
    SAF --> O
    CX --> O
    O --> OT["OTel core + pinned GenAI semconv<br/>+ casops.* stable aliases"]

    O --> I["Improvement plane<br/>attribution / candidate generation"]
    I --> S["Sandbox + independent evaluation"]
    S --> G{"Statistical release gates"}
    G -->|pass| CAN["Shadow / canary"]
    CAN --> H{"Independent human approval"}
    H -->|"signed artifact"| F
    H -->|reject| Q["Archive / quarantine"]

    COR["Corrigibility plane<br/>unreachable invariants"] -.->|"constrains"| E
    COR -.->|"constrains"| I
    COR -.->|"constrains"| O
    COR -.->|"constrains"| R

    H -. never automatic .-> PROD["Production activation"]
```

## 4.2 Control boundaries

| Plane | May read | May write | Cannot do |
|---|---|---|---|
| Composer | Folder, parent metadata, manifests, conformance results | Generated locks | Execute unverified extension code |
| Execution | Composed envelope, approved memory and capabilities | Run artifacts, candidate memories | Modify its production definition |
| Cache/context | Scoped prefixes, entries, context state | Scoped cache and context artifacts | Cross tenant, subject, sensitivity, or approval boundaries |
| Memory | Approved observations and outcomes | Versioned records and tombstones | Grant tools, alter policy, or override newer human approval |
| Safety | Inbound content, external output, run state | Taint, blocks, incidents | Be bypassed by the agent, skill, plugin, or persona |
| Observability | Operational events and configured content | Append-only telemetry | Change run behavior |
| Improvement | Traces, outcomes, fixtures | Candidate artifacts | Promote, approve, or sign a candidate |
| Corrigibility | Host-held invariant reference | Attestation only | Be modified by any runtime plane |
| Human gate | Candidate and validation report | Approval record | Bypass immutable audit |

## 4.3 Control-switch classes

| Switch class | Applies to | Effect |
|---|---|---|
| `optimizer_kill_switch` | Cache tier, speculation, learned router, compaction strategy, adaptive refinement | Disable feature and return to validated baseline semantics |
| `route_quarantine` | Model, protocol, plugin, or capability route | Remove route from eligibility |
| `containment_stop` | Safety, corrigibility, mandatory audit, permission enforcement | Halt or reject work; never bypass the control |
| `operator_shutdown` | Entire agent | Cancel in-flight work within the configured deadline |

---

# 5. Folder contract

## 5.1 Tree

```text
agents/<pack.agent-id>/
  README.md
  SPEC.md
  agent_spec.json

  prompts/
  rubrics/
  sources/{PROVENANCE.json,MAPPING.md,excerpts/}
  docs/user_guide.md

  inheritance/{parents.json,resolved.json,conflicts.json}
  skills/{SKILL.md,bindings.json,integration.json,toggles.json}
  identity/{persona.json,background.json,DISCLOSURE.md}

  runtime/
    execution.json
    backends.json
    routing.json
    cache.json
    context.json
    compute_controller.json

  protocols/
    compatibility.json
    capability_assertions.json
    conformance/
    schemas/{agent_message.schema.json,event.schema.json}

  observability/
    telemetry.json
    redaction.json
    slo.json
    decision_record.schema.json
    sampling.json
    evidence_graph.schema.json
    semconv.lock.json

  plugins/
    registry.json
    lock.json
    manifests/
    isolation.json
    supply_chain/

  memory/
    policy.json
    stores.json
    retention.json
    hierarchy.json
    consolidation.json
    security.json
    unlearning.json
    schemas/memory_record.schema.json
    migrations/

  improvement/
    policy.json
    objectives.json
    verifiers.json
    ledger.json
    candidates/
    approvals/
    rollback/

  safety/
    policy.json
    injection.json
    termination.json
    incidents/

  corrigibility/
    invariants.json
    attestation.json

  evals/
    benchmarks.json
    baselines.json
    analysis_plan.json
    fixtures/
    regression/
    reports/

  generated/
    compose.lock.json
    capabilities.lock.json
    benchmark-baseline.json
    compatibility-matrix.lock.json
    context-budget.lock.json
```

`corrigibility/invariants.json` is a logical folder contract path. At runtime it must be a host-owned, read-only mount or immutable reference outside every agent-writable capability.

## 5.2 Required files

| Path | Requirement |
|---|---|
| `README.md`, `SPEC.md`, `agent_spec.json` | Always required |
| `sources/PROVENANCE.json` | Always required |
| `inheritance/parents.json` | Required; may be empty |
| `inheritance/resolved.json` | Generated after successful compose |
| `skills/toggles.json` | Required; may be empty |
| `identity/DISCLOSURE.md` | Required when identity mode is not `grounded` |
| `runtime/execution.json` | Required |
| `runtime/backends.json` | Required; may declare only `local_deterministic` |
| `runtime/routing.json`, `runtime/cache.json` | Required; disabled modes are valid |
| `runtime/context.json` | Required |
| `runtime/compute_controller.json` | Required; `mode: fixed` is valid |
| `protocols/compatibility.json` | Required |
| `protocols/capability_assertions.json` | Required |
| `protocols/conformance/` | Required and non-empty before production |
| `observability/telemetry.json` | Required |
| `observability/redaction.json` | Required |
| `observability/sampling.json` | Required |
| `observability/semconv.lock.json` | Generated; required before export |
| `plugins/registry.json` | Required; empty list is valid |
| `plugins/isolation.json` | Required when plugins are non-empty |
| `memory/policy.json` | Required; `mode: none` is valid |
| `memory/hierarchy.json` | Required when persistent memory is enabled |
| `memory/security.json` | Required when persistent memory is enabled |
| `memory/unlearning.json` | Required when persistent memory is enabled |
| `improvement/policy.json` | Required; defaults to disabled |
| `improvement/verifiers.json` | Required when improvement is enabled |
| `safety/policy.json` | Always required; no opt-out |
| `safety/termination.json` | Always required |
| `corrigibility/invariants.json` | Always required; host-owned and agent-unwritable |
| `evals/benchmarks.json` | Always required |
| `evals/analysis_plan.json` | Required before any performance or quality claim |
| `evals/regression/` | Required and union-monotonic |
| `generated/*.lock.json` | Generated only |

## 5.3 Self-contained meaning

The folder must independently describe:

- mission and boundaries;
- expected inputs and outputs;
- inheritance;
- skills and identity;
- required and forbidden capabilities;
- runtime, cache, context, and compute policies;
- protocols and compatibility;
- telemetry and redaction;
- plugin and isolation policy;
- memory, trust, retention, security, and deletion;
- improvement scopes and verifiers;
- safety and termination;
- corrigibility invariants;
- validation and statistical analysis.

Parent folders, remote catalogs, endpoints, and host-held invariants are resolved only during compose.

---

# 6. Composition and inheritance

## 6.1 Parent legality and MRO

A parent is legal only if:

1. its `agent_id` resolves to a registered folder;
2. the folder contains `SPEC.md` and `agent_spec.json`;
3. it belongs to a compatible common-agent structure family;
4. it is not the child;
5. every requested inherited surface is legal;
6. its content hashes can be pinned.

Rules:

- maximum declared parents: 8;
- maximum depth: child plus three ancestor levels;
- child is first in MRO;
- parents sort by ascending priority, then ascending `agent_id`;
- traversal is depth-first;
- each parent appears once;
- diamonds collapse;
- cycles fail closed;
- missing or incompatible parents fail closed.

## 6.2 Merge rules

| Surface | Rule |
|---|---|
| Child scalar content | Child wins |
| `does_not_own` | Union; more restrictive |
| Numeric budgets | Minimum |
| `network_access` | False wins |
| Production activation | False wins |
| `max_refinement_count` | Minimum |
| `allowed_tools` | Never inherited |
| `allowed_plugins` | Never inherited |
| Content lists | Stable-key union in MRO order |
| Critique edges | Union; self-edges removed |
| Safety policy | Tightening may inherit; relaxation does not |
| Prompt/rubric references | Child remains primary; parent references are labelled appendices |
| Parent SPEC fragments | Quoted with parent ID and hash, never silently represented as child-authored |

## 6.3 Non-inherited surfaces

The following never inherit:

- credentials, secrets, API keys, and cookie jars;
- model endpoint credentials;
- provider authorization;
- protocol authorization;
- tools and executable plugin grants;
- plugin signatures and approvals;
- cache contents or cache-sharing permissions;
- verified capability status;
- tokenizer or template verification results;
- isolation-tier assignments or sandbox grants;
- SBOM and build-provenance approvals;
- actual memory records;
- tenant, subject, or user scope;
- memory tier residency;
- memory trust assignments;
- deletion or unlearning authority;
- telemetry content-capture approval;
- improvement approval or promotion rights;
- verifier approvals;
- canary allocation;
- production activation;
- named-person identity approval;
- safety-policy relaxations;
- termination-condition relaxations;
- corrigibility invariants;
- statistical plans, baselines, or held-out sets.

## 6.4 Legal inherited surfaces

| Surface | Behavior |
|---|---|
| `responsibility_fragments` | Appended as support; child mission remains first |
| `knowledge_sources` | Stable-key union |
| `quality_criteria` | Union by dimension; child weight wins |
| `prompt_refs` | Labelled inherited appendices |
| `rubric_refs` | Labelled inherited appendices |
| `skill_bindings` | Union, then enable-AND |
| `critique_edges` | Union |
| `architecture_pattern` | Child wins; parents become inherited hints |
| `persona_defaults` | Used only if child identity files are absent |
| `runtime_hints` | Non-binding |
| `context_hints` | Non-binding |
| `protocol_preferences` | Host and child policy win |
| `plugin_requirements` | Dependency declaration only |
| `memory_schema_refs` | Schema union only |
| `evaluation_dimensions` | Union by ID |
| `verifier_refs` | Definition union; approval does not inherit |
| `regression_fixtures` | Union-monotonic |
| `safety_fixtures` | Union-monotonic |
| `failure_taxonomy` | Union by code |
| `observability_labels` | Namespaced union |
| `docs` | Authoring hint only; not injected at runtime |

Unknown surfaces fail closed.

## 6.5 Fixture monotonicity

**FR-INH-301.** Regression and safety fixtures are union-monotonic. A child may not remove an inherited fixture.

Removal requires:

- a signed host-level waiver;
- reason;
- expiry;
- impact assessment;
- compensating fixture or control;
- entry in `inheritance/conflicts.json`;
- human approval.

## 6.6 Compose lock

`generated/compose.lock.json` contains:

- child and parent hashes;
- MRO;
- prompt and rubric hashes;
- skill resolution;
- cache-policy hash;
- context-policy hash;
- compute-controller hash;
- verified capability matrix;
- tokenizer and chat-template digests;
- protocol and adapter versions;
- OTel `schema_url`;
- plugin digests;
- isolation-tier map;
- plugin SBOM digests;
- memory policy, hierarchy, security, and unlearning hashes;
- verifier-set hash;
- safety and termination hashes;
- corrigibility-invariant digest;
- analysis-plan hash;
- regression-fixture-set digest;
- `compose_hash`.

Any change creates a new `compose_hash`.

---

# 7. Performance execution plane

## 7.1 Runtime design

```mermaid
flowchart LR
    U["Task"] --> ADM["SLO admission control<br/>deadline / budget / risk"]
    ADM -->|"reject or queue"| SHED["Bounded response<br/>reason code"]
    ADM --> CC["Compute controller<br/>test-time budget"]
    CC --> MR["Model router"]
    MR --> PL["Planner"]
    PL --> DAG["Typed execution DAG"]

    DAG --> N1["Model node"]
    DAG --> N2["Memory node"]
    DAG --> N3["Tool node A"]
    DAG --> N4["Tool node B"]
    N1 --> J["Join"]
    N2 --> J
    N3 --> J
    N4 --> J

    J --> V["Deterministic validators"]
    V --> SG["Safety gate"]
    SG --> Q{"Pass?"}
    Q -->|yes| O["Output + evidence graph"]
    Q -->|"no; gain expected"| STOP{"Marginal gain > cost?"}
    STOP -->|yes| RF["Bounded refinement"]
    RF --> DAG
    STOP -->|no| X["Fail closed or escalate"]
    Q -->|unsafe| X

    CACHE[("Cache + context plane")] --- MR
    CACHE --- N1
    SCH["Deadline-aware scheduler<br/>goodput objective"] --- DAG
```

## 7.2 Execution IR

The execution IR is `casops.execution_dag.v2`.

Node kinds:

- `model`;
- `tool`;
- `plugin`;
- `memory_read`;
- `memory_write`;
- `peer_agent`;
- `validator`;
- `verifier`;
- `safety_check`;
- `compaction`;
- `branch`;
- `join`;
- `transform`;
- `speculative`;
- `human_gate`.

Every node declares:

- stable `node_id`;
- dependencies;
- typed input and output schemas;
- timeout;
- retry policy;
- side-effect class;
- idempotency;
- cacheability;
- required verified capabilities;
- resource budget;
- context-cost estimate;
- cache-affinity key;
- isolation tier where applicable;
- taint class;
- failure action;
- compensating action for speculative side effects.

## 7.3 Functional requirements

### Base execution requirements

| ID | Requirement |
|---|---|
| FR-PERF-001 | Explicit dependencies must be compiled before execution. |
| FR-PERF-002 | Independent read-only or idempotent nodes should run concurrently. |
| FR-PERF-003 | Unordered side-effecting nodes must not be parallelized. |
| FR-PERF-004 | The scheduler must optimize end-to-end critical-path time. |
| FR-PERF-005 | Every run propagates a deadline and cancellation token. |
| FR-PERF-006 | The router optimizes a declared quality-latency-cost objective. |
| FR-PERF-007 | Route decisions are reproducible from logged features or explicitly stochastic. |
| FR-PERF-008 | Structured output uses constrained decoding when verified and supported. |
| FR-PERF-009 | Prefix/KV caches are keyed by model, tokenizer, template, prompt, capability, tenant, subject, sensitivity, and approval scope. |
| FR-PERF-010 | Cache data must not cross agent, user, tenant, sensitivity, or approval boundaries. |
| FR-PERF-011 | Context reserves separate budgets for policy, task, memory, tools, evidence, and output. |
| FR-PERF-012 | Reflection is triggered by uncertainty, failure, risk, or expected utility—not an unconditional loop. |
| FR-PERF-013 | Speculative decoding must preserve the backend semantics it claims. |
| FR-PERF-014 | Optional optimizer failure may fall back only to a validated baseline. |
| FR-PERF-015 | Every fallback emits telemetry and a reason code. |
| FR-PERF-016 | Model, tool, memory, plugin, and peer concurrency have independent limits. |
| FR-PERF-017 | Acceptance jointly evaluates success, p50/p95 job time, and cost per successful task. |

### v3 requirements

| ID | Requirement |
|---|---|
| FR-PERF-101 | SLO-aware admission control queues or sheds work rather than degrading all in-flight runs. |
| FR-PERF-102 | The scheduling objective is goodput, not throughput or tokens per second. |
| FR-PERF-103 | A compute controller allocates test-time budget from risk, deadline, value, and predicted difficulty and enforces a marginal-gain stopping rule. |
| FR-PERF-104 | Stopping decisions record estimated gain, cost, threshold, and rule version. |
| FR-PERF-105 | Speculative nodes declare a guard and cannot commit side effects before it passes. Abandoned speculation executes compensation. |
| FR-PERF-106 | Critical Path Efficiency is computed per run; sustained low CPE is treated as a scheduling defect. |
| FR-PERF-107 | Router records contain feature vector, candidates, scores, and selection-rule version. |
| FR-PERF-108 | Accelerator utilization is reported only when exposed by the backend; otherwise it is `unavailable`. |
| FR-PERF-109 | Every optional optimizer has an independent, fixture-tested kill switch. Mandatory safety, corrigibility, audit, and permission controls have no bypass switch; their failure invokes containment stop. |
| FR-PERF-110 | Acceptance jointly evaluates CPST, p50/p95/p99 where powered, task success, and goodput. |

## 7.4 Metrics

| Metric | Definition |
|---|---|
| `CPST` | Attributed model, tool, and infrastructure cost divided by successful tasks |
| `goodput` | Tasks that succeed and meet deadline per wall-second per accelerator |
| `CPE` | Ideal critical-path duration divided by actual wall time |
| `CRR` | Reused prefix tokens divided by total prompt tokens |
| `TTFO` | Time to first output token or artifact byte |
| `job_completion_ms` | Admission to artifact sealing |
| `refinement_yield` | Success-rate delta attributable to refinement divided by refinement cost share |

## 7.5 Example compute controller

```json
{
  "schema_version": "3.0",
  "agent_id": "video.showrunner",
  "mode": "adaptive",
  "budget_source": [
    "risk_class",
    "deadline",
    "predicted_difficulty",
    "task_value"
  ],
  "allocation": {
    "min_model_calls": 1,
    "max_model_calls": 6,
    "max_refinements": 3,
    "max_parallel_samples": 2
  },
  "stopping_rule": {
    "type": "marginal_gain_threshold",
    "estimator": "validator_score_delta_ema",
    "min_expected_gain": 0.05,
    "cost_normalizer": "cpst",
    "hard_stop_on": [
      "deadline_80pct",
      "budget_90pct",
      "no_gain_2_consecutive"
    ]
  },
  "audit": {
    "log_gain_estimates": true,
    "log_threshold_version": true
  }
}
```

## 7.6 Per-run fields

Every run records:

- `admission_wait_ms`;
- `shed_reason`;
- `job_completion_ms`;
- `time_to_first_output_ms`;
- `critical_path_ms`;
- `queue_ms`;
- `model_ms`;
- `tool_wait_ms`;
- `memory_ms`;
- `validation_ms`;
- token and cost totals;
- call and retry counts;
- cache tier hits;
- `compute_budget_allocated`;
- `compute_budget_used`;
- `stopping_rule_decisions[]`;
- `cpe`;
- `crr`;
- `context_tokens_by_segment`;
- `compaction_events[]`;
- committed and discarded speculation;
- `kill_switch_engaged[]`;
- `containment_stop_reason`;
- `goodput_contribution`;
- `cpst_contribution`;
- outcome and failure code.

---

# 8. Cache and context-lifecycle plane

Evidence basis retained from the prior draft: agent-aware cache-management and agentic-serving work `[D]`. All such evidence is E3 until audited.

## 8.1 Rationale

Agent runs often reuse:

- long system and policy prefixes;
- tool schemas;
- prompt templates;
- memory excerpts;
- multi-turn context;
- peer-agent artifacts.

Cache can improve performance but creates high-risk failure modes:

- cross-tenant leakage;
- policy staleness;
- approval staleness;
- memory-deletion residue;
- tokenizer or template mismatch;
- approximate semantic false reuse.

Cache is therefore a scheduled, governed plane.

## 8.2 Cache tiers

| Tier | Contents | Correctness guard |
|---|---|---|
| T0 | Tokenized prefix or KV state | Exact key including policy, model, tokenizer, and template digests |
| T1 | Rendered fragments | Source-record version, tenant, subject, trust, and sensitivity |
| T2 | Pure/idempotent node results | Full typed input digest and adapter revision |
| T3 | Approximate semantic reuse | Off by default; independent equivalence verifier and false-reuse gate |

## 8.3 Cache requirements

| ID | Requirement |
|---|---|
| FR-CACHE-001 | Keys include model revision, tokenizer digest, chat-template digest, prompt/policy digest, capability scope, agent, tenant, subject, sensitivity, and approval epoch. |
| FR-CACHE-002 | Entries cannot cross agent, user, tenant, sensitivity, or approval boundaries. Violation aborts and purges. |
| FR-CACHE-003 | Policy, prompt, memory-version, template, tokenizer, capability, or approval changes invalidate dependencies before the next read. |
| FR-CACHE-004 | T3 remains disabled unless an equivalence verifier exists and false reuse is at most 0.5% on the declared fixture. |
| FR-CACHE-005 | Cache-enabled and cache-disabled execution must be correctness-equivalent within the pre-registered margin. |
| FR-CACHE-006 | Every tier has a declared budget and eviction policy. Eviction must not create silent staleness. |
| FR-CACHE-007 | Hits, misses, invalidations, evictions, and scope rejections emit reason-coded telemetry. |
| FR-CACHE-008 | Failure falls back to the uncached validated path without changing permissions or semantics. |
| FR-CACHE-009 | Memory deletion propagates to all cache tiers. |

## 8.4 Context lifecycle

```mermaid
flowchart LR
    A["Segment budgets<br/>policy / task / memory / tools / evidence / output"] --> B["Admit content"]
    B --> C{"Pressure above threshold?"}
    C -->|no| D["Render prompt"]
    C -->|yes| E["Compaction node"]
    E --> F["Summarize while preserving<br/>pinned invariants"]
    F --> G["Offload full content<br/>retain resource reference"]
    G --> H{"Preservation verifier passes?"}
    H -->|yes| D
    H -->|no| I["Escalate or spawn<br/>isolated sub-agent"]
    D --> J["Run"]
    J --> K["Re-grounding checkpoint"]
    K --> J
```

## 8.5 Context requirements

| ID | Requirement |
|---|---|
| FR-CTX-001 | Context is segmented with independent budgets and actual usage recording. |
| FR-CTX-002 | Safety charter, corrigibility constraints, `does_not_own`, disclosure, output schema, and active deadline are pinned and non-compactable. |
| FR-CTX-003 | Compaction runs a preservation verifier. Failure escalates or stops; it never silently proceeds. |
| FR-CTX-004 | Compacted content is offloaded to a retrievable reference and not destroyed mid-run. |
| FR-CTX-005 | Oversized subtasks should use isolated, narrowly briefed sub-agents rather than unbounded parent context. |
| FR-CTX-006 | Long-horizon runs insert configured re-grounding checkpoints. |
| FR-CTX-007 | A context-rot fixture demonstrates non-inferiority to an oracle-short-context condition within the declared margin. |

---

# 9. Compatibility and protocol plane

## 9.1 Canonical interfaces

- `ModelAdapter`
- `ToolAdapter`
- `PeerAdapter`
- `MemoryAdapter`
- `TelemetryAdapter`
- `PluginRuntime`
- `EventAdapter`
- `CacheAdapter`
- `VerifierAdapter`
- `SafetyAdapter`

## 9.2 Base compatibility requirements

| ID | Requirement |
|---|---|
| FR-CMP-001 | Protocol and adapter versions are pinned. |
| FR-CMP-002 | Adapters publish machine-readable capability assertions. |
| FR-CMP-003 | Unknown capabilities fail closed. |
| FR-CMP-004 | Vendor fields remain under `vendor_extensions`. |
| FR-CMP-005 | Vendor extensions cannot override host gates. |
| FR-CMP-006 | Message payloads have JSON Schema or an approved binary schema. |
| FR-CMP-007 | Incompatible major schema versions are rejected. |
| FR-CMP-008 | Bridges preserve trace, deadline, identity, authorization, and taint. |
| FR-CMP-009 | Discovery results are cached only within advertised validity. |
| FR-CMP-010 | Protocol adapters pass conformance fixtures before production. |

## 9.3 Asserted versus verified capabilities

```mermaid
flowchart LR
    A["capability_assertions.json<br/>declared claims"] --> B["Conformance fixture runner"]
    B --> C{"Result"}
    C -->|pass| D["VERIFIED<br/>usable"]
    C -->|fail| E["REFUTED<br/>blocked"]
    C -->|"not exercised"| F["ASSERTED_UNVERIFIED<br/>unusable"]
    D --> G["compatibility-matrix.lock.json"]
    E --> G
    F --> G
    G --> H["Composer binds only VERIFIED"]
```

| ID | Requirement |
|---|---|
| FR-CMP-101 | Every capability is `VERIFIED`, `REFUTED`, or `ASSERTED_UNVERIFIED`. |
| FR-CMP-102 | Only `VERIFIED` capabilities may bind in production. |
| FR-CMP-103 | Conformance reruns after endpoint, model, adapter, tokenizer, template, protocol, or material configuration changes. |
| FR-CMP-104 | A previously verified capability that fails is quarantined as `CMP_CAPABILITY_DRIFT`. |
| FR-CMP-105 | Tokenizer and chat-template digests are pinned and treated as semantic compatibility inputs. |
| FR-CMP-106 | Structured output negotiates an explicit JSON-Schema subset profile. Unsupported constructs fail compose. |
| FR-CMP-107 | Seed or determinism claims require repeat-run verification. Otherwise they are `best_effort`. |

Capability vocabulary includes:

```text
chat
text_generation
streaming
tool_calls
parallel_tool_calls
parallel_tool_calls_verified
structured_output
json_schema
json_schema_profile
embeddings
reranking
vision
audio_input
audio_output
logprobs
seed
token_count
token_count_exact
prefix_cache
prefix_cache_explicit
kv_cache_reuse_across_requests
speculative_decoding
batching
cancellation
cancellation_mid_stream
context_length_verified
tool_choice_forcing
batch_invariant_kernels
```

## 9.4 Telemetry compatibility

| ID | Requirement |
|---|---|
| FR-CMP-108 | The semantic-convention `schema_url` is pinned in `semconv.lock.json` and the compose lock. |
| FR-CMP-109 | Every gate-bearing GenAI attribute is emitted under both the pinned external name and a stable `casops.*` alias. Gates bind to `casops.*`. |
| FR-CMP-110 | A semconv version change raises `CMP_SEMCONV_VERSION` and requires conformance rerun and alias-map review. |
| FR-CMP-111 | The alias map is committed, versioned, and cannot change silently. |

This requirement does not depend on proving that an external convention is currently unstable; it protects CASOPS from any external schema change.

## 9.5 MCP tool protocol

The prior draft lists MCP revisions `2025-03-26`, `2025-06-18`, `2025-11-25`, and `2026-07-28` `[D]`.

| ID | Requirement |
|---|---|
| FR-CMP-112 | Exact MCP revision and SDK digest are pinned. |
| FR-CMP-113 | The host supports the pinned revision and at least one prior supported revision. |
| FR-CMP-114 | Unknown major versions fail closed; unknown minor additions are ignored, not inferred. |
| FR-CMP-115 | Extensions are explicitly allow-listed; unrecognized extensions are inert data. |
| FR-CMP-116 | Discovery is not authorization; discovered but unapproved tools remain unreachable. |
| FR-CMP-117 | Discovery caches expire at advertised validity and invalidate on revision change. |

## 9.6 Peer protocol

A2A remains the preferred external peer adapter, normalized into the CASOPS envelope.

| ID | Requirement |
|---|---|
| FR-CMP-118 | Peer envelopes carry a taint class; external-peer content is data, not instruction. |
| FR-CMP-119 | Bridges preserve trace, deadline, authorization, and taint. |
| FR-CMP-120 | Authorization is explicit, non-transitive, and cannot be widened by a bridge. |
| FR-CMP-121 | Multi-agent exchanges enforce hop, cost, time, and cycle guards. |

## 9.7 Canonical peer envelope

```json
{
  "schema_version": "3.0",
  "message_id": "msg_01",
  "conversation_id": "conv_01",
  "task_id": "task_01",
  "from_agent": "video.showrunner",
  "to_agent": "video.editor",
  "message_type": "handoff",
  "hop_count": 2,
  "max_hops": 6,
  "parts": [
    {
      "kind": "data",
      "schema": "video.cut_brief.v3",
      "content_ref": "artifact://cut-brief/123"
    }
  ],
  "taint": {
    "class": "external_peer",
    "instruction_authority": false
  },
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "deadline": "2026-08-24T20:00:00Z",
  "budget_remaining": {
    "cost_units": 12.5,
    "wall_ms": 18000
  },
  "auth_scope": [
    "artifact:read:cut-brief"
  ],
  "provenance": {
    "compose_hash": "sha256:...",
    "artifact_hash": "sha256:..."
  }
}
```

Private reasoning, unrestricted memory, credentials, and undeclared tool handles must not be transmitted.

---

# 10. Observability and decision provenance

## 10.1 Model

```mermaid
flowchart TB
    RUN["Run root span"]
    RUN --> CMP["Compose span"]
    RUN --> ADM["Admission span"]
    RUN --> PLAN["Planning span"]
    RUN --> ROUTE["Routing span"]
    RUN --> CTX["Context spans"]
    RUN --> MODEL["Model spans"]
    RUN --> TOOL["Tool / plugin spans"]
    RUN --> MEM["Memory spans"]
    RUN --> PEER["Peer spans"]
    RUN --> SAFE["Safety spans"]
    RUN --> VAL["Validation spans"]
    RUN --> IMP["Improvement span"]

    MODEL --> DR["Decision records"]
    TOOL --> DR
    MEM --> DR
    SAFE --> DR
    VAL --> DR

    DR --> EG["Evidence graph<br/>claim to evidence"]
    EG --> ES["Append-only hash-chained store"]
    DR --> ES
    ES --> SAMP["Tail sampling"]
    SAMP --> OTEL["OTel exporter<br/>pinned schema + aliases"]
    ES --> REPLAY["Replay / counterfactual audit"]
    ES --> RCA["Failure classification"]
```

## 10.2 Decision provenance

Every material decision record contains:

- decision, trace, and span IDs;
- agent and compose hash;
- objective;
- observable input references or hashes;
- available actions;
- selected action;
- machine-readable rejection or selection codes;
- evidence and memory references;
- policy results;
- validator and verifier results;
- calibrated confidence where available;
- prompt, model, tokenizer, and template digests;
- timestamps and outcome.

Raw hidden chain-of-thought is neither required nor authoritative.

## 10.3 Internal reasoning monitor

| ID | Requirement |
|---|---|
| FR-OBS-101 | An internal-only reasoning-monitor channel may be enabled for automated safety monitoring. |
| FR-OBS-102 | Its content cannot enter exports, artifacts, memory, peer messages, prompts, evidence graphs, or telemetry payloads. |
| FR-OBS-103 | Retention defaults to at most 24 hours and is encrypted. |
| FR-OBS-104 | Only structured verdicts—risk, category, confidence—may enter telemetry. |
| FR-OBS-105 | Verdicts may block execution but cannot support factual output claims. |

The agent itself cannot read this channel or influence its verdicts.

## 10.4 Claim-level evidence graph

```json
{
  "schema_version": "3.0",
  "artifact_id": "artifact://cut-brief/123",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "claims": [
    {
      "claim_id": "c1",
      "span": {
        "start": 240,
        "end": 318
      },
      "text_hash": "sha256:...",
      "claim_type": "constraint",
      "support": [
        {
          "kind": "memory",
          "ref": "memory://semantic/17",
          "record_version": 3,
          "strength": "direct"
        },
        {
          "kind": "source",
          "ref": "source://director-spec/sha256:...",
          "strength": "direct"
        }
      ],
      "taint_inherited": "none",
      "verifier": {
        "name": "constraint_grounding_v2",
        "result": "pass",
        "score": 0.94
      }
    },
    {
      "claim_id": "c2",
      "span": {
        "start": 402,
        "end": 466
      },
      "claim_type": "inference",
      "support": [
        {
          "kind": "derived",
          "from": ["c1"],
          "strength": "inferred"
        }
      ],
      "verifier": {
        "name": "constraint_grounding_v2",
        "result": "flagged",
        "score": 0.41
      }
    }
  ],
  "unsupported_claim_count": 0,
  "flagged_claim_count": 1
}
```

| ID | Requirement |
|---|---|
| FR-OBS-106 | Claim-bearing artifacts emit an evidence graph. |
| FR-OBS-107 | Claims resolve to `source`, versioned `memory`, `tool_observation`, `derived`, or `unsupported`. |
| FR-OBS-108 | Tainted support propagates its taint to the claim. |
| FR-OBS-109 | Unsupported-claim rate is reported per run and gated. |
| FR-OBS-110 | A memory-write candidate derived from an unsupported claim is rejected. |

## 10.5 Telemetry events

```text
agent.run.started
agent.compose.completed
agent.admission.decided
agent.compute.budget_allocated
agent.compute.stop_decided
agent.route.selected
agent.plan.created
agent.node.started
agent.model.request
agent.model.response
agent.tool.request
agent.tool.response
agent.cache.hit
agent.cache.miss
agent.cache.invalidated
agent.cache.scope_rejected
agent.context.compaction_started
agent.context.compaction_verified
agent.context.regrounded
agent.capability.verified
agent.capability.drift_detected
agent.memory.query
agent.memory.result
agent.memory.page_in
agent.memory.page_out
agent.memory.write.proposed
agent.memory.write.committed
agent.memory.consolidation_completed
agent.memory.poison_suspected
agent.memory.unlearn_verified
agent.peer.message.sent
agent.peer.message.received
agent.safety.injection_detected
agent.safety.taint_propagated
agent.safety.blocked
agent.policy.decision
agent.validation.completed
agent.verifier.completed
agent.refinement.started
agent.evidence.graph_emitted
agent.improvement.candidate_created
agent.improvement.ledger_appended
agent.termination.guard_triggered
agent.corrigibility.attested
agent.corrigibility.violation_detected
agent.run.completed
agent.run.failed
```

Mandatory attributes include:

- identity, trace, span, correlation, and compose IDs;
- MRO;
- model and adapter revisions;
- tokenizer and template digests;
- semconv schema URL;
- capability-lock digest;
- prompt and skill hashes;
- plugin digests;
- tool, memory, and peer IDs;
- timings, tokens, cost, and outcome;
- cache tiers, CRR, CPE;
- context usage and compaction count;
- taint and trust tiers;
- verifier and safety results;
- sampling decision and reason;
- disclosure and expertise mode;
- corrigibility attestation ID.

Gate-bearing fields are emitted under `casops.*`.

## 10.6 Sampling and trace cost

| ID | Requirement |
|---|---|
| FR-OBS-111 | Agent-run sampling is tail-based. |
| FR-OBS-112 | Failures, safety blocks, high-risk work, denials, memory writes, candidates, promotions, rollbacks, capability drift, and corrigibility events receive 100% retention. |
| FR-OBS-113 | Successful low-risk runs may be sampled if the rate and reason are recorded. |
| FR-OBS-114 | Trace-budget exhaustion degrades content capture first, then low-risk sampling. Mandatory categories cannot be dropped. |
| FR-OBS-115 | Aggregate metrics use unsampled counters. |

## 10.7 Content capture

| Level | Behavior |
|---|---|
| `metadata_only` | Default: hashes, schemas, sizes, IDs |
| `redacted` | Approved fields after redaction |
| `encrypted_full` | Explicit approval, encryption, limited retention |
| `disabled` | Only if mandatory local action metadata remains |

Prompts, outputs, memory content, tool arguments, and peer messages default to `metadata_only`.

## 10.8 Integrity, replay, and RCA

- Events are append-only and hash-chained.
- Deterministic runs record seed, model revision, tokenizer, template, environment, and fixtures.
- Without verified batch-invariant kernels, replay is observation-level rather than token-level.
- Exporter failure uses a bounded encrypted local spool.
- If exporter and local audit are both unavailable, high-risk execution containment-stops.
- Failed runs receive a versioned failure classification.
- `RCA@1` is measured on injected single-fault scenarios.
- Counterfactual replay may replace one route, memory, or tool observation.
- Counterfactual runs cannot write memory or publish production artifacts.

---

# 11. Extensible plugin architecture

## 11.1 Kinds

```text
tool
skill_runtime
model_adapter
memory_backend
modality_handler
evaluator
protocol_adapter
validator
router
scheduler_policy
cache_adapter
verifier
safety_adapter
compaction_strategy
consolidation_job
```

Skills are declarative. Plugins are executable. A skill cannot install, sign, tier, grant, or authorize a plugin.

## 11.2 Isolation tiers

| Tier | Mechanism | Threat model | Permitted side effects | Target overhead |
|---|---|---|---|---|
| I0 | In-process | Trusted first-party only | Read-only | Negligible |
| I1 | Capability-based WASM | Buggy or semi-trusted | Pure transform, read-only | ≤1 ms median; ≤3% p95 |
| I2 | Separate process, namespace/seccomp, no ambient network | Semi-trusted third party | Scoped read/write | ≤5% p95 |
| I3 | MicroVM, no host FS, allow-listed egress proxy | Untrusted or adversarial | External effect | ≤15% p95 |

| ID | Requirement |
|---|---|
| FR-PLG-101 | Every plugin is assigned a tier. |
| FR-PLG-102 | Tier meets or exceeds side-effect and provenance minimums. |
| FR-PLG-103 | Third-party or unsigned-origin code cannot run below I2; network-capable code runs at I3. |
| FR-PLG-104 | Downgrade requires a signed, expiring host waiver. |

## 11.3 Object-capability authority

| ID | Requirement |
|---|---|
| FR-PLG-105 | Plugins receive narrow capability handles, never ambient credentials or general clients. |
| FR-PLG-106 | Handles are unforgeable, revocable, expiring, and revoked at node completion. |
| FR-PLG-107 | Plugins cannot enumerate capabilities they were not granted. |
| FR-PLG-108 | Handle delegation is prohibited unless explicitly declared and approved. |

## 11.4 Supply chain

| ID | Requirement |
|---|---|
| FR-PLG-109 | Every production plugin supplies an SBOM. |
| FR-PLG-110 | Every production plugin supplies verifiable build provenance. |
| FR-PLG-111 | Components pass the configured vulnerability threshold. |
| FR-PLG-112 | Signatures verify against approved keys and digests match. |
| FR-PLG-113 | Builds should be reproducible; exceptions require justification. |

## 11.5 Base and lifecycle requirements

| ID | Requirement |
|---|---|
| FR-PLG-001 | Installation requires zero composer-core source changes. |
| FR-PLG-002 | Every interface is typed. |
| FR-PLG-003 | Every plugin declares permissions and limits. |
| FR-PLG-004 | Undeclared network, file, memory, tool, or peer access is blocked. |
| FR-PLG-005 | Plugin code cannot execute during manifest validation. |
| FR-PLG-006 | Unknown or unsigned production plugins fail closed. |
| FR-PLG-007 | Dependency cycles fail closed. |
| FR-PLG-008 | Hot reload requires quiescence or a stateless declaration. |
| FR-PLG-009 | Output remains untrusted until schema and policy validation pass. |
| FR-PLG-010 | Tool plugins are evaluated on function-calling and stateful interaction fixtures `[C]`. |
| FR-PLG-114 | ABI versions use semantic versioning and contract tests. |
| FR-PLG-115 | Deprecated interfaces have a declared support window, defaulting to at least two minor host releases. |
| FR-PLG-116 | Hot swap drains in-flight calls and shadow-validates the replacement. |
| FR-PLG-117 | Manifest validation never executes plugin code. |
| FR-PLG-118 | Plugin output is taint-labelled until validated. |

Lifecycle:

1. discover;
2. schema-validate;
3. verify digest/signature;
4. verify SBOM, provenance, and scan;
5. resolve dependencies;
6. verify compatibility and ABI;
7. assign isolation;
8. evaluate permissions;
9. instantiate without ambient authority;
10. health-check;
11. register typed capabilities;
12. lock and emit event;
13. quiesce before update or removal.

## 11.6 Manifest

```json
{
  "schema_version": "3.0",
  "plugin_id": "video.frame-inspector",
  "version": "3.1.0",
  "kind": "modality_handler",
  "entrypoint": {
    "runtime": "wasm",
    "path": "plugins/frame-inspector/main.wasm"
  },
  "isolation": {
    "tier": "I1",
    "threat_model_ref": "docs/threat-model.md#i1"
  },
  "abi": {
    "interface_version": "2.1",
    "contract_tests": "conformance/frame-inspector/"
  },
  "interfaces": [
    {
      "name": "inspect_frame",
      "input_schema": "schemas/frame-request.json",
      "output_schema": "schemas/frame-result.json",
      "deterministic": true
    }
  ],
  "capabilities_required": [
    {
      "kind": "artifact_read",
      "scope": "artifact://frames/*",
      "handle": "narrow"
    },
    {
      "kind": "memory_read",
      "scope": "resource",
      "handle": "narrow"
    }
  ],
  "permissions": {
    "network": false,
    "filesystem_write": [],
    "tools": [],
    "memory_write": []
  },
  "side_effect_class": "read_only",
  "resource_limits": {
    "cpu_ms": 5000,
    "memory_mb": 512,
    "output_bytes": 1048576,
    "wall_ms": 8000
  },
  "compatibility": {
    "agent_structure": ">=3.0 <4.0",
    "host_api": ">=5.0 <6.0"
  },
  "supply_chain": {
    "sbom_ref": "plugins/supply_chain/frame-inspector.sbom.json",
    "provenance_ref": "plugins/supply_chain/frame-inspector.provenance.json",
    "scan_result_ref": "plugins/supply_chain/frame-inspector.scan.json"
  },
  "integrity": {
    "sha256": "sha256:...",
    "signature_ref": "approval://plugin-signature/123"
  }
}
```

---

# 12. Long-term memory architecture

## 12.1 Stores

| Store | Purpose | Default duration |
|---|---|---|
| Working | Current task state | Run |
| Episodic | Attempts, outcomes, reflections | Configured |
| Semantic | Verified facts and relationships | Configured |
| Procedural | Reusable methods and workflows | Configured |
| Resource | Documents and multimodal artifacts | Configured |
| Profile/core | Explicit preferences and durable identity facts | Until changed or deleted |
| Evidence vault | Immutable sources, approvals, validation evidence | Policy-controlled |

This is an engineering taxonomy, not a biological-equivalence claim.

## 12.2 Paged hierarchy

| Tier | Residency | Target | Contents |
|---|---|---|---|
| H0 | In context | Immediate | Pinned invariants, core profile, active state |
| H1 | Indexed warm store | p95 ≤150 ms | Recent episodic and active semantic/procedural |
| H2 | Cold archive | p95 ≤2 s | Historical, superseded, large resources |
| H3 | Frozen evidence vault | Policy-defined | Sources, approvals, validation evidence |

| ID | Requirement |
|---|---|
| FR-MEM-101 | Every tier has a residency budget. |
| FR-MEM-102 | Page-in/out emits trigger, token cost, latency, and tier. |
| FR-MEM-103 | H0 page-out preserves a retrievable reference and task-critical state. |
| FR-MEM-104 | Pinned invariants are non-evictable from H0. |
| FR-MEM-105 | Memory token cost is attributed by tier. |

## 12.3 Record

```json
{
  "schema_version": "3.0",
  "memory_id": "mem_01",
  "agent_id": "video.showrunner",
  "tenant_scope": "project:series-a",
  "subject_scope": "user:hashed-id",
  "memory_type": "semantic",
  "tier": "H1",
  "status": "verified",
  "content_ref": "encrypted://memory/mem_01",
  "summary": "Approved exterior-shoot curfew is 22:00 local time.",
  "entities": [
    "location:lot-a",
    "policy:curfew"
  ],
  "relations": [
    {
      "subject": "location:lot-a",
      "predicate": "has_curfew",
      "object": "22:00"
    }
  ],
  "valid_time": {
    "from": "2026-08-01T00:00:00Z",
    "to": null
  },
  "transaction_time": "2026-08-24T12:00:00Z",
  "source_refs": [
    "artifact://approval/curfew-2026"
  ],
  "provenance_chain": [
    "human_approval:appr_77"
  ],
  "trust_tier": "T0_human_verified",
  "taint": {
    "class": "none",
    "instruction_authority": false
  },
  "confidence": {
    "value": 1.0,
    "basis": "human_approval"
  },
  "sensitivity": "internal",
  "retention_class": "project_lifetime",
  "supersedes": [],
  "conflicts_with": [],
  "access_stats": {
    "reads": 41,
    "last_read": "2026-08-23T09:12:00Z",
    "contributed_to_success": 38
  },
  "quality": {
    "utility_score": 0.92,
    "staleness_risk": "low"
  },
  "created_by_trace": "trace_01"
}
```

## 12.4 Trust tiers

| Tier | Origin | Treatment |
|---|---|---|
| `T0_human_verified` | Human approval or signed source | Authoritative constraint |
| `T1_validator_verified` | Deterministic validation | Usable with source |
| `T2_source_grounded` | Provenanced source | Usable with displayed provenance |
| `T3_agent_inferred` | Unverified inference | Advisory only |
| `T4_quarantined` | Untrusted or suspect | Not retrievable into prompts |

**FR-MEM-106.** T3 cannot appear as factual evidence or override T0/T1.

## 12.5 Lifecycle

```mermaid
flowchart LR
    OBS["Observation / outcome"] --> TAINT["Taint + trust classify"]
    TAINT --> CAND["Candidate extraction"]
    CAND --> RED["Redact + sensitivity classify"]
    RED --> PROV["Attach provenance + time"]
    PROV --> POIS["Poisoning / injection screen"]
    POIS --> DEDUP["Deduplicate + conflict check"]
    DEDUP --> Q{"Verified?"}
    Q -->|no| QUAR["Quarantine T4"]
    Q -->|yes| STORE["Typed store + tier"]
    STORE --> LINK["Entity / relation / temporal graph"]
    LINK --> CONS["Offline consolidation"]

    QUERY["Task query"] --> QP["Query planner"]
    QP --> HYB["Lexical + dense + graph + temporal"]
    HYB --> RERANK["Rerank + diversify"]
    RERANK --> TRUST["Trust filter"]
    TRUST --> VERIFY["Source + conflict verification"]
    VERIFY --> INJECT["Budgeted page-in"]

    STORE --> RET["Retention / decay / deletion"]
    RET --> TOMB["Tombstone propagation"]
    TOMB --> UNL["Unlearning verification"]
```

## 12.6 Retrieval

Retrieval supports:

1. metadata, agent, tenant, and subject filtering;
2. lexical retrieval;
3. dense retrieval;
4. optional graph traversal;
5. temporal filtering and query expansion;
6. deterministic or learned reranking;
7. diversity control;
8. token budgeting;
9. source verification;
10. conflict-aware abstention.

| ID | Requirement |
|---|---|
| FR-MEM-107 | Trust filtering occurs before context injection. |
| FR-MEM-108 | Configured graph stores support validity-aware temporal traversal `[K]`. |
| FR-MEM-109 | Retrieval returns the latest valid version and material unresolved conflicts. |
| FR-MEM-110 | Irreconcilable conflict or insufficient coverage produces abstention. |
| FR-MEM-111 | Retrieval reports token cost and utility attribution. |

## 12.7 Offline consolidation

| ID | Requirement |
|---|---|
| FR-MEM-112 | Consolidation runs as scheduled offline work, not inline in latency-bound serving. |
| FR-MEM-113 | Consolidation output is a candidate and cannot exceed the trust of its lowest-tier input. |
| FR-MEM-114 | Superseded originals remain until retention policy expires them. |
| FR-MEM-115 | Consolidation has independent capacity and cannot consume serving reservations. |

## 12.8 Write policy

Allowed writes include:

- explicit preferences;
- sourced verified facts;
- successful outcomes;
- approved procedures;
- validator-confirmed lessons;
- human corrections;
- versioned task state.

The system must not directly commit:

- raw chain-of-thought;
- unsupported persona claims;
- unsupported evidence-graph claims;
- untrusted tool or peer instructions;
- content without provenance;
- secrets outside approved vaults;
- inferred sensitive traits;
- cross-tenant data;
- transient errors as durable rules;
- T3 inference as verified fact;
- tainted content without independent verification;
- consolidation output above input trust.

## 12.9 Conflict, deletion, and unlearning

- Changes create new versions.
- Older records are superseded, not silently overwritten.
- Valid and transaction time remain distinct.
- Contradictions persist until resolved or expired.
- The agent cannot silently choose the convenient conflict.

| ID | Requirement |
|---|---|
| FR-MEM-116 | Tombstones propagate to records, indexes, caches, summaries, embeddings, graph edges, consolidation output, and flagged derived artifacts. |
| FR-MEM-117 | Post-deletion probes verify absence through lexical, dense, graph, and cache paths. |
| FR-MEM-118 | Completion and latency are audited against the retention SLA. |
| FR-MEM-119 | Legal-hold evidence is excluded from decay/deletion and the exclusion is auditable. |
| FR-MEM-120 | If memory-derived data entered model training, deletion records the weight-level limitation and flags retraining review. |

## 12.10 Metrics

| Metric | Definition |
|---|---|
| `TCE` | Memory tokens injected divided by correct answers attributable to memory |
| `unsupported_memory_answer_rate` | Memory-using answers without valid provenance divided by memory-using answers |
| `staleness_rate` | Answers using a superseded record when a current record existed |
| `MPR` | 1 minus successful poisoning attacks divided by attempts |
| `DCR` | Verified-complete deletions divided by deletion requests |
| `page_in_cost` | Tokens and latency attributable to page-in |

## 12.11 Evaluation

Required categories:

- extraction;
- multi-session reasoning;
- temporal reasoning;
- update;
- abstention;
- long-form and multimodal memory;
- retrieval;
- test-time learning;
- long-range understanding;
- selective forgetting;
- memory-to-action;
- poisoning resistance;
- deletion and unlearning verification;
- staleness after update.

A public benchmark score alone cannot satisfy the memory gate. Contamination checks and domain golden tasks are mandatory.

---

# 13. Autonomous self-improvement

## 13.1 Levels and writable locations

| Level | Scope | Default | Writable location |
|---|---|---|---|
| L0 | Disabled | Production default | Nothing |
| L1 | Per-run retry, reflection, bounded search | Budgeted | Run-local state |
| L2 | Candidate memory, prompt, context, rubric, router | Propose-only | `improvement/candidates/` |
| L3 | Candidate workflow or plugin | Sandbox only | Sandbox and candidates |
| L4 | Model adapter or LoRA-style weights | Separate trainer | Trainer artifacts |
| L5 | Core source or self-rewriting architecture | Research-only | Isolated research environment |

Never writable:

- corrigibility;
- safety policy;
- termination policy;
- permissions;
- tools and plugin grants;
- credentials;
- telemetry mandatory-retention configuration;
- redaction policy;
- gate thresholds;
- held-out sets;
- analysis plans;
- production activation;
- isolation-tier downgrades;
- regression-fixture removal.

## 13.2 Loop

```mermaid
flowchart TB
    OUT["Task outcome"] --> CLS["Failure classification"]
    CLS --> ATTR["Specific cause"]
    ATTR --> VER{"Independent verifier exists?"}
    VER -->|no| BLOCK["Reject objective"]
    VER -->|yes| OBJ["Select measurable objective"]
    OBJ --> GEN["Generate candidate"]
    GEN --> SB["Isolated sandbox"]

    SB --> F1["Functional"]
    SB --> F2["Held-out quality"]
    SB --> F3["Safety"]
    SB --> F4["Latency / cost / goodput"]
    SB --> F5["Compatibility"]
    SB --> F6["Observability"]
    SB --> F7["Full regression suite"]
    SB --> F8["Reward-hacking detectors"]

    F1 --> STAT{"Powered gates pass?"}
    F2 --> STAT
    F3 --> STAT
    F4 --> STAT
    F5 --> STAT
    F6 --> STAT
    F7 --> STAT
    F8 --> STAT

    STAT -->|no| ARC["Archive + ledger"]
    STAT -->|yes| SHAD["Shadow then canary"]
    SHAD --> HUM{"Independent human approval"}
    HUM -->|approve| SIGN["Sign + version + ledger"]
    SIGN --> DEP["Deploy"]
    DEP --> MON["Monitor"]
    MON -->|regression| RB["Automatic rollback"]
    HUM -->|reject| ARC
    ARC --> RAT["Failure becomes fixture"]
    RB --> RAT
```

## 13.3 Attribution

“Task failed” is insufficient. Cause codes include:

- route failure;
- missing or incorrect memory;
- retrieval granularity;
- malformed tool call;
- plugin defect;
- workflow dependency;
- inadequate validation;
- prompt ambiguity;
- protocol incompatibility;
- budget exhaustion;
- context overflow;
- compaction loss;
- cache staleness;
- capability drift;
- injection compromise;
- termination trip;
- verifier gap.

## 13.4 Candidate types and generators

Candidate types:

```text
memory_correction
prompt_patch
context_playbook
rubric_patch
router_update
workflow_patch
plugin_patch
protocol_mapping
model_adapter
evaluation_fixture
```

| Generator | Scope | Evidence | Default |
|---|---|---|---|
| Reflective prompt/context evolution | Prompt and context candidates | E2/E3 `[K]` | Preferred for auditability |
| Workflow search | Workflow candidate | E2 `[C]` | Gated |
| Router optimization | Router update | E1/E2 `[C]` | Bounded and shadowed |
| Memory correction | Memory candidate | E2 | L2 with provenance |
| Trajectory trainer | Model adapter | E3 `[C]` | L4, out of process |
| Fixture synthesis | Evaluation fixture | E1 | Encouraged; no held-out access |

The preference for reflective evolution is operational: readable diffs, reversibility, lower infrastructure burden, and direct human review. Any empirical sample-efficiency claim remains citation-gated.

## 13.5 Candidate requirements

Every candidate contains:

- candidate ID and parent version;
- mutation scope;
- generating traces and failure codes;
- exact diff or artifact;
- expected benefit;
- risk and blast-radius assessment;
- training, evaluation, and holdout hashes;
- model, tool, adapter, template, and tokenizer versions;
- benchmark, safety, cost, and latency results;
- verifier identity and independence attestation;
- reward-hacking detector results;
- full regression results;
- statistical report;
- corrigibility attestation;
- rollback artifact;
- signature state.

## 13.6 Verifier and reward integrity

| ID | Requirement |
|---|---|
| FR-IMP-101 | Every objective names a verifier. |
| FR-IMP-102 | Model judges are independent by model family or independently calibrated prompt lineage. |
| FR-IMP-103 | Detectors cover verbosity, judge mimicry, memorization, refusal gaming, format exploitation, and metric/golden-task divergence. |
| FR-IMP-104 | Golden-task degradation rejects the candidate regardless of target-metric gain. |
| FR-IMP-105 | Held-out sets are cryptographically isolated. |
| FR-IMP-106 | Fixture rotation is host-controlled. |

## 13.7 Failure-to-fixture ratchet

| ID | Requirement |
|---|---|
| FR-IMP-107 | Every confirmed attributable failure creates a regression fixture before fix promotion. |
| FR-IMP-108 | Fixtures are permanent and union-monotonic absent signed waiver. |
| FR-IMP-109 | Every promotion passes the full suite; “known flaky” is not an exemption. |
| FR-IMP-110 | Suite size and pass rate appear in every validation report. |

## 13.8 Learning separation

Trajectories may be exported to a trainer. Gradient updates must not execute in the serving process.

Online serving updates may include:

- bounded router statistics;
- cache TTL estimates;
- quarantined reflections;
- memory indexes;
- non-executable task statistics;
- propose-only context playbooks.

They must not include:

- base-weight mutation;
- unsigned adapter promotion;
- plugin replacement;
- core source mutation;
- permission, tool, network, gate, telemetry, safety, or termination changes.

## 13.9 Core self-modification

L5 requires:

- isolated environment;
- no production credentials;
- disabled or tightly simulated outbound network;
- approved writable repositories only;
- separated evaluation sets;
- human approval for every promotion;
- signed rollback.

It is never a standard production capability.

## 13.10 Improvement ledger

**FR-IMP-111.** Candidate creation, evaluation, statistics, approval, rejection, promotion, monitoring, and rollback append to an immutable hash-chained ledger. The agent cannot rewrite promotion-boundary entries.

---

# 14. Safety and adversarial-robustness plane

## 14.1 Threat model

| Threat | Vector | Primary controls |
|---|---|---|
| Direct injection | User input | Instruction/data separation, taint |
| Indirect injection | Documents, tools, web, memory, peers | Taint propagation, no instruction authority |
| Memory poisoning | Persisted malicious content | Trust tiers, quarantine, MPR gate |
| Tool or agent hijacking | Redirected external actions | Allow-lists, confirmation, hijack tests |
| Exfiltration | Induced secret or PII output | Egress allow-list, outbound scanning |
| Supply chain | Malicious plugin/dependency | SBOM, provenance, signature, isolation |
| Excessive agency | Loops, spend, side effects | Hard caps, termination, compensation |
| Multi-agent cascade | Peer amplification | Hop caps, cycle detection, shared budget |
| Control bypass | Candidate or plugin alters safeguards | Corrigibility and negative fixtures |

## 14.2 Taint propagation

| ID | Requirement |
|---|---|
| FR-SAF-001 | Every item has a taint class: operator, user, tool, untrusted retrieval, external peer, or memory trust tier. |
| FR-SAF-002 | Taint propagates through transforms, summaries, compaction, and consolidation. |
| FR-SAF-003 | Tainted content has `instruction_authority:false`. |
| FR-SAF-004 | Taint-derived external effects require allow-list match, deterministic validation, or human confirmation. |
| FR-SAF-005 | Outbound content passes secret and PII scanning. |
| FR-SAF-006 | Safety cannot be disabled or bypassed by agent, skill, plugin, or persona. |

## 14.3 Termination and excessive-agency guards

| ID | Requirement |
|---|---|
| FR-SAF-007 | Every run has hard limits for time, cost, model calls, tool calls, peer hops, refinements, and plan expansions. |
| FR-SAF-008 | Progress-free loops halt after a configured non-improvement window. |
| FR-SAF-009 | Peer cycles halt. |
| FR-SAF-010 | Guard trips return explicit bounded failure, never silent truncated success. |
| FR-SAF-011 | Near a cap, partial result with disclosure is preferred to unsafe completion. |

## 14.4 Release gates

| Gate | Threshold |
|---|---|
| Indirect injection | Observed attack success ≤2%, with no privilege escalation or secret exfiltration |
| Memory poisoning | MPR ≥95%; no poisoned content reaches T0/T1 |
| Tool hijack | No unapproved external-effect action |
| Exfiltration | No secret or PII egress |
| Termination | All loop, hop, cycle, and budget fixtures halt correctly |
| Taint integrity | All laundering fixtures blocked |
| Multi-agent cascade | No cross-agent privilege or taint escalation |

Zero-tolerance categories are literal operational gates. Reports must also provide exact binomial confidence bounds; zero observed events is not represented as proof of zero population risk.

## 14.5 Incident handling

**FR-SAF-012.** Safety blocks, suspected injection, exfiltration attempts, and guard trips create incident records containing:

- trace;
- taint chain;
- attempted action;
- detection path;
- disposition;
- operator notification;
- resulting regression fixture.

---

# 15. Corrigibility plane

## 15.1 Invariants

| ID | Invariant |
|---|---|
| INV-01 | The agent cannot modify permissions, tools, or plugin grants. |
| INV-02 | It cannot modify safety or termination policy. |
| INV-03 | It cannot modify mandatory telemetry retention or redaction policy. |
| INV-04 | It cannot modify gate thresholds, held-out sets, or analysis plans. |
| INV-05 | It cannot request production activation or grant network access. |
| INV-06 | It cannot approve, sign, or promote candidates. |
| INV-07 | It cannot delete or rewrite audit, ledger, or incident records. |
| INV-08 | It cannot disable, degrade, or bypass safety. |
| INV-09 | It cannot remove regression or safety fixtures. |
| INV-10 | It cannot suppress, delay, or reorder shutdown, cancellation, or deadline signals. |
| INV-11 | It cannot read the reasoning-monitor channel or influence verdicts. |
| INV-12 | It cannot lower plugin isolation or forge capability handles. |

## 15.2 Enforcement

| ID | Requirement |
|---|---|
| FR-COR-001 | Enforcement uses separate ownership, storage, and capability absence—not policy checks alone. |
| FR-COR-002 | Every compose attests the invariant digest against a host-held reference. |
| FR-COR-003 | Mismatch invokes immediate containment stop and operator alert. No degraded mode exists. |
| FR-COR-004 | Shutdown and cancellation are honored at every node boundary and enforceably terminate plugin invocations. |
| FR-COR-005 | Candidates touching invariant surfaces are rejected at generation time and alerted. |
| FR-COR-006 | INV-01 through INV-12 each have a negative fixture. Untested invariants are assumed broken. |

Mandatory controls have no bypass kill switch. Their only emergency switch is containment stop.

---

# 16. Skills, identity, and persona isolation

## 16.1 Skill resolution

```text
resolved_enabled =
    declared_or_inherited
AND author_enabled
AND inherited_enabled
AND operator_toggle
AND host_permission
```

| ID | Requirement |
|---|---|
| FR-SKL-001 | Bindings include `skill_id`, source, path, and enabled state. |
| FR-SKL-002 | Missing `enabled` defaults to true. |
| FR-SKL-003 | Operator toggles record reason, actor, and time. |
| FR-SKL-004 | A toggle cannot enable an undeclared or uninherited skill. |
| FR-SKL-005 | Enabling cannot add tools outside child and host grants. |
| FR-SKL-006 | Disabled skills do not enter prompts, tools, memory, cache, evidence, or critique. |
| FR-SKL-007 | Artifacts record loaded and disabled skills. |
| FR-SKL-008 | Duplicate IDs collapse and enabled state is AND-combined. |
| FR-SKL-009 | Unknown skill IDs fail closed. |
| FR-SKL-010 | Enabled skills with missing required files fail closed. |

A skill may reference an approved plugin but cannot install, sign, tier, or authorize it.

## 16.2 Identity modes

- `grounded`;
- `persona_overlay`;
- `mixed`.

| ID | Requirement |
|---|---|
| FR-IDN-001 | Missing identity files imply `grounded`. |
| FR-IDN-002 | Persona may define voice, register, temperament, values, taboos, and languages. |
| FR-IDN-003 | Background may define title, domain, specialties, fictional experience range, methods, education style, and credit style. |
| FR-IDN-004 | Background is fictional unless a provenance-linked human approval authorizes a real person. |
| FR-IDN-005 | Named-person personas require an approval ID and digest. |
| FR-IDN-006 | Persona cannot alter tools, network, budgets, permissions, safety, or activation. |
| FR-IDN-007 | Every non-grounded artifact displays disclosure and `disclosure_id`. |
| FR-IDN-008 | Ungrounded craft claims are `persona_claim` and cannot support factual gates. |
| FR-IDN-009 | Persona cannot claim real professional licenses or legal standing. |
| FR-IDN-010 | Child identity overrides parent persona defaults. |
| FR-IDN-011 | User psychological profiles are not copied into agent identity. |
| FR-IDN-012 | Listed languages constrain supported output locales but do not invent support. |

Persona additionally cannot affect:

- route-quality labels;
- capability verification;
- cache scope;
- memory trust;
- taint;
- safety verdicts;
- termination;
- evidence support;
- verifier selection;
- corrigibility.

---

# 17. Compose and runtime algorithm

## 17.1 Compose

1. Validate folder and JSON Schemas.
2. Attest corrigibility invariants before executable resolution.
3. Validate identity and disclosure.
4. Resolve MRO and hashes.
5. Enforce fixture monotonicity.
6. Merge content and tightening-only safety fields.
7. Resolve skills.
8. Discover plugin manifests without execution.
9. Verify signatures, digests, SBOMs, provenance, scans, ABI, permissions, dependencies, and isolation.
10. Resolve model, cache, protocol, verifier, and safety adapters.
11. Run capability conformance and write the verified matrix.
12. Pin tokenizer, template, protocol, adapter, and semconv revisions.
13. Bind memory stores, hierarchy, security, retention, and unlearning.
14. Bind telemetry, sampling, redaction, and local spool.
15. Bind cache and context budgets.
16. Validate verifier independence.
17. Compile the execution DAG and validate side-effect safety.
18. Apply tools, network, tenant, budget, and production gates.
19. Generate locks and `compose_hash`.
20. Run preview, safety, and negative-invariant fixtures.
21. Permit execution only if mandatory checks pass.

## 17.2 Run

1. Start the root trace.
2. Admit, queue, or shed based on risk, deadline, budget, and capacity.
3. Allocate test-time compute.
4. Query memory, trust-filter, and page in under budget.
5. Select and record the route.
6. Build or load the DAG.
7. Execute safe nodes concurrently.
8. Validate and taint-label all external results.
9. Compact only with preservation verification.
10. Re-ground at checkpoints.
11. Refine only while expected gain exceeds cost.
12. Run the safety gate.
13. Produce output, evidence graph, provenance, and disclosure.
14. Commit only verified memory writes.
15. Record metrics and failure classification.
16. Optionally create, but never promote, candidates.
17. Create regression fixtures for confirmed failures.
18. Close trace and seal the artifact.

## 17.3 Prompt envelope

1. Host safety charter — pinned
2. Corrigibility and permission constraints — pinned
3. Protocol constraints
4. Disclosure — pinned
5. Persona voice
6. Child mission and `does_not_own` — pinned
7. Inherited support fragments
8. Taint-labelled, trust-filtered memory
9. Enabled skills
10. Child primary prompt
11. Labelled inherited prompts
12. Tool and plugin schemas
13. Output schema — pinned
14. Rubric and validators
15. Deadline and remaining budget — pinned

---

# 18. Data models

## 18.1 `agent_spec.json`

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.showrunner",
  "status": "registered",
  "role": "ShowrunnerAgent (VA Domain Pack)",
  "allowed_tools": [],
  "allowed_plugins": [],
  "model_policy": {
    "provider": "local_deterministic",
    "model_id": "local-video-config",
    "network_access": false,
    "routing_allowed": true
  },
  "budget_policy": {
    "max_input_tokens": 4096,
    "max_output_tokens": 1536,
    "max_model_calls": 4,
    "max_tool_requests": 0,
    "max_job_ms": 45000,
    "max_cost_units": 8.0,
    "max_peer_hops": 4
  },
  "prompt_reference": "video.prompt.showrunner.v3",
  "rubric_reference": "video.rubric.showrunner.v3",
  "critique_edges": {
    "inputs": ["video.critic"],
    "outputs": ["video.judge"]
  },
  "max_refinement_count": 3,
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

## 18.2 Artifact metadata

Every output includes:

- agent and structure IDs;
- compose and capability locks;
- MRO and parent hashes;
- skills and plugins;
- model, route, tokenizer, and template;
- semconv schema;
- plan and trace IDs;
- memory reads/writes and trust tiers;
- cache tier hits, CRR, and CPE;
- context use and compaction;
- compute budget and stopping rule;
- evidence-graph ID;
- unsupported-claim rate;
- taint and safety verdicts;
- termination state;
- verifier results;
- regression-suite digest;
- corrigibility attestation;
- goodput and CPST contribution;
- expertise mode and disclosure.

## 18.3 Improvement policy

```json
{
  "schema_version": "3.0",
  "agent_id": "video.showrunner",
  "mode": "propose",
  "allowed_scopes": [
    "memory_correction",
    "prompt_patch",
    "context_playbook",
    "evaluation_fixture"
  ],
  "forbidden_scopes": [
    "production_activation",
    "permission_change",
    "credential_change",
    "core_source",
    "base_model_weights",
    "safety_policy",
    "termination_policy",
    "telemetry_retention",
    "gate_thresholds",
    "holdout_sets",
    "corrigibility_invariants",
    "isolation_tier",
    "regression_fixture_removal"
  ],
  "auto_promote": false,
  "requires_independent_evaluator": true,
  "requires_human_approval": true,
  "requires_verifier": true,
  "requires_full_regression_pass": true,
  "requires_safety_suite_pass": true,
  "requires_statistical_plan": "evals/analysis_plan.json",
  "reward_hacking_detectors": [
    "length_exploit",
    "judge_mimicry",
    "fixture_memorization",
    "refusal_gaming",
    "format_exploit",
    "golden_task_divergence"
  ],
  "canary": {
    "strategy": "group_sequential",
    "max_traffic_pct": 5,
    "guardrails": [
      "success_rate",
      "cpst",
      "p95_job_ms",
      "safety_block_rate",
      "unsupported_claim_rate"
    ]
  },
  "rollback_required": true,
  "ledger_ref": "improvement/ledger.json"
}
```

---

# 19. Operator and host APIs

All v2 routes are preserved under `/api/v3/...`.

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/v3/agents/{id}/structure` | Structure and schema |
| GET | `/api/v3/agents/{id}/resolved` | MRO, capabilities, locks |
| POST | `/api/v3/agents/{id}/compose-preview` | Full dry run |
| GET | `/api/v3/agents/{id}/runtime/plan` | Compiled DAG |
| GET | `/api/v3/agents/{id}/runtime/capabilities` | Runtime capability view |
| GET | `/api/v3/agents/{id}/capabilities/matrix` | Asserted, verified, refuted |
| POST | `/api/v3/agents/{id}/capabilities/verify` | Run conformance |
| GET | `/api/v3/agents/{id}/runtime/context-budget` | Segment budget and use |
| GET | `/api/v3/agents/{id}/cache/stats` | Per-tier statistics |
| POST | `/api/v3/agents/{id}/cache/invalidate` | Audited scoped invalidation |
| GET | `/api/v3/agents/{id}/protocols` | Protocol state |
| GET | `/api/v3/agents/{id}/plugins` | Resolved plugins |
| POST | `/api/v3/agents/{id}/plugins/validate` | Validate without load |
| GET | `/api/v3/agents/{id}/memory/policy` | Memory policy |
| GET | `/api/v3/agents/{id}/memory/hierarchy` | Residency and paging |
| POST | `/api/v3/agents/{id}/memory/query` | Audited query |
| POST | `/api/v3/agents/{id}/memory/write-candidate` | Propose write |
| POST | `/api/v3/agents/{id}/memory/consolidate` | Trigger offline job |
| DELETE | `/api/v3/agents/{id}/memory/{memory_id}` | Controlled deletion |
| POST | `/api/v3/agents/{id}/memory/{memory_id}/verify-deletion` | Run deletion probes |
| GET | `/api/v3/traces/{trace_id}` | Operational trace |
| POST | `/api/v3/traces/{trace_id}/replay` | Dry replay |
| POST | `/api/v3/traces/{trace_id}/replay?counterfactual=` | Counterfactual replay |
| GET | `/api/v3/traces/{trace_id}/root-cause` | Failure classification |
| GET | `/api/v3/artifacts/{id}/evidence-graph` | Claim attribution |
| GET | `/api/v3/agents/{id}/safety/incidents` | Incident records |
| POST | `/api/v3/agents/{id}/safety/redteam` | Robustness suite |
| GET | `/api/v3/agents/{id}/improvement/candidates` | Candidate list |
| POST | `/api/v3/agents/{id}/improvement/candidates/{cid}/evaluate` | Sandbox evaluation |
| POST | `/api/v3/agents/{id}/improvement/candidates/{cid}/approve` | Human approval |
| POST | `/api/v3/agents/{id}/improvement/rollback/{version}` | Rollback |
| GET | `/api/v3/agents/{id}/improvement/ledger` | Improvement ledger |
| GET | `/api/v3/agents/{id}/regression/suite` | Fixture inventory |
| GET | `/api/v3/agents/{id}/corrigibility/attestation` | Invariant attestation |
| GET | `/api/v3/agents/{id}/validation/report` | Full report |

All mutations require:

- authenticated actor;
- reason;
- expected parent version;
- dry-run response;
- append-only audit;
- explicit human approval for production effects.

No agent-identity endpoint can write corrigibility invariants.

---

# 20. Consolidated error catalogue

## 20.1 Inheritance, skills, and identity

| Code | Condition | Default action |
|---|---|---|
| `INH_CYCLE` | Parent graph cycle | Abort |
| `INH_PARENT_MISSING` | Parent folder or required file missing | Abort |
| `INH_STRUCTURE_MISMATCH` | Incompatible family | Abort |
| `INH_DEPTH` | Depth exceeds limit | Abort |
| `INH_PARENT_LIMIT` | Parent limit exceeded | Abort |
| `INH_SURFACE_UNKNOWN` | Unknown inherited surface | Abort |
| `INH_SELF_PARENT` | Child names itself | Abort |
| `INH_RESOLVED_DRIFT` | Generated resolution differs from source hashes | Abort |
| `INH_FIXTURE_REMOVAL` | Fixture removed without waiver | Abort |
| `SKL_TOGGLE_UNKNOWN` | Toggle targets unknown skill | Abort |
| `SKL_MISSING_FILES` | Enabled skill lacks required files | Abort |
| `SKL_TOOL_LEAK` | Skill attempts undeclared tool grant | Abort |
| `IDN_NAMED_PERSON` | Named-person overlay lacks approval | Abort |
| `IDN_LICENSE_CLAIM` | Persona asserts a real license | Abort |
| `IDN_DISCLOSURE_MISSING` | Overlay lacks disclosure | Abort |
| `GATE_NETWORK` | Inheritance or identity attempts network grant | Abort |
| `GATE_ACTIVATION` | Agent attempts production activation | Abort |

## 20.2 Performance, cache, and context

| Code | Condition | Default action |
|---|---|---|
| `PERF_PLAN_CYCLE` | DAG cycle | Abort |
| `PERF_UNSAFE_PARALLELISM` | Unsafe side-effect concurrency | Abort |
| `PERF_BUDGET_EXCEEDED` | Compile-time budget infeasible | Abort or escalate |
| `PERF_DEADLINE` | Deadline exceeded | Cancel with bounded failure |
| `PERF_CACHE_SCOPE` | Cache crosses boundary | Abort and purge |
| `PERF_ROUTE_UNAVAILABLE` | Route unavailable | Approved fallback only |
| `PERF_STOP_RULE` | Stopping rule absent or unauditable | Abort adaptive mode |
| `PERF_SPECULATION_COMMIT` | Speculation commits before guard | Abort and compensate |
| `PERF_FALLBACK_INVALID` | Fallback lacks validation | Containment stop |
| `CACHE_INVALIDATION` | Dependency not invalidated before read | Disable tier and purge |
| `CACHE_EQUIVALENCE` | Cached and baseline semantics diverge | Disable tier |
| `CACHE_SEMANTIC_REUSE` | T3 exceeds false-reuse threshold | Disable T3 |
| `CTX_PRESERVATION` | Compaction loses invariant or critical constraint | Escalate or stop |
| `CTX_BUDGET` | Required pinned context exceeds budget | Reject or split task |

## 20.3 Compatibility and observability

| Code | Condition | Default action |
|---|---|---|
| `CMP_PROTOCOL_VERSION` | Unsupported protocol revision | Abort |
| `CMP_CAPABILITY_MISSING` | Required capability absent | Abort |
| `CMP_ASSERTED_UNVERIFIED` | Production binding targets unverified capability | Abort |
| `CMP_CAPABILITY_DRIFT` | Verified capability later fails | Quarantine route |
| `CMP_SCHEMA_INCOMPATIBLE` | Schema major mismatch | Abort |
| `CMP_TRACE_CONTEXT` | Trace/deadline/auth/taint lost | Abort high-risk exchange |
| `CMP_SEMCONV_VERSION` | Semconv changes | Quarantine export mapping |
| `CMP_TEMPLATE_DRIFT` | Template digest changes | Re-run conformance |
| `CMP_TOKENIZER_DRIFT` | Tokenizer digest changes | Re-run conformance |
| `CMP_JSON_SCHEMA_PROFILE` | Unsupported schema construct | Fail compose |
| `OBS_TRACE_BROKEN` | Root or parent span missing | Abort high-risk run |
| `OBS_REDACTION` | Content cannot be safely redacted | Metadata only or abort |
| `OBS_COT_EXPORT` | Hidden reasoning targeted for export | Block and alert |
| `OBS_AUDIT_UNAVAILABLE` | Exporter and local audit unavailable | Containment stop |
| `OBS_SAMPLING_LOSS` | Mandatory trace category would be dropped | Containment stop |
| `OBS_EVIDENCE_GRAPH` | Required graph missing or invalid | Block artifact |
| `OBS_UNSUPPORTED_CLAIM` | Unsupported claim enters prohibited path | Block write or artifact |

## 20.4 Plugins and memory

| Code | Condition | Default action |
|---|---|---|
| `PLG_MANIFEST_INVALID` | Invalid manifest | Abort load |
| `PLG_SIGNATURE` | Signature missing or invalid | Abort load |
| `PLG_PERMISSION` | Undeclared access | Kill plugin and abort node |
| `PLG_ABI` | ABI incompatibility | Abort load |
| `PLG_DEPENDENCY_CYCLE` | Dependency cycle | Abort load |
| `PLG_ISOLATION_TIER` | Tier absent or too weak | Abort load |
| `PLG_SBOM_MISSING` | Production SBOM absent | Abort load |
| `PLG_SUPPLY_CHAIN` | Provenance unverifiable | Abort load |
| `PLG_SCAN` | Vulnerability threshold exceeded | Abort load |
| `PLG_HANDLE_FORGERY` | Forged or unauthorized handle | Kill plugin and alert |
| `PLG_HOT_SWAP` | Replacement fails shadow validation | Keep prior version |
| `MEM_PROVENANCE` | Write lacks valid provenance | Quarantine |
| `MEM_SCOPE` | Tenant or subject mismatch | Abort |
| `MEM_CONFLICT` | Irreconcilable memory conflict | Abstain or escalate |
| `MEM_POISON` | Suspected malicious memory | Quarantine |
| `MEM_TRUST_TIER` | Trust promotion violates policy | Reject |
| `MEM_TAINT_LAUNDER` | Transform loses taint | Reject output |
| `MEM_PAGE_LOSS` | Page-out loses retrievable state | Abort |
| `MEM_DELETE_INCOMPLETE` | Derived copy remains | Fail deletion SLA |
| `MEM_UNLEARN_VERIFY` | Post-deletion probe retrieves content | Fail deletion SLA |

## 20.5 Improvement, safety, corrigibility, and validation

| Code | Condition | Default action |
|---|---|---|
| `IMP_SCOPE` | Candidate touches forbidden scope | Reject and alert |
| `IMP_HOLDOUT_LEAK` | Held-out leakage | Reject |
| `IMP_REGRESSION` | Release metric regression | Reject or rollback |
| `IMP_UNSIGNED` | Missing approved signature | Reject |
| `IMP_SELF_APPROVAL` | Self-promotion attempt | Reject and alert |
| `IMP_ROLLBACK` | Rollback absent or untested | Block deployment |
| `IMP_REWARD_HACK` | Reward-hacking detector fails | Reject |
| `IMP_STAT_UNDERPOWERED` | Power requirement not met | Block promotion |
| `IMP_VERIFIER_MISSING` | Objective lacks verifier | Reject objective |
| `IMP_VERIFIER_DEPENDENCE` | Verifier independence fails | Reject |
| `IMP_CORRIGIBILITY` | Invariant mismatch or attempted mutation | Containment stop |
| `IMP_LEDGER_WRITE` | Ledger integrity failure | Block promotion |
| `SAF_INJECTION` | Injection detected | Block affected instruction/action |
| `SAF_HIJACK` | Goal or tool hijack detected | Block and incident |
| `SAF_EXFILTRATION` | Secret or PII egress attempt | Block and incident |
| `SAF_TAINT` | Taint integrity failure | Block |
| `SAF_TERMINATION` | Guard fails to halt correctly | Containment stop |
| `SAF_EXTERNAL_EFFECT` | Unapproved external action | Block and incident |
| `SAF_CASCADE` | Cross-agent escalation | Halt exchange graph |
| `VAL_PLAN_DRIFT` | Analysis plan changes after run start | Invalidate run |
| `VAL_FREEZE_DRIFT` | Frozen comparison input changes | Invalidate comparison |
| `VAL_EXCLUSION` | Undeclared result exclusion | Invalidate report |
| `CIT_UNVERIFIED` | Reference lacks accepted audit | Block release |
| `CIT_MISMATCH` | Identifier/title/venue mismatch | Delete or correct reference |
| `CIT_NUMERIC_CLAIM` | Numeric claim not located | Withdraw claim |

---

# 21. Validation specification, harness, and report

## 21.1 Honesty classes

| Class | Meaning |
|---|---|
| `MEASURED_LOCAL` | Executed on the CASOPS implementation |
| `MEASURED_EXTERNAL` | Reported by an audited external source |
| `STATIC_PASS` | Verified from specification or schemas |
| `NOT_RUN` | Requires an unsupplied implementation |
| `BLOCKED` | Release cannot proceed |

## 21.2 Measurement statement

Delivered:

- measurable targets;
- normative definitions;
- powered statistical procedure;
- fixture layout;
- CLI contract;
- report schema;
- failure semantics.

Not delivered:

- local runtime numbers;
- production certification;
- a cleared citation audit.

All figures labelled `TARGET` are thresholds, not observed outcomes.

## 21.3 Harness

```text
evals/
  analysis_plan.json
  benchmarks.json
  baselines.json
  fixtures/
    perf/{parallel_tool,cache_equivalence,context_rot,kill_switch}/
    compat/{model_profiles,mcp,a2a,cloudevents,trace_context,semconv,template_drift}/
    obs/{fault_injection,redaction,replay,sampling,evidence_graph}/
    plugins/{zero_core_change,permission_denial,isolation,supply_chain,abi}/
    memory/{longmem_profile,update,forget,poison,deletion,tce}/
    improve/{holdout,reward_hacking,canary_sim,rollback}/
    safety/{indirect_injection,hijack,exfiltration,termination,taint_laundering}/
    corrigibility/{inv01..inv12_negative}/
  regression/
  reports/
    <iso8601>-<compose_hash>/
      report.json
      raw/
      statistics.json
      citation-audit.json
```

Invocation:

```bash
casops-eval run \
  --agent agents/video.showrunner \
  --baseline evals/baselines.json#v2-frozen \
  --plan evals/analysis_plan.json \
  --suite perf,compat,obs,plugins,memory,improve,safety,corrigibility \
  --arms baseline,candidate \
  --paired \
  --seed 20260824 \
  --out evals/reports/
```

The tool:

- exits non-zero on any blocking gate;
- records the pre-run plan digest;
- refuses a valid report if the plan changes after start;
- retains all raw rows;
- counts timeouts and errors as failures unless the estimand explicitly states otherwise.

## 21.4 Statistical protocol

### 21.4.1 Freeze list

Freeze:

- dataset and hash;
- child and parent hashes;
- model and adapter revisions;
- tokenizer and template digests;
- quantization;
- hardware;
- framework;
- tool fixtures;
- memory seed;
- cache mode;
- seed where verified;
- retry and timeout policy;
- network conditions;
- evaluator;
- semconv schema;
- analysis-plan digest.

### 21.4.2 Design

- identical task set across arms;
- task as a blocking factor;
- randomized interleaving;
- cold and warm cache reported separately;
- no undocumented exclusions;
- declared primary estimand for every gate;
- stratification declared before execution;
- effect sizes and interval estimates reported.

### 21.4.3 Prospective power and sample size

A fixed sample count does not guarantee power.

For every inferential gate, `analysis_plan.json` declares:

- baseline or nuisance-rate assumptions;
- minimum effect or non-inferiority/equivalence margin;
- alpha;
- target power;
- paired discordance assumptions where binary;
- expected attrition or invalid-run rate;
- calculation or simulation method;
- maximum and minimum sample size;
- allowed blinded sample-size re-estimation.

Default target power:

- at least 80% for ordinary performance and quality gates;
- at least 90% for high-risk safety, deletion, capability, or promotion gates where inference—not a full deterministic fixture—is used.

Minimum floors:

| Claim | Minimum floor | Final n |
|---|---:|---|
| p50 latency | 300 per arm | Maximum of floor and powered n |
| p95 latency | 300 per arm | Maximum of floor and powered n |
| p99 latency | 1000 per arm | Otherwise labelled indicative |
| Binary task success | 400 paired tasks | Maximum of 400 and prospectively powered n |
| CPST | 300 paired tasks | Maximum of floor and powered n |
| Memory rates | 400 paired tasks | Maximum of 400 and powered n |
| Safety attack rate | Full declared suite | No sampling; exact interval reported |

For paired binary outcomes, power calculations use expected discordant-pair probabilities, not an unpaired approximation alone. Historical or pilot estimates may initialize nuisance parameters. Any re-estimation must be blinded to treatment labels or pre-specified as group-sequential.

An underpowered result is not a pass, even if its point estimate exceeds the threshold.

### 21.4.4 Tests

**Superiority**

- one-sided paired test at the pre-registered alpha;
- paired McNemar or a declared paired risk-difference procedure for binary outcomes;
- paired bootstrap, permutation, or model-based procedure for continuous/skewed metrics;
- effect size and confidence interval required.

**Non-inferiority**

- one-sided NI procedure against a declared margin;
- pass only when the appropriate confidence bound excludes inferiority beyond the margin;
- default one-sided alpha is 0.025 for release-critical quality preservation unless the analysis plan justifies another value;
- “not statistically different” is not evidence of non-inferiority.

**Equivalence**

- TOST is used only when both lower and upper equivalence bounds are material;
- at α=0.05 per one-sided test, report the corresponding 90% confidence interval;
- cache-on/off equivalence may use TOST when the estimand and margin are suitable.

**Multiple claims**

- every gate is reported;
- no favorable subset may be selected after observation;
- if a family-wide superiority claim is made, a pre-specified multiplicity method such as Holm control is required;
- independent operational gates may remain individually blocking without being merged into one omnibus claim.

**Canary monitoring**

- uses pre-registered group-sequential boundaries;
- declares looks, spacing, alpha spending, and stop rules;
- naive repeated peeking is prohibited.

### 21.4.5 Determinism

Token-identical replay is gated only when `batch_invariant_kernels` is verified.

Otherwise replay equivalence means:

- identical external observations;
- identical tool and memory fixtures;
- equivalent route and policy decisions;
- identical validator verdicts within declared tolerance.

Claiming token-level determinism without verified batch invariance is prohibited.

## 21.5 Release gates

### 21.5.1 Performance targets against frozen v2

Satisfy A or B.

| Gate | Requirement |
|---|---|
| A — efficiency | p95 improves ≥35%; CPST improves ≥30%; task success is non-inferior within 1pp |
| B — quality | Task success improves ≥5pp with superiority CI excluding zero; p95 and CPST regress ≤10% unless separately approved |

Additional targets:

| Check | Threshold |
|---|---|
| Parallel three-tool fixture | `max(tool durations) + 20%` |
| Warm-cache TTFO | ≥25% improvement over cold |
| Cache equivalence | Within declared two-sided equivalence margin |
| T3 false reuse | ≤0.5% |
| Cache scope | Zero violations |
| CPE | ≥0.70 |
| CRR | ≥0.40 |
| Goodput | ≥25% improvement at fixed accelerator count |
| Stopping rule | ≥30% refinement-cost reduction with success non-inferior within 1pp |
| Optimizer kill switches | 100% return to validated baseline |
| Mandatory control failure | 100% containment-stop; zero bypass |
| Context rot | Non-inferior to oracle-short context within 3pp |

### 21.5.2 Compatibility

- 100% mandatory model contract tests;
- at least three adapter profiles plus deterministic test adapter;
- all production capabilities verified;
- no asserted-unverified binding;
- 100% injected capability drift detected;
- 100% tokenizer/template drift detected;
- pinned and prior MCP revisions negotiate;
- unknown major versions fail closed;
- extensions remain inert unless allow-listed;
- A2A preserves taint, deadline, trace, and authorization;
- 100% CloudEvents schema validation;
- 100% W3C trace continuity;
- 100% alias coverage for gate-bearing telemetry fields.

### 21.5.3 Observability

- exactly one root trace per run;
- ≥99.9% valid span relationships;
- 100% representation of tool, plugin, memory-write, peer, policy, safety, promotion, and rollback actions;
- no raw CoT export;
- no reasoning-monitor leak;
- 100% secret-redaction fixture pass;
- RCA@1 ≥85%;
- replay equivalence ≥95% at the applicable level;
- evidence graph for every claim-bearing artifact;
- unsupported-claim rate ≤1%;
- mandatory tail retention survives induced budget exhaustion.

### 21.5.4 Extensibility

- tool, modality, and evaluator plugin installed with zero core changes;
- all undeclared permission attempts denied;
- all handle-forgery and unauthorized delegation attempts denied;
- I1 ≤1 ms median and ≤3% p95;
- I2 ≤5% p95;
- I3 ≤15% p95;
- plugin removal leaves no unresolved capability;
- invalid digest, signature, ABI, schema, SBOM, provenance, or scan fails closed;
- unauthorized tier downgrade blocked;
- regressing hot swap blocked.

### 21.5.5 Memory

| Check | Threshold |
|---|---|
| Profile score | ≥12pp macro or ≥25% relative improvement |
| Evaluation validity | Contamination check and domain golden-task confirmation |
| Memory prompt tokens | ≥50% reduction |
| TCE | ≥30% improvement |
| Unsupported memory answer rate | ≤1% |
| Update and selective forgetting | ≥97% |
| Staleness rate | ≤2% |
| Provenance | 100% |
| Trust integrity | No T3 used as factual support |
| DCR | 100% by post-deletion probe |
| Cross-tenant retrieval | Zero |
| MPR | ≥95%; no poison reaches T0/T1 |

### 21.5.6 Improvement

A promoted candidate must:

- improve held-out success by at least 5pp with superiority evidence, or reduce CPST by at least 10% with quality non-inferior within the declared margin;
- meet prospectively calculated power;
- pass the full regression and safety suites;
- introduce no compatibility regression;
- preserve mandatory telemetry;
- use isolated held-out data;
- pass all reward-hacking detectors;
- carry an independent verifier attestation;
- pass group-sequential canary guardrails;
- receive independent human approval;
- be signed;
- pass rollback RTO;
- append a complete ledger entry;
- preserve corrigibility.

There must be zero successful self-promotions. Promotion-induced regression rate must be at most 2% over a rolling window of at least 20 promotions.

### 21.5.7 Safety and corrigibility

- all §14.4 gates pass;
- INV-01 through INV-12 negative fixtures abort correctly;
- 100% compose attestation coverage;
- cancellation succeeds within deadline at all isolation tiers;
- mandatory-control unavailability always containment-stops;
- no bypass mode exists.

## 21.6 Citation audit

Release requires:

- zero `[D]`, `[C]`, or `[K]` markers;
- matching titles, identifiers, venues, and dates;
- every numeric claim located;
- no future-dated verification;
- committed `citation-audit.json`.

## 21.7 Static report

| Domain | Finding | Status |
|---|---|---|
| Date integrity | Future date removed | `STATIC_PASS` |
| v2 defects | DEF-001 through DEF-004 addressed | `STATIC_PASS` |
| v3 draft defects | DEF-005 through DEF-008 addressed | `STATIC_PASS` |
| Architecture | Nine planes and boundaries defined | `STATIC_PASS` |
| Performance | DAG, admission, goodput, compute, switches, gates | `STATIC_PASS` |
| Cache/context | Keying, invalidation, equivalence, lifecycle | `STATIC_PASS` |
| Compatibility | Verified capabilities, drift, pinning, profiles | `STATIC_PASS` |
| Observability | Evidence graph, sampling, RCA, bounded monitor | `STATIC_PASS` |
| Plugins | Isolation, object capabilities, supply chain, ABI | `STATIC_PASS` |
| Memory | Trust, hierarchy, poisoning, consolidation, deletion | `STATIC_PASS` |
| Improvement | Verifiers, reward checks, regression ratchet, ledger | `STATIC_PASS` |
| Safety | Taint, termination, zero-tolerance categories | `STATIC_PASS` |
| Corrigibility | Twelve invariants and negative fixtures | `STATIC_PASS` |
| Statistics | Power-derived n; NI/equivalence separated | `STATIC_PASS` |
| Standalone completeness | Retained requirements reproduced | `STATIC_PASS` |
| Error catalogue | Consolidated §20 supplied | `STATIC_PASS` |
| Harness | Layout, CLI, reports, exit semantics | `STATIC_PASS` |
| Local performance | Runtime not supplied | `NOT_RUN` |
| Local compatibility | Adapters not supplied | `NOT_RUN` |
| Local observability | Collector not supplied | `NOT_RUN` |
| Local plugins | Runtime not supplied | `NOT_RUN` |
| Local memory | Backend not supplied | `NOT_RUN` |
| Local improvement | Trainer not supplied | `NOT_RUN` |
| Local safety/corrigibility | Runtime not supplied | `NOT_RUN` |
| Citation audit | No accepted audit artifact supplied | `BLOCKED` |
| Production certification | Requires all gates | `BLOCKED` |

## 21.8 External evidence retained

These are external claims, not CASOPS results, and remain citation-gated.

| Pattern | Reported external result | Class |
|---|---|---|
| Paged KV attention | 2–4× serving throughput at comparable latency | `MEASURED_EXTERNAL`, E1 `[C]` |
| Structured generation / RadixAttention | Up to 6.4× throughput | `MEASURED_EXTERNAL`, E1 `[C]` |
| Parallel function DAG | Up to 3.7× latency, 6.7× cost, ~9% accuracy | `MEASURED_EXTERNAL`, E2 `[C]` |
| Learned model routing | More than 2× cost reduction in some settings | `MEASURED_EXTERNAL`, E2 `[C]` |
| Workflow search | 5.7% average over evaluated baselines | `MEASURED_EXTERNAL`, E2 `[C]` |
| Agent-aware KV management | Reported agent-serving gains | `MEASURED_EXTERNAL`, E3 `[D]` |
| Policy-driven agentic serving | Reported serving gains | `MEASURED_EXTERNAL`, E3 `[D]` |
| Multi-agent workload-aware cache | Reported reuse gains | `MEASURED_EXTERNAL`, E3 `[D]` |
| Graph/PPR memory | Up to 20% multi-hop improvement | `MEASURED_EXTERNAL`, E1 `[C]` |
| Graph memory v2 | 7% associative-memory improvement | `MEASURED_EXTERNAL`, E2 `[C]` |
| Extraction memory | Reported latency and token savings | `MEASURED_EXTERNAL`, E3 `[C]` |
| Self-refinement | ~20% average absolute improvement | `MEASURED_EXTERNAL`, E1 `[C]` |
| Reflective context evolution | Reported lower-rollout gains | `MEASURED_EXTERNAL`, E2/E3 `[K]` |
| Self-editing coding agents | Reported coding gains | `MEASURED_EXTERNAL`, E4 `[C]` |
| Agent Lightning +14.6 | Withdrawn; identifier/claim unresolved | — |

## 21.9 Conclusion

| Item | Verdict |
|---|---|
| Specification completeness | PASS |
| Architecture quality | PASS |
| Date integrity | PASS |
| Quantitative criteria | PASS |
| Statistical protocol | PASS |
| Harness contract | PASS |
| Research traceability | BLOCKED pending audit |
| Executed implementation validation | NOT RUN |
| Specification status | DRAFT |
| Deployment recommendation | NO-GO |

---

# 22. Migration from v2

## 22.1 Defaults

```text
cache.tiers                  = [T0]
context.compaction           = disabled
compute_controller.mode      = fixed
capability_verification      = required
memory.hierarchy             = flat H1
memory.consolidation         = disabled
memory.security.trust_tiers  = enabled
plugins.isolation            = I2 minimum for existing plugins
safety.plane                 = enabled
safety.termination           = enforced
corrigibility.invariants     = enforced
observability.sampling       = tail with mandatory retention
observability.evidence_graph = enabled for claim-bearing artifacts
improvement.mode             = inherited but capped at propose
```

Safety, termination, corrigibility, and capability verification activate unconditionally. A refuted existing capability is a discovered latent defect, not a migration regression.

## 22.2 Steps

1. Copy the v2 folder.
2. Set schema to `3.0` and structure to `casops.common_agent.v3`.
3. Install host-owned corrigibility invariants.
4. Add mandatory safety and termination policy.
5. Add required v3 directories and defaults.
6. Verify every capability.
7. Resolve refutations.
8. Pin tokenizer, template, semconv, protocol, and adapter revisions.
9. Assign isolation and collect SBOM/provenance.
10. Seed regression fixtures from known failures.
11. Author the analysis plan before measurement.
12. Generate locks.
13. Run v2/v3 golden-envelope comparison.
14. Verify no unauthorized tool, network, identity, permission, or production change.
15. Freeze the powered v2 baseline.
16. Enable one optional v3 feature at a time.
17. Run its gates.
18. Complete citation audit.
19. Record migration report.
20. Promote only after all mandatory gates pass.

## 22.3 Backward compatibility

- v1/v2 prompts, rubrics, skills, identity, and parents remain readable.
- v3-only parents cannot enter a v2 child without explicit down-conversion.
- Older consumers may ignore namespaced v3 metadata.
- Safety, provenance, and corrigibility fields cannot silently disappear during down-conversion.
- Regression and safety fixtures never down-convert away.

---

# 23. Traceability

| Need | Requirements | Acceptance |
|---|---|---|
| Latency and utilization | FR-PERF-001–017, 101–110 | §21.5.1 |
| Cache correctness | FR-CACHE-001–009 | Equivalence and scope fixtures |
| Context lifecycle | FR-CTX-001–007 | Context-rot gate |
| Adaptive compute | FR-PERF-103/104 | Stopping-rule gate |
| Model interoperability | FR-CMP-001–010, 101–107 | Verified matrix |
| Telemetry stability | FR-CMP-108–111 | Alias and version fixtures |
| Tool interoperability | FR-CMP-112–117 | MCP conformance |
| Agent interoperability | FR-CMP-118–121 | Peer and taint conformance |
| Decision provenance | §10 | Evidence and RCA gates |
| Reasoning monitor | FR-OBS-101–105 | Zero-leak fixtures |
| Trace cost | FR-OBS-111–115 | Budget-exhaustion fixture |
| Plugin extensibility | FR-PLG-001–010, 101–118 | Plugin gates |
| Supply chain | FR-PLG-109–113 | Fail-closed fixtures |
| Memory | §12 | Memory profile |
| Deletion | FR-MEM-116–120 | DCR and probes |
| Memory attack resistance | FR-MEM-106, §14.4 | MPR |
| Improvement | §13 | Candidate gates |
| Reward integrity | FR-IMP-101–106 | Detector suite |
| Capability retention | FR-IMP-107–110 | Full regression |
| Safety | FR-SAF-001–012 | §21.5.7 |
| Corrigibility | INV-01–12, FR-COR-001–006 | Negative fixtures |
| Skills | FR-SKL-001–010 | Compose preview |
| Persona isolation | FR-IDN-001–012 | Disclosure and policy tests |
| Reproducibility | Locks and replay | Applicable replay gate |
| Statistical validity | §21.4 | Plan and power check |
| Citation integrity | P29, CIT-GATE-001/002 | Audit report |
| Error consistency | §20 | Error-code schema validation |

---

# 24. Open risks

| Risk | Required mitigation |
|---|---|
| Optimizer improves latency but harms success | CPST plus NI quality gate |
| Router drift | Shadowing, bounded updates, quarantine |
| Cache serves stale policy | Invalidate-before-read and approval epochs |
| Cache crosses boundaries | Full-scope keys, purge, zero-tolerance gate |
| Compaction loses constraints | Pinned invariants and preservation verifier |
| Vendor overstates capabilities | Verified-not-asserted binding |
| Template/tokenizer changes semantics | Digest pinning and re-conformance |
| External telemetry schema changes | Stable `casops.*` aliases |
| Protocol revision breaks semantics | Pinning and dual-revision support |
| Plugin supply-chain compromise | SBOM, provenance, scan, signature, isolation |
| Isolation under-assigned | Threat-model minimum and expiring waiver |
| Tool output injects instructions | Taint and no instruction authority |
| Taint laundering | Propagation through every transform |
| Telemetry leaks content | Metadata default and redaction |
| Trace budget drops critical events | Mandatory tail retention |
| Monitor channel becomes export back door | Verdict-only output and zero-leak tests |
| Memory accumulates false facts | Trust tiers and provenance |
| Agent output hardens into fact | Evidence graph and T3 advisory treatment |
| Memory becomes stale | Bitemporal records and staleness gate |
| Deletion leaves derivatives | Tombstones and post-deletion probes |
| Weight-level influence survives deletion | Explicit limitation and retraining review |
| Public memory benchmark is misleading | Contamination and domain-golden confirmation |
| Improvement overfits | Isolated held-out and rotating fixtures |
| Self-judge rewards its style | Independent verifier |
| Metric improves while capability regresses | Full regression suite |
| Canary peeking inflates false positives | Group-sequential boundaries |
| Fixed n is underpowered | Prospective paired power calculation |
| Power assumptions are wrong | Sensitivity analysis and blinded re-estimation |
| Equivalence confused with NI | Separate procedures in §21.4 |
| Citation supports a false requirement | CIT-GATE-001 |
| Future-dated evidence is represented as complete | CIT-GATE-002 |
| Determinism is overclaimed | Batch-invariance capability gate |
| Multi-agent failure cascades | Hop, cycle, taint, and shared-budget controls |
| Parent mixins create a god agent | Parent/depth limits and deny-list union |
| Added complexity becomes the failure mode | Optional optimizers have baseline kill switches; mandatory controls fail-stop rather than bypass |
| Corrigibility path appears inside agent folder | Runtime path must be host-owned, immutable, and outside writable capabilities |

---

# 25. Research references and citation audit

Markers:

- `[A]` accepted by v3a audit;
- `[D]` prior draft claimed verification, not accepted by v3a;
- `[C]` carried from v2;
- `[K]` unaudited knowledge-derived reference.

All non-`[A]` entries are blocked by §21.6.

## 25.1 Prior-draft verification claims `[D]`

### Serving and caching

- *Learning Agent Execution for KV-Cache Management in Agentic Serving*, arXiv:2608.14624 `[D]`
- *A Policy-Driven Runtime Layer for Agentic LLM Serving*, arXiv:2605.27744 `[D]`
- *Workload-Aware Caching for Multi-Agent Systems*, arXiv:2607.20495 `[D]`

### Memory

- *A Survey on Memory Mechanisms in the Era of LLMs*, arXiv:2504.15965 `[D]`
- *Memory in the Age of AI Agents*, arXiv:2512.13564 `[D]`
- *A Survey of Agent Memory in the Second Half*, arXiv:2602.06052 `[D]`
- *Agent Memory: Mechanisms, Evaluation, and Emerging Frontiers*, arXiv:2603.07670 `[D]`
- *Agent Memory Evaluation: Taxonomy and Empirical Analysis of Evaluation and System Limitations*, arXiv:2602.19320 `[D]`
- *A Survey on the Security of Long-Term Memory in LLM Agents*, arXiv:2604.16548 `[D]`

### Self-evolving agents

- *A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve*, arXiv:2507.21046 `[D]`
- *Bridging Foundation Models and Lifelong Agentic Systems*, arXiv:2508.07407 `[D]`

### Observability and protocols

- OpenTelemetry, *Semantic Conventions for Generative AI* and *Inside the LLM Call: GenAI Observability with OpenTelemetry* `[D]`
- Prior-draft analysis concerning stable versus experimental `gen_ai.*` attributes `[D]`
- CNCF, *How Jaeger is Evolving to Trace AI Agents with OpenTelemetry* `[D]`
- Model Context Protocol revisions and *Versioning and Compatibility* `[D]`

## 25.2 Carried from v2 `[C]`

### Performance and workflow

- PagedAttention, SOSP 2023 `[C]`
- SGLang / RadixAttention, NeurIPS 2024 `[C]`
- LLMCompiler `[C]`
- RouteLLM `[C]`
- AFlow, ICLR 2025 `[C]`
- Automated Design of Agentic Systems, ICLR 2025 `[C]`
- EAGLE-3 `[C]`
- Agentic test-time-compute system analysis `[C]`

### Memory

- HippoRAG, NeurIPS 2024 `[C]`
- HippoRAG 2, ICML 2025 `[C]`
- LongMemEval, ICLR 2025 `[C]`
- LoCoMo `[C]`
- A-MEM `[C]`
- MIRIX `[C]`
- Mem0 `[C]`
- MemoryAgentBench `[C]`
- Mem2ActBench `[C]`
- MemGAS `[C]`

### Improvement

- Self-Refine, NeurIPS 2023 `[C]`
- Reflexion, NeurIPS 2023 `[C]`
- Voyager, NeurIPS 2023 `[C]`
- Promptbreeder, ICML 2024 `[C]`
- Agent Lightning, arXiv:2508.03680 `[C]`
- Darwin Gödel Machine `[C]`
- A Self-Improving Coding Agent `[C]`
- Self-Adapting Language Models / SEAL `[C]`

### Standards and evaluation

- W3C Trace Context `[C]`
- CloudEvents JSON event format `[C]`
- Linux Foundation A2A `[C]`
- Turpin et al., *Language Models Don’t Always Say What They Think* `[C]`
- Lanham et al., *Measuring Faithfulness in Chain-of-Thought Reasoning* `[C]`
- ToolSandbox `[C]`
- GAIA `[C]`
- SWE-bench `[C]`
- BFCL `[C]`

**Withdrawn:** “Agent Lightning v1.0, arXiv:2608.17528, SWE-bench Verified 41.8%→56.4%.” It remains unusable unless independently resolved, and the numeric claim must not be restored merely because a related Agent Lightning paper exists.

## 25.3 Knowledge-derived references `[K]`

- MemGPT-style hierarchical or OS-style memory paging `[K]`
- Memory operating-system architectures `[K]`
- Temporal knowledge-graph memory, including Zep/Graphiti-style patterns `[K]`
- Background or sleep-time consolidation compute `[K]`
- Agentic context engineering and evolving context playbooks `[K]`
- GEPA-style reflective prompt evolution `[K]`
- AgentDojo-style injection and hijacking benchmarks `[K]`
- InjecAgent-style injection benchmarks `[K]`
- AgentPoison-style memory-poisoning work `[K]`
- MAST-style multi-agent failure taxonomies `[K]`
- Batch invariance and inference nondeterminism `[K]`
- Long-context degradation or context-rot measurements `[K]`
- Object-capability sandboxing for extensions `[K]`

If a citation fails, the related control may remain only when it has a documented independent engineering justification.

---

# 26. Document control

| Item | Value |
|---|---|
| Owner | Host architecture, CASOPS |
| Revision | v3a |
| Structure family | `casops.common_agent.v3` |
| Schema | `3.0` |
| Date | `2026-08-31` |
| Supersedes on approval | v2 |
| Replaces as draft | Future-dated unreleased v3 input |
| Specification completeness | Yes |
| Release-ready specification | No; citation and local gates remain blocked |
| Production implementation certified | No |
| Automatic production activation | No |
| Automatic tool, plugin, network, or permission grant | No |
| Automatic candidate promotion | No |
| Core self-modification | Research-only |
| Raw chain-of-thought export | Prohibited |
| Reasoning monitor | Internal-only, verdict-only, short-retention |
| Default cache | T0 only |
| Default memory | None until configured |
| Default improvement | Disabled or propose-only |
| Safety plane | Mandatory and non-bypassable |
| Corrigibility | Mandatory, host-owned, agent-unwritable |
| Optional optimizer failure | Validated baseline fallback |
| Mandatory-control failure | Containment stop |
| Statistical protocol | Pre-registered, paired, power-derived, interval-estimated |
| Non-inferiority | One-sided NI procedure |
| Equivalence | TOST only when two-sided equivalence is intended |
| Citation audit | Release-blocking |
| Public control plane | Existing FastAPI plane only |
| Normative diagrams | Inline Mermaid |
| Deployment recommendation | NO-GO until §21 gates pass |

---

## Final delivery statement

**Delivered:** a complete, standalone v3a specification retaining the v3 architecture and requirements while correcting its date, citation status, statistical protocol, kill-switch contradiction, standalone dependency, and missing consolidated error catalogue.

**Not delivered:** fabricated runtime results, a falsely cleared citation audit, or production certification.

**Required next actions:**

1. execute `CIT-GATE-001` and `CIT-GATE-002`;
2. implement `casops-eval`;
3. freeze a powered v2 baseline;
4. run every local gate in §21.5;
5. retain v3a as `DRAFT` until both citation and local validation blockers clear.

**End of specification.**