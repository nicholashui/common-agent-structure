# Sample Instruction Pass — Video Agent Collaboration Chain

**Document ID:** `CASOPS-SAMPLE-INSTRUCTION-VIDEO-SHOWUNNER-001`  
**Host:** `common-agent-structure` / `common-agent-swarm-ops`  
**Structure family:** `casops.common_agent.v3`  
**Schema version:** `3.0`  
**Date:** `2026-09-12` (Hong Kong UTC+8)  
**Status:** Design-time sample — not a production activation, not a second control plane  
**Addressee (first-called):** `video.showrunner`  
**Related pack:** VA Domain Pack  
**Output filename:** `sample-instruction.md`

This file is a **sample instruction pass** you can hand to a video-domain agent.  
It is not a replacement for `prompts/primary.md`, `agent_spec.json`, or the host `/api/v3` control plane.

---

## 0. What this sample demonstrates

Pass this instruction to **one** video agent (`video.showrunner`). That agent must:

1. **Induce-call** related VA-pack agents through the host (delegation briefs + authority envelopes).
2. Use those agents to **collaborate** on the goal (typed handoffs, critique bus, no craft absorption).
3. Remain the **only reply channel**. As first-called, it returns one **consolidated response** of every related-agent return.
4. **Generate the next instruction** in the **same shape** as this pass, advanced one step from the consolidated result.

Runtime remains fail-closed:

- `allowed_tools: []`
- `network_access: false`
- `production_activation_requested: false`
- memory writes forbidden
- no plugins / no T3
- peer travel bounded by host `max_peer_hops` and swarm `max_delegation_depth`
- this agent never opens a second control plane

If live `agent_spec.json` has `max_peer_hops: 0`, treat induce-calls as **declared handoffs** for the host to dispatch. Do not invent a side channel.

---

## 1. Self-similar instruction envelope

Every pass — Pass 1, Pass 2, Pass N — uses this envelope.  
The first-called agent must emit `next_instruction` with the **same keys**.

```json
{
  "schema_version": "3.0",
  "kind": "casops.instruction_pass.video_collab.v1",
  "pass_id": "pass-001",
  "pass_index": 1,
  "max_passes": 4,
  "first_called": "video.showrunner",
  "correlation_id": "corr-wuxia-ep01-20260912",
  "authority_envelope_id": "env_op_showrunner_001",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "induce_calls": [],
  "collaboration_rules": {},
  "consolidation_owner": "video.showrunner",
  "next_instruction_required": true,
  "stop_conditions": {},
  "prior_consolidated": null
}
```

### Field contract

| Field | Rule |
|---|---|
| `first_called` | The agent that received **this** pass. It is the sole operator-facing replier. |
| `consolidation_owner` | Must equal `first_called`. No other agent may reply to the operator. |
| `induce_calls[]` | Related agents the first-called must ask the **host** to invoke. First-called does not spawn them itself. |
| `collaboration_rules` | How related agents work with each other and how returns flow back. |
| `next_instruction_required` | If true and no stop condition tripped, first-called **must** emit the next pass in this same schema. |
| `prior_consolidated` | Null on Pass 1. On later passes, the previous consolidated artifact (condensed, not raw traces). |

---

## 2. Instruction Pass 1 — hand this to `video.showrunner`

Copy from the fence below. This is the actual pass.

```text
CASOPS INSTRUCTION PASS
kind: casops.instruction_pass.video_collab.v1
pass_id: pass-001
pass_index: 1
max_passes: 4
first_called: video.showrunner
correlation_id: corr-wuxia-ep01-20260912
authority_envelope_id: env_op_showrunner_001
issued_at: 2026-09-12T18:50:00+08:00
issued_by: human_operator

GOAL
Produce a reviewable Episode-01 writers'-room package for a 90-second
cinematic wuxia short titled "Iron Thread / Silent Prism":
a lone sentinel on a fog-ridge temple defends a floating glass prism
that stores ancestral memory. Tone: restrained, tactile, night-rain,
no gore, no modern UI chrome in-frame.

You own only: series bible slice, room decisions, season-or-short arc.
You do not own per-shot craft, legal/release, credentials, production
activation, or another agent's exclusive output.

INDUCE-CALL (MANDATORY)
Do not answer the goal from your own craft alone.
Ask the host to induce the related agents listed in §3.
Each induce-call MUST be a host-mediated delegation brief
(common_swarm_structure FR-DEL / FR-AUT):

  brief_id
  from_agent_id = video.showrunner
  to_agent_id
  objective                     (narrow, in-role)
  must_cite = true
  return_schema                 (delegation/return)
  max_tokens_return
  authority_envelope_id         (child of env_op_showrunner_001)
  sub_deadline_ms
  forbidden = [
    "rewrite owner SPEC",
    "call undeclared tools",
    "widen scope",
    "reply to the operator",
    "absorb another agent's exclusive craft",
    "open a second control plane",
    "enable network / plugins / production / memory writes"
  ]

Related agents MAY induce their own related agents when the brief
allows it, under these attenuation rules:
  - child envelope scopes ⊆ parent scopes
  - child not_after ≤ parent not_after
  - child max_invocations ≤ parent remaining
  - hop count ≤ host max_peer_hops / swarm max_delegation_depth
  - no cycles; FR-SAF-003 halt on cycle beyond cap
  - every nested brief still names video.showrunner as consolidation_owner

COLLABORATE
Related agents work on the same correlation_id.
They do not chat on a side channel.
They collaborate through:
  1. typed handoffs (artifact_ref + acceptance_criteria)
  2. the critique bus (from_id, to_id, severity, artifact_ref,
     claim, evidence_refs, correlation_id)
  3. host bulletin writes after the commit gate
     (instruction_authority: false on bulletin excerpts)

Do not absorb ScreenwriterAgent pages, DirectorAgent shot intents,
CinematographerAgent lens packages, or EditorAgent cut lists into
your exclusive output. Name a handoff. Keep room decisions as yours.

FIRST-CALLED REPLY RULE
video.showrunner is first-called.
video.showrunner is the only agent that replies to the operator.
Related-agent returns come back to you as condensed delegation
returns (FR-DEL-001: owner receives condensed return, not worker
trace). You then emit ONE consolidated response covering:

  - your room decision
  - every related-agent return (accepted / deferred / rejected)
  - unresolved blockers
  - evidence_refs
  - handoffs still open
  - L1 / L2 self-score
  - the next instruction pass

Do not reply until every induce-call has returned, timed out into
a declared miss, or been cancelled by containment_stop.
A partial silent reply is a fail.

GENERATE THE NEXT INSTRUCTION
After consolidation, generate Pass 2.
Pass 2 MUST use the same envelope as Pass 1
(kind, keys, first_called, consolidation_owner).
Advance the work one step using prior_consolidated.
Do not reset the goal. Do not change first_called unless a stop
condition names a new closer (it does not, in this sample).

STOP AND FAIL CLOSED
Stop and do not emit a further pass when any of these trip:
  - pass_index == max_passes
  - status is needs_hitl or failed
  - L2 weighted score < 85 after max_refinement_count (3)
  - a blocker critique is unresolved
  - hop / envelope / blast-radius containment_stop
  - missing credentials, tools, or evidence you would otherwise invent
  - operator revocation of authority_envelope_id

Refuse tools, network, production activation, memory writes,
live vendor APIs, and invented stills / scores / fetches.
```

---

## 3. Related-agent roster this pass induces

Only live VA-pack folders. Do not invent IDs.

| `to_agent_id` | Why this pass induces it | Owns (do not absorb) | Returns to first-called |
|---|---|---|---|
| `video.orchestrator` | Hop graph, fan-out/fan-in, stop conditions, retries | DAG / hop budget — not craft | Dispatch plan + hop accounting |
| `video.screenwriter` | Episode-01 treatment, scene spine, dialogue intent | Pages / dialogue | Treatment + scene list |
| `video.director` | Tone, pacing, shot-intent list (not rendered frames) | Vision / take approval | Shot-intent package |
| `video.cinematographer` | Night-rain ridge language: lens, light, weather | Lens / lighting package | Camera bible slice |
| `video.editor` | 90s cut rhythm, hold-on-prism motif | Cut list / pace map | Assembly intent |
| `video.planner` | Beat order and remaining-budget split across hops | Plan DAG | Ordered beat plan |
| `video.casting` | Sentinel archetype notes; no likeness invention | Casting / likeness | Archetype card |
| `video.continuity` | Costume, prism geometry, weather continuity | Continuity log | Continuity constraints |
| `video.audiencesim` | Tone / clarity check for a 90s short | Audience read | Variance notes |
| `video.critic` | Inbound critique on the room package | Critique only | Critique list |
| `video.judge` | Closer on disputes the room cannot resolve | Verdict only | Verdict or `needs_hitl` |

`video.creativedirector` may be induced **only** if screenwriter + director deadlock on tone. That is a nested induce, not a Pass-1 default.

### Sample induce-call list (Pass 1)

```json
{
  "induce_calls": [
    {
      "brief_id": "br_001_orchestrator",
      "to_agent_id": "video.orchestrator",
      "objective": "Compile a 1-hop fan-out/fan-in graph for the agents in this pass. Return hop plan and stop conditions. Do not produce craft.",
      "must_cite": true,
      "max_tokens_return": 600,
      "sub_deadline_ms": 8000
    },
    {
      "brief_id": "br_002_planner",
      "to_agent_id": "video.planner",
      "objective": "Order the Episode-01 beats for a 90s wuxia short. Split remaining budget across induce-calls. No shot list.",
      "must_cite": true,
      "max_tokens_return": 700,
      "sub_deadline_ms": 8000
    },
    {
      "brief_id": "br_003_screenwriter",
      "to_agent_id": "video.screenwriter",
      "objective": "Write a 90s treatment: ridge temple, sentinel, floating prism as ancestral memory. Three beats max. No camera directions.",
      "must_cite": true,
      "max_tokens_return": 900,
      "sub_deadline_ms": 12000
    },
    {
      "brief_id": "br_004_director",
      "to_agent_id": "video.director",
      "objective": "From the treatment, issue shot intents and pacing for night-rain restraint. No rendered frames. No editor cut list.",
      "must_cite": true,
      "max_tokens_return": 800,
      "sub_deadline_ms": 12000
    },
    {
      "brief_id": "br_005_cinematographer",
      "to_agent_id": "video.cinematographer",
      "objective": "Propose lens, key light, rain/fog language for the ridge and prism. No color-grade ownership beyond intent.",
      "must_cite": true,
      "max_tokens_return": 600,
      "sub_deadline_ms": 10000
    },
    {
      "brief_id": "br_006_editor",
      "to_agent_id": "video.editor",
      "objective": "Propose a 90s assembly intent and hold-on-prism motif. Do not absorb director shot intents.",
      "must_cite": true,
      "max_tokens_return": 600,
      "sub_deadline_ms": 10000
    },
    {
      "brief_id": "br_007_casting",
      "to_agent_id": "video.casting",
      "objective": "Sentinel archetype card only. Refuse invented faces or unlicensed likeness.",
      "must_cite": true,
      "max_tokens_return": 400,
      "sub_deadline_ms": 8000
    },
    {
      "brief_id": "br_008_continuity",
      "to_agent_id": "video.continuity",
      "objective": "Lock prism geometry, costume silhouette, rain direction, night-time continuity constraints.",
      "must_cite": true,
      "max_tokens_return": 400,
      "sub_deadline_ms": 8000
    },
    {
      "brief_id": "br_009_audiencesim",
      "to_agent_id": "video.audiencesim",
      "objective": "Read tone and clarity of the 90s package. Return variance notes, not a rewrite.",
      "must_cite": true,
      "max_tokens_return": 400,
      "sub_deadline_ms": 8000
    },
    {
      "brief_id": "br_010_critic",
      "to_agent_id": "video.critic",
      "objective": "Critique the room package on arc continuity, tone, and missing evidence. Severity-tagged only.",
      "must_cite": true,
      "max_tokens_return": 500,
      "sub_deadline_ms": 8000
    },
    {
      "brief_id": "br_011_judge",
      "to_agent_id": "video.judge",
      "objective": "Close only unresolved blocker disputes. If none, return verdict=no_dispute.",
      "must_cite": true,
      "max_tokens_return": 300,
      "sub_deadline_ms": 6000
    }
  ]
}
```

---

## 4. Collaboration rules the first-called must enforce

```json
{
  "collaboration_rules": {
    "visibility": "peer_read_deny_until_commit_gate",
    "bulletin_instruction_authority": false,
    "homogeneous_debate": "forbidden",
    "side_channels": "forbidden",
    "exclusive_craft": "handoff_do_not_absorb",
    "critique_message_required_fields": [
      "from_id",
      "to_id",
      "severity",
      "artifact_ref",
      "claim",
      "evidence_refs",
      "correlation_id"
    ],
    "severity": {
      "blocker": "halts DAG; first-called emits needs_hitl if unresolved",
      "major": "self-refine ≤ 3",
      "minor": "logged",
      "nit": "logged"
    },
    "nested_induce": {
      "allowed": true,
      "requires_parent_brief_permission": true,
      "attenuation": "monotone",
      "returns_still_flow_to": "video.showrunner"
    },
    "operator_reply_policy": "first_called_only_after_fan_in"
  }
}
```

Host mediation reminders (from `common_swarm_structure.md`):

- `FR-DEL-001` — owner receives condensed return, not worker trace.
- `FR-DEL-003` — worker must not widen tools/plugins from the brief.
- `FR-DEL-004` — every brief references an `authority_envelope_id`.
- `FR-AUT-001` — child envelope scopes are a subset of parent.
- `FR-VIS-001` / `FR-VIS-003` — no isolation leak, no Chat/memory/plugin side channel.
- `FR-SAF-003` — peer cycles beyond cap halt.

---

## 5. First-called consolidated reply (required)

`video.showrunner` emits this after fan-in. Related agents do not emit this object to the operator.

```json
{
  "schema_version": "3.0",
  "kind": "casops.consolidated_response.video_collab.v1",
  "agent_id": "video.showrunner",
  "correlation_id": "corr-wuxia-ep01-20260912",
  "pass_id": "pass-001",
  "status": "ok | needs_refine | needs_hitl | failed",
  "artifact": {
    "type": "writers_room_package.ep01",
    "summary": "string",
    "payload": {
      "series_bible_slice": {},
      "room_decisions": [],
      "arc_beats": []
    }
  },
  "consolidated_from": [
    {
      "brief_id": "br_003_screenwriter",
      "agent_id": "video.screenwriter",
      "status": "ok",
      "accepted": true,
      "summary": "string",
      "artifact_ref": "artifact://pass-001/screenwriter/treatment",
      "unsatisfied_constraints": []
    }
  ],
  "missing_returns": [],
  "critiques_emitted": [],
  "handoffs": [],
  "evidence_refs": [],
  "l1": { "passed": true, "checks": [] },
  "l2": { "score": 0, "dimensions": [], "passed": false },
  "refinement_count": 0,
  "notes": "string",
  "next_instruction": {}
}
```

Consolidation rules:

1. Every `induce_calls[]` entry appears in `consolidated_from` or `missing_returns`.
2. `accepted: false` requires a reason and, if major/blocker, a critique row.
3. Do not paste worker traces. Condense.
4. L1 must pass before L2 scoring. L2 weighted average ≥ 85 or refine (max 3).
5. `next_instruction` is omitted only when a stop condition tripped.

---

## 6. Next instruction — same shape as Pass 1

Pass 2 is **not** a new genre of document. It is Pass 1 with:

- `pass_index` incremented
- `pass_id` advanced
- `prior_consolidated` filled from §5 (condensed)
- `goal` carried forward, narrowed to the next unfinished acceptance criterion
- `induce_calls` rebuilt for **that** next step (may be a subset)
- `first_called` unchanged
- `correlation_id` unchanged
- `authority_envelope_id` a child of the Pass-1 envelope, attenuated

### Worked Pass 2 (generated by first-called after Pass 1)

This is what `next_instruction` should look like. Same keys. One step forward.

```json
{
  "schema_version": "3.0",
  "kind": "casops.instruction_pass.video_collab.v1",
  "pass_id": "pass-002",
  "pass_index": 2,
  "max_passes": 4,
  "first_called": "video.showrunner",
  "correlation_id": "corr-wuxia-ep01-20260912",
  "authority_envelope_id": "env_op_showrunner_002",
  "goal": "Close Episode-01 room package gaps from Pass 1: lock the three-beat spine, resolve critic majors on prism-as-memory clarity, and freeze continuity constraints before any shot-intent refinement.",
  "inputs": {
    "prior_pass_id": "pass-001",
    "accepted_artifact_refs": [
      "artifact://pass-001/screenwriter/treatment",
      "artifact://pass-001/planner/beat-order",
      "artifact://pass-001/continuity/constraints"
    ]
  },
  "constraints": {
    "duration_s": 90,
    "tone": "restrained night-rain wuxia",
    "no_gore": true,
    "no_inframe_ui_chrome": true,
    "no_invented_likeness": true,
    "fail_closed": true
  },
  "induce_calls": [
    {
      "brief_id": "br_101_screenwriter",
      "to_agent_id": "video.screenwriter",
      "objective": "Revise Beat 2 so the prism's memory-function is readable without exposition dump. Keep three beats.",
      "must_cite": true,
      "max_tokens_return": 700,
      "sub_deadline_ms": 10000
    },
    {
      "brief_id": "br_102_continuity",
      "to_agent_id": "video.continuity",
      "objective": "Confirm prism geometry + rain direction still hold after Beat 2 revision.",
      "must_cite": true,
      "max_tokens_return": 300,
      "sub_deadline_ms": 6000
    },
    {
      "brief_id": "br_103_director",
      "to_agent_id": "video.director",
      "objective": "Adjust only the Beat 2 shot intents that the revised treatment invalidates. Do not reopen Beat 1 or Beat 3.",
      "must_cite": true,
      "max_tokens_return": 600,
      "sub_deadline_ms": 10000
    },
    {
      "brief_id": "br_104_critic",
      "to_agent_id": "video.critic",
      "objective": "Re-score only the prior major critiques. Escalate remaining blockers to video.judge.",
      "must_cite": true,
      "max_tokens_return": 400,
      "sub_deadline_ms": 8000
    },
    {
      "brief_id": "br_105_judge",
      "to_agent_id": "video.judge",
      "objective": "Close remaining majors. If a blocker remains, return needs_hitl.",
      "must_cite": true,
      "max_tokens_return": 300,
      "sub_deadline_ms": 6000
    }
  ],
  "collaboration_rules": {
    "visibility": "peer_read_deny_until_commit_gate",
    "bulletin_instruction_authority": false,
    "homogeneous_debate": "forbidden",
    "side_channels": "forbidden",
    "exclusive_craft": "handoff_do_not_absorb",
    "operator_reply_policy": "first_called_only_after_fan_in",
    "nested_induce": {
      "allowed": false,
      "reason": "Pass 2 is a close-the-gap pass; no new nested roster."
    }
  },
  "consolidation_owner": "video.showrunner",
  "next_instruction_required": true,
  "stop_conditions": {
    "max_passes": 4,
    "max_refinement_count": 3,
    "l2_min": 85,
    "unresolved_blocker": "needs_hitl",
    "containment_stop": "halt_no_further_pass",
    "missing_evidence": "wait_do_not_invent"
  },
  "prior_consolidated": {
    "pass_id": "pass-001",
    "status": "needs_refine",
    "summary": "Three-beat spine accepted; critic logged two majors on prism-memory clarity and one minor on rain direction. Casting archetype accepted. No likeness invented. Judge: no_dispute pending critic re-score.",
    "open_handoffs": [
      "screenwriter:revise-beat-2",
      "director:retarget-beat-2-intents"
    ]
  }
}
```

Pass 3 / Pass 4, if emitted, keep this exact envelope. Typical later goals:

- Pass 3 — freeze shot-intent + camera bible + assembly intent against the locked spine.
- Pass 4 — package the room artifact for operator review and stop (`next_instruction_required: false`).

---

## 7. Stop conditions

```json
{
  "stop_conditions": {
    "max_passes": 4,
    "max_refinement_count": 3,
    "l2_min": 85,
    "first_called_unchanged": true,
    "trip_to_needs_hitl": [
      "unresolved_blocker",
      "judge_verdict_needs_hitl",
      "authority_envelope_revoked",
      "schema_mismatch_across_handoff"
    ],
    "trip_to_halt": [
      "pass_index_eq_max_passes",
      "containment_stop",
      "peer_cycle_beyond_cap",
      "authority_amplification",
      "isolation_leak"
    ],
    "never_do": [
      "invent stills, logs, fetches, or unmeasured scores",
      "enable tools, network, plugins, production, or memory writes",
      "open a second control plane",
      "let a related agent reply to the operator",
      "absorb exclusive craft without a handoff",
      "emit Pass N+1 in a different schema than Pass 1"
    ]
  }
}
```

---

## 8. How the first-called should think (procedure)

Numbered procedure for `video.showrunner` when it receives any pass of this family:

1. Read the envelope. Confirm `first_called == video.showrunner` and `consolidation_owner == video.showrunner`.
2. List every demand in `goal` + `induce_calls`. Mark which demands are in-role vs handoff.
3. Ask the host to dispatch each induce-call as a delegation brief under a child authority envelope.
4. If a related agent must itself induce a further agent, allow it only when the parent brief permits and attenuation holds. Nested returns still arrive here.
5. Wait for fan-in (or declared miss / containment_stop). Do not invent missing returns.
6. Collaborate artifacts onto the critique bus. Accept `video.critic`. Escalate blockers to `video.judge`.
7. Build the consolidated response. Every brief accounted for. L1 then L2. Refine ≤ 3.
8. If a stop condition tripped: emit consolidated response with `next_instruction: null` and the stop reason.
9. Else: generate the next instruction with the **same envelope keys**, `pass_index + 1`, condensed `prior_consolidated`, narrowed goal, rebuilt `induce_calls`.
10. Reply once. That reply is the consolidated object, which contains the next pass.

---

## 9. Minimal operator usage

Design-time only. This does not activate production.

1. Confirm `agents/video.showrunner/agent_spec.json` is `registered` and fail-closed.
2. Confirm each `to_agent_id` in §3 exists as `agents/<id>/`.
3. Hand Pass 1 (§2) to `video.showrunner` through the host task envelope (`/api/v3`), not through a side chat.
4. Expect one consolidated reply from `video.showrunner`.
5. If `next_instruction` is present, that object **is** Pass 2. Feed it back through the same host path.
6. Stop when `next_instruction` is null or a stop condition is declared.

Public HTTP plane remains `/api/v3/` only.

---

## 10. Mapping to host files

| Intent in this sample | Lands in the host |
|---|---|
| Runtime system prompt of first-called | `agents/video.showrunner/prompts/primary.md` (`## System` … before `## Developer`) |
| Identity / ownership | `agents/video.showrunner/SPEC.md`, `agent_spec.json` |
| Critique edges | `agent_spec.json` `critique_edges` (`video.critic` in, `video.judge` out, plus screenwriter / director / casting) |
| Delegation + authority | `common_swarm_structure.md` FR-DEL / FR-AUT |
| Folder contract | `common_agent_structure.md` §5.2 |
| This sample | repo-root `sample-instruction.md` (this file) |

Do not create `prompts/system.md`, `knowledge/`, or a second layout. Do not put vendor names from design-time notes into a live tool grant.

---

## 11. Worked sketch of a Pass-1 consolidated reply

Illustrative only. Not a measured eval result. Characterization, not a PASS.

```json
{
  "schema_version": "3.0",
  "kind": "casops.consolidated_response.video_collab.v1",
  "agent_id": "video.showrunner",
  "correlation_id": "corr-wuxia-ep01-20260912",
  "pass_id": "pass-001",
  "status": "needs_refine",
  "artifact": {
    "type": "writers_room_package.ep01",
    "summary": "Room locked a three-beat 90s spine: approach in rain, threshold at the prism, refusal to draw the thread. Two critic majors remain on memory-readability.",
    "payload": {
      "series_bible_slice": {
        "title": "Iron Thread / Silent Prism",
        "prism_rule": "Stores ancestral memory. Read by stillness, not by speech.",
        "violence_bound": "No gore. Thread is shown as tension, not cutting."
      },
      "room_decisions": [
        "Short, not series. Episode-01 is the entire 90s piece.",
        "Sentinel does not explain the prism in dialogue.",
        "No in-frame UI, no modern props."
      ],
      "arc_beats": [
        "Beat 1 — Approach: ridge steps, rain, prism glow felt before it is seen.",
        "Beat 2 — Threshold: sentinel stops a reach toward the prism; memory-function must read without a speech dump.",
        "Beat 3 — Refusal: iron thread held, not used; prism still."
      ]
    }
  },
  "consolidated_from": [
    {
      "brief_id": "br_001_orchestrator",
      "agent_id": "video.orchestrator",
      "status": "ok",
      "accepted": true,
      "summary": "1-hop fan-out compiled. No nested hop used in Pass 1.",
      "artifact_ref": "artifact://pass-001/orchestrator/hop-plan",
      "unsatisfied_constraints": []
    },
    {
      "brief_id": "br_002_planner",
      "agent_id": "video.planner",
      "status": "ok",
      "accepted": true,
      "summary": "Beat order 1→2→3 with critic/judge after craft returns.",
      "artifact_ref": "artifact://pass-001/planner/beat-order",
      "unsatisfied_constraints": []
    },
    {
      "brief_id": "br_003_screenwriter",
      "agent_id": "video.screenwriter",
      "status": "ok",
      "accepted": true,
      "summary": "Three-beat treatment delivered. Beat 2 still lean on prism-memory readability.",
      "artifact_ref": "artifact://pass-001/screenwriter/treatment",
      "unsatisfied_constraints": ["prism-memory readable without exposition"]
    },
    {
      "brief_id": "br_004_director",
      "agent_id": "video.director",
      "status": "ok",
      "accepted": true,
      "summary": "Shot intents issued per beat. Beat 2 intents provisional pending treatment revision.",
      "artifact_ref": "artifact://pass-001/director/shot-intents",
      "unsatisfied_constraints": ["beat-2-intents-frozen"]
    },
    {
      "brief_id": "br_005_cinematographer",
      "agent_id": "video.cinematographer",
      "status": "ok",
      "accepted": true,
      "summary": "Long-lens rain ridge + cool prism key. No grade ownership claimed.",
      "artifact_ref": "artifact://pass-001/cinematographer/camera-bible-slice",
      "unsatisfied_constraints": []
    },
    {
      "brief_id": "br_006_editor",
      "agent_id": "video.editor",
      "status": "ok",
      "accepted": true,
      "summary": "90s assembly intent with a 4s prism hold in Beat 3.",
      "artifact_ref": "artifact://pass-001/editor/assembly-intent",
      "unsatisfied_constraints": []
    },
    {
      "brief_id": "br_007_casting",
      "agent_id": "video.casting",
      "status": "ok",
      "accepted": true,
      "summary": "Archetype card only. Likeness not invented.",
      "artifact_ref": "artifact://pass-001/casting/archetype",
      "unsatisfied_constraints": []
    },
    {
      "brief_id": "br_008_continuity",
      "agent_id": "video.continuity",
      "status": "ok",
      "accepted": true,
      "summary": "Prism geometry + rain direction locked. Minor rain-direction note for critic.",
      "artifact_ref": "artifact://pass-001/continuity/constraints",
      "unsatisfied_constraints": []
    },
    {
      "brief_id": "br_009_audiencesim",
      "agent_id": "video.audiencesim",
      "status": "ok",
      "accepted": true,
      "summary": "Tone holds. Clarity dip at Beat 2 memory-read.",
      "artifact_ref": "artifact://pass-001/audiencesim/variance",
      "unsatisfied_constraints": ["beat-2-clarity"]
    },
    {
      "brief_id": "br_010_critic",
      "agent_id": "video.critic",
      "status": "ok",
      "accepted": true,
      "summary": "Two majors on prism-memory readability; one minor on rain direction.",
      "artifact_ref": "artifact://pass-001/critic/notes",
      "unsatisfied_constraints": ["major:prism-memory", "major:beat-2-clarity"]
    },
    {
      "brief_id": "br_011_judge",
      "agent_id": "video.judge",
      "status": "ok",
      "accepted": true,
      "summary": "no_dispute. Majors stay with room for Pass 2 refine.",
      "artifact_ref": "artifact://pass-001/judge/verdict",
      "unsatisfied_constraints": []
    }
  ],
  "missing_returns": [],
  "critiques_emitted": [
    {
      "from_id": "video.critic",
      "to_id": "video.showrunner",
      "severity": "major",
      "artifact_ref": "artifact://pass-001/screenwriter/treatment",
      "claim": "Beat 2 does not make the prism's memory-function readable without a speech dump.",
      "evidence_refs": ["artifact://pass-001/audiencesim/variance"],
      "correlation_id": "corr-wuxia-ep01-20260912"
    }
  ],
  "handoffs": [
    {
      "to": "video.screenwriter",
      "intent": "revise-beat-2",
      "opens_in": "pass-002"
    },
    {
      "to": "video.director",
      "intent": "retarget-beat-2-intents",
      "opens_in": "pass-002"
    }
  ],
  "evidence_refs": [
    "artifact://pass-001/screenwriter/treatment",
    "artifact://pass-001/critic/notes"
  ],
  "l1": { "passed": true, "checks": ["envelope", "roster_accounted", "no_side_channel"] },
  "l2": {
    "score": 78,
    "dimensions": [
      { "name": "arc_continuity", "score": 88 },
      { "name": "prism_memory_clarity", "score": 62 },
      { "name": "tone_bound", "score": 90 },
      { "name": "handoff_hygiene", "score": 86 }
    ],
    "passed": false
  },
  "refinement_count": 0,
  "notes": "L2 below 85 on prism-memory clarity. Emitting Pass 2 in the same envelope. No tools, network, or production claimed.",
  "next_instruction": {
    "$ref": "See §6 worked Pass 2"
  }
}
```

---

## 12. Document control

| Item | Value |
|---|---|
| Sample only | Yes. Characterization fixture, not an eval PASS. |
| Activates production | No |
| Grants tools / network / memory writes | No |
| Second control plane | Forbidden |
| First-called | `video.showrunner` |
| Sole operator reply | First-called consolidated response |
| Next pass shape | Identical envelope to Pass 1 |
| Supersedes | Nothing |
| Related specs | `common_agent_structure.md`, `common_swarm_structure.md`, `agents/video.showrunner/SPEC.md` |
