# Production Scale Framework (common-agent-swarm-ops)

**Document id:** `production_scale_framework.md`  
**Status:** Host-aligned operator guide (design + pack mapping)  
**Date:** 2026-07-30  
**Host:** common-agent-swarm-ops · video pack (114 agents)  
**Primary references:**

| Source | Role |
|--------|------|
| `va-agent-swarm/study/reference/how_to_build_a_video_agent_system/chapter_62.txt` | S1–S7 scale economics, ASAAF-style scaling ideas, phase-level workflows |
| `va-agent-swarm/study/ai_agent_video_production_workflow.md` | Common terms: roster, A–J archetypes, shared skeleton, L1/L2/L3, critique bus, S1–S7 profiles |
| `business/video/design/workflows/wf_video_arch_*.dna.json` | Host DNA workflow graphs for archetypes A–J |
| `business/video/agents/*` | Authoritative pack agent ids (`video.*`) |

**Runtime note (fail-closed):** Agent lists below are **crew capability maps**. Host `agent_spec.json` remains fail-closed (`network_access=false`, `production_activation_requested=false` unless a separate human gate enables production). Design-time tools (Sora/Veo/Seedance, etc.) are **not** auto-activated by this document.

---

## 1. Purpose

Chapter 62 describes seven production **scales** (S1–S7) with different budgets, teams, timelines, and AI agent depth. The VA workflow document maps those scales onto **agent crews**, **handoffs**, and **archetype workflows A–J**.

This framework answers, for **this host**:

1. What each scale means in common terms  
2. **When / who / how** to use it  
3. Which **pack agents** fulfill the work  
4. **Data flow** across the shared production skeleton  
5. Which **host DNA workflows** to start from  

It is the scale-aware operating companion to the agent roster and DNA graphs—not a second control plane.

---

## 2. Common Terms (shared vocabulary)

Use these names consistently with `ai_agent_video_production_workflow.md`:

| Term | Meaning on this host |
|------|----------------------|
| **Scale profile (S1–S7)** | Budget/time/risk envelope that selects crew size and gates |
| **Archetype (A–J)** | Content pattern (Viral Hook … Feature Film) |
| **Shared skeleton** | Greenlight → Pre-prod → Production → Post → Review → Distribution → Post-launch learning |
| **Lead agent** | Owns the phase artifact |
| **Critic / gate agent** | Scores or blocks handoff (critique bus + Judge/GateKeeper) |
| **L1 / L2 / L3** | Spec validation / craft rubric / preference or human baseline |
| **Handoff contract** | Typed artifact + `correlation_id` + evidence_refs + provenance |
| **OrchestratorAgent** | `video.orchestrator` — DAG schedule, retries, fan-out (host GraphEngine / pack spine) |
| **PlannerAgent** | `video.planner` — brief → phased plan + agent assignment |
| **ProducerAgent** | `video.producer` — scope, budget, greenlight coordination |
| **RouterAgent** | `video.router` — model/tool routing policy (host allow-list remains authoritative) |
| **MemoryAgent** | `video.memory` — project memory / retrieval |
| **JudgeAgent / GateKeeperAgent** | `video.judge` / `video.gatekeeper` — dispute & human-gate coordination |
| **Pack DNA** | `business/video/design/workflows/wf_video_arch_*.dna.json` |

**Chapter 62 acronym → host pack id (illustrative):**

| Chapter 62 style | Host pack agent(s) |
|------------------|--------------------|
| MO (Master Orchestrator) | `video.orchestrator` |
| EP (Executive Producer) | `video.producer` |
| DIR | `video.director` (+ `video.creativedirector` / `video.musicvideodirector` when relevant) |
| SCR | `video.screenwriter` |
| QA / consistency | `video.aiqaconsistency`, `video.critic`, `video.evaluationharness` |
| CIN | `video.cinematographer`, `video.cameraoperator` |
| ED | `video.editor`, `video.colorist` |
| AUD / MC / SD | `video.voiceover`, `video.composer`, `video.sounddesign`, `video.soundmixer` |
| VFX | `video.vfxsupervisor` |
| WB | `video.worldbuilding`, `video.productiondesign` |
| DHP / avatar | `video.avatardesign`, `video.voiceclone`, `video.lipsync` |
| SM / marketing | `video.socialmediastrategist`, `video.marketing`, `video.performancemarketer` |
| ERC / legal | `video.ethics`, `video.compliance`, `video.legal`, `video.trustsafety` |

---

## 3. Host System Context

```text
┌─────────────────────────────────────────────────────────────────┐
│ Tier 1 — Console (Next.js)                                      │
│  Brief / Composer · Registry · Canvas · Approvals · Agent Detail │
└───────────────────────────┬─────────────────────────────────────┘
                            │ REST commands + SSE projections
┌───────────────────────────▼─────────────────────────────────────┐
│ Tier 2 — Host control plane (/api/v1)                           │
│  Runs · Graphs · Approvals · Events · Video pack · Command bus  │
└───────────────────────────┬─────────────────────────────────────┘
                            │ task / graph / pack run
┌───────────────────────────▼─────────────────────────────────────┐
│ Tier 3 — Agent runtime (host-owned)                             │
│  GraphEngine · PackAgentRunner · tool broker · adapters         │
│  114 pack agents under business/video/agents/video.*            │
└─────────────────────────────────────────────────────────────────┘
```

**Scale selection rule of thumb (from chapter 62 + workflow §7.2):**

| Available time / risk | Scale | Agent depth (target band) | Quality bar |
|----------------------|-------|---------------------------|-------------|
| &lt; 4 hours, social spike | **S1** | ~15–25 active | L1 + light L2 |
| 4–24 hours | **S2** | ~25–40 | L1 + L2 ≥ 90 |
| 1–7 days, broadcast-ish | **S3** | ~40–55 | L2 + compliance |
| Weeks–months premium TV/MV | **S4** | ~55–75 | Full QC mesh |
| Multi-unit live/series | **S5** | ~75–95 | Multi-branch delivery |
| Long research/docu | **S6** | ~90–110 | Archive + rights heavy |
| Feature / cinematic | **S7** | **full 114 pool** (phased) | Formal release governance |

Numbers are **activation bands** (who is scheduled), not separate installs. The pack always has 114 definitions; scale decides **which subset the Planner/Orchestrator schedules**.

---

## 4. Shared Workflow Skeleton (all scales)

Every scale and every archetype A–J passes through the same **operational skeleton**. Scale only changes **depth, parallelism, and gate strictness**.

### 4.1 Phases and primary outputs

| Phase | Primary outputs | Mandatory gate owners (host ids) |
|-------|-----------------|----------------------------------|
| **0 Greenlight** | Brief, KPI, budget envelope, rights-risk, **scale profile S1–S7** | `video.producer`, `video.finance`, `video.compliance`, `video.planner` |
| **1 Pre-production** | Script lock, storyboard/lookbook, character/world bibles, consent, continuity baselines | `video.director`, `video.screenwriter`, `video.storyboard`, `video.continuity`, `video.legal` |
| **2 Production** | Shot intents, camera plans, takes/plates, render telemetry | `video.promptengineer`, `video.cinematographer`, `video.aiqaconsistency`, generators via host tools |
| **3 Post** | Timeline, grade, stems, captions, outlet variants | `video.editor`, `video.colorist`, `video.soundmixer`, `video.accessibility` |
| **4 Review & release pack** | AudienceSim, legal, provenance, sign-off, unresolved risks | `video.compliance`, `video.judge`, `video.gatekeeper` (+ HiTL) |
| **5 Distribution** | Mezzanine/masters, social cutdowns, metadata, archive | `video.distributor`, `video.channelmanager`, `video.archivemaster`, marketing agents |
| **6 Post-launch learning** | Telemetry, corrections, benchmark deltas, prompt/routing tickets | `video.analyst`, `video.evaluationharness`, `video.promptoptimizer` |

### 4.2 Canonical data flow (all scales)

```text
Human brief (UI)
    │  POST command (swarm/run) — not agent-direct
    ▼
PlannerAgent ──► ProductionPlan {phases[], agent_ids[], gates[], scale: Sx}
    │
    ▼
ProducerAgent + FinanceAgent + ComplianceAgent ──► GreenlightPacket
    │  gate: GateKeeper / HiTL if rights or budget fail
    ▼
OrchestratorAgent ──► DAG state machine (host GraphEngine / pack DNA)
    │
    ├── fan-out craft agents (scale-selected crew)
    │     each emits Artifact {type, payload, summary, evidence_refs}
    │     MemoryAgent stores episodic + long-term project facts
    │
    ├── CritiqueBus (structured CritiqueMessage)
    │     Critic/Judge/AIQAConsistency → refine ≤ max_refinement_count
    │
    ├── L1 Spec → L2 Rubric → L3 Preference / human baseline when required
    │
    └── RouterAgent (optional) ──► tool/model policy (host allow-list)
              │
              ▼
        Tool broker → adapters (media.stub | live media only if production-gated)
              │
              ▼
        Delivery package + SSE/event projection → Console
              │
              ▼
        Analyst / EvaluationHarness → learning tickets (closed loop)
```

### 4.3 Handoff payload (minimum contract)

Every inter-agent handoff SHOULD carry:

```json
{
  "correlation_id": "corr_…",
  "from_id": "video.screenwriter",
  "to_id": "video.director",
  "artifact_ref": "artifact:…",
  "artifact_type": "script_lock|shot_intent|timeline|…",
  "scale_profile": "S1|S2|…|S7",
  "workflow_archetype": "A|B|…|J",
  "evidence_refs": ["prompt:…", "rubric:…", "knowledge_usage:…"],
  "l1_passed": true,
  "l2_score": 0,
  "rights_state": "unknown|cleared|blocked",
  "needs_hitl": false
}
```

Pack offline runs also emit **`knowledge_usage`** (all bound sources: prompt, skill, rubric, SOURCE_CATALOG, RETHINK items, etc.) for test/UAT audit.

---

## 5. Scale Profiles (S1–S7)

For each scale: **background**, **when to use**, **who should use**, **how to use**, **agent crew**, **data flow**, **archetypes**, **host DNA**.

---

### S1 — Micro Production

| Attribute | Guidance (chapter 62 + host) |
|-----------|------------------------------|
| **Budget band** | ~$100–$50K (or AI tool cost-first) |
| **Team** | 1–15 humans + **~15–25 active agents** |
| **Duration** | 15s–~45m (typically short-form) |
| **Cycle** | Hours → few days |

#### Background

S1 is the foundation tier: **in-feed ads, promos, vlogs, unboxing, short tutorials**. Chapter 62 stresses extreme cost compression (AI vs agency) and **speed over cinematic depth**. Host posture: small crew, minimal branching, single primary outlet, light observability.

#### When to use

- Social spike / meme / viral hook  
- Single SKU promo under a day  
- Internal proof-of-concept with fail-closed tools  
- UAT of a single DNA graph (A/B/H)  

#### Who should use

| Role | Responsibility |
|------|----------------|
| Social / performance marketer | KPI, hook, CTA |
| Solo creator / SMB | End-to-end owner |
| Host operator | Start DNA run, watch canvas, approve light gates |

#### How to use (host)

1. Set **scale_profile = S1** on greenlight packet.  
2. Choose archetype **A** (Viral Hook), **B** (UGC ad), or **H** (Avatar) as default.  
3. Start DNA: `wf_video_arch_a_viral_hook_v1` / `b` / `h`.  
4. Keep **one** delivery branch (usually social).  
5. Quality: L1 hard; L2 threshold can be slightly relaxed only if brand risk is low.  
6. Skip theatrical/broadcast branches.  

#### Agents that fulfill S1 (core active set)

**Spine (always):**  
`video.orchestrator`, `video.planner`, `video.producer`, `video.router`, `video.memory`, `video.judge`, `video.gatekeeper`

**Creative minimal:**  
`video.trendintelligence`, `video.copywriter`, `video.screenwriter`, `video.director`, `video.promptengineer`, `video.aiqaconsistency`

**Make / finish:**  
`video.editor`, `video.accessibilityoptimizer` (or `video.accessibility`), `video.socialmediastrategist`, `video.compliance`

**Optional S1 add-ons:**  
`video.ugccreator`, `video.performancemarketer`, `video.motiongraphics`, `video.analyst`, `video.audiencesim`

**Typical active count:** ~15–25 (subset of 114).

#### Detail data flow (S1)

```text
Brief (UI)
  → Planner (S1 plan: 4–6 nodes)
  → Producer greenlight (budget + rights light)
  → TrendIntelligence + Copywriter → HookConcept
  → Screenwriter (optional short VO/script)
  → PromptEngineer → generation intents
  → AIQAConsistency gate
  → Editor assembles single timeline
  → AccessibilityOptimizer captions
  → SocialMediaStrategist packages 1–2 platform variants
  → Compliance light check
  → Analyst post-launch (views/CTR) → Memory
```

#### Mapped archetypes & DNA

| Archetype | DNA file |
|-----------|----------|
| A Viral Hook | `wf_video_arch_a_viral_hook_v1.dna.json` |
| B UGC Ad | `wf_video_arch_b_ugc_ad_v1.dna.json` |
| H AI Avatar | `wf_video_arch_h_ai_avatar_v1.dna.json` |
| D Birthday (light) | `wf_video_arch_d_personalized_birthday_v1.dna.json` |

---

### S2 — Small Production

| Attribute | Guidance |
|-----------|----------|
| **Budget** | ~$1K–$100K |
| **Team** | 2–30 humans + **~25–40 agents** |
| **Duration** | 30s–~120m (mini-programme, sketch, interview, short film) |
| **Cycle** | Days → few weeks |

#### Background

S2 adds **multi-scene coherence**, basic **cinematography/VFX**, and richer audio. Chapter 62 introduces CIN/VFX and multi-format outputs. Host adds continuity-lite, multi-format delivery, and stronger brand/compliance critics.

#### When to use

- Branded short film or multi-scene AI short (Archetype E light)  
- Animated explainer (C)  
- Podcast-to-video, interview package  
- Multiple social + one website/streaming mezzanine  

#### Who should use

| Role | Responsibility |
|------|----------------|
| Creative lead / director | Look, shot list |
| Brand manager | BrandAgent gates |
| Producer | Budget + schedule |

#### How to use

1. **scale_profile = S2**.  
2. Prefer archetypes **C, D, E (short), G (simple MV)**.  
3. Enable **≥2 distribution branches** (e.g. social + streaming/archive).  
4. Require **AIQAConsistency** on multi-shot identity.  
5. Optional Router multi-model **design** (not auto-live).  

#### Agents (S2 active band)

**All S1 core**, plus:

- Visual: `video.cinematographer`, `video.storyboard`, `video.conceptartist`, `video.vfxsupervisor` (light)  
- Audio: `video.composer`, `video.sounddesign`, `video.voiceover`  
- Brand: `video.brand`, `video.brandstrategist`  
- QC: `video.critic`, `video.colorist`  
- Learning: `video.promptoptimizer`  

#### Data flow (S2)

```text
Brief → Planner (multi-phase DAG)
  → Producer/Finance greenlight
  → Screenwriter multi-variant scripts (optional A/B)
  → Storyboard + ConceptArtist look pack
  → Director shot intents (shot-adjacency aware if RETHINK bound)
  → PromptEngineer + AIQAConsistency loop per shot
  → Editor rough cut → Colorist → Composer/SoundDesign
  → Brand + Compliance review
  → Multi-format package (social + mezzanine)
  → Analyst + AudienceSim post-launch
```

#### DNA

| Archetype | DNA |
|-----------|-----|
| C Explainer | `wf_video_arch_c_animated_explainer_v1.dna.json` |
| E Short film | `wf_video_arch_e_ai_short_film_v1.dna.json` |
| G Music video (light) | `wf_video_arch_g_music_video_v1.dna.json` |

---

### S3 — Medium Production

| Attribute | Guidance |
|-----------|----------|
| **Budget** | ~$20K–$1M |
| **Team** | 10–100 humans + **~40–55 agents** |
| **Content** | News, magazine, morning, cooking, mid-form series |
| **Cycle** | Days–weeks, often recurring |

#### Background

Professional **broadcast-like** cadence. Chapter 62 adds specialized production (costume, makeup, props, stunts) and early marketing (trailer/poster). Host maps those to pack craft agents and **scheduled publishing** + stronger fact/legal gates for news-adjacent work.

#### When to use

- Recurring show packaging  
- Corporate training series (F) with SME  
- Documentary “explained” segment (I light)  
- Multi-language localization required  

#### Who should use

Showrunner/EP, compliance officer, channel manager, instructional designer (training).

#### How to use

1. **scale_profile = S3**.  
2. Require **Compliance + Legal** before distribution.  
3. Turn on **MemoryAgent** project bible for series continuity.  
4. Distribution: social + streaming + archive (+ broadcast if needed).  
5. Post-launch: **CorrectionsAgent** path for factual shows.  

#### Agents (add beyond S2)

- Series: `video.showrunner`, `video.standardseditor`  
- Craft: `video.costumedesign`, `video.mua_makeup`, `video.productiondesign`, `video.choreography`  
- Docs/news: `video.journalist`, `video.factchecker`, `video.citation`  
- Education: `video.instructionaldesign`, `video.sme`, `video.lms`, `video.learnersim`  
- Marketing: `video.trailereditor`, `video.marketing`, `video.seo`  
- A11y: `video.signlanguageinterpreter`, `video.localizationqa`  

#### Data flow (S3)

```text
Series bible (Memory)
  → Showrunner + Planner seasonal plan
  → Episode brief → Screenwriter + SME
  → FactChecker / Compliance pre-clear
  → Production unit (Director/DoP/Prompt pool)
  → Post unit (Editor/Color/Sound/A11y)
  → StandardsEditor + Legal gate
  → ChannelManager multi-platform schedule
  → Analyst + Corrections feedback into Memory
```

#### DNA

| Archetype | DNA |
|-----------|-----|
| F Corporate training | `wf_video_arch_f_corporate_training_v1.dna.json` |
| I Documentary (segment) | `wf_video_arch_i_documentary_v1.dna.json` |
| C Explainer (premium) | `wf_video_arch_c_animated_explainer_v1.dna.json` |

---

### S4 — Medium-Large Production

| Attribute | Guidance |
|-----------|----------|
| **Budget** | ~$50K–$5M |
| **Team** | 20–200 humans + **~55–75 agents** |
| **Content** | Talk/late-night, sitcom, music video, stage |
| **Cycle** | 1–6 months |

#### Background

Premium television / high-end digital. Chapter 62 enables **full marketing stack** and inference/optimization agents. Host activates music-video and performance-marketing depth, rights-heavy clearance, and multi-outlet packaging in parallel (workflow §3.0 distribution branching).

#### When to use

- Music video (G) with live + AI VFX  
- Premium brand film  
- Multi-episode comedy/talk packaging  
- Label/digital release coordination  

#### Who should use

Label A&R / music video director, series producer, rights counsel, marketing lead.

#### How to use

1. **scale_profile = S4**.  
2. Parallel tracks: **picture** ∥ **sound** ∥ **marketing** from mid-production.  
3. Rights: `video.legal`, `video.musicsupervisor`, sample clearance before master.  
4. Ensemble/routing design via `video.router` + cost/latency optimizers (policy only until live tools enabled).  
5. Trailer cutdown starts before final picture lock when possible.  

#### Agents (add beyond S3)

- MV: `video.musicvideodirector`, `video.musicsupervisor`, `video.labela_r`, `video.labeldigital`  
- Perf: `video.casting`, `video.talent`, `video.choreography`  
- Growth: `video.roasoptimizer`, `video.retentionoptimizer`, `video.community`  
- Infra meta: `video.latencyoptimizer`, `video.costoptimizer`, `video.evaluationharness`  
- Safety: `video.safetyredteam`, `video.deepfakedetection`  

#### Data flow (S4)

```text
Greenlight (budget + rights register)
  → MusicVideoDirector / Showrunner concept pack
  → Choreography + Casting + ProductionDesign
  → Dual pipeline:
       Picture: DoP + Prompt pool + Continuity + VFX
       Audio: Composer + SoundMixer + MusicSupervisor
  → Editor picture lock candidate
  → Parallel: TrailerEditor + SocialMediaStrategist
  → Legal/Compliance/DeepfakeDetection gate
  → LabelDigital + Distributor multi-branch delivery
  → Analyst + ROAS/Retention optimizers → next episode plan
```

#### DNA

| Archetype | DNA |
|-----------|-----|
| G Music video | `wf_video_arch_g_music_video_v1.dna.json` |
| E Short film (premium) | `wf_video_arch_e_ai_short_film_v1.dna.json` |

---

### S5 — Large Production

| Attribute | Guidance |
|-----------|----------|
| **Budget** | ~$200K–$50M |
| **Team** | 50–500 humans + **~75–95 agents** |
| **Content** | Reality, variety, sports, concert, awards |
| **Cycle** | 2–12 months |

#### Background

Multi-unit simultaneous operations. Chapter 62 stresses **Audience Simulation**, award/campaign agents, merchandise. Host must support multi-crew fan-out, live-event timing, and heavy analytics.

#### When to use

- Multi-camera live or live-to-tape packaging  
- Large sports/concert highlight factories  
- Award-show style multi-segment shows  
- Enterprise multi-region campaigns  

#### Who should use

Network EP, sports producer, live showrunner, campaign strategist.

#### How to use

1. **scale_profile = S5**.  
2. Orchestrator runs **multiple concurrent unit DAGs** under one production id.  
3. AudienceSim + Analyst on every major segment.  
4. Comms + Community for real-time reputation.  
5. Formal HiTL on safety/rights segments.  

#### Agents (add beyond S4)

- Live/sports: `video.sportsanalyst`, `video.dronepilot`, `video.cameraoperator`  
- Campaign: `video.awardsstrategist`, `video.festivalstrategist`, `video.comms`  
- Sim: `video.audiencesim` (heavy), `video.emotionalarc`  
- Sales: `video.sales`, `video.crm`  
- Trust: `video.trustsafety`, `video.ethics`  

#### Data flow (S5)

```text
Production calendar (Planner)
  → Unit A (stage) ∥ Unit B (field) ∥ Unit C (social desk)
  → Orchestrator merge gates at segment boundaries
  → Editor multi-timeline assemble
  → AudienceSim segment test
  → Standards + Legal + TrustSafety
  → Multi-branch delivery (broadcast/stream/social/archive)
  → Live analytics loop → Planner re-prioritize remaining segments
```

#### DNA

Compose from **spine + E/I/G** patterns; use `wf_video_production_e2e_v1.dna.json` / `wf_video_spine_v1.dna.json` as backbone and attach specialty crews.

---

### S6 — Very Large Production

| Attribute | Guidance |
|-----------|----------|
| **Budget** | ~$300K–$30M |
| **Team** | 30–400 humans + **~90–110 agents** |
| **Content** | Documentary, docuseries, nature, historical, limited series |
| **Cycle** | 3–24 months |

#### Background

Research-heavy, archive-heavy, cultural authenticity. Chapter 62 highlights dataset/curation and long post. Host emphasizes **archive research**, **fact-check mesh**, **ethics**, multilingual packaging, and long-term memory.

#### When to use

- Documentary explained episode / series (I)  
- Historical or scientific limited series  
- Multi-language global launch  

#### Who should use

Showrunner, journalist/research lead, archive producer, standards & ethics board.

#### How to use

1. **scale_profile = S6**.  
2. Research track starts **before** full greenlight.  
3. Dual clearance: **Legal (rights)** + **Ethics (portrayal)**.  
4. ArchiveMaster + ArchiveResearch mandatory for stock.  
5. Corrections pipeline post-launch is mandatory.  

#### Agents (add beyond S5)

- Research: `video.archiveresearch`, `video.archiveproducer`, `video.archivemaster`, `video.webresearch`, `video.benchmarkresearch`, `video.interviewsynthesis`  
- Journalism: `video.journalist`, `video.factchecker`, `video.citation`, `video.corrections`, `video.standardseditor`  
- Domain: `video.medicalillustrator`, `video.sme`  
- Localization: `video.localizationqa` (full)  

#### Data flow (S6)

```text
Research brief
  → WebResearch + ArchiveResearch → SourceCatalog (Memory)
  → Journalist + Screenwriter treatment
  → FactChecker continuous mesh
  → Greenlight (Producer/Finance/Legal/Ethics)
  → Production (Director/DoP/ArchiveProducer inserts)
  → Post (Editor/VO/Color/Sound)
  → FactChecker + Legal + StandardsEditor + Ethics gates
  → Channel + SEO + ArchiveMaster package
  → Corrections + Analyst closed loop → distillation tickets
```

#### DNA

| Archetype | DNA |
|-----------|-----|
| I Documentary | `wf_video_arch_i_documentary_v1.dna.json` |
| E Short (docu-drama) | `wf_video_arch_e_ai_short_film_v1.dna.json` |

---

### S7 — Premium / Cinematic Production

| Attribute | Guidance |
|-----------|----------|
| **Budget** | ~$5M–$500M |
| **Team** | 200–2000+ humans + **phased full 114-agent pool** |
| **Content** | Feature, animated feature, epic, sci-fi film |
| **Cycle** | 6–60 months |

#### Background

Chapter 62’s premium tier: global infrastructure, parallel VFX, formal release governance. Host maps to **Archetype J**, full L1/L2/L3, C2PA/provenance expectations, festival/awards strategy, multi-territory sales, and long-tail learning. This is the only scale that routinely **schedules nearly the entire roster** across phases (not all 114 simultaneously).

#### When to use

- Feature-length AI-assisted film  
- High-risk IP/likeness/consent productions  
- Multi-territory theatrical + streaming + broadcast + archive  

#### Who should use

Studio EP, director, legal/compliance leadership, sales/distribution, festival strategist—**with mandatory HiTL** on consent, ethics, MPA, final release.

#### How to use

1. **scale_profile = S7**.  
2. Phase gates are **hard** (GateKeeper + human).  
3. Character bank + reference frame bank required for principal cast.  
4. Full distribution matrix (theatrical/stream/broadcast/archive + marketing).  
5. Awards/festival track optional but planned early.  
6. Promote tools only via host production activation + credentials—not SPEC prose.  

#### Agents (full pool by phase)

**Development:**  
`video.screenwriter`, `video.producer`, `video.director`, `video.conceptartist`, `video.casting`, `video.legal`, `video.ideation`, `video.novelty`, `video.narrativearc`

**Pre-production:**  
`video.storyboard`, `video.productiondesign`, `video.costumedesign`, `video.mua_makeup`, `video.continuity`, `video.worldbuilding`, `video.moodboard`

**Production:**  
`video.promptengineer`, `video.cinematographer`, `video.cameraoperator`, `video.voiceclone`, `video.lipsync`, `video.composer`, `video.aiqaconsistency`, `video.avatardesign`, `video.vfxsupervisor`

**Post:**  
`video.editor`, `video.colorist`, `video.soundmixer`, `video.sounddesign`, `video.trailereditor`

**Review:**  
`video.judge`, `video.gatekeeper`, `video.audiencesim`, `video.mpa`, `video.ethics`, `video.compliance`, `video.critic`

**Distribution:**  
`video.sales`, `video.distributor`, `video.marketing`, `video.archivemaster`, `video.festivalstrategist`, `video.awardsstrategist`

**Meta (continuous):**  
`video.orchestrator`, `video.planner`, `video.router`, `video.memory`, `video.evaluationharness`, `video.costoptimizer`, `video.latencyoptimizer`

*(All other pack agents available as specialty inserts: food, travel, sports, real estate, etc.)*

#### Data flow (S7)

```text
IP / rights intake (Legal + Ethics + TrustSafety)
  → Development writers' room (Screenwriter + Novelty + NarrativeArc)
  → Greenlight board (Producer + Finance + Compliance + HiTL)
  → Pre-prod bible (Storyboard + ProdDesign + Costume + Continuity) → Memory
  → Production DAG (Orchestrator)
       per sequence: Director → Prompt pool → AIQAConsistency → Continuity
       audio track parallel: Composer / Voice / LipSync
  → Post DAG: Editor → VFX → Color → Sound
  → Review mesh: AudienceSim + Critic + MPA + Legal (C2PA) + HiTL final
  → Sales/Distributor multi-territory packages
  → Trailer/Marketing/Festival/Awards parallel
  → ArchiveMaster long-term
  → Analyst + EvaluationHarness + PromptOptimizer closed loop (years)
```

#### DNA

| Archetype | DNA |
|-----------|-----|
| J Feature film | `wf_video_arch_j_feature_film_v1.dna.json` |
| Delivery | `wf_video_delivery_v1.dna.json` |
| E2E | `wf_video_production_e2e_v1.dna.json` |

---

## 6. Scale × Archetype Matrix

| Archetype | Primary scales | Host DNA |
|-----------|----------------|----------|
| **A** Viral Hook | S1–S2 | `wf_video_arch_a_viral_hook_v1` |
| **B** UGC Ad | S1–S3 | `wf_video_arch_b_ugc_ad_v1` |
| **C** Animated Explainer | S2–S4 | `wf_video_arch_c_animated_explainer_v1` |
| **D** Personalized Birthday | S1–S2 | `wf_video_arch_d_personalized_birthday_v1` |
| **E** AI Short Film | S2–S5 | `wf_video_arch_e_ai_short_film_v1` |
| **F** Corporate Training | S2–S5 | `wf_video_arch_f_corporate_training_v1` |
| **G** Music Video | S3–S5 | `wf_video_arch_g_music_video_v1` |
| **H** AI Avatar | S1–S4 | `wf_video_arch_h_ai_avatar_v1` |
| **I** Documentary | S4–S6 | `wf_video_arch_i_documentary_v1` |
| **J** Feature Film | S6–S7 | `wf_video_arch_j_feature_film_v1` |

**Rule:** pick **scale first** (budget/time/risk), then **archetype** (content shape). Planner must not schedule S7 crew for S1 budgets.

---

## 7. Quality & Critique by Scale

| Scale | L1 | L2 | L3 / HiTL | Critique density |
|-------|----|----|-----------|------------------|
| S1 | Required | Light | Rare (legal only) | Sparse |
| S2 | Required | Standard ≥90 | Brand/compliance | Moderate |
| S3 | Required | Standard | SME + legal | Dense on facts |
| S4 | Required | Strict | Rights + deepfake | Parallel picture/sound |
| S5 | Required | Strict | Live safety | Multi-unit merge gates |
| S6 | Required | Strict | Ethics + corrections | Continuous fact mesh |
| S7 | Required | Strict | Formal release board | Full mesh + festival sim |

Universal success criteria remain those in workflow §5 (craft metrics, delivery QC mesh). Surpass-human signals stay **benchmark / blind preference**, not marketing claims.

---

## 8. Implementation Mapping (host today)

| Framework need | Host mechanism |
|----------------|----------------|
| Scale profile | Greenlight packet field + Planner constraints |
| Agent crew | Pack agents `video.*` + DNA node lists |
| DAG execution | GraphEngine / workflow DNA / Orchestrator role |
| Offline craft proof | PackAgentRunner + `knowledge_usage` report |
| Live tools | Tool broker + media adapters (fail-closed) |
| Human gates | Approvals API + GateKeeper/Judge |
| Live UI updates | SSE event projections (not agent→UI) |
| Learning loop | Analyst + EvaluationHarness + prompt/rubric updates |

**Not yet full chapter-62 ASAAF automation:** automatic S1→S7 agent-count autoscaler, Ray/K8s agent pools, and live multi-provider ensembles remain **roadmap**. This document defines **what to schedule**; host production flags decide **what can execute live**.

---

## 9. Operator Checklist (any scale)

1. [ ] Set **scale_profile** S1–S7 and **archetype** A–J  
2. [ ] Confirm budget/rights greenlight owners  
3. [ ] Select DNA workflow file under `business/video/design/workflows/`  
4. [ ] Review scheduled agent list vs scale band (do not over-activate)  
5. [ ] Confirm fail-closed: no silent production activation  
6. [ ] Require L1; set L2 threshold by scale  
7. [ ] Define distribution branches (S2+ multi-branch)  
8. [ ] After run: inspect **knowledge_usage** (test/UAT) and audit evidence_refs  
9. [ ] Post-launch: Analyst tickets → Memory / prompt / routing updates  

---

## 10. Document Control

| Item | Value |
|------|--------|
| Supersedes | Ad-hoc scale notes only |
| Complements | `ai_agent_video_production_workflow.md`, chapter_62, DNA workflows |
| Agent authority | `business/video/agents/*/agent_spec.json` |
| Re-export UI | `scripts/business/export_pack_agents_for_ui.py` after agent changes |

---

*End of `production_scale_framework.md`.*  
*Scale-aware crews for common-agent-swarm-ops — grounded in chapter 62 economics and VA workflow common terms, bound to host pack agents and DNA graphs.*
