# Project Starter — Improved Living Task Spec  
  
**Project name:** `project_starter`    
**Package/repo name:** `project_starter`    
**Version:** `0.2.0-rethink`    
**Status:** Ready for Phase 0 execution    
**Created:** 2026-06-07    
**Primary objective:** Build a production-ready starter repo that installs, synchronizes, audits, and evolves a cross-agent coding harness for Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build, and similar tools.  
  
---  
  
## 0. Key Rethink Summary  
  
The original plan is strong but broad, partially duplicative, and slightly risky because it assumes “full installs” and “exact parity” across tools whose config systems differ. This improved spec makes the project more executable by:  
  
1. Making **ECC the foundation**, but installing curated profiles first instead of blindly copying everything.  
2. Replacing Bash-first sync with a **cross-platform Node.js CLI**.  
3. Defining **one source of truth** and generated adapters with drift checks.  
4. Treating “same skills/rules everywhere” as **semantic parity**, not identical file format parity.  
5. Adding license, source, checksum, and version manifests.  
6. Separating **instructions**, **skills**, **memory**, **hooks**, **MCP**, and **generated tool configs**.  
7. Adding an explicit **security threat model**.  
8. Replacing “log all reasoning traces” with **auditable summaries, evidence, decisions, diffs, commands, test results, and review outputs**. Do not request or store hidden chain-of-thought.  
9. Making self-improvement **proposal-only until human approval**.  
10. Adding measurable quality gates, sync tests, and install-time budgets.  
  
---  
  
## 1. Source Verification Snapshot  
  
Phase 0 must re-check all sources before implementation. Current intended source priorities:  
  
1. **ECC** — primary cross-agent harness foundation.  
2. **Karpathy-style behavioral rules** — concise behavioral layer.  
3. **claude-mem or equivalent** — persistent memory if compatible and safe.  
4. **Claude Code best-practice repositories** — selected planning/workflow patterns.  
5. **Curated skill libraries** — selective import only; no bulk install by default.  
6. **Official agent docs** — Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build, GitHub Copilot.  
  
Phase 0 must verify:  
  
- Latest version, commit, tag, or release.  
- License.  
- Installation method.  
- Supported config paths.  
- Security implications.  
- What is included, adapted, or rejected.  
  
---  
  
## 2. Non-Negotiable Principles  
  
1. **SDD first:** Specs drive implementation.  
2. **ECC-first on overlap:** Prefer ECC components, naming, conventions, security, and cross-harness architecture unless a source audit proves a better fit.  
3. **Karpathy behavior layer:** Think before coding, simplicity first, surgical changes, goal-driven execution.  
4. **Single source of truth:** Central `skills/`, `rules/`, `hooks/`, `mcp-configs/`, and manifests are authoritative.  
5. **Generated adapters:** `.claude/`, `.cursor/`, `.gemini/`, `.codex/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, etc. are generated or documented from the source of truth.  
6. **Safe by default:** No destructive automation, remote MCP, or skill mutation without explicit human approval.  
7. **Local-first:** Prefer local scripts, local memory, local audit logs, and optional external services.  
8. **Minimal core, optional bundles:** Starter must be lean; large skill libraries are curated, not fully installed.  
9. **Cross-platform:** macOS, Linux, Windows/PowerShell/WSL where possible.  
10. **Auditable, not opaque:** Store concise rationales, evidence, decisions, diffs, commands run, test results, and review summaries. Do **not** require hidden chain-of-thought.  
  
---  
  
## 3. Target Deliverables  
  
- [ ] New repo: `project_starter`.  
- [ ] One main CLI: `node scripts/project-starter.mjs`.  
- [ ] NPM scripts:  
  - `npm run init`  
  - `npm run sync`  
  - `npm run sync:check`  
  - `npm run doctor`  
  - `npm run security`  
  - `npm run review`  
  - `npm run test`  
  - `npm run format`  
- [ ] ECC-based starter profile.  
- [ ] Cross-agent sync engine.  
- [ ] Curated skills/rules/hooks/MCP manifests.  
- [ ] Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build adapters.  
- [ ] Optional GitHub Copilot, Zed, and Windsurf adapters.  
- [ ] Self-review/critic routine.  
- [ ] Skill lifecycle proposal/approval workflow.  
- [ ] Security baseline with AgentShield or equivalent.  
- [ ] Docs, examples, tests, and acceptance checks.  
  
---  
  
## 4. Proposed Repository Structure  
  
```text  
project_starter/  
├── AGENTS.md  
├── CLAUDE.md  
├── GEMINI.md  
├── README.md  
├── package.json  
├── task.md  
├── status.md  
├── .gitignore  
├── .editorconfig  
├── .claude/  
├── .cursor/  
├── .codex/  
├── .gemini/  
├── .github/  
│   ├── workflows/  
│   └── copilot-instructions.md  
├── agents/  
├── skills/  
│   ├── manifest.json  
│   ├── manifest.schema.json  
│   ├── planning/  
│   ├── implementation/  
│   ├── testing/  
│   ├── review/  
│   ├── security/  
│   ├── memory/  
│   └── lifecycle/  
├── rules/  
│   ├── manifest.json  
│   ├── 00-constitution.md  
│   ├── 10-karpathy.md  
│   ├── 20-sdd.md  
│   ├── 30-security.md  
│   ├── 40-testing.md  
│   ├── 50-token-efficiency.md  
│   └── 60-human-approval.md  
├── hooks/  
│   ├── manifest.json  
│   ├── specs/  
│   └── scripts/  
├── mcp-configs/  
│   ├── manifest.json  
│   ├── minimal.json  
│   └── optional/  
├── memory/  
│   ├── README.md  
│   ├── project.md  
│   ├── handoff.md  
│   └── reflections/  
├── reviews/  
├── suggestions/  
│   ├── pending/  
│   ├── approved/  
│   ├── rejected/  
│   └── audit-log.md  
├── scripts/  
│   ├── project-starter.mjs  
│   ├── sync.mjs  
│   ├── doctor.mjs  
│   ├── security.mjs  
│   ├── review.mjs  
│   ├── adapters/  
│   │   ├── claude.mjs  
│   │   ├── cursor.mjs  
│   │   ├── codex.mjs  
│   │   ├── opencode.mjs  
│   │   ├── gemini.mjs  
│   │   ├── grok-build.mjs  
│   │   └── copilot.mjs  
│   └── lib/  
├── docs/  
│   ├── installation.md  
│   ├── usage.md  
│   ├── architecture.md  
│   ├── decisions.md  
│   ├── source-audit.md  
│   ├── security.md  
│   ├── sync.md  
│   └── troubleshooting.md  
├── examples/  
│   ├── sdd-feature-workflow/  
│   ├── self-review-workflow/  
│   ├── skill-suggestion-workflow/  
│   └── cross-agent-sync-workflow/  
└── tests/  
    ├── fixtures/  
    ├── sync.test.mjs  
    ├── manifest.test.mjs  
    └── adapters.test.mjs  
```  
  
---  
  
## 5. Generated File Policy  
  
Every generated/adapted file must include a header:  
  
```text  
<!-- AUTO-GENERATED by project_starter. Do not edit directly.  
Source: skills/, rules/, hooks/, mcp-configs/  
Run: npm run sync  
-->  
```  
  
Rules:  
  
- [ ] Central files are authoritative.  
- [ ] Generated files are overwritten only after conflict checks.  
- [ ] Local user files are backed up before overwrite.  
- [ ] `--dry-run` must show exact writes/deletes.  
- [ ] `--check` must fail if generated files are stale.  
- [ ] Symlinks are preferred only where safe and supported.  
- [ ] Windows fallback is copy mode unless Developer Mode/admin symlink support is detected.  
  
---  
  
## 6. Phase 0 — Research, Scope Lock, and Source Audit  
  
**Goal:** Confirm latest sources, install commands, licenses, and compatibility before generating files.  
  
### Tasks  
  
- [ ] Verify latest ECC release, installer commands, profiles, and license.  
- [ ] Verify Karpathy-style rules source and Cursor rule variant.  
- [ ] Verify `claude-mem` or equivalent persistent-memory candidate.  
- [ ] Verify best-practice workflow repositories and select only non-duplicative patterns.  
- [ ] Verify curated skill libraries and choose only high-value bundles.  
- [ ] Verify official docs for Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build, and GitHub Copilot.  
- [ ] Create `docs/source-audit.md` with:  
  - source name  
  - URL  
  - version/commit/tag  
  - license  
  - install command  
  - selected components  
  - rejected components  
  - rationale  
- [ ] Create `docs/decisions.md` with ADR-style decisions.  
- [ ] Define starter profiles:  
  - **Core profile:** minimal, safe, under 5-minute init.  
  - **Power profile:** ECC broader install + memory + curated skills.  
  - **Experimental profile:** Grok Build, extra MCP, multi-agent demos.  
  
### Acceptance Criteria  
  
- [ ] No source is used without license and version/commit recorded.  
- [ ] No conflicting duplicate skills/rules are accepted.  
- [ ] Clear priority order exists: ECC > Karpathy > memory > best-practice > curated libraries.  
- [ ] Install commands are verified before scripting.  
  
---  
  
## 7. Phase 1 — Repo Skeleton and CLI Foundation  
  
**Goal:** Create a clean starter repo with portable scripts.  
  
### Tasks  
  
- [ ] Initialize Git repo named `project_starter`.  
- [ ] Add `package.json` with scripts:  
  - `init`  
  - `sync`  
  - `sync:check`  
  - `doctor`  
  - `security`  
  - `review`  
  - `test`  
  - `format`  
- [ ] Implement `scripts/project-starter.mjs` command router.  
- [ ] Implement `scripts/doctor.mjs` to check:  
  - Node version  
  - Git availability  
  - OS  
  - symlink capability  
  - Claude/Cursor/Codex/Gemini/OpenCode/Grok availability when installed  
  - required directories  
- [ ] Add `.editorconfig`, `.gitignore`, `README.md`, and base docs.  
- [ ] Add empty manifests with JSON schemas.  
- [ ] Add first `task.md` and `status.md`.  
  
### Acceptance Criteria  
  
- [ ] `npm run doctor` works on a clean machine.  
- [ ] `npm run test` passes with placeholder tests.  
- [ ] Repo skeleton can be created in under 1 minute.  
- [ ] All docs and generated headers use `project_starter`.  
  
---  
  
## 8. Phase 2 — ECC Foundation  
  
**Goal:** Install/adapt ECC as the primary harness layer.  
  
### Tasks  
  
- [ ] Add `scripts/adapters/ecc.mjs` or installer wrapper.  
- [ ] Support profiles:  
  - `--profile core`  
  - `--profile minimal`  
  - `--profile power`  
  - `--profile experimental`  
- [ ] Install/select ECC components:  
  - core rules  
  - planning/review/security skills  
  - AgentShield/security scan  
  - token/context optimization  
  - memory/instinct learning where safe  
  - dmux or parallel orchestration patterns  
  - MCP conventions  
- [ ] Avoid blind full copy by default.  
- [ ] Record ECC source version in `docs/source-audit.md`.  
- [ ] Add attribution to imported/derived files.  
- [ ] Run AgentShield/security scan after ECC setup.  
  
### Acceptance Criteria  
  
- [ ] ECC core profile is installed or referenced reproducibly.  
- [ ] Security scan runs.  
- [ ] No oversized skill dump is loaded by default.  
- [ ] ECC is the default conflict winner.  
  
---  
  
## 9. Phase 3 — Behavioral Rules and SDD Constitution  
  
**Goal:** Create concise, high-impact rules that every agent receives.  
  
### Central Rule Files  
  
- [ ] `rules/00-constitution.md`  
- [ ] `rules/10-karpathy.md`  
- [ ] `rules/20-sdd.md`  
- [ ] `rules/30-security.md`  
- [ ] `rules/40-testing.md`  
- [ ] `rules/50-token-efficiency.md`  
- [ ] `rules/60-human-approval.md`  
  
### Required Behavioral Layer  
  
- [ ] Think before coding.  
- [ ] Prefer simple solutions.  
- [ ] Make surgical changes.  
- [ ] Execute against the stated goal.  
- [ ] Ask only when blocked by meaningful ambiguity.  
- [ ] Plan before multi-file edits.  
- [ ] Run tests or explain why tests were not run.  
- [ ] Update `status.md` after major work.  
- [ ] Never auto-apply skill/rule/hook changes without human approval.  
  
### Acceptance Criteria  
  
- [ ] `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/*.mdc`, and tool adapters receive semantically identical behavior.  
- [ ] Rules remain concise and non-duplicative.  
- [ ] All rule conflicts are documented.  
  
---  
  
## 10. Phase 4 — Curated Skills  
  
**Goal:** Build a lean skill set that covers high-value workflows without bloat.  
  
### Core Skill Categories  
  
- [ ] Planning / SDD  
- [ ] Implementation  
- [ ] TDD / testing  
- [ ] Code review  
- [ ] Security review  
- [ ] Debugging  
- [ ] Refactoring  
- [ ] Documentation  
- [ ] Memory / handoff  
- [ ] Context compaction  
- [ ] Cross-agent sync  
- [ ] Self-review / critic  
- [ ] Skill suggestion lifecycle  
  
### Manifest Requirements  
  
Each skill entry in `skills/manifest.json` must include:  
  
- `id`  
- `name`  
- `version`  
- `description`  
- `source`  
- `source_priority`  
- `license`  
- `checksum`  
- `compatible_agents`  
- `side_effects`  
- `requires_human_approval`  
- `tags`  
- `paths`  
- `owner`  
- `last_reviewed`  
  
### Acceptance Criteria  
  
- [ ] Core profile has roughly 15–30 skills, not hundreds.  
- [ ] Optional bundles are selectable.  
- [ ] Every skill has attribution and versioning.  
- [ ] Skills are tested through sync adapters.  
  
---  
  
## 11. Phase 5 — Cross-Agent Synchronization Layer  
  
**Goal:** Make every supported agent receive the same curated skills, rules, hooks, and MCP configuration as far as each tool supports.  
  
### CLI  
  
Implement:  
  
```text  
npm run sync -- --all  
npm run sync -- --agent claude  
npm run sync -- --agent cursor  
npm run sync -- --agent codex  
npm run sync -- --agent gemini  
npm run sync -- --agent opencode  
npm run sync -- --agent grok-build  
npm run sync -- --dry-run  
npm run sync -- --check  
npm run sync -- --mode auto  
npm run sync -- --mode copy  
npm run sync -- --mode symlink  
npm run sync -- --select planning,review,security  
```  
  
### Adapter Targets  
  
- [ ] Claude Code:  
  - `.claude/skills/<skill>/SKILL.md`  
  - `.claude/rules/*.md`  
  - `.claude/settings.json`  
  - `.claude/commands/` compatibility shims where useful  
  - root `CLAUDE.md`  
- [ ] Cursor:  
  - `.cursor/rules/*.mdc`  
  - `.cursor/mcp.json`  
  - optional `.cursor/skills/` if supported by selected ECC pattern  
- [ ] Codex:  
  - `AGENTS.md`  
  - `.codex/` config where supported  
  - generated skills index if native skills are unavailable  
- [ ] OpenCode:  
  - `AGENTS.md`  
  - `opencode.json`  
  - optional agent definitions  
- [ ] Gemini CLI:  
  - `GEMINI.md`  
  - `.gemini/settings.json`  
  - optional context filename config  
- [ ] Grok Build:  
  - `AGENTS.md`  
  - compatible skills/hooks/MCP references where supported  
- [ ] GitHub Copilot:  
  - `.github/copilot-instructions.md`  
  
### Sync Safety  
  
- [ ] Backup modified generated files.  
- [ ] Detect manual edits to generated files.  
- [ ] Produce a sync report.  
- [ ] Fail on manifest/schema errors.  
- [ ] Support CI drift check.  
  
### Acceptance Criteria  
  
- [ ] Change central skill → run sync → all supported agents update.  
- [ ] `npm run sync -- --check` detects stale generated files.  
- [ ] At least Claude Code + Cursor + Codex/Gemini are tested.  
- [ ] No manual copying is required.  
  
---  
  
## 12. Phase 6 — Memory and Handoff  
  
**Goal:** Provide persistent, privacy-aware memory without context bloat.  
  
### Memory Layers  
  
- [ ] `status.md`: current progress.  
- [ ] `task.md`: living spec.  
- [ ] `memory/project.md`: stable project context.  
- [ ] `memory/handoff.md`: compact continuation summary.  
- [ ] `memory/reflections/`: review lessons and repeated patterns.  
- [ ] Optional `claude-mem` or ECC memory/instinct layer.  
  
### Rules  
  
- [ ] Never store secrets.  
- [ ] Redact credentials and personal data.  
- [ ] Summarize instead of dumping logs.  
- [ ] Load only relevant memory.  
- [ ] Prefer handoff files for session continuation.  
- [ ] Keep auto-injected context small.  
  
### Acceptance Criteria  
  
- [ ] A new session can resume from `task.md`, `status.md`, and `memory/handoff.md`.  
- [ ] Self-review outputs can generate reflection entries.  
- [ ] Memory can be disabled.  
  
---  
  
## 13. Phase 7 — Self-Evaluation and Critic Routine  
  
**Goal:** Add a structured plan → implement → review → refine loop.  
  
### Roles  
  
- **Actor/Solver:** Implements the task.  
- **Critic:** Reviews correctness, simplicity, spec adherence, security, performance, maintainability.  
- **Security Critic:** Optional focused security pass.  
- **Test Critic:** Optional test and verification pass.  
- **Judge:** Summarizes blocking vs non-blocking findings.  
  
### Rubric  
  
Score each dimension from 1–5:  
  
1. Correctness  
2. Spec adherence  
3. Simplicity / Karpathy alignment  
4. Security  
5. Test coverage  
6. Maintainability  
7. Performance/token efficiency  
8. Auditability  
9. Self-improvement value  
  
### Outputs  
  
- [ ] `reviews/<timestamp>-<task>.review.md`  
- [ ] `reviews/<timestamp>-<task>.review.json`  
- [ ] Blocking findings  
- [ ] Non-blocking suggestions  
- [ ] Tests run  
- [ ] Files changed  
- [ ] Recommended next tasks  
  
### Commands  
  
- [ ] Claude skill/command: `/self-review`  
- [ ] Claude skill/command: `/critic`  
- [ ] CLI: `npm run review`  
- [ ] Optional hook: post-task self-review  
  
### Guardrails  
  
- [ ] No hidden chain-of-thought logging.  
- [ ] Store concise rationale and evidence only.  
- [ ] Max 2 refine loops by default.  
- [ ] Human confirmation for high-impact changes.  
  
### Acceptance Criteria  
  
- [ ] Agent can critique its own work.  
- [ ] Critique includes actionable fixes.  
- [ ] Review can block completion if serious issues exist.  
- [ ] Review output feeds memory/reflection safely.  
  
---  
  
## 14. Phase 8 — Skill Lifecycle Suggestions with Human Approval  
  
**Goal:** Allow safe self-evolution of skills/rules/hooks through suggestions only.  
  
### Workflow  
  
1. Analyze skill usage, reviews, failures, gaps, duplication.  
2. Generate suggestion file.  
3. Human reviews.  
4. Human approves/rejects/modifies.  
5. Approved change applies to central source.  
6. Sync propagates change.  
7. Audit log records decision.  
  
### Suggestion Template  
  
Each suggestion must include:  
  
- ID  
- Action: add/update/remove  
- Target skill/rule/hook  
- Rationale  
- Evidence  
- Proposed diff/content  
- Risk assessment  
- Rollback plan  
- Confidence  
- Human approval field  
  
### Commands  
  
- [ ] `/suggest-skills`  
- [ ] `/review-suggestions`  
- [ ] `/approve-suggestion`  
- [ ] CLI: `npm run suggest-skills`  
- [ ] CLI: `npm run apply-suggestion -- --id <id>`  
  
### Acceptance Criteria  
  
- [ ] No skill/rule/hook mutation occurs without explicit approval.  
- [ ] Approved changes are logged.  
- [ ] Rejected suggestions are retained for audit.  
- [ ] Rollback path exists.  
  
---  
  
## 15. Phase 9 — Security Baseline  
  
**Goal:** Make the harness safe for real-world local use.  
  
### Threat Model  
  
Protect against:  
  
- [ ] Prompt injection through docs, issues, web pages, MCP output.  
- [ ] Secret exfiltration.  
- [ ] Destructive shell commands.  
- [ ] Over-permissive hooks.  
- [ ] Unsafe MCP servers.  
- [ ] Supply-chain risk from skill libraries.  
- [ ] Generated file drift.  
- [ ] Hidden remote telemetry.  
- [ ] Accidental global config overwrite.  
  
### Controls  
  
- [ ] AgentShield or equivalent scan.  
- [ ] Secret scanner.  
- [ ] MCP allowlist.  
- [ ] Hook command allowlist.  
- [ ] `.env`, key, cert, token file protections.  
- [ ] Human approval for destructive commands.  
- [ ] CI security check.  
- [ ] Dependency audit.  
- [ ] No default remote MCP credentials.  
- [ ] No `curl | bash` in scripts unless explicitly approved and documented.  
  
### Acceptance Criteria  
  
- [ ] `npm run security` runs locally.  
- [ ] Critical findings fail CI.  
- [ ] Sensitive files are protected.  
- [ ] Security docs explain the model.  
  
---  
  
## 16. Phase 10 — Docs and Examples  
  
**Goal:** Make the starter usable in under 10 minutes.  
  
### Docs  
  
- [ ] `README.md`: overview and quick start.  
- [ ] `docs/installation.md`: exact install commands.  
- [ ] `docs/usage.md`: day-to-day workflows.  
- [ ] `docs/architecture.md`: source-of-truth and adapters.  
- [ ] `docs/sync.md`: sync behavior and troubleshooting.  
- [ ] `docs/security.md`: security model.  
- [ ] `docs/decisions.md`: ADRs.  
- [ ] `docs/source-audit.md`: source versions and licenses.  
  
### Examples  
  
- [ ] SDD feature workflow.  
- [ ] Cross-agent sync workflow.  
- [ ] Self-review workflow.  
- [ ] Skill suggestion workflow.  
- [ ] Security scan workflow.  
  
### Acceptance Criteria  
  
- [ ] New user can initialize and sync in under 10 minutes.  
- [ ] Docs explain Claude/Cursor/Codex/Gemini/OpenCode differences.  
- [ ] Examples are runnable.  
  
---  
  
## 17. Phase 11 — Validation and CI  
  
**Goal:** Prevent regressions and prove the starter works.  
  
### Tests  
  
- [ ] Manifest schema validation.  
- [ ] Adapter snapshot tests.  
- [ ] Sync dry-run tests.  
- [ ] Generated file drift tests.  
- [ ] Security scan smoke test.  
- [ ] Windows path handling tests.  
- [ ] No duplicate skill IDs.  
- [ ] No generated files missing headers.  
  
### CI  
  
- [ ] Lint JS.  
- [ ] Validate JSON.  
- [ ] Validate Markdown links where possible.  
- [ ] Run tests.  
- [ ] Run `sync --check`.  
- [ ] Run security scan.  
- [ ] Upload review/security artifacts.  
  
### Acceptance Criteria  
  
- [ ] CI is green.  
- [ ] Fresh clone passes `npm install && npm test`.  
- [ ] `npm run sync -- --check` passes after generation.  
  
---  
  
## 18. Definition of Done  
  
The project is complete when:  
  
- [ ] `npm run init` creates a working starter.  
- [ ] `npm run sync` updates all supported agent configs.  
- [ ] Claude Code, Cursor, and at least one of Codex/Gemini/OpenCode are verified.  
- [ ] ECC foundation is installed/adapted and documented.  
- [ ] Karpathy behavior rules are active.  
- [ ] Self-review workflow works.  
- [ ] Skill suggestions require human approval.  
- [ ] Security scan works and blocks critical issues.  
- [ ] Docs are sufficient for a new user.  
- [ ] All generated files are reproducible.  
- [ ] Source audit and decisions are complete.  
- [ ] All project names, docs, generated headers, scripts, and examples consistently use `project_starter`.  
  
---  
  
## 19. Immediate Next Actions  
  
1. Create repo skeleton named `project_starter`.  
2. Run Phase 0 source audit.  
3. Implement `scripts/project-starter.mjs`, `doctor.mjs`, and empty sync framework.  
4. Add central rules and manifests.  
5. Implement Claude + Cursor adapters first.  
6. Add Codex/Gemini/OpenCode adapters next.  
7. Install/adapt ECC core profile.  
8. Run security scan.  
9. Write docs and examples.  
10. Commit as:  
  
```text  
chore: initialize project_starter  
```  
  
---  
  
## 20. Implementation Priority  
  
1. **Foundation:** repo, CLI, manifests, docs skeleton.  
2. **Sync:** central source → Claude/Cursor/Codex.  
3. **ECC:** install/adapt core.  
4. **Rules:** constitution + Karpathy + SDD.  
5. **Skills:** curated core.  
6. **Security:** AgentShield + secret protections.  
7. **Memory:** handoff + reflection.  
8. **Critic:** self-review workflow.  
9. **Lifecycle:** suggestions + human approval.  
10. **Polish:** examples, CI, docs.  
