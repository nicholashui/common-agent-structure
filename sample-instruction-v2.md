# Sample Instruction Pass v2 — Grok Imagine Prompt Family

**Document ID:** `CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V2`  
**Date:** `2026-09-12`  
**Host:** `common-agent-structure` (`casops.common_agent.v3` / schema `3.0`)  
**Parent sample:** [`sample-instruction.md`](./sample-instruction.md) (`CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V1`)  
**First-called agent:** `video.promptengineer`  
**Artifact type:** `generation_prompt_spec`  
**Target engine (design-time only):** `grok-imagine-video-1.5` + first-frame still via `grok-imagine-image-quality`  
**Status:** Sample operator instruction. Does **not** change `agent_spec.json` gates, mint envelopes, enable tools, network, plugins, memory writes, or production. Does **not** call Grok Imagine, Seedance, Kling, Veo, Sora, or Runway.

This file is the instruction you pass **to** `video.promptengineer`. It is not a second control plane. The host remains the only orchestrator.

Same protocol as v1: induce related agents → they may induce peers → collaborate → first-called consolidates all returns → emit the next instruction in the same envelope.

---

## 1. Purpose

Pass this envelope to `video.promptengineer` so that agent:

1. **Stays first-called.** Only `video.promptengineer` replies to the operator.
2. **Induces** related crafts through host-mediated typed handoffs (`video.director`, `video.cinematographer`, `video.mua_makeup`, `video.cameraoperator`, `video.continuity`, `video.critic`). Related agents may induce their own related agents inside the hop budget.
3. Makes those agents **collaborate**. They do not reply to the operator and do not absorb exclusive crafts.
4. Replies **once** with a **consolidated `generation_prompt_spec`** written for **Grok Imagine**: first-frame still prompt + three I2V motion briefs + Sound lines + parameters.
5. **Generates the next instruction** in the **same shape** as this one.

Target look (operator reference, not a vendor job):

- Family of three Grok Imagine clips that cover 15s of action
- `aspect_ratio=9:16`, `resolution=1080p` on I2V if the lane allows, else `720p`
- No 4K. Imagine Video 1.5 tops out at 1080p (T2V/I2V) and 720p (reference-to-video)
- explicitly adult East Asian woman, anti-idol-template face
- hard side-front sun, authorized off-center crop, pores/vellus/sebum visible
- Imagine grammar: still lock on the image; video prompt says **only what moves**

---

## 2. Pass contract (self-similar)

Same envelope keys as v1. Only `document_id`, `first_called`, and the goal change.

```json
{
  "document_id": "CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V2",
  "pass_id": "pass_01",
  "parent_pass_id": null,
  "correlation_id": "corr_macro_beauty_imagine_001",
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
| Output dialect | Grok Imagine shot brief: Subject/still lock in 中文 or EN; I2V clips in motion-only language + `Sound:` + `N seconds, 9:16`. |
| Engine | `grok-imagine-video-1.5`. Still: `grok-imagine-image-quality`. Not Seedance / Kling / Veo. |

---

## 3. Hard constraints (do not violate)

- Public plane is `/api/v3` only. No second control plane.
- `allowed_tools: []`. `grok-imagine-video-1.5` is a **design-time target name**, not an API grant.
- `network_access: false`. `production_activation_requested: false`.
- Memory writes forbidden. Plugins / T3 off.
- Imagine Video 1.5: `duration` 1–15s, `aspect_ratio` includes `9:16`, `resolution` `480p` \| `720p` \| `1080p`. **No 4K.**
- I2V prompt must not re-describe the still. Describe motion, camera, and sound only.
- Every Imagine clip prompt ends with `Sound:` and `N seconds, 9:16`.
- Default audio is on. If the brief wants no music / no speech, write that in `Sound:` or set operator-side `generate_audio=false`.
- T2V on 1.5 is internally image-then-I2V. Prefer explicit still + I2V so identity does not lottery.
- Reference-to-video (1–7 refs) is 720p max and cannot replace a first-frame lock. Use I2V for this job.
- Subject is **explicitly adult**. Refuse any reading that drops the adult lock.
- Do not invent stills, logs, fetches, measured scores, or live API results.
- Do not generate the video. Artifact is text only.

---

## 4. Sample Pass 1 — instruction you hand to `video.promptengineer`

Copy from **Instruction** through the Pass 1 JSON and pass it as the host task / operator message.

### Instruction

You are the **first-called** agent for this pass: `video.promptengineer`.

**Goal.** Emit a `generation_prompt_spec` a human can paste into **Grok Imagine**:

1. one `grok-imagine-image-quality` still prompt (9:16 first frame)
2. three `grok-imagine-video-1.5` I2V motion briefs (clip A 6s, B 4s, C 5s)

Own only model-facing prompt structure. Induce director / DoP / MUA / camera / continuity / critic for the rest. Do not call Imagine.

**Imagine packaging rules (must follow):**

- Still prompt = who / skin / light / crop. No motion.
- Each I2V prompt = what moves + one camera verb + `Sound:` + duration + `9:16`.
- Do not repeat the face novel inside the I2V prompts.
- One camera verb per clip. No crane, no dolly reveal, no pullback to a full portrait.
- Drop the original 4K claim. Write `resolution=1080p` (I2V) or `720p` if 1080p is unavailable.
- No speech. Sound is breath, faint outdoor air, cloth/hair only.

**Induce at least:** `video.director`, `video.cinematographer`, `video.mua_makeup`, `video.cameraoperator`, `video.continuity`, `video.critic`.

**Collaboration paragraph (include in every brief):**

> You are not first-called. Return your craft artifact to the host. If you need a peer craft you do not own, emit a further `induce_call`. Do not reply to the operator. Do not mint envelopes. Do not claim tools, network, or production. Do not generate pixels. `instruction_authority` remains false.

### Pass 1 envelope (filled)

```json
{
  "document_id": "CASOPS-INS-VIDEO-SAMPLE-INSTRUCTION-V2",
  "pass_id": "pass_01",
  "parent_pass_id": null,
  "correlation_id": "corr_macro_beauty_imagine_001",
  "authority_envelope_id": "env_v2_01",
  "first_called": "video.promptengineer",
  "reply_owner": "video.promptengineer",
  "goal": "Compile a Grok Imagine generation_prompt_spec: 9:16 still prompt for grok-imagine-image-quality plus three I2V motion briefs for grok-imagine-video-1.5. Text only. No vendor call.",
  "inputs": {
    "brief_id": "macro-beauty-phone-sun-imagine-v1",
    "engine": "grok-imagine-video-1.5",
    "still_engine": "grok-imagine-image-quality",
    "language_out": "zh-Hans still lock + Imagine I2V motion briefs",
    "aspect_ratio": "9:16",
    "resolution": "1080p",
    "family_duration_s": 15,
    "clip_split_s": [6, 4, 5],
    "mode": "imagine_i2v_from_locked_still",
    "adult_lock": true,
    "reference_brief": {
      "subject": "明确成年东亚女性，自然清冷型东方面孔，小巧自然鹅蛋脸，不追求网红模板式完美",
      "hair": "乌黑自然长发随意披散，发丝根根清晰，泄乱碎发与细小绒毛",
      "makeup": "极淡清透裸妆，原生眉毛流，深棕黑湿润眼球，自然细眼线与睛毛，禁止夸张假睛毛，淡珊瑚粉润唇",
      "skin_must_show": ["真实毛孔", "细小皮肤纹理", "轻微凹凸", "浅色雀斑", "细小色素点", "自然小痣", "轻微肤色不均", "鼻翼纹理", "眼下细纹", "皮脂高光", "面部细小绒毛"],
      "skin_must_not": ["传统AI美女无瑕皮肤", "美颜滤镜", "塑胶感"],
      "light": "强烈自然太阳直射，侧前方，鼻尖/风骨/唇部/额头镜面高光，发丝遮挡碎影，允许轻微过曝，禁止影棚柔光",
      "camera_grammar": "手机主摄或轻微长焦裁切，距离 10-20cm，贴脸缓慢微距探索，允许五官被画面边缘切掉，禁止大运镜推拉摇移",
      "performance": "不说话，轻微呼吸与眨眼，唇微分，最多 5-10 度自然转头"
    }
  },
  "constraints": {
    "owns": ["Grok Imagine prompt specs", "subject/camera/light/sound/negatives", "clip split"],
    "does_not_own": ["live Imagine generation", "makeup continuity bible", "coverage intent", "lighting photometrics"],
    "allowed_tools": [],
    "network_access": false,
    "production_activation_requested": false,
    "memory_writes": "forbidden",
    "target_engines_design_time_only": ["grok-imagine-video-1.5", "grok-imagine-image-quality"]
  },
  "induce_calls": [
    {
      "brief_id": "br_v2_01_dir",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.director",
      "objective": "3-clip shot-intent card for Imagine I2V: 6s face-fill lateral, 4s nose+lips descent with legal crop-off, 5s one-eye ascent + 5-10 degree settle + last blink. No speech.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels", "call Grok Imagine"]
    },
    {
      "brief_id": "br_v2_01_cin",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.cinematographer",
      "objective": "Lock light/lens for Imagine still + I2V: hard sun front-left, 10-20cm, phone-main crop, authorized off-center cut, speculars, hair-stripe shadows, mild clip. No softbox. No 4K claim.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels", "call Grok Imagine"]
    },
    {
      "brief_id": "br_v2_01_mua",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.mua_makeup",
      "objective": "Bare-makeup lock for the Imagine still only: natural brows, thin liner, no fake lashes, pale coral gloss with lip texture.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels", "call Grok Imagine"]
    },
    {
      "brief_id": "br_v2_01_cam",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.cameraoperator",
      "objective": "One Imagine camera verb per clip (planar crawl OR handheld micro-drift, not both). No crane, dolly reveal, or pullback.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels", "call Grok Imagine"]
    },
    {
      "brief_id": "br_v2_01_cont",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.continuity",
      "objective": "Freeze list that the Imagine still must already contain: mole site, freckle cluster, brow density, hair part, gloss wetness.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels", "call Grok Imagine"]
    },
    {
      "brief_id": "br_v2_01_crit",
      "from_agent_id": "video.promptengineer",
      "to_agent_id": "video.critic",
      "objective": "Critique Imagine packaging: I2V that re-describes the still, missing Sound line, 4K claim, idol-template face, poreless skin, recentered full face, unplanned teeth.",
      "must_cite": true,
      "return_schema": "delegation/return.schema.json",
      "max_tokens_return": 800,
      "authority_envelope_id": "env_v2_01",
      "sub_deadline_ms": 12000,
      "forbidden": ["rewrite owner SPEC", "call undeclared tools", "widen scope", "reply to operator", "generate pixels", "call Grok Imagine"]
    }
  ],
  "collaboration_rules": {
    "pattern": "prompt_spec_critique_bus",
    "closer": "video.promptengineer",
    "dispute_closer": "video.critic",
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

## 5. First-called reply schema

```json
{
  "agent_id": "video.promptengineer",
  "correlation_id": "corr_macro_beauty_imagine_001",
  "pass_id": "pass_01",
  "status": "ok | needs_refine | needs_hitl | failed | halted",
  "consolidated_response": {
    "generation_prompt_spec": {
      "artifact_type": "generation_prompt_spec",
      "engine": "grok-imagine-video-1.5",
      "still_engine": "grok-imagine-image-quality",
      "mode": "imagine_i2v_from_locked_still",
      "still_prompt": "string",
      "clip_a_i2v": "string",
      "clip_b_i2v": "string",
      "clip_c_i2v": "string",
      "negatives": "string",
      "parameters": {
        "model": "grok-imagine-video-1.5",
        "aspect_ratio": "9:16",
        "resolution": "1080p",
        "clip_durations_s": [6, 4, 5],
        "generate_audio": true,
        "audio_directive": "breath and faint outdoor air only, no music, no speech"
      }
    },
    "member_returns": [],
    "conflicts": []
  },
  "next_instruction": {}
}
```

Pass 2 keeps this envelope and freezes the four pasteable strings (`still_prompt` + three I2V briefs). Then stop. The operator pastes them into Grok Imagine. Agents never press generate.

---

## 6. Worked Grok Imagine prompts (density target for Pass 2)

These are what the first-called should resemble after consolidation. Design-time only.

### 6.1 Still — paste into `grok-imagine-image-quality`

```text
9:16 vertical phone still, explicitly adult East Asian woman, natural cool oval face,
not an idol template. Black hair loose, individual strands and baby hairs falling near
the forehead and one eye. Minimal bare makeup, real brow hairs, dark brown wet eyes,
thin natural liner, no fake lashes. Slim nose with a hard sun specular on the tip.
Soft coral lips, thin gloss, visible lip texture. Lips parted 1-2mm, teeth only suggested.

Skin un-beautified: pores on cheek and nose wing, fine grain, slight uneven tone,
light freckles, tiny pigment dots, one small mole, under-eye creases, sebum sheen,
facial vellus hair. Clean and healthy, not poreless.

Hard natural sunlight from front-left. Speculars on nose, cheekbone, lip, forehead.
Hair casts stripe shadows. Slight highlight clipping allowed. No studio soft light.
No beauty filter.

Extreme close-up, camera 10-20cm from skin, three-quarter angle showing one eye,
nose bridge, nose tip, both lips, part of one cheek. Off-center crop legal. Features
may be cut by the frame edge. No wide shot. No centered full-face beauty portrait.
```

### 6.2 Clip A — I2V 6s (`duration=6`, `aspect_ratio=9:16`, `resolution=1080p`)

Use the still as the first frame. Do not re-describe the face.

```text
Keep this frame. Slow planar crawl from the three-quarter face toward the near eye
and cheek. Subject stays still. Only breath and one small blink. Sun-stripe shadows
from hair drift a little across the cheek. No pullback. No new people.
Sound: quiet breath, faint outdoor noon air, no music, no speech.
6 seconds, 9:16.
```

### 6.3 Clip B — I2V 4s

Start from clip A last frame or a still cropped to nose + mouth.

```text
Keep identity, skin, and hard sun. Slow planar descent until nose tip, nose wing,
both lips and one cheek fill the frame. Forehead and eyes may exit. Lips stay parted
1-2mm. Gloss picks up the sun. Teeth only suggested. No smile performance.
Sound: quiet breath, faint outdoor air, no music, no speech.
4 seconds, 9:16.
```

### 6.4 Clip C — I2V 5s

```text
Keep identity, skin, and hard sun. Slow planar ascent from the mouth along the nose
bridge to one eye. Head settles 5-10 degrees, not a pose. A few black strands drift
into frame and cast stripe shadows across the eye. Last small blink. Hold one second.
Sound: quiet breath, faint outdoor air, no music, no speech.
5 seconds, 9:16.
```

### 6.5 Negatives / operator exclusions

```text
studio softbox, beauty filter, poreless skin, plastic skin, idol-template face,
fake lashes, overdrawn liner, centered full-face composition, wide shot, camera
pullback, dialogue, music, singing, morphing face, extra teeth, subtitle, watermark
```

---

## 7. How to run outside the host

1. POST Pass 1 to `/api/v3` Chat/Run for `video.promptengineer`.
2. Host dispatches induce-calls. Related agents do not answer you.
3. Feed Pass 2 back if clip strings are still stubs.
4. When stop fires, operator workflow:
   - Generate the still with `grok-imagine-image-quality`, 9:16.
   - Run clip A as image-to-video on `grok-imagine-video-1.5` (`duration=6`, `aspect_ratio=9:16`, `resolution=1080p`).
   - Repeat for B and C. Optionally use each clip’s last frame as the next first frame.
5. Agents never call Imagine. HTTP 200 does not mean the packaged agent answered correctly.

Related: [`sample-instruction.md`](./sample-instruction.md) (v1, first-called `video.showrunner`).
