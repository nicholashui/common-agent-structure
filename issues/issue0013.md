# ISSUE-0013 — Complete Program filmmaking workflow

**Status:** Implemented (CHARACTERIZATION). Host Program record, spawn gates, sequence `fused_request` null, Program UI W0–W6, hop table, and pack prompt/docs aligned. Not an eval PASS.  
**Severity:** High (Program today is code+name only; agent packs own crafts but settings do not run this pipeline)  
**Component:** Program (`casops.program.v1`, `/programs`), Project Chat Auto Pilot, clip canonical + sequence (ISSUE-0009), video.* packs  
**Observed:** 2026-09-16  
**Revised:** 2026-09-16 (complete filmmaking workflow from studio practice + AI multi-clip pipelines + pack inventory)  
**Operator statement:** A Program is a group of Projects. Each Project has video/audio output. The Program combines those like a non-linear editor into a full movie. The Program creates **all** related Projects, but **first** it must hold a complete generation list of each scene. Each scene has many segments. **One segment = one Project.** Workflow from story through generate through cut. Confirm whether screenplay is the first step (research: it is not).  
**Related:** ISSUE-0007 (clip Auto Pilot / five human locks), ISSUE-0008 (Project Chat spine), ISSUE-0009 (canonical clip; one pass = one clip; sequence concat is post; spec §10–11 long-form), ISSUE-0010–0012 (operation-guide dialects + SOP), Program nav (code + name only).  
**Honesty:** CHARACTERIZATION. Not an eval PASS. Not a production license. `sample/` stays read-only. Dry-run stays default. Only `grok-imagine` / `grok-image` are live; other generator tags stay fail-closed. Skills and citations are declared, not live grants. `sequence_compile.fused_request` stays null. Gold-body probes are never sent to agents or vendors.

This issue is the **complete filmmaking workflow**. Host + UI + Program hops + pack prompt/docs now state the same rules (CHARACTERIZATION). It does not activate fail-closed engines. It does not change v3 agent schema. It does not add `POST /swarms/{id}/runtime/run`. Child Auto Pilot hop counts are unchanged.

---

## 0. Goal

A Program is the **film**. A Project is **one generated segment** (one clip). The host, not an agent, orchestrates.

```text
Human CONTROL (Program brief)
  → W0 development     intent → logline → bible stub          LOCK logline
  → W1 literary        treatment → screenplay                 LOCK pages
  → W2 pre-production  breakdown → generation list
                       visual bible → storyboard/animatic     LOCK list + bible
  → W3 spawn           host: one Project per segment
  → W4 production      each Project: clip Auto Pilot + takes  accept takes
  → W5 post / NLE      assembly → picture lock → finish       LOCK picture
  → W6 delivery        masters, captions, archive             no live upload
```

**House rules**

1. Screenplay is **not** the first step. Logline and literary treatment come first. Breakdown comes after pages lock.
2. Do not spawn Projects until the **generation list** and **visual bible** are locked.
3. One segment = one Project = one `kind: clip` = one collab pass.
4. A scene may contain many segments. A Program contains many scenes.
5. Stills / character sheets / storyboard **before** motion. I2V: still carries look; motion describes change only (ISSUE-0010).
6. Concat is **post** (NLE). Never one overloaded generation for the whole film. `fused_request` is always null.
7. Picture lock **before** color, mix, and final graphics. Breaking picture lock after finishing wastes that work.
8. Unique T4 source blocks stay unique (Hair ≠ Subject, etc.).
9. Host join; PE does not write the novel; Program closer is `video.showrunner` until the cut pass, then `video.editor` owns picture; `video.soundmixer` owns the mix; `video.gatekeeper` signs phase exits.
10. Adjacent clips may chain last-frame → next start **only** after identity/geometry/prop/motion/exposure inspection. Refresh from approved references at scene boundaries (spec §11.3).

---

## 1. Research (why this shape)

### 1.1 Studio filmmaking is five stages, not “write script then generate”

Vancouver Film School / Storyflow / LTX (2026): development, pre-production, production, post-production, delivery. Three-stage “pre/prod/post” hides development (idea → script) and delivery.

| Stage | Question | Locked output |
|---|---|---|
| Development | What film, and should it be made? | Logline, treatment, screenplay, greenlight |
| Pre-production | Exactly how, with whom, in what units? | Breakdown, shot/segment list, bible, boards, schedule |
| Production | Did we capture each unit? | Takes + continuity ledger |
| Post-production | Does it cut, sound, and grade? | Picture lock, then finish |
| Delivery | Does the master match spec? | Package, QC, archive |

Development ends when pages are shootable. Pre-production **starts** at script lock. First pre-prod gate: lock the script, then break it down. You cannot spawn generation units from a moving script (Storyflow, LTX, StudioBinder).

Literary order (screenwriter userguide, McKee/Field/Truby, JP 映画製作 企画開発): **idea → logline → synopsis → treatment → screenplay**. Screenwriter pack owns **Treatment → screenplay**, not the Program start.

WIPO independent-filmmaker checklist: conceptualization and legal/IP **before** production design. Releases and likeness clearance are pre-prod, not delivery afterthoughts (Moonb 2026: unsigned talent/location releases are the most expensive skip).

### 1.2 Breakdown is not the screenplay and not the shot novel

A **script breakdown** (1st AD / producer; Wikipedia; Wrapbook; Jungle; MasterClass) tags production **elements** per scene: cast, extras, props, wardrobe, makeup, vehicles, SFX, special equipment. It feeds budget and schedule.

A **shot list / generation list** (director + DP lining the script; ASC Shot Craft) is coverage: which camera views exist. In this repo a generation **segment** is one clip (spec §1.2), not necessarily one traditional coverage angle — one clip has one dramatic purpose.

Story order ≠ shoot/generate order. NLE uses story order. Generate order may group by location, character, or identity lock. Both live on the list.

### 1.3 AI multi-clip pipelines add locks traditional crews get “for free”

Traditional crews share a physical set. Generators are stateless. Every serious AI film pipeline (InVideo 2026, Cinemagiq, Higgsfield, Ciaro, billpar `ai-cinematic-pipeline`, 0xadvait `ai-video-pipeline`, wushaojun `ai-short-film`, FilmAction, Dreamina, spec v2 §10.6) does:

```text
full script in context
  → scene / shot list (text, cheap)
  → lock character + location + prop stills
  → storyboard / animatic
  → generate one short clip at a time (often still → I2V)
  → continuity QA
  → assemble in an editor
  → audio as separate stems
```

Do **not** paste the whole screenplay into one text-to-video box. One beat ≈ one prompt (billpar: 2–3 s beats). Board **beats**, not every editorial cut (InVideo). Character sheet before any panel (0xadvait: one reference sheet on every still). Frame chaining is optional and inspected (spec §11.3). Native-audio clips are **sources**, not the mix (spec §11.2).

This repo already encoded the generation unit: ISSUE-0009 / spec §17: one collab pass = one clip; longer piece = sequence; concat is post.

### 1.4 Post has an order that punishes skipping

Moonb 2026; PeekAtThis indie post guide 2026; spec §11:

1. Backup / log / select takes  
2. **Assembly** (script order) → **rough cut** → **fine cut** → **picture lock**  
3. Then finishing: VFX / titles, sound edit then mix, color correct then grade, captions  
4. QC then export to spec  

Never pour color and mix into a cut that will still move. Picture lock is the gate. Assembly / rough / fine / lock are four editorial states, not one “NLE” hop.

Delivery specs belong **up front** (aspect, fps, loudness, captions). Discovering YouTube vs DCP after the master is rework (Krock; PeekAtThis: DCP / ProRes / H.264 / M&E stems).

### 1.5 This repo already has the crafts; it does not run the film

Spec v2 §10.6 long-form pipeline (already in-tree):

```text
brief → script and scene objectives → bibles and asset approval
  → storyboard or animatic → clip specifications → capability validation
  → prompt compilation → candidate takes → review and selection
  → continuity updates → editorial assembly → sound and graphics
  → finishing → delivery QC
```

ISSUE-0013 is that pipeline mapped onto **Program + child Projects**, with named pack agents. It is **not** something the agents discovered as one DAG. Clip Auto Pilot is W4 only. `sample-instruction.md` is a writers-room packet (W0–W1 fragment). Program is code + name.

---

## 2. Vocabulary (name collision)

Spec v2 §1.2 uses “Project” for a complete production. This issue uses **operator** names from the Program nav.

| Operator word | Spec v2 | Meaning |
|---|---|---|
| **Program** | Project / sequence package | The film. Bible, list, NLE, delivery. |
| **Scene** | Scene | Dramatic unit. Many generations. |
| **Segment** | Clip (generation unit) | One generated output, video + optional native audio. One purpose. |
| **Project** (`project/<slug>/`) | Clip | One segment. Existing Auto Pilot + canonical.yaml. |
| Beat | Beat | Change inside a shot. |
| Shot | Shot | Continuous camera view; often one segment. |
| Take | Take | One candidate generation for the same clip spec. |
| Sequence / cut | Sequence | Edited arrangement of clips, graphics, sound. Concat is post. |
| Literary treatment | (pages input) | Prose story **before** screenplay. `video.screenwriter`. |
| Directorial treatment | look / camera grammar | Visual language **after** pages. Director + CD + DoP. |
| Visual bible | bibles + approved assets | Locked character / location / prop stills. |
| Generation list | clip specifications | Complete scene → segment table. Spawn CONTROL. |
| Picture lock | editorial lock | No further recuts before finishing. |

**Invariant:** `generation_unit: clip`. `concat: post`. `one_pass_one_clip: true`. `fused_request` is always null.

---

## 3. What exists today (gap)

| Surface | Today | This issue target |
|---|---|---|
| Program | `program/<code>/program.json` — code + name | Phase, locks, bible refs, generation list, project_ids, sequence, delivery spec |
| Program UI | New Program two fields; read-only view | Program Chat + Workflow + list + NLE strip + phase gates |
| Project Chat | Clip Auto Pilot. First agents: intent-analysis → creative-agent → PE | Unchanged **inside** each spawned Project (W4) |
| Sequence | Per-Project `sequence.yaml`; concat post | Program-level sequence of **child** takes |
| Screenplay / showrunner | Packs exist; sample-instruction only | W0–W1 Program hops |
| Storyboard / worldbuilding / sound / VFX / a11y | Packs exist; unused by Chat/Program | W2 boards; W5 finish; W6 a11y |
| Editor | Pack unused | W5 picture owner |
| Gatekeeper | Pack unused | Phase-exit signer (declared, not C2PA live) |
| Spawn | Human creates Projects one by one | Host creates all Projects from locked list |
| Live generate | Grok Imagine/Image only; Dry-run default | Unchanged |

### 3.1 Agent settings do **not** match this workflow

Role lines are compatible. Runtime settings are not.

| Setting | Today | This workflow needs |
|---|---|---|
| Program first-called | None | `video.showrunner` |
| First agent hop | Clip: intent-analysis → creative-agent → **PE** | Program: intent-analysis → creative-agent → **showrunner** |
| Intent `DECIDE_BY` | `specials.general-creative-agent` | Showrunner at Program; PE only inside a child |
| Screenwriter | Not on Project Chat; sample induce | W1 after logline lock |
| Storyboard / editor / sound / VFX | Packs idle | W2 boards; W5 cut/sound/VFX |
| Generation-list lock | Does not exist | Required before spawn |
| Visual-bible lock | Does not exist | Required before spawn / motion |
| `max_peer_hops` | `0` on folders | Host-mediated hops; agents still do not spawn peers |
| Critique edges | Room bus / `spagent.*` on specials | Program parties + Create Program |
| Human locks | Five **clip** roles | Those stay on children; Program adds logline / pages / list / bible / picture |
| Sequence | Per-Project | Program sequence of children |
| Memory writes | Forbidden | Stay forbidden. `video.memory` is declared retrieval, not a live write grant |

Implementing this issue is **host orchestration + Program record + hop tables**, not “turn on the agents.” Do not rewrite every craft line.

---

## 4. Keep vs change

### Keep

- Child Project Chat hop order and five human domain roles (ISSUE-0007): PE, director, cinematographer, mua, continuity. Cameraoperator and critic stay agent-to-agent on the clip pass.
- Host join of owned clip fields (ISSUE-0009). One pass = one clip.
- Operation-guide SOP (ISSUE-0010–0012). Parameters are not prompt words. One camera move per clip.
- `sample/` never written. Gold-body probes never sent.
- Dry-run default; mutation contract; no T3 / plugin execute / memory writes.
- Fail-closed generator tags until profiled.
- Agent Profile packed Chat (ISSUE-0002) stays packed Chat.
- Unique T4 blocks stay unique.
- Relative paths on UI.
- Force as default Workflow layout.

### Change (when implementation is approved)

- Program record grows: phase, locks, refs, project_ids, delivery spec.
- Program Chat / Workflow: showrunner spine, then breakdown, bible, spawn, NLE.
- Host gates: spawn only after list + bible locks; finishing only after picture lock.
- Program sequence compiles child canonicals; still no fused vendor request.
- Optional characterization hop tables for Program (live: false) — do not overwrite child clip hop counts.

### Do not change in this issue

- Live-activating Seedance / Kling / Veo / LTX / Hailuo / GPT Image / Sora.
- Feature-length **one-shot** generation.
- v4 `POST /swarms/{id}/runtime/run`.
- Claiming eval PASS.
- Writing `sample/`.
- Absorbing another agent’s exclusive craft.
- Hard-coding a live agent-fleet count in UI or tests.
- Live festival upload, C2PA signing as production, voice-clone of real people without clearance.

---

## 5. Complete workflow

Two ingest paths:

| Path | Start | Skip |
|---|---|---|
| **Greenfield** | W0 | Nothing |
| **Script-in-hand** | Intent-analysis on the ingest ask → W1 lock | W0 idea-finding; still verify treatment/logline and run W2 |

Human CONTROL at Program is locution (brief). Domain novels are option crafts. Stop (`needs_hitl`) on blocker critique, failed L1, or missing lock. Do not invent stills, logs, fetches, or measured scores.

`video.gatekeeper` verifies each phase exit (L1 schema). It does not become a second control plane. `video.orchestrator` may propose hop graphs. Host dispatches.

---

### W0 — Development (what film)

**Purpose.** Decide what the film is. No screenplay yet. No Projects.

| Step | Party | Owns | Does not own |
|---|---|---|---|
| 0.1 | Human → Create Program | Brief (locution), working title | Shot grammar, pages |
| 0.2 | `specials.intent-analysis-agent` | Locution / illocution / OPTIONS / triggerability | Deliverable |
| 0.3 | `video.ideation` (if open) | Concept OPTIONS, hooks | Lock of one idea |
| 0.4 | `specials.general-creative-agent` | Campaign / world OPTIONS. `DECIDE_BY: video.showrunner` | Generator novel, pages |
| 0.5 | **`video.showrunner`** (Program first-called) | Bible stub, room, film/season arc | Per-shot craft, NLE, vendor calls |
| 0.6 | `video.worldbuilding` | Lore, geography, rules (if the world is invented) | Look stills |
| 0.7 | `video.audiencesim` | Promise read | Pages |
| 0.8 | `video.producer` | Viability / phase gate (not shot intent) | Creative lock |
| 0.9 | `video.compliance` / `video.ethics` | Early IP / likeness / disclosure risk | Legal advice as a bar license |
| 0.10 | Human lock | **Logline**, format (runtime class, aspect intent, language, fps intent) | — |

Showrunner may induce (host-mediated): `video.orchestrator`, `video.critic` (bus, not closer), `video.novelty` (optional).

**Exit W0:** Locked logline + format bounds + bible stub. `first_called` remains `video.showrunner`.

**Skip W0 idea-finding** only when a finished literary script is attached **and** the operator confirms ingest. Still run intent-analysis.

---

### W1 — Literary (pages)

**Purpose.** Turn the locked logline into lockable pages. Still no Projects.

| Step | Party | Artifact |
|---|---|---|
| 1.1 | `video.screenwriter` | Literary **treatment** (prose, scene order; full dialogue not required) |
| 1.2 | `video.narrativearc` | Plot spine, turning points |
| 1.3 | `video.emotionalarc` | Want/need, charge per scene |
| 1.4 | `video.comedywriter` | Only if genre needs it |
| 1.5 | `video.screenwriter` | **Screenplay** (sluglines, action, dialogue) |
| 1.6 | `video.standardseditor` | Editorial standards / sourcing (esp. fact-based) |
| 1.7 | `video.director` | Directorial notes on pages (tone, coverage **intent** — not the segment list yet) |
| 1.8 | `video.critic` | Critique bus |
| 1.9 | `video.judge` | Named closer for unresolved room disputes |
| 1.10 | `video.legal` / `video.compliance` | Clearance notes on pages (names, brands, likeness) |
| 1.11 | Human + showrunner + producer | **LOCK pages** |

`video.copywriter` is ads/hooks/VO, **not** screenplay. `specials.screenwriter-strategic-goal-achievement-agent` is career/process, **not** the video-pack writer.

Further page edits after lock **reopen W2** (re-breakdown). Silent page patches after spawn are forbidden.

**Exit W1:** Versioned treatment + beat sheet + locked screenplay.

---

### W2 — Pre-production (complete generation list + visual bible)

**Purpose.** The operator’s “complete generation list of each scene,” plus the stills that make those segments generate-able. **First production documents. Not the first Program hop.**

W2 has **two locks**. Spawn (W3) requires both.

#### W2a — Breakdown → generation list

| Step | Party | Artifact |
|---|---|---|
| 2a.1 | `video.director` | Numbered **scene list** from locked pages; coverage intent |
| 2a.2 | `video.planner` | Segment DAG: scene → ordered segments; dependencies; critic gates |
| 2a.3 | `video.producer` | Schedule class, generate-order vs story-order, spawn gate |
| 2a.4 | `video.costoptimizer` | Optional engine-class routing ($/quality). Does not activate fail-closed tags |
| 2a.5 | Department tags (induced) | Element lists per scene: cast, wardrobe, props, locations, SFX, VFX, music — breakdown, not novels |
| 2a.6 | `video.vfxsupervisor` | Which segments need VFX / cannot be “in-camera” generate |
| 2a.7 | `video.critic` | Completeness: every scene has ≥1 segment; no orphan dialogue; one purpose per segment |
| 2a.8 | Human + director + producer | **LOCK generation list** |

Each **segment** row (spawn CONTROL):

| Field | Rule |
|---|---|
| `segment_id` | Stable, unique in the Program |
| `scene_id` | Parent scene |
| `story_order` | NLE default |
| `generate_order` | May group by location / character; optional |
| `purpose` | One dramatic or visual purpose |
| `duration_s` | Target **edited** duration; generate may be longer then trim (spec §1) |
| `clip_kind` | `kind: clip` |
| `elements` | Cast / location / props / wardrobe ids from breakdown |
| `inherit` | Bible keys: identity, look, lighting, constraints |
| `chain_from` | Optional previous `segment_id` for last-frame start |
| `still_required` | Default true for I2V engines |
| `audio_plan` | `native` / `silent_plate` / `hybrid` |
| `project_slug` | Empty until W3 |
| `status` | `planned` until spawn |

Do **not** write vendor prompt novels on the list. The list is CONTROL for spawn, not a Grok/Seedance string.

#### W2b — Visual bible (stills before any child motion)

| Step | Party | Artifact |
|---|---|---|
| 2b.1 | `video.creativedirector` | Look / world promise (directorial treatment) |
| 2b.2 | `video.moodboard` | Reference board |
| 2b.3 | `video.conceptartist` | Key art |
| 2b.4 | `video.casting` / `video.avatardesign` | Character presence / synthetic identity notes (no live hiring) |
| 2b.5 | Host + still engine | **Character sheets** (front/side/face). Lock winners. Grok Image live; other still tags fail-closed |
| 2b.6 | Same | **Location / set** stills; **hero props** |
| 2b.7 | `video.continuity` | Identity / wardrobe / geography bible + ledger columns (spec §10.2) |
| 2b.8 | `video.cinematographer` | Lighting / look bible (inherited by every child) |
| 2b.9 | `video.productiondesign` / `video.costumedesign` / `video.mua_makeup` | Bible rows, not per-clip novels |
| 2b.10 | `video.cameraoperator` | Default camera grammar (one move per clip later) |
| 2b.11 | `video.choreography` | Only if movement design is the craft |
| 2b.12 | `video.trustsafety` | Impersonation / likeness screen on sheets |
| 2b.13 | Human + CD + continuity | **LOCK visual bible** |

No child Project motion until this lock. Generating “to see the face” is W2b stills, not W4.

#### W2c — Storyboard / animatic (before spawn)

| Step | Party | Artifact |
|---|---|---|
| 2c.1 | `video.storyboard` | Script → shot panels. One panel per segment minimum. Board beats, not every future editorial cut |
| 2c.2 | `video.editor` (optional) | Animatic: panels timed to target `duration_s` + scratch VO |
| 2c.3 | `video.voiceover` | Optional scratch / temp VO for animatic only |
| 2c.4 | Human + director | Approve boards. Rejected panels do not spawn |

**Exit W2:** Locked generation list + locked visual bible + approved boards. Gate for W3.

---

### W3 — Spawn Projects

**Purpose.** Host creates **all** related Projects from the locked list. Agents do not mkdir.

| Step | Party | Rule |
|---|---|---|
| 3.1 | Host | One `project/<slug>/` per segment. Slug from program code + `segment_id` |
| 3.2 | Host | Inherit bible, boards, element ids, chain_from into Start / canonical seed. Do not copy `sample/` |
| 3.3 | Host | Wire `program.json` `project_ids[]` and each project `program_id` + `segment_id` |
| 3.4 | Host | Dry-run default. Mutation contract |
| 3.5 | `video.showrunner` | Spawn report only. No media |
| 3.6 | `video.gatekeeper` | Phase exit: list lock + bible lock + N folders (or dry-run slug preview) |

**Forbidden:** Spawn from treatment only. One Project for a whole scene that needs many segments. A Project that *is* the Program NLE. Spawn without visual bible.

**Exit W3:** N Projects as empty clip collabs (`planned`). List rows have slugs.

---

### W4 — Production (per Project — existing clip spine)

**Purpose.** Each segment becomes accepted take(s). Reuse ISSUE-0007/0009. Do not invent a second clip pipeline.

Per Project, in order:

```text
Inherited brief (locution) + bible + board panel
  → specials.intent-analysis-agent
  → specials.general-creative-agent
  → video.promptengineer          first-called video agent on the child
  → video.creativedirector
  → video.director                Human lock
  → video.cinematographer         Human lock
  → video.mua_makeup              Human lock
  → video.cameraoperator          no human hop
  → video.continuity              Human lock
  → video.critic                  no human hop
  → host join canonical.yaml
  → compile (ISSUE-0010 dialect)
  → still (if still_required) then I2V when engine is grok-imagine and Dry-run off
  → video.aiqaconsistency         drift / identity / hands
  → take select (human or director)
```

Program bible is **input**. Child agents write only owned clip paths. Continuity across Projects is the Program bible + ledger, not a fused generate.

**Dailies / data (Moonb 3-2-1 analog, fail-closed):** takes land in `project/<slug>/output/`. Do not delete the only copy. Missing backup tool is a diagnostic, not a pretend archive.

**Chaining:** if `chain_from` is set, start image is the **approved** end frame of that segment after inspection (spec §11.3). Failed inspection → refresh from bible stills, do not inherit errors.

**Pickups:** rejected takes stay on disk. New take = same Project, new take id. Do not spawn a second Project for a retry unless the generation list grows a new segment.

**VFX plates:** if W2 tagged VFX, generate the plate as the clip; `video.vfxsupervisor` notes live on the Program, not as a second vendor “whole film” call.

**Exit W4:** Each segment has an accepted take **or** explicit `needs_hitl` / fail-closed diagnostic. Missing takes do not invent black leader as success. Continuity ledger rows filled (spec §10.2).

---

### W5 — Post / NLE (Program)

**Purpose.** Combine Project outputs like an NLE. Editorial, not a vendor “make the film” call. **Internal order is mandatory.**

`video.editor` is first-called **for the cut pass only**.

#### W5a — Ingest and select

Backup, log, select accepted takes. `video.editor` + director. Assembly uses **story_order**, not generate_order.

#### W5b — Picture (four states)

| State | Meaning | Owner |
|---|---|---|
| Assembly | All accepted takes in script order, no performance of pacing yet | `video.editor` |
| Rough cut | First creative choices | editor + director |
| Fine cut | Scenes timed; temp sound ok; **no** final grade/mix | editor + `video.audiencesim` optional |
| **Picture lock** | No further recuts | Human + editor + director |

`video.continuity` checks eyeline, wardrobe, geography, screen direction across cuts. `video.critic` on the cut, not a closer.

Graphics/credits: if they are **segments** in W2, they are child Projects. If they are editorial overlays, `video.motiongraphics` after lock (temp boards allowed before lock).

Trim may use a longer generated take than edited duration (spec §1).

**LOCK picture** before W5c–W5e. Reopening picture lock invalidates grade/mix.

#### W5c — VFX / animation / titles (after picture lock for finals)

| Party | Owns |
|---|---|
| `video.vfxsupervisor` | VFX plan against locked cut |
| `video.animator_2d` | Character motion/weight if 2D/3D craft is in-role |
| `video.motiongraphics` | Titles, lower thirds, kinetic type |
| Host | Comp into sequence rows; still concat post |

#### W5d — Sound (after picture lock)

Native-audio on clips is a **stem candidate**, not the mix (spec §11.2).

| Party | Owns |
|---|---|
| `video.editor` + director | Spotting session |
| `video.voiceover` | Narration / character VO (declared; not a live TTS grant) |
| `video.lipsync` | Viseme gate on talking faces |
| `video.voiceclone` | **Only** with clearance. Default off. `video.compliance` + `video.ethics` + `video.trustsafety` |
| `video.sounddesign` | Ambience, foley, SFX |
| `video.composer` | Original score intent |
| `video.musicsupervisor` | Cue fit / rights awareness (not a license grant) |
| `video.soundmixer` | Final mix / loudness / channel layout (5.1/Atmos as **spec**, not a live renderer) |

#### W5e — Color (after picture lock)

`video.colorist`: correct for match first, then grade for mood (Moonb). DoP may comment; colorist owns the grade.

#### W5f — Cut diagnostics

`video.critic`, `video.aiqaconsistency` on the joined timeline, `video.gatekeeper` phase exit.

Host writes `program/<code>/sequence.yaml`: one row per child clip + editorial overlays; `concat: post`; `fused_request: null`.

Optional local concat under `program/<code>/output/`. Absence of ffmpeg is fail-closed, not a pretend mp4.

**Exit W5:** Picture-locked sequence + finish notes + mix/grade intents. Optional concat file.

---

### W6 — Delivery (package, not a new generate)

Delivery **spec** should have been on the Program record from W0 (aspect, fps, captions, loudness). W6 executes it.

| Step | Party | Artifact |
|---|---|---|
| 6.1 | `video.accessibilityoptimizer` | Captions, contrast, audio description, color-blind safe |
| 6.2 | `video.accessibility` | Final a11y acceptance |
| 6.3 | `video.signlanguageinterpreter` | Optional ASL/BSL insert (own segment if generated) |
| 6.4 | `video.localizationqa` | Optional translation / cultural fit; M&E stems if dialogue replaced |
| 6.5 | `video.mpa` | Rating packaging inputs (declared) |
| 6.6 | `video.archivemaster` | Archive-grade package **plan** (not a live vault write) |
| 6.7 | `video.distributor` | Downstream spec list (platforms/territories) — no live upload |
| 6.8 | `video.trailereditor` | Optional trailer: **new generation list** of trailer segments, or recut of locked picture. Trailer is not a silent extra Project |
| 6.9 | `video.festivalstrategist` | Optional calendar notes. No live submission |
| 6.10 | `video.corrections` | Post-release fix protocol only |
| 6.11 | Human | Delivery accept |

No production activation. No live festival/platform upload. No invented QC scores.

**Exit W6:** Delivery folder with specs, caption files if produced, honesty CHARACTERIZATION, `allowed_tools: []`.

---

## 6. Locks and gates

| Lock | Phase | Who | Blocks |
|---|---|---|---|
| `logline` | W0 | Human + showrunner | W1 pages |
| `pages` | W1 | Human + showrunner + producer | W2 breakdown |
| `generation_list` | W2a | Human + director + producer | W3 spawn |
| `visual_bible` | W2b | Human + CD + continuity | W3 spawn and W4 motion |
| `storyboard` | W2c | Human + director | W3 spawn (may be waived only if every segment already has a still purpose — default **required**) |
| take accept | W4 | Human or director | That row in assembly |
| `picture` | W5b | Human + editor + director | Color, mix, final graphics |
| `delivery` | W6 | Human | Claim of a finished movie |

`video.gatekeeper` checks the lock exists and L1 files validate. It does not mint envelopes or call vendors.

---

## 7. Agent map

### 7.1 Program-level

| Agent | Phase | First-called? |
|---|---|---|
| `specials.intent-analysis-agent` | W0 first **agent** hop | No |
| `specials.general-creative-agent` | W0 | No |
| `video.ideation` | W0 if open | No |
| **`video.showrunner`** | W0–W3 closer | **Yes (Program)** |
| `video.worldbuilding` | W0 | No |
| `video.screenwriter` | W1 | No |
| `video.narrativearc` / `emotionalarc` / `comedywriter` | W1 induced | No |
| `video.standardseditor` | W1 | No |
| `video.orchestrator` | Hop graph | No — not a second control plane |
| `video.planner` | W2a DAG | No |
| `video.producer` | Greenlight / spawn | No |
| `video.director` | W1 notes; **W2a list owner**; W5 picture | No |
| `video.creativedirector` | W2b look | No |
| `video.storyboard` | W2c | No |
| `video.moodboard` / `conceptartist` / `avatardesign` | W2b | No |
| `video.continuity` | W2b bible; W4; W5 cut | No |
| `video.cinematographer` / `cameraoperator` | W2b grammar; W4 child | No |
| `video.casting` / `costumedesign` / `productiondesign` / `mua_makeup` | W2 | No |
| `video.vfxsupervisor` | W2a tag; W5c | No |
| `video.compliance` / `legal` / `ethics` / `trustsafety` | W0/W1/W2b/W5d | No |
| `video.critic` / `video.judge` | Room + list + cut | Judge = disputes only |
| `video.gatekeeper` | Every phase exit | No |
| **`video.editor`** | W5 cut pass | **Yes for cut pass only** |
| `video.colorist` | W5e | No |
| `video.sounddesign` / `soundmixer` | W5d | Mixer owns mix |
| `video.composer` / `musicsupervisor` | W5d | No |
| `video.voiceover` / `lipsync` | W5d | No |
| `video.motiongraphics` | W5c | No |
| `video.aiqaconsistency` | W4 / W5 | No |
| `video.accessibility` / `accessibilityoptimizer` | W6 | No |
| `video.archivemaster` / `distributor` | W6 | No |

### 7.2 Project-level (W4) — do not reorder

ISSUE-0008 spine. First **video** agent: `video.promptengineer`. First **agent** hop: `specials.intent-analysis-agent`.

`video.promptoptimizer` may comment on PE’s owned paths; it does not become first-called and does not overwrite another craft.

### 7.3 Not Program first-called

`video.screenwriter`, `video.promptengineer`, `video.planner`, `video.storyboard`. `video.editor` is first-called only on the cut pass.

### 7.4 Default-off (do not induce unless the brief names the genre)

Ads/growth/UGC/SEO/CRM/sales/ROAS/retention/channel/social, sports, real-estate, food, medical illustration, instructional/LMS, journalism unless documentary, children’s author, music-video director unless MV, travel cine, podcast specials, voice-clone of real people, deepfake detection except as trust-safety support, evaluation harness as live PASS.

`video.memory` remains declared retrieval. **No memory writes.**

---

## 8. Disk and schema (target)

No second control plane. Public API stays `/api/v3`. Companion Program paths stay companion.

```text
program/<code>/
  program.json
  bible/
    world.md
    cast.md
    locations.md
    look.md
    sound.md
    world_rules.md
  literary/
    treatment.md
    screenplay.fountain          (or .md)
  generation-list.yaml           LOCK
  storyboard/                    panels per segment
  assets/approved/               character / location / prop stills
  continuity/ledger.csv          spec §10.2
  sequence.yaml                  kind: sequence; rows → child clips
  edit/                          editor notes, picture-lock flag
  delivery/specifications.yaml
  output/                        optional concat / masters (fail-closed if no tool)
project/<segment-slug>/
  output/<slug>-canonical.yaml
  output/<slug>-prompt.txt
  output/compiled/<engine>/
  output/takes/
  output/<slug>.jpg / .mp4
```

`program.json` additions (implement in P1):

```json
{
  "schema_version": "casops.program.v1",
  "id": "sprism",
  "code": "sprism",
  "name": "S-PRISM",
  "honesty": "CHARACTERIZATION",
  "first_called": "video.showrunner",
  "phase": "w0|w1|w2|w3|w4|w5|w6",
  "locks": {
    "logline": false,
    "pages": false,
    "generation_list": false,
    "visual_bible": false,
    "storyboard": false,
    "picture": false,
    "delivery": false
  },
  "project_ids": [],
  "generation_list_ref": "program/sprism/generation-list.yaml",
  "sequence_ref": "program/sprism/sequence.yaml",
  "delivery": {
    "runtime_target_s": null,
    "aspect_ratio": null,
    "frame_rate_fps": 24
  },
  "production_activation": false,
  "allowed_tools": []
}
```

Spawn forbidden unless `generation_list` **and** `visual_bible` are true. Live generate inside a child remains Dry-run gated. Relative paths only on UI.

Align folder names with spec §10.1 where cheap (`bibles/`, `assets/approved/`, `continuity/ledger.csv`, `edit/`, `delivery/`).

---

## 9. UI (when implemented)

| Surface | Behavior |
|---|---|
| Left nav Program | Keep New Program (code + name). Existing programs expand to phases / child Projects |
| `/programs/:id` | Phase strip W0–W6, lock chips, generation list, bible thumbs, child links |
| `/programs/:id/chat` | Program hops (showrunner spine). Not Agent Profile packed Chat. Hop headers Human → agent |
| `/programs/:id/workflow` | Same parties as Chat. Default layout Force. Node click → Program Chat `?comm=` |
| Child `/projects/:id/chat` | Unchanged clip Auto Pilot. Banner: Program `<code>`, segment `<id>` |
| NLE strip | Story-order segments; take status; picture-lock chip. Selecting a row does not auto-POST Imagine |

Honesty banner: Program hops CHARACTERIZATION until a later issue marks a live hop. Child generate stays `live` only when Dry-run is off and the engine is actually live.

---

## 10. Phases (implementation, after approval)

### P0 — This document

Complete workflow, research, vocabulary, locks, agent map, settings mismatch.

**Exit:** Operator can read the film pipeline without opening Python.

### P1 — Program schema + generation list (no generate)

- Extend `casops.program.v1` with phase, locks, project_ids, delivery, refs.
- `generation-list.yaml` schema (scene / segment rows including `elements`, `chain_from`, `still_required`).
- Tests: spawn rejected without `generation_list` **and** `visual_bible`.
- UI: read-only list on Program view if files exist; New Program fields stay code + name.

**Exit:** Unit/contract tests. No live vendor. No auto-mkdir of N Projects.

### P2 — Program Chat W0–W1 (characterization hops)

- Host-stamped hops: intent-analysis → creative-agent → showrunner → screenwriter (+ induced literary).
- Walkthrough optional on a characterization program (do not copy `sample/` bodies).
- Child clip Auto Pilot hop counts unchanged.

**Exit:** Program Chat shows development hops. `live: false`. Pages lock is a human chip.

### P3 — W2a generation list UI + lock — shipped CHARACTERIZATION

- Director/planner overlays write list rows, not clip novels.
- Scene with zero segments cannot lock.

**Exit:** Locked list on disk. Spawn still gated on bible lock.

### P4 — W2b/W2c visual bible + storyboard — shipped CHARACTERIZATION (placeholders; fail-closed tags blocked)

- Still-sheet slots; Grok Image Dry-run gated; fail-closed still tags do not pretend success.
- `video.storyboard` hop; panel per segment.
- `visual_bible` + `storyboard` lock chips.

**Exit:** Bible stills + panels on disk (or dry-run placeholders). Unique T4 rules do not apply until child Chat.

### P5 — W3 spawn — shipped CHARACTERIZATION

- POST spawn (mutation contract, Dry-run default) creates one Project per segment.
- Child Start inherits bible/board; no gold probes.
- Program nav lists children.

**Exit:** Browser: dual lock → spawn (Dry-run on) → slug preview or folders. Dry-run off required to write.

### P6 — W4 reuse clip pipeline — shipped CHARACTERIZATION (inherit + chain inspect; live Grok take still Dry-run gated)

- Opening a child runs existing Auto Pilot.
- Bible injected as inherited constraints/identity; owned-path rules hold.
- Still then I2V; chaining inspected; `video.aiqaconsistency` diagnostic hop allowed without changing ISSUE-0007 five human locks.
- Generate still Dry-run gated.

**Exit:** One child take possible on Grok with Dry-run off. Other children may stay planned.

### P7 — W5 Program sequence / NLE with post order — shipped CHARACTERIZATION

- `program/<code>/sequence.yaml` rows → child takes.
- Editor hops for assembly / rough / fine / picture lock (characterization).
- Finishing hops (color, sound, VFX, titles) **refused** until `locks.picture`.
- `fused_request` null. Optional concat fail-closed if tool missing.

**Exit:** Unit tests: two child clips → two sequence rows, no fused request; finish-before-lock rejected. UI NLE strip + picture-lock chip.

### P8 — W6 delivery folder — shipped CHARACTERIZATION

- `delivery/specifications.yaml`; a11y/caption slots; archive plan.
- No live upload. Trailer = explicit new list or recut, not a silent spawn.

**Exit:** Delivery tree exists; honesty CHARACTERIZATION; no eval PASS.

Suggested first PR after approval: **P1 only**.

---

## 11. Acceptance (when implementation starts)

- [x] Greenfield Program does **not** call `video.screenwriter` as first-called.
- [x] First Program agent hop is `specials.intent-analysis-agent`; Program first-called is `video.showrunner`.
- [x] Screenplay lock is W1 exit, not W0.
- [x] Generation list can represent Scene 1 → many segments.
- [x] Host refuses spawn if `generation_list` or `visual_bible` is false.
- [x] One segment creates one Project folder; scene ≠ Project.
- [x] Storyboard/bible **locks** and W2 hops exist before spawn (still files remain Dry-run / fail-closed; not a live sheet generate).
- [x] Child Project Chat hop order and five human roles unchanged vs ISSUE-0007.
- [x] Unique T4 blocks stay unique on children (clip pipeline unchanged).
- [x] Still then I2V on Grok children; fail-closed engines stay fail-closed (unchanged).
- [x] Finish hops refused before picture lock.
- [x] Program sequence `fused_request` is null.
- [x] Dry-run default unchanged.
- [x] `sample/` never written; gold-body probes never sent.
- [x] UI paths relative only.
- [x] No eval PASS claim.
- [x] Program view shows phase + locks + list; spawn gated (UI unit tests). Live browser pass not required for this CHARACTERIZATION ship.

---

## 12. Honesty / non-goals

- Pack skills remain declared, not host-granted.
- `allowed_tools: []` on Program record. Network off. Production activation false.
- Do not mint envelopes in agents. Induce is host-mediated (`max_peer_hops` on folders may stay 0; hops are host-stamped).
- Do not claim identical faces across all child generates.
- Do not treat Chat HTTP 200 as agent-correct (ISSUE-0002 still applies to Agent Profile).
- Do not live-activate voice-clone, C2PA, festival submit, or fail-closed engines in this issue.
- This plan is CHARACTERIZATION until P-exits are evidenced in tests + UI.

---

## 13. Sources (research trail)

**Studio / independent film**

- Storyflow, *What is pre-production?* (2026): development vs pre-prod; lock script then breakdown.
- Storyflow, *Pre-production vs production vs post* (2026).
- LTX Blog, *Essential steps for film planning* (2026): lock script; breakdown feeds budget/schedule.
- Vancouver Film School, *Five stages of film production* (2026).
- WIPO, *Development and pitching of audiovisual projects* — planning checklist (2026): concept + legal before production design.
- StudioBinder / Wrapbook / Jungle / MasterClass / Wikipedia *Script breakdown*: 1st AD tags elements; producer preliminary vs AD master.
- ASC Shot Craft, *Analyzing a script*: lining coverage.
- Moonb, *Complete video production checklist* (2026): storyboard + shot list before shoot; 3-2-1 backup; picture lock before color/sound; releases in pre-prod.
- PeekAtThis, *Film post-production* (2026): assembly → rough → fine → picture lock; never break lock; M&E / DCP / ProRes.
- LMU production timeline worksheet: lock script, breakdown, boards, animatic, then shoot, then rough/fine/lock, then sound/color.

**AI multi-clip (do not paste the whole script into one generate)**

- Spec `video_generation_prompt_specification.v2.md` §1.2 units, §10 long-form + continuity ledger, §10.6 pipeline, §11 assembly/chaining, §17 CASOPS house rules.
- InVideo, treatment/script load → lock sheets → shot list → clip generate → edit (2026).
- Cinemagiq, Ciaro, Higgsfield, FilmAction, Dreamina, M Studio: script → breakdown → boards → stills → video → assemble.
- billpar/ai-cinematic-pipeline: breakdown → character/setting/prop/voice assets → 2–3 s beats → one prompt per beat → chain → audio stems → edit.
- 0xadvait/ai-video-pipeline: character bible + storyboard stills **before** motion; ffmpeg concat.
- wushaojun/ai-short-film: screenplay → assets (review gated) → storyboard → image → video → merge.
- ISSUE-0009/0010: one pass = one clip; still owns look; motion owns change; concat post.

**This repo packs (crafts used above)** — `agents/<id>/prompts/primary.md` responsibility lines for showrunner, screenwriter, storyboard, worldbuilding, editor, colorist, sounddesign, soundmixer, vfxsupervisor, motiongraphics, voiceover, lipsync, gatekeeper, aiqaconsistency, accessibility*, archivemaster, compliance, legal, ethics, trustsafety. Clip spine ISSUE-0007/0008. Program `src/casops/programs.py` (code + name only).

---

## 14. Operator cheat sheet

**Greenfield film:** New Program → brief → intent-analysis → showrunner → **lock logline** → screenwriter (treatment then pages) → **lock pages** → director/planner **generation list** → **lock list** → character/location stills + storyboard → **lock bible** → spawn one Project per segment → generate each child (still then motion) → editor assembly → **picture lock** → sound/color/titles → captions/archive.

**Script in hand:** New Program → attach pages → **lock pages** → generation list → bible + boards → lock → spawn → generate → cut → finish → deliver.

**Do not:** Call screenwriter first on a blank Program. Do not create Projects from a logline. Do not generate the whole movie in one prompt. Do not spawn before list **and** bible locks. Do not grade/mix before picture lock. Do not use `video.copywriter` as the script owner. Do not use `specials.screenwriter-strategic-goal-achievement-agent` as the video-pack writer. Do not treat current agent settings as already running this DAG.
