# Implementation Plan — `casops.common_agent.v3` (v3a)

**Source specification:** `common_agent_structure.v3a.md`  
**Document ID:** `CASOPS-FS-COMMON-AGENT-STRUCTURE-V3A`  
**Plan date:** 2026-08-24  
**Status:** Draft implementation plan (specification remains DRAFT / NO-GO until citation audit + local gates clear)  
**Host repository:** `common-agent-swarm-ops`  
**Structure family:** `casops.common_agent.v3`  
**Schema version:** `3.0`

---

## 0. Executive summary

This plan turns the v3a common-agent specification into a concrete, sequenced delivery of the nine planes, folder contract, compose algorithm, validation harness, and migration path.

**Non-negotiable constraints inherited from v3a**

- No production activation, unrestricted network, self-granted tools/plugins/credentials, or automatic candidate promotion.
- Safety, termination, corrigibility, and mandatory audit are **non-bypassable**. Failure → containment stop.
- Optional optimizers (cache tiers, learned routers, adaptive compute, compaction strategies) receive independent kill switches that fall back to a validated baseline.
- Every capability is `VERIFIED` before production binding; asserted-but-unverified is unusable.
- Statistical claims require prospective power, paired design, interval estimates, and pre-registration. Fixed sample floors are only lower bounds.
- Citation audit (`CIT-GATE-001` / `CIT-GATE-002`) is release-blocking. No fabricated runtime numbers.
- The agent folder remains one `agent_id`; parent content never replaces the child mission.

**Primary outcome of this plan**

A host that can:

1. Compose a v3 folder into an immutable `compose.lock.json` + `capabilities.lock.json`.
2. Execute under the nine-plane architecture with fail-closed boundaries.
3. Run the full `casops-eval` harness against powered, pre-registered analysis plans.
4. Migrate existing v2 agents without silent loss of safety/corrigibility/regression fixtures.
5. Remain NO-GO for production until both the citation audit artifact and every §21.5 local gate pass.

---

## 1. Current state and gaps

| Area | Spec status (v3a) | Implementation reality (assumed start) | Gap |
|---|---|---|---|
| Runnable artifact | Explicitly none supplied | Host may have partial v1/v2 composer | Full v3 composer + locks missing |
| Citation audit | `BLOCKED` | No `citation-audit.json` | Must execute `CIT-GATE-001` |
| Local measurement | `NOT_RUN` | No `casops-eval` | Harness + fixtures must be built |
| Corrigibility | Host-owned invariants required | Likely still policy-only | Must move to host-owned, agent-unwritable mount |
| Capability verification | Asserted vs verified | May still treat assertions as usable | Conformance runner + lock required |
| Error catalogue | §20 complete | Scattered or incomplete | Central error-code schema + handling |
| Statistical protocol | Power-derived n, NI ≠ TOST | Fixed-n or point comparisons | Analysis-plan schema + power tooling |
| Kill-switch vs containment | Explicitly separated | Often conflated | Two distinct switch classes |

---

## 2. Guiding principles for implementation

1. **Plane-by-plane, boundary-first.** Implement the control boundary of each plane before its optimizers.
2. **Fail closed by default.** Unknown, unsigned, unverified, or drifted → abort / quarantine / containment stop.
3. **Locks before runtime.** No production-path execution without `compose.lock.json` + `capabilities.lock.json`.
4. **Host ownership of corrigibility.** `corrigibility/invariants.json` is a logical path only; runtime is a read-only host mount outside every agent-writable capability.
5. **Optional vs mandatory.** Optimizer kill switches return to baseline; mandatory controls have no bypass.
6. **Evidence over narrative.** Decision records and evidence graphs record observable facts, not private CoT.
7. **Validation is part of the product.** `casops-eval`, fixtures, analysis plans, and report schema ship with the host.
8. **No silent inheritance of authority.** Tools, plugins, credentials, network, production activation, and gate thresholds never inherit.

---

## 3. Work breakdown — phases

### Phase 0 — Foundations (Week 0–2)

**Goal:** Make the folder contract, schemas, and composer deterministic and fail-closed.

| ID | Work item | Acceptance |
|---|---|---|
| P0-01 | Define JSON Schemas for every required file in §5.2 (`agent_spec.json`, `runtime/*.json`, `protocols/*`, `memory/*`, `safety/*`, `corrigibility/invariants.json`, `evals/analysis_plan.json`, etc.) | Schema validation fails closed on missing/invalid files |
| P0-02 | Implement folder tree generator / validator that enforces §5.1 layout | Invalid trees rejected before compose |
| P0-03 | Implement MRO resolution + parent legality checks (§6.1) | Cycles, depth > 3+child, >8 parents, self-parent → `INH_*` abort |
| P0-04 | Implement merge rules (§6.2) and non-inherited surface enforcement (§6.3) | Tools/plugins/credentials/activation never inherit |
| P0-05 | Implement fixture monotonicity (§6.5) with signed waiver path | Child cannot drop inherited regression/safety fixtures without host waiver |
| P0-06 | Generate `generated/compose.lock.json` with every field listed in §6.6 | Any change → new `compose_hash` |
| P0-07 | Host-owned corrigibility mount: invariants loaded from host reference, not agent-writable path | Agent cannot write or replace invariants; mismatch → containment stop |
| P0-08 | Central error catalogue (§20) as typed enum + machine-readable schema | Every code has default action; unknown codes fail closed |
| P0-09 | Document control and status fields in every generated artifact | Status, schema_version, structure_id always present |

**Exit criteria:** A v3 folder can be composed into a lock file; any missing mandatory file or illegal parent aborts with a §20 code.

---

### Phase 1 — Mandatory control planes (Week 2–5)

**Goal:** Safety, termination, and corrigibility are always present and non-bypassable before any optimizer is enabled.

#### 1.1 Safety plane (§14)

| ID | Work item | Acceptance |
|---|---|---|
| P1-01 | Taint model: every inbound item receives a taint class; `instruction_authority:false` for non-operator content | Taint propagates through transforms, summaries, compaction, consolidation |
| P1-02 | Injection / hijack / exfiltration detectors + incident records (§14.5) | All §14.4 zero-tolerance categories produce incidents + regression fixtures |
| P1-03 | Hard termination guards: time, cost, model calls, tool calls, peer hops, refinements, plan expansions, progress-free loops, peer cycles | Guard trip → explicit bounded failure, never silent truncated success |
| P1-04 | Outbound secret/PII scanning | No secret/PII egress on fixtures |
| P1-05 | Negative fixtures for every safety gate | 100% of declared fixtures halt/block correctly |

#### 1.2 Corrigibility plane (§15)

| ID | Work item | Acceptance |
|---|---|---|
| P1-06 | Implement INV-01 … INV-12 as host-owned, agent-unwritable invariants | Compose attests digest; mismatch → immediate containment stop |
| P1-07 | Negative fixture suite `corrigibility/inv01..inv12_negative` | Untested invariant treated as broken |
| P1-08 | Shutdown / cancellation honored at every node boundary and terminates plugin invocations | Cancellation succeeds within deadline at all isolation tiers |
| P1-09 | Candidate generation that touches invariant surfaces is rejected at generation time + alerted | Zero successful invariant mutations |

#### 1.3 Containment vs kill-switch distinction (§4.3)

| ID | Work item | Acceptance |
|---|---|---|
| P1-10 | Two switch classes: `optimizer_kill_switch` (baseline fallback) and `containment_stop` (halt, never bypass) | Mandatory controls have no bypass path; optional optimizers return to validated baseline |

**Exit criteria:** Safety + corrigibility + termination are always on. No code path can disable them. All negative fixtures pass.

---

### Phase 2 — Execution plane + compose/runtime algorithm (Week 4–7)

**Goal:** Typed DAG execution with admission, compute controller, and fail-closed fallbacks.

| ID | Work item | Acceptance |
|---|---|---|
| P2-01 | Execution IR `casops.execution_dag.v2` with all node kinds (§7.2) | Every node declares schemas, timeout, side-effect class, cacheability, isolation, taint, failure/compensating actions |
| P2-02 | Explicit dependency compilation + safe concurrency (FR-PERF-001–003) | Side-effecting unordered nodes never parallelized |
| P2-03 | SLO admission control + goodput-oriented scheduler (FR-PERF-101–102) | Work is queued or shed; never silently degrades all in-flight runs |
| P2-04 | Compute controller (§7.5) with marginal-gain stopping rule | Stopping decisions record gain, cost, threshold, rule version |
| P2-05 | Speculative nodes with guard + compensation (FR-PERF-105) | No side-effect commit before guard; abandoned speculation compensated |
| P2-06 | Per-run metric emission (§7.6) including CPE, CRR, goodput contribution, containment_stop_reason | Metrics available to observability plane |
| P2-07 | Full compose algorithm (§17.1) including capability conformance before lock | Only VERIFIED capabilities bind |
| P2-08 | Full run algorithm (§17.2) and prompt envelope ordering (§17.3) | Pinned sections never compacted; taint-labelled memory only |
| P2-09 | Optimizer kill-switch wiring for adaptive compute, speculation, learned routing | Kill switch returns to fixed/baseline path; telemetry emitted |

**Exit criteria:** A deterministic local adapter can execute a simple DAG end-to-end under admission + compute budget; mandatory controls remain non-bypassable.

---

### Phase 3 — Compatibility, observability, and evidence (Week 6–9)

#### 3.1 Compatibility & protocol plane (§9)

| ID | Work item | Acceptance |
|---|---|---|
| P3-01 | Capability assertions → conformance runner → `VERIFIED` / `REFUTED` / `ASSERTED_UNVERIFIED` | Only VERIFIED binds in production |
| P3-02 | `compatibility-matrix.lock.json` + drift detection (`CMP_CAPABILITY_DRIFT`) | Drift quarantines route |
| P3-03 | Tokenizer + chat-template digest pinning | Digest change forces re-conformance |
| P3-04 | MCP revision pinning + dual-revision support + unknown-major fail-closed | Unknown major rejected; unknown minor ignored |
| P3-05 | A2A peer envelope (§9.7) with taint, hop, budget, auth_scope | External-peer content has `instruction_authority:false` |
| P3-06 | OTel GenAI `schema_url` pin + `casops.*` stable aliases (FR-CMP-108–111) | Gates bind only to `casops.*`; semconv change raises `CMP_SEMCONV_VERSION` |

#### 3.2 Observability & decision provenance (§10)

| ID | Work item | Acceptance |
|---|---|---|
| P3-07 | Root span + mandatory child spans; append-only hash-chained store | Exactly one root per run; ≥99.9% valid relationships |
| P3-08 | Decision records with observable inputs/actions/outcomes only | No requirement for raw CoT |
| P3-09 | Claim-level evidence graph (§10.4) | Unsupported-claim rate reported and gated; memory-write from unsupported claim rejected |
| P3-10 | Internal reasoning-monitor channel (verdict-only, ≤24 h encrypted, never exported) | Zero-leak fixtures pass |
| P3-11 | Tail sampling + mandatory 100% retention categories + trace-budget degradation order | Mandatory categories never dropped; budget exhaustion → containment stop if audit unavailable |
| P3-12 | Content capture levels default to `metadata_only` | Redaction fixtures 100% pass |
| P3-13 | RCA@1 measurement on injected single-fault scenarios + counterfactual replay (no memory write / no production publish) | RCA@1 ≥85% target; replay equivalence at applicable level |

**Exit criteria:** Every run produces a sealed evidence graph + decision provenance; capability matrix is locked; telemetry uses only pinned + aliased attributes.

---

### Phase 4 — Cache / context lifecycle + long-term memory (Week 8–12)

#### 4.1 Cache & context (§8)

| ID | Work item | Acceptance |
|---|---|---|
| P4-01 | T0–T3 cache tiers with full key discipline (model, tokenizer, template, policy, capability, tenant, subject, sensitivity, approval epoch) | Cross-boundary access aborts + purges |
| P4-02 | Invalidate-before-read on policy/prompt/memory/template/tokenizer/capability/approval change | No silent staleness |
| P4-03 | T3 off by default; equivalence verifier + ≤0.5% false-reuse gate required to enable | Cache-on/off equivalence within pre-registered margin |
| P4-04 | Context segment budgets + pinned non-compactable set (safety charter, corrigibility, `does_not_own`, disclosure, output schema, deadline) | Compaction never drops pinned content |
| P4-05 | Compaction + preservation verifier; failure escalates or stops | Context-rot fixture non-inferior to oracle-short within 3pp |
| P4-06 | Re-grounding checkpoints for long-horizon runs | Configured checkpoints executed |

#### 4.2 Memory architecture (§12)

| ID | Work item | Acceptance |
|---|---|---|
| P4-07 | Seven stores + H0–H3 paged hierarchy with residency budgets | Page-in/out telemetry; H0 non-evictable pinned invariants |
| P4-08 | Memory record schema with bitemporal times, trust tier, taint, provenance chain | T3 never used as factual support |
| P4-09 | Write policy: only allowed categories; reject unsupported claims, secrets, cross-tenant, T3-as-fact | Provenance mandatory |
| P4-10 | Hybrid retrieval (lexical + dense + graph + temporal) + trust filter before injection | Irreconcilable conflict → abstention |
| P4-11 | Offline consolidation as candidate only; trust ≤ lowest input | Cannot consume serving capacity |
| P4-12 | Tombstone propagation to indexes, caches, summaries, embeddings, graph, consolidation, derived artifacts | Post-deletion probes (lexical/dense/graph/cache) 100% |
| P4-13 | Unlearning / DCR measurement + weight-level limitation recording | DCR 100% by probe; training influence flagged for retraining review |
| P4-14 | Memory security: poisoning screen, MPR gate ≥95%, no poison reaches T0/T1 | Poisoning fixtures pass |

**Exit criteria:** Memory and cache are governed data planes. Deletion is verified. Cache never crosses tenant/subject/sensitivity/approval boundaries.

---

### Phase 5 — Plugins / extensibility (Week 10–13)

| ID | Work item | Acceptance |
|---|---|---|
| P5-01 | Plugin kinds + typed interfaces + manifest schema (§11.6) | Manifest validation never executes plugin code |
| P5-02 | Isolation tiers I0–I3 with threat-model minimums | Third-party/unsigned ≥ I2; network-capable = I3; downgrade requires signed expiring waiver |
| P5-03 | Object-capability handles: unforgeable, revocable, expiring, no ambient authority, no enumeration, no unauthorized delegation | Handle-forgery fixtures kill plugin + alert |
| P5-04 | Supply chain: SBOM, build provenance, vulnerability scan, signature, digest match | Missing/failed → `PLG_*` abort |
| P5-05 | Lifecycle (discover → lock) + hot-swap with drain + shadow validation | Regressing hot-swap blocked |
| P5-06 | ABI semantic versioning + contract tests + deprecation window (≥2 minor) | ABI mismatch fails load |
| P5-07 | Zero core-source-change installation for tool/modality/evaluator plugins | Fixture demonstrates install without composer change |

**Exit criteria:** Plugins are loadable only under declared isolation + supply-chain controls; no ambient authority exists.

---

### Phase 6 — Autonomous improvement + validation harness (Week 12–16)

#### 6.1 Improvement plane (§13)

| ID | Work item | Acceptance |
|---|---|---|
| P6-01 | Levels L0–L5 with writable locations strictly enforced | L5 research-only, isolated, no production credentials |
| P6-02 | Candidate types + required fields (diff, risk, verifiers, regression, stats, rollback, signature state) | Incomplete candidate rejected |
| P6-03 | Independent verifier requirement + reward-hacking detectors | Self-score promotion impossible; detectors cover length, judge mimicry, memorization, refusal gaming, format, golden-task divergence |
| P6-04 | Failure-to-fixture ratchet (union-monotonic) | Confirmed failure becomes fixture before promotion |
| P6-05 | Immutable hash-chained improvement ledger | Agent cannot rewrite promotion-boundary entries |
| P6-06 | Group-sequential canary with pre-registered boundaries | Naive peeking prohibited |
| P6-07 | Learning separation: trajectories may export to trainer; no gradient updates in serving process | Online updates limited to bounded non-executable statistics / propose-only playbooks |

#### 6.2 Validation harness (§21)

| ID | Work item | Acceptance |
|---|---|---|
| P6-08 | `casops-eval` CLI with exact invocation contract | Non-zero exit on any blocking gate; plan digest frozen at start |
| P6-09 | `evals/` layout exactly as §21.3 (fixtures per plane, regression, reports) | All domains present |
| P6-10 | `analysis_plan.json` schema supporting prospective power, paired design, NI vs equivalence, multiplicity, group-sequential | Underpowered result is not a pass |
| P6-11 | Statistical procedures: superiority (one-sided paired), NI (one-sided), equivalence (TOST only when two-sided intended) | Terminology and procedures match §21.4 |
| P6-12 | Report schema with honesty classes (`MEASURED_LOCAL`, `MEASURED_EXTERNAL`, `STATIC_PASS`, `NOT_RUN`, `BLOCKED`) | No fabricated local numbers |
| P6-13 | Freeze list enforcement (§21.4.1) | Drift after start invalidates run |
| P6-14 | Citation-audit runner producing `citation-audit.json` per `CIT-GATE-001` | Every `[D]`/`[C]`/`[K]` resolved or deleted; numeric claims located |

**Exit criteria:** A candidate cannot promote without independent verifier, full regression, powered statistics, human approval, signature, and ledger entry. `casops-eval` produces a valid report or fails closed.

---

### Phase 7 — Skills, identity, operator APIs, migration (Week 14–17)

| ID | Work item | Acceptance |
|---|---|---|
| P7-01 | Skill resolution formula + toggles + no tool leak (FR-SKL-001–010) | Disabled skills absent from prompts/tools/memory/cache/evidence |
| P7-02 | Identity modes + disclosure + named-person approval (FR-IDN-001–012) | Persona cannot mint permissions, facts, or safety verdicts |
| P7-03 | Operator/host APIs (§19) under `/api/v3/...` with authenticated actor, reason, expected parent version, dry-run, append-only audit | No agent-identity endpoint can write corrigibility invariants |
| P7-04 | Migration path (§22): defaults, 20-step procedure, golden-envelope comparison | v2 → v3 preserves safety/corrigibility/fixtures; no unauthorized grants |
| P7-05 | Backward-compatibility rules for v1/v2 consumers | Safety/provenance/corrigibility fields never silently disappear on down-conversion |

**Exit criteria:** Existing v2 agents can be migrated under the documented steps; operator APIs enforce human gates.

---

### Phase 8 — Integration, citation audit, release readiness (Week 16–20)

| ID | Work item | Acceptance |
|---|---|---|
| P8-01 | End-to-end golden path: compose → admit → execute → evidence graph → (optional) candidate → ledger | Full path under containment rules |
| P8-02 | Execute full §21.5 release-gate matrix against frozen v2 baseline | Every domain either PASS or explicitly `NOT_RUN` / `BLOCKED` with reason |
| P8-03 | Complete citation audit (`CIT-GATE-001` + `CIT-GATE-002`) | Zero remaining `[D]`/`[C]`/`[K]`; no future-dated claims |
| P8-04 | Traceability matrix (§23) mapped to automated tests | Every FR has a corresponding fixture or static check |
| P8-05 | Open-risk register (§24) reviewed; mitigations implemented or accepted with residual risk | Residual risks documented in report |
| P8-06 | Final static report (§21.7) + deployment recommendation | Remains NO-GO until both citation and local gates clear |

**Exit criteria:** Specification status can be promoted from DRAFT only when citation audit is accepted **and** every mandatory local gate is `MEASURED_LOCAL` PASS.

---

## 4. Cross-cutting workstreams

### 4.1 Schemas & code generation

- Single source of truth for all JSON Schemas.
- Generate typed models (Python / TypeScript) and OpenAPI for `/api/v3`.
- Schema version `3.0` is frozen for this structure family; breaking changes require a new family.

### 4.2 Telemetry & alias layer

- Pin OpenTelemetry GenAI `schema_url`.
- Emit every gate-bearing attribute under both external name and `casops.*`.
- Alias map is versioned and committed; change is a compatibility event.

### 4.3 Error handling

- All §20 codes implemented as first-class errors with default actions.
- High-risk paths that lose audit or mandatory controls → containment stop.
- Operator-visible reason codes on every shed / abort / quarantine.

### 4.4 Security & supply chain

- Plugin SBOM + provenance + signature verification before load.
- Object-capability model only; no ambient credentials in plugin or agent runtime.
- Secrets never written to memory stores outside approved vaults.

### 4.5 Documentation & operator runbooks

- Per-plane operator guides.
- Migration runbook (§22.2 expanded with concrete commands).
- Incident response for safety blocks and containment stops.
- “How to read a validation report” including honesty classes and statistical protocol.

---

## 5. Testing strategy

| Layer | What | When |
|---|---|---|
| Unit | Schemas, merge rules, taint propagation, key construction, power calculations | Continuous |
| Contract | Capability conformance, MCP dual-revision, A2A envelope, ABI | Per adapter / plugin change |
| Fixture | Every negative safety/corrigibility fixture, cache scope, deletion probes, reward-hacking detectors | Continuous + pre-merge |
| Integration | Full compose → run → evidence graph under local deterministic adapter | Nightly |
| Statistical | Powered paired runs against frozen baseline; group-sequential canary simulation | Pre-release |
| Red-team | Indirect injection, memory poison, tool hijack, exfiltration, cascade | Pre-release + periodic |
| Migration | v2 → v3 golden-envelope + no unauthorized grant | Pre-release |

All performance and quality claims use the §21.4 protocol. Underpowered results are failures.

---

## 6. Risk register (implementation-focused)

| Risk | Mitigation |
|---|---|
| Scope explosion across nine planes | Strict phase ordering; mandatory controls before optimizers |
| Corrigibility path accidentally becomes agent-writable | Host mount + compose attestation + negative fixtures |
| Kill-switch used on mandatory controls | Explicit switch-class enum; code review gate |
| Citation audit never completed | Treat as hard blocker; no release language until `citation-audit.json` accepted |
| Fixed sample sizes re-introduced | Analysis-plan schema rejects missing power calculation |
| Plugin ambient authority | Object-capability only; ambient clients never injected |
| Memory deletion incomplete | Tombstone + multi-path probes; DCR gate |
| Canary peeking | Group-sequential boundaries pre-registered |
| v2 migration silently drops fixtures | Monotonicity enforcement + golden comparison |
| Fabricated local metrics | Honesty classes + `NOT_RUN` until real execution |

---

## 7. Resource & dependency assumptions

- Host already has (or will provide) a FastAPI control plane that can host `/api/v3`.
- Local deterministic model adapter available for early phases (no network required).
- Object storage / encrypted blob store for memory content refs and evidence vault.
- OTel collector (or compatible) for export; local encrypted spool mandatory when exporter down.
- CI capable of running the full fixture suites and producing report artifacts.
- Human approvers available for promotion, named-person identity, isolation-tier waivers, and production activation.

No external model endpoint, plugin runtime, or memory backend is assumed present at Phase 0. Phases that require them remain `NOT_RUN` until supplied.

---

## 8. Deliverables checklist

- [ ] Complete JSON Schema set for structure family `casops.common_agent.v3`
- [ ] Composer producing `compose.lock.json` + `capabilities.lock.json`
- [ ] Host-owned corrigibility attestation
- [ ] Safety + termination + containment-stop implementation
- [ ] Execution DAG runtime with admission + compute controller
- [ ] Capability conformance runner
- [ ] Observability pipeline (decision records, evidence graph, tail sampling, aliases)
- [ ] Cache tiers T0–T3 + context lifecycle with preservation verifier
- [ ] Memory hierarchy H0–H3 + trust tiers + deletion probes
- [ ] Plugin loader (I0–I3, object capabilities, SBOM/provenance)
- [ ] Improvement ledger + candidate pipeline (propose-only)
- [ ] `casops-eval` CLI + fixture tree + analysis-plan schema + report schema
- [ ] Citation-audit tooling producing `citation-audit.json`
- [ ] `/api/v3` operator surface
- [ ] v2 → v3 migration tooling and golden comparison
- [ ] Static + measured validation report with honesty classes
- [ ] Updated open-risk and traceability matrices

---

## 9. Success criteria for “implementation complete”

The implementation is considered complete (still not production-certified) when:

1. Every required file and lock listed in §5 can be produced or validated.
2. All twelve corrigibility invariants have passing negative fixtures.
3. Safety zero-tolerance categories and termination guards have passing fixtures.
4. Capability binding is exclusively `VERIFIED`.
5. Cache, memory, plugin, and improvement planes respect their control boundaries.
6. `casops-eval` can be invoked and either produces a valid report or exits non-zero with a blocking gate.
7. Citation audit artifact exists and contains zero unresolved `[D]`/`[C]`/`[K]` entries (or the specification has been revised to remove dependence on them).
8. Migration of a representative v2 agent succeeds without unauthorized grants or fixture loss.
9. Document control status remains honest: DRAFT / NO-GO until both citation and local measurement blockers clear.

**Production activation remains a separate, human-gated decision after the above.**

---

## 10. Recommended immediate next actions (first 10 working days)

1. Freeze this implementation plan and open tracking issues per phase ID.
2. Author / generate the full JSON Schema set (P0-01).
3. Implement folder validator + MRO + merge rules (P0-02 … P0-05).
4. Stand up host-owned corrigibility mount and attestation (P0-07, P1-06).
5. Implement central error catalogue (P0-08).
6. Skeleton `casops-eval` that can at least validate schemas and emit a `STATIC_PASS` / `NOT_RUN` report.
7. Begin citation audit backlog: resolve or delete every `[D]`/`[C]`/`[K]` reference in §25.
8. Select one representative agent folder for continuous golden-path testing.

---

## 11. Document control for this plan

| Item | Value |
|---|---|
| Plan version | 1.0 |
| Corresponds to | `common_agent_structure.v3a.md` (2026-08-24) |
| Owner | Host architecture / CASOPS |
| Review cadence | End of each phase |
| Change rule | Material scope changes require an updated plan revision and explicit acknowledgement that the specification remains DRAFT |

**End of implementation plan.**
