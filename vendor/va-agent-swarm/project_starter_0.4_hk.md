# project_starter

> 繁體中文（香港）版本。為保留技術準確性，檔名、指令、JSON key 與大部分程式碼區塊維持原文。

## 目的

`project_starter` 是一份可重用的樣板規格，用來建立具備 AI 編碼代理支援、來源下載、專案 bootstrap、驗證、文件、安全規則及可重複自動化能力的新軟件專案。

此檔案是**唯一真實來源的實作契約**。

編碼代理必須能夠讀取此檔案，並據此建立一個完整且可執行的 starter 專案。

產生出來的專案不得只有文件；它必須包含可運作的腳本、清單、驗證指令、代理設定檔、文件檔案及安全控制。

---

# 1. 專案模式

`project_starter.md` 支援兩種主要模式。

## 1.1 自我啟動模式

當你要實作這個樣板儲存庫本身時，請使用此模式。

範例提示：

```text
Implement project_starter.md in the current repository.

Use project_starter.md as the source-of-truth implementation contract.

Create all required files, directories, scripts, manifests, docs, tests, and agent configuration files.

Then run:

npm run bootstrap
```

預期結果：

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

## 1.2 建立新專案模式

當你要根據此樣板建立新專案時，請使用此模式。

範例提示：

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

預期結果：

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

# 2. 使用者應如何要求編碼代理使用此檔案

使用者可以使用以下提示。

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Create the new project at:

<OUTPUT_PATH>

把 project_starter.md 視為完整的唯一真實來源實作契約。

專案用途：

<PROJECT_PURPOSE>

主要技術堆疊：

<STACK>

所需代理支援：
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

安全要求：
- Do not execute downloaded third-party code.
- Do not install packages inside downloaded third-party repositories.
- Do not import downloaded third-party code automatically.
- Do not modify global user configuration.
- Do not use secrets unless explicitly provided.
- Do not overwrite existing files without permission.

如果無法使用網絡或 shell：
- Still create all project files.
- Still create all scripts.
- Mark source downloading as blocked in status.md.
- Tell the user to run:

cd <OUTPUT_PATH>
npm run bootstrap
```

---

# 3. 所需輸入變數

編碼代理可能會從使用者收到以下變數。

| 變數 | 說明 | 預設值 |
|---|---|---|
| `PROJECT_NAME` | 產生出來的專案名稱 | `project_starter_generated` |
| `OUTPUT_PATH` | Directory where the generated project should be created | `./project_starter_generated` |
| `PROJECT_PURPOSE` | 專案用途的簡短描述 | `AI coding-agent starter repository` |
| `STACK` | Main technology stack | `Node.js 20+, plain JavaScript, no runtime dependencies for bootstrap scripts` |
| `DOWNLOAD_SOURCES` | Whether to download configured upstream sources | `true` |
| `AGENT_SUPPORT` | Supported coding agents | `claude,codex,gemini,cursor,opencode,copilot` |
| `PACKAGE_MANAGER` | JavaScript package manager | `npm` |
| `LICENSE` | 產生專案所用授權 | `MIT` |

If a required value is missing, use the default value.

---

# 4. 編碼代理的所需行為

當編碼代理實作此規格時，必須遵守以下規則。

## 4.1 一般規則

編碼代理必須：

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

## 4.2 安全規則

編碼代理不得：

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

## 4.3 如果輸出目錄已存在

If `OUTPUT_PATH` already exists and is not empty, the coding agent must stop and ask for permission before continuing.

允許的例外情況：

If the user explicitly says to overwrite or update the existing directory, the agent may proceed, but must preserve important user-created files when possible.

---

# 5. 所需專案結構

產生出來的專案必須包含以下結構。

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

# 6. 所需的 `package.json`

產生出來的專案必須包含 `package.json`。

範例：

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

規則：

1. `name` must be a package-safe version of `PROJECT_NAME`.
2. `description` must match `PROJECT_PURPOSE`.
3. `type` must be `module`.
4. Runtime dependencies should be empty unless needed.
5. Scripts must work on macOS, Linux, and Windows where practical.

---

# 7. 所需根目錄檔案

## 7.1 `README.md`

產生出來的 `README.md` 必須包含：

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

This project includes configuration and instructions f或：

- Claude Code
- Codex
- Gemini CLI
- Cursor
- OpenCode
- GitHub Copilot

See `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `docs/agents.md`.

## 安全

Downloaded external sources are stored in:

```text
external/sources/
```

Do not execute downloaded third-party code unless explicitly reviewed.
```

## 7.2 `AGENTS.md`

`AGENTS.md` 是編碼代理通用的指示檔案。

它必須包含：

```md
# AGENTS.md

## Project

Project name: <PROJECT_NAME>

專案用途： <PROJECT_PURPOSE>

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

`CLAUDE.md` 必須包含針對 Claude 的專用指引。

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

`GEMINI.md` 必須包含針對 Gemini 的專用指引。

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

`task.md` 用來追蹤目前任務。

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

`status.md` 用來記錄目前實作狀態。

```md
# Status

## Project

名稱： <PROJECT_NAME>

用途： <PROJECT_PURPOSE>

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

所需 `.gitignore`：

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

所需 `.editorconfig`：

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

# 8. 所需來源清單

## 8.1 `sources/manifest.json`

此檔案列出可作為參考資料下載的上游儲存庫。

預設值 example:

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

規則：

1. Each source must have a unique `id`.
2. Each source must have `enabled`.
3. Each source must have `url`.
4. Each source must have `destination`.
5. Each source must have `execute: false`.
6. Disabled sources must not be downloaded unless enabled by the user.
7. Downloaded sources are for reference only.

## 8.2 `sources/docs-manifest.json`

此檔案列出文件參考來源。

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

此檔案由 `scripts/download-sources.mjs` 產生。

初始內容：

```json
{
  "version": 1,
  "generatedAt": null,
  "sources": []
}
```

產生出來的項目應包括：

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

允許的狀態：

```text
downloaded
skipped
failed
blocked
```

---

# 9. 所需腳本

所有腳本都必須使用現代 Node.js ESM 語法撰寫，除非另有需要，否則只可使用 Node.js 標準函式庫。

## 9.1 `scripts/bootstrap.mjs`

用途：

Run the complete project bootstrap flow.

所需行為：

1. Run `doctor`.
2. Run `sources:download`.
3. Run `sources:audit`.
4. Run `security`.
5. Run `sync -- --dry-run`.
6. Run `test`.
7. Update `status.md`.
8. Print final summary.

等效指令：

```bash
npm run doctor
npm run sources:download
npm run sources:audit
npm run security
npm run sync -- --dry-run
npm run test
```

失敗時的行為：

- If one step fails, record it.
- Continue when safe.
- Exit non-zero if any required step fails.
- If network is unavailable, mark source download as blocked but continue local checks.

## 9.2 `scripts/doctor.mjs`

用途：

Validate local project health.

所需檢查：

1. Node.js version is at least 20.
2. Required directories exist.
3. Required files exist.
4. `package.json` is valid JSON.
5. `sources/manifest.json` is valid JSON.
6. `sources/docs-manifest.json` is valid JSON.
7. Required npm scripts exist.
8. `external/sources/` exists.
9. No required root files are missing.

應輸出：

```text
doct或： pass
```

或：

```text
doct或： fail
```

## 9.3 `scripts/create-project.mjs`

用途：

Create a new project from this boilerplate.

Required CLI options:

```bash
node scripts/create-project.mjs --name abc --path ../abc
node scripts/create-project.mjs --name abc --path ../abc --purpose "My project"
node scripts/create-project.mjs --name abc --path ../abc --stack "Node.js, TypeScript"
node scripts/create-project.mjs --name abc --path ../abc --no-download
node scripts/create-project.mjs --name abc --path ../abc --force
```

所需行為：

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

所需輸出：

```text
Created project: abc
Path: ../abc

Next commands:
cd ../abc
npm run bootstrap
```

## 9.4 `scripts/download-sources.mjs`

用途：

Download enabled upstream source repositories.

所需行為：

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

用途：

Audit source manifests and downloaded sources.

所需檢查：

1. `sources/manifest.json` exists.
2. All source IDs are unique.
3. All enabled source destinations are under `external/sources/`.
4. All sources have `execute: false`.
5. `sources/source-lock.json` exists.
6. Downloaded sources are recorded.
7. No suspicious destination paths such as `..`, `/`, or home directories.
8. Create or update `docs/source-audit.md`.

所需輸出：

```text
sources audit: pass
```

或：

```text
sources audit: fail
```

## 9.6 `scripts/security-check.mjs`

用途：

Run basic repository safety checks.

所需檢查：

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

所需輸出：

```text
security: pass
```

或：

```text
security: fail
```

## 9.7 `scripts/sync-agent-configs.mjs`

用途：

Synchronize universal agent instructions into agent-specific files.

所需行為：

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

用途：

Run project tests.

所需行為：

1. Run smoke tests.
2. Verify required files.
3. Verify JSON files parse.
4. Verify key scripts exist.
5. Verify root docs exist.
6. Print test summary.

所需輸出：

```text
test: pass
```

或：

```text
test: fail
```

---

# 10. 所需工具腳本

## 10.1 `scripts/utils/fs.mjs`

Must provide helpers f或：

- Checking if a file exists.
- Checking if a directory exists.
- Ensuring a directory exists.
- Reading JSON.
- Writing JSON.
- Reading text.
- Writing text.
- Listing files.

## 10.2 `scripts/utils/git.mjs`

Must provide helpers f或：

- Checking if `git` is available.
- Running safe git commands.
- Cloning repositories.
- Getting current commit hash.
- Validating git URLs.

## 10.3 `scripts/utils/log.mjs`

Must provide helpers f或：

- Info logging.
- Warning logging.
- Error logging.
- Success logging.
- Step headers.

## 10.4 `scripts/utils/project.mjs`

Must provide helpers f或：

- Resolving project root.
- Validating paths are inside project.
- Validating paths are inside `external/sources`.
- Converting project name to package name.
- Loading project metadata.

---

# 11. 所需規則檔案

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

# 12. 所需技能檔案

## 12.1 `skills/planning.md`

```md
# Planning Skill

規劃工作時：

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

除錯時：

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

重構時：

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

測試時：

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

撰寫文件時：

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

進行安全審查時：

1. Check for secret exposure.
2. Check shell commands.
3. Check path traversal risks.
4. Check downloaded source handling.
5. Check permissions.
6. Check dependency changes.
7. Report unresolved risks.
```

---

# 13. 所需 Hook 檔案

## 13.1 `hooks/pre-task.md`

```md
# Pre-Task Hook

開始任務前：

1. Read `task.md`.
2. Read `status.md`.
3. Read relevant rules in `rules/`.
4. Identify the intended change.
5. Identify validation commands.
```

## 13.2 `hooks/post-task.md`

```md
# Post-Task Hook

完成任務後：

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

提交前：

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

# 14. 所需 MCP 設定檔

## 14.1 `mcp-configs/README.md`

```md
# MCP Configs

此目錄用來存放 Model Context Protocol 設定檔範例。

這些檔案僅為範例。

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

# 15. 所需記憶檔案

## 15.1 `memory/project-memory.md`

```md
# Project Memory

## 目的

此檔案用來儲存可供未來編碼代理使用的長期專案上下文。

## Current Summary

This project is generated from `project_starter.md`.

## 重要 Files

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

在此記錄架構與流程決策。

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

# 16. 所需文件檔案

## 16.1 `docs/architecture.md`

```md
# Architecture

## Overview

此專案被設計成一個可執行的樣板。

核心區域：

- Root instruction files
- Automation scripts
- Source manifests
- Agent rules
- Documentation
- Tests
- External reference sources

## 設計原則

1. Source-of-truth contract in `project_starter.md`.
2. Simple Node.js scripts.
3. No required runtime dependencies.
4. External sources are isolated.
5. AI agents receive consistent instructions.
```

## 16.2 `docs/setup.md`

```md
# Setup

## 需求

- Node.js 20 or newer
- npm
- git, if source downloading is enabled

## 安裝

No dependencies are required by default.

If dependencies are added later, run:

```bash
npm install
```

## Bootstrap

```bash
npm run bootstrap
```

## 驗證

```bash
npm run check
```
```

## 16.3 `docs/usage.md`

```md
# Usage

## 啟動專案

```bash
npm run bootstrap
```

## 執行 Doctor

```bash
npm run doctor
```

## 下載來源

```bash
npm run sources:download
```

## 審核來源

```bash
npm run sources:audit
```

## 執行安全檢查

```bash
npm run security
```

## 同步代理設定

```bash
npm run sync -- --dry-run
npm run sync
```

## 執行測試

```bash
npm run test
```

## 建立新專案

```bash
npm run create -- --name abc --path ../abc
```
```

## 16.4 `docs/source-audit.md`

初始內容：

```md
# Source Audit

## 狀態

尚未執行。

## Summary

Run:

```bash
npm run sources:audit
```

## Sources

尚未審核任何來源。
```

## 16.5 `docs/agents.md`

```md
# Agents

## 支援的代理

This project provides guidance f或：

- Claude Code
- Codex
- Gemini CLI
- Cursor
- OpenCode
- GitHub Copilot

## 通用指示

All agents should read:

1. `project_starter.md`
2. `AGENTS.md`
3. `task.md`
4. `status.md`

## 安全

Agents must not:

- Execute downloaded third-party code.
- Modify global configuration.
- Expose secrets.
- Write outside the project directory.
```

## 16.6 `docs/troubleshooting.md`

```md
# Troubleshooting

## `npm run doctor` 失敗

Check that all required files and directories exist.

## 來源下載失敗

Check:

1. Network access.
2. Git availability.
3. Source URL correctness.
4. Branch name correctness.

If network is unavailable, continue local work and run later:

```bash
npm run sources:download
```

## 安全檢查失敗

Read the reported issue and fix it.

Do not bypass security checks without understanding the risk.

## sync dry-run 回報有變更

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

# 17. 所需測試

## 17.1 `tests/smoke.test.mjs`

用途：

對專案結構進行煙霧測試。

所需檢查：

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

此目錄用來存放測試 fixture。
```

---

# 18. Bootstrap 流程

當使用者執行以下指令時：

```bash
npm run bootstrap
```

專案必須執行以下流程。

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

# 19. 驗證需求

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

# 20. 代理設定同步規則

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

# 21. 來源下載政策

外部儲存庫可作為範例或文件參考來源。

然而，它們並不是可信任的專案程式碼。

## 21.1 Allowed

專案可以：

1. Clone enabled repositories.
2. Read their documentation.
3. Record their commit hashes.
4. Reference them in audits.
5. Compare their configuration patterns.

## 21.2 Not Allowed

專案不得：

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

# 22. 安全政策

## 22.1 Secrets

專案不得提交任何秘密資訊。

禁止提交的秘密資訊範例：

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

腳本必須驗證路徑。

No script may write outside the project root unless the user explicitly provides a target path for project creation.

Source downloads must remain inside:

```text
external/sources/
```

---

# 23. 狀態更新要求

完成主要操作後，必須更新 `status.md`。

狀態表可使用的值：

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

範例：

```md
# Status

## Project

名稱： abc

用途： Example generated project.

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

# 24. 編碼代理的最終報告要求

在實作或產生專案後，編碼代理必須回報：

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
- doct或： pass/fail/blocked/not run
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

除非指令實際成功執行，否則代理不得聲稱它已通過。

---

# 25. 最低實作要求

只有在包含以下項目時，產生出來的專案才算最低可接受。

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

如果當中有任何一項缺失，實作即屬不完整。

---

# 26. 建議實作順序

建議編碼代理按以下順序實作：

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

# 27. 非目標

此樣板不要求：

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

這些可由下游專案自行加入，但不是此樣板的必要要求。

---

# 28. 延伸點

下游專案可以加入：

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

亦可以加入：

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

如果加入這些項目，應同步更新文件和測試。

---

# 29. 建立新專案提示範例

使用以下提示建立名為 `abc` 的專案。

```text
Create a new project named abc based on ./project_starter.md.

Create it at:

./abc

Use ./project_starter.md as the source-of-truth implementation contract.

專案用途：

AI coding-agent starter repository for bootstrapping agent-ready projects.

主要技術堆疊：

Node.js 20+, plain JavaScript, no runtime dependencies.

所需代理支援：
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

# 30. 自我啟動提示範例

使用以下提示來實作此樣板本身。

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

# 31. 完成定義

在以下情況下，專案才算完成：

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

# 32. 對編碼代理的最終指示

如果你是正在閱讀此檔案的編碼代理：

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

`project_starter.md` 完。
