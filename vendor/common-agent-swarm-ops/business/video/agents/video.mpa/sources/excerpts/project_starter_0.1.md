  
```
# project_starter.md: Build Ultimate Coding Agent Harness Starter Project


```
```
**Goal**  
Create a clean, production-ready **initial project** (repo + setup scripts + configs) called `ultimate-agent-harness-starter` (or your preferred name) that bootstraps a powerful, cross-tool coding agent environment.  

It combines the **best elements** from the top-ranked GitHub coding agent project settings/harnesses (as of June 2026), with **ECC as the primary foundation** on any overlaps. The result should be a one-command (or few-command) installable starter that gives immediate high-productivity agentic workflows for Claude Code, Cursor, Codex, OpenCode, Gemini CLI, and similar tools.

**Context & Principles**  
- **Spec-Driven Development (SDD)** first: Clear specs drive everything.  
- Prioritize **highest-ranked** items on feature/skill/rule overlap (ECC #1 > Karpathy rules #2 > claude-mem #3 > shanraisshan best-practice #4 > antigravity-awesome-skills #5, etc.).  
- Keep it **portable, minimal-Docker where possible, local-first**, with excellent security, memory, and token efficiency.  
- Output must be **agent-friendly**: clear phases, checklists, acceptance criteria, and hooks for critic/review agents.  
- Support iterative refinement (plan → implement → review → improve loops).  
- Target users: Solo developers, small teams, or power users building custom AI coding workflows (aligns with harness engineering + N1ch01as-style meta-systems).

**Success Criteria**  
- New project folder initializes in < 5 minutes with one main script.  
- ECC fully installed + configured as core harness.  
- Karpathy behavioral rules active by default.  
- Persistent memory (claude-mem or equivalent) enabled.  
- High-value skills from top libraries selectively merged (no duplication).  
- Best-practice configs, hooks, rules, and example workflows included.  
- Security baseline (AgentShield or equivalent) active.  
- Clear docs + task.md for further extension.  
- Works cross-platform (macOS/Linux/Windows where possible) and with multiple agents.  
- Includes quality gates (lint, tests, review prompts).
- **All supported coding agents share the exact same curated skills, rules, and hooks** via automated or documented synchronization from a single source of truth.

---

## Cross-Agent Skill & Rule Synchronization Layer (New Core Feature)

**Objective**: Ensure **every coding agent** (Claude Code, Cursor, Codex, OpenCode, Gemini CLI, etc.) "knows" the **same high-quality skills and rules** by keeping their respective config folders/files in sync from one central source of truth.

This solves the common problem where different agents have fragmented or outdated skills. We prioritize **ECC's cross-harness approach** first, then add lightweight adapters/sync scripts for full coverage.

**Design Principles** (ECC-first):
- Single source of truth: `./skills/`, `./rules/`, `./hooks/`, and `./mcp-configs/` in the repo root.
- Prefer symlinks where the target agent supports it (fast, always up-to-date).
- Fall back to smart copy + light transformation for agents with different folder structures or file formats.
- Leverage ECC's built-in cross-tool compatibility and adapters as much as possible.
- Keep the sync process simple, scriptable, and safe (idempotent, with backup/restore).

**Updated Folder Structure** (add these):

```
ultimate-agent-harness-starter/ ├── skills/ # ← Single source of truth (Markdown skills) ├── rules/ # ← Single source of truth (behavioral + coding standards) ├── hooks/ # ← Shared automation hooks ├── mcp-configs/ # ← Shared MCP definitions ├── .claude/ # Claude Code (skills, commands, hooks, rules) ← synced ├── .cursor/ # Cursor rules & settings ← synced/adapted ├── agents/ # Custom sub-agents ├── scripts/ │ ├── sync-skills.sh # ← Main sync script (or Node.js equivalent) │ ├── sync-to-claude.sh │ ├── sync-to-cursor.sh │ └── … ├── docs/ └── …  
```
**Tasks to Implement Synchronization**:
1. [ ] Create central `skills/`, `rules/`, `hooks/`, and `mcp-configs/` as the **authoritative source**.
2. [ ] Build or adapt a sync script (`scripts/sync-skills.sh`):
   - For **Claude Code** (`.claude/`): Copy or symlink skills/commands/hooks/rules. Use ECC's plugin/marketplace patterns where possible.
   - For **Cursor**: Generate or update `.cursor/rules/` or relevant config files from central `rules/`.
   - For **other agents** (Codex, OpenCode, Gemini CLI, etc.): Create appropriate root files (e.g., `AGENTS.md`, `CLAUDE.md` aggregates, or tool-specific folders) by combining central content + ECC adapters.
   - Support both **full sync** and **selective** (e.g., only planning + review skills).
   - Make it idempotent and safe (dry-run mode, conflict detection).
3. [ ] Integrate with ECC's existing cross-harness features and MCP configs first (highest priority).
4. [ ] Add a `sync` command or npm script so users/agents can run `npm run sync` or `./scripts/sync-skills.sh` after any skill update.
5. [ ] Document the sync process clearly in `docs/installation.md` and `docs/usage.md`.
6. [ ] Include a `.claude/commands/sync-skills.md` (or similar) so agents can trigger sync themselves.
7. [ ] Add version pinning or manifest (`skills/manifest.json`) so the same skill versions are used everywhere.
8. [ ] Test sync across at least Claude Code + Cursor + one other agent.

**Acceptance Criteria**:
- Updating a skill in the central `./skills/` folder and running the sync script instantly makes it available to all supported agents.
- No manual copying between folders required.
- Agents behave consistently because they reference the same curated content (prioritizing ECC + Karpathy + best practices).
- Sync is fast, safe, and documented.

This layer makes the entire starter **truly portable and consistent** across your coding agent stack.

---

## Self-Evaluation & Critic Routine (Agent Self-Quality Assessment) — Research-Enhanced

**Objective**: Add a built-in **routine** so the coding agent can **evaluate its own output quality** (self-critique / self-review). This creates a closed-loop improvement system: plan → implement → self-evaluate → refine.

This section is significantly strengthened based on deep research from xAI (Grok multi-agent capabilities, Grok Build agentic coding focus, transparent/auditable reasoning) and high-quality 2025–2026 research (Reflexion, Self-Refine, SAGE multi-agent self-evolution, SCALAR Structured Critic–Actor Loop, human-in-the-loop self-improvement frameworks, context folding/memory architectures).

**Research-Backed Design Principles**
- **Multi-agent critic patterns** (xAI Grok Multi-Agent + SAGE): Use specialized roles (Actor/Solver + Critic/Challenger + optional Judge) that can work in parallel. Each sub-agent shows its reasoning for full auditability and transparency.
- **Structured self-critique** (SCALAR, Reflexion, Self-Refine): Move beyond vague feedback. Use explicit verification of preconditions, state tracking, rubric scoring, and episodic memory of past reflections/critiques.
- **Human-in-the-loop safety** (strong research consensus): All high-impact changes require human confirmation. Optional human guidance when domain knowledge evolves rapidly.
- **Memory & context management**: Support hierarchical summaries, reflection storage, and context folding for long-horizon tasks (enhancing claude-mem with ideas from AgentFold / Recursive Language Models research).
- **Transparency & auditability** (core xAI philosophy): Every sub-agent reasoning step, critique, and decision is logged and reviewable.
- **ECC-first + Research layer**: Start with ECC’s existing review/critique capabilities as the foundation, then layer on stronger multi-agent critic loops and structured reflection.

**Enhanced Dimensions for Self-Evaluation** (rubric)
1. **Correctness & Functionality** (with explicit precondition and state verification)
2. **Simplicity & Karpathy Alignment**
3. **Spec / SDD Adherence**
4. **Security & Safety**
5. **Performance, Efficiency & Token Usage**
6. **Maintainability & Clarity**
7. **Reasoning Quality & Auditability** (new dimension — transparency and verifiability of thought process)
8. **Self-Improvement Potential** (how actionable the critique is for refinement)

**Core Routine Flow** (Actor → Multi-Agent Critic → Refine + Memory loop)
- **Actor/Solver**: Generates the implementation or solution using ECC skills + Karpathy rules.
- **Critic/Challenger** (can be multi-agent): Runs structured self-critique using the enhanced rubric. Can spawn parallel sub-agents for deeper analysis on different dimensions (e.g., one for security, one for simplicity). Produces scores + specific issues + concrete, actionable improvement suggestions.
- **Reflection Storage**: Critiques, lessons learned, and successful patterns are stored in episodic memory (build on claude-mem or add dedicated structured reflection store with hierarchical summaries).
- **Refine Loop**: Actor uses the critique + stored reflections to improve the output. Supports multiple iterations with intelligent context management.
- **Human Confirmation Gate**: High-impact suggestions (especially skill/rule changes) go through the human confirmation workflow.
- **Full Audit Log**: All reasoning traces, critiques, and decisions are recorded for transparency and later review (xAI-style auditability).

**Why This Matters**
- Prevents “vibe coding” drift.
- Enforces spec adherence (SDD).
- Catches issues early (correctness, security, complexity, token waste, maintainability).
- Makes the agent more autonomous and reliable over time.

**Design (ECC-first + Extensible)**
- Central critic skill(s) in `./skills/critic/` (or reuse/extend ECC’s existing review/critique capabilities).
- Structured self-evaluation prompt/template that outputs:
  - Overall quality score (e.g., 1–10 or rubric-based)
  - Breakdown across dimensions (Correctness, Simplicity/Karpathy alignment, Spec adherence, Security, Performance, Maintainability, Token efficiency)
  - Specific issues found
  - Concrete improvement suggestions (as new tasks or diff recommendations)
- Can be triggered:
  - Automatically via post-completion hook
  - Manually with `/self-review` or `/critic` command
  - As part of multi-step workflows (after implementing a feature spec)
- Output stored alongside the work (e.g., `review.md` or appended to `task.md` / `status.md`)
- Feeds back into the loop (agent can then refine based on its own critique)

**Dimensions for Self-Evaluation** (customizable rubric)
1. **Correctness & Functionality** — Does it meet the spec/task requirements? Tests pass?
2. **Simplicity & Karpathy Alignment** — Minimal, surgical changes? No unnecessary abstractions?
3. **Spec / SDD Adherence** — Stays true to the original specification and task breakdown?
4. **Security & Safety** — No obvious vulnerabilities, secrets, or unsafe patterns?
5. **Performance & Efficiency** — Reasonable complexity and token usage?
6. **Maintainability & Clarity** — Clean, well-documented, follows project rules?
7. **Overall Confidence** — How confident is the agent in this output?

**Tasks to Implement**
1. [ ] Create or adapt a core **critic / self-review skill** in `./skills/critic/self-review.md` (start with ECC’s review capabilities as base, enhance with Karpathy + best-practice patterns).
2. [ ] Define a reusable **self-evaluation prompt template** (in `rules/` or `skills/critic/`) that agents can invoke.
3. [ ] Add a **slash command** (e.g., `/self-review` or `/critic`) in `.claude/commands/` that triggers structured self-evaluation on the current context or last changes.
4. [ ] Create a **post-completion hook** that optionally runs self-review after significant code changes or task completion.
5. [ ] Make the routine output structured data (Markdown + optional JSON) that can be parsed by other agents or scripts.
6. [ ] Integrate with existing orchestration (e.g., after dmux parallel work or feature implementation from a spec).
7. [ ] Add example usage in `docs/usage.md` and a sample `examples/self-review-workflow/`.
8. [ ] Allow customization of the rubric (e.g., project-specific weights or extra dimensions like accessibility, i18n).
9. [ ] Ensure the critic routine itself can be self-evaluated (meta level) for continuous improvement of the harness.

**Acceptance Criteria**
- The agent can run a self-evaluation on its own recent work and produce a clear, actionable critique.
- Self-review can be triggered manually or automatically via hook.
- Output includes scores + concrete improvement tasks that can be fed back into the workflow.
- Uses highest-ranked sources first (ECC review skills + Karpathy principles + best practices).
- Becomes a standard quality gate in the starter’s workflows.

This routine turns the coding agent from a one-shot generator into a **self-improving system** — a key characteristic of advanced harness engineering.

---

## Skill Lifecycle: Auto-Suggest Add / Update / Remove with Human Confirmation

**Objective**: Enable the system to **automatically suggest** adding new skills, updating existing ones, or removing low-value/outdated skills — but **never apply changes without explicit human confirmation**. This creates a safe, controlled self-evolution loop for the skill set.

This builds directly on the Self-Evaluation & Critic Routine and the central `skills/` source of truth.

**Core Workflow (Human-in-the-Loop)**
1. **Analysis Phase** (triggered by critic, periodic review, or after completing significant work):
   - Agent analyzes current skill usage, quality scores from self-reviews, relevance to recent tasks, duplication, or gaps.
   - Uses high-ranking sources (ECC patterns first, then best-practice insights).
2. **Suggestion Generation**:
   - Produces clear, structured suggestions:
     - **Add**: New skill proposal (name, purpose, source or draft content, why it's valuable).
     - **Update**: Specific improvements to an existing skill (with diff or before/after summary).
     - **Remove**: Reason for removal (low usage, superseded, quality issues) + impact assessment.
   - Suggestions are saved to a `suggestions/` folder or `pending-skill-changes.md` with unique IDs.
3. **Human Review & Confirmation**:
   - Human reviews the suggestions (via file, dashboard, or agent command like `/review-suggestions`).
   - Human confirms, rejects, or modifies (e.g., edits the suggestion file or replies with approval).
   - Only confirmed items proceed.
4. **Safe Application**:
   - After confirmation, the change is applied to the central `skills/` (and `rules/` if relevant).
   - The Cross-Agent Sync Layer then propagates the update to all agents' folders (`.claude/`, `.cursor/`, etc.).
5. **Audit & Rollback**:
   - All changes are logged with timestamp, reason, and human approver.
   - Easy rollback via git or a dedicated undo mechanism.

**Design Principles**
- **Never auto-apply** — human confirmation is mandatory for any add/update/remove of skills.
- **ECC-first**: Leverage ECC’s continuous learning / instinct promotion patterns where possible, then extend with explicit suggestion + confirmation.
- **Transparent & Auditable**: Every suggestion includes clear rationale, expected benefit, and risk/impact.
- **Non-blocking**: Suggestions don’t interrupt work; they are collected and reviewed periodically or on demand.
- **Extensible**: The same pattern can later apply to rules, hooks, or even project-level improvements.

**Tasks to Implement**
1. [ ] Create a **suggestion generator skill** (or extend the critic routine) that can propose add/update/remove actions based on analysis.
2. [ ] Define a standard **suggestion format** (Markdown template with sections: Action, Skill Name, Rationale, Impact, Proposed Content/Diff, Confidence).
3. [ ] Add storage for pending suggestions (`suggestions/` folder + manifest or `pending-skill-changes.md`).
4. [ ] Create slash commands:
   - `/suggest-skills` — trigger analysis and generate new suggestions.
   - `/review-suggestions` — list pending suggestions with details.
   - `/approve-suggestion ` or `/confirm-changes` — human confirmation step.
5. [ ] Integrate with the Self-Evaluation routine so strong critiques can automatically trigger relevant suggestions.
6. [ ] After human confirmation, automatically apply the change to central `skills/` and trigger the sync layer.
7. [ ] Add logging/audit trail for all confirmed changes.
8. [ ] Document the full workflow in `docs/usage.md` with examples.
9. [ ] Make the suggestion system itself self-evaluable (meta-critic).

**Acceptance Criteria**
- The agent can generate clear, actionable suggestions for adding, updating, or removing skills.
- No skill is ever added, updated, or removed without explicit human confirmation.
- Confirmed changes are safely applied to the central source of truth and propagated via the sync layer.
- Full audit trail exists.
- Workflow feels natural and non-intrusive (agent proposes, human decides, system applies).

This completes a powerful **safe self-improvement loop** for the entire harness while keeping the human firmly in control — exactly the kind of robust, production-grade design that advanced coding agent setups need.

---

## Phase 0: Research & Final Selection (High-Level, Do Once)

**Objective**: Confirm latest versions and resolve any overlaps using ranking priority.

**Tasks**:
1. [ ] Verify current top repos (use web search or direct GitHub):
   - ECC (affaan-m/ECC) – primary harness (skills, agents, hooks, rules, security, MCP).
   - Karpathy rules (forrestchang/andrej-karpathy-skills or multica-ai mirror) – behavioral CLAUDE.md.
   - claude-mem (thedotmack/claude-mem) – persistent memory.
   - shanraisshan/claude-code-best-practice – workflows & patterns.
   - sickn33/antigravity-awesome-skills – bulk skill library (selective install only high-value bundles).
2. [ ] Identify overlaps and decide:
   - Core harness/rules/hooks/security/MCP → **ECC first** (highest rank + most comprehensive).
   - Behavioral guidelines → **Karpathy rules** (add as base or merge into ECC rules if compatible).
   - Memory → **claude-mem** (or ECC's built-in memory/instincts if sufficient; prefer dedicated if better persistence).
   - Planning / best-practice workflows → Merge from shanraisshan + ECC's planning skills.
   - Bulk skills → Use antigravity-awesome-skills installer but **curate** only top 20–50 most useful (planning, TDD, review, security, frontend, etc.). Avoid installing everything.
3. [ ] Check for official Anthropic skills or new high-rank additions since last check.
4. [ ] Document decisions in `docs/decisions.md` (use ECC's research-first style).

**Acceptance Criteria**:
- Clear decision log exists.
- No conflicting duplicate rules/skills in final setup.

---

## Phase 1: Project Scaffolding & ECC Foundation (Core – Highest Priority)

**Objective**: Create the repo skeleton and install ECC as the complete base harness.

**Tasks**:
1. [ ] Initialize new Git repo: `ultimate-agent-harness-starter` (or user-chosen name).
2. [ ] Create standard structure:

```
ultimate-agent-harness-starter/ ├── .claude/ # Claude Code specific (commands, skills, hooks, rules) ├── .cursor/ # Cursor rules if needed ├── agents/ # Custom sub-agents or extensions ├── skills/ # Curated high-value skills (merged) ├── rules/ # Merged behavioral + coding standards ├── hooks/ # Automation hooks ├── mcp-configs/ # MCP server configs ├── docs/ │ ├── README.md │ ├── decisions.md │ ├── installation.md │ └── usage.md ├── scripts/ # Bootstrap & helper scripts (bash/node) ├── examples/ # Example projects or workflows ├── task.md # This file + future task tracking └── .gitignore  
```
3. [ ] **Install ECC as foundation** (highest rank):
- Follow official ECC install (plugin or manual component copy).
- Copy/adapt core agents (63), skills (251+ curated), rules, hooks, and security (AgentShield).
- Enable key ECC features: token optimization, session persistence, instinct learning, MCP.
4. [ ] Add ECC's dmux-workflows or parallel orchestration support (includes task.md / handoff.md generation).
5. [ ] Create initial `CLAUDE.md` or project root rules file that references ECC + merges Karpathy principles (see Phase 2).

**Acceptance Criteria**:
- `npx` or `/plugin` style one-command can bootstrap ECC core.
- Basic agent commands (`/plan`, `/review`, security scan, etc.) work immediately.
- Repo passes basic lint/security checks.

---

## Phase 2: Add Karpathy Behavioral Rules + Best Practices (Priority #2 & #4)

**Objective**: Inject disciplined behavioral guardrails and production patterns.

**Tasks**:
1. [ ] Integrate **Karpathy rules** (4 core principles) as the **base behavioral layer**:
- Think Before Coding
- Simplicity First
- Surgical Changes
- Goal-Driven Execution
- Merge cleanly into ECC's rules/CLAUDE.md without conflict (ECC first on any overlap).
2. [ ] Pull high-value patterns from `shanraisshan/claude-code-best-practice`:
- Planning workflows, sub-agent usage, context management, slash commands, MCP patterns.
- Select only non-duplicative items (ECC already covers much).
3. [ ] Create or enhance root `CLAUDE.md` / `AGENTS.md` with combined behavioral + best-practice guidance.
4. [ ] Add example "constitution" or project spec template (SDD style) in `docs/`.

**Acceptance Criteria**:
- Agents consistently follow Karpathy + best-practice patterns out of the box.
- No rule conflicts.
- Clear documentation on how rules are loaded.

---

## Phase 3: Memory, Skills & Selective Library Integration (Priority #3 & #5)

**Objective**: Add persistent memory and curated high-impact skills.

**Tasks**:
1. [ ] Install **claude-mem** (or ECC equivalent if stronger) for cross-session persistent context.
- Configure to capture tool usage, summarize, and inject relevant spec/task context.
2. [ ] Use `sickn33/antigravity-awesome-skills` (or similar high-rank library) **selectively**:
- Install only top bundles: planning, TDD, code review, security, frontend/backend patterns, orchestration.
- Avoid full 1500+ install to prevent bloat (curate via script or manifest).
3. [ ] Merge any unique high-value skills into `./skills/` folder with clear attribution.
4. [ ] Create a `skills/manifest.json` or index for easy discovery and updates.
5. [ ] Add SDD-specific skills if not already in ECC (spec analysis, feature spec generation, roadmap tasks, validation gates).

**Acceptance Criteria**:
- Memory persists across sessions and improves context for long tasks.
- Curated skill set is lean yet powerful (document which ones were chosen and why).
- Easy way to add/remove skills later.

---

## Phase 4: Security, Hooks, MCP, Token Optimization & Polish

**Objective**: Production hardening using ECC strengths.

**Tasks**:
1. [ ] Enable **AgentShield** (or ECC security) + secret detection, vulnerability scanning.
2. [ ] Configure key **hooks** (pre-commit validation, post-completion review, context compaction, cost tracking).
3. [ ] Set up **MCP configs** for common tools (GitHub, file system, etc.) – start minimal and secure.
4. [ ] Apply ECC token optimization settings (MAX_THINKING_TOKENS, compact thresholds, etc.).
5. [ ] Add `.gitignore`, license (MIT), and contributor guidelines.
6. [ ] Create bootstrap script(s) in `scripts/`:
- `bootstrap.sh` or `install.js` that runs ECC install + memory + curated skills + config copy.
- Support flags for different agents (Claude Code, Cursor, etc.).

**Acceptance Criteria**:
- Security baseline active and documented.
- Hooks fire correctly.
- Token usage is visibly optimized.
- One main bootstrap command works reliably.

---

## Phase 5: Documentation, Examples, Validation & Quality Gates

**Objective**: Make the starter usable and extensible.

**Tasks**:
1. [ ] Write excellent `docs/`:
- `README.md` with quick start, architecture overview, ranking rationale.
- `installation.md` with exact commands.
- `usage.md` with example workflows (plan a feature with SDD, parallel agents via task.md, security review, etc.).
2. [ ] Add 2–3 example mini-projects or workflow demos in `examples/`.
3. [ ] Implement quality gates:
- Automated lint / security scan on changes.
- Review prompt or agent command for PRs/changes.
- Self-test script that verifies core commands work.
4. [ ] Add this `task.md` (and future task tracking) as the living spec.
5. [ ] Create critic/review agent prompt or skill for ongoing improvement of the harness itself.

**Acceptance Criteria**:
- New user can go from zero to productive agentic workflow in <10 minutes.
- Docs are clear and SDD-aligned.
- Repo is clean, secure, and ready for GitHub.

---

## Phase 6: Future Extensibility & Iteration Hooks

**Objective**: Design for ongoing evolution (your N1ch01as Architect style).

**Tasks**:
1. [ ] Add self-improvement loop skill (research new skills → propose additions → critic review → merge).
2. [ ] Support easy updates from upstream (ECC, skill libraries) via scripts.
3. [ ] Include placeholders for domain-specific extensions (e.g., trading skills, frontend design, Django/TS stacks).
4. [ ] Plan for multi-agent orchestration examples using ECC's dmux + task.md pattern.

**Acceptance Criteria**:
- Clear path to evolve the starter without breaking existing setups.
- Supports your preferred iterative refinement + critic agent workflow.

---

## Overall Execution Notes for Agents

- **Always start with planning/spec phase** (use ECC planning skills or new SDD skills).
- **Use high-ranking source first** on any overlap.
- **Generate task.md / status.md** for complex sub-tasks (following ECC dmux pattern).
- **Run critic/review** after major phases.
- **Track cost/token usage** throughout.
- **Security scan** before any merge or publish.
- **Document decisions** in `docs/decisions.md`.

**Initial Priority Order for Implementation**:
1. ECC foundation (Phase 1)
2. Karpathy + best practices (Phase 2)
3. Memory + curated skills (Phase 3)
4. Security/hooks/MCP (Phase 4)
5. Docs + validation (Phase 5)

---

**Next Immediate Action**  
Run Phase 0 research, then execute Phase 1 scaffolding + ECC install. Create the first commit with the skeleton + this task.md.

This task.md itself serves as the living **spec** for the project. Update it as we progress (or let a critic agent propose improvements).

**Status**: Ready for execution.  
**Owner**: You (or your coding agent harness)  
**Created**: 2026-06-07

---

*This task.md follows SDD principles and harness engineering best practices from the top sources.*

```
  
  
