# VA-Agent-Swarm — System Build Plan

**Document Version:** 1.0 (Ultra-Detailed, Implementation-Ready)
**Date:** May 29, 2026
**Target Build Agent:** **Claude Code** (Anthropic CLI coding agent)
**Authors:** Synthesized for Nicholas (nicholas_hui) from the complete `study/` specification corpus
**Purpose:** This is the **single, authoritative, step-by-step plan** for an AI coding agent (Claude Code) to build the entire **VA-Agent-Swarm** — a 114-agent, hierarchical multi-agent video-production system — from an empty repository to a hardened, observable, production-grade platform.

> **Scope contract:** This document does *not* re-derive the system design. It assumes the design is already specified across `study/` (see [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md), [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md), [`agents.md`](./agents.md), and the per-agent functional/technical specs). This plan tells Claude Code **what to build, in what order, with what acceptance gates, and how to use its own tooling to do it reliably.**

---

## 0. How To Use This Document (Read First — This Section Is For Claude Code)

### 0.1 Your operating loop for the whole build

You (Claude Code) will execute this plan as a sequence of **Milestones (M0–M12)**. For *every* milestone and *every* task inside it:

1. **Enter Plan Mode first** (`Shift+Tab` → plan mode). Read the referenced spec(s), restate the goal, list files you will create/modify, and surface unknowns. **Do not edit code in plan mode.**
2. **Confirm the plan** against the milestone's *Acceptance Gate* and *Definition of Done (DoD)*. If anything is ambiguous, ask one consolidated question rather than guessing.
3. **Write the test first** (TDD). Every unit of behavior gets a failing test before implementation. See §9.
4. **Implement** the smallest increment that makes the test pass.
5. **Run the local gate**: `make verify` (lint + type + unit). Never advance with a red gate.
6. **Self-review** using the `code-reviewer` subagent (§2.3) and the milestone's checklist.
7. **Commit** with a Conventional Commit message (§11.3) referencing the milestone (e.g., `feat(m2-orchestrator): ...`).
8. **Update progress**: tick the milestone checklist item in `BUILD_PROGRESS.md` (you maintain this file — see §0.4).
9. **`/clear` context** between unrelated tasks to keep the window clean. Use `/compact` only mid-task.

### 0.2 The "rethink 100 times" mandate, operationalized

The user asked for a plan rethought "100 times with full effort." That intensity is encoded structurally, not as a slogan:

- **§14** is a literal **100-point hardening checklist** (10 themes × 10 checks). The system is not "done" until all 100 pass.
- The reference workflow already defines a **100-pass reassessment discipline** ([`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §1.4). This build plan inherits it: every milestone's acceptance is re-challenged across the five bands (traceability → architecture → handoffs → metrics → wording).
- Every agent you build must clear the system's own **L1/L2/L3 quality framework** and the **Q1–Q6 delivery QC mesh** (§5.5). Quality is recursive: the system that judges videos must itself be judged.

### 0.3 Golden rules (violating these is a defect, even if tests pass)

| # | Rule | Why |
|---|------|-----|
| G1 | **Contracts before code.** The shared Pydantic contracts (§5) are built and frozen *before* any agent. Every agent imports them; none redefines them. | Prevents 114 divergent message formats. |
| G2 | **Vertical slice before breadth.** One workflow (Viral Hook, archetype A) runs end-to-end through real infra before the other 108 agents are built. | Validates the architecture cheaply before scale. |
| G3 | **Every agent is an instance of one base class.** No bespoke agent loops. New agents are *configuration + rubric + tools*, produced by the Agent Factory (§8). | 114 agents must share one lifecycle. |
| G4 | **No agent talks to the UI directly.** Agents publish to the Event Bus; the WebSocket Gateway fans out. | Per [`ui/architecture_communication.md`](./ui/architecture_communication.md). |
| G5 | **Determinism where possible.** Pin seeds, model versions, and prompt versions. Record them in provenance. | Reproducibility + audit. |
| G6 | **Cost & safety are gates, not afterthoughts.** The LLM gateway meters every token from M3; ComplianceAgent can BLOCK from the moment it exists. | Per spec; runaway cost/safety kills the project. |
| G7 | **Mock external gen-models behind an interface from day one.** Real Sora/Veo/Kling calls are expensive and rate-limited; the `MediaGenProvider` interface lets you run the whole DAG on cheap stubs in CI. | Testability + cost control. |

### 0.4 Artifacts you maintain throughout the build

- `BUILD_PROGRESS.md` — living checklist mirroring §6 milestones and §14 hardening; you tick items as you complete them.
- `DECISIONS.md` — an ADR (Architecture Decision Record) log; every non-obvious choice gets a dated entry.
- `CLAUDE.md` (root + per-package) — your persistent project memory (template in Appendix A).
- `.claude/` — your subagents, slash commands, settings, and hooks (Appendices B–D).

---

## 1. Mission & Build Philosophy

### 1.1 What is being built (one paragraph)

A hierarchical **multi-agent system (MAS)** that automates/augments professional video production from a client brief to multi-channel delivery. **114 specialized agents** (10 categories) run as nodes in a **LangGraph DAG**, made durable by **Temporal**, communicating creative artifacts via a **Shared Artifact Handoff Contract** and critique via a **CritiqueMessage bus**, gated by a **L1/L2/L3 + Q1–Q6 quality mesh**, observed via **LangSmith/Grafana**, surfaced to humans through a **Next.js 15 console** over REST + WebSocket. Cross-cutting services (Agentic RAG, Research, GCA, Optimization, DIA, Aesthetics, LLM-cost dashboard) provide reasoning, knowledge, creativity, and taste to every agent.

### 1.2 Build philosophy

1. **Walking skeleton first.** Get the thinnest possible end-to-end path alive (brief → 1 agent → artifact → UI event) before adding muscle.
2. **Platform, then agents.** ~70% of the hard engineering is the *platform* (orchestration, contracts, QC, observability, gateway). Agents are mostly declarative once the platform is right.
3. **Factory over hand-craft.** After the platform and 5 reference agents, the remaining ~109 agents are generated from spec via the Agent Factory and reviewed, not hand-coded loop-by-loop.
4. **Dogfood the Coding Agent spec.** The intended self-building "N1ch01as Architect" coding agent ([`coding_agent_functional_specification.md`](./coding_agent_functional_specification.md)) *is the role Claude Code plays* during this build. Where that spec defines conventions, follow them.
5. **Quality is recursive and measurable.** Use the system's own evaluation philosophy on the system itself: spec-conformance (L1), rubric (L2), preference/behavioral (L3).

---

## 2. Target Build Agent: Claude Code Operating Model

This section configures Claude Code so it builds the system reliably, with high context hygiene and minimal rework. **Set this up in M0 before writing product code.**

### 2.1 `CLAUDE.md` strategy (project memory)

Claude Code auto-loads `CLAUDE.md` from the repo root (and nested package dirs) into context. Use it as the always-on "constitution."

- **Root `CLAUDE.md`** (template in Appendix A): tech stack + pinned versions, monorepo map, the 7 Golden Rules (§0.3), build/test/lint commands, code-style rules, contract location, and "where to find the spec for X."
- **Per-package `CLAUDE.md`**: each `packages/*` and `services/*` gets a short `CLAUDE.md` describing its responsibility, public API, and local test command. Nested files load when you work in that subtree, keeping context tight.
- **Keep it lean.** `CLAUDE.md` competes with task context. Link to specs rather than pasting them. Run `/memory` to review; prune aggressively.
- Bootstrap with `/init`, then hand-edit to match Appendix A.

### 2.2 Mode discipline

| Mode | When | Trigger |
|------|------|---------|
| **Plan mode** | Start of every milestone/task; any change touching >2 files or a contract | `Shift+Tab` to plan mode |
| **Normal (ask-per-edit)** | Default implementation | — |
| **Auto-accept edits** | Only inside a tight TDD loop on a single file with a green safety net | `Shift+Tab` |
| **Extended thinking** | Architecture, contract design, debugging concurrency, the §14 hardening pass | Say "think hard" / "ultrathink" in the prompt |

### 2.3 Subagents to create (`.claude/agents/`)

Subagents have isolated context windows and scoped tools — ideal for keeping the main thread clean. Create these in M0 (full definitions in Appendix B):

| Subagent | Job | Tools (scoped) |
|----------|-----|----------------|
| `spec-reader` | Reads a `study/*.md` spec and returns a tight, structured summary + the exact requirements/acceptance criteria for the current task. Saves the main thread from loading whole specs. | Read, Grep, Glob |
| `contract-guardian` | Verifies a change does not violate or silently fork the frozen shared contracts (§5). Run before any commit that touches `packages/contracts`. | Read, Grep |
| `test-author` | Given a module + its spec section, writes the failing test suite first (unit + contract tests). | Read, Write, Edit |
| `test-runner` | Runs the relevant test subset, parses failures, returns a minimal diagnosis. Keeps long test logs out of the main window. | Bash(make test:*), Read |
| `code-reviewer` | Reviews a diff against the milestone DoD + §14 checklist + style; returns blocking/major/minor findings. | Read, Grep, Bash(git diff:*) |
| `agent-factory-smith` | Specialized for M6–M9: turns a row in `agents.md` + its spec into a concrete `AgentConfig` (prompt, rubric, tools, QC) using the factory template. | Read, Write, Edit, Grep |

> **Usage rule:** Delegate *reading* and *verification* to subagents; keep *decisions* and *integration* on the main thread. Invoke `spec-reader` at the top of each milestone instead of pasting specs.

### 2.4 Slash commands to create (`.claude/commands/`)

Repeatable workflows as version-controlled prompts (full bodies in Appendix C):

| Command | Purpose |
|---------|---------|
| `/milestone <id>` | Loads the milestone from this plan, invokes `spec-reader` on its referenced specs, enters plan mode, and drafts the task breakdown + acceptance checklist. |
| `/new-agent <number>` | Runs the Agent Implementation Playbook (§8) for one agent number from `agents.md`. |
| `/verify` | Runs `make verify` and summarizes failures with proposed fixes. |
| `/contract-check` | Invokes `contract-guardian` on the staged diff. |
| `/gate <Q1..Q6|L1..L3>` | Runs the named QC layer against a given artifact/module and reports pass/fail with evidence. |
| `/adr <title>` | Appends a new dated ADR to `DECISIONS.md` from the current discussion. |
| `/harden <theme>` | Runs one of the 10 themes from the §14 100-point checklist as a focused audit. |

### 2.5 MCP servers to configure (`.mcp.json`, project-scoped)

Configure incrementally — only when a milestone needs them:

| MCP server | Milestone | Use |
|------------|-----------|-----|
| **Postgres** (read-only role) | M2 | Let Claude Code inspect schema/state while debugging the orchestrator. |
| **Filesystem** (scoped to repo) | M0 | Already covered by native tools; add only if needed for large-asset dirs. |
| **GitHub** | M0 | PR/issue automation in CI (headless mode). |
| **LangSmith / observability** (if available) | M8+ | Pull traces while debugging agent runs. |
| **Temporal** (custom, optional) | M2 | Inspect workflow histories. |

> Keep MCP minimal. Each server adds tool-surface and context overhead. Prefer the repo's own `make` targets and the typed SDK over ad-hoc MCP where possible.

### 2.6 Hooks (`.claude/settings.json`)

Deterministic automation around your actions (events: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `PreCompact`, `SessionStart`):

| Hook | Event | Action |
|------|-------|--------|
| **Auto-format** | `PostToolUse` on Edit/Write to `*.py`/`*.ts` | Run `ruff format` / `prettier` on the changed file. |
| **Block protected paths** | `PreToolUse` on Edit/Write | Deny edits to `packages/contracts/**` unless the prompt explicitly says "contract change" + an ADR exists. Enforces G1. |
| **Type/lint gate** | `Stop` | Run `make verify`; if red, surface the failure so the turn doesn't end on a broken tree. |
| **Secret scan** | `PreToolUse` on Bash | Block commands that would print/commit `.env` or keys. |
| **Progress reminder** | `Stop` | Remind to update `BUILD_PROGRESS.md` if a milestone task was completed. |

### 2.7 Permissions & sandbox

- Maintain an allowlist in `.claude/settings.json` for safe, frequent commands (`make *`, `pytest`, `pnpm *`, `git status/diff/add/commit`, `docker compose *`).
- **Never** allowlist destructive/irreversible commands (`git push --force`, `rm -rf`, prod deploy). Those require explicit human confirmation.
- In CI/headless (`claude -p`), run inside a container with `--dangerously-skip-permissions` *only* because the container is the sandbox — never on a dev machine with credentials.

### 2.8 Context hygiene & parallelism

- **`/clear`** between milestones and unrelated tasks. A bloated window causes regressions and contradictions.
- **`/compact`** at natural breakpoints within a long task; write a one-line state summary to `BUILD_PROGRESS.md` before compacting so nothing is lost.
- **Git worktrees** for safe parallel tracks (e.g., UI in one worktree, meta-agents in another) without branch thrash:
  `git worktree add ../swarm-ui feature/m10-ui`.
- Prefer **subagents** for any sub-investigation that would otherwise dump large output (test logs, spec text, grep sweeps) into the main thread.

### 2.9 Definition of Done (applies to every task)

A task is **Done** only when **all** hold:
1. Behavior covered by tests written *before* the code; all green.
2. `make verify` passes (ruff + mypy/pyright + eslint + tsc + unit).
3. Public types/contracts unchanged, or changed via an ADR + `contract-guardian` sign-off.
4. `code-reviewer` subagent returns no blocking/major findings.
5. Relevant milestone Acceptance Gate criteria met with evidence (logged in `BUILD_PROGRESS.md`).
6. Conventional Commit made; no secrets, no debug cruft, no `TODO` without a tracked issue.
7. Docs touched: package `CLAUDE.md`/README updated if the public surface changed.


---

## 3. Tech Stack Decisions (Pinned)

These are **decisions, not options**. Record any deviation as an ADR. Versions are pinned at build start; the `dependency-upgrade` milestone (M12) is the only place they move.

### 3.1 Languages & runtimes

| Concern | Choice | Notes |
|---------|--------|-------|
| Backend / agents | **Python 3.12** | LangGraph, Temporal SDK, litellm, ML tooling all Python-first. |
| Python env & deps | **uv** (lockfile-driven) | Fast, reproducible; one workspace lock. |
| Frontend | **TypeScript 5.x, React 19, Next.js 15 (App Router)** | Per [`ui/architecture_communication.md`](./ui/architecture_communication.md). |
| JS package mgr / monorepo | **pnpm workspaces + Turborepo** | Caches builds across `apps/*` + `packages/*` (TS side). |
| Lint/format | **ruff** (Py), **eslint + prettier** (TS) | Enforced in hooks + CI. |
| Types | **pyright/mypy (strict)** (Py), **tsc strict** (TS) | No untyped public surface. |
| Tests | **pytest + pytest-asyncio + hypothesis** (Py), **vitest + Playwright** (TS) | Property tests for contracts; Playwright for UI E2E. |

### 3.2 Platform services

| Concern | Choice | Rationale (from specs) |
|---------|--------|------------------------|
| Agent orchestration (DAG) | **LangGraph** | DAG + conditional edges + first-class HiTL gates + checkpointing. |
| Durable workflow engine | **Temporal (Python SDK)** | Productions run minutes→hours; guaranteed delivery, retries, replay. |
| Event bus | **Redis Streams** (dev/MVP) → **NATS JetStream** (scale) | Pub/sub + persistence + replay; topic-per-production. |
| Relational store | **PostgreSQL 16** + **SQLModel/SQLAlchemy 2 + Alembic** | Production metadata, gate state, critiques, configs, audit log. (Spec mentions Drizzle; we standardize on Python ORM since the gateway is FastAPI. TS types are generated from Pydantic — see §5.6. ADR-001.) |
| Object storage | **S3 / Cloudflare R2** (via `boto3`/S3 API) | Video/audio/image artifacts; content-addressed keys. |
| Vector DB | **Chroma** (dev) → **Pinecone/Weaviate** (prod) | MemoryAgent + Agentic RAG retrieval. |
| Graph/Hybrid RAG | **LightRAG over OpenSearch** | Per [`agentic_rag_functional_specification.md`](./agentic_rag_functional_specification.md). |
| Cache / sessions / rate-limit | **Redis** | Hot data, locks, token buckets. |
| API gateway | **FastAPI** + **uvicorn/gunicorn** | REST + WebSocket gateway. |
| LLM access | **litellm** unified client | One interface for Grok-4.x, Gemini 2.5 Pro, GPT-4o, Claude 4, OSS. |
| Observability | **LangSmith** (agent traces) + **OpenTelemetry → Grafana/Tempo/Loki** | Traces, metrics, logs, replay. |
| Provenance | **C2PA** (`c2pa-python`) | Sign every artifact; verify chain downstream. |
| Containerization | **Docker** + **docker-compose** (dev) → **Kubernetes + Helm** (prod) | GPU node pool for gen tasks; CPU pool for LLM-only. |
| Secrets | **Doppler/Vault** (prod), `.env` + `direnv` (dev, gitignored) | Never in repo. |

### 3.3 External tool providers (behind interfaces — never called directly by agents)

| Capability | Providers | Interface to build |
|-----------|-----------|--------------------|
| Text/Video gen | Sora 2, Veo 3.1, Runway Gen-4.5, Kling 3.0, Seedance 2.0, Grok Imagine | `MediaGenProvider` (§5.4) with a `MockGenProvider` for CI |
| TTS / voice clone | ElevenLabs v3 | `VoiceProvider` |
| Lip-sync | Sync.so | `LipSyncProvider` |
| Music | Udio / Suno | `MusicProvider` |
| Spatial audio | Dolby Atmos Renderer | `MixProvider` |
| Eval metrics | VBench, EvalCrafter, CLIP-T, ArcFace, FVD, loudness (ITU-R BS.1770) | `EvalToolProvider` |

> **Decision (ADR-002):** All providers implement a common `Provider` protocol with `capabilities()`, `estimate_cost()`, `invoke()`, and `health()`. The `RouterAgent` selects among providers by cost/quality/latency. CI uses mock providers exclusively.

---

## 4. Monorepo Topology & Repository Scaffold

### 4.1 Top-level layout

```text
va-agent-swarm/                      # repo root (build target; specs live in study/)
├── CLAUDE.md                        # root project memory (Appendix A)
├── BUILD_PROGRESS.md                # living milestone + hardening checklist (you maintain)
├── DECISIONS.md                     # ADR log
├── Makefile                         # the single command surface: make verify|test|dev|...
├── .claude/                         # Claude Code config
│   ├── settings.json                # permissions + hooks (Appendix D)
│   ├── agents/                      # subagents (Appendix B)
│   └── commands/                    # slash commands (Appendix C)
├── .mcp.json                        # project-scoped MCP servers
├── docker-compose.yml               # postgres, redis, temporal, opensearch, chroma, minio
├── pyproject.toml                   # uv workspace root
├── uv.lock
├── pnpm-workspace.yaml
├── turbo.json
├── infra/                           # IaC: helm charts, k8s manifests, terraform
│
├── packages/                        # SHARED, REUSABLE (build these FIRST)
│   ├── contracts/                   # ⭐ FROZEN shared Pydantic models + generated TS types (§5)
│   ├── agent-core/                  # BaseAgent, lifecycle, Self-Refine/Reflexion loop (§5.3)
│   ├── agent-factory/               # AgentConfig → runnable agent (§8)
│   ├── llm-gateway/                 # litellm wrapper, metering, routing hooks (M3)
│   ├── providers/                   # MediaGen/Voice/LipSync/Music/Eval provider impls + mocks
│   ├── rag/                         # Agentic RAG client + indexers (M1)
│   ├── qc/                          # L1/L2/L3 judges + Q1–Q6 delivery mesh (§5.5)
│   ├── eventbus/                    # Redis Streams/NATS pub-sub + typed topics
│   ├── memory/                      # MemoryAgent store (episodic + vector)
│   ├── provenance/                  # C2PA signing/verification
│   └── observability/              # OTel + LangSmith wiring, structured logging
│
├── services/                        # DEPLOYABLE PROCESSES
│   ├── orchestrator/                # LangGraph graphs + Temporal workflows/activities (M2)
│   ├── agent-runtime/               # worker pool that executes agent nodes (M2/M6)
│   ├── api-gateway/                 # FastAPI REST + WebSocket gateway (M10)
│   └── scheduler/                   # cron/triggers for optimization + retraining loops
│
├── apps/
│   └── web/                         # Next.js 15 console (M10)
│
├── agents/                          # ⭐ 114 agent definitions (config + rubric + prompts)
│   ├── _registry.yaml               # the canonical agent registry (id→config path)
│   ├── production/                  # 1–52 craft agents
│   ├── meta/                        # 53–80 orchestration/creative/research/optimization
│   ├── support/                     # 81–114 workflow-support agents
│   └── crosscutting/               # GCA, Research, Optimization, DIA, Aesthetics, RAG, etc.
│
├── workflows/                       # the 10 archetype DAGs (A–J) as LangGraph graph defs
│
├── eval/                            # golden sets, rubrics, benchmark runners, sim personas
│   ├── golden/                      # frozen input→expected fixtures
│   ├── rubrics/                     # per-role L2 constitutions (JSON/YAML)
│   └── harness/                     # VBench/EvalCrafter/CLIP-T/FVD runners (wrap providers)
│
└── tests/                           # cross-package integration + E2E + contract tests
```

### 4.2 Build order of the scaffold (M0 produces this skeleton, empty but compiling)

1. `packages/contracts` (the constitution) → 2. `packages/observability` + `packages/eventbus` → 3. `packages/agent-core` → 4. everything else stubs that import contracts and pass `make verify`.

> **Rule:** every package ships with `__init__.py`/`index.ts`, a `CLAUDE.md`, a `tests/` dir, and at least one trivial passing test from the moment it exists, so `make verify` is green at every commit.

---

## 5. Cross-Cutting Contracts (Build These FIRST — They Are Frozen)

This is the most important section. **Everything downstream imports from `packages/contracts`.** Build it in M0–M1, freeze it, and gate changes behind ADR + `contract-guardian` (G1). Source of truth: [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §1.3, §6 and [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md) §7.

### 5.1 The Shared Artifact Handoff Contract

A single Pydantic v2 model carried with every artifact between phases. Fields map 1:1 to the spec table.

```python
# packages/contracts/artifact.py
from enum import Enum
from pydantic import BaseModel, Field

class TechnicalSpec(BaseModel):
    codec: str; aspect_ratio: str; duration_s: float
    frame_rate: float; color_space: str
    loudness_lufs: float | None = None
    caption_required: bool = False

class RightsAndConsent(BaseModel):
    license_state: str
    likeness_consent: bool = False
    voice_consent: bool = False
    territorial_limits: list[str] = []
    embargo_until: str | None = None

class ContinuityState(BaseModel):
    character_look: dict = {}
    props: list[str] = []
    wardrobe: dict = {}
    environment: dict = {}
    identity_hash: str | None = None     # for AIQA / Avatar identity drift

class QCStatus(BaseModel):
    l1_spec: bool | None = None
    l2_rubric: float | None = None        # 0–100
    l3_preference: float | None = None     # win-rate 0–1
    delivery_passes: dict[str, bool] = {}  # {"Q1": True, ... "Q6": False}

class ProvenanceManifest(BaseModel):
    c2pa_ref: str | None = None
    critique_log_ptr: str | None = None
    signoff_chain: list[str] = []
    model_versions: dict[str, str] = {}    # provider→version (determinism, G5)
    seeds: dict[str, int] = {}

class Artifact(BaseModel):
    artifact_id: str
    version: int = 1
    media_type: str                        # video|audio|image|script|manifest|...
    uri: str | None = None
    parent_assets: list[str] = []
    brief_scope: dict                       # subtask, acceptance criteria, audience
    technical_spec: TechnicalSpec | None = None
    rights_and_consent: RightsAndConsent
    continuity_state: ContinuityState = ContinuityState()
    qc_status: QCStatus = QCStatus()
    target_channels: list[str] = []
    provenance_manifest: ProvenanceManifest = ProvenanceManifest()
```

**Contract tests (write first):** round-trip JSON serialization; backward-compat schema snapshot test (fails if a field is removed/renamed without a version bump); `parent_assets` form a valid DAG (no cycles); every released artifact has a non-empty `provenance_manifest`.

### 5.2 The CritiqueMessage bus schema

Verbatim from [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §6. This is how any agent comments on any other.

```python
# packages/contracts/critique.py
from enum import Enum
from pydantic import BaseModel

class Severity(str, Enum):
    blocker = "blocker"; major = "major"; minor = "minor"; nit = "nit"

class Category(str, Enum):
    pacing="pacing"; continuity="continuity"; accuracy="accuracy"
    compliance="compliance"; accessibility="accessibility"; brand="brand"
    craft="craft"; aesthetic="aesthetic"   # aesthetic added per aesthetics_agent spec

class CritiqueMessage(BaseModel):
    critique_id: str
    from_agent: str
    to_agent: str
    artifact_ref: str
    severity: Severity
    category: Category
    evidence: list[str] = []
    suggested_action: str
    rubric_reference: str | None = None
    must_resolve_before: str | None = None   # phase id
    rubric_score: float | None = None
    timestamp: str
```

**Acceptance rules (implement in `agent-core`, test exhaustively):**
- `blocker` → halts the DAG node until resolved (Temporal signal / LangGraph interrupt).
- `major` → triggers Self-Refine/Reflexion loop on the receiver, **max 3 iterations**, then escalate to JudgeAgent.
- `minor`/`nit` → logged to MemoryAgent; aggregated as RLAIF reward signal for the next training cycle.
- Two-agent disputes → routed to JudgeAgent (multi-agent debate). ComplianceAgent critiques are always `blocker` (BLOCK gate).

### 5.3 The Common Agent base class

Every one of the 114 agents is an instance of `BaseAgent` (G3). Source: [`common-agent-structure.svg/html`](./common-agent-structure.html) and the per-agent spec tables (responsibility, knowledge source, self-quality, surpass signal, critique in/out).

```python
# packages/agent-core/base.py  (sketch — full impl in M2/M6)
class AgentConfig(BaseModel):
    id: str; name: str; category: str
    system_prompt_ref: str                 # path to versioned prompt
    model_policy: ModelPolicy              # preferred model(s), fallbacks, budget
    tools: list[str]                       # provider/tool ids the agent may call
    rubric_ref: str                        # L2 constitution for this role
    self_quality_metrics: list[MetricSpec] # e.g., CLIP-T>=0.32
    critiques_from: list[str]; critiques_on: list[str]
    max_refine_iters: int = 3

class BaseAgent:
    """draft -> self-critique(rubric) -> revise (Self-Refine, Madaan 2023);
       on failure store verbal feedback + retry (Reflexion, Shinn 2023)."""
    async def run(self, task: Task, ctx: RunContext) -> Artifact: ...
    async def self_refine(self, draft, rubric) -> Artifact: ...
    async def accept_critique(self, msg: CritiqueMessage) -> None: ...
    async def emit_critique(self, target, finding) -> CritiqueMessage: ...
    def provenance(self) -> ProvenanceManifest: ...
```

The base class wires in: LLM gateway (metered), RAG client, MemoryAgent, event-bus emit, provenance signing, OTel span. **No agent subclass reimplements these.** Specializations differ only by `AgentConfig`.

### 5.4 Provider interfaces (mockable)

```python
# packages/providers/base.py
class Provider(Protocol):
    def capabilities(self) -> set[str]: ...
    async def estimate_cost(self, req) -> CostEstimate: ...
    async def invoke(self, req) -> ProviderResult: ...
    async def health(self) -> bool: ...

class MediaGenProvider(Provider): ...      # Sora/Veo/Runway/Kling/Seedance
class MockGenProvider(MediaGenProvider):   # returns deterministic placeholder media + fake metrics for CI
    ...
```

**Rule:** CI and all unit/integration tests use mocks. A single nightly "live-smoke" job hits real providers behind a budget cap (§10.2).

### 5.5 The Quality Mesh — L1/L2/L3 + Q1–Q6

From [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §5. Implemented in `packages/qc`. The orchestrator advances a node only when its required QC layers pass.

| API | Layer | Mechanism | Pass |
|-----|-------|-----------|------|
| `qc.l1_spec(artifact)` | Spec | JSON-schema + tool validators (codec/LUFS/aspect/length) | 100% |
| `qc.l2_rubric(artifact, rubric)` | Rubric | LLM-as-judge w/ role constitution | ≥85/100 |
| `qc.l3_preference(artifact, baseline)` | Preference | Pairwise vs human ref + AudienceSim ≥200 personas + ≥20 HiTL | ≥0.50 parity / ≥0.55 surpass |
| `qc.delivery(artifact)` | Q1–Q6 | spec / artifact / audio-sync / continuity / perceptual / outlet-readiness | all 6 pass |

**Build note:** L1 and Q1/Q3/Q6 are deterministic validators (build first, fully testable). L2/L3/Q5 use LLM/sim judges (build with frozen-judge + golden sets to keep them stable; never let a judge model float unpinned).

### 5.6 Type propagation to the frontend

Generate TS types from the Pydantic contracts so the UI never drifts: `datamodel-code-generator`/`pydantic2ts` → `packages/contracts/ts/`. Turborepo task `contracts:gen` runs in CI; a check fails the build if generated types are stale. This keeps WebSocket event payloads and REST bodies (from [`ui/architecture_communication.md`](./ui/architecture_communication.md)) type-safe end to end.

### 5.7 Event-bus topic contract

Topics (from `ui/architecture_communication.md`): `production.{id}.agent_events`, `.critiques`, `.gates`, `.artifacts`, plus `system.alerts`. Every event is one of the typed WebSocket event models (`agent_state_change`, `artifact_created`, `critique_message`, `gate_ready`, `gate_resolved`, `budget_update`, `metric_update`, `memory_entry`, `tool_call`, `production_phase_change`, `error`). These live in `packages/contracts/events.py` and are the *only* shapes allowed on the bus.


---

## 6. Phased Build Roadmap (Milestones M0–M12)

**Sequencing principle** (from [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md) §11): Foundation → Intelligence → Production → Enhancement, but with a **vertical slice (G2)** punched through as early as M6 so the architecture is proven before breadth.

Each milestone below specifies: **Goal · Depends on · Build (files) · Claude Code workflow · Tests · Acceptance Gate**. Treat the Acceptance Gate as a hard stop — do not start the next milestone until it is green and logged in `BUILD_PROGRESS.md`.

> **Effort note:** "weeks" below are *relative sizing* for sequencing, not commitments. A single Claude Code session can complete several small tasks; large milestones (M2, M7, M10) span many sessions with `/clear` between tasks.

### Milestone dependency graph

```text
M0 Bootstrap ──► M1 RAG ──► M2 Orchestration ──► M3 LLM Gateway+Router+CostDash
                                  │                       │
                                  ▼                       ▼
                          M4 Research+Coding harness   M5 Intelligence (DIA,GCA,Opt,Goal,CPS,Aesthetics)
                                  │                       │
                                  └───────────┬───────────┘
                                              ▼
                                  M6 Agent Factory + VERTICAL SLICE (Workflow A) ◄── proves architecture
                                              ▼
                                  M7 Production agents 1–52 (factory breadth)
                                              ▼
                                  M8 Meta-agents 53–80 + QC mesh + GateKeeper
                                              ▼
                                  M9 Support agents 81–114 + Delivery fabric
                                              ▼
                                  M10 UI (web + gateway + websocket)   ── can start in parallel after M3 via worktree
                                              ▼
                                  M11 Enhancement (psych, podcast, personalization)
                                              ▼
                                  M12 Hardening, scale, security, launch (the §14 100-point pass)
```

---

### M0 — Bootstrap, Infra & Claude Code Setup

**Goal:** A compiling, green, fully-tooled empty monorepo with all Claude Code config in place. Nothing does anything yet — but `make verify` passes and `docker compose up` brings up every backing service.

**Depends on:** nothing.

**Build:**
- Repo scaffold from §4.1 (every package/service as an importable stub with one passing test).
- `Makefile` targets: `bootstrap`, `verify` (lint+type+unit), `test`, `test-int`, `dev`, `fmt`, `contracts:gen`, `up`, `down`, `clean`.
- `docker-compose.yml`: postgres, redis, temporal (+ UI), opensearch, chroma, minio (S3-compatible).
- `pyproject.toml` (uv workspace) + `pnpm-workspace.yaml` + `turbo.json`, all versions pinned (§3).
- CI pipeline (§11): lint → type → unit → contract-snapshot → build.
- **Claude Code config:** root + per-package `CLAUDE.md` (Appendix A), `.claude/agents/*` (Appendix B), `.claude/commands/*` (Appendix C), `.claude/settings.json` hooks/permissions (Appendix D), `.mcp.json` (Postgres+GitHub only).
- `BUILD_PROGRESS.md` and `DECISIONS.md` seeded (ADR-001, ADR-002).

**Claude Code workflow:** Start with `/init`; hand-edit `CLAUDE.md` to Appendix A. Create subagents/commands. Use plan mode to lay out the scaffold; generate it package-by-package, running `make verify` after each so green is continuous.

**Tests:** one trivial test per package; CI proves the matrix (Py 3.12, Node 20) green; `docker compose up` health-checks pass.

**Acceptance Gate G-M0:** `make bootstrap && make up && make verify` all green from a clean clone; `.claude/` subagents callable; ADR log started. ✅ before M1.

---

### M1 — Foundation: Agentic RAG (Knowledge Backbone)

**Goal:** The shared knowledge service every agent will call. Spec: [`agentic_rag_functional_specification.md`](./agentic_rag_functional_specification.md).

**Depends on:** M0.

**Build (`packages/rag`):**
- Ingestion pipeline: chunk → embed → index into Chroma (dev) + LightRAG/OpenSearch graph layer.
- Hybrid retrieval: vector + graph + keyword, with reranking; query-planning ("agentic" retrieval that decides what to fetch).
- `RAGClient` API: `retrieve(query, filters, k)`, `compound(query)` (multi-hop), `ingest(doc)`, `cite()` (returns source-graded provenance for FactChecker/Citation agents).
- Knowledge namespaces: per-project, per-domain, and global (so a project's world-bible is isolated).
- Freshness/eviction + a deterministic offline embedding model option for CI.

**Claude Code workflow:** `spec-reader` on the RAG spec → plan namespaces + retrieval modes → TDD the `RAGClient` against a tiny golden corpus (5 docs) → integrate Chroma/OpenSearch behind the interface (mock embeddings in unit tests, real in `make test-int`).

**Tests:** retrieval precision@5 ≥ 0.9 on the golden corpus Q&A set; citation grading returns primary/secondary/tertiary correctly; multi-hop compound query returns linked evidence; namespace isolation (project A can't see project B).

**Acceptance Gate G-M1:** `RAGClient` passes precision target on golden set; graph + vector both queried; provenance-graded citations returned. ✅

---

### M2 — Foundation: Orchestration Runtime (the Control Plane)

**Goal:** The beating heart — LangGraph DAG execution made durable by Temporal, wired to the Event Bus and Asset/State stores. This is the largest platform milestone.

**Depends on:** M0 (contracts), M1 (so nodes can call RAG).

**Build:**
- `packages/eventbus`: typed Redis Streams pub/sub; topic contract (§5.7); replayable; at-least-once + idempotency keys.
- `packages/observability`: OTel tracing + structured logs + LangSmith hookup; every node run is a span.
- `services/orchestrator`:
  - **LangGraph graph runtime**: nodes = agent tasks; conditional edges; **HiTL interrupt** points (gates); checkpointer backed by Postgres.
  - **Temporal workflows/activities**: each agent task is a Temporal activity (retry/backoff/timeout); the production is a Temporal workflow (resumable across restarts).
  - **OrchestratorAgent / PlannerAgent / RouterAgent / JudgeAgent / GateKeeperAgent / MemoryAgent** skeletons (agents #53–58) — these are *platform* agents, built here, refined in M8.
  - DAG primitives: fan-out/fan-in, dependency-triggered rerender, deadlock detection, SLA timers.
- `packages/memory`: episodic + long-term project memory (Reflexion/MemGPT pattern) over the vector DB; `MemoryAgent` retrieval API.
- Asset/Data backbone: immutable `artifact_id`, copy-on-write versions, dependency edges, searchable metadata (Postgres + S3/MinIO), C2PA signing via `packages/provenance`.
- State store: production state machine; gate state; durable, auditable, resumable.

**Claude Code workflow:** This is a "think hard" milestone. Plan the LangGraph↔Temporal boundary explicitly (ADR-003: *what lives in LangGraph vs Temporal*). Build the event bus + a 2-node toy graph first (echo → echo), prove durability by killing the worker mid-run and resuming. Then add HiTL interrupt, then the platform-agent skeletons. Use the Postgres MCP to inspect checkpoints while debugging.

**Tests:** kill-and-resume integration test (worker crash mid-DAG → resumes from checkpoint, no lost/dup tasks); fan-out/fan-in correctness; blocker-critique halts the node; gate interrupt waits for an external signal then proceeds; event replay reconstructs full state; deadlock detector trips on a cyclic plan.

**Acceptance Gate G-M2:** A hard-coded 3-node DAG (`Planner → echo-agent → GateKeeper`) runs end-to-end on real Temporal+Redis+Postgres, survives a mid-run worker kill, emits correct typed events, and signs artifacts with C2PA. ✅ This is the *walking skeleton*.

---

### M3 — Foundation: LLM Gateway, Router & Cost Dashboard

**Goal:** Every token metered and routed from day one (G6). Specs: [`llm_usage_functional_specification.md`](./llm_usage_functional_specification.md); RouterAgent in [`agents.md`](./agents.md) §9.

**Depends on:** M2.

**Build:**
- `packages/llm-gateway`: litellm wrapper exposing `complete()/stream()/embed()` with: provider/model abstraction (Grok-4.x, Gemini 2.5 Pro, GPT-4o, Claude 4, OSS), automatic retry/fallback, **per-call token+cost metering** emitted to the bus (`budget_update`), prompt+model **version tagging** into provenance (G5), response caching, and a **frozen-judge** mode for QC.
- **RouterAgent (#55)** real impl: capability registry + benchmark history → pick agent/model by cost/quality/latency; budget-aware. **CostOptimizerAgent (#74)** hooks.
- **LLM Usage Dashboard** backend: aggregates spend per production/agent/provider; alert thresholds; exposes `/api/llm-usage`.
- Budget guardrails: per-production budget envelope; hard stop + escalation when exceeded (ProducerAgent gate).

**Claude Code workflow:** TDD the metering math first (golden token→cost fixtures per provider price sheet). Build the registry as data (`agents/_registry.yaml` + a benchmark table) so routing is configurable, not hard-coded.

**Tests:** cost computed correctly per provider; fallback on provider error; budget-exceeded halts + emits escalation; router picks the Pareto-optimal provider on a fixture matrix; cache hit avoids a call; every call writes model+prompt version to provenance.

**Acceptance Gate G-M3:** Any agent call is metered, routed, version-tagged, and visible in the cost dashboard; budget breach triggers a real stop. ✅

---

### M4 — Foundation: Research Agent + Coding Agent Harness

**Goal:** The knowledge-acquisition service and the self-build conventions. Specs: [`research_agent_functional_specification.md`](./research_agent_functional_specification.md) (+ technical spec), [`coding_agent_functional_specification.md`](./coding_agent_functional_specification.md).

**Depends on:** M1 (RAG), M3 (gateway).

**Build:**
- **Research Agent** (`agents/crosscutting/research/`): query planning → multi-source retrieval (web + archive via providers) → synthesis → source-graded, cited dossier (writes to RAG namespaces). Sub-capabilities map to meta-agents #66–72 (built fully in M8; here build the core service they share).
- **Coding Agent harness**: codify the [`coding_agent_functional_specification.md`](./coding_agent_functional_specification.md) conventions as the project's own `.claude/` standards (this *is* Claude Code's playbook). Build the `agent-factory` scaffolding it relies on (templates, validators) — even though factory breadth comes in M6.

**Claude Code workflow:** Note that the Coding Agent spec describes *your own role*. Extract its conventions (naming, structure, review rubric) into `CLAUDE.md` and the `code-reviewer` subagent so they're enforced for the rest of the build.

**Tests:** Research Agent returns a cited dossier whose claims each carry a graded source; refuses to assert uncited claims (FactChecker-style guard); dossier is ingested and retrievable via RAG.

**Acceptance Gate G-M4:** Research Agent produces a graded, cited dossier on a test topic and stores it in RAG; coding conventions enforced by `code-reviewer`. ✅

---

### M5 — Intelligence Layer (Reasoning Services)

**Goal:** The shared "brains" every production agent consumes. Specs: [`intent_analysis_agent_functional_specification.md`](./intent_analysis_agent_functional_specification.md) (DIA), [`general_creative_agent_functional_specification.md`](./general_creative_agent_functional_specification.md)+technical (GCA/SSOR), [`optimization_agent_functional_specification.md`](./optimization_agent_functional_specification.md)+technical, [`strategic_goal_achievement_agent_functional_specification.md`](./strategic_goal_achievement_agent_functional_specification.md), [`complex_problem_solution_process_model.md`](./complex_problem_solution_process_model.md), [`aesthetics_agent_functional_specification.md`](./aesthetics_agent_functional_specification.md).

**Depends on:** M1–M4.

**Build (each as a crosscutting service agent, all on `BaseAgent`):**
1. **DIA (Deep Intent Analysis)** — parses briefs → structured intent (goals, audience, hidden agendas, constraints). The entry point of every production.
2. **GCA (SSOR)** — creative ideation engine; the 7-phase SSOR pipeline + domain factory. Consumed by Director/Screenwriter/ConceptArtist/Ideation.
3. **Process Optimization Agent** — DMAIC + Lean + multi-agent consensus over workflow telemetry.
4. **Strategic Goal Achievement** — 6-stage goal-clarification framework used by all planning agents.
5. **Complex Problem Solving** — WHAT/WHY/HOW/DO/REVIEW methodology for diagnostic agents.
6. **Aesthetics Agent** — the decomposed multimodal Critic + Aligner + Taste-Keeper (per the spec you authored); supplies `qc.l2`/perceptual scoring, novelty (D9) to GCA, and `aesthetic` critiques. Wire its `AestheticVerdict` into `packages/qc` and the critique bus.

**Claude Code workflow:** One sub-task per service; `/clear` between them. Each follows the Agent Implementation Playbook (§8). GCA and Aesthetics form a generate↔evaluate loop — build GCA's novelty score to *call* the Aesthetics Agent (don't duplicate).

**Tests:** DIA extracts the structured-intent schema from sample briefs (golden set); GCA produces traceable SSOR output with per-dimension scores; Aesthetics returns a decomposed `AestheticVector` + `hack_likelihood` and escalates low-confidence; Optimization proposes a measurable workflow delta on a telemetry fixture.

**Acceptance Gate G-M5:** All six reasoning services callable via the gateway, each passing its golden-set behavioral test; GCA↔Aesthetics loop demonstrated. ✅

---

### M6 — Agent Factory + Vertical Slice (Workflow A, end-to-end) ⭐

**Goal:** Prove the *entire* architecture with the cheapest real workflow before building 109 more agents (G2). Implement the **Agent Factory** and just enough craft agents to run **Workflow A — Viral Hook Clip** end-to-end through real infra with mock gen-providers.

**Depends on:** M2–M5.

**Build:**
- **Agent Factory** (`packages/agent-factory`): `AgentConfig (YAML) → runnable BaseAgent`. Validates prompt/rubric/tools/QC refs; registers into `agents/_registry.yaml`; generates the per-agent test skeleton. This is the engine for M7–M9.
- **Workflow A craft agents** (subset, via factory): TrendIntelligenceAgent, CopywriterAgent, SocialMediaStrategistAgent, PromptEngineerAgent/GeneratorOperator, AIQAConsistencyAgent, EditorAgent, AccessibilityOptimizerAgent, AudienceSimAgent, AnalystAgent — exactly the crew in [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3.1.
- **Workflow A DAG** (`workflows/A_viral_hook.py`): Concept → Production → Post → Review → Distribution → Post-launch, with the spec'd critic gates.
- End-to-end run: brief → DIA → Planner builds the A-DAG → agents execute (mock gen) → artifacts flow with handoff contract → critique bus active → QC mesh gates → C2PA-signed deliverable → events on the bus.

**Claude Code workflow:** "ultrathink" the factory design — it must produce all 114 agents later, so its `AgentConfig` schema must be complete now. Build factory + one agent + its test, then the rest of the crew, then the DAG, then the E2E test. Use `agent-factory-smith` subagent for each agent config.

**Tests:** full E2E integration test of Workflow A on mocks (deterministic); each agent passes L1+L2 on golden inputs; a `blocker` critique halts and re-routes; budget metered end-to-end; provenance chain verifiable from final artifact back to brief.

**Acceptance Gate G-M6 (CRITICAL):** `make e2e-workflow-a` produces a signed deliverable from a brief, with every handoff contract populated, every gate enforced, all events emitted, full provenance, under budget — using mock providers. **This gate proves the platform. Do not proceed to breadth until it is rock-solid.** ✅

---

### M7 — Production Agents 1–52 (Breadth via Factory)

**Goal:** Implement the remaining craft agents (categories 1–8: agents #1–52) as factory-produced configs + rubrics + prompts. Specs: [`agents.md`](./agents.md) §1–8 and [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §2.1–2.8; deep specs for Screenwriter ([`screenwriter_strategic_goal_achievement_agent_functional_specification.md`](./screenwriter_strategic_goal_achievement_agent_functional_specification.md)) and shared VO/podcast patterns.

**Depends on:** M6.

**Build:** For each agent, the Playbook (§8) produces: `AgentConfig`, versioned system prompt, L2 rubric/constitution (in `eval/rubrics/`), self-quality metric wiring (e.g., DoP: rule-of-thirds + exposure-zone + color-temp; Colorist: ΔE<2; SoundMixer: LUFS+STOI; etc. — all already enumerated in the spec tables), tool allowlist, and critique in/out edges (from the §4 critique matrix). Batch by category to share rubric scaffolding.

**Claude Code workflow:** Use `/new-agent <n>` per agent. Process category-by-category (camera 6–8, editorial/color 9–18, sound 19–22, performance 23–27, marketing 28–31, domain 32–45, AI-era 46–52). `/clear` between categories. For each agent, `spec-reader` pulls its exact row (self-quality, surpass signal, critique edges) → factory config → test → review.

**Tests:** every agent: L1 schema conformance; L2 rubric ≥85 on its golden inputs; emits/accepts critique per the matrix; respects its tool allowlist; metered. Category-level integration tests (e.g., DoP→Colorist→Editor handoff preserves continuity_state).

**Acceptance Gate G-M7:** All 52 craft agents registered, each green on L1+L2 golden tests and critique-matrix tests; at least 3 additional workflow archetypes (e.g., C Animated Explainer, E AI Short Film, B UGC Ad) run end-to-end on mocks. ✅

---

### M8 — Meta-Agents 53–80 + Full QC Mesh + Gatekeeping

**Goal:** Promote the M2 platform-agent skeletons to full implementations and add the creative/research/optimization meta-agents that "shape how the work is done." Specs: [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §2.9.

**Depends on:** M7.

**Build:**
- **Orchestration (53–58):** harden Orchestrator/Planner/Router/Judge/GateKeeper/Memory with full dispute-resolution (multi-agent debate), stage-gate sign-off, and escaped-defect=0 discipline.
- **Creative (59–65):** Ideation, NarrativeArc, StyleTransfer, MoodBoard, Novelty/Anti-Cliché, EmotionalArc, WorldBuilding — many delegate to GCA/Aesthetics (no duplication).
- **Research (66–72):** Web/Archive/Trend/Competitor/Citation/InterviewSynthesis/Benchmark — built on the M4 Research Agent core.
- **Optimization (73–80):** Prompt/Cost/Latency/Retention/ROAS/Accessibility optimizers + EvaluationHarness + SafetyRedTeam.
- **Full QC mesh**: complete L3 (AudienceSim ≥200 personas + HiTL sampling) and Q1–Q6 delivery validators; `GateKeeperAgent` enforces "zero leaked defects."

**Claude Code workflow:** Build per family. `EvaluationHarnessAgent` (#79) and `SafetyRedTeamAgent` (#80) are force-multipliers — build them early in M8 so they continuously test everything else (regression alerts, adversarial probes).

**Tests:** Judge inter-rater agreement κ≥0.8 vs a fixture human-panel; GateKeeper blocks a seeded defect; SafetyRedTeam attack-success ≤1% on the seeded attack set; EvaluationHarness detects an injected regression <1h; AudienceSim L3 win-rate computed on a golden pair.

**Acceptance Gate G-M8:** All 80 agents live; full L1/L2/L3 + Q1–Q6 enforced on every release path; red-team + eval-harness running continuously in CI nightly. ✅

---

### M9 — Workflow-Support Agents 81–114 + Delivery Fabric

**Goal:** Production-infrastructure agents and multi-channel delivery. Specs: [`agents.md`](./agents.md) §10; delivery branching in [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3.0.

**Depends on:** M8.

**Build:**
- **81–90** asset mgmt/versioning/render dispatch: RenderFarmAgent (GPU batch dispatch + autoscale), AssetManagerAgent, VersioningAgent, DependencyRerenderAgent.
- **91–100** quality gates/delivery packaging/compliance: DeliveryAgent, QCGateAgent, packaging into DCP / streaming mezzanine / broadcast master / archive / trailer / social cutdowns with outlet-specific specs, captions, metadata, DRM/KDM, C2PA payloads.
- **101–114** analytics/feedback/retraining: AnalyticsAgent, FeedbackLoopAgent, RetrainingTriggerAgent (RLAIF reward aggregation from minor/nit critiques), CorrectionsAgent.
- **Delivery Fabric**: branching pipeline (theatrical/streaming/broadcast/archive + marketing derivatives in parallel) with per-outlet validation.

**Claude Code workflow:** Factory configs for the agents; real engineering for RenderFarm autoscale and the delivery packaging validators (deterministic — TDD heavily). Wire the post-launch learning loop into the Optimization Agent (M5) and RetrainingTrigger.

**Tests:** delivery packager emits each outlet variant passing Q6; RenderFarm autoscales under a queued-job fixture; dependency change triggers correct re-render set; RLAIF aggregation produces a reward delta from logged nit critiques.

**Acceptance Gate G-M9:** A production produces all four delivery branches + marketing derivatives, each Q6-valid with provenance; post-launch telemetry flows back into a retraining ticket. ✅


---

### M10 — UI: Console, API Gateway & WebSocket Layer

**Goal:** The human operator surface. Specs: all of [`ui/`](./ui/) — [`architecture_communication.md`](./ui/architecture_communication.md), [`agent_management_ui.md`](./ui/agent_management_ui.md), [`backend_agent_management.md`](./ui/backend_agent_management.md), [`ui_design.md`](./ui/ui_design.md), [`project_creation_flow.md`](./ui/project_creation_flow.md), [`production_scale_discovery.md`](./ui/production_scale_discovery.md), [`video_remake_enhancement.md`](./ui/video_remake_enhancement.md), [`RETHINK_100_IMPROVEMENTS.md`](./ui/RETHINK_100_IMPROVEMENTS.md).

**Depends on:** M3 (events exist); can **start in parallel after M3 in a git worktree** against a fake-event emitter, then integrate.

**Build:**
- `services/api-gateway` (FastAPI): REST endpoints + WebSocket gateway exactly per the API contract tables in [`architecture_communication.md`](./ui/architecture_communication.md) (`POST /api/productions`, gate decisions, critiques, retry/skip, router-config, artifacts, delivery). Auth/RBAC, rate-limit, validation, C2PA signing on gate approval. Subscribes to the Event Bus, filters by `production_id`, fans out over WebSocket.
- `apps/web` (Next.js 15 + React 19): Brief Studio, DAG Canvas (live node states), Artifact Gallery, Critique Feed, Gate Approval Dialog, Budget Tracker, Quality Dashboard, Agent Inspector, Memory Panel, Delivery Hub. State via Zustand + React Query; WebSocket via socket.io-client (auto-reconnect, room-per-production). Types imported from generated `packages/contracts/ts` (§5.6).
- Project-creation flow + production-scale discovery (S0–S? scale profiles) + video-remake/enhancement flow.

**Claude Code workflow:** Build gateway first (typed, tested) so the UI has a real contract. Then UI components, driven by the WebSocket event types. Use Playwright for the critical journeys. Honor `RETHINK_100_IMPROVEMENTS.md` as a UI hardening backlog.

**Tests:** gateway contract tests (REST + WS payloads match `packages/contracts`); Playwright E2E: launch Workflow A from Brief Studio → watch DAG nodes transition live → approve a gate → see artifact in Gallery → trigger delivery. WebSocket reconnect resumes state. RBAC denies unauthorized gate approval.

**Acceptance Gate G-M10:** A human can launch, monitor in real time, critique, approve gates, and download deliverables for Workflow A entirely through the browser, with <50ms-class live updates and no agent→UI direct calls. ✅

---

### M11 — Enhancement Layer

**Goal:** Personalization and audio-first variants. Specs: [`psychological_profile_agent_functional_specifications.md`](./psychological_profile_agent_functional_specifications.md), [`psychological_recommendation_agent_functional_specification.md`](./psychological_recommendation_agent_functional_specification.md), [`podcast_agent_functional_specifcation.md`](./podcast_agent_functional_specifcation.md).

**Depends on:** M7–M9.

**Build:**
- **Psychological Profiling** (100 creator profiles: MBTI, motivations, fears, creative params) → feeds Casting/Talent/Personalization/UGC agents and Aesthetic-Agent *audience-cohort profiles*.
- **Psychological Recommendation** (Big Five / emotional-state preference prediction) → AudienceSim, PerformanceMarketer, Personalization.
- **PersonalizationEngineerAgent** templating (name/face/voice swap) with privacy/consent audit (GDPR/CCPA via ComplianceAgent).
- **Podcast Agent** audio-first workflow (preparation → execution → ending → follow-up), reusing VO/SoundMixer/Editor.

**Tests:** profile-conditioned generation changes output measurably and traceably; personalization render-success ≥99.5% on a batch fixture; consent audit blocks an unconsented likeness; podcast workflow runs end-to-end on mocks.

**Acceptance Gate G-M11:** Personalized + audience-cohort-conditioned variants generate under consent gates; podcast archetype runs end-to-end. ✅

---

### M12 — Hardening, Scale, Security & Launch (the 100-Point Pass)

**Goal:** Take everything to production-grade. This milestone *is* the §14 100-point checklist, executed theme by theme.

**Depends on:** M0–M11.

**Build/Do:**
- **Scale:** load-test the orchestrator (concurrent productions), GPU autoscale tuning, NATS migration if Redis Streams is the bottleneck, hot/warm/archive storage tiering, LatencyOptimizer pass (caching, batching, speculative decoding).
- **Security:** secret management hardening, RBAC review, dependency CVE scan, SBOM, prompt-injection defenses on every agent that ingests external content, SafetyRedTeam full sweep.
- **Reliability:** chaos test (kill workers, drop Redis, fail a provider) → graceful degradation; backup/restore of Postgres + asset store; DR runbook.
- **Compliance:** C2PA on 100% of releasable artifacts; FTC/HIPAA/GDPR/IP checklists wired into ComplianceAgent blocking gate; audit-trail completeness.
- **Cost:** cost dashboards + budget alerts validated under realistic load; CostOptimizer Pareto frontier check.
- **Docs:** operator runbooks, on-call playbooks, architecture diagrams regenerated, `CLAUDE.md`s current.
- **Launch:** staged rollout (internal → limited → GA) with feature flags; live-smoke against real providers behind budget caps.

**Claude Code workflow:** Run `/harden <theme>` for each of the 10 themes in §14; fix every finding; only when all 100 boxes are checked is the system "done." Use extended thinking for the chaos/security analysis.

**Acceptance Gate G-M12 (FINAL):** All 100 hardening checks pass; a full **Workflow J (Feature Film)** dry-run exercising all 114 agents completes on mocks with full QC/provenance/observability; live-smoke on real providers succeeds within budget; DR runbook validated. ✅ **Ship.**

---

### 6.1 Vertical-Slice-First Strategy (why M6 sits where it does)

Building 114 agents before proving one workflow end-to-end would be the classic distributed-systems mistake: discovering an architecture flaw after 80% of the code assumes it. The plan deliberately:

1. Builds the **platform** (M0–M5) — contracts, orchestration, gateway, intelligence.
2. Punches **one thin vertical slice** (M6, Workflow A) all the way through real infra on mock gen-providers. Workflow A is chosen because it has the fewest agents and shortest runtime, so it's the cheapest possible full proof.
3. Only then scales **breadth** (M7–M9) via the factory, with the architecture already battle-tested.
4. Adds **surface** (M10 UI) and **enrichment** (M11), then **hardens** (M12).

If the M6 gate reveals an architectural problem (e.g., the handoff contract is missing a field, or Temporal↔LangGraph boundary is wrong), you fix it in the platform with 9 agents in flight — not 114. This is the single most important sequencing decision in the plan.


---

## 7. The Repeatable Pattern: One Workflow Archetype = One DAG

Each of the 10 archetypes (A–J) in [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3 becomes one LangGraph graph in `workflows/`. They share the §3.0 skeleton (Greenlight → Pre-production → Production → Post → Review/Release → Distribution → Post-launch) and differ only in which agents lead each phase and which critics gate the handoff.

**Build order of workflows:** A (M6) → C, E, B (M7) → F, G, H, I (M8) → D (M11, needs personalization) → J (M12, full-system dry-run). A workflow is "done" when its DAG runs end-to-end on mock providers, every phase gate enforces its critic set, and the final artifact carries a complete provenance chain.

---

## 8. Agent Implementation Playbook (Run For Each of the 114 Agents)

This is the exact, repeatable recipe the `/new-agent <n>` command automates. **No agent is hand-built outside this recipe** (G3).

**Inputs:** the agent's number and its rows in [`agents.md`](./agents.md) + [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §2 (Responsibility, Knowledge Distillation Source, Self-Quality Criteria, Surpass-Human Signal, Accepts Critique From, Comments On) + any deep spec.

**Steps:**
1. **Read (subagent).** `spec-reader` extracts the six fields above into a structured `AgentBrief`.
2. **Map self-quality → metrics.** Convert "Self-Quality Criteria" into concrete `MetricSpec`s with thresholds (e.g., DoP `rule_of_thirds>=τ, exposure_zone∈[III,VII], color_temp_var<=ΔK`; Colorist `deltaE<2`; SoundMixer `lufs==target, stoi>=0.85`). Many map to existing `packages/qc` validators or the Aesthetics Agent.
3. **Author the L2 rubric/constitution.** Turn "Surpass-Human Signal" + craft sources into a role constitution in `eval/rubrics/<agent>.yaml` (this is what LLM-as-judge scores against). Cite the craft authority named in the spec (Murch's Rule of Six for Editor, 12 principles for Animator, etc.).
4. **Define tools.** Allowlist only the providers/tools this agent may call (e.g., PromptEngineer → MediaGenProvider; Colorist → grade tool; FactChecker → RAG + WebResearch). Enforced by `agent-core`.
5. **Wire critique edges.** From the §4 critique matrix: `critiques_from` and `critiques_on`. ComplianceAgent edges are always blocking.
6. **Write the AgentConfig (YAML)** and register in `agents/_registry.yaml`.
7. **Author the versioned system prompt** (`agents/.../prompt.vN.md`) embedding role, constitution summary, self-refine instruction, and output schema (must emit a valid `Artifact`).
8. **TDD (subagent `test-author`):** golden-input fixtures → assert L1 schema pass, L2 rubric ≥85, correct critique emission/acceptance, tool-allowlist enforcement, metering present, provenance populated.
9. **Implement = instantiate.** `AgentFactory.build(config)` — no new code path; if you find yourself writing bespoke logic, that logic belongs in `agent-core` or a tool, not the agent.
10. **Review (subagent `code-reviewer`)** against DoD + §14 themes; fix; commit `feat(agent-<n>): <Name>`.
11. **Register in workflows** that use it; extend the relevant archetype integration test.

**Anti-patterns to reject:** an agent with no L2 rubric; an agent that calls a provider directly instead of through a tool interface; an agent that mutates another agent's artifact instead of emitting a critique; an agent whose "self-quality" is unmeasurable prose.

---

## 9. Testing & Evaluation Strategy

The system is an *evaluation engine*; its own test suite must be exemplary. Five layers:

### 9.1 Unit (per package/agent)
Pure-logic tests, fully mocked, deterministic, fast (<5s suite per package). Includes property tests (hypothesis) for contracts (serialization round-trips, DAG acyclicity, metering math).

### 9.2 Contract tests
Snapshot the JSON schema of every `packages/contracts` model. A change that removes/renames a field **fails CI** unless a version bump + ADR + `contract-guardian` sign-off exists (G1). Generated TS types must be in sync (`contracts:gen` diff check).

### 9.3 Integration (real backing services, mock gen-providers)
Run against `docker compose` (Postgres/Redis/Temporal/OpenSearch/Chroma/MinIO). Cover: DAG execution, kill-and-resume durability, event replay, gate interrupts, handoff-contract propagation across a phase, critique-bus routing, budget enforcement.

### 9.4 Behavioral / golden-set evaluation (the L1/L2/L3 mesh on the system itself)
- **Golden sets** in `eval/golden/`: frozen brief→expected fixtures per agent and per workflow. Inputs and expected structured outputs are version-controlled.
- **L2 judges are frozen + pinned** (specific model + prompt version) to keep scores stable across runs; never let a judge model float (regression-noise killer).
- **L3 AudienceSim**: ≥200 simulated personas (from Psychological Profiling, M11) + ≥20 HiTL samples; reports win-rate vs the stored human/baseline reference.
- **`EvaluationHarnessAgent` (#79)** runs these nightly and on every PR touching an agent; posts regressions to `system.alerts`.

### 9.5 Adversarial / safety (`SafetyRedTeamAgent` #80)
Continuous attacks: deepfake/likeness misuse, prompt injection via ingested web content, jailbreaks, defamation, bias. Target attack-success ≤1%. Runs nightly + pre-release.

### 9.6 E2E (UI)
Playwright journeys (M10): launch → live-monitor → critique → gate-approve → deliver, plus WebSocket reconnect and RBAC.

> **CI test pyramid:** PRs run unit + contract + the affected agent's golden L1/L2 + lint/type (minutes). Nightly runs full integration + L3 + red-team + benchmark harness + live-smoke (budget-capped).

---

## 10. Observability, Cost, Safety & Compliance Gates

### 10.1 Observability (from M2, deepened in M8/M12)
- **Tracing:** every agent run, tool call, LLM call, and gate decision is an OTel span; LangSmith captures agent-reasoning traces. A production has one trace tree from brief to delivery.
- **Metrics → Grafana:** DAG completion rate, node latency p50/p95, retry/deadlock counts, queue depth, GPU utilization, per-agent L2 score trend, escaped-defect rate.
- **Replay:** event-sourced bus + Temporal history → reconstruct any production's full decision path for debugging/audit (the "Observability & Replay" layer).
- **Structured logs:** JSON, correlated by `production_id` + `artifact_id` + `trace_id`.

### 10.2 Cost (from M3)
- Per-call metering → `budget_update` events → cost dashboard per production/agent/provider.
- Per-production **budget envelope**; hard stop + ProducerAgent escalation on breach (G6).
- **CostOptimizerAgent** keeps routing on the cost/quality Pareto frontier.
- **Live-smoke budget cap**: nightly real-provider job aborts at a fixed dollar ceiling.

### 10.3 Safety & Compliance (ComplianceAgent can BLOCK from M6)
- **ComplianceAgent (#37)** is a blocking gate on every release path: FTC, HIPAA, GDPR/CCPA, IP/likeness clearance, EU AI Act, AI-disclosure.
- **Consent chain**: any likeness/voice clone requires a verified consent record in `rights_and_consent`; AvatarDesign/VoiceClone agents cannot proceed without it.
- **C2PA**: 100% of releasable artifacts signed; downstream verifies the chain.
- **Provenance/audit**: every artifact traces back to brief + prompts + model versions + sign-offs.
- **Content-safety**: SafetyRedTeam + input-sanitization on any agent ingesting external/user content.

### 10.4 The non-negotiable release predicate
An artifact is releasable **iff**: `L1==pass AND L2>=85 AND L3>=threshold AND all(Q1..Q6) AND compliance==clear AND c2pa_signed AND budget_ok`. Encode this as a single `qc.release_ok(artifact)` function; the GateKeeperAgent calls only this.

---

## 11. CI/CD & Environments

### 11.1 Environments
- **dev** (docker-compose, mock providers, local secrets via direnv).
- **staging** (K8s, mock+limited-real providers, synthetic load).
- **prod** (K8s, real providers, full secrets via Vault, GPU pool autoscale).

### 11.2 Pipelines (GitHub Actions)
- **PR pipeline:** `make verify` (lint+type+unit) → contract-snapshot → affected-agent golden L1/L2 → build images. Required to merge.
- **Main pipeline:** full integration (compose services) → publish images → deploy staging → smoke.
- **Nightly:** full L3 + red-team + benchmark harness + dependency CVE scan + live-smoke (budget-capped).
- **Release:** tag → SBOM → staged rollout (feature-flagged) → canary → GA.

### 11.3 Conventions
- **Conventional Commits**, milestone-scoped (`feat(m7-colorist): ...`, `fix(m2-orchestrator): ...`).
- **Trunk-based** with short-lived branches; PRs small and milestone-tagged.
- **No direct pushes to main**; every change via PR with green checks + `code-reviewer` pass.
- Claude Code in headless mode (`claude -p`) may run scoped CI fix-ups inside the sandboxed runner only.

---

## 12. Data, Model & Prompt Management

- **Prompt registry:** every agent system prompt is versioned (`prompt.vN.md`); the active version is referenced by `AgentConfig` and recorded in provenance (G5). Prompt changes go through PromptOptimizer (#73) eval before promotion.
- **Model registry:** pinned model+version per agent policy; upgrades are eval-gated (run golden L2/L3 before/after; no regression allowed).
- **Seed/LoRA/style registries:** StyleTransfer (#61) and gen agents reference versioned seeds/LoRAs/reference-frame banks for reproducibility and look-consistency.
- **Golden-set governance:** golden fixtures are frozen and reviewed; changing an expected output requires justification (it may indicate a rubric drift).
- **Aesthetic profiles:** consent-governed, versioned `AestheticProfile`s (per the Aesthetics Agent spec) stored and signed; audience-cohort profiles link to Psychological Recommendation.
- **Eval datasets:** VBench/EvalCrafter/MT-Bench/FVD/CLIP-T runners wrapped behind `EvalToolProvider`; benchmark baselines tracked over time by BenchmarkResearch (#72) + EvaluationHarness (#79).

---

## 13. Risk Register & Mitigations

| # | Risk | Likelihood | Impact | Mitigation (where in plan) |
|---|------|-----------|--------|----------------------------|
| R1 | Architecture flaw discovered after broad agent build | Med | High | Vertical slice M6 before breadth (G2, §6.1) |
| R2 | Contract drift across 114 agents | High | High | Frozen contracts + `contract-guardian` + snapshot tests (§5, §9.2) |
| R3 | Runaway LLM/gen cost | High | High | Metering+budget gates from M3; mock providers in CI; live-smoke cap (§10.2) |
| R4 | Temporal↔LangGraph boundary confusion | Med | High | ADR-003 + kill/resume tests in M2 (§6 M2) |
| R5 | LLM-judge score noise destabilizes gates | High | Med | Frozen, pinned judges + golden sets (§9.4) |
| R6 | Reward hacking / "pretty slop" from aesthetic reward | Med | Med | Aesthetics Agent anti-hack layer; ensemble disagreement; HiTL on low confidence |
| R7 | Provider outage/rate-limit stalls productions | Med | Med | Provider abstraction + Router fallback + retries (§3.3, RouterAgent) |
| R8 | Consent/IP violation in generated likeness/voice | Low | Critical | ComplianceAgent blocking gate + consent chain + C2PA (§10.3) |
| R9 | Context bloat causes Claude Code regressions during build | High | Med | `/clear`+`/compact`+subagents+per-package CLAUDE.md (§2.8) |
| R10 | Prompt injection via ingested web/research content | Med | High | Input sanitization + SafetyRedTeam + least-tool-privilege (§10.3, §9.5) |
| R11 | Scale bottleneck on Redis Streams | Med | Med | NATS migration path designed in from M2 (§3.2, M12) |
| R12 | Non-deterministic tests flake CI | Med | Med | Deterministic mocks + pinned seeds/judges; quarantine flaky tests (§9) |
| R13 | Scope creep (role inflation: new agents that close no real gap) | Med | Med | Reject per workflow-doc rule §1.1 working-rule #4; ADR required for any agent beyond the 114 |


---

## 14. The 100-Point Hardening Checklist ("Rethink 100 Times", Operationalized)

The system is **not done** until all 100 boxes are checked. Organized as **10 themes × 10 checks**. Run each theme with `/harden <theme>` in M12 (and re-run any theme whose surface changed). This is the literal, structural form of the "rethink 100 times" mandate. Maintain the live state in `BUILD_PROGRESS.md`.

### Theme 1 — Contracts & Schema Integrity (1–10)
1. Every inter-agent message is a typed `packages/contracts` model; zero ad-hoc dicts on the bus.
2. Handoff `Artifact` populated at every phase boundary (no empty required fields).
3. Contract snapshot tests guard all models; removal/rename requires version bump + ADR.
4. Generated TS types are in sync with Pydantic (CI diff check green).
5. `parent_assets` always form an acyclic provenance DAG.
6. CritiqueMessage severity semantics enforced (blocker halts, major→3-iter refine, minor/nit→memory).
7. Event-bus payloads validate against `events.py`; invalid events are rejected, not silently dropped.
8. Versioning is copy-on-write; no in-place artifact mutation anywhere.
9. `qc_status` and `provenance_manifest` are never null on a releasable artifact.
10. No package redefines a shared contract locally (grep proves single source).

### Theme 2 — Orchestration & State (11–20)
11. Kill-and-resume: worker crash mid-DAG resumes from checkpoint with no lost/duplicate work.
12. Fan-out/fan-in correctness verified under concurrency.
13. Deadlock detector trips on cyclic/blocked plans; no silent hangs.
14. SLA timers + timeouts on every node; stalls escalate to HiTL.
15. Temporal↔LangGraph boundary documented (ADR-003) and respected in code.
16. Gate interrupts truly block until an external signal; no race that advances early.
17. Idempotency keys prevent double-execution on retry.
18. Event sourcing replays a full production deterministically.
19. Backpressure handled when the bus/queue saturates.
20. Graceful degradation when a backing service (Redis/Postgres/OpenSearch) is briefly unavailable.

### Theme 3 — Agent Correctness (21–30)
21. All 114 agents instantiated via the factory (no bespoke loops).
22. Each agent passes L1 schema conformance on its golden inputs.
23. Each agent scores ≥85 on its L2 rubric (frozen judge).
24. Critique edges match the §4 matrix exactly (no missing/extra edges).
25. Tool allowlist enforced; an agent calling a disallowed tool fails closed.
26. Self-Refine caps at `max_refine_iters`; runaway loops impossible.
27. Reflexion memory writes/reads verified; lessons persist across retries.
28. No agent mutates another's artifact; it emits a critique instead.
29. Every agent's self-quality criteria are *measurable* metrics, not prose.
30. ComplianceAgent BLOCK edges verified on every release path.

### Theme 4 — Quality Mesh (31–40)
31. `qc.release_ok()` is the single release predicate; GateKeeper calls only it.
32. L1 deterministic validators cover codec/aspect/duration/frame-rate/LUFS/captions.
33. L2 judges are pinned (model+prompt version); score variance within tolerance across reruns.
34. L3 AudienceSim uses ≥200 personas + ≥20 HiTL; win-rate computed correctly.
35. Q1–Q6 delivery mesh each implemented and gating.
36. Continuity (Q4) detects identity/wardrobe/prop drift via `identity_hash`.
37. Aesthetic scoring returns decomposed vector + `hack_likelihood`; low confidence escalates.
38. Reward-hacking defenses active (ensemble disagreement, variance monitoring).
39. Accessibility (WCAG 2.2 AA min) gated for any human-facing output.
40. A seeded defect is reliably caught and blocked before release.

### Theme 5 — Cost & Performance (41–50)
41. Every LLM/gen call metered; cost matches provider price sheets on fixtures.
42. Per-production budget envelope enforced with hard stop + escalation.
43. CostOptimizer keeps routing on the cost/quality Pareto frontier.
44. Response/embedding caching reduces redundant calls (cache-hit test).
45. p95 node latency within target under nominal load.
46. GPU pool autoscales under queued-render load; scales down when idle.
47. Storage tiering (hot/warm/archive) configured and tested.
48. Batch/interactive workloads separated; batch never starves interactive.
49. Live-smoke real-provider job aborts at its budget ceiling.
50. Load test: N concurrent productions complete within SLA.

### Theme 6 — Safety, Security & Compliance (51–60)
51. SafetyRedTeam attack-success ≤1% across the attack taxonomy.
52. Prompt-injection defenses on every agent ingesting external/user content.
53. Consent chain verified before any likeness/voice generation.
54. C2PA signs 100% of releasable artifacts; verification passes downstream.
55. FTC/HIPAA/GDPR-CCPA/IP/EU-AI-Act checklists wired into ComplianceAgent.
56. Secrets never in repo/logs; secret-scan hook + CI gate active.
57. RBAC enforced on all gateway mutations (gate approve, retry, config).
58. Dependency CVE scan + SBOM produced each release; criticals block.
59. AI-disclosure applied where required (avatar/synthetic content).
60. PII handled with generic placeholders in samples; real PII only in consented project data.

### Theme 7 — Observability & Operability (61–70)
61. One trace tree per production (brief→delivery) in LangSmith/Tempo.
62. Grafana dashboards: completion rate, latency, retries, deadlocks, queue depth, GPU, L2 trend, escaped-defect rate.
63. Logs are structured JSON correlated by production/artifact/trace id.
64. Any production fully replayable from the event log + Temporal history.
65. Alerts on `system.alerts` fire for regressions, budget breach, safety, SLA.
66. EvaluationHarness regression detection latency <1h.
67. Runbooks exist for top failure modes; on-call playbook current.
68. Backup/restore of Postgres + asset store verified.
69. DR drill: full-region failure recovery within RTO/RPO targets.
70. Feature flags allow safe staged rollout + instant rollback.

### Theme 8 — Frontend & Human Experience (71–80)
71. UI launches/monitors/critiques/approves/delivers Workflow A end-to-end.
72. WebSocket live updates are <50ms-class; DAG node states accurate.
73. No agent→UI direct calls (all via event bus + gateway).
74. WebSocket reconnect restores full state without duplication.
75. Gate Approval Dialog signs C2PA on approval; rejection routes feedback correctly.
76. Budget/quality dashboards reflect backend truth in real time.
77. Playwright E2E covers the critical journeys; green in CI.
78. RBAC denies unauthorized actions in the UI and gateway.
79. `RETHINK_100_IMPROVEMENTS.md` items triaged; criticals addressed.
80. Production-scale discovery adapts the DAG to project complexity (S-tiers).

### Theme 9 — Build Process & Claude Code Hygiene (81–90)
81. Root + per-package `CLAUDE.md` current and lean.
82. Subagents (`spec-reader`, `contract-guardian`, `test-author`, `test-runner`, `code-reviewer`, `agent-factory-smith`) defined and used.
83. Slash commands (`/milestone`, `/new-agent`, `/verify`, `/contract-check`, `/gate`, `/adr`, `/harden`) defined.
84. Hooks enforce auto-format, protected-path block, type/lint gate, secret scan.
85. `DECISIONS.md` has an ADR for every non-obvious choice (incl. ADR-001/002/003).
86. `BUILD_PROGRESS.md` reflects true milestone + hardening state.
87. Every commit is Conventional + milestone-scoped; no secrets/debug cruft.
88. `make verify` green at every commit; CI required checks enforced.
89. Context hygiene practiced (`/clear` between tasks; no contradictory stale context).
90. TDD honored: tests precede implementation across the codebase (spot-audit git history).

### Theme 10 — End-to-End System Validation (91–100)
91. All 10 workflow archetypes (A–J) run end-to-end on mock providers.
92. Workflow J (Feature Film) dry-run exercises all 114 agents successfully.
93. Provenance chain verifiable from any final artifact back to the brief.
94. Multi-channel delivery (theatrical/streaming/broadcast/archive + marketing) all Q6-valid.
95. Post-launch telemetry flows into retraining tickets (RLAIF loop closes).
96. Optimization Agent demonstrably improves a workflow metric over a baseline.
97. GCA↔Aesthetics generate↔evaluate loop produces measurably better candidates.
98. Research/FactChecker path produces only source-graded, cited claims.
99. Live-smoke on real providers completes within budget and passes QC.
100. A cold reader (new engineer) can build from this plan + specs without tribal knowledge.

> **Completion rule:** "Done" = 100/100 checked in `BUILD_PROGRESS.md`, with evidence (test name, dashboard link, or artifact id) beside each.

---

## 15. Sequencing Summary & Critical Path

### 15.1 Milestone → Acceptance Gate → Spec mapping

| M | Milestone | Acceptance Gate (one-line) | Primary specs |
|---|-----------|----------------------------|---------------|
| M0 | Bootstrap + Claude config | Clean clone → `make verify` green; `.claude/` live | SYSTEM_REFERENCE §11 |
| M1 | Agentic RAG | precision@5 ≥0.9 on golden corpus; graded citations | agentic_rag |
| M2 | Orchestration runtime | 3-node DAG survives worker kill; typed events; C2PA | workflow §1.2; ui/architecture |
| M3 | LLM gateway + Router + Cost | every call metered/routed/version-tagged; budget stop | llm_usage; agents §9 |
| M4 | Research + Coding harness | cited dossier in RAG; conventions enforced | research_*; coding_agent |
| M5 | Intelligence layer | 6 reasoning services pass golden behavioral tests | intent/gca/optimization/goal/cps/aesthetics |
| M6 | Factory + Vertical Slice A | `make e2e-workflow-a` signed deliverable on mocks | workflow §3.1 |
| M7 | Production agents 1–52 | all 52 green on L1+L2+critique; 3 more workflows E2E | agents §1–8 |
| M8 | Meta-agents 53–80 + QC | all 80 live; full L1/L2/L3+Q1–Q6; red-team+harness nightly | workflow §2.9, §5 |
| M9 | Support 81–114 + delivery | 4 delivery branches Q6-valid; learning loop closes | agents §10; workflow §3.0 |
| M10 | UI + gateway + WS | human runs Workflow A fully in browser, live | all ui/ |
| M11 | Enhancement | personalized/cohort variants under consent; podcast E2E | psych_*; podcast |
| M12 | Hardening + launch | 100/100 checks; Workflow J all-114 dry-run; live-smoke | §14 |

### 15.2 Critical path
`M0 → M2 → M3 → M5 → M6 → M7 → M8 → M9 → M12`. M1 feeds M2/M4; M4 supports M8; **M10 can parallelize from M3** in a worktree; M11 slots after M9. The single highest-leverage checkpoint is **G-M6** (vertical slice) — it converts architectural risk into a proven foundation.

### 15.3 What "full effort" means here
Depth over breadth at the start (platform + contracts + one perfect slice), then mechanical breadth via the factory, then recursive quality (the system judges videos to L1/L2/L3 — so it must judge *itself* to L1/L2/L3), then a literal 100-point hardening sweep. The plan is engineered so that a flaw is cheapest to fix exactly when it is most likely to be found.


---

## 16. Appendices (Copy-Paste Starters for Claude Code)

### Appendix A — Root `CLAUDE.md` Template

```markdown
# VA-Agent-Swarm — Project Memory (CLAUDE.md)

## What this is
A 114-agent video-production multi-agent system. Specs live in `study/`.
Authoritative map: study/SYSTEM_REFERENCE.md. Build plan: study/system_build_plan.md.

## Golden Rules (NEVER violate)
G1 Contracts before code — never edit packages/contracts without an ADR + contract-guardian.
G2 Vertical slice before breadth (Workflow A proves the platform).
G3 Every agent = BaseAgent instance via the factory; no bespoke agent loops.
G4 Agents never talk to the UI; publish to the event bus.
G5 Determinism: pin seeds/model/prompt versions; record in provenance.
G6 Cost & safety are gates from M3/M6, not afterthoughts.
G7 External gen-models are always behind a Provider interface; CI uses mocks.

## Stack (pinned — change only via ADR)
Python 3.12 + uv | TS5/React19/Next15 + pnpm/turbo | LangGraph + Temporal |
Redis Streams | Postgres + SQLModel/Alembic | S3/MinIO | Chroma→Pinecone |
LightRAG/OpenSearch | FastAPI | litellm | LangSmith + OTel/Grafana | C2PA | Docker→K8s.

## Commands
make verify  # lint + type + unit (MUST be green before commit)
make test    # unit ; make test-int # integration on docker-compose
make up/down # backing services ; make contracts:gen # regen TS types
make e2e-workflow-a  # the vertical-slice gate

## Where things live
Contracts: packages/contracts | Agent base: packages/agent-core | Factory: packages/agent-factory
Agents: agents/{production,meta,support,crosscutting} + agents/_registry.yaml
Workflows: workflows/ | QC: packages/qc | Rubrics: eval/rubrics | Golden sets: eval/golden

## Working rules
- Plan mode first for any change >2 files or touching a contract.
- TDD always: failing test before code.
- Use subagents for reading specs / running tests / reviewing diffs.
- /clear between unrelated tasks. Update BUILD_PROGRESS.md when a task completes.
- One ADR per non-obvious decision in DECISIONS.md.
```

### Appendix B — Subagent Definitions (`.claude/agents/*.md`)

```markdown
---
name: spec-reader
description: Reads a study/*.md spec and returns a tight structured summary + exact requirements/acceptance criteria for the current task. Use at the top of every milestone.
tools: Read, Grep, Glob
---
You extract, you do not implement. Given a spec path and a task focus, return:
1) One-paragraph purpose. 2) The exact requirements as a checklist.
3) Inputs/outputs/contracts referenced. 4) Acceptance criteria/metrics with thresholds.
5) Open questions/ambiguities. Keep under 400 words. Quote thresholds verbatim.
```

```markdown
---
name: contract-guardian
description: Verifies a staged diff does not violate or silently fork packages/contracts. Run before any commit touching contracts. MUST be used proactively.
tools: Read, Grep, Bash(git diff:*)
---
Fail the check if: a contract field is removed/renamed without a version bump + ADR;
a shape is redefined outside packages/contracts; generated TS types are stale;
an event/critique/artifact uses an ad-hoc dict. Report PASS/FAIL + exact violations.
```

```markdown
---
name: code-reviewer
description: Reviews a diff against the milestone DoD, the §14 hardening themes, and style. Use after implementing, before commit.
tools: Read, Grep, Bash(git diff:*)
---
Return findings as blocker/major/minor/nit with file:line + fix. Check: tests-first,
types strict, no direct provider calls, no UI calls from agents, allowlist respected,
provenance populated, no secrets, DoD met. Block on any blocker/major.
```

> Also create `test-author`, `test-runner`, and `agent-factory-smith` analogously (scoped tools, single responsibility).

### Appendix C — Slash Command Definitions (`.claude/commands/*.md`)

```markdown
---
# .claude/commands/milestone.md
description: Load a milestone from the build plan and start it correctly.
argument-hint: <M0..M12>
---
1) Read the milestone $ARGUMENTS section of study/system_build_plan.md.
2) Invoke spec-reader on each spec it references.
3) Enter plan mode. Draft: task breakdown, files to create/modify, test list,
   and the milestone Acceptance Gate as a checklist. 4) Stop for confirmation. Do NOT edit yet.
```

```markdown
---
# .claude/commands/new-agent.md
description: Implement one agent via the Agent Implementation Playbook (§8).
argument-hint: <agent number 1-114>
---
Run §8 for agent $ARGUMENTS: spec-reader → metrics → rubric (eval/rubrics) →
tools allowlist → critique edges (§4 matrix) → AgentConfig + registry → versioned prompt →
test-author writes failing tests → AgentFactory.build → code-reviewer → commit feat(agent-$ARGUMENTS).
```

```markdown
---
# .claude/commands/harden.md
description: Run one theme of the 100-point hardening checklist (§14).
argument-hint: <theme 1-10 or name>
---
Audit the codebase against the 10 checks in §14 theme $ARGUMENTS. For each: PASS/FAIL +
evidence (test name / dashboard / artifact id) or the exact fix needed. Update BUILD_PROGRESS.md.
```

> Also: `/verify` (run `make verify`, summarize failures), `/contract-check` (invoke contract-guardian on staged diff), `/gate <Q1..Q6|L1..L3>` (run a QC layer + report), `/adr <title>` (append dated ADR).

### Appendix D — `.claude/settings.json` (permissions + hooks)

```json
{
  "permissions": {
    "allow": [
      "Bash(make:*)", "Bash(pytest:*)", "Bash(uv:*)", "Bash(pnpm:*)",
      "Bash(git status)", "Bash(git diff:*)", "Bash(git add:*)", "Bash(git commit:*)",
      "Bash(docker compose:*)"
    ],
    "deny": [
      "Bash(git push --force:*)", "Bash(rm -rf:*)", "Read(.env)", "Read(**/secrets/**)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "scripts/hooks/format_changed.sh" }] }
    ],
    "PreToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "scripts/hooks/protect_contracts.sh" }] },
      { "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "scripts/hooks/secret_scan.sh" }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "make verify || echo 'GATE RED — fix before ending turn'" }] }
    ]
  }
}
```

> `protect_contracts.sh` exits non-zero (blocking the edit) when the target is under `packages/contracts/**` and the session lacks an explicit "contract change" + ADR marker — enforcing G1 mechanically.

### Appendix E — Definition of Done (pin in every PR template)

- [ ] Tests written before code; all green; `make verify` passes.
- [ ] Contracts unchanged, or changed via ADR + contract-guardian PASS.
- [ ] code-reviewer: no blocker/major findings.
- [ ] Milestone Acceptance Gate criteria met (evidence in `BUILD_PROGRESS.md`).
- [ ] Conventional, milestone-scoped commit; no secrets/cruft/untracked TODOs.
- [ ] Package `CLAUDE.md`/README updated if public surface changed.
- [ ] Relevant §14 hardening checks re-validated if surface changed.

### Appendix F — Glossary

| Term | Meaning |
|------|---------|
| **Handoff Contract** | The `Artifact` manifest carried between phases (§5.1). |
| **CritiqueMessage** | Typed inter-agent feedback (§5.2). |
| **L1/L2/L3** | Spec / Rubric / Preference quality layers (§5.5). |
| **Q1–Q6** | Six-pass delivery QC mesh (§5.5). |
| **Vertical slice** | One workflow built end-to-end before breadth (M6, G2). |
| **Factory** | Turns an `AgentConfig` into a runnable `BaseAgent` (§8). |
| **Frozen judge** | Pinned model+prompt LLM evaluator for stable scores (§9.4). |
| **Release predicate** | `qc.release_ok()` — the single gate for releasability (§10.4). |
| **GCA / SSOR** | General Creative Agent / Strategic Sparse Outlier Recombination. |
| **DIA** | Deep Intent Analysis (brief→structured intent). |
| **C2PA** | Provenance signing standard applied to every artifact. |

---

## 17. Final Word

This plan is engineered around one conviction: **build the platform and one perfect slice before the breadth, then let a factory and a recursive quality mesh do the scaling.** Contracts are frozen first so 114 agents cannot diverge. The vertical slice (M6) converts the system's biggest risk — an architecture flaw discovered late — into a cheap, early, provable checkpoint. Quality is recursive: the system that judges video to L1/L2/L3 must pass L1/L2/L3 on itself. And the "rethink 100 times" mandate is not rhetoric — it is the literal 100-point gate in §14 that stands between "works on my machine" and "production".

Claude Code: start at **M0**, run `/milestone M0`, and do not advance a milestone until its Acceptance Gate is green and logged. Build it like the system it is — planned, tested, observed, and signed.

**End of Build Plan.**
*Save as `study/system_build_plan.md`. Companion to `SYSTEM_REFERENCE.md`. Begin at M0.*
