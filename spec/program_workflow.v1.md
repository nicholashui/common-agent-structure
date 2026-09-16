# Program Workflow Specification v1

**Document ID:** `program_workflow.v1`  
**Version:** 1.0.0  
**Status:** Specification. Operator UX + business features for ISSUE-0013 steps 1–18 (Start → Create Project(s)). CHARACTERIZATION; not an eval PASS.  
**Date:** 2026-09-16  
**Related:** `issues/issue0013.md`, `docs/program_filmmaking.md`, `ui/public/docs/programs/userguide.md`, `spec/video_generation_prompt_specification.v2.md`, ISSUE-0007/0009 (child clip Auto Pilot)  
**Scope:** Greenfield Program from New Program through host **Spawn** (one child Project per segment). Does **not** specify W4 child generate, W5 NLE finish, or W6 delivery beyond the spawn gate.

> **Core principle:** Four Program surfaces cover eighteen tasks. Locks are the product. Agents do not mkdir Projects. Screenplay is not step 1.

---

## 0. What this spec is for

Operators asked: for filmmaking steps **1–18**, how many UIs, and what should they look like.

This document:

1. Records **research** on similar products (AI film suites + traditional pre-prod).
2. States **complete requirements** for Start → Create Project(s).
3. Lists **business features** that are **variable** (on by default vs optional vs later).
4. Defines the **UI inventory** and **mock list** for review.

Honesty: CHARACTERIZATION. Dry-run default. `sample/` never written. Fail-closed engines do not pretend success. Skills declared, not live grants.

---

## 1. Research: similar products and what UX to take

Two families. CASS is a **host-orchestrated agent swarm**, not a single “type prompt → movie” box. UX must combine both families.

### 1.1 AI film / multi-clip suites

| Product | How they get from idea to clips | UX takeaway for CASS 1–18 |
|---|---|---|
| **LTX Studio** | Workspaces in order: Gen Space (look) → Storyboard → generate → timeline. Storyboard is the highest-leverage cheap stage. Parse script **before** rendering panels. | Phase strip + **do not generate motion until boards exist**. Edit structure (merge/split) before images. |
| **InVideo agent** | Load **full script** first; lock character + world (4 options per asset); shot list; generate **act-by-act / shot-by-shot**; never paste the whole film into one prompt. Crew of typed agents (producer holds bible, storyboard agent, DoP per scene). | Program Chat = crew hops. Overview = bible + list. **Approve before spend**. Always-ask on locks. |
| **Runway** (multi-shot) | Plan the sequence first (establish → develop → payoff). One prompt per shot. Last-frame → next start. | One segment = one Project. Chain inspect, do not inherit a failed end frame (ISSUE-0013 P6). |
| **FilmAction-style** | Script → Cast → Sets → Storyboard → Shooting (takes) → Audio → Cut. | Same spine as W0–W5. Spawn sits between Storyboard and Shooting. |
| **Open-source “script → film” editors** (e.g. AI video production editor) | Format hub → Analyze script (cast/locations/props) → Director pass (shot list) → Concept/cast stills → Storyboard → Filming. | **Analyze** is our breakdown (step 13). **Concept** is visual bible (15–16). **Filming** is child Auto Pilot **after** 18. |

Common failure they all avoid: **one generate for the whole movie**. Common success: **lock identity stills, then one clip at a time**.

### 1.2 Traditional pre-production (non-AI)

| Product | Strength | UX takeaway |
|---|---|---|
| **StudioBinder** | Script breakdown (element tags), shot list in **story order** then **shoot order**, boards and schedules share one database. | Generation list is a **table**, not a chat dump. Scene cards with segments as rows. Story order ≠ generate order. |
| **Boords** | Script beside frames; board → shot list in one step; version + comments. | Storyboard grid with script line under each panel. Convert board → spawn list, do not retype. |
| **Celtx / Movie Magic** | Script-to-set paperwork; eighths; stripboard. | Lock pages before breakdown. Changing pages after spawn is a **new pass**, not a silent patch. |
| **Frame.io** | Timestamped review, conflict-visible notes. | Lock chips + hop headers Human → agent. Critique is a **bus**, not a closer (`video.judge` for disputes). |
| **Storyflow / Milanote** | Vision canvas; lookbook. | Moodboard is W2b, not the Program start. Do not start on a blank canvas of clips. |

### 1.3 UX patterns to copy

1. **Stage workspaces, not 18 pages** — LTX: one workspace per phase. CASS: **4 Program UIs**.
2. **Always-ask locks** — InVideo Always Ask; StudioBinder lock script then breakdown. CASS: lock chips are first-class; Spawn disabled until dual lock.
3. **Structure before pixels** — LTX/Boords edit scene/shot count **before** rendering. CASS: generation list lock fails if any scene has **zero segments**.
4. **Assets before motion** — InVideo 4 options per character; LTX Elements. CASS: visual bible + storyboard files/placeholders before Spawn.
5. **One unit of generation** — Runway one shot; spec v2 one clip. CASS: one segment = one Project.
6. **Crew, not a god agent** — InVideo typed sub-agents. CASS: first hop intent-analysis; first-called **showrunner**; screenwriter W1; PE only on the child.
7. **Host mkdir** — no product lets a specialist agent create the production company. CASS: Spawn is a host button.

### 1.4 UX patterns **not** to copy

| Anti-pattern | Why it fails 1–18 |
|---|---|
| Single prompt box “make the film” | Violates one-pass-one-clip; fused_request must stay null. |
| Jump to New Project in left nav | Creates orphan clips with no Program bible. |
| Screenwriter as first screen | Research: logline/treatment first. |
| Auto-spawn on save Program | Missing list + bible. |
| Chat as the only surface for the shot list | StudioBinder: the list is a **table** operators scan. |
| Generating motion to “see the face” | That is W2b stills, not W4. |

---

## 2. Vocabulary (operator)

| Word | Meaning |
|---|---|
| **Program** | The film. `program/<code>/`. |
| **Scene** | Dramatic unit. Many segments. |
| **Segment** | One generation unit. One child Project. |
| **Project** | `project/<slug>/` clip collab (existing Auto Pilot). |
| **Lock** | Human + named closer. Blocks the next gate. |
| **Spawn** | Host creates **all** child Projects from the locked list. |
| **Literary treatment** | Prose before pages. |
| **Visual bible** | Locked character/location/prop stills + look. |

Invariant: `generation_unit: clip`. `concat: post`. `fused_request` null. One pass = one clip.

---

## 3. Complete requirements (steps 1–18)

### 3.1 Ingest paths

| Path | Start | Skip |
|---|---|---|
| **Greenfield** | Step 1 | Nothing |
| **Script-in-hand** | Step 1 → intent-analysis on ingest → jump to lock pages (12) after attach | Steps 4–10 idea-finding; still run 2–3 and 13–18 |

### 3.2 Task → UI → gate

| # | Task | UI | Must exist before next | Party |
|---|---|---|---|---|
| 1 | New Program (code + name) | **New program** | Folder `program/<code>/` (Dry-run writes nothing) | Human |
| 2 | Brief (locution) | **Chat** | Non-empty brief | Human |
| 3 | Intent analysis | **Chat** | OPTIONS returned; not triggerable until complete | `specials.intent-analysis-agent` |
| 4 | Creative OPTIONS | **Chat** | 3 OPTIONS; `DECIDE_BY: video.showrunner` | `specials.general-creative-agent` |
| 5 | Showrunner bible/arc | **Chat** | Bible stub | `video.showrunner` (**first-called**) |
| 6 | Optional ideation / world | **Chat** | Skip if logline already clear | `video.ideation` / `video.worldbuilding` |
| 7 | **LOCK logline** + format | **Overview** | `locks.logline` | Human + showrunner |
| 8 | Literary treatment | **Chat** | Treatment artifact | `video.screenwriter` |
| 9 | Narrative / emotional / comedy | **Chat** | Induced only if genre needs it | `video.narrativearc` / `emotionalarc` / `comedywriter` |
| 10 | Screenplay | **Chat** | Pages | `video.screenwriter` |
| 11 | Director notes on pages | **Chat** | Coverage **intent**, not segment rows | `video.director` |
| 12 | **LOCK pages** | **Overview** | `locks.pages` | Human + showrunner + producer |
| 13 | Breakdown: scenes → segments | **Overview** table + **Chat** | Every scene ≥1 segment; one purpose each | director + planner |
| 14 | **LOCK generation list** | **Overview** | Host **refuses** if any scene has 0 segments | Human + director + producer |
| 15 | Visual bible stills | **Overview** slots | Character/location/prop placeholders or stills | CD, continuity, still engine |
| 16 | **LOCK visual bible** | **Overview** | `locks.visual_bible` | Human + CD + continuity |
| 17 | Storyboard (1 panel / segment) | **Overview** grid | `locks.storyboard` (default required) | `video.storyboard` |
| 18 | **Spawn / Create Project(s)** | **Overview** | Dual lock: `generation_list` **and** `visual_bible`. One segment → one Project. Dry-run = slug preview only | Host; showrunner reports |

**Workflow** UI is the same parties as Chat (diagram). It does not add a fifth kind of work.

### 3.3 Hard gates (host)

1. New Program fields: **code** (`^[a-z][a-z0-9]{0,47}$`) and **name** only.
2. Dry-run default. Mutation contract on writes.
3. `generation_list` lock fails if no scenes or any scene has zero segments.
4. Spawn fails unless `generation_list` **and** `visual_bible` are true. JSON `detail` names missing locks.
5. Spawn fails if the list has no segments.
6. Agents do not mkdir. Spawn is host.
7. Child Start inherits bible/board refs. No `sample/` copy. No gold-body probes.
8. One Program-level generate of the whole film is forbidden (`fused_request` stays null).
9. Changing locked pages after spawn is a **new Program pass**, not a silent patch.
10. Fail-closed still tags must not return `success: true`.

### 3.4 Agent order (must match packs)

- Program first **agent hop:** `specials.intent-analysis-agent`
- Program **first-called:** `video.showrunner`
- **Not** first-called: `video.screenwriter` (W1), `video.promptengineer` (child only)
- Child after 18: existing Auto Pilot (intent-analysis → creative → PE + five human locks). Unchanged.

### 3.5 Non-requirements for this spec (later issues)

W4 live takes, W5 picture lock / color / mix, W6 delivery upload, live Seedance/Kling/Veo/LTX/Hailuo/GPT Image, v4 swarm run, eval PASS, memory writes, T3, plugins.

---

## 4. Business features (variable)

**Variable** = product can ship a default, an optional toggle, or a later slice without breaking the 1–18 spine.

### 4.1 Default-on (spine — not optional)

| ID | Feature | Notes |
|---|---|---|
| F-NEW | New Program code + name | Only two fields |
| F-CHAT | Program Chat hops | live: false until a later issue |
| F-FLOW | Program Workflow = same parties | Default layout Force |
| F-OVER | Overview: phases, locks, list, spawn | Relative paths |
| F-LOCK | Lock chips: logline, pages, generation_list, visual_bible, storyboard | Pages/list/bible/storyboard as in ISSUE-0013 |
| F-LIST | Scene → segment table | Add scene / add segment |
| F-GATE-LIST | Refuse list lock on empty scene | P3 |
| F-GATE-SPAWN | Refuse spawn without list + bible | Dual lock |
| F-SPAWN | One Project per segment | Inherit bible/board |
| F-DRY | Dry-run default | Preview slugs |
| F-HONEST | CHARACTERIZATION banner | Not eval PASS |

### 4.2 Default-on, **variable content** (operator-configurable)

| ID | Feature | Variable |
|---|---|---|
| V-FORMAT | Runtime class, aspect, fps, language | Values on logline lock |
| V-GENRE | Comedywriter / choreography / VFX tags | Induce only if genre needs it |
| V-INGEST | Greenfield vs script-in-hand | Skip 4–10 when pages attached |
| V-ORDER | `story_order` vs `generate_order` | Table columns; NLE uses story order |
| V-CHAIN | `chain_from` previous segment | Inspect; reject failed end frame |
| V-STILL | `still_required` per segment | Default true for I2V |
| V-AUDIO | `native` / `silent_plate` / `hybrid` | Per segment; mix is post |
| V-ENGINE | Child engine tag | Grok live; others fail-closed |

### 4.3 Optional (off unless the brief names them)

| ID | Feature | When |
|---|---|---|
| O-IDEA | `video.ideation` OPTIONS | Step 6 if logline not ready |
| O-WORLD | `video.worldbuilding` | Invented setting |
| O-ANIMATIC | Editor times boards + scratch VO | Step 17 extra |
| O-COST | `video.costoptimizer` engine class | Does not activate fail-closed tags |
| O-LEGAL | compliance / ethics / legal on pages | Fact-based / likeness |
| O-CAST | Casting / avatar notes | No live hiring |
| O-TRAILER | Trailer as **new** generation list | Not a silent extra Project |

### 4.4 Later / out of 1–18

| ID | Feature | Phase |
|---|---|---|
| L-TAKE | Child Auto Pilot generate | W4 after spawn |
| L-CUT | Assembly → rough → fine → picture lock | W5 |
| L-FINISH | Color / mix / VFX / titles | After picture lock |
| L-DELIVER | Captions, archive, no live upload | W6 (folder already exists) |
| L-CONCAT | ffmpeg concat | Fail-closed if tool missing |

---

## 5. UI inventory (how many UIs)

**Four Program UIs** cover 1–18. **Minimum three** if Workflow is collapsed into Chat.

| Surface | Route | Steps | Job |
|---|---|---|---|
| **U1 New program** | `/programs/new` | 1 | Create the film container |
| **U2 Program Chat** | `/programs/:id/chat` | 2–13 (talk) | Crew hops, OPTIONS, pages |
| **U3 Program Workflow** | `/programs/:id/workflow` | 2–13 (map) | Same parties, Force layout |
| **U4 Program Overview** | `/programs/:id` | 7, 12, 14–18 | Locks, table, bible, spawn |

After 18: existing **Project Start / Workflow / Chat** per child (W4). Not part of this spec’s mock set.

### 5.1 Layout rules (from research + CASS)

- **Header:** Common Agents Swarm System (CASS). Dry-run control. No agent switcher (that lives on Agent Profile only).
- **Nav:** Program above Project. New program first. After spawn, children listed under the Program.
- **Phase strip:** W0–W6 on Overview; 1–18 live in W0–W3.
- **Lock chips:** monospaced; on = emerald; Spawn hint names missing locks.
- **Chat hops:** header `Human → agent` / `agent → agent`; `live: false`.
- **Paths:** repo-relative only (`program/<code>/…`).
- **Spawn:** primary button disabled until dual lock; Dry-run shows `preview <slug>`.
- **Mobile:** same four surfaces; lock chips wrap; table stacks as cards.

### 5.2 What each UI must show (acceptance)

**U1 New program**

- Fields: Program Code, Program Name only.
- Hint: filmmaking starts after save; first hop intent-analysis; first-called showrunner.
- Save disabled until code valid + name non-empty.

**U2 Chat**

- Ordered hops. First hop **to** `specials.intent-analysis-agent`.
- First-called instruction **to** `video.showrunner`.
- Screenwriter hop labeled W1, not first.
- Honesty: CHARACTERIZATION.

**U3 Workflow**

- Numbered parties matching Chat.
- Node click → Chat (optional `?comm=`).
- Default layout Force.

**U4 Overview**

- Phase strip W0–W6.
- Lock chips including `generation_list`, `visual_bible`, `storyboard`.
- Generation list: scenes with nested segments; cannot lock list if a scene is empty.
- Bible + storyboard relative paths.
- Spawn + missing-lock hint.
- Child links after spawn.
- `fused_request: null` (read-only honesty; generate is later).

---

## 6. UI mock list (for review)

Mocks are **review artifacts**, not production UI. They describe the four surfaces plus two detail states (empty list vs lockable list, spawn gated vs ready).

| Mock ID | Artboard | Surface | What to check |
|---|---|---|---|
| M1 | New Program | U1 | Only two fields; Dry-run; no shot list |
| M2 | Program Chat W0 | U2 | First hop intent-analysis; showrunner first-called; Human → agent headers |
| M3 | Program Overview — empty list | U4 | `generation_list` lock disabled; Spawn disabled; missing locks named |
| M4 | Program Overview — lockable list + bible | U4 | Scene 1 with two segments; list lock enabled; bible/storyboard paths |
| M5 | Program Overview — spawn ready | U4 | Dual lock on; Spawn enabled; Dry-run preview copy |
| M6 | Program Workflow | U3 | Ordered parties; Force; not a clip DAG |

Review questions:

1. Is four surfaces too many, or is Chat+Overview enough (drop Workflow from 1–18)?
2. Should generation list be a **spreadsheet** (StudioBinder) or **scene cards** (LTX)?
3. Should Spawn sit on Overview only, or also a confirm modal listing N slugs?
4. Script-in-hand: extra control on New Program (“I already have pages”) or a Chat attach chip?

---

## 7. Mapping to current code

Already in tree (CHARACTERIZATION): New Program; Overview locks/list/spawn; Chat hops; Workflow party list; P3 empty-scene lock; P4 placeholder bible/boards; P5 inherit; dual-lock spawn.

This spec does **not** require new routes. It requires **UX completeness** of U1–U4 against §5.2 and mock review.

Gaps vs this spec (variable / polish, not new products):

- Script-in-hand toggle on New Program (V-INGEST).
- Story-order vs generate-order columns (V-ORDER).
- Confirm modal listing spawn slugs (review Q3).
- Workflow node → `?comm=` (nice-to-have).
- Scene-card vs table (review Q2).

---

## 8. Honesty

- Not an eval PASS.
- Pack skills declared, not granted.
- `allowed_tools: []`. No production activation.
- Do not live-activate fail-closed engines in this workflow.
- Child generate remains Dry-run gated (W4, after mock set).
