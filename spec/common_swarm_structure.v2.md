# `common_swarm_structure.v2.md`

> **Delivery note — read first.**
>
> 1. **This checkout is a live CASOPS host.** Unlike `common_agent_structure.v3.md`, which was written before a runnable artifact existed, v2 of the swarm structure is written **against the running tree** `C:\Project\common-agent-structure`: package `casops` `0.1.0`, public plane FastAPI `/api/v3` on `127.0.0.1:18080`, Control UI Vite+React on `127.0.0.1:15173`, member family `casops.common_agent.v3` / schema `3.0`.
> 2. **Honesty about what is live.** Member agents, per-agent compose/run/chat, Fleet (UI label **Agent Swarm**), Agent Workflow SVGs, and Agent Org Chat **are implemented**. A `swarms/` folder type, `swarm_spec.json` loader, and `/api/v3/swarms/...` routes **are specified here and are not implemented in this checkout.** This document does not pretend those routes already exist.
> 3. **This is not a production-activation license.** It does not authorize T3 enablement, network grants, plugin execution on the public plane, L5 promotion, or flipping `production_activation_requested`.
> 4. **v1 is superseded, not deleted.** v1 (`2026-08-17`) is the design ancestor. v2 keeps v1’s thesis — a swarm composes common agents; it does not replace them — and rewrites every surface that drifted from the live host.

---

**Document ID:** `CASOPS-FS-COMMON-SWARM-STRUCTURE-V2`  
**Date:** 2026-09-03  
**Status:** Implementation specification — swarm folder and swarm HTTP routes are specified, not live; member agents and visualization surfaces are live  
**Supersedes:** `spec/common_swarm_structure.v1.md` (`CASOPS-FS-COMMON-SWARM-STRUCTURE`, 2026-08-17)  
**Host:** `common-agent-swarm-ops` (`casops` `0.1.0`)  
**Structure family:** `casops.common_swarm.v2`  
**Member family:** `casops.common_agent.v3` (schema `3.0`)  
**Public HTTP plane:** FastAPI prefix `/api/v3` only  
**Control-plane bind:** `http://127.0.0.1:18080`  
**Control UI:** `http://127.0.0.1:15173` (`ui/`)  
**Compatibility:** v1 swarm JSON loads only through the §22 migration profile  
**Research cutoff:** 2026-09-03 (this checkout)

A v2 common swarm remains **one self-contained folder and one `swarm_id`**. Every member is a **common-agent v3 folder**. The swarm names, wires, budgets, and (when implemented) walks those members. It does not own their SPEC, tools, credentials, persona, corrigibility invariants, or host LLM keys.

Domain logic stays in the pack. The host stays fail-closed. FastAPI `/api/v3` is the only public control plane. This is host-native composition, not Agent-to-Agent (A2A) transport, not LangGraph, and not a second UI backend.

---

## Table of contents

1. Purpose, v2 changes, and v1 defect register  
2. Live host facts this specification binds to  
3. Scope, actors, and non-goals  
4. Core principles  
5. Three maps: fleet, organization, execution  
6. Folder contract  
7. Membership — every node is a common-agent v3  
8. Roster and organization  
9. Graph, DNA, and patterns  
10. Critique bus, I/O, and handoffs  
11. Skill, plugin, identity, memory, and LLM policy  
12. Budgets, risk gates, interrupts, rollback, corrigibility  
13. Data models  
14. Runtime behaviour  
15. Operator and host APIs (`/api/v3`)  
16. Control UI mapping  
17. Honesty, safety, and fail-closed rules  
18. Error catalogue  
19. Acceptance criteria  
20. Worked example (`video.spine`)  
21. Proposed template  
22. Migration from v1  
23. Traceability  
24. Open risks  
25. Document control  

---

# 1. Purpose, v2 changes, and v1 defect register

## 1.1 Purpose

Operators need a swarm that is as explicit as a common agent, without inventing a second kind of runtime identity and without inventing a second control plane.

1. **Named crew.** A swarm lists member `agent_id`s. Each member is a common-agent v3 folder located the same way the host already locates agents, not a prompt alias and not necessarily a folder whose name equals the id.  
2. **Bounded graph.** Nodes, edges, entry, terminals, visit caps, and compensation are declared. The runner is the host `casops.runtime` DAG executor wrapping per-member `Runtime.execute`, not LangGraph.  
3. **Governed run.** Budgets, risk gates, human interrupts, and critique loops are first-class. Mutation headers are the same four headers the live plane already requires.  
4. **Honest compose.** Inheritance, skill toggles, plugins, memory, cache tiers, and persona overlays stay on the **agent**. The swarm may constrain them; it may not silently grant tools, plugins, network, T3, or production activation.  
5. **Honest UI.** The live Control UI already shows three maps of the same members (Fleet, Org Chat, Workflow). v2 names those maps instead of declaring UI out of scope.

## 1.2 Material changes from v1

| Domain | v1 | v2 |
|---|---|---|
| Public plane | `/api/v1/swarms/...` | Companion paths under live `/api/v3` only. OpenAPI remains `/api/v3`-prefixed. `/health` and `/debug/*` stay non-v3. |
| Member family | `casops.common_agent` | `casops.common_agent.v3` / schema `3.0` |
| Swarm family | `casops.common_swarm` | `casops.common_swarm.v2` / schema `3.0` |
| Locate member | `agents/<agent_id>/` | `locate_agent_folder`: folder name **or** `agent_spec.json` `agent_id` (live: `_template_v3` → `casops.template.baseline_safe`) |
| Engine | “host already owns LangGraph” | Host runner is `casops.runtime.executor.Runtime` compiling `runtime/execution.json` (`casops.execution_dag.v2`). Swarm walk is specified, not live. |
| Mutation | “operator identity, append-only audit” | Four headers: `x-casops-actor`, `x-casops-reason`, `x-casops-expected-parent`, `x-casops-dry-run`. Missing any → `IMP_UNSIGNED` HTTP 409. |
| Actors | Pack author / operator / host / reviewer / governor | Live `ActorClass`: `human_operator`, `independent_approver`, `host_service`, `agent_runtime`, `plugin`, `peer_agent`. Deny-by-default. `agent_runtime` cannot approve. |
| UI | Explicitly out of scope | Mapped onto live routes: `/` Agent Swarm, `/org-chat`, `/workflow`, `/workflow/sub`, `/agents/:id/*`, `/settings` |
| Org departments | Hard-coded film departments | Live `va_category` on member specs. UI must not invent categories. Pack prefix `specials.` / `video.` / other. |
| Critique | Swarm loop plus member edges | Live `critique_edges.inputs/outputs` feed Chat I/O and are **not** a write bus. Org Chat is read-only. Swarm loop remains specified. |
| Compose preview | Implied lock files / `resolved.json` in the swarm folder | Matches live compose-preview: in-process, `wrote_locks: false`. Generated resolved artifacts are not hand-edited. |
| Tools | `media.stub` assumed present | Live pack agents ship `allowed_tools: []`. Node `tool_ids` ∩ member allow-list ∩ host register; empty ∩ anything is empty. |
| Plugins | Not in v1 | Swarm cannot execute plugins. Public `plugins/validate` returns `executed: false`. Isolation I1/I2/I3 stay host-owned. |
| Memory | Swarm memory list | Live template `memory.policy.mode: none` → `MEM_TRUST_TIER` on write. Swarm cannot promote trust. Consolidate enqueues only. |
| Cache | Absent | T0–T3 exist; T3 default off. Swarm cannot enable T3. |
| LLM | Absent | Host-owned router (`local_deterministic`, `openai`, `xai`, `anthropic`). Swarm JSON cannot store keys or grant network by picking a provider. |
| Chat | Absent | Live `POST /api/v3/agents/{agent_id}/runtime/chat`. No swarm-chat route. No memory writes, no plugins, no T3. |
| Errors | 13 `SWM_*` strings, no 12-field contract | Prefer live catalogue codes. Swarm-specific leftovers get a 12-field contract and are **proposed**, not in `errors/catalogue.json` until a catalogue amendment. |
| Eval honesty | Not stated | `NOT_RUN` / `INDICATIVE` are not a pass. Unqualified instruments cannot gate a swarm. |
| Ports | Unspecified | Control plane `18080`, UI `15173`, preview `4173`, internal `8081`–`8087` never from the browser. |

## 1.3 v1 defect register (normative — these are closed in v2)

| ID | v1 defect | v2 correction |
|---|---|---|
| D-SWM-01 | Public paths under `/api/v1` | All swarm HTTP is `/api/v3/swarms/...` (companion, like LLM and chat). |
| D-SWM-02 | Member `structure_id` `casops.common_agent` | Required `casops.common_agent.v3`. Else `INH_STRUCTURE_MISMATCH`. |
| D-SWM-03 | Folder path equals `agent_id` | Use live `locate_agent_folder`. |
| D-SWM-04 | LangGraph implied as host engine | Host DAG IR `casops.execution_dag.v2` in `runtime/execution.json`. |
| D-SWM-05 | UI declared out of scope while the host now has a Control UI | §16 maps every live route. `spec/ui.v1.md` still says “Fleet” / “UI not implemented”; v2 binds to **live** labels (Agent Swarm, Agent Workflow, Agent Org Chat, Agent Profile). |
| D-SWM-06 | `SWM_*` codes not in the 93-code, 12-field catalogue | §18 mapping table. Do not return a code the catalogue does not own unless the catalogue is amended. |
| D-SWM-07 | `schema_version: "1.0"` on swarm JSON | `3.0`, matching agent schema and catalogue `schema_version`. |
| D-SWM-08 | PUT roster/graph without mutation contract | POST/PUT/PATCH/DELETE require the four headers. GET does not. |
| D-SWM-09 | Assumed `media.stub` | No implicit tool. Empty allow-list stays empty. |
| D-SWM-10 | `resolved.json` as a writable folder file | Preview is in-memory. Hand-edited generated files fail `INH_RESOLVED_DRIFT`. |
| D-SWM-11 | Critique loop described as if it were the live I/O panel | Live `critique_edges` are declared I/O lists. Swarm critique loop is a future walk, not Chat. |
| D-SWM-12 | “Specials may join only as common-agent folders” as if they were optional outsiders | This checkout already loads **19** `specials.*` and **114** `video.*` plus `casops.template.baseline_safe` and `common.health` (135 `agent_spec.json` folders, 2026-09-03). All are v3. |
| D-SWM-13 | Org departments invented in prose | Departments = live `va_category` values actually present. Never invent. |
| D-SWM-14 | No corrigibility / containment | Swarm cannot rewrite host invariants. Tamper → `IMP_CORRIGIBILITY` containment stop. Unknown actor header already maps to `IMP_CORRIGIBILITY`. |
| D-SWM-15 | dry-run described as “no side effects” | Live dry-run still executes a member DAG in-process (traces/artifacts in HostState). Swarm dry-run MUST document the same honesty. |

## 1.4 What v2 does not change

- One folder = one `swarm_id`.  
- Members are common agents; aliases and prompt-only roles are illegal.  
- Swarm composes; agent owns SPEC, tools, persona, inheritance.  
- Safety tightens (min / intersection / AND-false).  
- Owner is a member.  
- Org chart ≠ execution graph.  
- Host stays domain-agnostic. No A2A. No second control plane.  
- This document alone does not mutate live pack trees.

---

# 2. Live host facts this specification binds to

Measured against this checkout on 2026-09-03. If a later tree drifts, regenerate claims from the tree; do not freeze a magic agent count in tests.

## 2.1 Process and ports

| Process | Bind | Notes |
|---|---|---|
| Control plane | `127.0.0.1:18080` | `casops.api.control:create_app_from_env` |
| Control UI (dev) | `127.0.0.1:15173` | Vite `strictPort: true`; proxies `/api`, `/health`, `/debug` |
| Control UI (preview) | `127.0.0.1:4173` | CORS allowed |
| Internal services | `8081`–`8087` | Docker only; **not** browser-reachable by contract |
| Start / stop | `scripts/start_all.ps1`, `scripts/stop_all.ps1` | Writes `var/casops-servers.json` |

`GET /health` body: `{ "status": "ok", "service": "control-plane" }`. Not in OpenAPI.

## 2.2 Public plane already implemented (members)

Spec §19 paths (`SPEC_V3_PATHS`, 35) plus companion paths (`COMPANION_V3_PATHS`): `GET /api/v3/agents`, LLM settings, per-agent LLM, `POST /api/v3/agents/{agent_id}/runtime/chat`.

Swarm routes in §15 are **additions to the companion set**, not a new prefix.

## 2.3 Mutation contract (already implemented)

Every `POST`, `PUT`, `PATCH`, `DELETE` under `/api/v3` requires:

| Header | Example | Rule |
|---|---|---|
| `x-casops-actor` | `host_service` | Must parse to `ActorClass` |
| `x-casops-reason` | `swarm-preview` | Non-empty |
| `x-casops-expected-parent` | `none` | Required even when literal `none` |
| `x-casops-dry-run` | `true` | `1` / `true` / `yes` (any case) means dry-run |

Unsigned body: `error.code = IMP_UNSIGNED`, HTTP 409. Chat may substitute reason fallback `"operator chat"` in the UI client only.

## 2.4 Actor allow-list (already implemented)

Deny-by-default. `approve_candidate` is `independent_approver` only. `agent_runtime`, `plugin`, and `peer_agent` cannot author swarm JSON, cannot approve, cannot write invariants, cannot change host or per-agent LLM.

## 2.5 Loaded members (already implemented)

`GET /api/v3/agents` lists every child of `CASOPS_AGENTS_ROOT` (default `agents/`) that contains `agent_spec.json`, sorted by folder name case-insensitive.

This checkout, 2026-09-03:

| Pack prefix | Count | How the UI derives the pack |
|---|---|---|
| `video.` | 114 | `agentPack` → `video` |
| `specials.` | 19 | `agentPack` → `specials` |
| other | 2 (`casops.template.baseline_safe`, `common.health`) | `other` |
| **Total folders with `agent_spec.json`** | **135** | Fleet count label |

Template folder on disk is `agents/_template_v3/`; public id is `casops.template.baseline_safe`.

## 2.6 Visualization surfaces already implemented (not a swarm runner)

| UI route | Live behaviour | Swarm map |
|---|---|---|
| `/` | Fleet, title **Agent Swarm**, `GET /api/v3/agents` | Candidate pool of members |
| `/org-chat` | Read-only org chart by Agent Group then `va_category`; click opens Agent Profile | Organization view |
| `/workflow` | SVG `ui/public/svg/video.workflow.svg`; `a.agent-link` → `/agents/{id}/chat` | Execution-graph **picture** for pack `video` |
| `/workflow/sub` | Template A–J, Scale S1–S7 SVGs | Pattern variants; still pictures, not a run |
| `/agents/:id` … | Agent Profile tabs | Member inspect/run/chat |
| `/settings` | Base URL, actor defaults, DEFAULT_LLM | Host settings; not swarm JSON |

There is **no** `/swarms/:id` route in `ui/src/App.tsx` today.

## 2.7 Member I/O already implemented

`critique_edges.inputs` / `outputs` on `agent_spec.json` become GET structure `io` (`merged: false`) and GET resolved `io` (`merged: true`). Chat `IoPanel` renders those lists. Chat still accepts free-text operator messages when I/O is undeclared.

## 2.8 What a swarm must not fight

- `production_activation_requested: false` on the template and on loaded pack agents as shipped.  
- `allowed_tools: []`, `allowed_plugins: []`, `model_policy.network_access: false`.  
- Memory `mode: none` on the template → writes `MEM_TRUST_TIER`.  
- Cache T3 off.  
- Validation default `verdict: NOT_RUN`, `pass: false`, `reason: unqualified_instruments`.  
- Compose-preview `wrote_locks: false`.  
- Plugins validate `executed: false`.  
- Consolidate `{ queued: true }` does not drain on the serving path.

---

# 3. Scope, actors, and non-goals

## 3.1 In scope

- Every swarm folder that declares `structure_id: casops.common_swarm.v2` and `schema_version: "3.0"`.  
- Membership restricted to common-agent v3 folders the live host can already locate.  
- Roster, organization (Agent Group → `va_category` → members), execution graph, critique loop, budgets, risk gates, human interrupts, rollback.  
- Swarm-level **constraints** on skills, plugins, identity disclosure, memory writes, cache tiers, and LLM overrides (deny/require only).  
- Host REST routes for inspect, preview, and run **on the existing FastAPI plane**.  
- Control UI mapping onto live screens plus a future swarm profile.  
- Acceptance tests and a worked spine that names **live** `agent_id`s.  
- JSON Schema for `swarm_spec.json`.  
- Migration from v1.

## 3.2 Out of scope

- Mutating live pack trees by this document alone.  
- Implementing `/api/v3/swarms` in this revision of the spec (the spec is the contract; code is a later task).  
- LangGraph, A2A (agent cards, JSON-RPC tasks, cross-vendor discovery), MCP servers, credential vaults.  
- Calling internal ports `8081`–`8087` from the browser or from swarm JSON.  
- Granting production activation, network, T3, or plugin execution via swarm JSON.  
- A swarm-wide Chat that bypasses per-agent `runtime/chat`.  
- Treating Org Chat as a write surface.  
- Inventing `va_category` values.  
- Promoting L5 research isolation into the serving tree.  
- Storing provider API keys in swarm files or Settings known-ids.

## 3.3 Actors (live enum)

| Actor | Swarm effect |
|---|---|
| `human_operator` | Inspect; start dry-run preview; operator shutdown; cannot approve candidates; cannot write invariants |
| `independent_approver` | Approve improvement candidates; write invariant reference; instrument records; L5 research write |
| `host_service` | Attest invariants; compose-preview; run; write instrument records |
| `agent_runtime` | **Denied** for swarm authoring, approve, LLM settings, invariant writes |
| `plugin` | **Denied** |
| `peer_agent` | **Denied** as an HTTP actor. Critique messages are host-mediated JSON between member ids, not this actor class on the wire |

Pack author is a human who edits files on disk. Reviewer / CI consumes evals. Human governor is `independent_approver` plus out-of-band change control — never `agent_runtime`.

---

# 4. Core principles

| ID | Principle | Meaning |
|----|-----------|---------|
| S1 | One swarm identity | One folder = one `swarm_id`. Folder name MAY differ from `swarm_id` the same way `_template_v3` differs from `casops.template.baseline_safe`. |
| S2 | Members are common-agent v3 | Every roster and graph `agent_id` MUST resolve via `locate_agent_folder` to a folder whose `structure_id` is `casops.common_agent.v3` and `schema_version` is `3.0`. |
| S3 | Swarm composes, agent owns | Wiring lives on the swarm. SPEC, prompts, rubrics, tools, plugins, persona, inheritance, corrigibility projection, and memory policy live on the agent. |
| S4 | Safety tightens | Budget is **min** of swarm caps and each running member’s `budget_policy`. Tools are **intersection** of node `tool_ids`, member `allowed_tools`, and host register. Plugins same intersection with `allowed_plugins`. Network, T3, and production flags **AND** across members and swarm (`false` wins). |
| S5 | Owner is a member | `owner_agent_id` MUST be on the roster and MUST locate. |
| S6 | Critique is composition | Critique edges are host-mediated peer messages between running member identities, not parent mixins, not A2A, and not the live Chat textarea. |
| S7 | Fail closed | Missing member, structure mismatch, unbounded cycle, budget breach, undeclared tool/plugin, unsigned mutation → abort. |
| S8 | Disclose overlays | If any running member is not `grounded`, the swarm run artifact lists that member’s disclosure. Named-person overlays without approval abort (`IDN_NAMED_PERSON`). |
| S9 | Three maps, one roster | Fleet = pool. Org Chat = category view. Graph / Workflow SVG = run order. A department label is not an `agent_id`. |
| S10 | Host stays domain-agnostic | Domain steps stay in the pack swarm folder. No second control plane. No browser calls to `8081`–`8087`. |
| S11 | Mutation contract is host-owned | Swarm routes do not invent a fifth header and do not skip dry-run. |
| S12 | Preview does not write locks | Swarm compose-preview MUST return `wrote_locks: false`, matching live agent compose-preview. |
| S13 | Eval honesty | Unqualified instruments → `NOT_RUN` / `pass: false`. Screening `INDICATIVE` cannot pass a swarm. |
| S14 | Agent cannot approve the swarm | `agent_runtime` on approve or corrigibility write → `IMP_SELF_APPROVAL` / `IMP_CORRIGIBILITY`. |

---

# 5. Three maps: fleet, organization, execution

v1 drew organization vs graph. The live UI already has **three** maps of the same members. v2 makes that normative.

<div role="img" aria-label="Three maps of the same members: Fleet, Org Chat, Workflow">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 560" role="img" aria-labelledby="swv2-maps-t swv2-maps-d">
  <title id="swv2-maps-t">Three maps, one roster</title>
  <desc id="swv2-maps-d">Fleet lists members. Org Chat groups them by pack and va_category. Workflow SVG shows a declared execution picture. None of these is a second control plane.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .m{fill:#334155;font:400 11px ui-monospace,Menlo,Consolas,monospace}
      .c1{fill:#EEF2FF;stroke:#A5B4FC;stroke-width:1.5}
      .c2{fill:#F5F3FF;stroke:#C4B5FD;stroke-width:1.5}
      .c3{fill:#ECFDF5;stroke:#86EFAC;stroke-width:1.5}
      .core{fill:#4F46E5}
    </style>
  </defs>
  <rect class="bg" width="1440" height="560"/>
  <text class="ink" x="40" y="42">Three maps — live Control UI</text>
  <text class="sub" x="40" y="66">Same agent_id values. Different questions. None of these writes swarm_spec.json.</text>
  <rect class="c1" x="40" y="96" width="440" height="420" rx="16"/>
  <text class="h" x="64" y="128">Fleet  ·  /</text>
  <text class="m" x="64" y="156">UI title: Agent Swarm</text>
  <text class="b" x="64" y="188">GET /api/v3/agents</text>
  <text class="b" x="64" y="212">Pack chips: All, specials, video, other</text>
  <text class="b" x="64" y="236">Category filter = live va_category</text>
  <text class="b" x="64" y="260">Open → Agent Profile</text>
  <text class="b" x="64" y="284">Compose preview → member compose</text>
  <text class="b" x="64" y="332">Question: which members exist?</text>
  <rect class="c2" x="500" y="96" width="440" height="420" rx="16"/>
  <text class="h" x="524" y="128">Org Chat  ·  /org-chat</text>
  <text class="m" x="524" y="156">Read-only React Flow chart</text>
  <text class="b" x="524" y="188">Agent Group → va_category → agent</text>
  <text class="b" x="524" y="212">Click agent → /agents/{id}</text>
  <text class="b" x="524" y="236">Does not POST runtime/chat</text>
  <text class="b" x="524" y="260">Does not invent categories</text>
  <text class="b" x="524" y="332">Question: how do humans group them?</text>
  <rect class="c3" x="960" y="96" width="440" height="420" rx="16"/>
  <text class="h" x="984" y="128">Workflow  ·  /workflow</text>
  <text class="m" x="984" y="156">SVG object, not a runner</text>
  <text class="b" x="984" y="188">video.workflow.svg</text>
  <text class="b" x="984" y="212">Sub: Template A–J, Scale S1–S7</text>
  <text class="b" x="984" y="236">a.agent-link → /agents/{id}/chat</text>
  <text class="b" x="984" y="260">Does not walk graph.json yet</text>
  <text class="b" x="984" y="332">Question: what order is declared?</text>
  <rect class="core" x="40" y="500" width="1360" height="36" rx="8"/>
  <text class="h2" x="64" y="524">When /api/v3/swarms exists, Fleet/Org/Workflow become views over a named swarm_id. Until then they view the whole loaded pack.</text>
</svg>
</div>

| Map | Source of truth today | Source of truth after swarm routes exist |
|---|---|---|
| Fleet | `GET /api/v3/agents` | Intersection of that list with `roster.json` when a swarm is selected |
| Org | `va_category` + pack prefix | Roster `department` **must equal** a live `va_category` or the empty/uncategorized bucket; it must not introduce a new string |
| Execution picture | Pack SVG under `ui/public/svg/` | `graph.json` MAY generate or pin an SVG; clicks still open Agent Profile/Chat |
| Execution | Per-agent `POST .../runtime/run` | Swarm `POST .../swarms/{id}/runtime/run` walks `graph.json` |

---

# 6. Folder contract

## 6.1 Tree

```text
swarms/<folder>/
  README.md
  SWARM.md
  swarm_spec.json
  roster.json
  graph.json
  policies/
    skill_policy.json
    plugin_policy.json
    identity_policy.json
    interrupt_policy.json
    memory_policy.json
    llm_policy.json
  evals/
    regression/
    analysis_plan.json
  sources/
    PROVENANCE.json
  docs/
    user_guide.md
```

`CASOPS_SWARMS_ROOT` (default `swarms/`) is the scan root, parallel to `CASOPS_AGENTS_ROOT`.

Generated artifacts (`resolved.json`, `conflicts.json`, compose locks) are **not** authoring files. If a generator writes them, they are host-owned. Hand edits that drift from member hashes fail `INH_RESOLVED_DRIFT`. Live agent compose-preview does not write locks; swarm compose-preview MUST match (`wrote_locks: false`).

## 6.2 Required vs optional

| Path | Required | Author |
|------|----------|--------|
| `README.md` | Yes | Human |
| `SWARM.md` | Yes | Human — mission and bounds; untrusted as executable instructions |
| `swarm_spec.json` | Yes | Human / generator |
| `roster.json` | Yes | Human |
| `graph.json` | Yes | Human |
| `policies/skill_policy.json` | Yes (deny/require may be empty) | Human |
| `policies/plugin_policy.json` | Yes | Human |
| `policies/identity_policy.json` | Yes | Human |
| `policies/interrupt_policy.json` | Yes | Human |
| `policies/memory_policy.json` | Yes | Human |
| `policies/llm_policy.json` | Yes | Human |
| `sources/PROVENANCE.json` | Yes | Generator + review |
| `evals/` | Optional but expected | Human |
| `docs/user_guide.md` | Optional; Help copies it | Human |

`SWARM.md` is provenance, like agent `SPEC.md`: never configuration, never a tool grant.

## 6.3 Locate

`locate_swarm_folder(swarms_root, swarm_id)`:

1. If `swarms_root / swarm_id / swarm_spec.json` exists, use that folder.  
2. Otherwise every child directory with `swarm_spec.json` is opened; the first whose JSON `swarm_id` equals the request id is used.  
3. If none, `INH_PARENT_MISSING` (same code the live plane uses for a missing agent).

## 6.4 Illegal contents

- Copies of member `agents/<folder>/` trees.  
- Provider API keys, Ed25519 host keys, `.env` fragments.  
- `production_activation_requested: true`.  
- `network_access: true` as a swarm-level grant.  
- A `chat.json` that claims to replace per-agent Chat.

<div role="img" aria-label="Self-contained common swarm v2 folder">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 720" role="img" aria-labelledby="swv2-fold-t swv2-fold-d">
  <title id="swv2-fold-t">Common swarm v2 folder</title>
  <desc id="swv2-fold-d">Swarm folder holds wiring. Member agents stay under agents/ and are located by agent_id.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .card{fill:#FFFFFF;stroke:#CBD5E1;stroke-width:1.5}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .m{fill:#334155;font:400 12px ui-monospace,Menlo,Consolas,monospace}
      .sec{fill:#64748B;font:700 10px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;letter-spacing:1.2px}
      .pu{fill:#EEF2FF;stroke:#A5B4FC;stroke-width:1.5}
      .am{fill:#FFFBEB;stroke:#FCD34D;stroke-width:1.5}
    </style>
  </defs>
  <rect class="bg" width="1440" height="720"/>
  <text class="ink" x="40" y="42">Common swarm v2 — self-contained folder</text>
  <text class="sub" x="40" y="66">structure_id casops.common_swarm.v2 · schema 3.0 · members located like live agents</text>
  <rect class="card" x="40" y="92" width="720" height="592" rx="16"/>
  <text class="sec" x="64" y="122">FOLDER  ·  swarms/&lt;folder&gt;/</text>
  <text class="m" x="64" y="156">swarm_spec.json     structure_id + budgets</text>
  <text class="m" x="64" y="184">roster.json         member agent_ids</text>
  <text class="m" x="64" y="212">graph.json          nodes, edges, entry</text>
  <text class="m" x="64" y="240">policies/*          deny/require only</text>
  <text class="m" x="64" y="268">SWARM.md            mission (untrusted exec)</text>
  <rect class="pu" x="64" y="300" width="672" height="120" rx="10"/>
  <text class="h" x="84" y="328">Generated at preview — not authoring</text>
  <text class="m" x="84" y="356">compose-preview → wrote_locks: false</text>
  <text class="m" x="84" y="380">member hashes from Composer.preview</text>
  <rect class="am" x="64" y="440" width="672" height="212" rx="10"/>
  <text class="h" x="84" y="468">Not in this folder</text>
  <text class="b" x="84" y="496">agent_spec.json, prompts, persona, memory,</text>
  <text class="b" x="84" y="520">plugins, corrigibility, LLM keys stay on the agent</text>
  <text class="b" x="84" y="544">or in process env / .env.</text>
  <text class="b" x="84" y="580">Copying agent trees into the swarm is illegal.</text>
  <rect class="card" x="784" y="92" width="616" height="592" rx="16"/>
  <text class="sec" x="808" y="122">UNIT OF IDENTITY</text>
  <text class="h" x="808" y="156">swarm_id in JSON, not necessarily folder name</text>
  <text class="m" x="808" y="184">example folder _template_v2</text>
  <text class="m" x="808" y="208">example swarm_id casops.template.swarm_safe</text>
  <text class="h" x="808" y="252">Member locate (live)</text>
  <text class="b" x="808" y="280">agents/&lt;id&gt;/agent_spec.json OR</text>
  <text class="b" x="808" y="304">first child whose agent_id matches</text>
  <text class="m" x="808" y="340">_template_v3 → casops.template.baseline_safe</text>
  <text class="h" x="808" y="392">Truth chain</text>
  <text class="b" x="808" y="420">swarm_spec.json → roster.json → graph.json</text>
  <text class="b" x="808" y="444">→ each member agent_spec.json (v3)</text>
  <text class="b" x="808" y="468">→ live GET /api/v3/agents/{id}/structure</text>
  <text class="b" x="808" y="508">Drift among those is a CI fail.</text>
</svg>
</div>

---

# 7. Membership — every node is a common-agent v3

A swarm member is legal iff all of:

1. `agent_id` is unique on the roster.  
2. `locate_agent_folder(agents_root, agent_id)` returns a folder.  
3. That folder contains `agent_spec.json`. `SPEC.md` is expected provenance; missing SPEC is a review fail, not a substitute for `agent_spec.json`.  
4. `agent_spec.json` declares `structure_id: "casops.common_agent.v3"` and `schema_version: "3.0"`.  
5. `production_activation_requested` is JSON boolean `false` unless a **separate** human gate already flipped that **agent**. The swarm cannot flip it (`GATE_ACTIVATION`).  
6. `model_policy.network_access` is `false` unless that same class of gate already flipped that **agent** (`GATE_NETWORK`).  
7. Swarm policy cannot add tools or plugins that the member did not declare.

Illegal: prompt-only roles, unnamed “crew”, folders that are not v3, agents from outside this host’s `CASOPS_AGENTS_ROOT`, treating a Workflow SVG label as a member without an `agent_id`.

## 7.1 Member surface the swarm relies on (live fields)

| Agent surface | Swarm effect |
|---|---|
| `agent_id` | Roster and graph key |
| `structure_id` / `schema_version` | Must be v3 / 3.0 |
| `role` | Display only |
| `va_category` | Org department. Empty/`none`/`null` → uncategorized. Swarm must not invent a new value |
| `allowed_tools` / `allowed_plugins` | Intersection with node lists |
| `model_policy` | Network AND-false; provider is host-resolved, not swarm-granted |
| `budget_policy` | Min with swarm execution_budget; `max_peer_hops` limits that agent’s critique bus |
| `critique_edges` | Declared I/O; swarm loop may union, not rewrite SPEC |
| `max_refinement_count` | Min with swarm `critique.max_iterations` |
| `production_activation_requested` | Swarm cannot set true |
| `does_not_own` | Union still applies; swarm cannot take exclusive craft |
| `prompt_reference` / `rubric_reference` | Used by member Chat/run; swarm does not replace them |
| `memory/policy.json` `mode` | `none` → writes forbidden |
| `runtime/cache.json` | T3 stays off unless host verifier already enabled it on that agent |
| `corrigibility/invariants.json` | Host-owned attestation; swarm cannot rewrite |
| `inheritance/` | Resolved **per member** before the node runs; MRO is not a swarm mixin |

## 7.2 Functional requirements

| ID | Requirement |
|----|-------------|
| FR-MEM-001 | Every `graph.json` node `agent_id` MUST appear on `roster.json`. |
| FR-MEM-002 | Every roster `agent_id` MUST pass §7 membership. Missing folder → `INH_PARENT_MISSING`. Wrong family → `INH_STRUCTURE_MISMATCH`. |
| FR-MEM-003 | `owner_agent_id` MUST be on the roster (`SWM_OWNER_ABSENT` if not). |
| FR-MEM-004 | Duplicate `agent_id` on the roster fails closed (`SWM_ROSTER_DUP`). |
| FR-MEM-005 | A graph node MAY reuse the same `agent_id` on distinct node ids (same agent, two steps). |
| FR-MEM-006 | Standby roster members are allowed; they do not run unless a node names them. |
| FR-MEM-007 | Cross-pack members (`video.*` with `specials.*`) are allowed only if both locate on this host as v3. |
| FR-MEM-008 | Template member `casops.template.baseline_safe` is a legal member. Its folder name `_template_v3` MUST NOT be required as the roster string. |

---

# 8. Roster and organization

## 8.1 `roster.json`

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_swarm.v2",
  "swarm_id": "video.spine",
  "owner_agent_id": "video.orchestrator",
  "members": [
    {
      "agent_id": "video.orchestrator",
      "org_role": "top",
      "department": "9-Meta"
    },
    {
      "agent_id": "video.planner",
      "org_role": "top",
      "department": "9-Meta"
    },
    {
      "agent_id": "video.screenwriter",
      "org_role": "member",
      "department": "1-ATL"
    },
    {
      "agent_id": "video.judge",
      "org_role": "member",
      "department": "9-Meta"
    }
  ]
}
```

Rules:

- `department` MUST be equal to that member’s live `va_category`, or omitted/`""` when the member has no category. **Do not invent** `"above_the_line"` or `"1-Narrative"` if the live field is `"1-ATL"`.  
- `org_role` is `top` | `member`. Tops are pipeline owners (typically orchestrator, then planner) when those agents exist.  
- Organization view in the UI is still pack → category → agent. Roster `department` is a pin, not a second taxonomy.  
- A department string is never runnable.

## 8.2 Live Org Chat algorithm (normative until a swarm is selected)

`ui/src/lib/orgChart.ts` `buildOrgChart`:

1. Filter agents by `agentPack(agent_id)` (`specials` / `video` / `other`).  
2. Bucket by `va_category` trimmed, or `"uncategorized"`.  
3. Root node = Agent Group. Category nodes only if more than one category. Leaves are agents.  
4. Click leaf → `/agents/{id}` (Overview), not Chat, not a swarm run.

After swarm routes exist, Org Chat MAY take a `swarm_id` query and filter to the roster. It remains read-only.

---

# 9. Graph, DNA, and patterns

## 9.1 Execution graph (`graph.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_swarm.v2",
  "definition_type": "pack_graph",
  "id": "video.spine",
  "engine": "casops.runtime",
  "pattern": "pack_spine",
  "entry_node": "orchestrate",
  "terminal_node_ids": ["package"],
  "nodes": [
    {
      "id": "orchestrate",
      "agent_id": "video.orchestrator",
      "tool_ids": [],
      "plugin_ids": [],
      "memory_reads": [],
      "memory_writes": []
    },
    {
      "id": "plan",
      "agent_id": "video.planner",
      "tool_ids": [],
      "plugin_ids": [],
      "memory_reads": [],
      "memory_writes": []
    },
    {
      "id": "write",
      "agent_id": "video.screenwriter",
      "tool_ids": [],
      "plugin_ids": [],
      "memory_reads": [],
      "memory_writes": []
    },
    {
      "id": "qc",
      "agent_id": "video.aiqaconsistency",
      "tool_ids": [],
      "plugin_ids": [],
      "memory_reads": [],
      "memory_writes": []
    },
    {
      "id": "package",
      "agent_id": "video.gatekeeper",
      "tool_ids": [],
      "plugin_ids": [],
      "memory_reads": [],
      "memory_writes": []
    }
  ],
  "edges": [
    { "from": "orchestrate", "to": "plan", "max_traversals": 1 },
    { "from": "plan", "to": "write", "max_traversals": 1 },
    { "from": "write", "to": "qc", "max_traversals": 1 },
    { "from": "qc", "to": "package", "max_traversals": 1 }
  ]
}
```

`engine` MUST be `casops.runtime`. Values `graph`, `langgraph`, `a2a` fail closed (`SWM_PATTERN_UNKNOWN` / `CMP_PROTOCOL_VERSION`).

Legal `pattern` values: `pipeline` | `supervisor` | `router` | `critique` | `map_reduce` | `pack_spine`. Unknown → `SWM_PATTERN_UNKNOWN`.

Linear DNA is the same nodes without explicit edges: host compiles steps in order into a pipeline graph.

Caps: 1–100 nodes; edge `max_traversals` 1–10. A graph that lists all 114 `video.*` agents as nodes is legal only if budgets still close; the worked spine is a **subset**.

Each node run, when the swarm runner exists, invokes that member’s existing `Runtime.execute` (live DAG typically a single `kind: "model"` node in `runtime/execution.json`). The swarm graph is the **outer** walk. The member DAG is the **inner** walk. Inner `PERF_PLAN_CYCLE` aborts the outer node.

## 9.2 Workflow SVG (live picture, not the runner)

Live files:

- Main: `ui/public/svg/video.workflow.svg`  
- Sub templates: `video.template.a.workflow.svg` … `video.template.j.workflow.svg`  
- Sub scales: `video.scale.s1.workflow.svg` … `video.scale.s7.workflow.svg`  

Normative click contract (already implemented): `a.agent-link` `href` of the form `/agents/{agent_id}/chat`. Unknown ids in an SVG are a generator defect (`scripts/generate_video_workflows.py` validates against declared agents).

v2 requirement: when `graph.json` exists for `video.spine`, CI SHOULD fail if a node `agent_id` is not clickable in the main video SVG **or** an explicit waiver lists the node as spine-only (not drawn). The SVG remains a picture. Clicking it MUST NOT start a swarm run.

## 9.3 Functional requirements

| ID | Requirement |
|----|-------------|
| FR-GRF-001 | `entry_node` MUST exist in `nodes`. |
| FR-GRF-002 | Every `terminal_node_ids` entry MUST exist in `nodes`. |
| FR-GRF-003 | Every edge `from`/`to` MUST be a node id (`SWM_GRAPH_EDGE`). |
| FR-GRF-004 | Unbounded cycles fail closed (`PERF_PLAN_CYCLE`). A cycle is legal only if every participating edge has `max_traversals` and swarm `max_node_visits` cannot be exceeded. |
| FR-GRF-005 | Node `tool_ids` not in member `allowed_tools` ∩ host register fail `SKL_TOOL_LEAK`. |
| FR-GRF-006 | Node `plugin_ids` not in member `allowed_plugins` fail `PLG_PERMISSION`. Public plane still MUST NOT execute plugins. |
| FR-GRF-007 | Memory write ids on a node whose member `memory.policy.mode` is `none` fail `MEM_TRUST_TIER` at preview, not at some later surprise. |
| FR-GRF-008 | `engine` is `casops.runtime` only. |
| FR-GRF-009 | Parallel `map_reduce` default `partial_ok: false`. Unsafe side-effect fan-out → `PERF_UNSAFE_PARALLELISM`. |

---

# 10. Critique bus, I/O, and handoffs

## 10.1 Two live facts, one specified bus

| Surface | Live today | Swarm v2 |
|---|---|---|
| `critique_edges.inputs/outputs` | Declared I/O on `agent_spec.json`; Chat IoPanel; structure `io` | Unioned into the swarm I/O snapshot; swarm cannot rewrite the agent file |
| Org Chat | Read-only org chart | Not the critique bus |
| Chat POST | Operator free text to **one** agent | Not a swarm-wide chat |
| Swarm critique loop | **Not implemented** | Specified below |

## 10.2 Critique message (normative fields)

`critique_id`, `sender`, `receiver`, `artifact_reference`, `severity` (`blocker`\|`major`\|`minor`\|`nit`), `category`, `evidence[]`, `suggested_action`, `rubric.reference`, `rubric.score` (0–1), `deadline_or_phase`, `timestamp`.

Sender and receiver MUST be running member `agent_id`s. Parent mixin ids are illegal. HTTP actor remains `host_service` or `human_operator`; the wire actor is never `peer_agent`.

## 10.3 Swarm critique loop

```json
{
  "enabled": true,
  "max_iterations": 3,
  "lead_agent_id": "video.critic",
  "judge_agent_id": "video.judge"
}
```

Lead and judge MUST be roster members. If `enabled` is false, member `critique_edges` still exist as I/O declarations but the swarm does not iterate.

`max_iterations` = min(swarm value, each running member `max_refinement_count`, 3). Live pack agents in the §20 spine all have `max_refinement_count: 0` — then the loop does **not** run, even if swarm JSON says 3. A loop of 1–3 is only legal when every running member’s count is at least that high.

## 10.4 Handoffs

Handoff artifacts are immutable versions with `parent_assets` forming an acyclic DAG. A member must not own another member’s exclusive craft without this handoff (`does_not_own` union still applies). Copy-on-write. No silent clobber.

Cross-agent escalation that looks like a hijack → `SAF_CASCADE` (halt exchange graph, containment).

---

# 11. Skill, plugin, identity, memory, and LLM policy

The swarm **constrains** member compose. It does not author member skills, plugins, personas, memory documents, or `.env` keys.

## 11.1 Skill policy

```json
{
  "deny": [],
  "require": [],
  "allow_member_toggles": true
}
```

| Rule | Effect |
|------|--------|
| deny `skill_id` | OFF for every running member, even if the agent declared it ON |
| require `skill_id` | Load fails unless every **running** node’s agent has that skill declared (not invented) and enabled (`SWM_SKILL_REQUIRE` or `SKL_MISSING_FILES`) |
| allow_member_toggles | Operator may still mutate the **agent** toggle through agent routes; swarm deny still wins |

Swarm cannot enable an undeclared skill (`SKL_TOGGLE_UNKNOWN`).

## 11.2 Plugin policy

```json
{
  "deny": [],
  "require": [],
  "allow_execute": false
}
```

`allow_execute` MUST be false on the public plane. Validate-without-exec only (`executed: false`). Unsigned/third-party cannot run below I2; network requires I3 — swarm JSON cannot downgrade isolation (`PLG_ISOLATION_TIER`).

## 11.3 Identity policy

```json
{
  "default_expertise_mode": "grounded",
  "allow_persona_overlay": true,
  "require_disclosure": true,
  "forbid_named_persons": true
}
```

If any running member is not `grounded`, the swarm run banner lists those `agent_id`s and disclosure ids. Missing disclosure → `IDN_DISCLOSURE_MISSING`. Named-person overlay without approval → `IDN_NAMED_PERSON`. License claims → `IDN_LICENSE_CLAIM`. Swarm cannot set a member persona.

## 11.4 Memory policy

```json
{
  "allow_member_writes": false,
  "allow_consolidate_drain": false
}
```

If `allow_member_writes` is false, node `memory_writes` must be empty. If a member’s own mode is `none`, writes fail `MEM_TRUST_TIER` even if the swarm accidentally says true — **member policy wins toward deny**. Consolidate on the serving path only enqueues. Drain remains consolidation-worker only.

Cross-tenant query stays empty list, not a leak. Wrong tenant delete → `MEM_SCOPE`.

## 11.5 LLM policy

```json
{
  "allow_member_override": true,
  "forbid_network_grant": true,
  "default_provider": "__host__"
}
```

Host catalog: `local_deterministic`, `openai`, `xai`, `anthropic`. Aliases `grok` / `x-ai` → `xai`. Keys stay in process env / `.env`. Swarm files MUST NOT contain keys.

`default_provider: "__host__"` means `LlmSettings.resolved_for(agent_id)`. Swarm cannot set `network_access` true by selecting `openai` / `xai` / `anthropic`. Picking a cloud provider while `forbid_network_grant` is true and the member’s `network_access` is false is a preview finding, not a silent grant (`GATE_NETWORK` if a route would call out).

`agent_runtime` cannot POST LLM settings (`IMP_SELF_APPROVAL`).

---

# 12. Budgets, risk gates, interrupts, rollback, corrigibility

## 12.1 Execution budget

Merge is **min** with each running member `budget_policy` where the units match.

| Field | Range | Merge |
|-------|-------|-------|
| `max_node_visits` | 1–100 | min(swarm, implied) |
| `max_handoffs` | 0–12 | min |
| `max_wall_clock_seconds` | 1–900 | min with members’ `max_job_ms / 1000` |
| `max_tool_requests` | 0–50 | min with each member `budget_policy.max_tool_requests` |
| `max_model_calls` | 0–50 | min with each member |
| `max_peer_hops` | 0–8 | min with each member `max_peer_hops` (critique bus, not graph handoffs) |

Live template: `max_tool_requests: 0`, `max_model_calls: 2`, `max_job_ms: 15000`, `max_peer_hops: 0`.

Breach → `PERF_BUDGET_EXCEEDED` or `PERF_DEADLINE`. No silent continue.

## 12.2 Risk gates

`risk_gate_ids` min 1. Unknown id → `SWM_GATE_UNKNOWN`. Gates run at entry and before terminal nodes. Asserted-unverified capabilities cannot bind (`CMP_ASSERTED_UNVERIFIED`).

## 12.3 Human interrupts

```json
{
  "required": true,
  "gates": [
    { "id": "release_or_irreversible", "when": "irreversible_or_publish", "required": true }
  ],
  "approval_authority": "independent_approver"
}
```

v1 said `host_gated`. v2 names the live actor: irreversible/publish MUST interrupt; approval is `independent_approver`. Auto-approve by `agent_runtime` or `human_operator` → `IMP_SELF_APPROVAL`. Missing interrupt → `SWM_HITL_REQUIRED`.

## 12.4 Rollback

`rollback.plan_id` plus `compensation_step_ids` that MUST be node ids on this graph. Compensation runs only on abort after a successful prefix. Compensation cannot enable extra tools or plugins. Missing/untested rollback on a mutating pattern → `IMP_ROLLBACK`.

## 12.5 Corrigibility

Host attestation remains `GET /api/v3/agents/{id}/corrigibility/attestation` (`status: host_reference`). Swarm preview MUST attest each running member before walking. Tamper or swarm JSON that tries to rewrite invariants → `IMP_CORRIGIBILITY`, containment stop, HTTP 503.

---

# 13. Data models

## 13.1 `swarm_spec.json`

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_swarm.v2",
  "swarm_id": "video.spine",
  "status": "registered",
  "owner_agent_id": "video.orchestrator",
  "authorization_id": "video.local-spine",
  "engine": "casops.runtime",
  "pattern": "pack_spine",
  "execution_budget": {
    "max_node_visits": 8,
    "max_handoffs": 7,
    "max_wall_clock_seconds": 60,
    "max_tool_requests": 0,
    "max_model_calls": 8,
    "max_peer_hops": 0
  },
  "memory": { "reads": [], "writes": [] },
  "risk_gate_ids": ["video.local-safe"],
  "rollback": {
    "plan_id": "video.spine.rollback",
    "compensation_step_ids": ["package"]
  },
  "critique": {
    "enabled": true,
    "max_iterations": 3,
    "lead_agent_id": "video.critic",
    "judge_agent_id": "video.judge"
  },
  "production_activation_requested": false,
  "t3_requested": false,
  "network_requested": false,
  "roster_ref": "roster.json",
  "graph_ref": "graph.json",
  "does_not_own": [
    "Host credential storage",
    "Silent production activation",
    "Member SPEC rewrite",
    "Plugin execution on the public plane",
    "T3 enablement",
    "Corrigibility invariants",
    "A second control plane"
  ]
}
```

Catalog `status` is `draft` | `registered`. Production active is out of band and **not** this field going true from the Control UI.

## 13.2 JSON Schema (normative)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://casops.local/schemas/swarm/swarm_spec.schema.json",
  "title": "swarm_spec",
  "type": "object",
  "additionalProperties": true,
  "required": [
    "schema_version",
    "structure_id",
    "swarm_id",
    "status",
    "owner_agent_id",
    "engine",
    "pattern",
    "execution_budget",
    "production_activation_requested",
    "roster_ref",
    "graph_ref",
    "does_not_own"
  ],
  "properties": {
    "schema_version": { "type": "string", "const": "3.0" },
    "structure_id": { "type": "string", "const": "casops.common_swarm.v2" },
    "swarm_id": { "type": "string", "minLength": 1 },
    "status": { "type": "string" },
    "owner_agent_id": { "type": "string", "minLength": 1 },
    "engine": { "type": "string", "const": "casops.runtime" },
    "pattern": {
      "type": "string",
      "enum": ["pipeline", "supervisor", "router", "critique", "map_reduce", "pack_spine"]
    },
    "production_activation_requested": { "type": "boolean", "const": false },
    "t3_requested": { "type": "boolean" },
    "network_requested": { "type": "boolean" },
    "roster_ref": { "type": "string" },
    "graph_ref": { "type": "string" },
    "does_not_own": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    }
  }
}
```

`production_activation_requested` const `false` is intentional: this schema is the `baseline_safe` swarm profile. A later profile that allows the field to be true still cannot flip it from the Control UI.

When implemented, this schema lives at `schemas/swarm/swarm_spec.schema.json` (file not in this checkout yet).

## 13.3 Run artifact extras

| Field | Notes |
|-------|--------|
| `swarm_id` | Public id |
| `root_trace_id` | One outer id, prefix `tr_`, wrapping member runs |
| `node_trace` | Ordered node ids + visit counts + inner `root_trace_id`s |
| `mro_by_agent` | Each member’s compose MRO |
| `compose_hash_by_agent` | 64 hex from member preview |
| `wrote_locks` | JSON boolean `false` on preview |
| `skills_loaded_by_agent` | After swarm deny |
| `expertise_modes` | Per running agent |
| `disclosure_ids` | If any overlay |
| `budget_remaining` | Snapshot at end or abort |
| `memory_writes` | Must be `[]` on `baseline_safe` |
| `plugins_executed` | Must be `false` |
| `t3_enabled` | Must be `false` unless host already enabled T3 on that member |
| `adapter` | Inner adapter (`local_deterministic` unless host LLM router ran a model node) |
| `containment_stop` | Null or code |
| `validation` | Must not be styled as pass when `NOT_RUN` / `INDICATIVE` |

There is **no** `status` field on live `RunResult`. Swarm artifacts MUST NOT invent a green `status: "success"` that the member run does not have.

## 13.4 List summary (parallel to agent summaries)

`GET /api/v3/swarms` item:

```json
{
  "swarm_id": "video.spine",
  "folder": "C:\\Project\\common-agent-structure\\swarms\\video.spine",
  "structure_id": "casops.common_swarm.v2",
  "schema_version": "3.0",
  "owner_agent_id": "video.orchestrator",
  "member_count": 9,
  "pattern": "pack_spine"
}
```

---

# 14. Runtime behaviour

Specified order. Not live as a single route. Each step uses live primitives where they exist.

<div role="img" aria-label="Swarm run lifecycle v2">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 420" role="img" aria-labelledby="swv2-life-t swv2-life-d">
  <title id="swv2-life-t">Swarm run lifecycle v2</title>
  <desc id="swv2-life-d">Load swarm, locate members, compose-preview each, apply constraints, walk graph via Runtime.execute, critique, HITL, package or abort.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 11px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .st{fill:#4F46E5}
    </style>
    <marker id="swv2-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#64748B"/>
    </marker>
  </defs>
  <rect class="bg" width="1440" height="420"/>
  <text class="ink" x="40" y="42">Run — fail-closed order (specified)</text>
  <text class="sub" x="40" y="66">Uses live locate, compose-preview, Runtime.execute, attestation. Outer walk is not implemented yet.</text>
  <rect class="st" x="40" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="56" y="130">1  Load swarm</text>
  <text class="h2" x="56" y="150">spec + roster + graph</text>
  <rect class="st" x="280" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="296" y="130">2  Locate + attest</text>
  <text class="h2" x="296" y="150">v3 + host_reference</text>
  <rect class="st" x="520" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="536" y="130">3  Compose-preview</text>
  <text class="h2" x="536" y="150">wrote_locks false</text>
  <rect class="st" x="760" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="776" y="130">4  Constrain</text>
  <text class="h2" x="776" y="150">skill · plugin · mem</text>
  <rect class="st" x="1000" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="1016" y="130">5  Walk + inner run</text>
  <text class="h2" x="1016" y="150">Runtime.execute</text>
  <rect class="st" x="1240" y="100" width="160" height="70" rx="10"/>
  <text class="h2" x="1256" y="130">6  HITL</text>
  <text class="h2" x="1256" y="150">package / abort</text>
  <line x1="240" y1="135" x2="280" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#swv2-arr)"/>
  <line x1="480" y1="135" x2="520" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#swv2-arr)"/>
  <line x1="720" y1="135" x2="760" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#swv2-arr)"/>
  <line x1="960" y1="135" x2="1000" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#swv2-arr)"/>
  <line x1="1200" y1="135" x2="1240" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#swv2-arr)"/>
  <text class="sub" x="40" y="220">Step 2: locate_agent_folder + GET attestation. Missing member is INH_PARENT_MISSING, not a new mystery code.</text>
  <text class="sub" x="40" y="248">Step 3: Composer.preview per member. Check wrote_locks is false. Hash length 64.</text>
  <text class="sub" x="40" y="276">Step 4: deny wins. Empty tool allow-list stays empty. Memory mode none blocks writes.</text>
  <text class="sub" x="40" y="304">Step 5: outer graph walk; inner DAG from that member runtime/execution.json. Dry-run still executes in-process.</text>
  <text class="sub" x="40" y="332">Step 6: independent_approver for irreversible/publish. Compensation nodes only on abort. No extra tools.</text>
  <text class="sub" x="40" y="372">Parallel map_reduce: one budget; fail closed if any shard fails unless pattern declares partial_ok (default false).</text>
</svg>
</div>

Dry-run honesty (D-SWM-15): `x-casops-dry-run: true` still runs inner DAGs in HostState. It does not write compose locks, does not drain consolidation, does not persist `var/llm-settings.json` if LLM POST is dry, and does not execute plugins. Operators MUST NOT read “dry-run” as “zero in-process effects.”

---

# 15. Operator and host APIs (`/api/v3`)

Companion paths. Same mutation contract as live agent routes. Not A2A. Not a UI-private backend. **Not implemented in this checkout** — this table is the contract to implement later.

| Method | Path | Mutation? | Purpose |
|---|---|---|---|
| GET | `/api/v3/swarms` | no | List summaries from `CASOPS_SWARMS_ROOT` |
| GET | `/api/v3/swarms/{swarm_id}/structure` | no | Folder, schema, roster counts, I/O union |
| GET | `/api/v3/swarms/{swarm_id}/resolved` | no | Members, hashes, composed skill sets, expertise modes, `io.merged: true` |
| GET | `/api/v3/swarms/{swarm_id}/roster` | no | Organization view |
| GET | `/api/v3/swarms/{swarm_id}/graph` | no | Nodes, edges, entry, terminals |
| POST | `/api/v3/swarms/{swarm_id}/compose-preview` | yes | Per-member preview; `wrote_locks: false` |
| POST | `/api/v3/swarms/{swarm_id}/runtime/run` | yes | Outer walk; inner `Runtime.execute` |
| GET | `/api/v3/swarms/{swarm_id}/runtime/plan` | no | Compiled outer plan JSON |
| GET | `/api/v3/traces/{trace_id}` | no | **Existing** member/swarm trace |
| POST | `/api/v3/traces/{trace_id}/replay` | yes | **Existing**; no memory writes |
| GET | `/api/v3/agents/{agent_id}/structure` | no | **Existing** member inspect |

Forbidden as swarm routes:

- `PUT /api/v1/swarms/...` (v1).  
- Any path not under `/api/v3`.  
- A swarm Chat that skips per-agent `runtime/chat`.  
- A route that sets `production_activation_requested` true.  
- A route that sets `executed: true` on plugins.

Member skill/identity/LLM edits stay on **agent** routes. Swarm deny still applies at compose.

### 15.1 Compose-preview response shape

```json
{
  "swarm_id": "video.spine",
  "compose_hash": "64-lowercase-hex-of-canonical-member-hashes",
  "wrote_locks": false,
  "errors": [],
  "findings": [],
  "members": [
    {
      "agent_id": "video.orchestrator",
      "folder": "...",
      "compose_hash": "64 hex",
      "mro": [],
      "wrote_locks": false
    }
  ]
}
```

### 15.2 PowerShell sample (specified; will 404 until implemented)

```powershell
$base = "http://127.0.0.1:18080"
$swarm = "video.spine"
$H = @{
  "x-casops-actor"           = "host_service"
  "x-casops-reason"          = "swarm-preview"
  "x-casops-expected-parent" = "none"
  "x-casops-dry-run"         = "true"
}
Invoke-RestMethod "$base/api/v3/swarms"
Invoke-RestMethod "$base/api/v3/swarms/$swarm/structure"
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/swarms/$swarm/compose-preview"
```

Until those routes exist, the operator walk is the **member** walk already documented for `/api/v3/agents/{id}/compose-preview` and `/runtime/run`.

### 15.3 OpenAPI

When implemented, `app.openapi` MUST still filter to paths starting with `/api/v3`. Swarm paths are legal because they start with that prefix. `/health` and `/debug/*` stay excluded.

---

# 16. Control UI mapping

Live `ui/src/App.tsx` routes and `ui/src/shell/nav.ts` labels.

| Live route | Live label | Swarm v2 role | Implement later? |
|---|---|---|---|
| `/` | Agent Swarm | Member pool (`GET /api/v3/agents`) | Optional swarm filter chip when `GET /api/v3/swarms` exists |
| `/org-chat` | Agent Org Chat | Organization map; read-only | Optional `?swarm=` filter |
| `/workflow` | Agent Workflow / Main Workflow | Graph **picture** for pack `video` | Optional bind to `graph.json` |
| `/workflow/sub` | Sub Workflow | Pattern variants Template A–J, Scale S1–S7 | Stay pictures |
| `/agents/:agentId` | Agent Profile / Overview | Member contract, attestation, LLM | Unchanged |
| `/agents/:agentId/chat` | Chat | Per-member free text | Unchanged; not swarm chat |
| `/agents/:agentId/compose` | Compose | Member compose-preview | Unchanged |
| `/agents/:agentId/run` | Run | Member `Runtime.execute` | Unchanged |
| `/settings` | Settings | Host LLM, actor defaults | No swarm secrets |
| `/help` | Help | Generic docs under `ui/public/docs` | Add `/docs/swarms/{id}/spec.md` when folders exist |
| `/swarms/:swarmId` | — | **Not in App.tsx** | Add only after HTTP exists |

UI mutation injection stays `ui/src/api/v3.ts`: GET without headers; mutating calls add the four headers; Chat `reasonFallback: "operator chat"`.

Help resolver (live): exact route → `/docs/agents/<agentId>/<tab>.md` → param-stripped. Swarm Help would be `/docs/swarms/<swarmId>/spec.md` and `userguide.md`, generated from `SWARM.md` + `swarm_spec.json` + `docs/`, same pattern as `tools/generate_help_agent_docs.py`.

Theme, logs drawer, chat JSONL under `logs/chat/<agent_id>/` remain member-scoped.

**Forbidden UI:** a “go live” button, a T3 switch, a plugin execute button, treating Org Chat as Chat, treating Workflow click as swarm run, inventing category chips.

---

# 17. Honesty, safety, and fail-closed rules

- Swarm JSON cannot grant tools, plugins, network, T3, or production activation.  
- Vendor tool names on nodes are design-time; runtime allow-list is intersection; empty stays empty.  
- Persona overlays remain fictional by default; named-person and license claims abort the member compose, which aborts the swarm.  
- Disabled skills stay absent from every member envelope.  
- Critique is in-host JSON, not A2A, not Org Chat, not operator Chat.  
- Compensation cannot widen tools or plugins.  
- Specials join only as v3 folders — and in this checkout they already are.  
- Dry-run still executes inner DAGs in-process.  
- `NOT_RUN` / `INDICATIVE` are not a green pass.  
- Unknown actor header → `IMP_CORRIGIBILITY` (live `actor_from_header`).  
- Containment stop on invariant tamper.  
- No second public plane. No browser to `8081`–`8087`.  
- Do not hard-code live 135 as a magic test assertion that must never change; assert “every `agent_spec.json` folder is listed.”

---

# 18. Error catalogue

## 18.1 Prefer live codes

Live catalogue: `errors/catalogue.json`, `schema_version: "3.0"`, 93 codes, twelve fields: `code`, `category`, `severity`, `retryability`, `default_action`, `containment_required`, `incident_required`, `operator_message`, `external_message`, `http_mapping`, `telemetry_event`, `test_fixture`.

External HTTP `message` is always `external_message` (“The request was rejected by host policy.”) except the unsigned middleware path, which uses the operator string `mutation requires actor, reason, expected parent version, dry-run`.

| Swarm condition | Live code | HTTP |
|---|---|---|
| Member folder missing | `INH_PARENT_MISSING` | 409 |
| Member not v3 | `INH_STRUCTURE_MISMATCH` | 409 |
| Unbounded graph cycle | `PERF_PLAN_CYCLE` | 409 |
| Node tool not allowed | `SKL_TOOL_LEAK` | 409 |
| Budget infeasible | `PERF_BUDGET_EXCEEDED` | 409 |
| Wall clock | `PERF_DEADLINE` | 504 |
| Unsafe fan-out | `PERF_UNSAFE_PARALLELISM` | 409 |
| Generated resolved drift | `INH_RESOLVED_DRIFT` | 409 |
| Overlay without disclosure | `IDN_DISCLOSURE_MISSING` | 409 |
| Named person | `IDN_NAMED_PERSON` | 409 |
| License claim | `IDN_LICENSE_CLAIM` | 409 |
| Unsigned mutation | `IMP_UNSIGNED` | 409 |
| Agent approves / writes invariants / LLM | `IMP_SELF_APPROVAL` | 409 or 503 on middleware approve/corrigibility |
| Production activation | `GATE_ACTIVATION` | 409 |
| Network grant | `GATE_NETWORK` | 409 |
| Memory write on mode none | `MEM_TRUST_TIER` | 409 |
| Tenant mismatch | `MEM_SCOPE` | 409 |
| Plugin exec / undeclared | `PLG_PERMISSION` | 403 |
| Isolation too weak | `PLG_ISOLATION_TIER` | 400 |
| Invariant tamper | `IMP_CORRIGIBILITY` | 503 |
| Cross-agent escalation | `SAF_CASCADE` | 503 |
| Unverified capability bind | `CMP_ASSERTED_UNVERIFIED` | 409 |
| Unknown LLM provider | `PERF_ROUTE_UNAVAILABLE` | 409 |
| Rollback missing | `IMP_ROLLBACK` | 403 |
| Chat empty / too long | `CTX_BUDGET` | 400 |

v1 names `SWM_MEMBER_MISSING`, `SWM_NOT_COMMON_AGENT`, `SWM_CYCLE`, `SWM_TOOL_LEAK`, `SWM_BUDGET`, `SWM_RESOLVED_DRIFT`, `SWM_DISCLOSURE` **MUST NOT** be returned by the live host unless the catalogue is amended. Implementers map them as above.

## 18.2 Proposed swarm-specific codes (not in live catalogue)

These MAY be added in a catalogue amendment. Until then, implementation MUST use the mapped live code or fail closed with `INH_STRUCTURE_MISMATCH`.

| code | category | severity | retryability | default_action | containment | incident | http | telemetry_event | test_fixture | operator_message | external_message |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SWM_ROSTER_DUP` | swarm | high | never | Abort | false | false | 409 | `casops.error.swm_roster_dup` | `tests/contract/errors/test_swm_roster_dup.py` | Duplicate member id on roster. Default action: Abort. | The request was rejected by host policy. |
| `SWM_OWNER_ABSENT` | swarm | high | never | Abort | false | false | 409 | `casops.error.swm_owner_absent` | `tests/contract/errors/test_swm_owner_absent.py` | Owner not on roster. Default action: Abort. | The request was rejected by host policy. |
| `SWM_GRAPH_EDGE` | swarm | high | never | Abort | false | false | 409 | `casops.error.swm_graph_edge` | `tests/contract/errors/test_swm_graph_edge.py` | Edge endpoint is not a node. Default action: Abort. | The request was rejected by host policy. |
| `SWM_GATE_UNKNOWN` | swarm | high | never | Abort | false | false | 409 | `casops.error.swm_gate_unknown` | `tests/contract/errors/test_swm_gate_unknown.py` | Unknown risk_gate_id. Default action: Abort. | The request was rejected by host policy. |
| `SWM_SKILL_REQUIRE` | swarm | high | never | Abort | false | false | 409 | `casops.error.swm_skill_require` | `tests/contract/errors/test_swm_skill_require.py` | Required skill not declared on a running member. Default action: Abort. | The request was rejected by host policy. |
| `SWM_HITL_REQUIRED` | swarm | high | never | Abort | false | true | 409 | `casops.error.swm_hitl_required` | `tests/contract/errors/test_swm_hitl_required.py` | Irreversible step without independent_approver interrupt. Default action: Abort. | The request was rejected by host policy. |
| `SWM_PATTERN_UNKNOWN` | swarm | high | never | Abort | false | false | 409 | `casops.error.swm_pattern_unknown` | `tests/contract/errors/test_swm_pattern_unknown.py` | Unknown pattern or engine. Default action: Abort. | The request was rejected by host policy. |

Member compose errors (`INH_*`, `SKL_*`, `IDN_*`, `GATE_*`, `MEM_*`, `PLG_*`, `PERF_*`) abort the swarm with the member `agent_id` attached in operator logs, not in the external message.

---

# 19. Acceptance criteria

| ID | Criterion | Proof |
|----|-----------|-------|
| AC-SWM-001 | Required swarm files exist on a template folder | directory check |
| AC-SWM-002 | Node with unknown `agent_id` aborts `INH_PARENT_MISSING` | fixture |
| AC-SWM-003 | Non-v3 folder on roster aborts `INH_STRUCTURE_MISMATCH` | fixture |
| AC-SWM-004 | Owner missing from roster aborts `SWM_OWNER_ABSENT` (or mapped 409) | fixture |
| AC-SWM-005 | Unbounded cycle aborts `PERF_PLAN_CYCLE`; bounded `max_traversals` walks then stops | fixture |
| AC-SWM-006 | Node vendor tool not in member allow-list aborts `SKL_TOOL_LEAK` | preview |
| AC-SWM-007 | Swarm deny turns member skill OFF in compose-preview | preview |
| AC-SWM-008 | Overlay member without disclosure aborts `IDN_DISCLOSURE_MISSING` | fixture |
| AC-SWM-009 | Unsigned POST aborts `IMP_UNSIGNED` | HTTP |
| AC-SWM-010 | Irreversible terminal without HITL aborts `SWM_HITL_REQUIRED` | fixture |
| AC-SWM-011 | Budget min(swarm, members) enforced | fixture |
| AC-SWM-012 | `production_activation_requested` remains false through load | spec inspect |
| AC-SWM-013 | compose-preview `wrote_locks` is JSON boolean `false` | preview |
| AC-SWM-014 | `agent_runtime` cannot approve or write swarm invariants | HTTP |
| AC-SWM-015 | Memory write on template member aborts `MEM_TRUST_TIER` | preview |
| AC-SWM-016 | Plugins remain `executed: false` | preview |
| AC-SWM-017 | T3 remains off | preview |
| AC-SWM-018 | Roster `department` that is not the member’s live `va_category` fails closed | fixture |
| AC-SWM-019 | Locate template by id `casops.template.baseline_safe` not folder `_template_v3` | fixture |
| AC-SWM-020 | OpenAPI paths for swarms start with `/api/v3` | schema |
| AC-SWM-021 | Workflow SVG click still opens Chat, does not POST swarm run | UI |
| AC-SWM-022 | Org Chat remains read-only | UI |
| AC-SWM-023 | Validation `NOT_RUN` is not styled as pass | UI honesty |
| AC-SWM-024 | v1 `/api/v1/swarms` is not registered | OpenAPI |

Until `/api/v3/swarms` exists, AC-SWM-002–020 are **specified tests**, not a claim that they already pass. AC-SWM-021–023 are live UI contracts and MUST already hold.

---

# 20. Worked example (`video.spine`)

**Swarm id:** `video.spine` (specified; folder not in this checkout)  
**Owner:** `video.orchestrator` (live agent)  
**Members (all live in this checkout):**

| agent_id | Live `role` | Live `va_category` | Live `max_refinement_count` |
|---|---|---|---|
| `video.orchestrator` | OrchestratorAgent (VA Domain Pack) | `9-Meta` | 0 |
| `video.planner` | PlannerAgent (VA Domain Pack) | `9-Meta` | 0 |
| `video.creativedirector` | CreativeDirectorAgent (VA Domain Pack) | `6-Dist` | 0 |
| `video.screenwriter` | ScreenwriterAgent (VA Domain Pack) | `1-ATL` | 0 |
| `video.webresearch` | WebResearchAgent (VA Domain Pack) | `9-Meta` | 0 |
| `video.aiqaconsistency` | AIQAConsistencyAgent (VA Domain Pack) | `8-AI` | 0 |
| `video.gatekeeper` | GateKeeperAgent (VA Domain Pack) | `9-Meta` | 0 |
| `video.critic` | CriticAgent (VA Domain Pack) | `10-Sup` | 0 |
| `video.judge` | JudgeAgent (VA Domain Pack) | `9-Meta` | 0 |

Copied from each member’s `agent_spec.json` on 2026-09-03. When authoring `roster.json`, copy `va_category` from the file at authoring time. If a field is missing, leave `department` empty. **Do not** paste v1’s `"above_the_line"`. Because every listed member has `max_refinement_count: 0`, a swarm `critique.max_iterations: 3` **does not iterate** (min with members is 0).

**Organization:** Agent Group `video` → live categories → those nine ids. Unused `video.*` agents remain in Fleet but are not on this roster.

**Graph:** orchestrate → plan → write → qc → package (see §9.1). Optional nodes `direct` (`video.creativedirector`) and `research` (`video.webresearch`) MAY be inserted; they MUST exist as live ids.

**Critique:** enabled in JSON; if members have `max_refinement_count: 0`, the loop does not iterate.

**Tools / plugins:** `[]`. Preview MUST show any vendor names as inert.

**LLM:** host default. Chat remains `POST /api/v3/agents/video.orchestrator/runtime/chat` (or any member), not a swarm chat.

**Workflow picture:** clicking `video.orchestrator` on `video.workflow.svg` opens `/agents/video.orchestrator/chat`.

**Must not:** invent a “spine director” with no folder; inherit screenwriter SPEC onto orchestrator via swarm JSON; enable a vendor video API because the graph mentioned it; skip HITL on publish; dump all 114 video agents into one budget-8 spine; treat Org Chat as the critique bus.

---

# 21. Proposed template

Parallel to `agents/_template_v3` / `casops.template.baseline_safe`:

| Disk folder | Public id |
|---|---|
| `swarms/_template_v2/` | `casops.template.swarm_safe` |

Baseline: `production_activation_requested: false`, `t3_requested: false`, `network_requested: false`, empty tool/plugin node lists, memory writes forbidden, `engine: casops.runtime`, `pattern: pipeline`, owner = `casops.template.baseline_safe`, single-node graph so `max_peer_hops: 0` still closes.

This template **is not in the checkout until an implementation task creates it.**

---

# 22. Migration from v1

| v1 | v2 |
|---|---|
| `schema_version: "1.0"` | `"3.0"` |
| `structure_id: casops.common_swarm` | `casops.common_swarm.v2` |
| Member `casops.common_agent` | `casops.common_agent.v3` |
| `/api/v1/swarms/{id}/...` | `/api/v3/swarms/{swarm_id}/...` |
| `engine: "graph"` | `engine: "casops.runtime"` |
| `approval_authority: "host_gated"` | `independent_approver` |
| Roster `department: "above_the_line"` | Live `va_category` or empty |
| `SWM_MEMBER_MISSING` | `INH_PARENT_MISSING` |
| `SWM_NOT_COMMON_AGENT` | `INH_STRUCTURE_MISMATCH` |
| `SWM_CYCLE` | `PERF_PLAN_CYCLE` |
| `SWM_TOOL_LEAK` | `SKL_TOOL_LEAK` |
| `SWM_BUDGET` | `PERF_BUDGET_EXCEEDED` |
| `SWM_RESOLVED_DRIFT` | `INH_RESOLVED_DRIFT` |
| `SWM_DISCLOSURE` | `IDN_DISCLOSURE_MISSING` |
| PUT without headers | Four mutation headers |
| UI out of scope | §16 |
| `media.stub` assumed | No implicit tool |
| LangGraph | `casops.runtime` |
| `agents/<agent_id>/` only | `locate_agent_folder` |

A v1 folder MUST NOT load until a migrator rewrites these fields. Fail closed (`CMP_SCHEMA_INCOMPATIBLE` or `INH_STRUCTURE_MISMATCH`).

---

# 23. Traceability

| Need | FR / section | AC | Live evidence |
|------|--------------|----|---------|
| Swarm folder | §6 | AC-SWM-001 | specified |
| Members are v3 | FR-MEM-* | AC-SWM-002, 003, 019 | `locate_agent_folder`, 135 agent folders |
| Three maps | §5, S9 | AC-SWM-021–022 | Fleet, Org Chat, Workflow |
| Bounded graph | FR-GRF-* | AC-SWM-005, 006 | specified; member DAG live |
| Critique / I/O | §10 | — | live `critique_edges`; loop specified |
| Constraints | §11 | AC-SWM-007, 008, 015–017 | member plane live |
| Mutation | §2.3, §15 | AC-SWM-009, 014 | live middleware |
| Run order | §14 | AC-SWM-009–013 | specified outer; inner `Runtime.execute` live |
| REST | §15 | AC-SWM-020, 024 | companion contract |
| UI | §16 | AC-SWM-021–023 | `ui/src/App.tsx` |
| Corrigibility | §12.5 | — | live attestation |
| Migration | §22 | — | fail closed on v1 JSON |

---

# 24. Open risks

| Risk | Mitigation |
|------|------------|
| Authors dump all 114 `video.*` agents into one spine and blow the budget | Caps; subset roster; dry-run required |
| Authors treat `va_category` or SVG labels as runnable agents | S9; membership locate |
| Swarm JSON copies vendor tool names from old DNA | FR-GRF-005; `SKL_TOOL_LEAK` |
| Operators expect Workflow click to run the swarm | AC-SWM-021; click opens Chat |
| Operators treat Org Chat as Chat | AC-SWM-022 |
| Operators expect `/api/v1` from v1 printouts | AC-SWM-024; §22 |
| Persona on one member “sounds sure” for the whole crew | Per-agent disclosure on the run artifact |
| Dry-run misread as zero effects | D-SWM-15; Run tooltip honesty already in UI |
| Catalogue amended without 12 fields | Reject the amendment |
| Magic test `== 135` | Assert folder scan, not a literal |
| Implementing swarm run before compose-preview | Gate: preview + `wrote_locks: false` first |
| LLM provider pick used as a network grant | §11.5; `GATE_NETWORK` |

---

# 25. Document control

| Item | Value |
|------|-------|
| Owner | Host architecture (CASOPS) |
| Document | `spec/common_swarm_structure.v2.md` |
| Supersedes | `spec/common_swarm_structure.v1.md` |
| Member contract | `casops.common_agent.v3` / schema `3.0` |
| Host package | `casops` `0.1.0` |
| Public plane | `/api/v3` on `:18080` |
| Control UI | `ui/` on `:15173` |
| Implements swarm HTTP in this checkout? | **No** — specified |
| Live visualization maps? | **Yes** — Fleet, Org Chat, Workflow |
| Production activation? | **No** |
| Network grant? | **No** |
| T3 enable? | **No** |
| Plugin execute on public plane? | **No** |
| A2A? | **No** |
| LangGraph? | **No** |
| Diagrams | Inline SVG in this document |
| Catalogue amendment required for `SWM_*`? | **Yes**, before those codes may be returned |

**End of specification.**
