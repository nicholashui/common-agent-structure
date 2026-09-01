# Project Creation & Management Flow

> Defines the Project layer that sits ABOVE productions — allowing users to plan, iterate, and collaborate before any agents run or money is spent.

---

## Core Concept: Project vs. Production

```text
PROJECT = Container (free, persistent, collaborative)
PRODUCTION = Execution (costs money, runs agents, produces artifacts)

┌─────────────────────────────────────────────────────────────────┐
│  PROJECT "Brand Campaign Q3"                                     │
│  (free to create, free to hold, free to plan)                    │
│                                                                 │
│  ├── Shared Assets: brand kit, voices, style refs               │
│  ├── Team: owner + editors + reviewers                          │
│  ├── Budget Pool: $240 allocated                                │
│  ├── Default Settings: compliance, models, platforms            │
│  │                                                              │
│  ├── Production 1: "Hero Video" (Type E, completed ✓, $62)     │
│  ├── Production 2: "TikTok Cut" (Type A, running ●, $28)       │
│  └── Production 3: "Training" (Type F, DRAFT ○, $0)            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

KEY RULE: No money is spent until user explicitly clicks [▶ Launch].
          Everything before that is FREE preparation.
```

---

## User Journey: From Zero to Running Production

```text
Step 1: CREATE PROJECT ──────────────────── $0 (instant, free)
Step 2: PREPARE (assets, team, settings) ── $0 (take days/weeks)
Step 3: CREATE PRODUCTION DRAFT ─────────── $0 (brief saved, editable)
Step 4: GET COST ESTIMATE ───────────────── $0 (PlannerAgent preview)
Step 5: LAUNCH PRODUCTION ───────────────── $$$ (agents start HERE)
Step 6: MONITOR + APPROVE ───────────────── (production running)
Step 7: DELIVER ─────────────────────────── (complete)
Step 8: CREATE NEXT PRODUCTION ──────────── repeat from Step 3
```

---

## Page 1: Dashboard (Updated with Projects)

```text
┌─────────────────────────────────────────────────────────────────────┐
│  DASHBOARD                                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─── MY PROJECTS ─────────────────────────────────────────────┐    │
│  │                                                             │    │
│  │  [+ New Project]                                            │    │
│  │                                                             │    │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌───────────┐ │    │
│  │  │ Brand Q3         │  │ Luna Short Film  │  │ + New     │ │    │
│  │  │ 3 productions    │  │ 1 production     │  │ Project   │ │    │
│  │  │ 2 running · $90  │  │ completed · $95  │  │           │ │    │
│  │  │ Updated: 2m ago  │  │ Updated: 3d ago  │  │           │ │    │
│  │  └──────────────────┘  └──────────────────┘  └───────────┘ │    │
│  │                                                             │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── ACTIVE PRODUCTIONS (across all projects) ────────────────┐    │
│  │  ┌─────────────┐  ┌─────────────┐                          │    │
│  │  │ Hero Video  │  │ TikTok Cut  │                          │    │
│  │  │ Brand Q3    │  │ Brand Q3    │                          │    │
│  │  │ ████████░░  │  │ ██████░░░░  │                          │    │
│  │  └─────────────┘  └─────────────┘                          │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── QUICK START (skip project setup) ────────────────────────┐    │
│  │  "Just make something fast?" → Pick template, auto-project  │    │
│  │  [A Hook] [B UGC] [C Explainer] [D Birthday] [E Film] ...  │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Page 2: Create Project Dialog

```text
┌──────────────────────────────────────────────────────────────────┐
│  CREATE NEW PROJECT                                    [×]        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Project Name: [________________________________]                │
│                                                                  │
│  Description (optional):                                         │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ e.g., "Q3 brand awareness campaign across social + web"  │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── BUDGET POOL ──────────────────────────────────────────┐    │
│  │  Total budget for all productions: $[_____]               │    │
│  │  ☐ No limit (pay as you go)                               │    │
│  │  Billing method: [Credit card ending 4242 ▼]              │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── TEAM (optional — add later) ──────────────────────────┐    │
│  │  You: Owner                                               │    │
│  │  [+ Invite]  ______@email.com  Role: [Editor ▼]           │    │
│  │                                                           │    │
│  │  Roles:                                                   │    │
│  │  • Owner — full control, billing, delete                  │    │
│  │  • Editor — create/launch productions, manage assets      │    │
│  │  • Reviewer — view, comment, approve gates                │    │
│  │  • Viewer — read-only access                              │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── DEFAULTS (apply to all productions unless overridden) ─┐    │
│  │  Compliance: ☑ C2PA  ☑ WCAG AA  ☐ SAG-AFTRA  ☐ GDPR     │    │
│  │  Model preference: [Cost-optimized ▼]                      │    │
│  │    Options: Cost-optimized │ Quality-first │ Speed-first   │    │
│  │  Brand kit: [Upload now ▼] or [Add later]                 │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│              [ Cancel ]           [ Create Project ]              │
│                                                                  │
│  ℹ️ Creating a project is free. You're only charged when you      │
│    launch a production.                                          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Page 3: Project Workspace

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROJECT: "Brand Campaign Q3"                    [Archive] [Settings ⚙]     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Overview] [Productions] [Assets] [Team] [Settings] [Activity]       │
│                                                                             │
├─── OVERVIEW TAB ────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── STATUS CARDS ────────────────────────────────────────────────────┐    │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐   │    │
│  │  │Productions │  │  Budget    │  │   Team     │  │  Assets    │   │    │
│  │  │     3      │  │ $90/$240   │  │  3 members │  │  12 files  │   │    │
│  │  │ 1✓ 1● 1○  │  │ 38% used   │  │            │  │            │   │    │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── PRODUCTIONS ─────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  [+ New Production]     Sort: [Recent ▼]    Filter: [All ▼]         │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ✓ "Hero Video"        │ Type E │ Completed 2 days ago      │    │    │
│  │  │   Cost: $62 │ Duration: 5:20 │ Delivered: YouTube, TikTok  │    │    │
│  │  │   [View Artifacts]  [View Analytics]  [Duplicate as Draft]  │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ● "TikTok Cut"        │ Type A │ Running — Production phase│    │    │
│  │  │   Cost: $28 │ Progress: 55% │ ETA: 2 min                   │    │    │
│  │  │   [Open Console]  [Pause]                                   │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ○ "Training Module"   │ Type F │ DRAFT — not launched       │    │    │
│  │  │   Cost: $0 │ Brief: 80% complete │ Est. cost: ~$35          │    │    │
│  │  │   [Edit Brief]  [Get Estimate]  [▶ Launch]  [Delete]        │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── RECENT ACTIVITY ─────────────────────────────────────────────────┐    │
│  │  • 2m ago: "TikTok Cut" — EditorAgent completed rough cut          │    │
│  │  • 5m ago: "TikTok Cut" — Gate #1 approved by you                  │    │
│  │  • 2d ago: "Hero Video" — Delivered to YouTube + TikTok            │    │
│  │  • 3d ago: Sarah joined as Reviewer                                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Page 4: Assets Tab (Shared Library)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROJECT: "Brand Campaign Q3" > ASSETS                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [+ Upload Assets]   [Connect Brand Kit]                                    │
│                                                                             │
│  ┌─── BRAND KIT ──────────────────────────────────────────────────────┐    │
│  │  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐                              │    │
│  │  │logo│ │font│ │color│ │guide│ │tone│                              │    │
│  │  │.svg│ │.otf│ │.json│ │.pdf│ │.md │                              │    │
│  │  └────┘ └────┘ └────┘ └────┘ └────┘                              │    │
│  │  Auto-loaded into every production's BrandAgent                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── VOICE LIBRARY ─────────────────────────────────────────────────┐     │
│  │  🎤 "Brand Voice A" — energetic, young, ElevenLabs clone          │     │
│  │  🎤 "Brand Voice B" — authoritative, mature, custom trained       │     │
│  │  🎤 "Narrator" — neutral, clear, standard TTS                     │     │
│  │  [+ Add Voice]                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── STYLE REFERENCES ──────────────────────────────────────────────┐     │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │     │
│  │  │ ref_mood1.jpg│ │ ref_style.mp4│ │ ref_comp.png│                 │     │
│  │  │ "Neo-noir"  │ │ "Pacing ref"│ │ "Framing"   │                 │     │
│  │  └─────────────┘ └─────────────┘ └─────────────┘                 │     │
│  │  [+ Add Reference]                                                │     │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── SCRIPTS & DOCUMENTS ───────────────────────────────────────────┐     │
│  │  📄 brand_messaging_guide.md                                       │     │
│  │  📄 target_audience_research.pdf                                   │     │
│  │  📄 competitor_analysis.xlsx                                       │     │
│  │  [+ Upload Document]                                              │     │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ℹ️ All assets here are automatically available to every production         │
│    in this project. Agents reference them without re-uploading.             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Page 5: Production Draft (Edit Before Launch)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODUCTION DRAFT: "Training Module"              Status: DRAFT (not launched)│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── BRIEF EDITOR ──────────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  Template: [F] Corporate Training    [Change]                      │     │
│  │                                                                    │     │
│  │  Title: [Training Module: Product Onboarding___]                   │     │
│  │                                                                    │     │
│  │  Vision:                                                           │     │
│  │  ┌──────────────────────────────────────────────────────────────┐  │     │
│  │  │ A 10-minute interactive training video that teaches new      │  │     │
│  │  │ employees how to use our product dashboard. Should feel      │  │     │
│  │  │ modern, friendly, and include knowledge checks.              │  │     │
│  │  └──────────────────────────────────────────────────────────────┘  │     │
│  │                                                                    │     │
│  │  Duration: [10 min]  Format: [16:9]  Tone: [friendly, professional]│     │
│  │  Learning objectives: [Tag: navigate dashboard, create report, ...]│     │
│  │  Assessment type: [Quiz after each section ▼]                      │     │
│  │  Delivery: ☑ SCORM  ☑ xAPI  ☐ Standalone video                    │     │
│  │                                                                    │     │
│  │  References from project: ☑ Brand Kit ☑ Voice "Brand Voice A"     │     │
│  │  Additional: [product_screenshots.zip] uploaded                    │     │
│  │                                                                    │     │
│  │  Budget for this production: $[35___]                              │     │
│  │  (Project pool remaining: $150 of $240)                            │     │
│  │                                                                    │     │
│  │  Last saved: 2 minutes ago (auto-save)                             │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── COST ESTIMATE PREVIEW ─────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  [🔄 Refresh Estimate]    Last estimated: 10 min ago               │     │
│  │                                                                    │     │
│  │  Estimated breakdown:                                              │     │
│  │  • Script + Instructional Design: ~$3                              │     │
│  │  • Avatar rendering (10 min): ~$12                                 │     │
│  │  • Voice synthesis: ~$4                                            │     │
│  │  • Motion graphics: ~$6                                            │     │
│  │  • Assessment generation: ~$2                                      │     │
│  │  • QC + Compliance: ~$3                                            │     │
│  │  • LMS packaging: ~$1                                              │     │
│  │  ─────────────────────────────                                     │     │
│  │  TOTAL ESTIMATE: ~$31 (±15%)                                       │     │
│  │                                                                    │     │
│  │  Agents needed: 18 │ Estimated duration: ~8 min                    │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── TEAM COMMENTS ON THIS DRAFT ───────────────────────────────────┐     │
│  │  Sarah (Reviewer): "Can we add a section on report exports?"      │     │
│  │  You: "Good idea, added to learning objectives"                    │     │
│  │  [+ Add comment]                                                   │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── ACTIONS ───────────────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  [ Save Draft ]    [ Share for Review ]    [ ▶ Launch Production ] │     │
│  │                                                                    │     │
│  │  ▶ Launch will:                                                    │     │
│  │    • Charge up to $35 from project budget pool                     │     │
│  │    • Activate 18 agents (Instructional, Avatar, Voice, LMS, ...)   │     │
│  │    • Begin production — you'll monitor in Production Console       │     │
│  │    • Estimated completion: ~8 minutes                              │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Launch Confirmation Dialog

```text
┌──────────────────────────────────────────────────────────┐
│  LAUNCH PRODUCTION                                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Production: "Training Module"                            │
│  Template: F (Corporate Training)                         │
│  Project: "Brand Campaign Q3"                             │
│                                                          │
│  ┌─── COST SUMMARY ──────────────────────────────────┐   │
│  │  Estimated cost: ~$31 (budget cap: $35)            │   │
│  │  Project budget remaining: $150                     │   │
│  │  After this launch: ~$119 remaining                │   │
│  └────────────────────────────────────────────────────┘   │
│                                                          │
│  ┌─── WHAT WILL HAPPEN ──────────────────────────────┐   │
│  │  1. PlannerAgent decomposes your brief             │   │
│  │  2. 18 agents activate (InstructionalDesign,       │   │
│  │     Avatar, Voice, MotionGraphics, LMS, ...)       │   │
│  │  3. You'll see progress on the Production Console  │   │
│  │  4. Gate approvals will pause for your review      │   │
│  │  5. Estimated completion: ~8 minutes               │   │
│  └────────────────────────────────────────────────────┘   │
│                                                          │
│  ☑ I understand this will charge my project budget        │
│                                                          │
│         [ Cancel ]          [ ▶ Launch Now ]              │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## Updated Information Architecture

```text
ROOT
├── Dashboard
│   ├── My Projects (grid)
│   ├── Active Productions (across all projects)
│   └── Quick Start (template picker → auto-project)
│
├── Project Workspace (per-project)          ← NEW
│   ├── Overview (status cards, productions list, activity)
│   ├── Productions (list with status: draft/running/complete)
│   ├── Assets (shared brand kit, voices, refs, docs)
│   ├── Team (members, roles, invitations)
│   ├── Settings (budget, defaults, compliance, models)
│   └── Activity (log of all project events)
│
├── Production Draft (per-production, pre-launch)  ← NEW
│   ├── Brief Editor (full editable form)
│   ├── Cost Estimate Preview
│   ├── Team Comments
│   └── Launch Button
│
├── Production Console (per-production, post-launch)  ← EXISTING
│   ├── DAG Canvas
│   ├── Timeline View
│   ├── Artifact Gallery
│   ├── Critique Feed
│   ├── Gate Control
│   └── Agent Inspector
│
├── Agent Registry                           ← EXISTING
├── Memory & Knowledge                       ← EXISTING
├── Delivery Hub                             ← EXISTING
├── Settings & Admin                         ← EXISTING
└── Help & Docs                              ← EXISTING
```

---

## API: Project Layer (Backend)

```text
NO AGENTS INVOLVED — pure CRUD operations:

POST   /api/projects                              Create project
GET    /api/projects                              List projects
GET    /api/projects/{id}                         Get project
PUT    /api/projects/{id}                         Update project
DELETE /api/projects/{id}                         Archive project

POST   /api/projects/{id}/assets                  Upload shared asset
GET    /api/projects/{id}/assets                  List assets
DELETE /api/projects/{id}/assets/{aid}             Remove asset

POST   /api/projects/{id}/members                 Invite member
PUT    /api/projects/{id}/members/{uid}           Change role
DELETE /api/projects/{id}/members/{uid}           Remove member

POST   /api/projects/{id}/productions             Create draft ($0)
GET    /api/projects/{id}/productions             List productions
PUT    /api/projects/{id}/productions/{pid}/brief Edit brief (draft only)
POST   /api/projects/{id}/productions/{pid}/estimate  Preview cost
POST   /api/projects/{id}/productions/{pid}/launch    ← AGENTS START HERE
POST   /api/projects/{id}/productions/{pid}/pause     Pause running
POST   /api/projects/{id}/productions/{pid}/resume    Resume paused
POST   /api/projects/{id}/productions/{pid}/duplicate Clone as new draft
DELETE /api/projects/{id}/productions/{pid}            Delete draft
```

---

## Data Model

```typescript
interface Project {
  id: string;
  name: string;
  description?: string;
  owner_id: string;
  status: "active" | "archived";
  
  // Budget
  budget_pool: number | null;      // null = no limit
  budget_spent: number;            // sum of all production spending
  billing_method_id: string;
  
  // Team
  members: {
    user_id: string;
    role: "owner" | "editor" | "reviewer" | "viewer";
    joined_at: Date;
  }[];
  
  // Shared resources
  shared_assets: {
    id: string;
    type: "brand_kit" | "voice" | "style_ref" | "document" | "script";
    name: string;
    url: string;
    metadata: object;
  }[];
  
  // Defaults
  default_settings: {
    compliance: string[];
    model_strategy: "cost_optimized" | "quality_first" | "speed_first";
    platform_targets: string[];
  };
  
  // Metadata
  created_at: Date;
  updated_at: Date;
}

interface Production {
  id: string;
  project_id: string;
  title: string;
  template: 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J';
  
  // Lifecycle
  status: "draft" | "launching" | "running" | "paused" | "completed" | "failed";
  
  // Brief (editable while draft)
  brief: {
    vision: string;
    genre?: string;
    duration: number;
    aspect_ratio: string;
    tone: string[];
    target_audience: string;
    references: string[];          // asset IDs (shared + production-specific)
    constraints: object;
    platform_targets: string[];
    template_specific: object;     // learning objectives, beat count, etc.
  };
  
  // Budget
  budget_cap: number;
  budget_spent: number;
  
  // Estimate (from PlannerAgent preview)
  estimate?: {
    cost_low: number;
    cost_mid: number;
    cost_high: number;
    agents_needed: number;
    estimated_duration_seconds: number;
    breakdown: { category: string; cost: number }[];
    generated_at: Date;
  };
  
  // Team comments on draft
  comments: {
    user_id: string;
    content: string;
    created_at: Date;
  }[];
  
  // Only populated after launch
  dag?: DAGState;
  artifacts?: Artifact[];
  launched_at?: Date;
  completed_at?: Date;
  
  created_at: Date;
  updated_at: Date;
}
```

---

## Quick Start Path (For Impatient Users)

Users who don't want to set up a project first can still go fast:

```text
Dashboard → Click template [A Viral Hook] →

System auto-creates:
  • Project: "Untitled Project" (can rename later)
  • Production: "Viral Hook" (pre-filled brief)
  • Lands on Brief Editor in draft mode
  
User fills minimal info → clicks [▶ Launch] → agents start

The "project" still exists — they can add more productions later,
rename it, invite team. But the initial friction is near-zero.
```

---

## Summary: What Changed

| Before (original design) | After (with Project layer) |
|--------------------------|---------------------------|
| Dashboard → Brief Studio → Launch (immediate) | Dashboard → Project → Draft → Edit → Launch (when ready) |
| Every production is standalone | Productions live inside Projects |
| Assets uploaded per-production | Shared asset library per project |
| No team collaboration before launch | Team reviews drafts, leaves comments |
| No cost visibility before committing | Free cost estimate on any draft |
| Can't iterate on brief without spending | Draft mode = unlimited free edits |
| No way to group related videos | Project groups campaign variants |
| Budget per-production only | Budget pool across project + per-production caps |
