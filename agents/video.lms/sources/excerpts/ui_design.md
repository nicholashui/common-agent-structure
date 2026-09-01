# VA Agent Swarm — Complete UI Layout Design

> Covers every operation in the [Composition Diagram](../agents.md#composition-diagram) and provides a full production-start journey for all 10 workflow types (A–J).

---

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [Information Architecture](#2-information-architecture)
3. [Master Shell Layout](#3-master-shell-layout)
4. [Surface Inventory](#4-surface-inventory)
5. [Page-by-Page Breakdown](#5-page-by-page-breakdown)
6. [Production Start Flow](#6-production-start-flow)
7. [Composition Diagram Coverage Map](#7-composition-diagram-coverage-map)
8. [Responsive & Accessibility Notes](#8-responsive--accessibility-notes)
9. [Component Library Summary](#9-component-library-summary)
10. [Interaction Patterns](#10-interaction-patterns)

---

## 1. Design Philosophy

### 1.1 Core Principles

| Principle | Rationale |
|-----------|-----------|
| **Brief-First** | Every production starts from a human brief; UI makes brief-entry the gravity center |
| **Progressive Disclosure** | 114 agents are overwhelming; show only what the current phase needs |
| **Live DAG Visibility** | The Composition Diagram runs in real-time; users must see agent state at a glance |
| **Gate-Driven Confidence** | GateKeeperAgent phase transitions surface as explicit approval moments in the UI |
| **Critique Transparency** | Every agent critique message is viewable, searchable, and actionable |
| **Production-Type Aware** | The 10 workflow templates (A–J) shape which agents activate and which panels appear |

### 1.2 Target Users

| Persona | Needs |
|---------|-------|
| **Creator** | Start production fast, review outputs, approve gates |
| **Producer** | Monitor budget/schedule, resolve escalations, manage team |
| **Technical Operator** | Tune prompts, inspect agent logs, manage model routing |
| **Reviewer/Client** | View deliverables, leave feedback, approve final |


---

## 2. Information Architecture

```text
ROOT
├── Dashboard (Home)
│   ├── Active Productions Grid
│   ├── Quick-Start Brief Wizard
│   └── System Health Banner
│
├── Brief Studio
│   ├── Template Selector (A–J workflows)
│   ├── Brief Editor (structured + freeform)
│   ├── Reference Upload (mood boards, scripts, assets)
│   └── Launch Confirmation (→ PlannerAgent)
│
├── Production Console (per-production)
│   ├── DAG Canvas (live Composition Diagram)
│   │   ├── Agent Nodes (state: idle/running/blocked/done)
│   │   ├── Edge Flows (artifact handoffs)
│   │   └── Gate Checkpoints (approve/reject/comment)
│   │
│   ├── Timeline View
│   │   ├── Phase Swimlanes (Pre-pro → Production → Post → Delivery)
│   │   ├── Milestone Markers
│   │   └── Budget Burn Overlay
│   │
│   ├── Agent Inspector (drill-down panel)
│   │   ├── Agent Identity & Role
│   │   ├── Current Task & Progress
│   │   ├── Input/Output Artifacts
│   │   ├── Critique Bus (sent/received)
│   │   ├── Quality Metrics (self-score vs threshold)
│   │   └── Tool Calls Log
│   │
│   ├── Artifact Gallery
│   │   ├── Grid/List Toggle
│   │   ├── Version History per Artifact
│   │   ├── Preview (video/audio/image/text)
│   │   ├── Provenance Chain (C2PA)
│   │   └── Compare Mode (A/B side-by-side)
│   │
│   ├── Critique Feed
│   │   ├── Chronological Message Stream
│   │   ├── Filter by Agent / Phase / Severity
│   │   └── Human Intervention Slot
│   │
│   └── Gate Control Panel
│       ├── Pending Approvals Queue
│       ├── Gate Criteria Checklist (L1/L2/L3)
│       ├── Approve / Reject / Request Changes
│       └── C2PA Sign-off Confirmation
│
├── Agent Registry
│   ├── All 114 Agents (searchable, filterable by category)
│   ├── Agent Detail Card (capabilities, tools, patterns)
│   ├── Dependency Graph
│   └── Performance Benchmarks
│
├── Memory & Knowledge
│   ├── Project Memory (MemoryAgent contents)
│   ├── Episodic Log (Reflexion entries)
│   ├── Series Bible / World-Building DB
│   └── Brand Asset Library
│
├── Delivery Hub
│   ├── Master Package Builder
│   ├── Channel-Specific Variants
│   ├── QC Status Matrix
│   ├── Distribution Tracker
│   └── Analytics Dashboard (post-release)
│
├── Settings & Admin
│   ├── Model Routing Config (RouterAgent rules)
│   ├── Cost/Latency Budgets
│   ├── API Key Management
│   ├── Team & Permissions
│   └── Compliance Config (constitutions, consent DB)
│
└── Help & Docs
    ├── Agent Glossary
    ├── Workflow Templates Guide
    └── API Reference
```


---

## 3. Master Shell Layout

### 3.1 Shell Anatomy

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  TOP BAR (64px)                                                              │
│  ┌──────┬──────────────────────────────┬───────────────────────────────────┐ │
│  │ Logo │  Global Search (Cmd+K)       │  Notifications │ User │ Settings │ │
│  └──────┴──────────────────────────────┴───────────────────────────────────┘ │
├────────┬─────────────────────────────────────────────────────────────────────┤
│  SIDE  │  MAIN CANVAS                                                        │
│  NAV   │                                                                     │
│ (72px) │  ┌─────────────────────────────────────────────────────────────┐    │
│        │  │  CONTEXT BAR (production name, phase, budget, health)       │    │
│  ○ Dash│  ├─────────────────────────────────────────────────────────────┤    │
│  ○ Brief│ │                                                             │    │
│  ○ Prod │ │              PRIMARY VIEW AREA                              │    │
│  ○ Agents│ │          (DAG / Timeline / Gallery / Feed)                 │    │
│  ○ Memory│ │                                                            │    │
│  ○ Deliver│ │                                                           │    │
│  ○ Settings│ │                                                          │    │
│        │  │                                                             │    │
│        │  ├─────────────────────────────────────────────────────────────┤    │
│        │  │  DETAIL DRAWER (slides up: Agent Inspector / Artifact View) │    │
│        │  └─────────────────────────────────────────────────────────────┘    │
│        │                                                                     │
├────────┴─────────────────────────────────────────────────────────────────────┤
│  STATUS BAR (32px)                                                           │
│  Running Agents: 12/27 │ Phase: Production │ Budget: $42/$100 │ ETA: 3m     │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Layout Zones

| Zone | Height/Width | Purpose |
|------|-------------|---------|
| Top Bar | 64px fixed | Global nav, search (searches agents, artifacts, critiques), notifications |
| Side Nav | 72px wide, icon-only (expands on hover to 240px with labels) | Primary navigation |
| Context Bar | 48px fixed | Current production context breadcrumb |
| Primary View | Flex-grow | The active workspace surface |
| Detail Drawer | 0–50% from bottom, resizable | Inspector / preview without leaving context |
| Status Bar | 32px fixed | Live production telemetry at a glance |

### 3.3 Navigation Model

| Level | Mechanism | Example |
|-------|-----------|---------|
| L0 — App sections | Side Nav icons | Dashboard → Brief Studio → Production Console |
| L1 — Views within section | Tab bar inside Primary View | DAG Canvas │ Timeline │ Gallery │ Critique Feed |
| L2 — Detail | Drawer (bottom) or Modal | Agent Inspector, Artifact Viewer, Gate Approval Dialog |
| L3 — Contextual actions | Right-click menu / Command Palette (Cmd+K) | "Retry agent", "Compare versions", "Export artifact" |


---

## 4. Surface Inventory

Every UI surface maps to one or more Composition Diagram operations:

| # | Surface | Composition Diagram Operation(s) | Primary Agent(s) Served |
|---|---------|----------------------------------|------------------------|
| S1 | Brief Wizard | `[Brief]` entry point | User → PlannerAgent |
| S2 | Template Selector | Workflow type selection (A–J) | PlannerAgent |
| S3 | DAG Canvas | Full `PlannerAgent → OrchestratorAgent → RouterAgent → Craft Agents` flow | OrchestratorAgent, RouterAgent |
| S4 | Agent Node Card | Individual agent status within DAG | Any of 114 agents |
| S5 | Gate Approval Dialog | `GateKeeperAgent` phase transitions | GateKeeperAgent, JudgeAgent |
| S6 | Critique Feed | `CritiqueMessages` bus | All agents (bi-directional) |
| S7 | Memory Panel | `MemoryAgent` retrieval/store | MemoryAgent |
| S8 | Agent Inspector | Agent drill-down (tools, metrics, I/O) | Any agent |
| S9 | Artifact Gallery | Outputs from all craft agents | 52 craft agents (§1–§8) |
| S10 | Artifact Viewer | Preview + compare + provenance | All producing agents |
| S11 | Timeline View | Schedule/phase visualization | ProducerAgent, OrchestratorAgent |
| S12 | Budget Tracker | Cost monitoring | ProducerAgent, CostOptimizerAgent |
| S13 | Router Config | Model/agent routing rules | RouterAgent, CostOptimizerAgent |
| S14 | Prompt Lab | Prompt editing + optimization | PromptEngineerAgent, PromptOptimizerAgent |
| S15 | Quality Dashboard | VBench/EvalCrafter/CLIP-T scores | AIQAConsistencyAgent, EvalHarnessAgent |
| S16 | Delivery Packager | Channel-specific export | DistributorAgent, SoundMixerAgent, ColoristAgent |
| S17 | Analytics Panel | Post-release performance | AnalystAgent, RetentionOptimizerAgent |
| S18 | Compliance Checker | Legal/consent/C2PA status | ComplianceAgent, TrustSafetyAgent |
| S19 | Creative Meta Panel | Ideation/Narrative/Style/Mood/Novelty/Emotion | Creative meta-agents (§9.2) |
| S20 | Research Panel | Web/Archive/Trend/Competitor/Citation | Research meta-agents (§9.3) |
| S21 | Optimization Panel | Prompt/Cost/Latency/Retention/ROAS/A11y | Optimization meta-agents (§9.4) |
| S22 | Notification Center | Escalations, approvals, alerts | ProducerAgent, all gate agents |
| S23 | Team / Permissions | Human-in-the-loop configuration | Admin |
| S24 | Series Bible Editor | Long-running episodic memory | ShowrunnerAgent, WorldBuildingAgent |


---

## 5. Page-by-Page Breakdown

### 5.1 Dashboard (Home)

```text
┌─────────────────────────────────────────────────────────────────────┐
│  DASHBOARD                                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─── QUICK START ──────────────────────────────────────────────┐   │
│  │  [+ New Production]  "Describe what you want to create..."   │   │
│  │  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ...     │   │
│  │  │ A  │ │ B  │ │ C  │ │ D  │ │ E  │ │ F  │ │ G  │         │   │
│  │  │Hook│ │UGC │ │Expl│ │Bday│ │Film│ │Corp│ │ MV │         │   │
│  │  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘         │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─── ACTIVE PRODUCTIONS ──────────────────────────────────────┐    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │    │
│  │  │ Proj "Luna"  │  │ Proj "Spark" │  │ Proj "Atlas" │      │    │
│  │  │ Type: E      │  │ Type: B      │  │ Type: I      │      │    │
│  │  │ Phase: Post  │  │ Phase: Prod  │  │ Phase: Pre   │      │    │
│  │  │ ████████░░   │  │ ██████░░░░   │  │ ██░░░░░░░░   │      │    │
│  │  │ 80% · $62    │  │ 55% · $28    │  │ 15% · $8     │      │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘      │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── SYSTEM HEALTH ──────────────────────────────────────────┐     │
│  │  Agents Online: 114/114  │  Pending Gates: 3  │  Alerts: 1 │     │
│  └─────────────────────────────────────────────────────────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Key Interactions:**
- Click template card (A–J) → opens Brief Studio pre-loaded with that workflow
- Click production card → opens Production Console for that project
- "+ New Production" or type in search → Brief Studio (blank)


### 5.2 Brief Studio

```text
┌─────────────────────────────────────────────────────────────────────┐
│  BRIEF STUDIO                                          [Launch ▶]   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─── STEP 1: TEMPLATE ────────────────────────────────────────┐    │
│  │  Selected: [E] AI Short Film                                │    │
│  │  (shows activated agents for this template in preview)      │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── STEP 2: BRIEF DETAILS ──────────────────────────────────┐    │
│  │                                                             │    │
│  │  Title: ___________________________                         │    │
│  │  Vision Statement: (freeform, 2–5 sentences)                │    │
│  │  ┌──────────────────────────────────────────────┐           │    │
│  │  │                                              │           │    │
│  │  └──────────────────────────────────────────────┘           │    │
│  │                                                             │    │
│  │  Genre: [Dropdown]    Duration: [Slider 15s–120min]         │    │
│  │  Aspect Ratio: ○16:9 ○9:16 ○1:1 ○4:3                       │    │
│  │  Tone: [Tag input: cinematic, moody, ...]                   │    │
│  │  Target Audience: [Dropdown + custom]                       │    │
│  │  Budget Cap: [$___]   Deadline: [Date picker]               │    │
│  │                                                             │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── STEP 3: REFERENCES ─────────────────────────────────────┐    │
│  │                                                             │    │
│  │  [Drop Zone: scripts, mood images, reference videos, audio] │    │
│  │  ┌────┐ ┌────┐ ┌────┐ ┌──────────────────────────┐         │    │
│  │  │.fdx│ │.png│ │.mp4│ │  + Add from Brand Library │         │    │
│  │  └────┘ └────┘ └────┘ └──────────────────────────┘         │    │
│  │                                                             │    │
│  │  Style References: [Paste URL or upload]                    │    │
│  │  Voice/Talent Preferences: [Select from library]            │    │
│  │                                                             │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── STEP 4: CONSTRAINTS & COMPLIANCE ───────────────────────┐    │
│  │  ☑ Require C2PA provenance signing                          │    │
│  │  ☑ WCAG 2.2 AA accessibility                                │    │
│  │  ☐ SAG-AFTRA AI consent verification                        │    │
│  │  ☐ GDPR/CCPA personal data handling                         │    │
│  │  Platform targets: ☑YouTube ☑TikTok ☐Meta ☐Broadcast       │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── STEP 5: REVIEW & LAUNCH ────────────────────────────────┐    │
│  │  Plan Preview: PlannerAgent will decompose into ~N phases   │    │
│  │  Estimated agents: 34 │ Est. cost: $XX │ Est. time: Xm      │    │
│  │                                                             │    │
│  │       [ Save Draft ]    [ ▶ LAUNCH PRODUCTION ]             │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Template-Specific Presets:**

| Template | Pre-filled Fields | Activated Agent Groups |
|----------|-------------------|----------------------|
| A — Viral Hook | 15–60s, 9:16, TikTok/Reels targets | Hook agents, UGC, Trend, Social, Retention |
| B — UGC Ad | 15–45s, 9:16, performance targets | UGC, Performance, Brand, Copy, A/B |
| C — Animated Explainer | 60–180s, 16:9, education | Animator, MotionGraphics, Instructional, VO |
| D — Personalized Birthday | 30–60s, personalization vars | Personalization, Template, Avatar, Voice |
| E — AI Short Film | 3–15min, 16:9, cinematic | Full Above-the-Line + Camera + Editorial + Sound |
| F — Corporate Training | 5–30min, 16:9, SCORM/xAPI | Instructional, LMS, Avatar, SME, Assessment |
| G — Music Video | 3–5min, 16:9/9:16, beat-sync | MV Director, Choreography, Editor, Label A&R |
| H — AI Avatar | 1–10min, presenter-led | Avatar, Voice Clone, Lip Sync, Brand |
| I — Documentary | 10–90min, 16:9, archival | Journalist, Archive, Fact-Check, Standards |
| J — Feature Film | 90–180min, cinematic | Full 114-agent roster, all gates active |


### 5.3 Production Console — DAG Canvas

The heart of the UI. Renders the live Composition Diagram as an interactive node graph.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODUCTION: "Luna" (Type E: AI Short Film)     Phase: Production  ⏱ 12m    │
├──────────────────┬──────────────────────────────────────────────────────────┤
│  VIEW TABS:      │                                                          │
│  [DAG] Timeline  │                                                          │
│  Gallery Critique│            ┌─────────────┐                               │
│                  │            │  [Brief]    │                               │
│  FILTER:         │            └──────┬──────┘                               │
│  ○ All           │                   │                                      │
│  ○ Active        │                   ▼                                      │
│  ○ Blocked       │        ┌──────────────────┐                              │
│  ○ Completed     │        │  PlannerAgent    │                              │
│                  │        │  ✓ Complete      │                              │
│  ZOOM: [─────●]  │        └────────┬─────────┘                              │
│                  │                 │                                         │
│  LAYERS:         │                 ▼                                         │
│  ☑ Orchestration │     ┌─────────────────────┐                              │
│  ☑ Craft         │     │  OrchestratorAgent  │                              │
│  ☑ Meta-Creative │     │  ● Running          │                              │
│  ☑ Meta-Research │     └────┬───────────┬────┘                              │
│  ☑ Meta-Optimize │          │           │                                   │
│  ☑ Critique      │          ▼           ▼                                   │
│                  │   ┌───────────┐  ┌──────────────┐                        │
│                  │   │RouterAgent│  │MemoryAgent   │                        │
│                  │   │ ● Running │  │ ● Listening  │                        │
│                  │   └─────┬─────┘  └──────────────┘                        │
│                  │         │                                                 │
│                  │    ┌────┼────┬────────┬──────────┐                        │
│                  │    ▼    ▼    ▼        ▼          ▼                        │
│                  │ ┌────┐┌────┐┌────┐┌────────┐┌────────┐                   │
│                  │ │Dir ││DoP ││Edit││Composer││VFX Sup │                   │
│                  │ │ ●  ││ ○  ││ ○  ││  ○     ││  ○     │                   │
│                  │ └────┘└────┘└────┘└────────┘└────────┘                   │
│                  │         │         ▲                                       │
│                  │         ▼         │                                       │
│                  │  ┌──────────────────────┐                                │
│                  │  │   GateKeeperAgent    │                                │
│                  │  │   ⚠ Awaiting Approval │                                │
│                  │  └──────────────────────┘                                │
│                  │         ▲                                                 │
│                  │         │                                                 │
│                  │  ┌──────────────┐                                        │
│                  │  │  JudgeAgent  │                                        │
│                  │  │  ● Scoring   │                                        │
│                  │  └──────────────┘                                        │
│                  │                                                          │
├──────────────────┴──────────────────────────────────────────────────────────┤
│  DETAIL DRAWER ▲                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ DirectorAgent │ Task: Shot Intent #4 │ Score: CLIP-T 0.34 (✓≥0.32)  │   │
│  │ Input: Scene 2 script │ Output: shot_intent_04.json │ Critiques: 2   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**DAG Node States:**
| Symbol | State | Color |
|--------|-------|-------|
| ✓ | Complete | Green |
| ● | Running | Blue (pulsing) |
| ○ | Idle/Queued | Gray |
| ⚠ | Blocked/Needs Approval | Amber |
| ✗ | Failed | Red |

**DAG Interactions:**
- Click node → opens Agent Inspector in Detail Drawer
- Double-click node → full-screen Agent Inspector
- Click edge → shows artifact being passed
- Click GateKeeper → opens Gate Approval Dialog
- Right-click node → context menu: Retry, Skip, Inspect, View Critiques
- Drag to pan, scroll to zoom, Ctrl+click to multi-select


### 5.4 Production Console — Timeline View

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  TIMELINE VIEW                                                    Budget: $42│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  t=0          t=2m        t=5m        t=8m       t=12m       t=15m (est)   │
│  │            │           │           │          │           │              │
│  ├────────────┼───────────┼───────────┼──────────┼───────────┤              │
│  │            │           │           │          │           │              │
│  │ PRE-PRODUCTION         │           │          │           │              │
│  │ ████████████████       │           │          │           │              │
│  │ Plan│Screen│Story│Cast │           │          │           │              │
│  │            │           │           │          │           │              │
│  │            │ PRODUCTION            │          │           │              │
│  │            │ ░░░░░░░░░░████████████│          │           │              │
│  │            │ Dir│DoP│Camera│Gen│VFX│          │           │              │
│  │            │           │           │          │           │              │
│  │            │           │    POST-PRODUCTION   │           │              │
│  │            │           │    ░░░░░░░░░░░░░░░░░░████        │              │
│  │            │           │    Edit│Color│Sound│Mix│         │              │
│  │            │           │           │          │           │              │
│  │            │           │           │    DELIVERY          │              │
│  │            │           │           │    ░░░░░░░░░░░░░░░░░░│              │
│  │            │           │           │    QC│Package│Dist   │              │
│  │            │           │           │          │           │              │
│  ├──Gate 1────┼──Gate 2───┼──Gate 3───┼──Gate 4──┼───────────┤              │
│  │  ✓ Pass    │  ✓ Pass   │  ⚠ Review │  ○ Pend  │  ○ Pend   │              │
│  │            │           │           │          │           │              │
│  │─── Budget Burn Line ─────────────────────────────$42──────│              │
│  │ $8         │ $22       │ $35       │ $42      │           │              │
│  └────────────┴───────────┴───────────┴──────────┴───────────┘              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.5 Production Console — Artifact Gallery

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  ARTIFACT GALLERY                      [Grid ▣] [List ≡]  Filter: [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ ▶ ░░░░░░░░░  │  │ ▶ ░░░░░░░░░  │  │   ┌─────┐   │  │  📄           │   │
│  │   Shot 1     │  │   Shot 2     │  │   │mood │   │  │  screenplay   │   │
│  │   v3 ✓      │  │   v2 ●      │  │   │board│   │  │  v4 ✓        │   │
│  │   by DoP     │  │   by DoP     │  │   └─────┘   │  │  by Writer    │   │
│  │   CLIP: 0.35 │  │   CLIP: 0.31 │  │  Concept v2 │  │  Beats: 12/12 │   │
│  │  [C2PA ✓]    │  │  [C2PA ✓]    │  │  by Concept │  │  [C2PA ✓]     │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ 🎵 ─────     │  │ 🎵 ─────     │  │ ▶ ░░░░░░░░░  │  │  📊 Chart    │   │
│  │  Score Cue 1 │  │  SFX Pack    │  │  Rough Cut   │  │  Quality     │   │
│  │  v1 ●       │  │  v2 ✓       │  │  v1 ⚠       │  │  Report      │   │
│  │  by Composer │  │  by SoundDes │  │  by Editor   │  │  by QA       │   │
│  │  Mood: 0.88  │  │  Sync: ✓     │  │  Pacing: B+  │  │  VBench: 0.8 │   │
│  │  [C2PA ✓]    │  │  [C2PA ✓]    │  │  [C2PA ✓]    │  │              │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                                             │
│  Showing 8 of 47 artifacts │ Page [1] 2 3 4 5 ►                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Artifact Card Features:**
- Thumbnail preview (video frame / waveform / image / doc icon)
- Version badge with state indicator
- Producing agent attribution
- Key quality metric
- C2PA provenance badge
- Click → opens Artifact Viewer in drawer (side-by-side compare, version history, full provenance chain)


### 5.6 Production Console — Critique Feed

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  CRITIQUE FEED              Filter: [All Agents ▼] [All Phases ▼] [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  12:04:32 │ EditorAgent → DirectorAgent                          Severity:│
│  ─────────┼──────────────────────────────────────────────────────── Info  │
│           │ "Pacing in Scene 3 exceeds genre prior by 1.2σ.                │
│           │  Suggest trimming B-roll between beats 7–8."                   │
│           │  📎 Attached: pacing_curve_s3.json                             │
│           │  [Accept] [Reject] [Discuss] [View Artifact]                   │
│           │                                                                │
│  12:03:58 │ AIQAConsistencyAgent → GeneratorAgent               Severity:│
│  ─────────┼──────────────────────────────────────────────────── Warning  │
│           │ "Frame 142–148: hand artifact detected (confidence 0.91).      │
│           │  Recommend re-roll with seed+1."                               │
│           │  📎 Attached: frame_142_annotated.png                          │
│           │  [Auto-Fix] [Manual Review] [Dismiss]                          │
│           │                                                                │
│  12:03:22 │ ComplianceAgent → ALL                               Severity:│
│  ─────────┼──────────────────────────────────────────────────── Critical │
│           │ "Voice clone consent for talent #3 expires in 48h.             │
│           │  Block delivery until renewal confirmed."                       │
│           │  [Resolve] [Escalate to Human] [Extend Deadline]               │
│           │                                                                │
│  12:02:45 │ JudgeAgent → ScreenwriterAgent + DirectorAgent      Severity:│
│  ─────────┼──────────────────────────────────────────────────────── Info  │
│           │ "Debate resolved: Act 2 midpoint placement at 52%              │
│           │  (DirectorAgent position) wins by rubric score 0.82 vs 0.71."  │
│           │  [View Debate Log] [View Rubric]                               │
│           │                                                                │
│  ── HUMAN INTERVENTION SLOT ────────────────────────────────────────────   │
│  │  💬 Type your critique or instruction to any agent...          [Send] │  │
│  │  @Agent: [autocomplete]  Priority: [Normal ▼]                         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.7 Gate Approval Dialog

```text
┌──────────────────────────────────────────────────────────┐
│  GATE APPROVAL — Phase: Pre-Production → Production       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Gate: #2 (Script Lock + Storyboard Approval)            │
│  GateKeeperAgent Assessment: READY FOR REVIEW            │
│  JudgeAgent Score: 0.87/1.00                             │
│                                                          │
│  ┌─── CRITERIA CHECKLIST ──────────────────────────────┐ │
│  │  ✓ Script beat-sheet coverage: 12/12 (100%)         │ │
│  │  ✓ Dialogue distinctiveness: 0.42 (≥0.35)          │ │
│  │  ✓ Storyboard shot coverage: 24/24 (100%)          │ │
│  │  ✓ Budget estimate within cap: $85 ≤ $100          │ │
│  │  ⚠ Style consistency: 0.83 (target ≥0.85)          │ │
│  │  ✓ Compliance pre-check: PASS                       │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌─── ARTIFACTS FOR REVIEW ────────────────────────────┐ │
│  │  📄 screenplay_v4.fdx    [Preview]                  │ │
│  │  🖼  storyboard_panels/  [Preview Gallery]          │ │
│  │  📊 budget_estimate.json [View]                     │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  Comments: ________________________________________      │
│                                                          │
│  [ ✓ APPROVE ]  [ ✗ REJECT ]  [ ↩ REQUEST CHANGES ]    │
│                                                          │
│  C2PA: Signing as [user@org]  ☑ Attach provenance       │
└──────────────────────────────────────────────────────────┘
```


### 5.8 Agent Inspector (Detail Drawer)

```text
┌──────────────────────────────────────────────────────────────────────────┐
│  AGENT INSPECTOR: DirectorAgent (#1)                        [Full Screen]│
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─── IDENTITY ──────────┐  ┌─── CURRENT TASK ──────────────────────┐   │
│  │ Category: Above-Line  │  │ Task: Generate Shot Intent #5          │   │
│  │ Pattern: Self-Refine  │  │ Status: ● Running (iteration 2/5)     │   │
│  │ Accepts from: 3 agents│  │ Started: 12:03:22                      │   │
│  │ Comments on: 4 agents │  │ Est. complete: 12:04:50                │   │
│  └───────────────────────┘  └────────────────────────────────────────┘   │
│                                                                          │
│  ┌─── QUALITY METRICS ──────────────────────────────────────────────┐    │
│  │  CLIP-T Score:  ████████████████░░░░  0.34 / 0.32 threshold ✓   │    │
│  │  Beat Coverage: ████████████████████  12/12 (100%) ✓            │    │
│  │  Pacing Match:  ██████████████░░░░░░  0.78 / 0.70 threshold ✓   │    │
│  │  Self-Refine Iterations: [2] of max [5]                          │    │
│  └──────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─── I/O ARTIFACTS ──────────────┐  ┌─── TOOL CALLS ───────────────┐   │
│  │ INPUT:                         │  │ 12:03:25 Sora 2 API          │   │
│  │  • screenplay_v4.fdx          │  │   prompt: "Close-up, rain..." │   │
│  │  • storyboard_panel_05.png    │  │   → generating (45s)          │   │
│  │  • mood_board_act2.json       │  │                               │   │
│  │                               │  │ 12:03:22 MemoryAgent.recall   │   │
│  │ OUTPUT:                        │  │   query: "Act 2 visual tone"  │   │
│  │  • shot_intent_05.json (v2)   │  │   → 3 results returned        │   │
│  │  • reference_frame_05.png     │  │                               │   │
│  └────────────────────────────────┘  └───────────────────────────────┘   │
│                                                                          │
│  ┌─── CRITIQUE BUS ────────────────────────────────────────────────┐     │
│  │ RECEIVED:                                                       │     │
│  │  • EditorAgent: "Shot 4 transition too abrupt" (12:02:58)      │     │
│  │  • AudienceSim: "Scene 2 clarity score 0.6, below 0.7" (12:01)│     │
│  │ SENT:                                                           │     │
│  │  • → EditorAgent: "Approved cut on beat 6" (12:03:10)          │     │
│  │  • → DoPAgent: "Use wider lens for Scene 3" (12:02:45)         │     │
│  └─────────────────────────────────────────────────────────────────┘     │
│                                                                          │
│  [Retry Task] [Skip] [Send Critique] [View Full History]                 │
└──────────────────────────────────────────────────────────────────────────┘
```

### 5.9 Agent Registry

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT REGISTRY                    Search: [____________]  Filter: [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CATEGORIES:                                                                │
│  [All 114] [Above-Line 5] [Camera 3] [Editorial 10] [Sound 4]             │
│  [Performance 5] [Distribution 4] [Education 14] [AI-Specialist 7]         │
│  [Meta-Orchestration 6] [Meta-Creative 7] [Meta-Research 7]                │
│  [Meta-Optimization 8] [Workflow Support 34]                               │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ # │ Agent               │ Pattern        │ Tools        │ Status    │   │
│  ├───┼─────────────────────┼────────────────┼──────────────┼───────────┤   │
│  │ 1 │ DirectorAgent       │ Self-Refine    │ Sora,Veo,Run │ ● Active  │   │
│  │ 2 │ ProducerAgent       │ Agentic Graph  │ Sheets,Tempo │ ● Active  │   │
│  │ 3 │ ScreenwriterAgent   │ Reflexion      │ Fountain,Emb │ ○ Idle    │   │
│  │ 4 │ ShowrunnerAgent     │ Multi-Debate   │ LongCtx,Vec  │ ○ Idle    │   │
│  │ ...│                    │                │              │           │   │
│  │46 │ PromptEngineerAgent │ DSPy/OPRO      │ Sora,Veo,Kli │ ● Active  │   │
│  │53 │ OrchestratorAgent   │ Agentic Graph  │ LangGraph    │ ● Active  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Click any row → opens Agent Detail Card with full capabilities table       │
└─────────────────────────────────────────────────────────────────────────────┘
```


### 5.10 Memory & Knowledge Panel

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  MEMORY & KNOWLEDGE                                                         │
├─────────────┬───────────────────────────────────────────────────────────────┤
│  SECTIONS:  │                                                               │
│             │  ┌─── PROJECT MEMORY (MemoryAgent) ──────────────────────┐    │
│  ● Project  │  │                                                       │    │
│    Memory   │  │  Search: [________________________] [Semantic] [Exact] │    │
│             │  │                                                       │    │
│  ○ Episodic │  │  Recent Entries:                                      │    │
│    Log      │  │  • "Act 2 tone: melancholic, rain motif" (12:02)     │    │
│             │  │  • "Character A wears blue in all exteriors" (11:58) │    │
│  ○ Series   │  │  • "Budget revised: VFX cap at $30" (11:45)         │    │
│    Bible    │  │  • "Style lock: Veo 3.1 seed #4412" (11:40)         │    │
│             │  │                                                       │    │
│  ○ Brand    │  │  Accessed by: DirectorAgent (6×), EditorAgent (3×),  │    │
│    Library  │  │              ScreenwriterAgent (2×)                   │    │
│             │  │                                                       │    │
│  ○ World    │  │  [+ Add Manual Entry]  [Export]  [Clear Stale]       │    │
│    DB       │  └───────────────────────────────────────────────────────┘    │
│             │                                                               │
└─────────────┴───────────────────────────────────────────────────────────────┘
```

### 5.11 Delivery Hub

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  DELIVERY HUB — "Luna"                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MASTER STATUS:  ⚠ 4/6 channels ready                                      │
│                                                                             │
│  ┌─── CHANNEL MATRIX ─────────────────────────────────────────────────┐    │
│  │ Channel    │ Format   │ QC     │ Captions │ A11y  │ C2PA  │ Status │    │
│  ├────────────┼──────────┼────────┼──────────┼───────┼───────┼────────┤    │
│  │ YouTube    │ H.264 4K │ ✓ Pass │ ✓ EN,ES  │ ✓ AA  │ ✓     │ Ready  │    │
│  │ TikTok     │ H.265 9:16│ ✓ Pass│ ✓ EN     │ ✓ AA  │ ✓     │ Ready  │    │
│  │ Meta       │ H.264 1080│ ✓ Pass│ ⚠ Pend  │ ✓ AA  │ ✓     │ ⚠ Pend │    │
│  │ Broadcast  │ ProRes 422│ ✓ Pass│ ✓ CC     │ ✓ AAA │ ✓     │ Ready  │    │
│  │ Theatrical │ DCP       │ ○ N/A │ ○ N/A    │ ○ N/A │ ✓     │ N/A    │    │
│  │ Archive    │ Master+Stems│✓ Pass│ ✓ All   │ ✓ AAA │ ✓     │ Ready  │    │
│  └────────────┴──────────┴────────┴──────────┴───────┴───────┴────────┘    │
│                                                                             │
│  ┌─── QC SUMMARY ─────────────────────────────────────────────────────┐    │
│  │  L1 (Technical): ✓ Pass   Loudness -23 LUFS │ Color ΔE<2 │ Res ✓  │    │
│  │  L2 (Creative):  ✓ Pass   Pacing B+ │ Beat-sync ✓ │ Style 0.87    │    │
│  │  L3 (Compliance):⚠ 1 issue  Caption lang gap (Meta - Spanish)     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  [ Package All Ready ]  [ Fix Pending Issues ]  [ View Full QC Report ]    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.12 Settings — Router Configuration

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  ROUTER CONFIGURATION                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── MODEL ROUTING RULES ────────────────────────────────────────────┐    │
│  │                                                                    │    │
│  │  Task Type           │ Primary Model  │ Fallback    │ Max $/task   │    │
│  │  ────────────────────┼────────────────┼─────────────┼──────────── │    │
│  │  Video Generation    │ Veo 3.1 (4K)   │ Kling 3.0   │ $2.50       │    │
│  │  Video (Budget)      │ Kling 3.0      │ Runway Gen-4│ $0.80       │    │
│  │  Voice Synthesis     │ ElevenLabs v3  │ —           │ $0.15       │    │
│  │  Avatar Rendering    │ HeyGen IV      │ Synthesia   │ $1.00       │    │
│  │  Image Generation    │ DALL-E 3       │ Midjourney  │ $0.08       │    │
│  │  LLM (Creative)     │ Gemini 2.5 Pro │ GPT-4o      │ $0.05       │    │
│  │  LLM (Judge/QA)     │ GPT-4o         │ Claude 4    │ $0.03       │    │
│  │  Music Generation   │ Udio           │ Suno        │ $0.50       │    │
│  │                                                                    │    │
│  │  [+ Add Rule]  [Import Preset]  [Optimize (CostOptimizerAgent)]   │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── COST GUARDRAILS ───────────────────────────────────────────────┐     │
│  │  Global budget cap: $[___] per production                         │     │
│  │  Alert at: [80]% spend                                            │     │
│  │  Auto-downgrade quality at: [90]% spend                           │     │
│  │  Hard stop at: [100]% spend (requires human override)             │     │
│  └───────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```


### 5.13 Prompt Lab (PromptEngineerAgent + PromptOptimizerAgent Interface)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROMPT LAB                                              Production: "Luna" │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── PROMPT EDITOR ──────────────────────────────────────────────────┐    │
│  │  Agent: [DirectorAgent ▼]  Model: [Veo 3.1 ▼]  Shot: [#5 ▼]      │    │
│  │                                                                    │    │
│  │  ┌────────────────────────────────────────────────────────────┐    │    │
│  │  │ A slow dolly push through rain-slicked streets at golden   │    │    │
│  │  │ hour. Camera height: eye-level. Subject walks away from    │    │    │
│  │  │ camera, coat billowing. Style: melancholic neo-noir.       │    │    │
│  │  │ Aspect: 16:9, 1080p, 8s duration.                         │    │    │
│  │  └────────────────────────────────────────────────────────────┘    │    │
│  │                                                                    │    │
│  │  Parameters:                                                       │    │
│  │  Seed: [4412]  CFG: [7.5]  Steps: [50]  Neg: [artifacts, text]   │    │
│  │                                                                    │    │
│  │  [Generate ▶]  [Optimize (OPRO)]  [A/B Test]  [Seed Walk]        │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── OPTIMIZATION HISTORY ───────────────────────────────────────────┐    │
│  │  Iter │ CLIP-T │ Aesthetic │ Change Summary             │ Accepted │    │
│  │  ─────┼────────┼───────────┼────────────────────────────┼──────── │    │
│  │  1    │ 0.29   │ 5.8       │ Original prompt            │ No       │    │
│  │  2    │ 0.32   │ 6.2       │ Added "golden hour" time   │ No       │    │
│  │  3    │ 0.34   │ 6.5       │ Added camera motion detail │ ✓ Yes    │    │
│  │  4    │ 0.33   │ 6.4       │ Tried "steady" (regressed) │ No       │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── GENERATED OUTPUTS ──────────────────────────────────────────────┐    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │    │
│  │  │ ▶ Iter 1    │  │ ▶ Iter 2    │  │ ▶ Iter 3 ✓  │                │    │
│  │  │ CLIP: 0.29  │  │ CLIP: 0.32  │  │ CLIP: 0.34  │                │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                │    │
│  │                                                                    │    │
│  │  [Compare Side-by-Side]  [Send to Director for Approval]          │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.14 Quality & Evaluation Dashboard

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  QUALITY DASHBOARD                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── OVERALL SCORES ─────────────────────────────────────────────────┐    │
│  │                                                                    │    │
│  │  VBench:       ████████████████░░░░  0.82  (threshold: 0.75) ✓    │    │
│  │  CLIP-T avg:   █████████████████░░░  0.34  (threshold: 0.32) ✓    │    │
│  │  FVD:          ██████████████░░░░░░  142   (threshold: <180) ✓    │    │
│  │  Aesthetic:    ████████████████████  6.5/7 (threshold: 5.5) ✓     │    │
│  │  Audio STOI:   ██████████████████░░  0.88  (threshold: 0.85) ✓    │    │
│  │  Loudness:     ████████████████████  -23.1 LUFS (target: -23) ✓   │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── PER-SHOT BREAKDOWN ─────────────────────────────────────────────┐    │
│  │  Shot │ CLIP-T │ Hands │ Face-ID │ Temporal │ Style │ Status       │    │
│  │  ─────┼────────┼───────┼─────────┼──────────┼───────┼──────────── │    │
│  │  1    │ 0.35   │ ✓     │ 0.98    │ ✓        │ 0.87  │ ✓ Pass      │    │
│  │  2    │ 0.31   │ ⚠     │ 0.96    │ ✓        │ 0.85  │ ⚠ Review    │    │
│  │  3    │ 0.34   │ ✓     │ 0.97    │ ✓        │ 0.88  │ ✓ Pass      │    │
│  │  4    │ 0.36   │ ✓     │ 0.95    │ ⚠        │ 0.84  │ ⚠ Review    │    │
│  │  5    │ 0.34   │ ✓     │ 0.98    │ ✓        │ 0.86  │ ✓ Pass      │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── REGRESSION ALERTS ──────────────────────────────────────────────┐    │
│  │  ⚠ Shot 2: Hand artifact at frame 142 (score dropped 0.03)        │    │
│  │  ⚠ Shot 4: Temporal flicker at transition (score: 0.71 < 0.75)    │    │
│  │  [Auto-Fix All]  [Manual Review]  [Dismiss Non-Critical]          │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```


---

## 6. Production Start Flow

The complete user journey from idea to running production:

```text
USER JOURNEY: Brief → Launch → Monitor → Approve → Deliver

Step 1: ARRIVE AT DASHBOARD
   │
   ├── Option A: Click template card (A–J) → Brief Studio (pre-filled)
   ├── Option B: Click "+ New Production" → Brief Studio (blank)
   └── Option C: Type in global search → AI suggests template
   │
   ▼
Step 2: BRIEF STUDIO
   │
   ├── 2a. Select/confirm template (activates workflow-specific agent set)
   ├── 2b. Fill brief details (title, vision, genre, duration, aspect, tone)
   ├── 2c. Upload references (scripts, mood boards, audio refs, brand assets)
   ├── 2d. Set constraints (compliance, platforms, accessibility, budget, deadline)
   └── 2e. Review plan preview (PlannerAgent pre-decomposition estimate)
   │
   ▼
Step 3: LAUNCH
   │
   ├── Brief → PlannerAgent (decomposes into phased DAG)
   ├── PlannerAgent → OrchestratorAgent (initializes execution)
   ├── OrchestratorAgent → RouterAgent (assigns models + agents)
   ├── MemoryAgent initialized with brief + references
   └── UI transitions to Production Console (DAG Canvas view)
   │
   ▼
Step 4: PRE-PRODUCTION PHASE (automated)
   │
   ├── ScreenwriterAgent → script
   ├── StoryboardAgent → panels
   ├── ConceptArtistAgent → look dev
   ├── CastingAgent → voice/talent selection
   ├── ComposerAgent → initial themes
   ├── Creative Meta-agents assist (Ideation, NarrativeArc, Mood, Style)
   ├── Research Meta-agents feed context (Web, Archive, Trend)
   │
   ├── GateKeeperAgent checks L1 criteria
   └── Gate Approval Dialog appears → USER APPROVES → next phase
   │
   ▼
Step 5: PRODUCTION PHASE (automated with optional HiTL)
   │
   ├── DirectorAgent issues shot intents
   ├── PromptEngineerAgent crafts generation prompts
   ├── RouterAgent routes to Veo/Sora/Runway/Kling
   ├── CinematographerAgent validates composition
   ├── AIQAConsistencyAgent runs per-frame QC
   ├── Optimization agents tune (Prompt, Cost, Latency)
   │
   ├── Critique messages flow (viewable in Critique Feed)
   ├── Artifacts appear in Gallery as generated
   ├── User can intervene via Critique Feed human slot
   │
   ├── GateKeeperAgent checks L2 criteria
   └── Gate Approval Dialog → USER APPROVES → next phase
   │
   ▼
Step 6: POST-PRODUCTION PHASE (automated with optional HiTL)
   │
   ├── EditorAgent assembles cut
   ├── ColoristAgent applies grade
   ├── SoundDesignAgent + ComposerAgent lay audio
   ├── SoundMixerAgent final mix
   ├── VFXSupervisorAgent composites
   ├── AccessibilityOptimizerAgent adds captions/AD
   │
   ├── JudgeAgent scores via rubric
   ├── GateKeeperAgent checks L3 criteria
   └── Gate Approval Dialog → USER APPROVES → delivery
   │
   ▼
Step 7: DELIVERY PHASE
   │
   ├── Delivery Hub shows channel matrix
   ├── DistributorAgent packages per-outlet specs
   ├── ComplianceAgent final legal sign-off
   ├── C2PA provenance signed across all outputs
   ├── User reviews final QC, approves distribution
   └── Assets published to target channels
   │
   ▼
Step 8: POST-RELEASE (optional)
   │
   ├── AnalystAgent collects performance data
   ├── RetentionOptimizerAgent / ROASOptimizerAgent analyze
   ├── Analytics Panel shows results
   └── Learnings feed back into MemoryAgent for future productions
```

### 6.1 Workflow-Specific Variations

| Template | Notable UI Differences |
|----------|----------------------|
| A — Viral Hook | Compressed timeline (all phases in 2–5 min); TrendIntel panel prominent; retention curve preview |
| B — UGC Ad | Performance targets panel; A/B variant grid; ROAS predictions visible |
| C — Animated Explainer | Learning objectives editor in brief; assessment builder; Bloom-level tagger |
| D — Personalized Birthday | Variable template editor; merge-field preview; batch render queue |
| E — AI Short Film | Full DAG visible; all 52 craft agents active; multiple gate approvals |
| F — Corporate Training | LMS packaging panel; SCORM preview; learner simulation results |
| G — Music Video | Beat-grid timeline; audio waveform overlay; choreography reference |
| H — AI Avatar | Avatar design studio; voice clone consent flow; lip-sync validation |
| I — Documentary | Archive research panel; source-grade tracker; interview synthesis |
| J — Feature Film | Episode/act navigation; series bible; full 114-agent roster; festival strategy |


---

## 7. Composition Diagram Coverage Map

Every node and edge in the Composition Diagram maps to specific UI surfaces:

```text
COMPOSITION DIAGRAM                          UI SURFACE(S)
═══════════════════                          ═════════════

[Brief]                                      S1: Brief Wizard
    │                                        S2: Template Selector
    ▼
PlannerAgent                                 S3: DAG Canvas (node)
    │                                        S11: Timeline View (plan → schedule)
    │                                        S8: Agent Inspector (drill-down)
    ▼
OrchestratorAgent                            S3: DAG Canvas (central orchestrator node)
    │                                        S11: Timeline View (phase progression)
    │                                        S22: Notification Center (escalations)
    │                                        S12: Budget Tracker (resource allocation)
    ▼
RouterAgent                                  S3: DAG Canvas (routing node)
    │                                        S13: Router Config (model selection rules)
    │                                        S21: Optimization Panel (cost/latency routing)
    ▼
52 Craft Agents (§1–§8)                      S3: DAG Canvas (all craft nodes)
    │                                        S4: Agent Node Cards
    │                                        S8: Agent Inspector (per-agent)
    │                                        S9: Artifact Gallery (outputs)
    │                                        S10: Artifact Viewer (preview/compare)
    │                                        S14: Prompt Lab (generation prompts)
    │                                        S15: Quality Dashboard (scores)
    │
    ├── CritiqueMessages ◄──────────────►    S6: Critique Feed (full stream)
    │                                        S8: Agent Inspector → Critique Bus tab
    │
    ▼
JudgeAgent                                   S3: DAG Canvas (judge node)
    │                                        S5: Gate Approval Dialog (scores)
    │                                        S6: Critique Feed (debate outcomes)
    ▼
GateKeeperAgent                              S3: DAG Canvas (gate node, amber state)
    │                                        S5: Gate Approval Dialog (criteria checklist)
    │                                        S18: Compliance Checker (legal gates)
    ▲
    │
MemoryAgent                                  S7: Memory Panel
                                             S24: Series Bible Editor
                                             S8: Agent Inspector → recalls shown

Creative Meta-Agents                         S19: Creative Meta Panel
  IdeationAgent                                   Brainstorm cards
  NarrativeArcAgent                               Beat-sheet visualizer
  StyleTransferAgent                              Style-lock controls
  MoodBoardAgent                                  Mood board composer
  NoveltyAgent                                    Cliché warnings
  EmotionalArcAgent                               Emotion curve graph

Research Meta-Agents                         S20: Research Panel
  WebResearchAgent                                Live search results
  ArchiveResearchAgent                            Source cards
  TrendIntelligenceAgent                          Trend timeline
  CompetitorIntelligenceAgent                     Competitor grid
  CitationAgent                                   Source-grade badges
  InterviewSynthesisAgent                         Theme clusters
  BenchmarkResearchAgent                          Leaderboard diffs

Optimization Meta-Agents                     S21: Optimization Panel
  PromptOptimizerAgent                            S14: Prompt Lab (OPRO controls)
  CostOptimizerAgent                              S12: Budget Tracker + S13: Router Config
  LatencyOptimizerAgent                           Pipeline timing view
  RetentionOptimizerAgent                         Retention curve predictor
  ROASOptimizerAgent                              ROAS projection chart
  AccessibilityOptimizerAgent                     A11y compliance checklist
  EvaluationHarnessAgent                          S15: Quality Dashboard (benchmark runner)
  SafetyRedTeamAgent                              S18: Compliance → Red Team tab
```


---

## 8. Responsive & Accessibility Notes

### 8.1 Breakpoints

| Breakpoint | Layout Adaptation |
|-----------|-------------------|
| ≥1440px (Desktop XL) | Full shell: side nav + canvas + drawer all visible simultaneously |
| 1024–1439px (Desktop) | Side nav collapses to icon-only; drawer overlays canvas |
| 768–1023px (Tablet) | Single-pane view; tabs switch between canvas/gallery/critique; drawer full-screen |
| <768px (Mobile) | Dashboard + brief studio functional; Production Console read-only (monitoring) |

### 8.2 Accessibility Requirements (WCAG 2.2 AA)

| Requirement | Implementation |
|-------------|---------------|
| Color contrast | All text ≥4.5:1; Large text ≥3:1; status indicators use shape+color |
| Keyboard navigation | Full keyboard access; focus rings; Cmd+K command palette |
| Screen reader | ARIA landmarks, live regions for status updates, agent-state announcements |
| Motion sensitivity | Reduced motion mode: DAG animations → static transitions |
| Color-blind safe | Node states use shape (✓●○⚠✗) + color; never color-only |

### 8.3 Dark/Light Mode

Both themes supported. DAG canvas uses a muted background in both modes to ensure node visibility.

---

## 9. Component Library Summary

### 9.1 Core Components

| Component | Usage | Variants |
|-----------|-------|----------|
| `AgentNodeCard` | DAG canvas nodes | mini (DAG), expanded (inspector), list-row (registry) |
| `ArtifactCard` | Gallery items | thumbnail, detail, compare |
| `CritiqueMessage` | Feed items | info, warning, critical, resolved |
| `GateCheckpoint` | DAG + timeline | pending, reviewing, approved, rejected |
| `MetricBar` | Quality dashboard | pass (green), warning (amber), fail (red) |
| `TimelineSwim` | Phase swimlanes | pre-pro, production, post, delivery |
| `BriefField` | Brief studio inputs | text, dropdown, slider, tag-input, file-drop, toggle |
| `DrawerPanel` | Detail views | bottom-slide, side-slide, full-screen |
| `CommandPalette` | Global search/action | Cmd+K triggered |
| `NotificationBadge` | Top bar + nav | count badge, priority indicator |
| `ProvBadge` | C2PA provenance | verified, pending, unsigned |
| `BudgetGauge` | Cost tracking | linear progress with threshold markers |

### 9.2 Composite Patterns

| Pattern | Composed From | Used In |
|---------|--------------|---------|
| Agent Inspector | NodeCard + MetricBars + CritiqueMessages + ArtifactCards | Drawer / Full-screen |
| Gate Dialog | GateCheckpoint + checklist + ArtifactCards + action buttons | Modal overlay |
| Prompt Editor | Code editor + parameter sliders + output gallery + optimization history | Prompt Lab |
| Channel Row | Status badges + QC indicators + action buttons | Delivery Hub |
| Timeline Phase | TimelineSwim + milestone markers + budget overlay + gate markers | Timeline View |

---

## 10. Interaction Patterns

### 10.1 Command Palette (Cmd+K)

Global search + action launcher accessible from anywhere:

```text
┌───────────────────────────────────────────────┐
│  🔍 Search agents, artifacts, actions...       │
├───────────────────────────────────────────────┤
│  RECENT                                       │
│  → DirectorAgent Inspector                    │
│  → Shot Intent #5 artifact                    │
│  → Gate #2 approval                           │
│                                               │
│  ACTIONS                                      │
│  → New Production                             │
│  → Retry failed agents                        │
│  → Export all artifacts                        │
│  → Open Router Config                         │
│                                               │
│  AGENTS (filtered as you type)                │
│  → DirectorAgent (● running)                  │
│  → EditorAgent (○ idle)                       │
│  → AIQAConsistencyAgent (● running)           │
└───────────────────────────────────────────────┘
```

### 10.2 Human-in-the-Loop Patterns

| Trigger | UI Response | User Action |
|---------|-------------|-------------|
| Gate checkpoint reached | Gate Approval Dialog appears + notification | Approve / Reject / Request Changes |
| Agent requests human input | Critique Feed highlights + notification badge | Respond in critique feed |
| Budget threshold hit | Banner alert + cost dialog | Override / Downgrade / Stop |
| Compliance block | Modal with legal details | Resolve / Escalate |
| Quality regression | Quality Dashboard alert + affected shots highlighted | Auto-fix / Manual review |

### 10.3 Real-Time Updates

| Data | Update Frequency | UI Behavior |
|------|-----------------|-------------|
| Agent states | 1–5s | Node color/symbol transitions smoothly |
| Critique messages | Event-driven (websocket) | New messages slide in, badge increments |
| Artifacts | On completion | Card appears in gallery with animation |
| Budget burn | Per-task completion | Gauge animates, status bar updates |
| Quality scores | Per-evaluation | MetricBar transitions, alerts if regression |
| Gate status | On criteria met | GateCheckpoint pulses amber, notification fires |

### 10.4 Bulk Operations

| Operation | Available In | Scope |
|-----------|-------------|-------|
| Retry all failed | DAG Canvas context menu | All failed agents |
| Approve all pending | Gate panel | All gates meeting threshold |
| Export artifacts | Gallery toolbar | Selected or all |
| Compare versions | Artifact viewer | Any 2 versions side-by-side |
| Clear stale memory | Memory panel | Entries older than N days |


---

## 11. Notification & Alert System

### 11.1 Priority Levels

| Priority | Trigger | Notification Style | Requires Action |
|----------|---------|-------------------|-----------------|
| Critical | Compliance block, budget overrun, legal expiry | Full-screen modal + audio chime | Yes (cannot dismiss) |
| High | Gate ready for approval, quality failure | Toast + badge + status bar flash | Yes (within 5min) |
| Medium | Agent completed task, new critique received | Badge increment + feed highlight | No (informational) |
| Low | Optimization suggestion, memory entry added | Badge only | No |

### 11.2 Notification Center

```text
┌────────────────────────────────────────────┐
│  NOTIFICATIONS (3 unread)                  │
├────────────────────────────────────────────┤
│  🔴 Compliance: Voice consent expiring     │
│     2 min ago · [Resolve]                  │
│                                            │
│  🟡 Gate #3 ready for review               │
│     5 min ago · [Open Gate]                │
│                                            │
│  🟡 AIQAAgent: Hand artifact in Shot 2     │
│     8 min ago · [View Shot]                │
│                                            │
│  ── Read ─────────────────────────────     │
│  🔵 EditorAgent completed rough cut        │
│  🔵 PromptOptimizer improved CLIP-T +0.02  │
│  🔵 BudgetAgent: 42% spent                 │
└────────────────────────────────────────────┘
```

---

## 12. Data Model (UI State)

The UI maintains the following state objects (synced via WebSocket from backend):

```typescript
interface Production {
  id: string;
  title: string;
  template: 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J';
  phase: 'brief'|'pre_production'|'production'|'post_production'|'delivery'|'released';
  brief: Brief;
  dag: DAGState;
  budget: BudgetState;
  gates: GateState[];
  artifacts: Artifact[];
  critiques: CritiqueMessage[];
  memory: MemoryEntry[];
  delivery: DeliveryState;
  analytics?: AnalyticsState;
}

interface DAGState {
  nodes: AgentNode[];        // All active agents with state
  edges: ArtifactEdge[];     // Handoff connections
  activePhase: string;
  completionPercent: number;
}

interface AgentNode {
  agentId: number;           // 1–114
  name: string;
  category: string;
  state: 'idle'|'running'|'blocked'|'complete'|'failed';
  currentTask?: Task;
  metrics: MetricScore[];
  critiquesReceived: CritiqueRef[];
  critiquesSent: CritiqueRef[];
  toolCalls: ToolCall[];
  artifacts: ArtifactRef[];
}

interface GateState {
  gateId: string;
  phase: string;
  criteria: GateCriterion[];
  judgeScore: number;
  status: 'pending'|'reviewing'|'approved'|'rejected';
  approvedBy?: string;
  c2paSigned: boolean;
}

interface Artifact {
  id: string;
  version: number;
  type: 'video'|'audio'|'image'|'text'|'data'|'package';
  producedBy: number;       // Agent ID
  qualityScores: Record<string, number>;
  c2paStatus: 'signed'|'pending'|'unsigned';
  parentAssets: string[];
  thumbnailUrl?: string;
}

interface CritiqueMessage {
  id: string;
  timestamp: string;
  fromAgent: number;
  toAgent: number | 'ALL';
  severity: 'info'|'warning'|'critical';
  content: string;
  attachments: ArtifactRef[];
  status: 'open'|'accepted'|'rejected'|'resolved';
  humanResponse?: string;
}
```

---

## 13. Technology Stack Recommendations

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Framework | React 19 + Next.js 15 | SSR for dashboard, client-side for real-time console |
| State Management | Zustand + React Query | Lightweight; WebSocket sync for real-time DAG state |
| DAG Rendering | React Flow (xyflow) | Purpose-built for node graphs; supports custom nodes |
| Timeline | Custom SVG + D3.js | Swimlane visualization with budget overlay |
| Video Preview | Shaka Player / Video.js | Supports multiple codecs, adaptive streaming |
| Audio Waveform | WaveSurfer.js | Lightweight waveform visualization |
| Real-time | WebSocket (Socket.io) | Agent state updates, critique bus, notifications |
| Styling | Tailwind CSS + Radix UI | Accessible primitives + utility-first styling |
| Charts | Recharts / Nivo | Quality metrics, budget burn, analytics |
| Command Palette | cmdk | Proven Cmd+K implementation |
| Icons | Lucide React | Clean, consistent icon set |
| Code Editor | Monaco (prompt lab) | Syntax highlighting for prompts, JSON preview |

---

## 14. Wireframe Reference

See companion SVG files:
- [`master-shell.svg`](./master-shell.svg) — Full application shell wireframe
- [`surface-map.svg`](./surface-map.svg) — Coverage map: Composition Diagram → UI surfaces

---

*End of UI Design Document*
