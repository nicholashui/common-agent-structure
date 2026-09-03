# Common Swarm Structure
## Complete Functional Specification

**Document ID:** `CASOPS-FS-COMMON-SWARM-STRUCTURE`  
**Date:** 2026-08-17  
**Status:** Design specification — **not** a live pack mutation, **not** a production-activation license  
**Host:** `common-agent-swarm-ops`  
**Structure family:** `casops.common_swarm`

A common swarm is a **self-contained folder** that names, wires, budgets, and runs a set of **common agents**. One folder is one `swarm_id`. Every member agent is itself a common-agent folder (`structure_id: casops.common_agent`): owned SPEC, fail-closed `agent_spec.json`, optional inheritance mixins, skill enable/disable, and identity overlay. The swarm does not replace those identities. It composes them.

Domain logic stays in the pack. The host stays fail-closed. FastAPI is the only public control plane. This is host-native composition, not an Agent-to-Agent (A2A) transport.

**Normative diagrams** are drawn inline in this document (folder contract, membership, pipeline, critique bus, run lifecycle).

---

## Table of contents

1. Purpose  
2. Scope, actors, and non-goals  
3. Core principles  
4. Folder contract  
5. Membership — every node is a common agent  
6. Roster and organization  
7. Graph, DNA, and patterns  
8. Critique bus and handoffs  
9. Swarm skill and identity policy  
10. Budgets, risk gates, interrupts, rollback  
11. Data model  
12. Runtime behaviour  
13. Operator and host APIs  
14. Honesty, safety, and fail-closed rules  
15. Error catalogue  
16. Acceptance criteria  
17. Worked example  
18. Traceability  
19. Open risks

---

## 1. Purpose

Operators need a swarm that is as explicit as a common agent, without inventing a second kind of runtime identity.

1. **Named crew.** A swarm lists member `agent_id`s. Each member is a common-agent folder, not a prompt alias.  
2. **Bounded graph.** Nodes, edges, entry, terminals, visit caps, and compensation are declared.  
3. **Governed run.** Budgets, risk gates, human interrupts, and critique loops are first-class.  
4. **Honest compose.** Inheritance, skill toggles, and persona overlays stay on the **agent**. The swarm may constrain them; it may not silently grant tools, network, or production activation.

This specification is the complete contract for that swarm folder.

<div role="img" aria-label="Swarm composes common agents; it does not replace them">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 720" role="img" aria-labelledby="sw1-t sw1-d">
  <title id="sw1-t">Swarm membership</title>
  <desc id="sw1-d">A swarm folder lists member agent folders. Each member follows the common agent structure.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .m{fill:#334155;font:400 11px ui-monospace,Menlo,Consolas,monospace}
      .core{fill:#1D4ED8}
      .ag{fill:#EFF6FF;stroke:#93C5FD;stroke-width:1.5}
      .sw{fill:#F5F3FF;stroke:#C4B5FD;stroke-width:1.5}
      .ok{fill:#ECFDF5;stroke:#86EFAC;stroke-width:1.5}
    </style>
  </defs>
  <rect class="bg" width="1440" height="720"/>
  <text class="ink" x="40" y="42">Common swarm — compose, do not replace</text>
  <text class="sub" x="40" y="66">Every graph node names a common-agent folder. Swarm policy can tighten; it cannot loosen host gates.</text>
  <rect class="sw" x="40" y="96" width="420" height="560" rx="16"/>
  <text class="h" x="64" y="128">swarms/&lt;pack.swarm-id&gt;/</text>
  <text class="m" x="64" y="160">SWARM.md</text>
  <text class="m" x="64" y="184">swarm_spec.json</text>
  <text class="m" x="64" y="208">roster.json</text>
  <text class="m" x="64" y="232">graph.json</text>
  <text class="m" x="64" y="256">policies/</text>
  <text class="m" x="64" y="280">evals/</text>
  <text class="b" x="64" y="320">Owns: wiring, budget, gates,</text>
  <text class="b" x="64" y="344">critique loop, rollback plan.</text>
  <text class="b" x="64" y="380">Does not own: agent SPEC,</text>
  <text class="b" x="64" y="404">tools, credentials, persona</text>
  <text class="b" x="64" y="428">facts, or another agent’s</text>
  <text class="b" x="64" y="452">exclusive craft output.</text>
  <rect class="core" x="520" y="200" width="160" height="64" rx="10"/>
  <text class="h2" x="540" y="238">roster[]</text>
  <rect class="ag" x="760" y="96" width="640" height="160" rx="14"/>
  <text class="h" x="780" y="128">agents/video.orchestrator/</text>
  <text class="b" x="780" y="156">SPEC · agent_spec · skills · identity</text>
  <text class="m" x="780" y="184">structure_id: casops.common_agent</text>
  <rect class="ag" x="760" y="276" width="640" height="160" rx="14"/>
  <text class="h" x="780" y="308">agents/video.planner/</text>
  <text class="b" x="780" y="336">SPEC · agent_spec · skills · identity</text>
  <text class="m" x="780" y="364">same folder family · own agent_id</text>
  <rect class="ok" x="760" y="456" width="640" height="200" rx="14"/>
  <text class="h" x="780" y="488">Membership rule</text>
  <text class="b" x="780" y="516">Unknown, missing, or non-common agent_id</text>
  <text class="b" x="780" y="540">fails closed. Aliases and prompt-only</text>
  <text class="b" x="780" y="564">roles are illegal swarm members.</text>
  <text class="b" x="780" y="600">Inheritance mixins stay inside the agent.</text>
  <text class="b" x="780" y="624">The swarm never copies parent folders.</text>
</svg>
</div>

---

## 2. Scope, actors, and non-goals

### 2.1 In scope

- Every swarm folder that declares `structure_id: casops.common_swarm`.  
- Membership restricted to common agents (`casops.common_agent`).  
- Roster, organization (orchestrator → planner → departments/roles → members), execution graph, critique loop, budgets, risk gates, human interrupts, rollback.  
- Swarm-level skill allow/deny and identity disclosure policy (constraints only).  
- Host REST routes for inspect, preview, and dry-run.  
- Acceptance tests and a worked spine example.

### 2.2 Out of scope

- Mutating live pack trees by this document alone.  
- LangGraph engine internals (the host already owns the graph engine).  
- A2A protocol (agent cards, JSON-RPC tasks, cross-vendor discovery).  
- UI screen contracts and CLI command maps (a UI or CLI may call the REST routes later).  
- New vendor APIs, MCP servers, or credential vaults.  
- Granting production activation or network via swarm JSON.

### 2.3 Actors

| Actor | Does |
|-------|------|
| Pack author | Declares swarm folder, roster, graph, budgets, gates |
| Operator | Selects swarm, previews compose, toggles allowed member skills only through agent APIs |
| Host runtime | Validates members, composes each agent, walks the graph, records evidence |
| Reviewer / CI | Cycle check, member hashes, budget dry-run, no tool leak |
| Human governor | Irreversible/publish interrupts; production activation; named-person personas |

---

## 3. Core principles

| ID | Principle | Meaning |
|----|-----------|---------|
| S1 | One swarm identity | One folder = one `swarm_id`. |
| S2 | Members are common agents | Every `agent_id` on the roster and every graph node MUST resolve to a common-agent folder. |
| S3 | Swarm composes, agent owns | Wiring lives on the swarm. SPEC, tools, persona, and inheritance live on the agent. |
| S4 | Safety tightens | Swarm budget is the **min** of swarm caps and each member’s caps. Tools are the **intersection** of node `tool_ids`, member `allowed_tools`, and host register. Network AND production flags AND across members and swarm (false wins). |
| S5 | Owner is a member | `owner_agent_id` MUST be on the roster and MUST be a common agent (typically orchestrator). |
| S6 | Critique is composition | Critique edges are peer messages between running member identities, not parent mixins and not A2A. |
| S7 | Fail closed | Missing member, graph cycle (unless declared bounded loop), budget breach, undeclared tool → abort. |
| S8 | Disclose overlays | If any running member is not `grounded`, the swarm run artifact carries that member’s disclosure. |
| S9 | Org chart ≠ execution graph | Category departments are a roster view. The run follows `graph.json`. |
| S10 | Host stays domain-agnostic | Domain steps stay in the pack swarm folder. No second control plane. |

---

## 4. Folder contract

<div role="img" aria-label="Self-contained common swarm folder">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 820" role="img" aria-labelledby="sw2-t sw2-d">
  <title id="sw2-t">Common swarm folder</title>
  <desc id="sw2-d">Swarm folder tree: SWARM.md, swarm_spec, roster, graph, policies, evals.</desc>
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
      .pu{fill:#F5F3FF;stroke:#C4B5FD;stroke-width:1.5}
      .bl{fill:#EFF6FF;stroke:#93C5FD;stroke-width:1.5}
      .am{fill:#FFFBEB;stroke:#FCD34D;stroke-width:1.5}
    </style>
  </defs>
  <rect class="bg" width="1440" height="820"/>
  <text class="ink" x="40" y="42">Common swarm — self-contained folder</text>
  <text class="sub" x="40" y="66">One folder = one swarm_id. Offline-readable. Member agents stay in agents/&lt;id&gt;/.</text>
  <rect class="card" x="40" y="92" width="720" height="692" rx="16"/>
  <text class="sec" x="64" y="122">FOLDER  ·  swarms/&lt;pack.swarm-id&gt;/</text>
  <text class="m" x="64" y="156">README.md</text>
  <text class="b" x="300" y="156">folder index</text>
  <text class="m" x="64" y="184">SWARM.md</text>
  <text class="b" x="300" y="184">owned mission and bounds</text>
  <text class="m" x="64" y="212">swarm_spec.json</text>
  <text class="b" x="300" y="212">host runtime binding</text>
  <text class="m" x="64" y="240">roster.json</text>
  <text class="b" x="300" y="240">member agent_ids + roles</text>
  <text class="m" x="64" y="268">graph.json</text>
  <text class="b" x="300" y="268">nodes, edges, entry, terminals</text>
  <text class="m" x="64" y="296">policies/</text>
  <text class="b" x="300" y="296">skill, identity, interrupt</text>
  <text class="m" x="64" y="324">evals/</text>
  <text class="b" x="300" y="324">golden dry-runs</text>
  <text class="m" x="64" y="352">sources/</text>
  <text class="b" x="300" y="352">PROVENANCE</text>
  <rect class="pu" x="64" y="384" width="672" height="120" rx="10"/>
  <text class="h" x="84" y="412">Generated at load</text>
  <text class="m" x="84" y="440">resolved.json     member hashes + composed envelopes</text>
  <text class="m" x="84" y="464">conflicts.json    policy vs member clashes</text>
  <rect class="am" x="64" y="524" width="672" height="220" rx="10"/>
  <text class="h" x="84" y="552">Not in this folder</text>
  <text class="b" x="84" y="580">Agent SPEC.md, prompts, persona, inheritance</text>
  <text class="b" x="84" y="604">remain under agents/&lt;agent_id&gt;/.</text>
  <text class="b" x="84" y="640">The swarm references those folders by id.</text>
  <text class="b" x="84" y="664">Copying agent trees into the swarm is illegal.</text>
  <rect class="bl" x="784" y="92" width="616" height="692" rx="16"/>
  <text class="sec" x="808" y="122">UNIT OF IDENTITY</text>
  <text class="h" x="808" y="156">swarm_id = pack.swarm-name</text>
  <text class="m" x="808" y="184">video.spine</text>
  <text class="m" x="808" y="208">video.pack-spine</text>
  <text class="h" x="808" y="252">Host binding (swarm_spec.json)</text>
  <text class="b" x="808" y="280">owner_agent_id · engine · pattern</text>
  <text class="b" x="808" y="304">execution_budget · risk_gate_ids</text>
  <text class="b" x="808" y="328">rollback · critique · interrupts</text>
  <text class="b" x="808" y="352">production_activation_requested = false</text>
  <text class="h" x="808" y="400">Truth chain</text>
  <text class="b" x="808" y="428">pack swarm index → swarm_spec.json</text>
  <text class="b" x="808" y="452">→ SWARM.md mission → roster.json</text>
  <text class="b" x="808" y="476">→ graph.json → each member agent_spec</text>
  <text class="b" x="808" y="516">Drift among those is a CI fail.</text>
  <text class="h" x="808" y="560">Engine</text>
  <text class="b" x="808" y="588">graph (bounded pack graph)</text>
  <text class="b" x="808" y="612">or linear DNA steps compiled to graph</text>
  <text class="b" x="808" y="636">Host chooses the runner. Swarm JSON</text>
  <text class="b" x="808" y="660">does not open a second product API.</text>
</svg>
</div>

### 4.1 Tree

```text
swarms/<pack.swarm-id>/
  README.md
  SWARM.md
  swarm_spec.json
  roster.json
  graph.json
  policies/
    skill_policy.json
    identity_policy.json
    interrupt_policy.json
  evals/
  sources/
    PROVENANCE.json
  resolved.json          # generated
  conflicts.json         # generated
```

### 4.2 Required vs optional

| Path | Required | Author |
|------|----------|--------|
| `README.md` | Yes | Human |
| `SWARM.md` | Yes | Human |
| `swarm_spec.json` | Yes | Human / generator |
| `roster.json` | Yes | Human |
| `graph.json` | Yes | Human |
| `policies/skill_policy.json` | Yes (may be empty allow) | Human |
| `policies/identity_policy.json` | Yes | Human |
| `policies/interrupt_policy.json` | Yes | Human |
| `sources/PROVENANCE.json` | Yes | Generator + review |
| `resolved.json` | Yes after first successful load | **Generator only** |
| `evals/` | Optional but expected | Human |

`resolved.json` is a load-time artifact. Hand edits that drift from member hashes fail closed.

---

## 5. Membership — every node is a common agent

A swarm member is legal iff all of:

1. `agent_id` is unique on the roster.  
2. Folder `agents/<agent_id>/` exists under a pack on this host.  
3. That folder contains `SPEC.md` and `agent_spec.json`.  
4. `agent_spec.json` declares `structure_id: casops.common_agent` (or is loadable as that family).  
5. The agent has an owned `## Responsibility` (child mission). Optional inheritance mixins, skill toggles, and identity overlay follow the common-agent contract restated below.  
6. `production_activation_requested` is false unless a separate human gate already flipped that **agent** (the swarm cannot flip it).  
7. `model_policy.network_access` is false unless that same class of gate already flipped that **agent**.

### 5.1 Common-agent contract the swarm relies on (restated)

The swarm does not redefine the agent folder. It requires this membership surface:

| Agent surface | Swarm effect |
|---------------|--------------|
| `SPEC.md` mission | Bound to graph node; swarm cannot rewrite it |
| `agent_spec.json` | Tools, budget, critique edges, activation |
| `inheritance/` | Resolved **before** the node runs; MRO is per-agent |
| `skills/` + toggles | Swarm skill_policy may **deny** or **require**; it may not enable an undeclared skill |
| `identity/` | Swarm identity_policy may require `grounded` or disclosure; it may not invent a persona |

Illegal: prompt-only roles, unnamed “crew”, specials that are not common-agent folders, agents from outside this host.

### 5.2 Functional requirements

| ID | Requirement |
|----|-------------|
| FR-MEM-001 | Every `graph.json` node `agent_id` MUST appear on `roster.json`. |
| FR-MEM-002 | Every roster `agent_id` MUST pass the membership checks in §5. |
| FR-MEM-003 | `owner_agent_id` MUST be on the roster. |
| FR-MEM-004 | Duplicate `agent_id` on the roster fails closed (`SWM_ROSTER_DUP`). |
| FR-MEM-005 | A graph node MAY reuse the same `agent_id` on distinct node ids (same agent, two steps). |
| FR-MEM-006 | Standby / unused roster members are allowed; they do not run unless a node names them. |
| FR-MEM-007 | Cross-pack members are allowed only if both packs use common-agent folders on this host. |

---

## 6. Roster and organization

<div role="img" aria-label="Swarm organization: orchestrator, planner, departments, members">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 640" role="img" aria-labelledby="sw3-t sw3-d">
  <title id="sw3-t">Swarm organization</title>
  <desc id="sw3-d">Orchestrator above Planner. Departments hang under Planner. Member agents hang under departments. Execution graph is separate.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .top{fill:#1D4ED8}
      .dept{fill:#0F766E}
      .ag{fill:#78716C}
      .note{fill:#FFFBEB;stroke:#FCD34D;stroke-width:1.5}
    </style>
    <marker id="sw3-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#64748B"/>
    </marker>
  </defs>
  <rect class="bg" width="1440" height="640"/>
  <text class="ink" x="40" y="42">Organization view — reporting, not the run</text>
  <text class="sub" x="40" y="66">Matches the Registry org chart idea: Orchestrator → Planner → category departments → members. Specials are members only if they are common agents.</text>
  <rect class="top" x="560" y="92" width="320" height="56" rx="10"/>
  <text class="h2" x="584" y="126">Orchestrator  ·  run state</text>
  <line x1="720" y1="148" x2="720" y2="176" stroke="#64748B" stroke-width="2" marker-end="url(#sw3-arr)"/>
  <rect class="top" x="560" y="180" width="320" height="56" rx="10"/>
  <text class="h2" x="584" y="214">Planner  ·  task graph</text>
  <line x1="720" y1="236" x2="200" y2="284" stroke="#64748B" stroke-width="2" marker-end="url(#sw3-arr)"/>
  <line x1="720" y1="236" x2="520" y2="284" stroke="#64748B" stroke-width="2" marker-end="url(#sw3-arr)"/>
  <line x1="720" y1="236" x2="840" y2="284" stroke="#64748B" stroke-width="2" marker-end="url(#sw3-arr)"/>
  <line x1="720" y1="236" x2="1160" y2="284" stroke="#64748B" stroke-width="2" marker-end="url(#sw3-arr)"/>
  <rect class="dept" x="80" y="292" width="240" height="48" rx="8"/>
  <text class="h2" x="100" y="322">Above-the-line</text>
  <rect class="dept" x="400" y="292" width="240" height="48" rx="8"/>
  <text class="h2" x="420" y="322">Editorial / craft</text>
  <rect class="dept" x="720" y="292" width="240" height="48" rx="8"/>
  <text class="h2" x="740" y="322">Quality / gate</text>
  <rect class="dept" x="1040" y="292" width="280" height="48" rx="8"/>
  <text class="h2" x="1060" y="322">Meta / support</text>
  <rect class="ag" x="80" y="368" width="240" height="40" rx="8"/>
  <text class="h2" x="100" y="394">director · screenwriter</text>
  <rect class="ag" x="400" y="368" width="240" height="40" rx="8"/>
  <text class="h2" x="420" y="394">editor · color · sound</text>
  <rect class="ag" x="720" y="368" width="240" height="40" rx="8"/>
  <text class="h2" x="740" y="394">judge · critic · qc</text>
  <rect class="ag" x="1040" y="368" width="280" height="40" rx="8"/>
  <text class="h2" x="1060" y="394">router · memory · ux</text>
  <rect class="note" x="80" y="440" width="1240" height="160" rx="12"/>
  <text class="h" x="104" y="472">Two maps, one roster</text>
  <text class="b" x="104" y="500">Organization view groups members by category for humans (org chart).</text>
  <text class="b" x="104" y="524">Execution view is graph.json (orchestrate → plan → craft → qc → package).</text>
  <text class="b" x="104" y="548">Critique overlay is optional dashed peer edges; it is not the reporting line.</text>
  <text class="b" x="104" y="572">A department label is not an agent_id and cannot run.</text>
</svg>
</div>

### 6.1 `roster.json`

```json
{
  "schema_version": "1.0",
  "swarm_id": "video.spine",
  "owner_agent_id": "video.orchestrator",
  "members": [
    { "agent_id": "video.orchestrator", "org_role": "top", "department": "orchestration" },
    { "agent_id": "video.planner", "org_role": "top", "department": "orchestration" },
    { "agent_id": "video.screenwriter", "org_role": "member", "department": "above_the_line" },
    { "agent_id": "video.creativedirector", "org_role": "member", "department": "above_the_line" },
    { "agent_id": "video.judge", "org_role": "member", "department": "quality" },
    { "agent_id": "video.critic", "org_role": "member", "department": "quality" }
  ]
}
```

`department` is a label for organization view only. `org_role` is `top` | `member`. Tops are the pipeline (orchestrator, then planner). Departments fan out from planner.

---

## 7. Graph, DNA, and patterns

### 7.1 Execution graph (`graph.json`)

```json
{
  "schema_version": "1.0",
  "definition_type": "pack_graph",
  "id": "video.spine",
  "engine": "graph",
  "pattern": "pack_spine",
  "entry_node": "orchestrate",
  "terminal_node_ids": ["package"],
  "nodes": [
    { "id": "orchestrate", "agent_id": "video.orchestrator", "tool_ids": [], "memory_reads": [], "memory_writes": [] },
    { "id": "plan", "agent_id": "video.planner", "tool_ids": [], "memory_reads": [], "memory_writes": [] },
    { "id": "write", "agent_id": "video.screenwriter", "tool_ids": [], "memory_reads": [], "memory_writes": [] },
    { "id": "qc", "agent_id": "video.aiqaconsistency", "tool_ids": [], "memory_reads": [], "memory_writes": [] },
    { "id": "package", "agent_id": "video.gatekeeper", "tool_ids": [], "memory_reads": [], "memory_writes": [] }
  ],
  "edges": [
    { "from": "orchestrate", "to": "plan", "max_traversals": 1 },
    { "from": "plan", "to": "write", "max_traversals": 1 },
    { "from": "write", "to": "qc", "max_traversals": 1 },
    { "from": "qc", "to": "package", "max_traversals": 1 }
  ]
}
```

Legal `pattern` values: `pipeline` | `supervisor` | `router` | `critique` | `map_reduce` | `pack_spine`.

Linear DNA is the same nodes without explicit edges: host compiles steps in order into a pipeline graph. Caps: 1–100 nodes; edge `max_traversals` 1–10.

### 7.2 Functional requirements

| ID | Requirement |
|----|-------------|
| FR-GRF-001 | `entry_node` MUST exist in `nodes`. |
| FR-GRF-002 | Every `terminal_node_ids` entry MUST exist in `nodes`. |
| FR-GRF-003 | Every edge `from`/`to` MUST be a node id. |
| FR-GRF-004 | Unbounded cycles fail closed. A cycle is legal only if every participating edge has `max_traversals` and swarm `max_node_visits` cannot be exceeded. |
| FR-GRF-005 | Node `tool_ids` that are not in that member’s `allowed_tools` ∩ host register fail closed (`SWM_TOOL_LEAK`). |
| FR-GRF-006 | `media.stub` (or equivalent local stub) is the only tool family assumed present without a human gate. Named vendor tools in JSON are design-time and non-activating. |
| FR-GRF-007 | Memory read/write ids MUST be declared on the swarm memory list. |

---

## 8. Critique bus and handoffs

<div role="img" aria-label="Critique bus between running swarm members">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 520" role="img" aria-labelledby="sw4-t sw4-d">
  <title id="sw4-t">Critique and handoff</title>
  <desc id="sw4-d">Typed artifacts flow along graph edges. Critique messages flow on a bus between member identities. Not A2A.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .n{fill:#1D4ED8}
      .c{fill:#7C3AED}
      .am{fill:#FFFBEB;stroke:#FCD34D;stroke-width:1.5}
    </style>
  </defs>
  <rect class="bg" width="1440" height="520"/>
  <text class="ink" x="40" y="42">Two buses — handoff vs critique</text>
  <text class="sub" x="40" y="66">Handoff follows graph edges. Critique follows member critique_edges, unioned with swarm critique loop.</text>
  <rect class="n" x="80" y="100" width="200" height="56" rx="10"/>
  <text class="h2" x="100" y="134">screenwriter</text>
  <rect class="n" x="360" y="100" width="200" height="56" rx="10"/>
  <text class="h2" x="380" y="134">director</text>
  <rect class="n" x="640" y="100" width="200" height="56" rx="10"/>
  <text class="h2" x="660" y="134">editor</text>
  <rect class="n" x="920" y="100" width="200" height="56" rx="10"/>
  <text class="h2" x="940" y="134">gatekeeper</text>
  <text class="b" x="80" y="184">handoff artifact → → → (graph edge, versioned, copy-on-write)</text>
  <rect class="c" x="360" y="220" width="200" height="56" rx="10"/>
  <text class="h2" x="400" y="254">critic</text>
  <rect class="c" x="640" y="220" width="200" height="56" rx="10"/>
  <text class="h2" x="700" y="254">judge</text>
  <text class="b" x="80" y="308">critique JSON ← → (sender, receiver, artifact_reference, severity, evidence, rubric score)</text>
  <rect class="am" x="80" y="340" width="1280" height="140" rx="12"/>
  <text class="h" x="104" y="372">Not A2A</text>
  <text class="b" x="104" y="400">No agent cards, no JSON-RPC tasks, no cross-host discovery.</text>
  <text class="b" x="104" y="424">Sender and receiver are running member agent_ids (children), never parent mixins.</text>
  <text class="b" x="104" y="448">Max refine = min(swarm critique.max_iterations, each member max_refinement_count, 1–3).</text>
</svg>
</div>

### 8.1 Critique message (normative fields)

`critique_id`, `sender`, `receiver`, `artifact_reference`, `severity` (`blocker`|`major`|`minor`|`nit`), `category`, `evidence[]`, `suggested_action`, `rubric.reference`, `rubric.score` (0–1), `deadline_or_phase`, `timestamp`.

### 8.2 Swarm critique loop

```json
{
  "enabled": true,
  "max_iterations": 3,
  "lead_agent_id": "video.critic",
  "judge_agent_id": "video.judge"
}
```

Lead and judge MUST be roster members. If `enabled` is false, member `critique_edges` still exist but the swarm does not iterate a loop.

Handoff artifacts are immutable versions with `parent_assets` forming an acyclic DAG. A member must not own another member’s exclusive craft without this handoff (`does_not_own` union still applies).

---

## 9. Swarm skill and identity policy

The swarm **constrains** member compose. It does not author member skills or personas.

### 9.1 Skill policy

```json
{
  "deny": ["undeclared_vendor_media"],
  "require": [],
  "allow_member_toggles": true
}
```

| Rule | Effect |
|------|--------|
| deny `skill_id` | That skill is OFF for every member in this swarm, even if the agent declared it ON |
| require `skill_id` | Load fails unless every **running** node’s agent has that skill declared (not invented) and enabled |
| allow_member_toggles | Operator may still PATCH the **agent** skill toggle; swarm deny still wins |

### 9.2 Identity policy

```json
{
  "default_expertise_mode": "grounded",
  "allow_persona_overlay": true,
  "require_disclosure": true,
  "forbid_named_persons": true
}
```

If any running member is not `grounded`, the swarm run banner lists those `agent_id`s and disclosure ids. Swarm cannot set a member persona.

---

## 10. Budgets, risk gates, interrupts, rollback

### 10.1 Execution budget

| Field | Range | Merge |
|-------|-------|-------|
| `max_node_visits` | 1–100 | min(swarm, members’ implied visits) |
| `max_handoffs` | 0–12 | min |
| `max_wall_clock_seconds` | 1–900 | min |
| `max_tool_requests` | 0–50 | min with each member `budget_policy.max_tool_requests` |

Breach → `SWM_BUDGET` abort. No silent continue.

### 10.2 Risk gates

`risk_gate_ids` min 1. Unknown gate id fails closed. Gates run at entry and before terminal nodes.

### 10.3 Human interrupts

```json
{
  "required": true,
  "gates": [
    { "id": "release_or_irreversible", "when": "irreversible_or_publish", "required": true }
  ],
  "approval_authority": "host_gated"
}
```

Irreversible or publish steps MUST interrupt. The swarm cannot auto-approve.

### 10.4 Rollback

`rollback.plan_id` plus `compensation_step_ids` that MUST be node ids on this graph. Compensation nodes run only on abort after a successful prefix. Compensation cannot enable extra tools.

---

## 11. Data model

### 11.1 `swarm_spec.json`

```json
{
  "schema_version": "1.0",
  "structure_id": "casops.common_swarm",
  "swarm_id": "video.spine",
  "status": "registered",
  "owner_agent_id": "video.orchestrator",
  "authorization_id": "video.local-spine",
  "engine": "graph",
  "pattern": "pack_spine",
  "execution_budget": {
    "max_node_visits": 8,
    "max_handoffs": 7,
    "max_wall_clock_seconds": 60,
    "max_tool_requests": 16
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
  "roster_ref": "roster.json",
  "graph_ref": "graph.json"
}
```

### 11.2 Run artifact extras

| Field | Notes |
|-------|--------|
| `swarm_id` | |
| `run_id` / `correlation_id` | Host |
| `mro_by_agent` | Each member’s resolved MRO |
| `skills_loaded_by_agent` | After swarm deny |
| `expertise_modes` | Per running agent |
| `disclosure_ids` | If any overlay |
| `node_trace` | Ordered node ids + visit counts |
| `budget_remaining` | Snapshot at end or abort |

---

## 12. Runtime behaviour

<div role="img" aria-label="Swarm run lifecycle">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 420" role="img" aria-labelledby="sw5-t sw5-d">
  <title id="sw5-t">Swarm run lifecycle</title>
  <desc id="sw5-d">Validate members, compose each agent, walk graph, critique, interrupt, package or abort.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 11px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .st{fill:#1D4ED8}
    </style>
    <marker id="sw5-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#64748B"/>
    </marker>
  </defs>
  <rect class="bg" width="1440" height="420"/>
  <text class="ink" x="40" y="42">Run — fail-closed order</text>
  <text class="sub" x="40" y="66">Any step may abort. Production activation stays a separate human gate.</text>
  <rect class="st" x="40" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="56" y="130">1  Load swarm</text>
  <text class="h2" x="56" y="150">spec + roster + graph</text>
  <rect class="st" x="280" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="296" y="130">2  Members</text>
  <text class="h2" x="296" y="150">common-agent compose</text>
  <rect class="st" x="520" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="536" y="130">3  Policy</text>
  <text class="h2" x="536" y="150">skill deny · identity</text>
  <rect class="st" x="760" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="776" y="130">4  Walk graph</text>
  <text class="h2" x="776" y="150">budget · handoff</text>
  <rect class="st" x="1000" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="1016" y="130">5  Critique</text>
  <text class="h2" x="1016" y="150">loop ≤ min caps</text>
  <rect class="st" x="1240" y="100" width="160" height="70" rx="10"/>
  <text class="h2" x="1256" y="130">6  Gate</text>
  <text class="h2" x="1256" y="150">HITL · package</text>
  <line x1="240" y1="135" x2="280" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#sw5-arr)"/>
  <line x1="480" y1="135" x2="520" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#sw5-arr)"/>
  <line x1="720" y1="135" x2="760" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#sw5-arr)"/>
  <line x1="960" y1="135" x2="1000" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#sw5-arr)"/>
  <line x1="1200" y1="135" x2="1240" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#sw5-arr)"/>
  <text class="sub" x="40" y="220">Step 2 composes each member: identity → parents MRO → merge → skills AND-gate → host tools/net/budget. Same order as a standalone common agent.</text>
  <text class="sub" x="40" y="248">Step 4 intersects node tool_ids with the composed member allow-list. Design-time vendor names stay inert.</text>
  <text class="sub" x="40" y="276">Step 6: irreversible/publish requires human interrupt. Terminal node emits the run artifact.</text>
  <text class="sub" x="40" y="320">Abort runs compensation_step_ids only. No extra tools. Evidence keeps the node_trace and error code.</text>
  <text class="sub" x="40" y="360">Parallel map_reduce pattern: fan-out nodes share a barrier; still one budget; still fail closed if any shard fails unless the pattern declares partial-ok (default false).</text>
</svg>
</div>

Catalog `status` is `draft` | `registered`. Production active is out of band.

---

## 13. Operator and host APIs

Functional HTTP routes on the existing FastAPI control plane. Not a UI spec. Not a CLI spec. Not A2A.

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/v1/swarms/{id}/structure` | `{ structure_id }` |
| GET | `/api/v1/swarms/{id}/resolved` | Members, hashes, composed skill sets, expertise modes |
| GET | `/api/v1/swarms/{id}/roster` | Organization view |
| GET | `/api/v1/swarms/{id}/graph` | Nodes, edges, entry, terminals |
| PUT | `/api/v1/swarms/{id}/roster` | Authoring; dry-run default |
| PUT | `/api/v1/swarms/{id}/graph` | Authoring; dry-run default |
| POST | `/api/v1/swarms/{id}/compose-preview` | Envelope dump per member, no model call |
| POST | `/api/v1/swarms/{id}/dry-run` | Walk graph with stubs, no network, no activation |
| GET | `/api/v1/swarms/{id}/runs/{run_id}` | Trace, budget, disclosures |

Mutating calls fail closed without operator identity, append-only audit, cannot set `production_activation_requested` true.

Member skill/identity edits stay on **agent** routes (`/api/v1/agents/{id}/…`). Swarm deny still applies at compose.

---

## 14. Honesty, safety, and fail-closed rules

- Swarm JSON cannot grant tools, network, or production activation.  
- Vendor tool names on nodes are design-time; runtime uses host register ∩ member allow-list ∩ node `tool_ids`.  
- Persona overlays remain fictional by default; named-person and license claims still abort the member compose, which aborts the swarm.  
- Disabled skills stay absent from every member envelope.  
- Critique is in-host JSON, not A2A.  
- Compensation cannot widen tools.  
- Specials may join only as common-agent folders.

---

## 15. Error catalogue

| Code | When |
|------|------|
| `SWM_MEMBER_MISSING` | Roster or node `agent_id` has no common-agent folder |
| `SWM_NOT_COMMON_AGENT` | Folder exists but is not `casops.common_agent` |
| `SWM_ROSTER_DUP` | Duplicate member id |
| `SWM_OWNER_ABSENT` | Owner not on roster |
| `SWM_GRAPH_EDGE` | Edge endpoint not a node |
| `SWM_CYCLE` | Unbounded cycle |
| `SWM_TOOL_LEAK` | Node tool not on composed allow-list |
| `SWM_BUDGET` | Visit, handoff, wall clock, or tool cap |
| `SWM_GATE_UNKNOWN` | Unknown risk_gate_id |
| `SWM_SKILL_DENY_CONFLICT` | Require skill that member does not declare |
| `SWM_RESOLVED_DRIFT` | Hand-edited resolved.json |
| `SWM_HITL_REQUIRED` | Irreversible step without interrupt |
| `SWM_DISCLOSURE` | Overlay member without disclosure |

Member compose errors (`INH_*`, `SKL_*`, `IDN_*`, `GATE_*`) abort the swarm with the member `agent_id` attached.

---

## 16. Acceptance criteria

| ID | Criterion | Proof |
|----|-----------|-------|
| AC-SWM-001 | Required swarm files exist | directory check |
| AC-SWM-002 | Node with unknown agent_id aborts `SWM_MEMBER_MISSING` | fixture |
| AC-SWM-003 | Non-common folder on roster aborts `SWM_NOT_COMMON_AGENT` | fixture |
| AC-SWM-004 | Owner missing from roster aborts | fixture |
| AC-SWM-005 | Unbounded cycle aborts; bounded max_traversals walks then stops | fixture |
| AC-SWM-006 | Node vendor tool not in member allow-list aborts `SWM_TOOL_LEAK` | preview |
| AC-SWM-007 | Swarm deny turns member skill OFF in compose-preview | preview |
| AC-SWM-008 | Overlay member without DISCLOSURE aborts | fixture |
| AC-SWM-009 | dry-run uses stubs only; no network | integration, network disabled |
| AC-SWM-010 | Irreversible terminal without HITL aborts `SWM_HITL_REQUIRED` | fixture |
| AC-SWM-011 | Budget min(swarm, members) enforced | fixture |
| AC-SWM-012 | production_activation_requested remains false through load | spec inspect |

---

## 17. Worked example

**Swarm:** `video.spine`  
**Owner:** `video.orchestrator`  
**Members:** orchestrator, planner, creativedirector, screenwriter, webresearch, aiqaconsistency, gatekeeper, critic, judge  

**Organization:** tops = orchestrator, planner. Departments: above-the-line (director, screenwriter), research (webresearch), quality (aiqaconsistency, critic, judge), gate (gatekeeper).

**Graph:** orchestrate → plan → direct → write → research → qc → package.

**Critique:** enabled; lead critic; judge judge; max_iterations = min(3, members).

**Tools:** node lists may mention vendor media; runtime allow-list is empty or stub unless a human gate already listed tools on those **agents**. Preview must show vendor names as inert.

**Must not:** invent a “spine director” that has no agent folder; inherit screenwriter SPEC onto orchestrator via swarm JSON; enable Sora because the graph mentioned it; skip HITL on publish.

---

## 18. Traceability

| Need | FR / section | AC | Diagram |
|------|--------------|----|---------|
| Swarm folder | §4 | AC-SWM-001 | folder |
| Members are common agents | FR-MEM-* | AC-SWM-002, 003 | membership |
| Org vs graph | §6, S9 | — | organization |
| Bounded graph | FR-GRF-* | AC-SWM-005, 006 | — |
| Critique / handoff | §8 | — | critique |
| Skill/identity constraints | §9 | AC-SWM-007, 008 | — |
| Run order | §12 | AC-SWM-009–012 | lifecycle |
| REST | §13 | AC-SWM-009 | — |

---

## 19. Open risks

| Risk | Mitigation |
|------|------------|
| Graph lists 114 agents and blows the budget | Caps on visits/handoffs/wall clock; dry-run required |
| Authors treat department labels as runnable agents | Department is not an agent_id (S9) |
| Swarm JSON copies vendor tool names from DNA | FR-GRF-006; SWM_TOOL_LEAK |
| Persona on one member “sounds sure” for the whole crew | Per-agent disclosure list on the run artifact |
| Operators expect A2A or CLI | §2.2; HTTP only |

---

## Document control

| Item | Value |
|------|-------|
| Owner | Host architecture (CASOPS) |
| Implements in live packs? | **No** until a separate implementation task |
| Production activation? | **No** |
| Network? | **No** |
| A2A / CLI / UI specs? | **No** — REST only |
| Diagrams | Inline SVG in this document |
| Member contract | Common agent folder (`casops.common_agent`): SPEC, agent_spec, optional inheritance, skills, identity |

**End of specification.**
