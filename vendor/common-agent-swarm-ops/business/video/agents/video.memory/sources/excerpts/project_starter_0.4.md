# project_starter.md

## Purpose

`project_starter` is a reusable boilerplate specification for creating new software projects with built-in support for AI coding agents, source downloading, project bootstrapping, validation, documentation, safety rules, and repeatable automation.

This file is the **source-of-truth implementation contract**.

A coding agent must be able to read this file and create a complete, executable starter project from it.

The generated project must not be only documentation. It must include working scripts, manifests, validation commands, agent configuration files, documentation files, and safety controls.

---

# 1. Project Modes

`project_starter.md` supports two major modes.

## 1.1 Self-Bootstrap Mode

Use this mode when implementing the boilerplate repository itself.

Example prompt:

```text
Implement project_starter.md in the current repository.

Use project_starter.md as the source-of-truth implementation contract.

Create all required files, directories, scripts, manifests, docs, tests, and agent configuration files.

Then run:

npm run bootstrap
```

Expected result:

```text
project_starter/
├── project_starter.md
├── README.md
├── package.json
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── task.md
├── status.md
├── sources/
├── scripts/
├── rules/
├── skills/
├── hooks/
├── mcp-configs/
├── memory/
├── docs/
├── tests/
└── external/
```

## 1.2 Create-New-Project Mode

Use this mode when creating a new project from this boilerplate.

Example prompt:

```text
Create a new project named abc based on ./project_starter.md.

Create it at:

./abc

Use project_starter.md as the complete implementation contract.

Create a working executable project, not just Markdown.

Download all enabled sources.

Run:

npm run bootstrap
```

Expected result:

```text
abc/
├── project_starter.md
├── README.md
├── package.json
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── task.md
├── status.md
├── sources/
├── scripts/
├── rules/
├── skills/
├── hooks/
├── mcp-configs/
├── memory/
├── docs/
├── tests/
└── external/
```

---

# 2. How a Human Should Ask a Coding Agent to Use This File

A human can use the following prompt.

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Create the new project at:

<OUTPUT_PATH>

Use project_starter.md as the complete source-of-truth implementation contract.

Project purpose:

<PROJECT_PURPOSE>

Primary stack:

<STACK>

Required agent support:
- Claude Code
- Codex
- Gemini CLI
- Cursor
- OpenCode
- GitHub Copilot

You must:
1. Read the entire project_starter.md.
2. Create the target project directory.
3. Create all files and directories required by project_starter.md.
4. Replace boilerplate metadata with the new project name and purpose.
5. Copy project_starter.md into the new project root.
6. Create package.json.
7. Create source manifests.
8. Create executable scripts.
9. Create rule files.
10. Create documentation files.
11. Create tests.
12. Create agent configuration files.
13. Download all enabled upstream sources into external/sources/.
14. Generate sources/source-lock.json.
15. Generate docs/source-audit.md.
16. Run bootstrap validation.
17. Update status.md with actual results.
18. Report final pass/fail status.

Security requirements:
- Do not execute downloaded third-party code.
- Do not install packages inside downloaded third-party repositories.
- Do not import downloaded third-party code automatically.
- Do not modify global user configuration.
- Do not use secrets unless explicitly provided.
- Do not overwrite existing files without permission.

If network or shell access is unavailable:
- Still create all project files.
- Still create all scripts.
- Mark source downloading as blocked in status.md.
- Tell the user to run:

cd <OUTPUT_PATH>
npm run bootstrap
```

---

# 3. Required Input Variables

A coding agent may receive these variables from the user.

| Variable | Description | Default |
|---|---|---|
| `PROJECT_NAME` | Name of the generated project | `project_starter_generated` |
| `OUTPUT_PATH` | Directory where the generated project should be created | `./project_starter_generated` |
| `PROJECT_PURPOSE` | Short description of the generated project | `AI coding-agent starter repository` |
| `STACK` | Main technology stack | `Node.js 20+, plain JavaScript, no runtime dependencies for bootstrap scripts` |
| `DOWNLOAD_SOURCES` | Whether to download configured upstream sources | `true` |
| `AGENT_SUPPORT` | Supported coding agents | `claude,codex,gemini,cursor,opencode,copilot` |
| `PACKAGE_MANAGER` | JavaScript package manager | `npm` |
| `LICENSE` | License for the generated project | `MIT` |

If a required value is missing, use the default value.

---

# 4. Required Behavior for Coding Agents

When a coding agent implements this specification, it must follow these rules.

## 4.1 General Rules

The coding agent must:

1. Treat this file as the implementation contract.
2. Create a complete working project.
3. Prefer simple, auditable scripts.
4. Use Node.js standard library for automation scripts unless dependencies are explicitly required.
5. Avoid unnecessary third-party packages.
6. Keep generated files readable and maintainable.
7. Make commands idempotent where practical.
8. Record all generated status information in `status.md`.
9. Record all downloaded source metadata in `sources/source-lock.json`.
10. Record all source audit information in `docs/source-audit.md`.

## 4.2 Safety Rules

The coding agent must not:

1. Execute downloaded third-party repository code.
2. Run `npm install`, `pnpm install`, `yarn install`, `pip install`, `cargo build`, `go build`, or equivalent inside downloaded repositories.
3. Automatically import source files from downloaded repositories into the main project.
4. Modify files outside the target project directory.
5. Modify global agent configuration.
6. Store secrets in committed files.
7. Delete user files without explicit permission.
8. Overwrite an existing non-empty output directory without explicit permission.
9. Run destructive commands such as `rm -rf /`, `git clean -fdx`, or equivalent.
10. Assume network access is available.

## 4.3 If Output Directory Already Exists

If `OUTPUT_PATH` already exists and is not empty, the coding agent must stop and ask for permission before continuing.

Allowed exception:

If the user explicitly says to overwrite or update the existing directory, the agent may proceed, but must preserve important user-created files when possible.

---

# 5. Required Project Structure

The generated project must contain the following structure.

```text
<PROJECT_NAME>/
├── project_starter.md
├── README.md
├── package.json
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── task.md
├── status.md
├── .gitignore
├── .editorconfig
├── sources/
│   ├── manifest.json
│   ├── docs-manifest.json
│   └── source-lock.json
├── scripts/
│   ├── bootstrap.mjs
│   ├── doctor.mjs
│   ├── create-project.mjs
│   ├── download-sources.mjs
│   ├── audit-sources.mjs
│   ├── security-check.mjs
│   ├── sync-agent-configs.mjs
│   ├── test.mjs
│   └── utils/
│       ├── fs.mjs
│       ├── git.mjs
│       ├── log.mjs
│       └── project.mjs
├── rules/
│   ├── universal-rules.md
│   ├── safety-rules.md
│   ├── coding-rules.md
│   ├── git-rules.md
│   ├── testing-rules.md
│   └── source-rules.md
├── skills/
│   ├── planning.md
│   ├── debugging.md
│   ├── refactoring.md
│   ├── testing.md
│   ├── documentation.md
│   └── security-review.md
├── hooks/
│   ├── pre-task.md
│   ├── post-task.md
│   └── pre-commit.md
├── mcp-configs/
│   ├── README.md
│   └── example.mcp.json
├── memory/
│   ├── project-memory.md
│   ├── decisions.md
│   └── glossary.md
├── docs/
│   ├── architecture.md
│   ├── setup.md
│   ├── usage.md
│   ├── source-audit.md
│   ├── agents.md
│   ├── troubleshooting.md
│   └── changelog.md
├── tests/
│   ├── smoke.test.mjs
│   └── fixtures/
│       └── README.md
└── external/
    └── sources/
        └── .gitkeep
```

---

# 6. Required `package.json`

The generated project must include a `package.json`.

Example:

```json
{
  "name": "<PROJECT_NAME>",
  "version": "0.1.0",
  "description": "<PROJECT_PURPOSE>",
  "private": true,
  "type": "module",
  "license": "MIT",
  "engines": {
    "node": ">=20.0.0"
  },
  "scripts": {
    "bootstrap": "node scripts/bootstrap.mjs",
    "doctor": "node scripts/doctor.mjs",
    "create": "node scripts/create-project.mjs",
    "sources:download": "node scripts/download-sources.mjs",
    "sources:audit": "node scripts/audit-sources.mjs",
    "security": "node scripts/security-check.mjs",
    "sync": "node scripts/sync-agent-configs.mjs",
    "test": "node scripts/test.mjs",
    "check": "npm run doctor && npm run security && npm run sources:audit && npm run test"
  },
  "dependencies": {},
  "devDependencies": {}
}
```

Rules:

1. `name` must be a package-safe version of `PROJECT_NAME`.
2. `description` must match `PROJECT_PURPOSE`.
3. `type` must be `module`.
4. Runtime dependencies should be empty unless needed.
5. Scripts must work on macOS, Linux, and Windows where practical.

---

# 7. Required Root Files

## 7.1 `README.md`

The generated `README.md` must include:

```md
# <PROJECT_NAME>

<PROJECT_PURPOSE>

## Quick Start

```bash
npm run bootstrap
```

## Common Commands

```bash
npm run doctor
npm run sources:download
npm run sources:audit
npm run security
npm run sync -- --dry-run
npm run test
```

## Project Structure

See `project_starter.md` for the full implementation contract.

## AI Coding Agents

This project includes configuration and instructions for:

- Claude Code
- Codex
- Gemini CLI
- Cursor
- OpenCode
- GitHub Copilot

See `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `docs/agents.md`.

## Safety

Downloaded external sources are stored in:

```text
external/sources/
```

Do not execute downloaded third-party code unless explicitly reviewed.
```

## 7.2 `AGENTS.md`

`AGENTS.md` is the universal instruction file for coding agents.

It must include:

```md
# AGENTS.md

## Project

Project name: <PROJECT_NAME>

Project purpose: <PROJECT_PURPOSE>

## Source of Truth

The source-of-truth implementation contract is:

```text
project_starter.md
```

## Agent Rules

1. Read `project_starter.md` before making structural changes.
2. Follow `rules/universal-rules.md`.
3. Follow `rules/safety-rules.md`.
4. Do not execute downloaded third-party source code.
5. Do not modify global user configuration.
6. Keep changes small and reviewable.
7. Update `status.md` after major changes.
8. Update docs when behavior changes.
9. Run tests before reporting completion.

## Standard Validation

Run:

```bash
npm run check
```

## Source Handling

External source repositories are reference material only.

They live in:

```text
external/sources/
```

Do not import or execute them automatically.
```

## 7.3 `CLAUDE.md`

`CLAUDE.md` must include Claude-specific guidance.

```md
# CLAUDE.md

## Instructions for Claude Code

Read these files first:

1. `project_starter.md`
2. `AGENTS.md`
3. `task.md`
4. `status.md`

## Required Behavior

- Use `project_starter.md` as the implementation contract.
- Follow safety rules in `rules/safety-rules.md`.
- Keep edits minimal and explicit.
- Do not execute downloaded third-party code.
- Run validation before reporting completion.

## Validation Command

```bash
npm run check
```
```

## 7.4 `GEMINI.md`

`GEMINI.md` must include Gemini-specific guidance.

```md
# GEMINI.md

## Instructions for Gemini CLI

Read these files first:

1. `project_starter.md`
2. `AGENTS.md`
3. `task.md`
4. `status.md`

## Required Behavior

- Treat this repository as an executable boilerplate project.
- Follow all safety and source handling rules.
- Do not execute downloaded third-party code.
- Prefer simple scripts using Node.js standard library.
- Update `status.md` after completing changes.

## Validation Command

```bash
npm run check
```
```

## 7.5 `task.md`

`task.md` tracks the current task.

```md
# Task

## Current Goal

Implement and maintain this project according to `project_starter.md`.

## Checklist

- [ ] Read `project_starter.md`
- [ ] Verify project structure
- [ ] Verify scripts
- [ ] Verify source manifests
- [ ] Run bootstrap
- [ ] Run tests
- [ ] Update status

## Notes

Add task-specific notes here.
```

## 7.6 `status.md`

`status.md` records the current implementation status.

```md
# Status

## Project

Name: <PROJECT_NAME>

Purpose: <PROJECT_PURPOSE>

## Last Updated

Not yet updated.

## Bootstrap Status

| Check | Status | Notes |
|---|---|---|
| doctor | unknown | Not run |
| sources download | unknown | Not run |
| source audit | unknown | Not run |
| security | unknown | Not run |
| sync dry-run | unknown | Not run |
| tests | unknown | Not run |

## Known Issues

None recorded.

## Next Steps

Run:

```bash
npm run bootstrap
```
```

## 7.7 `.gitignore`

Required `.gitignore`:

```gitignore
node_modules/
.DS_Store
.env
.env.*
!.env.example
coverage/
dist/
build/
tmp/
.cache/
external/sources/*
!external/sources/.gitkeep
sources/source-lock.json.tmp
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
```

## 7.8 `.editorconfig`

Required `.editorconfig`:

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2

[*.md]
trim_trailing_whitespace = false
```

---

# 8. Required Source Manifests

## 8.1 `sources/manifest.json`

This file lists upstream repositories that may be downloaded as reference material.

Default example:

```json
{
  "version": 1,
  "description": "External source repositories used as reference material only.",
  "sources": [
    {
      "id": "anthropic-claude-code-docs",
      "type": "git",
      "enabled": true,
      "url": "https://github.com/anthropics/claude-code.git",
      "branch": "main",
      "destination": "external/sources/anthropic-claude-code-docs",
      "purpose": "Reference material for Claude Code conventions.",
      "execute": false
    },
    {
      "id": "openai-codex-reference",
      "type": "git",
      "enabled": false,
      "url": "https://github.com/openai/codex.git",
      "branch": "main",
      "destination": "external/sources/openai-codex-reference",
      "purpose": "Reference material for Codex conventions if available.",
      "execute": false
    },
    {
      "id": "google-gemini-cli",
      "type": "git",
      "enabled": false,
      "url": "https://github.com/google-gemini/gemini-cli.git",
      "branch": "main",
      "destination": "external/sources/google-gemini-cli",
      "purpose": "Reference material for Gemini CLI conventions if available.",
      "execute": false
    }
  ]
}
```

Rules:

1. Each source must have a unique `id`.
2. Each source must have `enabled`.
3. Each source must have `url`.
4. Each source must have `destination`.
5. Each source must have `execute: false`.
6. Disabled sources must not be downloaded unless enabled by the user.
7. Downloaded sources are for reference only.

## 8.2 `sources/docs-manifest.json`

This file lists documentation references.

```json
{
  "version": 1,
  "description": "Documentation references for agent configuration and project conventions.",
  "docs": [
    {
      "id": "project-contract",
      "type": "local",
      "path": "project_starter.md",
      "purpose": "Primary implementation contract"
    },
    {
      "id": "agent-instructions",
      "type": "local",
      "path": "AGENTS.md",
      "purpose": "Universal coding agent instructions"
    },
    {
      "id": "safety-rules",
      "type": "local",
      "path": "rules/safety-rules.md",
      "purpose": "Safety requirements for humans and agents"
    }
  ]
}
```

## 8.3 `sources/source-lock.json`

This file is generated by `scripts/download-sources.mjs`.

Initial content:

```json
{
  "version": 1,
  "generatedAt": null,
  "sources": []
}
```

Generated entries should include:

```json
{
  "id": "example",
  "url": "https://github.com/example/example.git",
  "branch": "main",
  "destination": "external/sources/example",
  "status": "downloaded",
  "commit": "abc123",
  "downloadedAt": "2026-01-01T00:00:00.000Z"
}
```

Allowed statuses:

```text
downloaded
skipped
failed
blocked
```

---

# 9. Required Scripts

All scripts must be written in modern Node.js ESM syntax and use only Node.js standard library unless otherwise required.

## 9.1 `scripts/bootstrap.mjs`

Purpose:

Run the complete project bootstrap flow.

Required behavior:

1. Run `doctor`.
2. Run `sources:download`.
3. Run `sources:audit`.
4. Run `security`.
5. Run `sync -- --dry-run`.
6. Run `test`.
7. Update `status.md`.
8. Print final summary.

Equivalent command:

```bash
npm run doctor
npm run sources:download
npm run sources:audit
npm run security
npm run sync -- --dry-run
npm run test
```

Failure behavior:

- If one step fails, record it.
- Continue when safe.
- Exit non-zero if any required step fails.
- If network is unavailable, mark source download as blocked but continue local checks.

## 9.2 `scripts/doctor.mjs`

Purpose:

Validate local project health.

Required checks:

1. Node.js version is at least 20.
2. Required directories exist.
3. Required files exist.
4. `package.json` is valid JSON.
5. `sources/manifest.json` is valid JSON.
6. `sources/docs-manifest.json` is valid JSON.
7. Required npm scripts exist.
8. `external/sources/` exists.
9. No required root files are missing.

Should print:

```text
doctor: pass
```

or:

```text
doctor: fail
```

## 9.3 `scripts/create-project.mjs`

Purpose:

Create a new project from this boilerplate.

Required CLI options:

```bash
node scripts/create-project.mjs --name abc --path ../abc
node scripts/create-project.mjs --name abc --path ../abc --purpose "My project"
node scripts/create-project.mjs --name abc --path ../abc --stack "Node.js, TypeScript"
node scripts/create-project.mjs --name abc --path ../abc --no-download
node scripts/create-project.mjs --name abc --path ../abc --force
```

Required behavior:

1. Parse CLI arguments.
2. Validate project name.
3. Validate output path.
4. Refuse to overwrite non-empty directories unless `--force` is provided.
5. Create required directory structure.
6. Copy `project_starter.md`.
7. Generate all required files.
8. Replace placeholders with project values.
9. Optionally run source download unless `--no-download` is used.
10. Print next steps.

Required output:

```text
Created project: abc
Path: ../abc

Next commands:
cd ../abc
npm run bootstrap
```

## 9.4 `scripts/download-sources.mjs`

Purpose:

Download enabled upstream source repositories.

Required behavior:

1. Read `sources/manifest.json`.
2. For each enabled source:
   - Validate URL.
   - Validate destination is inside `external/sources/`.
   - Refuse if `execute` is not `false`.
   - Clone repository if destination does not exist.
   - Fetch latest if destination exists and is a git repo.
   - Checkout configured branch.
   - Record commit hash.
3. Write `sources/source-lock.json`.
4. Never execute code from downloaded repositories.
5. Never run package install commands inside downloaded repositories.
6. Continue if one source fails.
7. Exit non-zero if required downloads fail.

Allowed shell commands:

```bash
git clone --depth 1 --branch <branch> <url> <destination>
git -C <destination> rev-parse HEAD
git -C <destination> fetch --depth 1 origin <branch>
git -C <destination> checkout <branch>
git -C <destination> pull --ff-only
```

Disallowed shell commands inside external sources:

```bash
npm install
pnpm install
yarn install
pip install
cargo build
go build
make
```

## 9.5 `scripts/audit-sources.mjs`

Purpose:

Audit source manifests and downloaded sources.

Required checks:

1. `sources/manifest.json` exists.
2. All source IDs are unique.
3. All enabled source destinations are under `external/sources/`.
4. All sources have `execute: false`.
5. `sources/source-lock.json` exists.
6. Downloaded sources are recorded.
7. No suspicious destination paths such as `..`, `/`, or home directories.
8. Create or update `docs/source-audit.md`.

Required output:

```text
sources audit: pass
```

or:

```text
sources audit: fail
```

## 9.6 `scripts/security-check.mjs`

Purpose:

Run basic repository safety checks.

Required checks:

1. No `.env` file is committed.
2. No obvious secret placeholders are filled with real-looking values.
3. No source destination escapes `external/sources/`.
4. No manifest source has `execute: true`.
5. No downloaded source is referenced as executable project code.
6. No global config paths are targeted.
7. No dangerous script commands are present in `package.json`.

Dangerous command patterns include:

```text
rm -rf /
sudo rm
curl ... | sh
wget ... | sh
chmod -R 777 /
```

Required output:

```text
security: pass
```

or:

```text
security: fail
```

## 9.7 `scripts/sync-agent-configs.mjs`

Purpose:

Synchronize universal agent instructions into agent-specific files.

Required behavior:

1. Read `AGENTS.md`.
2. Read rule files from `rules/`.
3. Update or verify:
   - `CLAUDE.md`
   - `GEMINI.md`
   - `docs/agents.md`
4. Support dry-run mode:

```bash
npm run sync -- --dry-run
```

5. In dry-run mode, do not write files.
6. Print what would change.

Optional future targets:

```text
.cursor/rules/
.github/copilot-instructions.md
opencode.md
```

The script must not modify global agent configuration.

## 9.8 `scripts/test.mjs`

Purpose:

Run project tests.

Required behavior:

1. Run smoke tests.
2. Verify required files.
3. Verify JSON files parse.
4. Verify key scripts exist.
5. Verify root docs exist.
6. Print test summary.

Required output:

```text
test: pass
```

or:

```text
test: fail
```

---

# 10. Required Utility Scripts

## 10.1 `scripts/utils/fs.mjs`

Must provide helpers for:

- Checking if a file exists.
- Checking if a directory exists.
- Ensuring a directory exists.
- Reading JSON.
- Writing JSON.
- Reading text.
- Writing text.
- Listing files.

## 10.2 `scripts/utils/git.mjs`

Must provide helpers for:

- Checking if `git` is available.
- Running safe git commands.
- Cloning repositories.
- Getting current commit hash.
- Validating git URLs.

## 10.3 `scripts/utils/log.mjs`

Must provide helpers for:

- Info logging.
- Warning logging.
- Error logging.
- Success logging.
- Step headers.

## 10.4 `scripts/utils/project.mjs`

Must provide helpers for:

- Resolving project root.
- Validating paths are inside project.
- Validating paths are inside `external/sources`.
- Converting project name to package name.
- Loading project metadata.

---

# 11. Required Rule Files

## 11.1 `rules/universal-rules.md`

```md
# Universal Rules

1. Read the task before editing.
2. Read relevant existing files before modifying them.
3. Prefer small, clear changes.
4. Do not invent project requirements.
5. Do not remove safety checks.
6. Update documentation when behavior changes.
7. Update tests when behavior changes.
8. Run validation before reporting completion.
9. Report what changed.
10. Report what was not completed.
```

## 11.2 `rules/safety-rules.md`

```md
# Safety Rules

1. Do not execute downloaded third-party code.
2. Do not install dependencies inside downloaded repositories.
3. Do not modify global user configuration.
4. Do not expose secrets.
5. Do not write outside the project directory.
6. Do not overwrite existing user work without permission.
7. Do not run destructive shell commands.
8. Do not turn reference sources into runtime dependencies without review.
9. Do not disable security checks to make tests pass.
10. When unsure, stop and ask.
```

## 11.3 `rules/coding-rules.md`

```md
# Coding Rules

1. Prefer simple code.
2. Prefer Node.js standard library for scripts.
3. Use ESM syntax.
4. Use clear names.
5. Validate inputs.
6. Fail with useful errors.
7. Keep scripts idempotent where practical.
8. Avoid hidden side effects.
9. Avoid unnecessary dependencies.
10. Keep generated files deterministic where practical.
```

## 11.4 `rules/git-rules.md`

```md
# Git Rules

1. Do not rewrite history unless explicitly requested.
2. Do not force push.
3. Do not commit secrets.
4. Keep external sources isolated under `external/sources/`.
5. Do not create commits unless requested.
6. Show changed files before final response.
7. Prefer descriptive commit messages if commits are requested.
```

## 11.5 `rules/testing-rules.md`

```md
# Testing Rules

1. Add or update tests when behavior changes.
2. Run tests before reporting completion.
3. If tests cannot run, explain why.
4. Do not fake test results.
5. Keep smoke tests fast.
6. Test required project structure.
7. Test manifest parsing.
8. Test security checks.
```

## 11.6 `rules/source-rules.md`

```md
# Source Rules

1. External sources are reference material only.
2. Download external sources only into `external/sources/`.
3. Do not execute external source code.
4. Do not install dependencies inside external sources.
5. Do not import external source files automatically.
6. Record downloaded commits in `sources/source-lock.json`.
7. Audit sources after downloading.
8. Keep source manifests explicit.
```

---

# 12. Required Skill Files

## 12.1 `skills/planning.md`

```md
# Planning Skill

When planning work:

1. Restate the goal.
2. Identify files to inspect.
3. Identify files to change.
4. Identify risks.
5. Create a short checklist.
6. Execute in small steps.
7. Validate results.
```

## 12.2 `skills/debugging.md`

```md
# Debugging Skill

When debugging:

1. Reproduce the issue.
2. Read the error carefully.
3. Identify the smallest failing unit.
4. Inspect recent changes.
5. Form one hypothesis at a time.
6. Test the hypothesis.
7. Record the fix.
```

## 12.3 `skills/refactoring.md`

```md
# Refactoring Skill

When refactoring:

1. Preserve behavior.
2. Make tests pass before and after.
3. Change one concept at a time.
4. Prefer clarity over cleverness.
5. Remove dead code only when certain.
6. Update documentation if structure changes.
```

## 12.4 `skills/testing.md`

```md
# Testing Skill

When testing:

1. Run existing tests first.
2. Add smoke tests for new behavior.
3. Test expected success.
4. Test expected failure.
5. Keep tests deterministic.
6. Do not fake outputs.
```

## 12.5 `skills/documentation.md`

```md
# Documentation Skill

When documenting:

1. Explain purpose first.
2. Show quick start commands.
3. Document inputs and outputs.
4. Document safety rules.
5. Keep examples copy-pasteable.
6. Update docs when behavior changes.
```

## 12.6 `skills/security-review.md`

```md
# Security Review Skill

When reviewing security:

1. Check for secret exposure.
2. Check shell commands.
3. Check path traversal risks.
4. Check downloaded source handling.
5. Check permissions.
6. Check dependency changes.
7. Report unresolved risks.
```

---

# 13. Required Hook Files

## 13.1 `hooks/pre-task.md`

```md
# Pre-Task Hook

Before starting a task:

1. Read `task.md`.
2. Read `status.md`.
3. Read relevant rules in `rules/`.
4. Identify the intended change.
5. Identify validation commands.
```

## 13.2 `hooks/post-task.md`

```md
# Post-Task Hook

After completing a task:

1. Run validation.
2. Update `status.md`.
3. Update docs if needed.
4. Summarize changed files.
5. Summarize tests run.
6. Summarize known issues.
```

## 13.3 `hooks/pre-commit.md`

```md
# Pre-Commit Hook

Before committing:

1. Run:

```bash
npm run check
```

2. Verify no secrets are staged.
3. Verify no downloaded external source code is staged unless explicitly intended.
4. Verify documentation is updated.
5. Verify status is accurate.
```

---

# 14. Required MCP Config Files

## 14.1 `mcp-configs/README.md`

```md
# MCP Configs

This directory stores example Model Context Protocol configuration files.

These files are examples only.

Do not place secrets in this directory.

Do not modify global MCP configuration automatically.
```

## 14.2 `mcp-configs/example.mcp.json`

```json
{
  "mcpServers": {}
}
```

---

# 15. Required Memory Files

## 15.1 `memory/project-memory.md`

```md
# Project Memory

## Purpose

This file stores durable project context for future coding agents.

## Current Summary

This project is generated from `project_starter.md`.

## Important Files

- `project_starter.md`
- `AGENTS.md`
- `task.md`
- `status.md`
- `sources/manifest.json`

## Notes

Add long-lived project notes here.
```

## 15.2 `memory/decisions.md`

```md
# Decisions

Record architectural and process decisions here.

## Decision Log

No decisions recorded yet.
```

## 15.3 `memory/glossary.md`

```md
# Glossary

## Terms

### Project Starter

The boilerplate specification used to create this project.

### External Sources

Downloaded third-party repositories stored under `external/sources/`.

### Source Lock

The generated record of downloaded source commits.
```

---

# 16. Required Documentation Files

## 16.1 `docs/architecture.md`

```md
# Architecture

## Overview

This project is structured as an executable boilerplate.

Core areas:

- Root instruction files
- Automation scripts
- Source manifests
- Agent rules
- Documentation
- Tests
- External reference sources

## Design Principles

1. Source-of-truth contract in `project_starter.md`.
2. Simple Node.js scripts.
3. No required runtime dependencies.
4. External sources are isolated.
5. AI agents receive consistent instructions.
```

## 16.2 `docs/setup.md`

```md
# Setup

## Requirements

- Node.js 20 or newer
- npm
- git, if source downloading is enabled

## Install

No dependencies are required by default.

If dependencies are added later, run:

```bash
npm install
```

## Bootstrap

```bash
npm run bootstrap
```

## Validate

```bash
npm run check
```
```

## 16.3 `docs/usage.md`

```md
# Usage

## Bootstrap Project

```bash
npm run bootstrap
```

## Run Doctor

```bash
npm run doctor
```

## Download Sources

```bash
npm run sources:download
```

## Audit Sources

```bash
npm run sources:audit
```

## Run Security Check

```bash
npm run security
```

## Sync Agent Configs

```bash
npm run sync -- --dry-run
npm run sync
```

## Run Tests

```bash
npm run test
```

## Create a New Project

```bash
npm run create -- --name abc --path ../abc
```
```

## 16.4 `docs/source-audit.md`

Initial content:

```md
# Source Audit

## Status

Not yet run.

## Summary

Run:

```bash
npm run sources:audit
```

## Sources

No sources audited yet.
```

## 16.5 `docs/agents.md`

```md
# Agents

## Supported Agents

This project provides guidance for:

- Claude Code
- Codex
- Gemini CLI
- Cursor
- OpenCode
- GitHub Copilot

## Universal Instructions

All agents should read:

1. `project_starter.md`
2. `AGENTS.md`
3. `task.md`
4. `status.md`

## Safety

Agents must not:

- Execute downloaded third-party code.
- Modify global configuration.
- Expose secrets.
- Write outside the project directory.
```

## 16.6 `docs/troubleshooting.md`

```md
# Troubleshooting

## `npm run doctor` fails

Check that all required files and directories exist.

## Source download fails

Check:

1. Network access.
2. Git availability.
3. Source URL correctness.
4. Branch name correctness.

If network is unavailable, continue local work and run later:

```bash
npm run sources:download
```

## Security check fails

Read the reported issue and fix it.

Do not bypass security checks without understanding the risk.

## Sync dry-run reports changes

Run:

```bash
npm run sync
```

Then run:

```bash
npm run check
```
```

## 16.7 `docs/changelog.md`

```md
# Changelog

## 0.1.0

Initial generated project structure.
```

---

# 17. Required Tests

## 17.1 `tests/smoke.test.mjs`

Purpose:

Smoke test project structure.

Required checks:

1. Root files exist.
2. Required directories exist.
3. JSON files parse.
4. Package scripts exist.
5. Source manifest is valid.
6. Safety rules exist.
7. Scripts exist.

The file may be executed by `scripts/test.mjs`.

## 17.2 `tests/fixtures/README.md`

```md
# Fixtures

This directory stores test fixtures.
```

---

# 18. Bootstrap Flow

When a user runs:

```bash
npm run bootstrap
```

The project must perform the following flow.

```text
start
  |
  v
doctor
  |
  v
sources:download
  |
  v
sources:audit
  |
  v
security
  |
  v
sync --dry-run
  |
  v
test
  |
  v
update status.md
  |
  v
print summary
end
```

If source downloading fails because of network issues, the bootstrap should continue with local checks and mark the download as blocked or failed.

---

# 19. Validation Requirements

The project is valid when:

1. `npm run doctor` passes.
2. `npm run security` passes.
3. `npm run sources:audit` passes.
4. `npm run sync -- --dry-run` passes.
5. `npm run test` passes.
6. `npm run bootstrap` completes with an accurate summary.
7. No safety rule is violated.
8. Required files exist.
9. Required directories exist.
10. JSON files parse successfully.

---

# 20. Agent Configuration Sync Rules

The project must support syncing universal instructions into agent-specific files.

## 20.1 Source Files

The source files are:

```text
AGENTS.md
rules/universal-rules.md
rules/safety-rules.md
rules/coding-rules.md
rules/source-rules.md
```

## 20.2 Target Files

The target files are:

```text
CLAUDE.md
GEMINI.md
docs/agents.md
```

Optional future targets:

```text
.cursor/rules/project.md
.github/copilot-instructions.md
opencode.md
```

## 20.3 Sync Behavior

The sync script must:

1. Read source files.
2. Check target files for required safety language.
3. In dry-run mode, report missing or outdated sections.
4. In write mode, update managed sections.
5. Avoid deleting user-written content outside managed sections.

Managed sections should use markers:

```md
<!-- BEGIN MANAGED AGENT RULES -->

Generated content here.

<!-- END MANAGED AGENT RULES -->
```

---

# 21. Source Download Policy

External repositories may be useful as examples or documentation references.

However, they are not trusted project code.

## 21.1 Allowed

The project may:

1. Clone enabled repositories.
2. Read their documentation.
3. Record their commit hashes.
4. Reference them in audits.
5. Compare their configuration patterns.

## 21.2 Not Allowed

The project must not:

1. Execute their scripts.
2. Install their dependencies.
3. Copy their code into runtime paths automatically.
4. Treat them as trusted dependencies.
5. Commit large downloaded repositories by default.
6. Use secrets found in them.
7. Modify them unless explicitly requested.

## 21.3 Location

All downloaded sources must live under:

```text
external/sources/
```

No source may be downloaded outside that directory.

---

# 22. Security Policy

## 22.1 Secrets

The project must not commit secrets.

Examples of forbidden committed secrets:

```text
API keys
OAuth tokens
Private keys
Session tokens
Database passwords
Cloud credentials
```

## 22.2 Environment Files

`.env` files are ignored.

An example file may be created:

```text
.env.example
```

But it must contain placeholders only.

## 22.3 Shell Commands

Scripts must avoid dangerous shell behavior.

Forbidden patterns:

```text
curl https://example.com/script.sh | sh
wget https://example.com/script.sh | bash
rm -rf /
sudo rm -rf
chmod -R 777 /
```

## 22.4 Path Safety

Scripts must validate paths.

No script may write outside the project root unless the user explicitly provides a target path for project creation.

Source downloads must remain inside:

```text
external/sources/
```

---

# 23. Status Update Requirements

After major operations, `status.md` must be updated.

Status table values:

```text
pass
fail
blocked
skipped
unknown
```

`status.md` should include:

1. Project name.
2. Project purpose.
3. Last updated timestamp.
4. Bootstrap status.
5. Known issues.
6. Next steps.

Example:

```md
# Status

## Project

Name: abc

Purpose: Example generated project.

## Last Updated

2026-01-01T00:00:00.000Z

## Bootstrap Status

| Check | Status | Notes |
|---|---|---|
| doctor | pass | Required files found |
| sources download | blocked | Network unavailable |
| source audit | pass | Manifest valid |
| security | pass | No obvious issues |
| sync dry-run | pass | Agent files up to date |
| tests | pass | Smoke tests passed |

## Known Issues

- Source download blocked by network.

## Next Steps

Run:

```bash
npm run sources:download
npm run bootstrap
```
```

---

# 24. Final Report Requirements for Coding Agents

After implementing or generating a project, the coding agent must report:

```text
Created project: <PROJECT_NAME>
Path: <OUTPUT_PATH>

Generated:
- package.json
- scripts/
- sources/
- rules/
- skills/
- hooks/
- mcp-configs/
- memory/
- docs/
- tests/
- agent configs

Validation:
- doctor: pass/fail/blocked/not run
- sources download: pass/fail/blocked/not run
- source audit: pass/fail/blocked/not run
- security: pass/fail/blocked/not run
- sync dry-run: pass/fail/blocked/not run
- tests: pass/fail/blocked/not run

Known issues:
- <issues or none>

Next command:
cd <OUTPUT_PATH>
npm run bootstrap
```

The agent must not claim a command passed unless it actually ran successfully.

---

# 25. Minimal Implementation Requirement

A generated project is minimally acceptable only if it includes:

```text
project_starter.md
README.md
package.json
AGENTS.md
CLAUDE.md
GEMINI.md
task.md
status.md
sources/manifest.json
sources/docs-manifest.json
sources/source-lock.json
scripts/bootstrap.mjs
scripts/doctor.mjs
scripts/create-project.mjs
scripts/download-sources.mjs
scripts/audit-sources.mjs
scripts/security-check.mjs
scripts/sync-agent-configs.mjs
scripts/test.mjs
rules/
skills/
hooks/
mcp-configs/
memory/
docs/
tests/
external/sources/.gitkeep
```

If any of these are missing, implementation is incomplete.

---

# 26. Recommended Implementation Order

Coding agents should implement in this order:

1. Create directories.
2. Create root metadata files.
3. Create manifests.
4. Create rules.
5. Create skills.
6. Create hooks.
7. Create memory files.
8. Create docs.
9. Create package.json.
10. Create utility scripts.
11. Create validation scripts.
12. Create bootstrap script.
13. Create create-project script.
14. Create tests.
15. Run doctor.
16. Run security.
17. Run tests.
18. Run bootstrap.
19. Update status.
20. Report final result.

---

# 27. Non-Goals

This boilerplate does not require:

1. A web app.
2. A backend server.
3. A database.
4. A frontend framework.
5. TypeScript.
6. Docker.
7. Kubernetes.
8. Cloud deployment.
9. Runtime third-party dependencies.
10. Automatic global configuration of AI tools.

These may be added by downstream projects, but they are not required by the boilerplate.

---

# 28. Extension Points

Downstream projects may add:

```text
src/
app/
packages/
services/
web/
api/
cli/
config/
.github/
.cursor/
.vscode/
```

They may also add:

```text
TypeScript
ESLint
Prettier
Vitest
Jest
Playwright
Docker
CI workflows
Release workflows
Deployment configs
```

If these are added, documentation and tests should be updated.

---

# 29. Example Create-New-Project Prompt

Use this prompt to create a project named `abc`.

```text
Create a new project named abc based on ./project_starter.md.

Create it at:

./abc

Use ./project_starter.md as the source-of-truth implementation contract.

Project purpose:

AI coding-agent starter repository for bootstrapping agent-ready projects.

Primary stack:

Node.js 20+, plain JavaScript, no runtime dependencies.

Required agent support:
- Claude Code
- Codex
- Gemini CLI
- Cursor
- OpenCode
- GitHub Copilot

You must:
1. Read project_starter.md fully.
2. Create ./abc.
3. Generate the full required project structure.
4. Copy project_starter.md into ./abc/project_starter.md.
5. Create all required files.
6. Create all required scripts.
7. Create all required docs.
8. Create all required tests.
9. Download enabled upstream sources into ./abc/external/sources/.
10. Generate ./abc/sources/source-lock.json.
11. Generate ./abc/docs/source-audit.md.
12. Run npm run bootstrap from inside ./abc.
13. Update ./abc/status.md.
14. Report final pass/fail status.

Do not execute downloaded third-party code.

If network or shell access is unavailable, create all local files anyway and mark downloads as blocked.
```

---

# 30. Example Self-Bootstrap Prompt

Use this prompt to implement the boilerplate itself.

```text
Implement this repository according to ./project_starter.md.

Use ./project_starter.md as the complete source-of-truth implementation contract.

Create all required files, directories, manifests, scripts, docs, tests, rules, skills, hooks, memory files, and agent configuration files.

Then run:

npm run bootstrap

If network is unavailable, continue local implementation and mark source downloads as blocked in status.md.

Do not execute downloaded third-party code.
```

---

# 31. Completion Definition

The project is complete when:

1. All required files exist.
2. All required scripts exist.
3. `npm run doctor` passes.
4. `npm run security` passes.
5. `npm run sources:audit` passes.
6. `npm run sync -- --dry-run` passes.
7. `npm run test` passes.
8. `npm run bootstrap` has been run or clearly marked blocked.
9. `status.md` is accurate.
10. The final report is honest and complete.

---

# 32. Final Instruction to Coding Agents

If you are a coding agent reading this file:

1. Do not summarize this file instead of implementing it.
2. Do not create only Markdown files.
3. Do not skip executable scripts.
4. Do not skip tests.
5. Do not skip safety checks.
6. Do not execute downloaded third-party code.
7. Do not modify files outside the project directory.
8. If you cannot run commands, say so clearly.
9. If network access is unavailable, mark source downloading as blocked.
10. Always update `status.md`.
11. Always provide a final report with actual validation results.

End of `project_starter.md`.
