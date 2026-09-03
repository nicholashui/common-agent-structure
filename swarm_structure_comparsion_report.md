# Swarm structure comparison report

**File:** `swarm_structure_comparsion_report.md`  
**Date:** 2026-09-03  
**Purpose:** Compare what this checkout actually implements (and has vibe-specified) against the latest research study `common_swarm_structure.md` (`casops.common_swarm.v4`). List structure differences, pros/cons, and recommendations for improving swarm structure in this project.

This report is an analysis. It does not authorize production activation, T3, network grants, plugin execution, L5 promotion, or implementing an LLM as live orchestrator.

---

## 1. What is being compared

This project started from **common-agent folders** (`casops.common_agent.v3`) and a host that can load, compose-preview, run, and chat with **one agent at a time**. Swarm structure was then specified in a vibe loop (`spec/common_swarm_structure.v1.md` → `.v2.md` → `.v3.md`) without a swarm runner.

The new research file is:

| Item | Value |
|---|---|
| File | `common_swarm_structure.md` (same text as `spec/common_swarm_structure.v4.md`) |
| Document ID | `CASOPS-FS-COMMON-SWARM-STRUCTURE-V4` |
| Structure family | `casops.common_swarm.v4` |
| Schema | `4.0` (independent of member schema `3.0`) |
| Self-status | Production-ready **specification**, not a production license; **NO-GO** until citation and local gates clear |

### 1.1 Three layers of “existing”

Calling the current tree “the swarm implementation” is too coarse. There are three layers:

| Layer | What it is | Live in this checkout? |
|---|---|---|
| **A. Member host** | FastAPI `/api/v3` agents, mutation headers, compose-preview (`wrote_locks: false`), `Runtime.execute`, per-agent Chat, LLM router, error catalogue, eight Docker processes | **Yes** |
| **B. Swarm visualization** | UI title **Agent Swarm** (`/`), **Agent Org Chat** (`/org-chat`), **Agent Workflow** SVGs (`/workflow`, `/workflow/sub`). Clicks open Agent Profile/Chat. Pack chips from `agent_id` prefix; categories from live `va_category` | **Yes** (pictures and lists, not a runner) |
| **C. Swarm contract (vibe specs)** | `spec/common_swarm_structure.v1.md` … `.v3.md`: folder type `swarms/`, `swarm_spec.json`, roster/graph, `/api/v3/swarms/...` | **Specified only.** No `swarms/` tree, no `casops` swarm module, no `/api/v3/swarms` routes |

`grep` over `src/casops` and the UI client finds **zero** swarm HTTP paths. The honest baseline for “existing implement” is **A + B**, with **C** as the current design intent that v4 would replace.

### 1.2 Spec ancestry (design only)

```text
v1 (2026-08-17)  /api/v1, casops.common_agent, LangGraph implied
  → v2 (2026-09-03)  bind live host: /api/v3, locate_agent_folder, three UI maps
    → v3 (2026-09-03)  isolation, bulletin, delegation, topology class, conformal commit
      → v4 research     five new swarm-native planes + static plan simulator
```

v4 keeps the v2/v3 thesis: **a swarm composes common agents; it does not replace them; it must not increase a member’s reach.**

---

## 2. Structure differences

### 2.1 Identity and schema

| | Existing implement / vibe v2–v3 | New research (v4) |
|---|---|---|
| Public unit of work | One `agent_id` per HTTP call | One `swarm_id` wrapping many `agent_id`s |
| Member family | `casops.common_agent.v3` / schema `3.0` | Unchanged — members stay v3 |
| Swarm family | v2: `casops.common_swarm.v2`; v3: `.v3`; schema `3.0` tied to members | `casops.common_swarm.v4` / schema **`4.0` independent of member schema** |
| Folder locate | Agents: `locate_agent_folder` (id field, not disk name). Swarm locate specified, not coded | Same locate rule, plus host-owned swarm corrigibility mount |

**Difference.** v4 finally separates swarm schema versioning from agent schema versioning. That is a real improvement if both evolve. The existing tree has no swarm schema file at all (`schemas/` has only `agent_spec` and `compose.lock`).

### 2.2 Planes (the largest structural gap)

Existing **implemented** planes are **member** planes only (execution, cache, protocols, plugins, memory, improvement, safety, corrigibility, eval). The UI adds three **views**, not planes.

Vibe **v2** swarm: membership + graph + critique loop + constraint policies (skill/plugin/identity/memory/LLM).

Vibe **v3** swarm: adds isolation/bulletin/delegation, topology class + optional codebook, commit policy, multi-agent risk fixtures.

**v4 research** names **eight swarm-native planes** plus the nine member planes (seventeen-plane composition):

| # | Swarm-native plane | In live code? | In v2 spec? | In v3 spec? | In v4 research? |
|---|---|---|---|---|---|
| 1 | Topology + pinning | No (Workflow SVG is a picture) | Pattern enum only | Class + optional codebook | Class + codebook + **compile-time propagation analysis** |
| 2 | Coordination / visibility | No (`critique_edges` are I/O lists) | Critique loop | Isolation windows + bulletin + briefs | Phased visibility + bulletin + stigmergy |
| 3 | Delegation + **authority** | No | Graph edges only | Typed brief + condensed return | Brief + **authority envelopes** (attenuation, expiry, joint-scope) |
| 4 | Verification + commit | Per-agent validation `NOT_RUN` | Lead/judge loop | Isolated critique + heuristic stop + conformal commit | **Diversity policy**, **sequential-test governor**, **pre-registered aggregation** |
| 5 | Shared-memory **consistency** | Per-agent memory `mode: none` | Swarm memory list | Bulletin + taint | Declared consistency model + version fences + four failure fixtures |
| 6 | **Scheduling / goodput** | Per-agent `budget_policy` | Budget minima | Budget minima | Sub-deadlines, starvation bound, priority inversion, coordination-overhead ratio |
| 7 | **Propagation containment** | `SAF_CASCADE` code exists; no graph reach analysis | Mention cascade | Hammond fixtures | Blast radius, sanitizer cut-set, worm / topology-guided fixtures |
| 8 | Swarm corrigibility | Host attestation **per agent** | Attest each member | Same | Swarm invariant set, host-owned, agent-unwritable |

v4’s new corollary: **a swarm may not increase any member’s informational, authorizational, or adversarial reach.** Existing code cannot enforce that: there is no compiled outer graph and no reach analysis.

### 2.3 Maps (UI / operator mental model)

| Map | Existing UI | v2 spec | v3 spec | v4 research |
|---|---|---|---|---|
| Fleet / Agent Swarm | Live `/` — all 135 agents | Candidate pool | Same | Filterable by `swarm_id` later |
| Organization | Live `/org-chat` — pack → `va_category` | Same | Same | Same |
| Execution picture | Live `/workflow` SVG; click → Chat | Picture of `graph.json` | Same | Same, plus isolation overlay |
| Isolation | **Absent** | Absent | Specified overlay | Specified |
| **Propagation** | **Absent** | Absent | Absent | **New** read-only heat map of reach / blast radius |

Existing Workflow clicks **must not** start a swarm run (v2 AC-SWM-021). v4 keeps that prohibition. That is already correct in code.

### 2.4 Folder contract

**Existing:** `agents/<folder>/agent_spec.json` + v3 surfaces. No `swarms/`.

**v2 specified:**

```text
swarms/<folder>/
  swarm_spec.json  roster.json  graph.json
  policies/{skill,plugin,identity,interrupt,memory,llm}_policy.json
```

**v3 specified** additionally: `topology/`, `isolation/`, `delegation/`, more policies, `safety/multi_agent_risk.json`.

**v4 specified** additionally:

```text
  topology/propagation_analysis.json     # generated, required before production
  isolation/visibility_schedule.json
  delegation/authority_envelope.schema.json
  policies/{scheduling,authority,consistency,diversity,
            propagation,stopping,aggregation}_policy.json
  safety/fault_injection.json
  corrigibility/swarm_invariants.json    # host-owned mount
  evals/baselines.json
  generated/{swarm_compose,member_matrix,propagation,authority}.lock.json
```

v4 requires **18 policy files** (v3 had ~13; v2 had 6). Authoring cost jumps sharply.

### 2.5 Runtime and HTTP

| | Existing implement | v2 specified | v3 specified | v4 research |
|---|---|---|---|---|
| Runner | `POST .../agents/{id}/runtime/run` inner DAG only | Outer walk wrapping inner `Runtime.execute` | Same + isolation phases | Same + envelopes, sub-deadlines, reach bounds |
| Simulate | None | None | None | **`POST .../runtime/simulate`** — no member invocation |
| Fault inject | Safety red-team fixture per agent | None | Fixtures on paper | **`POST .../faults/inject`** |
| Inspect extras | — | structure, roster, graph | + isolation, bulletin | + **propagation, authority, consistency, scheduling** |
| Chat | Per-agent `runtime/chat` | Explicitly not swarm chat | Same | Same |
| Mutation | Four headers | Same; no fifth header | Same | Same |

v4 adds inspect surfaces that only make sense after compose-preview exists. Implementing run before simulate/propagation would skip the highest-value static gates.

### 2.6 Errors, FRs, acceptance

| | Live catalogue | v2 spec | v3 spec | v4 research |
|---|---|---|---|---|
| Catalogue codes | 93, 12-field, **no `SWM_*`** | Prefer live codes; 7 proposed `SWM_*` | ~15 proposed `SWM_*` | **37** proposed `SWM_*` (22 new vs v3) |
| Membership FR id | n/a | `FR-MEM-*` (collides with member memory FRs) | Same collision | **`FR-MBR-*`** |
| Acceptance criteria | Agent tests live | 24 ACs, many “specified not passing” | 34 | **70** |
| Fixture families | Agent evals | Few | 16 | **47** |

v4’s `FR-MBR-*` rename is a real spec hygiene fix. None of the `SWM_*` codes are in `errors/catalogue.json` today; returning them from the host would violate the live 12-field contract until an amendment.

### 2.7 Validation and citations

| | Existing implement | v4 research |
|---|---|---|
| Default eval | `NOT_RUN` / `pass: false` / `unqualified_instruments` | Same honesty classes |
| Swarm quality | Not measured | **Plan simulator** with eleven instruments **before** a runner |
| Citations | Host `casops-citation`; swarm v3 used non-standard `[A-abstract]` | Unified `[A]/[D]/[C]/[K]` + depth `P/B/N`; **0 external page-depth confirms**; `CIT-GATE-001` **BLOCKED**; v3’s headline papers reclassified `[D:B]` |

v4 is more honest than v3 about evidence. It is also **heavier** and still **NO-GO**.

### 2.8 What existing code already matches v4 (do not redo)

These v4 rules are already true of the member host. A swarm layer should reuse them, not reimplement:

- Public plane `/api/v3` only; `/health` and `/debug/*` excluded from OpenAPI  
- Four mutation headers; `IMP_UNSIGNED`; deny-by-default actors  
- `locate_agent_folder` by `agent_id` (`_template_v3` ≠ public id)  
- Compose-preview `wrote_locks: false`  
- Empty `allowed_tools` / `allowed_plugins`; T3 off; memory `mode: none` → `MEM_TRUST_TIER`  
- Chat does not write memory, run plugins, or enable T3  
- Org Chat is read-only; Workflow click opens Chat  
- UI must not invent `va_category`  
- Tests must not hard-code live agent count `135`

---

## 3. Pros and cons

### 3.1 Existing implementation (member host + three UI maps)

**Pros**

- **Shippable operator loop today.** List agents, inspect structure, compose-preview, run one DAG, chat, attest, log.  
- **Fail-closed is real code**, not prose: unsigned mutations 409, agent cannot approve, unknown agent `INH_PARENT_MISSING`.  
- **Cheap mental model.** One `agent_id` = one folder = one Chat. Operators already use Fleet / Org / Workflow.  
- **Fits the loaded pack.** 114 `video.*` + 19 `specials.*` are independently chattable without inventing a 114-node spine.  
- **Low authoring cost.** No 18-file swarm folder to keep in sync.  
- **Visualization without a fake runner.** Workflow SVG is honest: a picture, not `runtime/run`.

**Cons**

- **No crew semantics.** There is no roster, no owner, no outer visit cap, no handoff artifact between `video.screenwriter` and `video.director`.  
- **Critique is not a bus.** `critique_edges` drive IoPanel and org grouping, not isolated gathering or commit.  
- **Reach is unbounded in the picture.** A Workflow SVG can draw edges that would be illegal under v4 blast-radius rules; nothing checks them.  
- **Delegation is informal.** Chat to orchestrator cannot mint an attenuated authority envelope; a compromised node has whatever the host LLM + empty tool list allows — tools are empty, but **information** still flows through Chat history.  
- **Scheduling is per-agent only.** No swarm-level starvation or sub-deadline.  
- **“Agent Swarm” UI label oversells.** The home page is a fleet, not a swarm run.  
- **Vibe specs drifted.** v1 (`/api/v1`, LangGraph) vs live host; v3 added research planes still unimplemented; operators cannot tell which spec is the contract.

### 3.2 Existing vibe swarm specs (v2–v3, not coded)

**Pros**

- v2 correctly **rebounds** v1 onto the live host (ports, headers, locate, three maps).  
- v3 names isolation, bulletin, and “debate is not a verifier” — the right instincts for a video pack with critic/judge.  
- Prefer live error codes over inventing `SWM_*` until the catalogue is amended.

**Cons**

- **Specified but not executed.** ACs that 404 teach nothing.  
- v3 **citation overclaim** (`[A-abstract]` on coordination papers) is exactly what v4 walks back.  
- `FR-MEM-*` collision with the member memory plane.  
- Heuristic stop (`no_gain_2_consecutive`) has no error budget.  
- Bulletin without a consistency model.  
- Topology pinned but never analyzed — a legal graph can still connect untrusted retrieval to publish.

### 3.3 New research (v4)

**Pros**

- **Closes real multi-agent holes** the current host cannot see: authority amplification, aggregation inference, concurrent shared writes, topology as attack surface, starvation, verifier collapse, heuristic stopping.  
- **Reach-is-computed** (S29) is the highest-leverage idea for *this* repo: you can run a static analyzer on a declared `graph.json` (or even on Workflow SVG `a.agent-link` + drawn edges) **before** any swarm HTTP.  
- **Plan simulator** (`runtime/simulate`) gives orchestration metrics without invoking members — matches the project’s eval honesty (`NOT_RUN` until instruments qualify).  
- **Independent justifications** (§2.4): controls survive citation failure. That is how this host already treats T3/L5 (implemented, gated, off).  
- **Schema 4.0** decoupled from member `3.0`.  
- **`FR-MBR-*`**, unified citation markers, no fifth mutation header — compatible with live `casops.api.control`.  
- Explicit **quarantine** of learned topology search and LLM-as-orchestrator (E4) — agrees with current “no auto-orchestrate” UI ban.

**Cons**

- **Not implementable as a single vibe pass.** 147 FR rows, 22 policy objects, 37 error codes, 70 ACs, 47 fixture families. Dropping that on a host that still has no `swarms/` scan will stall.  
- **Authoring burden.** Eighteen required policy files per swarm vs today’s zero. The video pack will not get a correct `video.spine` if every policy is copy-paste `deny: []`.  
- **Citation is BLOCKED and worse than v3 claimed.** Zero external `[A:P]`. Numeric thresholds in v4 (α/β, blast radius, overhead ratios) **must not** be copied into tests as if measured here.  
- **Upstream date defect (`UP-AGT-001`)** in the member contract is a compose-abort in v4 — cheap to fix, easy to forget.  
- **Risk of paper-architecture.** Authority envelopes, sequential tests, and MAST attribution are unused until there is an outer walk. Building them before compose-preview repeats the v3 pattern (spec richness, zero runtime).  
- **UI explosion.** Five new `/swarms/:id/*` screens on top of an already dense Agent Profile.  
- **Catalogue amendment required** before any `SWM_*` is returned; otherwise the live 12-field contract is violated.

---

## 4. Side-by-side: what would change for *this* project

| Concern | If we stay on existing implement | If we adopt v4 wholesale now | Better middle |
|---|---|---|---|
| Operator value | Chat/run any of 135 agents | Many new empty screens | Named `video.spine` subset + compose-preview |
| Safety | Tools empty; no crew reach analysis | Full envelopes + blast radius | **Static propagation on a declared graph first** |
| Eval honesty | `NOT_RUN` is correct | Simulator can score plans without lying about runs | Implement simulate **before** run |
| Spec vs code | Specs ahead of code (v3) | Specs much further ahead (v4) | Freeze a **thin v2-grain folder + v4 static gates** |
| Citations | Host citation audit exists | Swarm CIT-GATE blocked | Do not gate product on unaudited paper numbers |
| Risk | Under-specified crew | Over-specified crew | Phase: preview → propagate → simulate → isolate → run |

---

## 5. Recommendations (what to improve, in order)

These are project recommendations, not a license to enable forbidden ops.

### 5.1 Do not do

1. Do not implement `POST /api/v3/swarms/{id}/runtime/run` first. That skips v4’s only pre-runner measurements.  
2. Do not treat Workflow SVG clicks as swarm run. Keep Chat.  
3. Do not add a swarm Chat or make Org Chat writable.  
4. Do not enable T3, network, plugins, or `production_activation_requested` via swarm JSON.  
5. Do not put learned topology generators or “LLM orchestrator” on the serving path (v4 E4).  
6. Do not return `SWM_*` until `errors/catalogue.json` has 12-field rows. Until then map to live codes (`INH_PARENT_MISSING`, `INH_STRUCTURE_MISMATCH`, `PERF_PLAN_CYCLE`, `SKL_TOOL_LEAK`, `GATE_*`, `SAF_CASCADE`, …) as v2 already requires.  
7. Do not copy v4 numeric TARGET tables into pytest as if locally measured.  
8. Do not invent `va_category` or dump all 114 `video.*` agents into one spine.

### 5.2 Keep (existing strengths)

1. Member v3 folder contract and `locate_agent_folder`.  
2. Four-header mutation contract; no fifth header (v4 agrees).  
3. Three maps as views over members.  
4. Eval default `NOT_RUN` / `pass: false`.  
5. Per-agent Chat with `memory_writes: []`, `plugins_executed: false`, `t3_enabled: false`.

### 5.3 Improve, phased

**Phase 0 — honesty and spec freeze (cheap, this week)**

- Treat `common_swarm_structure.md` (v4) as the **research target**, `spec/common_swarm_structure.v2.md` as the **minimum implementable contract**, and v3 as a superseded midpoint. Put that sentence in `implementation_status.md` so vibe work stops mixing `/api/v1`, LangGraph, and v4 envelopes in one PR.  
- Fix member-contract date drift (`UP-AGT-001`) if v4 compose will later abort on it.  
- Rename any leftover swarm `FR-MEM-*` in notes to `FR-MBR-*` so they do not collide with memory-plane FRs.

**Phase 1 — thinnest live swarm object (unblocks everything else)**

Implement only:

- `CASOPS_SWARMS_ROOT` (default `swarms/`)  
- `locate_swarm_folder`  
- template `swarms/_template_v2/` or `_template_v4/` with **one node** (`casops.template.baseline_safe`) so `max_peer_hops: 0` still closes  
- `GET /api/v3/swarms` and `GET .../structure|roster|graph`  
- `POST .../compose-preview` with `wrote_locks: false`, per-member `Composer.preview`, `production_activation_requested` remains false  

This is v2 grain. It reuses live compose. It does not need 18 policy files yet: start with the v2 six, default extra v4 policies to **deny/min/off**.

**Phase 2 — static propagation (highest v4 value, no runner)**

- Author `video.spine` as a **subset** roster (the nine live ids already used in v2’s worked example: orchestrator, planner, creativedirector, screenwriter, webresearch, aiqaconsistency, gatekeeper, critic, judge). Copy `va_category` from disk (`1-ATL`, `6-Dist`, `8-AI`, `9-Meta`, `10-Sup`).  
- Compile reach / blast radius from `graph.json` (and optionally from Workflow SVG edges).  
- Fail compose if untrusted retrieval can reach an irreversible/publish node with no sanitizer cut (`video.gatekeeper` is the likely only cut — **prove it**).  
- Expose `GET .../topology/propagation` (read-only). Optional UI: a fourth map, not a control.

This is the v4 finding that applies to the **current** 135-agent pack before any outer `run`.

**Phase 3 — plan simulator (eval honesty)**

- `POST .../runtime/simulate`: no member `Runtime.execute`, no Chat, no memory writes.  
- Emit the plan-grade instruments v4 lists (visit feasibility, reach bound, deadline decomposition, coordination-overhead **plan** ratio). Label them plan-grade, not run-grade.  
- Keep default swarm validation `NOT_RUN` until instruments are qualified — same as members.

**Phase 4 — coordination without debate-as-verifier**

- Isolation / visibility windows for any parallel search nodes.  
- Bulletin with an explicit consistency model (start with **single-writer** or **host-sequenced**; do not start with unbounded eventual).  
- Critique: keep `max_refinement_count: 0` on current video members until a diversity policy exists; do not turn on a 3-iteration loop that the member specs already set to 0.  
- Commit: act-or-defer at publish; `independent_approver` for irreversible steps (already the live approve rule).

**Phase 5 — authority envelopes (before multi-hop run)**

- Mint only as `host_service`; never `agent_runtime`.  
- Monotone attenuation, `not_after`, `max_invocations`.  
- Joint-scope grant for joining two partitions (v4 S27) — relevant if critic+judge see disjoint evidence.  
- Do not expose envelope mint in the UI.

**Phase 6 — scheduling and fault injection (after a real outer walk)**

- Sub-deadlines min’d with member `max_job_ms`.  
- Fault-injection suite only once `runtime/run` exists; until then, keep member red-team as-is.

### 5.4 UI recommendations

- Keep **Agent Swarm** as the fleet unless/until a swarm is selected; then filter by roster (`?swarm=`).  
- Do not add envelope editors or “generate topology”.  
- If a propagation map is added, read-only, like Org Chat.  
- Help: generate `/docs/swarms/<id>/` the same way agent Help is generated; do not inline 135 SPECs into the operator book.

### 5.5 Suggested contract for the next implementation PR

A single PR should be allowed to claim “swarm structure started” only if it delivers **Phase 1 + Phase 2 static fail-closed**, with tests that:

- unknown `swarm_id` → `INH_PARENT_MISSING`  
- member not v3 → `INH_STRUCTURE_MISMATCH`  
- unsigned POST → `IMP_UNSIGNED`  
- `wrote_locks === false`  
- a fixture graph with retrieval → publish and no sanitizer **fails compose**  

That is a v4-shaped **gate** on a v2-shaped **folder**, which is the improvement this project can actually absorb.

---

## 6. Summary judgment

| Question | Answer |
|---|---|
| Is the new research better architecture than the vibe swarm specs? | **Yes**, especially authority attenuation, consistency, reach analysis, stopping/aggregation honesty, and pre-runner simulation. |
| Should this repo switch the live host to v4 overnight? | **No.** There is still no swarm folder or HTTP. v4 is NO-GO on citations and is too large to vibe-implement as one structure. |
| What is the existing implement good at? | Single-agent fail-closed ops and honest visualization. |
| What is it bad at as a “swarm”? | Crew identity, handoffs, reach, isolation, and any claim that Fleet is a swarm run. |
| Best improvement? | **Thin `swarms/` + compose-preview + static propagation analyzer** on a small `video.spine`, then simulate, then isolate, then run. Keep member Chat/Workflow behavior. |

**Existing implement:** a strong **agent** host with swarm **pictures**.  
**New research:** a complete **swarm** contract that this host is not yet ready to execute, but whose **static reach and simulate** pieces are the right next structure — if they are implemented without pretending the rest is live.
