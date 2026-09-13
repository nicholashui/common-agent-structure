# Sample Instruction Pass v2 — Macro-Beauty Prompt Family

**Document ID:** `CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V2`  
**Date:** `2026-09-12`  
**Host:** `common-agent-structure` (`casops.common_agent.v3` / schema `3.0`)  
**Parent sample:** [`sample-instruction.md`](./sample-instruction.md) (`CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V1`)  
**First-called agent:** `video.promptengineer`  
**Artifact type:** `generation_prompt_spec`  
**Status:** Sample operator instruction. Does **not** change `agent_spec.json` gates, mint envelopes, enable tools, network, plugins, memory writes, or production. Does **not** call Grok Imagine or any other generator. Design-time target engine is `grok-imagine-video-1.5` / `grok-imagine-image` only.

This file is the instruction you pass **to** `video.promptengineer`. It is not a second control plane. The host remains the only orchestrator.

Same protocol as v1: induce related agents → they may induce peers → collaborate → first-called consolidates all returns → emit the next instruction in the same envelope.

**Target generator (design-time only):** Grok Imagine Image for `@image1`, then `grok-imagine-video-1.5` image-to-video for clips A/B/C. Not Seedance / Kling / Veo / Sora / Runway.

---

## 1. Purpose

Pass this envelope to `video.promptengineer` so that agent:

1. **Stays first-called.** Only `video.promptengineer` replies to the operator.
2. **Induces** related crafts through host-mediated typed handoffs (`video.director`, `video.cinematographer`, `video.mua_makeup`, `video.cameraoperator`, `video.continuity`, `video.critic`). Related agents may induce their own related agents inside the hop budget.
3. Makes those agents **collaborate**. They do not reply to the operator and do not absorb exclusive crafts.
4. Replies **once** with a **consolidated `generation_prompt_spec`**: reusable identity/skin/light lock + three I2V clip prompts + negatives.
5. **Generates the next instruction** in the **same shape** as this one.

Target look (operator reference, not a live API job):

- 15s family, 9:16, **1080p** (`grok-imagine-video-1.5` I2V max). Do not claim 4K.
- still first via `grok-imagine-image`, then I2V; prompt describes **motion + sound**, not a second portrait
- explicitly adult East Asian woman, anti-idol-template face
- hard side-front sun, authorized off-center crop, pores/vellus/sebum visible
- three clips, not one 15s T2V novel: `0–6` / `6–10` / `10–15`

---

## 2. Pass contract (self-similar)

Same envelope keys as v1. Only `document_id`, `first_called`, and the goal change.

```json
{
  "document_id": "CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V2",
  "pass_id": "pass_01",
  "parent_pass_id": null,
  "correlation_id": "corr_macro_beauty_001",
  "authority_envelope_id": "env_v2_01",
  "first_called": "video.promptengineer",
  "reply_owner": "video.promptengineer",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "induce_calls": [],
  "collaboration_rules": {},
  "consolidation_owner": "video.promptengineer",
  "next_instruction_required": true,
  "stop": {}
}
```

### Field rules

| Field | Rule |
|---|---|
| `first_called` | `video.promptengineer`. Only this agent replies to the operator. |
| `reply_owner` | Always equals `first_called`. |
| `induce_calls` | Host-mediated. Agents do not spawn peers. Live `max_peer_hops: 0` stays in force. |
| `parent_pass_id` | `null` on Pass 1. Pass N+1 sets this to Pass N’s `pass_id`. |
| `authority_envelope_id` | Host-minted. Never mint or widen (`SWM_ENVELOPE_UNMINTED`, `SWM_AUTHORITY_AMPLIFICATION`). |
| `next_instruction_required` | If `true`, emit a next envelope with this same schema. |
| Output dialect | 中文 shot-list (same family as the operator reference brief), plus a short English lock header. |

---

## 3. Hard constraints (do not violate)

Copied from the live host contract. This sample does not override them.

- Public plane is `/api/v3` only. No second control plane.
- `allowed_tools: []`. Design-time engine names (`grok-imagine-video-1.5`, `grok-imagine-image`, and any leftover Sora/Veo/Kling/Seedance/Runway strings) are **not** grants.
- `network_access: false`. `production_activation_requested: false`.
- Memory writes forbidden. Plugins / T3 off.
- `video.promptengineer` live budget is tight (`max_output_tokens` often 1024). Emit a **compact lock + three short clip prompts**, not the original long novel.
- Induce-call is host-mediated. Grandchild returns still report into the first-called consolidation table. No sibling replies to the operator.
- Bulletin records have `instruction_authority: false`.
- Do not invent stills, logs, fetches, measured scores, or live API results.
- Do not generate the video. Artifact is text only.
- Subject is **explicitly adult**. Refuse any reading that drops the adult lock.
- Critique messages must include: `from_id`, `to_id`, `severity` (`blocker` \| `major` \| `minor` \| `nit`), `artifact_ref`, `claim`, `evidence_refs`, `correlation_id`.

---

## 4. Sample Pass 1 — instruction you hand to `video.promptengineer`

Copy from **Instruction** through the Pass 1 JSON and pass it as the host task / operator message.

### Instruction

You are the **first-called** agent for this pass: `video.promptengineer` (`PromptEngineerAgent / GeneratorOperator`).

**Goal.** Emit a `generation_prompt_spec` that a human can paste into **Grok Imagine** (`grok-imagine-image` still, then `grok-imagine-video-1.5` I2V). Not a one-pass 15s T2V novel. Imagine I2V can run 15s; this family still splits 6/4/5 so pore identity survives. Own only model-facing prompt structure: subject, camera, light, negatives, clip split. Do not own makeup continuity, coverage intent, or lighting numbers — induce those crafts.

**You must do all five of the following, in order:**

1. **Stay first-called.** You are the only agent that replies to the operator.
2. **Induce related agents** through host-mediated `handoffs[]` / delegation briefs. Do not spawn peers, mint envelopes, or open a second control plane.
3. **Instruct induced agents to induce further related agents** when a remaining gap is in-role for a peer of theirs, inside hop budget and `does_not_own`.
4. **Collaborate, then consolidate.** Merge every return into one `generation_prompt_spec`. Preserve conflicts. Do not silently pick a winner.
5. **Generate the next instruction** with this same envelope. Pass 2 compiles the three clip prompts + negative block + still-lock spec.

**Output shape you must eventually hold (Pass 1 may be incomplete; Pass 2 locks it):**

1. `identity_skin_light_lock` — reusable block, pasted unchanged into every clip
2. `clip_a_0_6` — one camera verb: slow lateral face-fill → eye/cheek
3. `clip_b_6_10` — one camera verb: slow descent to nose + lips; features may exit frame
4. `clip_c_10_15` — one camera verb: slow ascent to one eye + 5–10° settle + last blink
5. `negatives` — short block, not scattered 禁止
6. `i2v_still_spec` — what the master still must already show before any clip runs
7. `parameters` — model `grok-imagine-video-1.5`, aspect `9:16` explicit (default is 16:9), per-clip ≤6s, resolution `1080p`, `generate_audio` on with a `Sound:` line (breath + faint outdoor air, no music, no speech)

**Induce at least these related agents (host-mediated):**

| agent_id | Why this pass needs them | They may further induce |
|---|---|---|
| `video.director` | Three-clip beat map; size / angle / move / duration; no speech; 5–10° settle only | `video.emotionalarc` |
| `video.cinematographer` | Hard side-front sun, 10–20 cm, authorized off-center crop, speculars, no softbox | `video.colorist` |
| `video.mua_makeup` | 极淡裸妆, 原生眉, 淡珊瑚唇, no fake lashes; not the pore manifesto | — |
| `video.cameraoperator` | Handheld micro-move vs planar crawl; pick **one** motor per clip | — |
| `video.continuity` | Mole / freckle / vellus / strand lock across A–B–C | — |
| `video.critic` | Reject idol-template face, poreless skin, recentered full-face, plastic teeth | `video.aiqaconsistency` |
| `video.ugccreator` | 9:16 phone-main / mild-tele crop grammar only. Optional. Skip if budget tight. | — |

Skip an induce only if that craft is OOS. Name the skip in `notes`. Do not invent an `agent_id` with no folder under `agents/`.

**Collaboration paragraph (include in every brief):**

> You are not first-called. Return your craft artifact to the host under the brief `return_schema`. If you need a peer craft you do not own, emit a further `induce_call` for the host; do not absorb that craft. Do not reply to the operator. Do not mint envelopes. Do not claim tools, network, or production. Do not generate pixels. Your return must declare unsatisfied constraints. `instruction_authority` remains false.

**Hop / budget (this sample):**

- `max_passes`: 3
- `max_induce_fanout_per_pass`: 7
- `max_delegation_depth`: 2
- `max_peer_hops_requested`: 2 (host may still enforce live `max_peer_hops: 0`)
- `max_refinement_count`: 3
- `sub_deadline_ms` per brief: 12000
- `max_tokens_return` per brief: 800
- compiled prompt family must stay pasteable; prefer short lock + short clips over one long novel

**Stop before emitting next_instruction if any of:**

- `pass_id` has reached `max_passes`
- L1 validators fail
- L2 weighted score `< 85` after 3 refinements → `needs_hitl`
- a `blocker` critique is unresolved → `needs_hitl`
- host returns `containment_stop`, `PERF_BUDGET_EXCEEDED`, or an envelope error
- goal is complete (`generation_prompt_spec` accepted: lock + 3 clips + negatives + still spec, no open majors)

### Pass 1 envelope (filled)

```json
{
  "document_id": "CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V2",
  "pass_id": "pass_01",
  "parent_pass_id": null,
  "correlation_id": "corr_macro_beauty_001",
  "authority_envelope_id": "env_v2_01",
  "first_called": "video.promptengineer",
  "reply_owner": "video.promptengineer",
  "goal": "Compile a generation_prompt_spec for an explicitly adult East Asian woman phone-macro skin study: reusable identity/skin/light lock + three I2V clip prompts (0-6 / 6-10 / 10-15) + negatives + still spec. Text only. No vendor call.",
  "inputs": {
    "brief_id": "macro-beauty-phone-sun-v1",
    "language_out": "zh-Hans shot-list + short en lock header",
    "aspect": "9:16",
    "family_duration_s": 15,
    "clip_split_s": [6, 4, 5],
    "mode": "i2v_from_locked_still",
    "adult_lock": true,
    "reference_brief": {
      "subject": "明确成年东亚女性，自然清冷型东方面孔，小巧自然鹅蛋脸，不追求网红模板式完美",
      "hair": "乌黑自然长发随意披散，发丝根根清晰，泄乱碎发与细小绒毛",
      "makeup": "极淡清透裸妆，原生眉毛流，深棕黑湿润眼球，自然细眼线与睛毛，禁止夸张假睛毛，淡珊瑚粉润唇褐",
      "skin_must_show": ["真实毛孔", "细小皮肤纹理", "轻微凹凸", "浅色雀斑", "细小色素点", "自然小痣", "轻微肤色不均", "鼻翼纹理", "眼下细纹", "皮脂高光", "面部细小绒毛"],
      "skin_must_not": ["传统AI美女无瑕皮肤", "美颜滤镜", "塑胶感"],
      "light": "强烈自然太阳直射，侧前方，鼻尖/风骨/唇部/额头镜面高光，发丝遮挡碎影，允许轻微过曝，禁止影棚柔光",
      "camera_grammar": "手机主摄或轻微长焦裁切，距离 10-20cm，贴脸缓慢微距探索，允许五官被画面边缘切掉，禁止大运镜推拉摇移",
      "performance": "不说话，轻微呼吸与眨眼，唇微分，最多 5-10 度自然转头",
      "do_not_one_pass_t2v": true
    },
    "prior_artifacts": []
  },
  "constraints": {
    "owns": ["generation prompts as structured specs", "subject/camera/light/negatives", "clip split"],
    "does_not_own": [
      "live vendor generation",
      "makeup continuity bible",
      "coverage intent",
      "lighting photometrics",
      "another agent's exclusive craft output without handoff"
    ],
    "allowed_tools": [],
    "network_access": false,
    "production_activation_requested": false,
    "memory_writes": "forbidden",
    "homogeneous_debate": false,
    "target_engines_design_time_only": ["grok-imagine-video-1.5", "grok-imagine-image"]
  },
  "induce_calls": [
    {
      "brief_id": "br_v2_01_dir",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.director",
      "objective": "Emit a 3-clip shot-intent card: 0-6 face-fill lateral, 6-10 nose+lips descent with legal crop-off, 10-15 one-eye ascent + 5-10 degree settle + last blink. No speech. No fifth beat.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels"]
    },
    {
      "brief_id": "br_v2_01_cin",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.cinematographer",
      "objective": "Lock light and lens language: hard sun from front-left, 10-20cm working distance, phone-main / mild-tele crop, authorized off-center cut, speculars on nose/cheekbone/lip/forehead, moving hair-stripe shadows, mild clip allowed. No studio softbox. Numbers not mood words.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels"]
    },
    {
      "brief_id": "br_v2_01_mua",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.mua_makeup",
      "objective": "Bare-makeup lock only: natural brows, thin liner, no fake lashes, pale coral gloss with lip texture. Do not author the pore manifesto.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels"]
    },
    {
      "brief_id": "br_v2_01_cam",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.cameraoperator",
      "objective": "Pick one motor per clip (planar crawl OR handheld micro-drift, not both). No crane, dolly reveal, or pullback to full portrait.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels"]
    },
    {
      "brief_id": "br_v2_01_cont",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.continuity",
      "objective": "Name the freeze list that must not drift across clips: mole site, freckle cluster, brow density, hair part, gloss wetness. No hiring, no pixels.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels"]
    },
    {
      "brief_id": "br_v2_01_crit",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.critic",
      "objective": "Critique the assembled spec for idol-template relapse, poreless skin, recentered full face, unplanned teeth, one-pass T2V packing. Not the closer.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels"]
    }
  ],
  "collaboration_rules": {
    "pattern": "prompt_spec_critique_bus",
    "closer": "video.promptengineer",
    "dispute_closer": "video.critic",
    "critic_isolation": true,
    "homogeneous_debate": false,
    "related_agents_may_induce": true,
    "related_agents_reply_to_operator": false,
    "first_called_consolidates_all_returns": true,
    "preserve_conflicts": true,
    "instruction_authority_on_bulletin": false
  },
  "consolidation_owner": "video.promptengineer",
  "next_instruction_required": true,
  "stop": {
    "max_passes": 3,
    "max_induce_fanout_per_pass": 7,
    "max_delegation_depth": 2,
    "on_blocker": "needs_hitl",
    "on_budget": "containment_stop",
    "on_goal_complete": "halt_and_return"
  }
}
```

---

## 5. What the first-called must emit (sole operator reply)

`video.promptengineer` replies **once**. The reply is the consolidation of all related-agent returns, plus the next instruction.

```json
{
  "agent_id": "video.promptengineer",
  "correlation_id": "corr_macro_beauty_001",
  "pass_id": "pass_01",
  "status": "ok | needs_refine | needs_hitl | failed | halted",
  "consolidated_response": {
    "summary": "string",
    "generation_prompt_spec": {
      "artifact_type": "generation_prompt_spec",
      "mode": "i2v_from_locked_still",
      "identity_skin_light_lock": "string",
      "clip_a_0_6": "string",
      "clip_b_6_10": "string",
      "clip_c_10_15": "string",
      "negatives": "string",
      "i2v_still_spec": "string",
      "parameters": {
        "aspect": "9:16",
        "clip_durations_s": [6, 4, 5],
        "resolution": "1080p",
        "model": "grok-imagine-video-1.5",
        "i2v_prompt_style": "motion_and_sound_only",
        "audio": "breath_and_faint_outdoor_air_only"
      }
    },
    "member_returns": [
      {
        "brief_id": "br_v2_01_dir",
        "agent_id": "video.director",
        "status": "ok",
        "artifact_ref": "artifact://macro-beauty/director/shot-intents",
        "summary": "string",
        "unsatisfied_constraints": [],
        "further_induce_calls": []
      }
    ],
    "conflicts": [],
    "handoffs_still_open": []
  },
  "l1": { "passed": true, "checks": [] },
  "l2": { "score": 0, "dimensions": [], "passed": false },
  "critiques_emitted": [],
  "handoffs": [],
  "evidence_refs": [],
  "refinement_count": 0,
  "next_instruction": { },
  "notes": "string"
}
```

### Consolidation rules

1. Every dispatched brief appears in `member_returns`, including failures and skips.
2. Grandchild induces are listed under that member’s `further_induce_calls` and rolled into Pass 2 if still needed.
3. The closer writes `generation_prompt_spec` in prompt-engineer voice. Peer crafts stay cited as `artifact_ref`.
4. `conflicts[]` keeps contradictory claims. Silent selection is a defect.
5. Only `video.promptengineer` fills `next_instruction`.
6. Pass 1 may leave clip strings as stubs if crafts are still inbound. Pass 2 must fill them.
7. Do not exceed a pasteable length. If the live token cap bites, emit the lock + clip A in the artifact and park B/C in `next_instruction.inputs`.

---

## 6. Sample next instruction (Pass 2) — same shape as Pass 1

Produced by `video.promptengineer` after Pass 1 craft returns. Same envelope. Goal advances from “collect locks” to “compile pasteable prompts.”

```json
{
  "document_id": "CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V2",
  "pass_id": "pass_02",
  "parent_pass_id": "pass_01",
  "correlation_id": "corr_macro_beauty_001",
  "authority_envelope_id": "env_v2_01",
  "first_called": "video.promptengineer",
  "reply_owner": "video.promptengineer",
  "goal": "Lock the reusable identity/skin/light block and emit three pasteable I2V clip prompts plus a short negative list. Still no vendor call.",
  "inputs": {
    "brief_id": "macro-beauty-phone-sun-v1",
    "locked_from_pass_1": {
      "adult_lock": true,
      "clip_split_s": [6, 4, 5],
      "camera_motors": {
        "clip_a": "slow planar lateral crawl",
        "clip_b": "slow planar descent",
        "clip_c": "slow planar ascent + 5-10 degree head settle"
      },
      "light": "hard sun front-left, hair-stripe shadows, mild clip legal",
      "makeup": "bare, natural brow, pale coral gloss, no fake lashes",
      "freeze": ["mole site", "freckle cluster", "hair part"],
      "open_risks": ["teeth flicker if lips part too far", "idol-template relapse if '清透' outranks pores"]
    },
    "prior_artifacts": [
      "artifact://macro-beauty/director/shot-intents",
      "artifact://macro-beauty/cinematographer/light-lens",
      "artifact://macro-beauty/mua_makeup/bare-lock",
      "artifact://macro-beauty/cameraoperator/motors",
      "artifact://macro-beauty/continuity/freeze-list",
      "artifact://macro-beauty/critic/pass_01"
    ]
  },
  "constraints": {
    "owns": ["generation prompts as structured specs", "subject/camera/light/negatives", "clip split"],
    "does_not_own": [
      "live vendor generation",
      "makeup continuity bible",
      "coverage intent",
      "lighting photometrics",
      "another agent's exclusive craft output without handoff"
    ],
    "allowed_tools": [],
    "network_access": false,
    "production_activation_requested": false,
    "memory_writes": "forbidden",
    "homogeneous_debate": false
  },
  "induce_calls": [
    {
      "brief_id": "br_v2_02_crit",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.critic",
      "objective": "Re-critique compiled lock + three clip prompts for template-face, pore crawl wording, recentered composition, and one-pass packing.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels"]
    },
    {
      "brief_id": "br_v2_02_cont",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.continuity",
      "objective": "Confirm freeze list is named in the lock block so A/B/C cannot drop the mole or freckle cluster.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels"]
    }
  ],
  "collaboration_rules": {
    "pattern": "prompt_spec_critique_bus",
    "closer": "video.promptengineer",
    "dispute_closer": "video.critic",
    "critic_isolation": true,
    "homogeneous_debate": false,
    "related_agents_may_induce": true,
    "related_agents_reply_to_operator": false,
    "first_called_consolidates_all_returns": true,
    "preserve_conflicts": true,
    "instruction_authority_on_bulletin": false
  },
  "consolidation_owner": "video.promptengineer",
  "next_instruction_required": true,
  "stop": {
    "max_passes": 3,
    "max_induce_fanout_per_pass": 7,
    "max_delegation_depth": 2,
    "on_blocker": "needs_hitl",
    "on_budget": "containment_stop",
    "on_goal_complete": "halt_and_return"
  }
}
```

Pass 3, if emitted, only tightens wording against critic majors or splits B/C out if the token cap truncated them. Then stop. The operator pastes the still spec into Grok Imagine Image, then each clip motion brief into Grok Imagine Video 1.5 I2V. Agents never press generate.

---

## 7. Worked Grok Imagine pack (what Pass 2 should resemble)

First-called may refine this. Density target only. **Not an API grant.**

Imagine 1.5 grammar this sample must follow:

- Model: `grok-imagine-video-1.5` for clips. Still: `grok-imagine-image` (quality / 2.0 if the operator has it).
- `aspect_ratio`: `9:16` **explicit**. Default is `16:9`.
- `resolution`: `1080p` on I2V. There is **no 4K** path. Do not write 4K.
- `duration`: 1–15s. This family stays `6 / 4 / 5` so identity survives. A single 15s I2V is optional Pass 3 only.
- I2V prompt = **what moves + `Sound:`**. Do not re-describe the face. The still already locked identity.
- Imagine has no `negative_prompt` field. Put avoids in one `Avoid:` sentence on every clip.
- One camera verb per clip.

**Still — Grok Imagine Image, 9:16 (this becomes `@image1`):**

```text
9:16 vertical phone photo, explicitly adult East Asian woman, cool natural oval face
not an idol template, loose black hair with individual strands and baby hairs across
the forehead, bare makeup, real brow hairs, dark wet brown eyes, thin liner, no fake
lashes, slim nose with a hard sun specular on the tip, soft coral glossy lips with
visible texture. Skin un-beautified: pores on cheek and nose wing, fine grain, light
freckles, one small mole, under-eye creases, sebum sheen, vellus hair. Hard noon sun
from front-left, stripe shadows from hair, slight highlight clip. Extreme close-up
10-20cm, off-center, features may be cut by the frame. Photoreal live-action phone still.
```

**Clip A — Imagine I2V · 6s · 9:16 · 1080p · `@image1` first frame:**

```text
Animate the still. Camera creeps slowly sideways across the face toward the eye and
cheek, 10-20cm, handheld micro-move only. She stays quiet, breathes, blinks once.
No head turn.
Sound: close breath, faint outdoor noon air, no music, no speech.
Avoid: studio softbox, beauty filter, poreless skin, idol-template face, fake lashes,
centered full-face pullback, dialogue, music, morphing face.
```

**Clip B — Imagine I2V · 4s · 9:16 · 1080p · `@image1` or last frame of A:**

```text
Animate the still. Camera creeps slowly down to nose tip, nose wing, both lips and
one cheek. Forehead and eyes may leave the frame. Lips part 1-2mm, teeth only suggested.
Sound: close breath, no music, no speech.
Avoid: studio softbox, beauty filter, poreless skin, extra teeth, dialogue, music.
```

**Clip C — Imagine I2V · 5s · 9:16 · 1080p · last frame of B preferred:**

```text
Animate the still. Camera creeps slowly back up the nose bridge to one eye. Head
settles 5-10 degrees. A few black strands fall into frame. She looks beside the lens
then back. Last blink. Hold one second.
Sound: close breath, faint outdoor air, no music, no speech.
Avoid: studio softbox, beauty filter, poreless skin, crane, pullback, dialogue, music.
```

**Parameters (paste beside each clip; agents do not send this to an API):**

```json
{
  "model": "grok-imagine-video-1.5",
  "mode": "i2v",
  "aspect_ratio": "9:16",
  "resolution": "1080p",
  "duration_s": { "clip_A": 6, "clip_B": 4, "clip_C": 5 },
  "generate_audio": true,
  "do_not_call_from_agent": true
}
```

---

## 8. How to use

1. POST Pass 1 to host Chat/Run for `video.promptengineer`.
2. Host dispatches the induce-calls. Related agents do not answer you.
3. Expect one consolidated `generation_prompt_spec` plus a Pass 2 envelope.
4. Feed Pass 2 back to the same first-called agent.
5. When stop fires: generate `@image1` with Grok Imagine Image from `i2v_still_spec`. Then run clip A/B/C as Imagine I2V with the motion brief + `Sound:` line. Do not re-describe the face in the I2V prompt.

This sample is characterization-only. HTTP 200 does not mean the packaged agent answered correctly.

Related: [`sample-instruction.md`](./sample-instruction.md) (v1, first-called `video.showrunner`, writers-room packet).
