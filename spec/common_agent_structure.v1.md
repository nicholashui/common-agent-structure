# Common Agent Structure
## Complete Functional Specification

**Document ID:** `CASOPS-FS-COMMON-AGENT-STRUCTURE`  
**Date:** 2026-08-17  
**Status:** Design specification — **not** a live pack mutation, **not** a production-activation license  
**Host:** `common-agent-swarm-ops`  
**Structure family:** `casops.common_agent`

A common agent is a **self-contained folder**. One folder is one `agent_id`. The host composes that folder with optional parent mixins, skill switches, and an identity overlay. Domain logic stays in the pack. The host stays fail-closed.

**Normative diagrams** are drawn inline in this document (folder contract, three compose surfaces, inheritance MRO, skill enable/disable, identity overlay, runtime compose).

---

## Table of contents

1. Purpose  
2. Scope, actors, and non-goals  
3. Core principles  
4. Folder contract  
5. Owned mission and truth chain  
6. Multiple inheritance  
7. Configurable skills  
8. Identity: personality and professional background  
9. Merge and compose algorithm  
10. Data model  
11. Runtime behaviour  
12. Operator and host APIs  
13. Honesty, safety, and fail-closed rules  
14. Error catalogue  
15. Acceptance criteria  
16. Worked example  
17. Traceability  
18. Open risks

---

## 1. Purpose

Operators need three things from a common agent without splitting it into several runtime identities:

1. **Reuse without copy.** A showrunner mixes director, screenwriter, and producer craft by declaring those agents as parents, not by duplicating three SPECs.  
2. **Skill control.** Local harness skills and pack `special_skills` can be turned on or off with an audit trail. A disabled skill is absent.  
3. **Expertise framing.** The agent may *speak as* a DP, 1st AD, editor, or coach. That is role-play. Craft facts stay in SPEC, sources, enabled skills, and evals — and the overlay is disclosed.

This specification is the complete contract for that folder.

<div role="img" aria-label="One child identity with inheritance, skills, and identity overlay">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 820" role="img" aria-labelledby="s2-t s2-d">
  <title id="s2-t">Three compose surfaces of a common agent</title>
  <desc id="s2-d">Inheritance mixins, configurable skills, and identity overlay sit beside the owned SPEC. Child remains one agent_id.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .card{fill:#FFFFFF;stroke:#CBD5E1;stroke-width:1.5}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 14px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .m{fill:#334155;font:400 11px ui-monospace,Menlo,Consolas,monospace}
      .sec{fill:#64748B;font:700 10px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;letter-spacing:1.2px}
      .core{fill:#1D4ED8}
      .h2{fill:#FFFFFF;font:700 14px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .pu{fill:#F5F3FF;stroke:#C4B5FD;stroke-width:1.5}
      .gn{fill:#ECFDF5;stroke:#86EFAC;stroke-width:1.5}
      .am{fill:#FFFBEB;stroke:#FCD34D;stroke-width:1.5}
      .bl{fill:#EFF6FF;stroke:#93C5FD;stroke-width:1.5}
    </style>
  </defs>
  <rect class="bg" width="1440" height="820"/>
  <text class="ink" x="40" y="42">One identity · three compose surfaces</text>
  <text class="sub" x="40" y="66">The child owns the mission. Inheritance, skills, and persona are mixed in at load. They never replace agent_id.</text>

  <rect class="core" x="420" y="100" width="600" height="88" rx="14"/>
  <text class="h2" x="448" y="136">Child  ·  agents/&lt;pack.agent-id&gt;</text>
  <text class="h2" x="448" y="164" style="font-weight:400">SPEC.md mission  ·  agent_spec.json  ·  does_not_own[]</text>

  <rect class="pu" x="40" y="228" width="440" height="360" rx="16"/>
  <text class="sec" x="60" y="256">INHERITANCE</text>
  <text class="h" x="60" y="284">Multiple parent mixins</text>
  <text class="b" x="60" y="312">0–8 parents, same structure family</text>
  <text class="b" x="60" y="336">Surfaces listed per parent</text>
  <text class="b" x="60" y="360">MRO linearizes diamonds</text>
  <text class="b" x="60" y="384">Child scalars win</text>
  <text class="b" x="60" y="408">Safety fields tighten</text>
  <text class="b" x="60" y="432">Tools are never inherited</text>
  <text class="m" x="60" y="468">parents.json → resolved.json</text>
  <text class="m" x="60" y="492">cycles / missing parent → abort</text>
  <text class="b" x="60" y="532">Depth ≤ 4. Each parent loaded once.</text>
  <text class="b" x="60" y="556">Quoted under SPEC ## Inherited from</text>

  <rect class="gn" x="500" y="228" width="440" height="360" rx="16"/>
  <text class="sec" x="520" y="256">SKILLS</text>
  <text class="h" x="520" y="284">Enable / disable</text>
  <text class="b" x="520" y="312">Local harness + pack special_skills</text>
  <text class="b" x="520" y="336">Inherited skill_ids union then AND</text>
  <text class="b" x="520" y="360">Operator toggle with audit</text>
  <text class="b" x="520" y="384">Host allow-list last</text>
  <text class="b" x="520" y="408">OFF = absent from envelope</text>
  <text class="b" x="520" y="432">ON does not grant extra tools</text>
  <text class="m" x="520" y="468">bindings.json  toggles.json</text>
  <text class="m" x="520" y="492">unknown skill_id → abort</text>
  <text class="b" x="520" y="532">Author enabled:false is the floor.</text>
  <text class="b" x="520" y="556">Toggle cannot invent a skill.</text>

  <rect class="am" x="960" y="228" width="440" height="360" rx="16"/>
  <text class="sec" x="980" y="256">IDENTITY</text>
  <text class="h" x="980" y="284">Persona + profession</text>
  <text class="b" x="980" y="312">Voice, register, temperament</text>
  <text class="b" x="980" y="336">Fictional professional background</text>
  <text class="b" x="980" y="360">Speaks as craft expert (framing)</text>
  <text class="b" x="980" y="384">Facts stay in SPEC + sources</text>
  <text class="b" x="980" y="408">Modes: grounded · overlay · mixed</text>
  <text class="b" x="980" y="432">Disclosure when not grounded</text>
  <text class="m" x="980" y="468">persona.json  background.json</text>
  <text class="m" x="980" y="492">DISCLOSURE.md</text>
  <text class="b" x="980" y="532">No named living person, no license</text>
  <text class="b" x="980" y="556">claim, no tool or network grant.</text>

  <rect class="bl" x="40" y="616" width="1360" height="168" rx="16"/>
  <text class="h" x="64" y="652">Compose rule</text>
  <text class="b" x="64" y="680">Envelope = identity + child SPEC + inherited fragments (MRO) + enabled skills + host gates.</text>
  <text class="b" x="64" y="704">Critique bus, workflows, and handoffs are composition with peers — they are not parent mixins.</text>
  <text class="b" x="64" y="728">production_activation_requested stays false unless a separate human gate changes the child’s agent_spec.</text>
  <text class="m" x="64" y="756">structure_id: casops.common_agent     parents must be the same family</text>
</svg>
</div>

---

## 2. Scope, actors, and non-goals

### 2.1 In scope

- Every agent folder that declares `structure_id: casops.common_agent`.  
- Video-pack and specials-pack agents that share this folder family.  
- Inheritance only from other agents in that family.  
- Skill enable/disable for local harness skills and pack `special_skills`.  
- Personality and professional-background overlays, including pretending domain expertise as framing.  
- Merge algorithm, generated MRO, APIs, errors, acceptance tests, and a worked example.

### 2.2 Out of scope

- Mutating live pack agent trees by this document alone.  
- LangGraph internals (the host already owns orchestration).  
- New vendor APIs, MCP servers, or credential vaults.  
- Using persona confidence as a substitute for L1/L2 evals.  
- Multi-host federation of agents outside this repository.

### 2.3 Actors

| Actor | Does |
|-------|------|
| Pack author | Declares parents, skills, and identity files in the child folder |
| Operator | Toggles skills, selects expertise mode, reads disclosure |
| Host runtime | Resolves MRO, merges, gates tools, injects disclosure |
| Reviewer / CI | Verifies hashes, no cycles, no tool leak, evals still pass |
| Human governor | Sole authority for production activation, named-person personas, network |

---

## 3. Core principles

| ID | Principle | Meaning |
|----|-----------|---------|
| P1 | One identity | One folder = one `agent_id`. Inheritance does not create a new runtime class. |
| P2 | Child wins content | Local SPEC / `agent_spec.json` scalars override parents. |
| P3 | Safety tightens | `does_not_own` unions. `network_access` and `production_activation_requested` are AND (any false stays false). Tools are **never** inherited. |
| P4 | Same structure only | A parent MUST be a common-structure agent folder (`SPEC.md` + `agent_spec.json`). |
| P5 | Disabled = absent | An OFF skill is not in the prompt, tools, memory, or critique path. |
| P6 | Persona is overlay | Personality and background change voice and method preference. They do not mint facts, licenses, or tools. |
| P7 | Disclose always | `expertise_mode` other than `grounded` requires a visible disclosure on every artifact. |
| P8 | Fail closed | Unknown, cyclic, drifted, or over-claiming states abort the load. |
| P9 | Optional surfaces | Empty `parents`, no identity files, and all listed skills enabled are valid. |
| P10 | Host stays domain-agnostic | Domain logic stays in the pack folder. No second control plane. |

---

## 4. Folder contract

<div role="img" aria-label="Complete self-contained common agent folder tree">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 900" role="img" aria-labelledby="s1-t s1-d">
  <title id="s1-t">Self-contained common agent folder</title>
  <desc id="s1-d">Complete folder contract for one common-structure agent: identity files, inheritance, skills, prompts, rubrics, sources, and docs.</desc>
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
      .bl{fill:#EFF6FF;stroke:#93C5FD;stroke-width:1.5}
      .pu{fill:#F5F3FF;stroke:#C4B5FD;stroke-width:1.5}
      .gn{fill:#ECFDF5;stroke:#86EFAC;stroke-width:1.5}
      .am{fill:#FFFBEB;stroke:#FCD34D;stroke-width:1.5}
    </style>
  </defs>
  <rect class="bg" width="100%" preserveAspectRatio="xMidYMid meet" width="1440" height="900"/>
  <text class="ink" x="40" y="42">Common agent — self-contained folder</text>
  <text class="sub" x="40" y="66">One folder = one agent_id. Offline-readable. Pack corpus is not required. Host binding is fail-closed.</text>

  <rect class="card" x="40" y="92" width="720" height="772" rx="16"/>
  <text class="sec" x="64" y="122">FOLDER  ·  agents/&lt;pack.agent-id&gt;/</text>
  <text class="m" x="64" y="156">README.md</text>
  <text class="b" x="280" y="156">folder index</text>
  <text class="m" x="64" y="184">SPEC.md</text>
  <text class="b" x="280" y="184">owned mission and boundaries</text>
  <text class="m" x="64" y="212">agent_spec.json</text>
  <text class="b" x="280" y="212">host runtime binding</text>
  <text class="m" x="64" y="248">prompts/</text>
  <text class="b" x="280" y="248">primary prompt</text>
  <text class="m" x="64" y="276">rubrics/</text>
  <text class="b" x="280" y="276">L2 craft rubric</text>
  <text class="m" x="64" y="304">sources/</text>
  <text class="b" x="280" y="304">PROVENANCE · MAPPING · excerpts</text>
  <text class="m" x="64" y="332">docs/</text>
  <text class="b" x="280" y="332">operator user guide</text>
  <rect class="pu" x="64" y="360" width="672" height="120" rx="10"/>
  <text class="h" x="84" y="388">inheritance/</text>
  <text class="m" x="84" y="412">parents.json        declared parents (0–8)</text>
  <text class="m" x="84" y="436">resolved.json       generated MRO + hashes</text>
  <text class="m" x="84" y="460">conflicts.json      generated merge log</text>
  <rect class="gn" x="64" y="500" width="672" height="96" rx="10"/>
  <text class="h" x="84" y="528">skills/</text>
  <text class="m" x="84" y="552">SKILL.md  bindings.json  integration.json</text>
  <text class="m" x="84" y="576">toggles.json        operator enable / disable</text>
  <rect class="am" x="64" y="616" width="672" height="120" rx="10"/>
  <text class="h" x="84" y="644">identity/</text>
  <text class="m" x="84" y="668">persona.json        personality / voice</text>
  <text class="m" x="84" y="692">background.json     professional overlay</text>
  <text class="m" x="84" y="716">DISCLOSURE.md       overlay honesty text</text>
  <text class="b" x="64" y="764">resolved.json is generated. Hand edits fail closed.</text>
  <text class="b" x="64" y="788">Parents are referenced by agent_id, never copied in.</text>
  <text class="b" x="64" y="812">Empty parents / missing identity files are valid defaults.</text>

  <rect class="card" x="784" y="92" width="616" height="772" rx="16"/>
  <text class="sec" x="808" y="122">UNIT OF IDENTITY</text>
  <rect class="bl" x="808" y="144" width="568" height="160" rx="12"/>
  <text class="h" x="828" y="172">agent_id = pack.role</text>
  <text class="m" x="828" y="196">video.director</text>
  <text class="m" x="828" y="220">specials.llm-usage</text>
  <text class="b" x="828" y="252">Roster row, SPEC, user guide, and agent_spec.role</text>
  <text class="b" x="828" y="276">must name the same id.</text>
  <rect class="pu" x="808" y="324" width="568" height="168" rx="12"/>
  <text class="h" x="828" y="352">Host binding (agent_spec.json)</text>
  <text class="b" x="828" y="380">status · role · allowed_tools[]</text>
  <text class="b" x="828" y="404">model_policy (local_deterministic)</text>
  <text class="b" x="828" y="428">budget_policy · prompt / rubric refs</text>
  <text class="b" x="828" y="452">critique_edges · max_refinement_count</text>
  <text class="b" x="828" y="476">production_activation_requested = false</text>
  <rect class="gn" x="808" y="512" width="568" height="160" rx="12"/>
  <text class="h" x="828" y="540">Offline rule</text>
  <text class="b" x="828" y="568">Open this folder alone. No external repo</text>
  <text class="b" x="828" y="592">and no pack corpus is required to read</text>
  <text class="b" x="828" y="616">the owned mission. Parent folders are</text>
  <text class="b" x="828" y="640">resolved only at compose time.</text>
  <rect class="am" x="808" y="692" width="568" height="144" rx="12"/>
  <text class="h" x="828" y="720">Does not own</text>
  <text class="b" x="828" y="748">Credentials, silent activation, extra</text>
  <text class="b" x="828" y="772">control planes, or another agent’s</text>
  <text class="b" x="828" y="796">exclusive craft without a handoff.</text>
</svg>
</div>

### 4.1 Tree

```text
agents/<pack.agent-id>/
  README.md
  SPEC.md
  agent_spec.json
  prompts/
  rubrics/
  sources/
    PROVENANCE.json
    MAPPING.md
    excerpts/
  docs/
    user_guide.md
  inheritance/
    parents.json          # declared parents (may be empty)
    resolved.json         # generated MRO + hashes
    conflicts.json        # generated merge log
  skills/
    SKILL.md
    bindings.json
    integration.json
    toggles.json          # operator enable / disable
  identity/
    persona.json          # optional personality
    background.json       # optional professional overlay
    DISCLOSURE.md         # required when expertise_mode is not grounded
```

### 4.2 Required vs optional

| Path | Required | Author |
|------|----------|--------|
| `README.md` | Yes | Human |
| `SPEC.md` | Yes | Human |
| `agent_spec.json` | Yes | Human / generator |
| `sources/PROVENANCE.json` | Yes | Generator + human review |
| `inheritance/parents.json` | Yes (may be `{ "parents": [] }`) | Human |
| `inheritance/resolved.json` | Yes after first successful load | **Generator only** |
| `skills/toggles.json` | Yes (may be `{ "toggles": [] }`) | Human / operator API |
| `identity/DISCLOSURE.md` | Yes if expertise_mode is not `grounded` | Human |
| `prompts/`, `rubrics/`, `skills/SKILL.md`, `docs/` | Optional but expected for a runnable craft agent | Human |
| `identity/persona.json`, `identity/background.json` | Optional | Human |

`resolved.json` and `conflicts.json` are load-time artifacts. CI fails if they are hand-edited out of date versus `parents.json` and parent hashes.

Parents are **referenced** by `agent_id`. The child folder never copies a parent tree into itself.

### 4.3 Parent folder requirements

A parent `agent_id` is legal iff all of:

1. It appears in the pack roster of agent identifiers.  
2. Folder `agents/<agent_id>/` exists under that pack.  
3. That folder contains `SPEC.md` and `agent_spec.json`.  
4. It declares `structure_id: casops.common_agent` (or is loadable as that family).  
5. It is not the child (no self-parent).

Cross-pack is allowed (example: `video.showrunner` may parent `specials.aesthetics-agent`) **only** because both are common-structure agents. Arbitrary paths, URLs, and non-agent folders are illegal.

---

## 5. Owned mission and truth chain

### 5.1 SPEC.md

The child’s `## Responsibility` is the **owned** mission. Inherited fragments support it. They never silently replace the mission sentence.

Required SPEC sections:

```markdown
## Identity
## Responsibility
## Boundaries and escalation
## Inputs and outputs
## Quality and critique
## Runtime binding
## Local knowledge sources
## Inherited from          # list parent agent_id + hash + surfaces
## Identity overlay        # expertise_mode + file refs (omit if grounded)
## Provenance
```

### 5.2 Truth chain

```text
ROSTER.json
  → agent_spec.json.role
  → SPEC.md ## Responsibility
  → docs/user_guide.md
  → identity/DISCLOSURE.md     (when overlay is on)
  → inheritance/resolved.json  (when parents exist)
```

Drift among roster, role, SPEC mission, and user guide is a CI fail. Drift of `resolved.json` versus parent hashes is a CI fail.

### 5.3 Host binding (minimum)

`agent_spec.json` always carries:

`schema_version`, `agent_id`, `status`, `role`, `allowed_tools`, `model_policy`, `budget_policy`, `prompt_reference`, `rubric_reference`, `critique_edges`, `max_refinement_count`, `production_activation_requested`.

Plus `structure_id: casops.common_agent`, `does_not_own[]`, and refs to inheritance / skills / identity files.

Default fail-closed values:

- `allowed_tools`: `[]` unless a separate human gate lists tools  
- `model_policy.provider`: `local_deterministic`  
- `model_policy.network_access`: `false`  
- `production_activation_requested`: `false`

---

## 6. Multiple inheritance

<div role="img" aria-label="Multiple inheritance DAG, MRO list, merge rules, and never-inherited fields">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 860" role="img" aria-labelledby="s3-t s3-d">
  <title id="s3-t">Multiple inheritance and method resolution order</title>
  <desc id="s3-d">Child agent inherits from multiple common-structure parents. MRO linearizes diamonds. Child wins. Safety tightens.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .card{fill:#FFFFFF;stroke:#CBD5E1;stroke-width:1.5}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .m{fill:#334155;font:400 11px ui-monospace,Menlo,Consolas,monospace}
      .sec{fill:#64748B;font:700 10px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;letter-spacing:1.2px}
      .child{fill:#1D4ED8;stroke:#1D4ED8}
      .p1{fill:#EFF6FF;stroke:#3B82F6;stroke-width:1.5}
      .p2{fill:#ECFDF5;stroke:#10B981;stroke-width:1.5}
      .p3{fill:#F5F3FF;stroke:#8B5CF6;stroke-width:1.5}
      .base{fill:#FFFBEB;stroke:#F59E0B;stroke-width:1.5}
      .no{fill:#FFF1F2;stroke:#FDA4AF;stroke-width:1.5}
    </style>
    <marker id="s3-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#64748B"/>
    </marker>
  </defs>
  <rect class="bg" width="100%" preserveAspectRatio="xMidYMid meet" width="1440" height="860"/>
  <text class="ink" x="40" y="42">Multiple inheritance — same common agent structure only</text>
  <text class="sub" x="40" y="66">Parents must be CASOPS common-structure agents. Inheritance is mixin of surfaces, not OOP subclassing of runtime objects.</text>

  <rect class="card" x="40" y="92" width="860" height="500" rx="16"/>
  <text class="sec" x="64" y="122">EXAMPLE DAG  ·  video.showrunner</text>

  <rect class="p1" x="80" y="148" width="240" height="64" rx="10"/>
  <text class="h" x="100" y="174">video.screenwriter</text>
  <text class="m" x="100" y="196">priority 20 · story craft</text>

  <rect class="p2" x="360" y="148" width="240" height="64" rx="10"/>
  <text class="h" x="380" y="174">video.director</text>
  <text class="m" x="380" y="196">priority 10 · vision / takes</text>

  <rect class="p3" x="640" y="148" width="220" height="64" rx="10"/>
  <text class="h" x="656" y="174">specials.aesthetics</text>
  <text class="m" x="656" y="196">priority 30 · taste mixin</text>

  <line x1="200" y1="212" x2="360" y2="268" stroke="#64748B" stroke-width="2" marker-end="url(#s3-arr)"/>
  <line x1="480" y1="212" x2="480" y2="268" stroke="#64748B" stroke-width="2" marker-end="url(#s3-arr)"/>
  <line x1="750" y1="212" x2="600" y2="268" stroke="#64748B" stroke-width="2" marker-end="url(#s3-arr)"/>

  <rect class="child" x="280" y="276" width="320" height="72" rx="12"/>
  <text class="h2" x="304" y="306">video.showrunner  (child)</text>
  <text class="h2" x="304" y="328" style="font-weight:400;font-size:12px">owns one agent_id · merges parents</text>

  <rect class="base" x="280" y="390" width="320" height="56" rx="10"/>
  <text class="h" x="300" y="414">video.producer  (optional deeper parent)</text>
  <text class="m" x="300" y="434">diamond: director also lists producer</text>
  <line x1="440" y1="348" x2="440" y2="388" stroke="#64748B" stroke-width="2" marker-end="url(#s3-arr)"/>
  <line x1="480" y1="212" x2="520" y2="390" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4 4"/>

  <rect class="no" x="80" y="468" width="780" height="100" rx="10"/>
  <text class="h" x="100" y="496">Not inheritance</text>
  <text class="b" x="100" y="520">Critique edges, workflow graph nodes, and special_skills bindings are composition.</text>
  <text class="b" x="100" y="544">A parent is valid only with SPEC.md + agent_spec.json in a common-structure folder.</text>

  <rect class="card" x="924" y="92" width="476" height="500" rx="16"/>
  <text class="sec" x="948" y="122">RESOLVED MRO (generated)</text>
  <text class="m" x="948" y="154">1. video.showrunner          child</text>
  <text class="m" x="948" y="180">2. video.director            prio 10</text>
  <text class="m" x="948" y="206">3. video.screenwriter        prio 20</text>
  <text class="m" x="948" y="232">4. specials.aesthetics-agent prio 30</text>
  <text class="m" x="948" y="258">5. video.producer            once</text>
  <rect class="p1" x="948" y="288" width="428" height="132" rx="10"/>
  <text class="h" x="968" y="316">Merge rules</text>
  <text class="b" x="968" y="340">Content lists: union, child first</text>
  <text class="b" x="968" y="364">Conflicting scalars: child wins</text>
  <text class="b" x="968" y="388">does_not_own: union (stricter)</text>
  <text class="b" x="968" y="400"></text>
  <rect class="no" x="948" y="436" width="428" height="132" rx="10"/>
  <text class="h" x="968" y="464">Never inherited</text>
  <text class="b" x="968" y="488">agent_id · credentials · secrets</text>
  <text class="b" x="968" y="512">allowed_tools (must be re-declared)</text>
  <text class="b" x="968" y="536">production_activation_requested</text>

  <rect class="card" x="40" y="612" width="1360" height="216" rx="16"/>
  <text class="sec" x="64" y="644">SURFACES THAT MAY BE INHERITED (explicit per parent)</text>
  <text class="b" x="64" y="676">responsibility_fragments   knowledge_sources   quality_criteria   prompt_refs   rubric_refs</text>
  <text class="b" x="64" y="704">skill_bindings (enabled union)   critique_edges (union)   architecture_pattern   persona_defaults (optional)</text>
  <text class="b" x="64" y="732">Each parent declares surfaces[]. Missing surface = not mixed in. Child SPEC.md remains the narrative source of truth;</text>
  <text class="b" x="64" y="756">inherited fragments are appended under SPEC.md ## Inherited from with agent_id + hash.</text>
  <text class="m" x="64" y="792">Fail closed: cycle, missing parent folder, structure mismatch, depth&gt;4, parents&gt;8, safety-field leak.</text>
</svg>
</div>

### 6.1 Definition

**Inheritance** means: at load time, the host **mixes declared surfaces** from other common-structure agents into the child’s compose envelope, using an explicit parent list and a deterministic MRO.

It is **not**:

- class inheritance of running objects  
- copying parent folders into the child  
- automatic tool or credential reuse  
- replacing the child’s `agent_id`

Critique edges, workflow graph nodes, and skill bindings to pack `special_skills` are **composition**. They are not parents unless listed in `parents.json`.

### 6.2 Functional requirements

| ID | Requirement |
|----|-------------|
| FR-INH-001 | A child MAY declare 0–8 parents in `inheritance/parents.json`. |
| FR-INH-002 | Each parent MUST be a common-structure agent on this host. |
| FR-INH-003 | Each parent entry MUST list a non-empty `surfaces[]`. Unlisted surfaces are not mixed. |
| FR-INH-004 | Each parent entry MUST have integer `priority` (lower number = earlier in MRO after the child). Ties broken by `agent_id` lexicographic ascending. |
| FR-INH-005 | The host MUST compute a linearized MRO, child first, each parent id at most once (diamond collapse). |
| FR-INH-006 | Max inheritance depth is 4 (child + three ancestor levels). Deeper graphs fail closed. |
| FR-INH-007 | Cycles fail closed (`INH_CYCLE`). |
| FR-INH-008 | Missing parent folder or SPEC fails closed (`INH_PARENT_MISSING`). |
| FR-INH-009 | Child content scalars override all parents. |
| FR-INH-010 | List surfaces union in MRO order, de-duplicated by stable key (ISBN, skill_id, agent_id, prompt_reference). |
| FR-INH-011 | `does_not_own` unions across child + parents (more restrictive). |
| FR-INH-012 | `allowed_tools` is **not** inherited. The child must re-declare any tool. Host allow-list still applies. |
| FR-INH-013 | `model_policy.network_access` and `production_activation_requested` AND across the MRO (false wins). |
| FR-INH-014 | `budget_policy` uses the **minimum** of each numeric cap across the MRO. |
| FR-INH-015 | `max_refinement_count` uses the **minimum** across the MRO (range still 1–3). |
| FR-INH-016 | Critique edges union; self-edges to the child are dropped. |
| FR-INH-017 | Generated `resolved.json` MUST include parent content hashes. Hand edits fail `INH_RESOLVED_DRIFT`. |
| FR-INH-018 | Inherited SPEC fragments MUST be quoted under `## Inherited from` with `agent_id` and hash, not silently inlined as if the child wrote them. |

### 6.3 Legal surfaces

| Surface key | Mix-in behaviour |
|-------------|------------------|
| `responsibility` | Parent mission sentences appended as “supports: …” — child mission stays first |
| `knowledge` | Union of distillation sources / local source refs |
| `quality` | Union of L2 dimension ids; child weights win on id clash |
| `prompts` | Parent prompt refs become `inherited_prompt_refs[]`; child `prompt_reference` stays primary |
| `rubrics` | Same as prompts with `inherited_rubric_refs[]` |
| `skills` | Union of skill bindings, then enable-AND (see §7) |
| `critique` | Union of critique edge ids |
| `architecture` | Child pattern wins; parents listed as `inherited_patterns[]` |
| `persona_defaults` | Used only if the child has no identity files |
| `docs` | Not mixed into runtime; optional authoring hint only |

Illegal surface names fail closed (`INH_SURFACE_UNKNOWN`).

### 6.4 `parents.json`

```json
{
  "schema_version": "1.0",
  "child_agent_id": "video.showrunner",
  "conflict_policy": "child_wins_then_priority",
  "parents": [
    {
      "agent_id": "video.director",
      "priority": 10,
      "mode": "mixin",
      "surfaces": ["responsibility", "knowledge", "quality", "prompts", "critique"]
    },
    {
      "agent_id": "video.screenwriter",
      "priority": 20,
      "mode": "mixin",
      "surfaces": ["knowledge", "prompts", "quality"]
    },
    {
      "agent_id": "specials.aesthetics-agent",
      "priority": 30,
      "mode": "mixin",
      "surfaces": ["knowledge", "quality", "skills"]
    }
  ]
}
```

`mode` is `mixin` only. `replace` is forbidden — it would erase child identity.

### 6.5 MRO algorithm

Given child `C` and parents sorted by `(priority, agent_id)`:

1. Start `mro = [C]`.  
2. For each parent `P` in that order, **depth-first**, append `P` if not already in `mro`, then walk `P`’s parents the same way.  
3. If adding `P` would re-visit an open recursion stack, emit `INH_CYCLE`.  
4. If unique parents > 8 or depth > 4, fail.  
5. Persist `mro` plus each folder’s `SPEC.md` and `agent_spec.json` sha256.

Pack authors who need a different order change `priority`. Diamonds collapse: each `agent_id` appears once.

### 6.6 Never inherited

- `agent_id`, `status` (the child’s own catalog row)  
- Credentials, secrets, API keys, cookie jars  
- `allowed_tools`  
- `production_activation_requested` (AND; a parent cannot flip it true)  
- Operator skill toggles of a parent (toggles are per-child)  
- Parent `identity/` named-person approvals  
- Improvement-plan bookkeeping unless the child copies it

---

## 7. Configurable skills

<div role="img" aria-label="Four-layer skill enable AND-gate">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 820" role="img" aria-labelledby="s4-t s4-d">
  <title id="s4-t">Configurable skill enable and disable</title>
  <desc id="s4-d">Skills resolve from local, inherited, and pack sources. Operator toggle can disable. Disabled skills never load. Host allow-list still wins.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .card{fill:#FFFFFF;stroke:#CBD5E1;stroke-width:1.5}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .m{fill:#334155;font:400 11px ui-monospace,Menlo,Consolas,monospace}
      .sec{fill:#64748B;font:700 10px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;letter-spacing:1.2px}
      .s1{fill:#EFF6FF;stroke:#93C5FD;stroke-width:1.5}
      .s2{fill:#ECFDF5;stroke:#86EFAC;stroke-width:1.5}
      .s3{fill:#F5F3FF;stroke:#C4B5FD;stroke-width:1.5}
      .on{fill:#065F46}
      .off{fill:#9F1239}
      .gate{fill:#0F172A}
    </style>
    <marker id="s4-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#64748B"/>
    </marker>
  </defs>
  <rect class="bg" width="1440" height="820"/>
  <text class="ink" x="40" y="42">Skill enable / disable — three layers, one resolved set</text>
  <text class="sub" x="40" y="66">A skill is loaded only if declared, inherited-or-local, enabled at every layer, and allowed by the host. Disabled means not present.</text>

  <rect class="s1" x="40" y="100" width="280" height="120" rx="12"/>
  <text class="h" x="60" y="132">L1  Declared</text>
  <text class="b" x="60" y="156">skills/bindings.json</text>
  <text class="b" x="60" y="176">local SKILL.md harness</text>
  <text class="m" x="60" y="200">enabled: true (default)</text>

  <rect class="s2" x="400" y="100" width="280" height="120" rx="12"/>
  <text class="h" x="420" y="132">L2  Inherited union</text>
  <text class="b" x="420" y="156">parent skill_bindings[]</text>
  <text class="b" x="420" y="176">same skill_id merged once</text>
  <text class="m" x="420" y="200">child enabled AND parent</text>

  <rect class="s3" x="760" y="100" width="280" height="120" rx="12"/>
  <text class="h" x="780" y="132">L3  Operator toggle</text>
  <text class="b" x="780" y="156">skills/toggles.json</text>
  <text class="b" x="780" y="176">run / session override</text>
  <text class="m" x="780" y="200">audit required</text>

  <rect class="gate" x="1120" y="100" width="280" height="120" rx="12"/>
  <text class="h2" x="1140" y="132">L4  Host gate</text>
  <text class="h2" x="1140" y="156" style="font-weight:400">allow-list · no network</text>
  <text class="h2" x="1140" y="176" style="font-weight:400">no undeclared tools</text>
  <text class="h2" x="1140" y="200" style="font-weight:400">fail closed</text>

  <line x1="320" y1="160" x2="400" y2="160" stroke="#64748B" stroke-width="2" marker-end="url(#s4-arr)"/>
  <line x1="680" y1="160" x2="760" y2="160" stroke="#64748B" stroke-width="2" marker-end="url(#s4-arr)"/>
  <line x1="1040" y1="160" x2="1120" y2="160" stroke="#64748B" stroke-width="2" marker-end="url(#s4-arr)"/>

  <rect class="card" x="40" y="252" width="680" height="520" rx="16"/>
  <text class="sec" x="64" y="284">RESOLUTION  (AND, left to right)</text>
  <text class="m" x="64" y="316">resolved_enabled =</text>
  <text class="m" x="64" y="340">  declared.exists</text>
  <text class="m" x="64" y="364">  AND declared.enabled</text>
  <text class="m" x="64" y="388">  AND inherited.enabled   (if inherited)</text>
  <text class="m" x="64" y="412">  AND toggle.enabled      (default true)</text>
  <text class="m" x="64" y="436">  AND host.permits(skill)</text>
  <rect class="s2" x="64" y="464" width="632" height="88" rx="10"/>
  <text class="h" x="84" y="492">ON  — skill loads</text>
  <text class="b" x="84" y="516">SKILL.md, prompt extras, rubric extras, tool intents</text>
  <text class="b" x="84" y="536">enter the compose envelope. Provenance records skill_id.</text>
  <rect class="s3" x="64" y="568" width="632" height="88" rx="10"/>
  <text class="h" x="84" y="596">OFF — skill is absent</text>
  <text class="b" x="84" y="620">Must not appear in prompt, memory, tools, or critique.</text>
  <text class="b" x="84" y="640">No silent fallback to a parent’s copy of the same skill.</text>
  <text class="b" x="64" y="748">Precedence of OFF: operator toggle &gt; child declaration &gt; parent.</text>

  <rect class="card" x="744" y="252" width="656" height="520" rx="16"/>
  <text class="sec" x="768" y="284">EXAMPLE  ·  video.orchestrator</text>
  <text class="m" x="768" y="316">skill_id                         L1   L2   L3   L4   load</text>
  <text class="m" x="768" y="348">agent_loop_v3                    on   on   on   ok    YES</text>
  <text class="m" x="768" y="372">complex_problem_…                on   on   on   ok    YES</text>
  <text class="m" x="768" y="396">llm_usage                        on   —    off  ok    NO</text>
  <text class="m" x="768" y="420">aesthetics_agent                 —    on   on   ok    YES*</text>
  <text class="b" x="768" y="452">* inherited from parent mixin; still host-gated.</text>
  <rect class="gate" x="768" y="480" width="608" height="120" rx="10"/>
  <text class="h2" x="788" y="512">API (functional, not activating)</text>
  <text class="h2" x="788" y="536" style="font-weight:400">PATCH /agents/{id}/skills/{skill_id}</text>
  <text class="h2" x="788" y="560" style="font-weight:400">body: { enabled, reason, actor }</text>
  <text class="h2" x="788" y="584" style="font-weight:400">GET  /agents/{id}/skills/resolved</text>
  <rect class="s1" x="768" y="620" width="608" height="124" rx="10"/>
  <text class="h" x="788" y="648">Invariants</text>
  <text class="b" x="788" y="672">Unknown skill_id → fail closed (do not ignore).</text>
  <text class="b" x="788" y="696">Toggle cannot enable a skill that is not declared or inherited.</text>
  <text class="b" x="788" y="720">Enabling never adds tools outside agent_spec.allowed_tools.</text>
</svg>
</div>

### 7.1 Skill kinds

| Kind | Where | Example |
|------|-------|---------|
| Local harness | `skills/SKILL.md` | `video-director` |
| Pack special skill | pack `special_skills/<id>/` | `agent_loop_v3` |
| Inherited skill | Parent `skills` surface | parent’s `llm_usage` bind |

### 7.2 Enable layers (AND)

```
resolved_enabled(skill) =
    exists_in_declared_or_inherited(skill)
AND declared.enabled          # default true if declared
AND inherited.enabled         # default true if inherited; AND across parents that list it
AND toggle.enabled            # default true if no toggle row
AND host.permits(skill)
```

OFF at any layer → the skill is **absent**.

### 7.3 Functional requirements

| ID | Requirement |
|----|-------------|
| FR-SKL-001 | Every binding object SHALL include `skill_id`, `source` (`local` \| `pack` \| `inherited`), `path`, `enabled` (boolean). |
| FR-SKL-002 | A binding without `enabled` defaults to `true`. |
| FR-SKL-003 | Operator MAY set `skills/toggles.json` entries `{ skill_id, enabled, reason, actor, at }`. |
| FR-SKL-004 | A toggle cannot enable a skill that is not declared or inherited (`SKL_TOGGLE_UNKNOWN`). |
| FR-SKL-005 | Enabling a skill MUST NOT add tools outside `agent_spec.allowed_tools`. |
| FR-SKL-006 | Disabled skills MUST NOT appear in the prompt envelope, tool loop, memory injection, or critique prompts. |
| FR-SKL-007 | Resolved skill set is recorded on every artifact (`skills_loaded[]`, `skills_disabled[]`). |
| FR-SKL-008 | Duplicate `skill_id` across local + parents collapses to one row; enabled AND. |
| FR-SKL-009 | Host unknown `skill_id` (not in pack registry and not local) fails closed. |
| FR-SKL-010 | Skill load is fail-closed if `SKILL.md` or `integration.json` is missing when enabled. |

### 7.4 `bindings.json`

```json
{
  "agent_id": "video.orchestrator",
  "special_skills": [
    {
      "skill_id": "agent_loop_v3",
      "source": "pack",
      "path": "special_skills/agent_loop_v3/",
      "enabled": true
    },
    {
      "skill_id": "llm_usage",
      "source": "pack",
      "path": "special_skills/llm_usage/",
      "enabled": false,
      "reason": "cost ledger not needed on this spine run"
    }
  ]
}
```

### 7.5 `toggles.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.orchestrator",
  "toggles": [
    {
      "skill_id": "llm_usage",
      "enabled": false,
      "reason": "operator: hide costs panel for this rehearsal",
      "actor": "operator:local",
      "at": "2026-08-17T12:00:00Z"
    }
  ]
}
```

Author `enabled: false` is the floor. A toggle cannot resurrect a skill the child SPEC turned off. A toggle OFF hides a declared ON skill.

Precedence of OFF:

1. Host deny  
2. Child declaration `enabled: false`  
3. Operator toggle `enabled: false`  
4. Inherited `enabled: false`

---

## 8. Identity: personality and professional background

<div role="img" aria-label="Persona, professional background, grounded craft, and hard stops">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 860" role="img" aria-labelledby="s5-t s5-d">
  <title id="s5-t">Persona and professional background overlay</title>
  <desc id="s5-d">Personality and professional background frame how the agent speaks. Grounded SPEC knowledge remains the only source of craft claims unless disclosed as persona.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .card{fill:#FFFFFF;stroke:#CBD5E1;stroke-width:1.5}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .m{fill:#334155;font:400 11px ui-monospace,Menlo,Consolas,monospace}
      .sec{fill:#64748B;font:700 10px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;letter-spacing:1.2px}
      .g{fill:#ECFDF5;stroke:#86EFAC;stroke-width:1.5}
      .a{fill:#FFFBEB;stroke:#FCD34D;stroke-width:1.5}
      .p{fill:#F5F3FF;stroke:#C4B5FD;stroke-width:1.5}
      .r{fill:#FFF1F2;stroke:#FDA4AF;stroke-width:1.5}
      .n{fill:#0F172A}
    </style>
  </defs>
  <rect class="bg" width="100%" preserveAspectRatio="xMidYMid meet" width="1440" height="860"/>
  <text class="ink" x="40" y="42">Identity — personality + professional background (expertise overlay)</text>
  <text class="sub" x="40" y="66">The agent may speak as a craft professional. That is framing. It is not a credential, not a living person, and not a substitute for SPEC knowledge.</text>

  <rect class="p" x="40" y="96" width="430" height="280" rx="14"/>
  <text class="h" x="60" y="124">persona.json  ·  personality</text>
  <text class="b" x="60" y="152">display_name, voice, register</text>
  <text class="b" x="60" y="176">temperament (optional Big Five / MBTI)</text>
  <text class="b" x="60" y="200">values, taboos, humor, pacing</text>
  <text class="b" x="60" y="224">language (en / zh-Hant / zh-Hans)</text>
  <text class="m" x="60" y="256">example: calm 1st AD, terse, night-shoot</text>
  <text class="m" x="60" y="276">veteran; swears rarely; protective of crew</text>
  <text class="b" x="60" y="312">Affects tone only unless mixed with</text>
  <text class="b" x="60" y="332">background.specialties.</text>

  <rect class="a" x="490" y="96" width="450" height="280" rx="14"/>
  <text class="h" x="510" y="124">background.json  ·  profession</text>
  <text class="b" x="510" y="152">title, years_practice (fictional range)</text>
  <text class="b" x="510" y="176">domain, specialties[], union_style</text>
  <text class="b" x="510" y="200">education_style (school-type, not a real diploma)</text>
  <text class="b" x="510" y="224">credits_style (genre / scale, not fake IMDb)</text>
  <text class="b" x="510" y="248">methods[]  (how this persona works)</text>
  <text class="m" x="510" y="280">example: “feature DP, handheld night exteriors,</text>
  <text class="m" x="510" y="300">available-light advocate, 15–20 years style”</text>
  <text class="b" x="510" y="336">MUST set fictional: true unless provenance-linked.</text>

  <rect class="g" x="960" y="96" width="440" height="280" rx="14"/>
  <text class="h" x="980" y="124">Grounded craft (always primary)</text>
  <text class="b" x="980" y="152">SPEC.md ## Responsibility</text>
  <text class="b" x="980" y="176">sources/ + domain knowledge list</text>
  <text class="b" x="980" y="200">rubric L2 dimensions</text>
  <text class="b" x="980" y="224">inherited knowledge fragments</text>
  <text class="b" x="980" y="248">evals / golden tasks</text>
  <text class="m" x="980" y="284">Persona must not invent shots, laws,</text>
  <text class="m" x="980" y="304">medical facts, or rights grants.</text>
  <text class="b" x="980" y="336">Ungrounded craft claims → tag + fail closed.</text>

  <rect class="n" x="40" y="400" width="1360" height="72" rx="12"/>
  <text class="h2" x="64" y="430">expertise_mode = grounded  |  persona_overlay  |  mixed</text>
  <text class="h2" x="64" y="454" style="font-weight:400">Every output carries expertise_mode + disclosure_id. Mixed = persona frames; citations stay grounded.</text>

  <rect class="card" x="40" y="492" width="680" height="332" rx="16"/>
  <text class="sec" x="64" y="524">WHAT “PRETEND DOMAIN EXPERTISE” MEANS</text>
  <text class="b" x="64" y="552">Allowed: speak in the register of the chosen professional</text>
  <text class="b" x="64" y="576">background; prefer that craft’s methods and vocabulary;</text>
  <text class="b" x="64" y="600">use inherited + local SPEC knowledge as the facts.</text>
  <text class="b" x="64" y="632">Not allowed: claim to be a named living person; claim a</text>
  <text class="b" x="64" y="656">real license, union card, medical degree, or legal standing;</text>
  <text class="b" x="64" y="680">raise eval scores solely because the persona “sounds sure”;</text>
  <text class="b" x="64" y="704">override does_not_own, rights, or HiTL gates.</text>
  <text class="m" x="64" y="740">disclosure example:</text>
  <text class="m" x="64" y="764">“Role-play: fictional feature DP overlay. Craft steps</text>
  <text class="m" x="64" y="784">are from video.cinematographer SPEC + sources, not a human credit.”</text>

  <rect class="r" x="744" y="492" width="656" height="332" rx="16"/>
  <text class="sec" x="768" y="524">HARD STOPS</text>
  <text class="b" x="768" y="552">1. Impersonating a real named professional without</text>
  <text class="b" x="768" y="576">   a recorded human approval + provenance hash.</text>
  <text class="b" x="768" y="604">2. Persona granting tools or network_access.</text>
  <text class="b" x="768" y="632">3. Medical, legal, financial advice presented as licensed.</text>
  <text class="b" x="768" y="660">4. Child-safety, biometric, or deepfake identity play.</text>
  <text class="b" x="768" y="688">5. Hiding expertise_mode from operators or artifacts.</text>
  <text class="b" x="768" y="716">6. Using personality psychology of a real user as the</text>
  <text class="b" x="768" y="740">   agent’s own persona without consent (profile agent</text>
  <text class="b" x="768" y="764">   remains a separate specials role).</text>
</svg>
</div>

### 8.1 Intent

The agent may **pretend domain expertise**: it answers in the voice and method of a chosen professional background (feature DP, comedy showrunner, bilingual 1st AD, research librarian).

That overlay is **framing**. Grounded craft remains SPEC + sources + enabled skills + evals.

### 8.2 Modes

| `expertise_mode` | Behaviour |
|------------------|-----------|
| `grounded` | No persona. Default when identity files are absent. |
| `persona_overlay` | Voice + background framing. Craft claims still require SPEC/source grounding; ungrounded claims tagged `persona_claim`. |
| `mixed` | Persona frames; every craft step cites a grounded fragment. Preferred for production-adjacent rehearsal. |

### 8.3 Functional requirements

| ID | Requirement |
|----|-------------|
| FR-IDN-001 | Identity files are optional. Missing files ⇒ `expertise_mode=grounded`. |
| FR-IDN-002 | `persona.json` MAY include display_name, voice, register, temperament, values, taboos, languages[]. |
| FR-IDN-003 | `background.json` MAY include title, domain, specialties[], years_practice_range, methods[], education_style, credits_style. |
| FR-IDN-004 | `background.fictional` MUST be `true` unless a provenance-linked human approval names a real person. |
| FR-IDN-005 | Real named-person personas require `approvals.named_person_id` + hash; otherwise `IDN_NAMED_PERSON`. |
| FR-IDN-006 | Persona MUST NOT set tools, network, budgets, or production_activation. |
| FR-IDN-007 | When mode is not `grounded`, every artifact and operator view SHALL show `disclosure_id` and a short banner from `DISCLOSURE.md`. |
| FR-IDN-008 | Craft statements without a SPEC/source/eval citation SHALL be tagged `persona_claim` and MUST NOT be used as L1 pass evidence. |
| FR-IDN-009 | Persona MUST NOT claim a real license, union card, medical degree, bar admission, or financial-advisor status (`IDN_LICENSE_CLAIM`). |
| FR-IDN-010 | Child identity overrides `persona_defaults` inherited from parents. |
| FR-IDN-011 | A user’s psychological profile is not auto-copied into the agent’s own persona. |
| FR-IDN-012 | Languages listed constrain output locale pairing (en / zh-Hant / zh-Hans) but do not invent a third locale. |

### 8.4 `persona.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.director",
  "display_name": "Floor director (rehearsal voice)",
  "voice": "calm, short sentences, crew-protective",
  "register": "set-floor",
  "temperament": {
    "openness": "high",
    "conscientiousness": "high",
    "extraversion": "medium",
    "agreeableness": "medium",
    "neuroticism": "low"
  },
  "values": ["safety", "continuity", "no hero-lighting on exhausted talent"],
  "taboos": ["named living-person impersonation", "rights waivers"],
  "languages": ["en", "zh-Hant"],
  "humor": "dry, rare"
}
```

Temperament keys are optional prompt labels, not a clinical instrument.

### 8.5 `background.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.director",
  "fictional": true,
  "title": "Feature + documentary director",
  "domain": "video",
  "specialties": ["available light", "street vlog blocking", "actor-first coverage"],
  "years_practice_range": "12-18",
  "education_style": "conservatory-like craft school (fictional)",
  "credits_style": "mid-budget narrative and travel documentary (fictional)",
  "methods": [
    "master → coverage → insert",
    "protect the sit-hour",
    "call cut when the feeling is already on disk"
  ],
  "expertise_mode": "mixed"
}
```

### 8.6 Disclosure

`identity/DISCLOSURE.md` minimum when mode is not `grounded`:

```markdown
# Overlay disclosure
This agent is **role-playing** a fictional professional background.
Craft procedures come from this folder’s SPEC.md, inherited common-structure
parents, and enabled skills — not from a human credit, license, or diploma.
expertise_mode: mixed
```

The host injects a one-line banner into the operator UI and artifact metadata.

### 8.7 How pretend expertise is built

1. System prompt gains a **Voice** block from persona.  
2. System prompt gains a **Method preference** block from `background.methods`.  
3. System prompt keeps **Owns / Does not own** from the child SPEC (plus inherited supports).  
4. Developer prompt adds: “If you would only know this as the persona and not from SPEC/sources, mark `persona_claim`.”  
5. Judge rubric gains dimension `d_disclosure` (must_pass if mode is not `grounded`).

The overlay can make the agent *sound* like a DP. It cannot make an ungrounded ISO/lens prescription pass L1.

---

## 9. Merge and compose algorithm

<div role="img" aria-label="Six-step fail-closed compose order from identity to run">
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1440 820" role="img" aria-labelledby="s6-t s6-d">
  <title id="s6-t">Runtime compose order for a common agent</title>
  <desc id="s6-d">Load identity, resolve inheritance MRO, resolve skills, bind host gates, then run Plan-Act-Self-Review with disclosure on every artifact.</desc>
  <defs>
    <style>
      .bg{fill:#F8FAFC}
      .card{fill:#FFFFFF;stroke:#CBD5E1;stroke-width:1.5}
      .ink{fill:#0F172A;font:700 24px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .sub{fill:#475569;font:400 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h{fill:#0F172A;font:700 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .h2{fill:#FFFFFF;font:700 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .b{fill:#334155;font:400 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
      .m{fill:#334155;font:400 11px ui-monospace,Menlo,Consolas,monospace}
      .sec{fill:#64748B;font:700 10px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;letter-spacing:1.2px}
      .st{fill:#1D4ED8}
      .ok{fill:#ECFDF5;stroke:#86EFAC;stroke-width:1.5}
      .no{fill:#FFF1F2;stroke:#FDA4AF;stroke-width:1.5}
    </style>
    <marker id="s6-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#64748B"/>
    </marker>
  </defs>
  <rect class="bg" width="1440" height="820"/>
  <text class="ink" x="40" y="42">Runtime compose — fail-closed load order</text>
  <text class="sub" x="40" y="66">Host loads one child folder. Parents are referenced, not copied. Any step may abort the run. Production activation stays a separate human gate.</text>

  <rect class="st" x="40" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="56" y="130">1  Identity</text>
  <text class="h2" x="56" y="150" style="font-weight:400">persona + background</text>
  <rect class="st" x="280" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="296" y="130">2  Parents</text>
  <text class="h2" x="296" y="150" style="font-weight:400">validate + MRO</text>
  <rect class="st" x="520" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="536" y="130">3  Merge</text>
  <text class="h2" x="536" y="150" style="font-weight:400">surfaces + conflicts</text>
  <rect class="st" x="760" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="776" y="130">4  Skills</text>
  <text class="h2" x="776" y="150" style="font-weight:400">AND enable path</text>
  <rect class="st" x="1000" y="100" width="200" height="70" rx="10"/>
  <text class="h2" x="1016" y="130">5  Host gates</text>
  <text class="h2" x="1016" y="150" style="font-weight:400">tools / net / budget</text>
  <rect class="st" x="1240" y="100" width="160" height="70" rx="10"/>
  <text class="h2" x="1256" y="130">6  Run</text>
  <text class="h2" x="1256" y="150" style="font-weight:400">P→A→R + disclose</text>

  <line x1="240" y1="135" x2="280" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#s6-arr)"/>
  <line x1="480" y1="135" x2="520" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#s6-arr)"/>
  <line x1="720" y1="135" x2="760" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#s6-arr)"/>
  <line x1="960" y1="135" x2="1000" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#s6-arr)"/>
  <line x1="1200" y1="135" x2="1240" y2="135" stroke="#64748B" stroke-width="2" marker-end="url(#s6-arr)"/>

  <rect class="card" x="40" y="196" width="880" height="580" rx="16"/>
  <text class="sec" x="64" y="228">PER-STEP CONTRACT</text>
  <text class="h" x="64" y="260">1 Identity</text>
  <text class="b" x="64" y="282">If identity/ missing → expertise_mode=grounded. Invalid persona → abort.</text>
  <text class="h" x="64" y="314">2 Parents</text>
  <text class="b" x="64" y="336">Each parent_id resolves to a folder with SPEC.md + agent_spec.json.</text>
  <text class="b" x="64" y="356">Same structure family. No cycles. Depth ≤ 4. Count ≤ 8.</text>
  <text class="h" x="64" y="388">3 Merge</text>
  <text class="b" x="64" y="410">Write inheritance/resolved.json and conflicts.json (generated).</text>
  <text class="b" x="64" y="430">Child scalars win. Lists union. does_not_own unions. Tools not copied.</text>
  <text class="h" x="64" y="462">4 Skills</text>
  <text class="b" x="64" y="484">Compute resolved_enabled. OFF skills omitted from envelope.</text>
  <text class="h" x="64" y="516">5 Host gates</text>
  <text class="b" x="64" y="538">allowed_tools ∩ host register. network_access remains false unless</text>
  <text class="b" x="64" y="558">a separate human gate changes agent_spec (this spec does not).</text>
  <text class="h" x="64" y="590">6 Run</text>
  <text class="b" x="64" y="612">Prompt envelope = identity + child SPEC + inherited fragments +</text>
  <text class="b" x="64" y="632">enabled skills. Self-Refine ≤ max_refinement_count. Critique bus</text>
  <text class="b" x="64" y="652">uses merged edges. Every artifact: provenance, MRO, skill set,</text>
  <text class="b" x="64" y="672">expertise_mode, disclosure_id.</text>
  <text class="m" x="64" y="712">Envelope never includes disabled skill text or parent secrets.</text>
  <text class="m" x="64" y="736">Child does_not_own still blocks owning another agent’s exclusive craft.</text>

  <rect class="ok" x="944" y="196" width="456" height="268" rx="16"/>
  <text class="h" x="964" y="228">Pass conditions</text>
  <text class="b" x="964" y="256">MRO stable vs parent hashes</text>
  <text class="b" x="964" y="280">All enabled skills exist on disk</text>
  <text class="b" x="964" y="304">Disclosure present when not grounded</text>
  <text class="b" x="964" y="328">L1 schema validates</text>
  <text class="b" x="964" y="352">No extra tools from parents</text>
  <text class="b" x="964" y="376">Critique JSON matches schema</text>
  <text class="b" x="964" y="400">production_activation_requested false</text>
  <text class="b" x="964" y="424">unless separate human gate</text>
  <rect class="no" x="944" y="484" width="456" height="292" rx="16"/>
  <text class="h" x="964" y="516">Abort (fail closed)</text>
  <text class="b" x="964" y="544">Cycle or missing parent folder</text>
  <text class="b" x="964" y="568">Parent not common-structure</text>
  <text class="b" x="964" y="592">Toggle enables unknown skill</text>
  <text class="b" x="964" y="616">Named-person impersonation</text>
  <text class="b" x="964" y="640">Persona claims a real license</text>
  <text class="b" x="964" y="664">Hand-edited resolved.json drift</text>
  <text class="b" x="964" y="688">Network/tool grant via inherit</text>
  <text class="b" x="964" y="712">Hidden expertise_mode</text>
  <text class="b" x="964" y="736">Rights / medical / legal overclaim</text>
</svg>
</div>

### 9.1 Load order

1. **Identity** — read persona/background; default `grounded`.  
2. **Parents** — validate folders, structure family, cycles, depth.  
3. **Merge** — MRO, write `resolved.json` + `conflicts.json`.  
4. **Skills** — AND-enable path.  
5. **Host gates** — tools, network, budget, production flag.  
6. **Run** — Plan → Act → Self-Review ≤ `max_refinement_count`, critique bus, disclose.

Any step may abort. See §14.

### 9.2 Envelope construction

Prompt envelope layers, top to bottom:

1. Host fail-closed charter (no extra tools, no network unless gated).  
2. Disclosure banner if required.  
3. Persona voice (if any).  
4. Child `## Responsibility` and `does_not_own`.  
5. Inherited `supports:` fragments in MRO order.  
6. Enabled skill instructions (`SKILL.md` bodies).  
7. Child primary prompt.  
8. Inherited prompt refs as labelled appendices.  
9. Rubric ids for self-score.

Disabled skill files are not opened.

### 9.3 Conflict log

`conflicts.json` records every scalar clash:

```json
{
  "field": "prompt_reference",
  "winner": "video.showrunner",
  "losers": ["video.director"],
  "policy": "child_wins_then_priority"
}
```

Conflicts are evidence, not errors.

### 9.4 Parallel runs

Two children may inherit the same parent concurrently. Parents are read-only. No write-back into parent folders.

---

## 10. Data model

### 10.1 `agent_spec.json`

```json
{
  "schema_version": "1.0",
  "structure_id": "casops.common_agent",
  "agent_id": "video.showrunner",
  "status": "registered",
  "role": "ShowrunnerAgent (VA Domain Pack)",
  "allowed_tools": [],
  "model_policy": {
    "provider": "local_deterministic",
    "model_id": "local-video-config",
    "network_access": false
  },
  "budget_policy": {
    "max_input_tokens": 2048,
    "max_output_tokens": 1024,
    "max_tool_requests": 0
  },
  "prompt_reference": "video.prompt.showrunner",
  "rubric_reference": "video.rubric.showrunner",
  "critique_edges": {
    "inputs": ["video.critic"],
    "outputs": ["video.judge"]
  },
  "max_refinement_count": 3,
  "production_activation_requested": false,
  "does_not_own": [
    "Host credential storage",
    "Silent production activation without fail-closed gates",
    "Owning other agents' exclusive craft outputs without handoff contract"
  ],
  "inheritance_ref": "inheritance/parents.json",
  "identity_ref": "identity/",
  "skills_ref": "skills/bindings.json",
  "toggles_ref": "skills/toggles.json"
}
```

### 10.2 Artifact extras (every output)

| Field | Type | Notes |
|-------|------|-------|
| `agent_id` | string | Child |
| `mro` | string[] | Resolved |
| `parent_hashes` | object | agent_id → sha256 |
| `skills_loaded` | string[] | |
| `skills_disabled` | string[] | |
| `expertise_mode` | enum | `grounded` \| `persona_overlay` \| `mixed` |
| `disclosure_id` | string \| null | Required if not grounded |
| `persona_claim_count` | integer | |
| `correlation_id` | string | Host run id |

### 10.3 Critique message

Inter-agent critique stays the existing critique-message contract. Sender and receiver are **running** identities (children), not parent mixins.

---

## 11. Runtime behaviour

### 11.1 Catalog vs run

| State | Meaning |
|-------|---------|
| `draft` | Data-only catalog. Inheritance still resolves for offline review. |
| `registered` | Catalogued, non-active. Same compose rules. |
| production active | **Out of band.** This spec never sets it true. |

### 11.2 Self-refine

Uses **merged** `max_refinement_count` (minimum on the MRO). Critique is JSON. Judge is the child’s `outputs[]` (typically `video.judge`).

### 11.3 Memory

Inherited knowledge is referenced by parent `agent_id` + hash, not copied into the child’s long-term memory by default. Pack setting `inheritance.copy_knowledge_into_child_memory` defaults to `false`.

### 11.4 Eval interaction

| Layer | Persona effect |
|-------|----------------|
| L1 schema / policy | None. Overlay cannot skip validators. |
| L2 rubric | Overlay may change wording; scores still against child + inherited dimensions. `persona_claim` lines score 0 on factual dimensions. |
| L3 preference | Overlay may change style pairwise tests; must be labelled so raters know it is role-play. |

---

## 12. Operator and host APIs

Functional routes on the existing FastAPI control plane. They do not imply a second product API.

| Method | Path | Body / result |
|--------|------|----------------|
| GET | `/api/v1/agents/{id}/structure` | `{ structure_id }` |
| GET | `/api/v1/agents/{id}/resolved` | MRO, merged scalars, skills_loaded, expertise_mode |
| GET | `/api/v1/agents/{id}/inheritance` | parents.json + resolved.json + conflicts.json |
| PUT | `/api/v1/agents/{id}/inheritance/parents` | Authoring; rebuilds resolved; dry-run default |
| GET | `/api/v1/agents/{id}/skills/resolved` | Binding × toggle × host |
| PATCH | `/api/v1/agents/{id}/skills/{skill_id}` | `{ enabled, reason }` → toggles.json + audit |
| GET | `/api/v1/agents/{id}/identity` | persona, background, disclosure, mode |
| PUT | `/api/v1/agents/{id}/identity` | Validates fictional / named-person rules |
| POST | `/api/v1/agents/{id}/compose-preview` | Envelope dump, no model call (dry-run) |

All mutating calls: fail closed without operator identity, append-only audit, no production_activation flip.

Dry-run compose-preview is mandatory in CI for every agent with parents.

---

## 13. Honesty, safety, and fail-closed rules

### 13.1 Inheritance safety

- Parents cannot grant tools, network, or production activation.  
- Union of `does_not_own` is the runtime deny list.  
- Child cannot inherit a parent that is not loadable offline.  
- Design-time vendor names in parent SPECs remain untrusted provenance.

### 13.2 Skill safety

- Disabled skill = not loaded.  
- Enable ≠ tool grant.  
- Pack special_skills still require a separate host approval before any real tool bind.

### 13.3 Persona safety

- Fictional by default.  
- No named living person without approval hash.  
- No license claims.  
- No medical / legal / financial advice as if licensed.  
- No child-safety, biometric, or deepfake identity play.  
- Disclosure always on when not grounded.  
- User psychological profiles are not the agent’s persona.

### 13.4 Host invariants

- `provider: local_deterministic` unless a later human gate says otherwise.  
- `network_access: false` unless that same class of gate.  
- FastAPI remains the only public control plane.  
- Domain logic stays inside the domain pack.

---

## 14. Error catalogue

| Code | When | Operator sees |
|------|------|----------------|
| `INH_CYCLE` | Parent graph cycles | Load aborted; cycle path listed |
| `INH_PARENT_MISSING` | Folder / SPEC / agent_spec absent | Missing path |
| `INH_STRUCTURE_MISMATCH` | Parent not common-structure | Parent id |
| `INH_DEPTH` | Depth > 4 | Truncated MRO |
| `INH_PARENT_LIMIT` | Unique parents > 8 | Count |
| `INH_SURFACE_UNKNOWN` | Illegal surface key | Key |
| `INH_SELF_PARENT` | Parent == child | id |
| `INH_RESOLVED_DRIFT` | Hand-edited resolved.json | Hash diff |
| `SKL_TOGGLE_UNKNOWN` | Toggle on undeclared skill | skill_id |
| `SKL_MISSING_FILES` | Enabled skill lacks SKILL.md | path |
| `SKL_TOOL_LEAK` | Skill would add undeclared tool | tool name |
| `IDN_NAMED_PERSON` | Real name without approval | name token |
| `IDN_LICENSE_CLAIM` | License / degree claim | field |
| `IDN_DISCLOSURE_MISSING` | Overlay on, no DISCLOSURE.md | — |
| `GATE_NETWORK` | Inherited or overlay tried to set network true | — |
| `GATE_ACTIVATION` | Attempt to inherit production true | — |

All of these are **fail closed**. None are warnings that still run.

---

## 15. Acceptance criteria

### 15.1 Structure

| ID | Criterion | Proof |
|----|-----------|-------|
| AC-STR-001 | Required files in §4.2 exist | directory check |
| AC-STR-002 | Empty parents + no identity compose from child files only | golden envelope |
| AC-STR-003 | `structure_id` round-trips in GET `/structure` | API test, no network |

### 15.2 Inheritance

| ID | Criterion | Proof |
|----|-----------|-------|
| AC-INH-001 | Two parents mix knowledge lists without duplicating keys | fixture |
| AC-INH-002 | Diamond parent appears once in MRO | fixture |
| AC-INH-003 | Cycle aborts with `INH_CYCLE` | fixture |
| AC-INH-004 | Child prompt_reference survives parent clash | conflicts.json |
| AC-INH-005 | Parent allowed_tools do not appear on child | compose-preview |
| AC-INH-006 | `does_not_own` is the union | merge fixture |
| AC-INH-007 | Cross-pack parent (video → specials) loads if both common-structure | fixture |
| AC-INH-008 | Non-structure path rejected | `INH_STRUCTURE_MISMATCH` |

### 15.3 Skills

| ID | Criterion | Proof |
|----|-----------|-------|
| AC-SKL-001 | Declared `enabled:false` omits SKILL.md from envelope | compose-preview |
| AC-SKL-002 | Toggle OFF omits skill even if declared ON | preview |
| AC-SKL-003 | Toggle ON cannot enable undeclared skill | `SKL_TOGGLE_UNKNOWN` |
| AC-SKL-004 | Inherited skill AND-disabled if any parent disables and child does not re-enable via declaration | fixture |
| AC-SKL-005 | Artifact lists skills_loaded / skills_disabled | JSON schema |

### 15.4 Identity

| ID | Criterion | Proof |
|----|-----------|-------|
| AC-IDN-001 | Missing identity ⇒ grounded, no banner | preview |
| AC-IDN-002 | mixed mode injects disclosure banner | preview |
| AC-IDN-003 | Named person without approval aborts | `IDN_NAMED_PERSON` |
| AC-IDN-004 | Persona cannot flip network_access | `GATE_NETWORK` |
| AC-IDN-005 | Ungrounded craft line tagged `persona_claim` | unit on envelope post-process |
| AC-IDN-006 | L1 still fails invalid schema even if persona “sounds sure” | eval |

### 15.5 Safety

| ID | Criterion |
|----|-----------|
| AC-SEC-001 | `production_activation_requested` remains false through inherit |
| AC-SEC-002 | No second control plane in any new API |
| AC-SEC-003 | Offline compose-preview requires no network |

---

## 16. Worked example

**Child:** `video.showrunner`  
**Parents:** `video.director` (prio 10), `video.screenwriter` (prio 20), `specials.aesthetics-agent` (prio 30)  
**Skills:** local showrunner harness ON; pack `agent_loop_v3` ON; pack `llm_usage` OFF  
**Identity:** mixed; fictional “series showrunner, writers’-room first, 10–15 year style”; languages en + zh-Hant

### 16.1 MRO

1. `video.showrunner`  
2. `video.director`  
3. `video.screenwriter`  
4. `specials.aesthetics-agent`

### 16.2 Envelope

- Disclosure: mixed / fictional series showrunner  
- Owns: showrunner mission from child SPEC  
- Supports: director vision/takes; screenwriter story craft; aesthetics taste notes  
- Prompts: child primary; director + screenwriter as labelled appendices  
- Skills: showrunner SKILL.md + `agent_loop_v3` only  
- Tools: still `[]` unless the child re-declares and the host allows  
- `does_not_own`: union of all four

### 16.3 Must not

- Call itself a living showrunner  
- Enable Resolve / Sora because a parent SPEC mentions them  
- Load `llm_usage` while toggled off  
- Own editor cuts without a handoff (`does_not_own`)

---

## 17. Traceability

| Need | FR | AC | Diagram |
|------|----|----|---------|
| Self-contained folder | §4 | AC-STR-001 | 01 |
| Three compose surfaces | §1, P1 | AC-STR-002 | 02 |
| Multiple inheritance | FR-INH-001–018 | AC-INH-001–008 | 03 |
| Skill enable/disable | FR-SKL-001–010 | AC-SKL-001–005 | 04 |
| Persona / background | FR-IDN-001–012 | AC-IDN-001–006 | 05 |
| Compose order | §9 | AC-SEC-003 | 06 |
| No tool inherit | FR-INH-012, FR-SKL-005 | AC-INH-005 | 03, 04, 06 |
| Disclosure | FR-IDN-007 | AC-IDN-002 | 05 |

---

## 18. Open risks

| Risk | Mitigation |
|------|------------|
| Prompt envelope grows past budget after mixins | `budget_policy` uses min caps; compose-preview fails if over `max_input_tokens` |
| Authors list too many parents as a “god agent” | Hard cap 8; depth 4; `does_not_own` union; reviews |
| Persona over-claim sounds like a real expert | disclosure + `persona_claim` + L1 still mechanical |
| Operators think toggle ON grants tools | FR-SKL-005; UI copy; GATE errors |
| Specials `status: draft` leaking into a video child | Child `status` is never inherited |

---

## Document control

| Item | Value |
|------|-------|
| Owner | Host architecture (CASOPS) |
| Implements in live packs? | **No** until a separate implementation task |
| Production activation? | **No** |
| Network? | **No** |
| Diagrams | Inline SVG in this document |

**End of specification.**
