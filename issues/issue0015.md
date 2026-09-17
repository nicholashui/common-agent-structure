# ISSUE-0015 — YouTube: AI facial + micro-expression atlas

**Status:** Plan. Not implemented. Next issue after ISSUE-0014 (RSI stays deferred; this issue does not wait on models-complete).  
**Severity:** High (operator content + Program production; unbounded “ALL” will fail if treated as one prompt)  
**Component:** Program (`casops.program.v1`), child Project Chat Auto Pilot, visual bible stills, Grok Imagine I2V, `video.director` beats, `video.mua_makeup` face finish, `video.continuity` identity, `video.cameraoperator` angle, `video.cinematographer` look  
**Observed:** 2026-09-16  
**Operator statement:** Create a YouTube on how to use AI to generate **all** facial expressions and **micro** facial expressions on a human, in every situation, every personality, every shooting angle, every movie style. Give a plan on how to do it and what to do. Output as next issue.  
**Related:** ISSUE-0013 (Program filmmaking W0–W6), ISSUE-0007 (clip Auto Pilot + five human locks), ISSUE-0009 (one pass = one clip; unique T4 blocks), ISSUE-0010–0012 (still owns look, motion owns change), `spec/video_generation_prompt_specification.v2.md` §17, `spec/grok_imagine_operation_guide.md`, ISSUE-0014 (hop-policy RSI — **do not** start here).  
**Honesty:** CHARACTERIZATION until Dry-run is off and takes exist. Not an eval PASS. `sample/` never written. Dry-run default. Only `grok-imagine` / `grok-image` are live; other tags stay fail-closed. Skills and citations declared, not live grants. `fused_request` stays null. Gold-body probes never sent to agents or vendors. Unique T4 blocks stay unique (Hair ≠ Subject ≠ Skin). Synthetic-media disclosure on YouTube is required. No real-person likeness without rights. Psychological-profile is creative-workflow traits, not clinical diagnosis.

This issue is the **plan**: YouTube series architecture + CASS Program production method. It does not create a Program folder, does not spawn Projects, and does not call Imagine.

---

## 0. Goal (honest)

You cannot put “every expression, every situation, every personality, every angle, every style” in **one** generate. That cartesian product is unbounded and will collapse identity, light, and performance into tag soup.

**What “all” means here:** a **finite, labeled atlas** you can grow. Each cell is one clip. YouTube teaches the **method** (one variable per generate) and shows the **catalog** (chapters / Shorts / playlist), not a magic prompt.

```text
Lock ONE identity (visual bible rest face)
  → still = look + angle + style (frozen)
  → motion = only the face change (AU / micro / blink)
  → one cell = one Project = one collab pass
  → NLE concat + on-screen labels = YouTube atlas
```

**Thesis for the video:** AI does not “act.” You **isolate one facial variable**, keep identity locked, and compile still vs motion. That is how you cover the grid without melting the face.

---

## 1. What to make (YouTube)

Not one 10-minute “watch me type a prompt.” A **series + one method film**.

| Piece | Length | Job |
|---|---|---|
| **Ep 0 — Method** | 12–20 min, 16:9 | How the atlas works. One variable per clip. Still then I2V. Why one prompt fails. |
| **Ep 1 — Macro emotions** | 8–12 min | Ekman 7 + rest, one identity, locked camera, one style. |
| **Ep 2 — Microexpressions** | 8–12 min | Same 7, 40–500 ms beats. Slow-mo / hold last frame. Label duration. |
| **Ep 3 — Angles** | 8–12 min | One expression (e.g. AU12 smile) × coverage grid. |
| **Ep 4 — Movie styles** | 8–12 min | One expression × look bible (noir, golden hour, documentary, anime, neon, 35mm drama, …). |
| **Ep 5 — Personality as modifier** | 8–12 min | Same AU, different Big Five / HEXACO **performance** (social smile vs Duchenne vs smirk). Not a psych diagnosis. |
| **Ep 6 — Situation** | 8–12 min | Same face, different *why* (lie, reunion, threat, joke, grief). Situation chooses AU combo; still not “all of life.” |
| **Shorts** | 15–60 s, 9:16 | One cell each. Title = label (`AU4 brow lowerer · ECU · noir`). |
| **Atlas cut** | 20–40 min | Grid montage + chapter markers. Companion to Ep 0. |

**Titles (honest):** “How we built an AI face atlas (one variable per clip)” — not “AI generates every human expression forever.”

**On-screen label every take:** identity id · FACS / micro id · duration · angle · look · situation · personality modifier. If a take cannot be labeled, it is not in the atlas.

**Delivery spec (W6, lock in W0):** YouTube long-form 16:9 24fps; Shorts 9:16; captions on; synthetic-media disclosure in description and spoken in Ep 0; no live upload from the host.

---

## 2. What “all” is made of (finite axes)

Do **not** implement a full factorial in v1. Build **layers**. Each layer freezes the other axes.

### 2.1 Expression (the thing that changes)

Use **FACS Action Units** as the scientific spine (Ekman & Friesen). Macros are AU *chords*. Micros are the same chords at 40–500 ms.

| Layer | Cells (v1) | Notes |
|---|---|---|
| Rest | 1 | Neutral / bare face. The identity still. Required before any motion. |
| Macro (Ekman 7) | 7 | Happiness, sadness, anger, fear, surprise, disgust, contempt. |
| FACS singles (core) | ~20 | AU1, 2, 4, 5, 6, 7, 9, 10, 12, 14, 15, 17, 20, 23, 24, 25, 26, 27, 43, 45 (blink). |
| Micro | 7 | Same as macros; beat window in `action.beats` (e.g. 0.00–0.20 s). |
| Combos (later) | small set | e.g. AU4+AU7 (anger), AU1+AU2+AU5+AU26 (surprise). Do not enumerate all 2^n. |

**Owner of the change:** `video.director` → `creative.shots[].action.beats` (coverage / performance).  
**Owner of face finish:** `video.mua_makeup` → `creative.shots[].subjects[].scene_state` (Makeup heading).  
**Owner of identity:** `video.continuity` → Subject / Hair / Skin (unique blocks).  
**Owner of emotion-over-the-piece:** `video.emotionalarc` (valence/arousal of the *YouTube episode*, not the AU).  
Do not let PE write the face novel. Do not let MUA overwrite Hair/Subject.

### 2.2 Shooting angle (camera, not expression)

v1 coverage grid (locked-off unless the *angle* is the variable):

| Code | Shot |
|---|---|
| `ecu-eyes` | Extreme close-up eyes |
| `ecu-mouth` | Extreme close-up mouth |
| `cu` | Close-up face |
| `mcu` | Medium close-up |
| `three-quarter` | 3/4 view |
| `profile-l` / `profile-r` | True profile |
| `high` / `low` | High / low angle |
| `ots` | Over-shoulder (later; needs a second body or empty foreground) |

**Owner:** `video.cameraoperator` → `creative.shots[].camera`.  
**Rule:** When the atlas cell is an *expression*, camera is locked. When the cell is an *angle*, expression is locked (usually rest or AU12). **One camera move per clip** (Imagine SOP). For micros, prefer **no** camera move.

### 2.3 Movie style (look, not plot)

v1 look bible (named references in the *still*, not tag soup):

| Code | Look |
|---|---|
| `studio-soft` | Soft key, clean beauty |
| `noir` | Hard key, deep shadow |
| `golden-hour` | Warm raking sun |
| `doc-handheld` | Overhead fluorescent / mixed; style in still; motion still locked for expression cells |
| `anime` | Stylized; identity lock harder — call it out in Ep 4 |
| `neon-night` | Practical neon, cool fill |
| `35mm-drama` | 50–85mm look, shallow |
| `wuxia` | From Imagine style recipes; optional |

**Owner:** `video.cinematographer` → lighting + look. Style lives in the **still**. Motion does not restate “cinematic, 8k, masterpiece.”

### 2.4 Personality (modifier, not a new face)

`specials.psychological-profile-agent`: Big Five / HEXACO for **creative-workflow**, never DSM, never a patient record, never invented NEO scores.

Personality does **not** mint a new identity. It changes *how the same AU is performed* (amplitude, onset, whether AU6 joins AU12, eye contact).

v1: three modifiers on one AU (smile): `open-warm`, `social-polite`, `held-back`. Map loosely to extraversion / agreeableness / neuroticism in VO, not as clinical labels.

### 2.5 Situation (why the AU fires)

Closed catalog, not “every situation in life”:

`rest`, `told-a-lie`, `hears-a-joke`, `sees-a-threat`, `reunion`, `grief-news`, `interview-pause`, `first-look-at-camera`.

Situation selects an AU chord + timing. It is a **generation-list column**, not extra prompt adjectives piled on identity.

### 2.6 Volume (do not explode)

Full factorial of (57 expressions × 8 angles × 8 styles × 3 personalities × 8 situations) ≈ **87k clips**. That is not v1.

| Pass | Frozen | Variable | Approx cells | YouTube |
|---|---|---|---|---|
| **A** | 1 identity, `cu`, `studio-soft`, rest personality | Rest + 7 macros + 7 micros | 15 | Ep 1–2 |
| **B** | 1 identity, `cu`, `studio-soft` | ~20 FACS singles | 20 | Atlas appendix |
| **C** | 1 identity, AU12, `studio-soft` | Angle grid | 8–10 | Ep 3 |
| **D** | 1 identity, AU12, `cu` | Style grid | 8 | Ep 4 |
| **E** | 1 identity, AU12, `cu`, `studio-soft` | 3 personality modifiers | 3 | Ep 5 |
| **F** | 1 identity, `cu`, `studio-soft` | 8 situations | 8 | Ep 6 |
| **v1 total** | | | **~60–70 Projects** | Series + atlas cut |

Grow later by adding identities (age / ancestry / skin) as **new visual bibles**, not by mixing faces in one clip.

---

## 3. How to do it in CASS (ISSUE-0013 mapped)

Program = the atlas series. Project = one cell. Same W0–W6. Screenplay is still not step 1.

```text
W0  Brief: “Face Atlas YouTube — one identity, one variable per clip”
    intent-analysis → creative-agent → video.showrunner
    LOCK logline + format (16:9 method + 9:16 Shorts)
    specials.psychological-profile-agent: modifier list only (optional)

W1  video.screenwriter: Ep 0 VO + episode run-of-show (not a feature screenplay)
    video.emotionalarc: episode valence only
    LOCK pages (the VO / slate script)

W2  Breakdown → generation list (one row per cell: scene=axis, segment=cell)
    video.avatardesign + continuity: identity stills (rest, 3/4, profile, eyes, mouth)
    video.mua_makeup: bare-face lock (no beauty filter, no fake lashes unless a cell asks)
    video.director: beat grammar (onset / peak / offset; micro windows)
    video.cinematographer: look bible stills
    video.cameraoperator: angle stills from the rest face
    video.storyboard: 1 panel per cell
    LOCK generation_list AND visual_bible

W3  Host Spawn: one Project per segment (~60–70 for v1)
    Child Start inherits bible/board refs. No sample/ copy.

W4  Each child: existing Auto Pilot
    first hop intent-analysis → creative-agent → video.promptengineer
    five human locks: PE, director, cinematographer, mua, continuity
    Still (grok-image / Imagine still) then I2V (grok-imagine)
    Fail-closed tags do not pretend success
    Cameraoperator + critic agent-to-agent

W5  video.editor: assembly in **atlas order** (not shoot order)
    Titles/slates with labels. Picture lock before color/grade.
    fused_request stays null. Concat is post.

W6  Captions, YouTube description disclosure, archive
    No live upload from host
```

**House rules for this Program (add to showrunner / director / PE / mua / continuity prompts when implementing):**

1. **One variable per clip.** Expression cells freeze camera and look. Angle cells freeze expression. Style cells freeze expression and camera.
2. **Rest still is the parent.** Every I2V starts from the approved rest (or the approved still for that angle/style). Do not restyle identity in motion.
3. **Still = look. Motion = change only.** Micro: motion text is the AU onset/offset, not a new portrait.
4. **Front-load the subject** in the still. No tag soup.
5. **Unique blocks stay unique.** Hair ≠ Subject ≠ Skin. Makeup does not rewrite identity.
6. **Duration is a parameter**, not craft prose. Micros need short `generation.duration_s` and numeric `beats.start_s` / `end_s`.
7. **Do not paste the whole atlas into one prompt.** `fused_request` null.
8. **Identity lock before any AU.** Changing the face to “make anger read” is a failed take, not a new character.
9. **No real celebrity / private person likeness.** Atlas identity is a **synthetic** bible (`video.avatardesign` + continuity). Ethics + compliance review before publish.
10. **Label or discard.** Unlabeled takes do not ship.

---

## 4. Generation list shape (W2 table)

Scene = axis. Segment = cell.

| scene_id | title | segment_id | purpose | duration_s | angle | look | au | micro | personality | situation |
|---|---|---|---|---|---|---|---|---|---|---|
| sc-macro | Macro emotions | seg-hap | AU12+AU6 peak | 6 | cu | studio-soft | 12+6 | no | — | rest |
| sc-micro | Micros | seg-hap-μ | AU12+AU6 flash | 2 | cu | studio-soft | 12+6 | yes | — | rest |
| sc-angle | Angles | seg-au12-profile | AU12 held | 4 | profile-l | studio-soft | 12 | no | — | rest |
| sc-look | Styles | seg-au12-noir | AU12 held | 4 | cu | noir | 12 | no | — | rest |
| sc-trait | Personality | seg-au12-held | AU12 low amplitude | 4 | cu | studio-soft | 12 | no | held-back | rest |
| sc-sit | Situation | seg-lie | AU12 without AU6 | 6 | cu | studio-soft | 12 | no | social-polite | told-a-lie |

Empty scenes cannot lock (ISSUE-0013 P3). Every scene ≥ 1 segment. One segment = one Project.

Suggested Program **code** `face-atlas`, **name** Face Atlas — create only when implementing, not in this pass.

---

## 5. Child clip craft (W4)

Five human locks unchanged. Field owners:

| Heading | Owner | This atlas |
|---|---|---|
| Subject / Hair / Skin | `video.continuity` | Same identity hashes across all cells |
| Makeup | `video.mua_makeup` | Bare face unless the cell is a makeup change (v1: none) |
| Coverage / performance | `video.director` | AU / micro beat only |
| Light / look | `video.cinematographer` | From look bible still |
| Camera lock | `video.cameraoperator` | From angle still; locked-off for expression cells |
| Frame | `video.promptengineer` | duration / aspect; does not invent AU |
| Negatives | `video.critic` | Identity drift, beauty-filter, extra heads, camera move on micros |

**I2V split (ISSUE-0010):**

- Still: rest (or angle/style still) — identity, light, lens, wardrobe frozen.
- Motion: “The brow lowers (AU4) then holds; no camera move; no new light.”

**Microexpressions:** treat as a **beat window**, not a different identity. If Imagine’s minimum duration is longer than the micro, generate the short flash then hold rest; editor slates the flash. Do not slow the whole clip in-camera if that invents motion.

**Lipsync:** out of v1 unless a later episode is visemes (`video.lipsync`). Face atlas is silent or room tone; VO lives on Ep 0, not on cells.

---

## 6. YouTube production checklist (operator)

### 6.1 Before any generate

1. Write Ep 0 outline (method, not results).
2. New Program `face-atlas` / Face Atlas (code + name only at create).
3. Lock logline: one synthetic identity; one variable per clip; YouTube atlas.
4. Shoot/generate **identity bible stills** (rest, 3/4, profile, ECU eyes, ECU mouth) with Dry-run off only when ready. Approve hashes.
5. Fill generation list Pass A only. Lock list + bible. Spawn.

### 6.2 Per cell

1. Open child Project Chat. Keep Dry-run on for hops; off only for the take.
2. Confirm still is the parent bible (or the angle/style still), not a new face.
3. Director beat = the AU. MUA = no beauty filter. Continuity = identity.
4. Generate still if needed, then I2V. Fail-closed engines stay blocked.
5. Accept or reject. Identity drift → reject, do not “fix in prompt” by changing the person.

### 6.3 After Pass A

1. Assembly with slates. Picture lock. Captions.
2. Cut Ep 1–2 and 8–10 Shorts.
3. Record Ep 0 VO over the atlas (screenwriter pages).
4. Disclose synthetic media. Then Pass B–F.

### 6.4 What not to do

- One prompt: “every expression every angle every style.”
- Motion prompt that restates wardrobe, pores, and “cinematic 8k.”
- Mixing two identities to “cover diversity” inside one clip.
- Using a real actor’s face without a release.
- Claiming Chat hops are live agent-correct (ISSUE-0002).
- Starting ISSUE-0014 RSI on this Program.

---

## 7. Agents (who does what — no pack rewrite until implement)

| Agent | Role on Face Atlas |
|---|---|
| `specials.intent-analysis-agent` | Program + child first **agent hop** |
| `specials.general-creative-agent` | OPTIONS for series format (long + Shorts), not AU list |
| `video.showrunner` | Program first-called; owns atlas bible/arc |
| `specials.psychological-profile-agent` | Personality **modifiers** only; OOS if clinical |
| `video.screenwriter` | Ep 0 VO + slates after logline lock |
| `video.emotionalarc` | Episode arc, not FACS |
| `video.director` | AU / micro beats |
| `video.planner` | Generation list rows |
| `video.avatardesign` | Synthetic identity mesh/look-dev |
| `video.continuity` | Subject / Hair / Skin lock |
| `video.mua_makeup` | Face finish; refuse beauty-filter |
| `video.cinematographer` | Look bible |
| `video.cameraoperator` | Angle grid; locked-off on expression cells |
| `video.storyboard` | One panel per cell |
| `video.promptengineer` | Child first-called; compile still vs motion |
| `video.critic` / `video.judge` | Identity drift, unlabeled takes |
| `video.editor` | Atlas concat, slates, picture lock |
| `video.ethics` / `video.compliance` | Likeness + YouTube disclosure |
| `video.gatekeeper` | Phase exits (declared) |

Do not make PE or screenwriter first-called. Do not mkdir Projects from an agent.

---

## 8. Work if/when implementing (host + UI + packs)

Not this pass. When started:

| P | Work |
|---|---|
| **P0** | Create Program `face-atlas` / Face Atlas. Stamp Program hops with atlas house rules. |
| **P1** | Identity bible still slots + hashes under `program/face-atlas/bible/`. Rest face required. |
| **P2** | Generation-list schema columns: `au`, `micro`, `angle`, `look`, `personality`, `situation`. Lock fails if any scene has 0 segments. |
| **P3** | Pass A list (~15 cells) + spawn. Child inherit bible. |
| **P4** | Compile SOP: still from rest/angle/style; motion = AU only; camera locked on expression cells. |
| **P5** | Slate/label fields on sequence rows for editor. |
| **P6** | Pass B–F lists as later Program passes (not a silent patch of locked pages). |
| **P7** | Pack prompt blocks: director AU beats; mua no beauty-filter; continuity identity drift = reject; cameraoperator locked-off rule. |
| **P8** | Delivery: 16:9 + 9:16 specs, captions, disclosure copy. No live upload. |

**Out of scope:** ISSUE-0014 dream/replay; weight training; live fail-closed engines; viseme episode; real-person clone; claiming completeness of FACS×life.

---

## 9. Exit (when eventually implemented)

- Operator can explain on camera: one variable per clip; still vs motion; why “all in one prompt” fails.
- Pass A exists as spawned Projects with labeled takes or honest Dry-run previews.
- Rest identity still is the parent of expression I2V.
- Hair / Subject / Skin stay unique. `fused_request` null.
- YouTube Ep 0 + at least one atlas montage **or** a CHARACTERIZATION storyboard of that cut.
- Synthetic disclosure written. No `sample/` write. Not an eval PASS.

**This file is the next issue. It is the plan. Do not start production in this pass unless the operator says to implement ISSUE-0015.**
