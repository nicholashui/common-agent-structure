# project_starter

> 繁體中文（香港）版本。為保留技術準確性，檔名、指令、JSON key 與大部分程式碼區塊維持原文。

**專案名稱：** `project_starter`  
**用途：** 建立一個可執行的 starter 儲存庫，用來下載、審核、整理及同步 Claude Code、Cursor、Codex、Gemini CLI、OpenCode、Grok Build、GitHub Copilot 及相關代理框架的 AI 編碼代理設定來源。  
**目前規格版本：** `1.1.0-merged-bootstrap`  
**最後更新：** 2026-06-09  

---

## 如何配合編碼代理使用此樣板

此儲存庫是一份樣板規格。

使用者可以透過以下提示，要求編碼代理根據此檔案建立新專案：

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Use project_starter.md as the source-of-truth implementation contract.

Create the new project at:

<OUTPUT_PATH>

The project purpose is:

<PROJECT_PURPOSE>

The primary stack is:

<STACK>

You must:
1. Read project_starter.md fully.
2. Create the new project directory.
3. Create all directories and files required by project_starter.md.
4. Replace boilerplate metadata with the new project name and purpose.
5. Copy project_starter.md into the new project.
6. Create package.json.
7. Create source manifests.
8. Create executable scripts.
9. Create rule files.
10. Create docs.
11. Download all enabled upstream GitHub repositories into external/sources/.
12. Generate sources/source-lock.json.
13. Generate docs/source-audit.md.
14. Run bootstrap validation.
15. Update status.md.
16. Report final pass/fail status.

不要只總結這些指示。
不要只撰寫 Markdown。
請建立一個可實際執行的專案。

如果無法使用網絡或 shell，仍然要建立所有專案檔案，並在 status.md 中標示來源下載已被阻擋。

## 專案模式

此規格支援兩種有效的實作模式：

1. **自我啟動模式**：在目前儲存庫中實作這個 starter 儲存庫本身。
2. **建立新專案模式**：根據此規格，在目標目錄中產生一個新的下游專案。

自我啟動模式範例提示：

```text
Implement project_starter.md in the current repository.

Use project_starter.md as the complete implementation contract.

Create all required files, directories, manifests, scripts, docs, tests, and agent configuration files.

Then run:

npm run bootstrap
```

建立新專案模式範例提示：

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Create it at:

<OUTPUT_PATH>

Use project_starter.md as the complete implementation contract.

Create a working executable project, not just Markdown.

Download all enabled sources unless told not to.

Then run:

npm run bootstrap
```

## 所需輸入變數

在產生下游專案時，編碼代理可能會收到以下變數：

| 變數 | 說明 | 預設值 |
|---|---|---|
| `PROJECT_NAME` | 產生出來的專案名稱 | `project_starter_generated` |
| `OUTPUT_PATH` | 產生專案的目標目錄 | `./project_starter_generated` |
| `PROJECT_PURPOSE` | 專案用途的簡短描述 | `AI coding-agent starter repository` |
| `STACK` | 主要技術堆疊 | `Node.js 20+, plain JavaScript, no runtime dependencies for bootstrap scripts` |
| `DOWNLOAD_SOURCES` | 是否下載已啟用的上游來源 | `true` |
| `AGENT_SUPPORT` | 支援的編碼代理 | `claude,cursor,codex,gemini,opencode,copilot,grok-build` |
| `PACKAGE_MANAGER` | 主要 JavaScript 套件管理工具 | `npm` |
| `LICENSE` | 產生專案所用授權 | `MIT` |

如果缺少必要值，編碼代理應使用預設值。

## 現有輸出目錄規則

If `OUTPUT_PATH` already exists and is non-empty, the coding agent must stop and ask for permission before overwriting or updating it.

允許的例外情況：

- If the user explicitly says to overwrite or update the existing directory, the agent may proceed, but should preserve important user-created files when possible.

## 0. 對編碼代理的關鍵指示

此檔案**不只是文件**。

當編碼代理收到此檔案並被要求實作時，代理**必須**建立一個真正可執行的專案。

代理**不得**只寫完 Markdown 就停止。

代理**必須**：

1. Create the `project_starter/` repository structure.
2. Create `package.json`.
3. Create `sources/manifest.json`.
4. Create `sources/docs-manifest.json`.
5. Create `scripts/project-starter.mjs`.
6. Create `scripts/create-project.mjs`.
7. Create `scripts/source-download.mjs`.
8. Create `scripts/source-audit.mjs`.
9. Create `scripts/doctor.mjs`.
10. Create `scripts/sync.mjs`.
11. Create `scripts/security.mjs`.
12. Download every enabled GitHub repository listed in `sources/manifest.json`.
13. Save downloaded repos under `external/sources/`.
14. Save download metadata to `sources/source-lock.json`.
15. Generate `docs/source-audit.md`.
16. Support both self-bootstrap and create-new-project workflows.
17. Run the bootstrap validation commands.
18. Report success or exact blockers.

If network access or shell execution is unavailable, the agent **MUST** say:

```text
BLOCKED: cannot download sources because network/shell execution is unavailable.
```

and still create all scripts and manifests so the human can run:

```bash
npm run bootstrap
```

later.

---

## 1. 不可妥協的成果

After implementation, this command:

```bash
npm run bootstrap
```

**MUST** perform this flow:

```text
doctor
→ create required directories
→ validate sources/manifest.json
→ clone/update all enabled GitHub sources
→ write sources/source-lock.json
→ generate docs/source-audit.md
→ run security smoke checks
→ run sync dry-run
→ run tests
```

除非來源儲存庫已實際下載至以下位置，否則此專案**不算完成**：

```text
external/sources/
```

---

## 2. 所需儲存庫結構

編碼代理**必須**建立以下結構：

```text
project_starter/
├── project_starter.md
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── package.json
├── task.md
├── status.md
├── .gitignore
├── .editorconfig
├── sources/
│   ├── manifest.json
│   ├── docs-manifest.json
│   ├── source-lock.json
│   └── README.md
├── external/
│   ├── .gitignore
│   └── sources/
├── scripts/
│   ├── project-starter.mjs
│   ├── create-project.mjs
│   ├── source-download.mjs
│   ├── source-audit.mjs
│   ├── doctor.mjs
│   ├── sync.mjs
│   ├── security.mjs
│   ├── review.mjs
│   ├── adapters/
│   │   ├── claude.mjs
│   │   ├── cursor.mjs
│   │   ├── codex.mjs
│   │   ├── gemini.mjs
│   │   ├── opencode.mjs
│   │   ├── grok-build.mjs
│   │   └── copilot.mjs
│   └── lib/
│       ├── git.mjs
│       ├── fs-safe.mjs
│       ├── manifest.mjs
│       └── report.mjs
├── rules/
│   ├── manifest.json
│   ├── 00-constitution.md
│   ├── 10-karpathy.md
│   ├── 20-sdd.md
│   ├── 30-security.md
│   ├── 40-testing.md
│   ├── 50-token-efficiency.md
│   └── 60-human-approval.md
├── skills/
│   ├── manifest.json
│   ├── planning/
│   ├── implementation/
│   ├── testing/
│   ├── review/
│   ├── security/
│   ├── memory/
│   └── lifecycle/
├── hooks/
│   ├── manifest.json
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
├── docs/
│   ├── installation.md
│   ├── usage.md
│   ├── agents.md
│   ├── architecture.md
│   ├── source-audit.md
│   ├── security.md
│   ├── sync.md
│   ├── troubleshooting.md
│   └── changelog.md
├── examples/
│   ├── sdd-feature-workflow/
│   ├── self-review-workflow/
│   ├── skill-suggestion-workflow/
│   └── cross-agent-sync-workflow/
└── tests/
    ├── fixtures/
    ├── source-download.test.mjs
    ├── source-audit.test.mjs
    ├── sync.test.mjs
    ├── manifest.test.mjs
    └── adapters.test.mjs
```

---

## 3. 所需的 `package.json`

編碼代理**必須**建立以下 `package.json`，或功能等同且更完整的版本：

```json
{
  "name": "project_starter",
  "version": "1.1.0-merged-bootstrap",
  "private": true,
  "type": "module",
  "description": "Executable starter repo for downloading, auditing, curating, and syncing AI coding-agent harness sources.",
  "scripts": {
    "bootstrap": "node scripts/project-starter.mjs bootstrap",
    "create": "node scripts/project-starter.mjs create",
    "init": "node scripts/project-starter.mjs init",
    "doctor": "node scripts/doctor.mjs",
    "sources:download": "node scripts/source-download.mjs",
    "sources:update": "node scripts/source-download.mjs --update",
    "sources:check": "node scripts/source-download.mjs --check",
    "sources:audit": "node scripts/source-audit.mjs",
    "sync": "node scripts/sync.mjs",
    "sync:check": "node scripts/sync.mjs --check",
    "security": "node scripts/security.mjs",
    "review": "node scripts/review.mjs",
    "test": "node --test tests/*.test.mjs",
    "format": "node scripts/project-starter.mjs format"
  },
  "engines": {
    "node": ">=20.0.0"
  }
}
```

第一版實作不需要任何套件相依；只使用 Node 內建模組即可。

---

## 4. 強制性的 GitHub 來源下載清單

編碼代理**必須**建立以下完全指定的檔案：

```text
sources/manifest.json
```

代理**必須**下載所有符合以下條件的來源：

```json
"enabled": true
```

代理**不得**在沒有說明的情況下略過任何已啟用來源。

如果必要來源失敗，指令必須以非零狀態碼結束。

Create `sources/manifest.json` with this content:

```json
{
  "schema_version": "1.0",
  "generated_from": "project_starter.md",
  "default_profile": "all",
  "download_root": "external/sources",
  "sources": [
    {
      "id": "ecc",
      "name": "ECC / Everything Claude Code",
      "url": "https://github.com/affaan-m/ECC.git",
      "target": "external/sources/ecc",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "core",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Primary cross-agent harness source: skills, agents, commands, hooks, rules, MCP conventions, security scanner references."
    },
    {
      "id": "anthropic-claude-code",
      "name": "Anthropic Claude Code",
      "url": "https://github.com/anthropics/claude-code.git",
      "target": "external/sources/anthropic-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code repository for docs, issues, release notes, and compatibility references."
    },
    {
      "id": "anthropic-claude-code-action",
      "name": "Anthropic Claude Code Action",
      "url": "https://github.com/anthropics/claude-code-action.git",
      "target": "external/sources/anthropic-claude-code-action",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub Action patterns for Claude Code automation, PR review, issue workflows, and CI integration."
    },
    {
      "id": "anthropic-skills",
      "name": "Anthropic Agent Skills",
      "url": "https://github.com/anthropics/skills.git",
      "target": "external/sources/anthropic-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Official Agent Skills examples, specification, templates, and skill packaging patterns."
    },
    {
      "id": "anthropic-claude-plugins-official",
      "name": "Anthropic Claude Plugins Official",
      "url": "https://github.com/anthropics/claude-plugins-official.git",
      "target": "external/sources/anthropic-claude-plugins-official",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code plugin marketplace structure and plugin manifest examples."
    },
    {
      "id": "openai-codex",
      "name": "OpenAI Codex CLI",
      "url": "https://github.com/openai/codex.git",
      "target": "external/sources/openai-codex",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Codex CLI source and AGENTS.md behavior reference."
    },
    {
      "id": "google-gemini-cli",
      "name": "Google Gemini CLI",
      "url": "https://github.com/google-gemini/gemini-cli.git",
      "target": "external/sources/google-gemini-cli",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Gemini CLI source for GEMINI.md, MCP, settings, and command compatibility."
    },
    {
      "id": "opencode",
      "name": "OpenCode",
      "url": "https://github.com/anomalyco/opencode.git",
      "target": "external/sources/opencode",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "OpenCode source for AGENTS.md, opencode config, agents, MCP, and plugin compatibility."
    },
    {
      "id": "modelcontextprotocol-servers",
      "name": "Model Context Protocol Servers",
      "url": "https://github.com/modelcontextprotocol/servers.git",
      "target": "external/sources/modelcontextprotocol-servers",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Current MCP server examples and server discovery references."
    },
    {
      "id": "modelcontextprotocol-registry",
      "name": "Model Context Protocol Registry",
      "url": "https://github.com/modelcontextprotocol/registry.git",
      "target": "external/sources/modelcontextprotocol-registry",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "MCP registry references for discovering MCP servers safely."
    },
    {
      "id": "github-mcp-server",
      "name": "GitHub MCP Server",
      "url": "https://github.com/github/github-mcp-server.git",
      "target": "external/sources/github-mcp-server",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub MCP server for GitHub issue, PR, repo, workflow, and code search integration."
    },
    {
      "id": "agents-md",
      "name": "AGENTS.md Specification",
      "url": "https://github.com/openai/agents.md.git",
      "target": "external/sources/agents-md",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "standard",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "AGENTS.md standard/reference for cross-agent repository instructions."
    },
    {
      "id": "andrej-karpathy-skills",
      "name": "Andrej Karpathy Skills",
      "url": "https://github.com/forrestchang/andrej-karpathy-skills.git",
      "target": "external/sources/andrej-karpathy-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "behavior-rules",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Karpathy-style behavioral rules: think before coding, simplicity, surgical changes, goal-driven execution."
    },
    {
      "id": "andrej-karpathy-skills-cursor-vscode",
      "name": "Andrej Karpathy Skills for Cursor and VS Code",
      "url": "https://github.com/mbeijen/andrej-karpathy-skills-cursor-vscode.git",
      "target": "external/sources/andrej-karpathy-skills-cursor-vscode",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "behavior-rules",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Cursor/VS Code rule-file adaptation of Karpathy-style behavior rules."
    },
    {
      "id": "claude-mem",
      "name": "Claude Mem",
      "url": "https://github.com/thedotmack/claude-mem.git",
      "target": "external/sources/claude-mem",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "memory",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Persistent memory architecture reference. Must not install automatically."
    },
    {
      "id": "superpowers",
      "name": "Superpowers",
      "url": "https://github.com/obra/superpowers.git",
      "target": "external/sources/superpowers",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "skills",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Composable software-development skill methodology for multiple coding agents."
    },
    {
      "id": "claude-code-best-practice",
      "name": "Claude Code Best Practice",
      "url": "https://github.com/shanraisshan/claude-code-best-practice.git",
      "target": "external/sources/claude-code-best-practice",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "best-practices",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community best-practice source for Claude Code agents, commands, skills, hooks, and workflows."
    },
    {
      "id": "awesome-claude-code",
      "name": "Awesome Claude Code",
      "url": "https://github.com/hesreallyhim/awesome-claude-code.git",
      "target": "external/sources/awesome-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Curated discovery list for Claude Code skills, hooks, commands, plugins, workflows, and tooling."
    },
    {
      "id": "awesome-agent-skills",
      "name": "Awesome Agent Skills",
      "url": "https://github.com/VoltAgent/awesome-agent-skills.git",
      "target": "external/sources/awesome-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Cross-agent discovery list for Claude Code, Codex, Gemini CLI, Cursor, and related skills."
    },
    {
      "id": "wshobson-agents",
      "name": "Claude Code Subagents by wshobson",
      "url": "https://github.com/wshobson/agents.git",
      "target": "external/sources/wshobson-agents",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "agents",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community Claude Code subagent definitions for specialist-agent patterns."
    },
    {
      "id": "vercel-agent-skills",
      "name": "Vercel Labs Agent Skills",
      "url": "https://github.com/vercel-labs/agent-skills.git",
      "target": "external/sources/vercel-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "skills",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Frontend, React, Next.js, and deployment-oriented agent skill patterns."
    },
    {
      "id": "awesome-cursorrules",
      "name": "Awesome Cursor Rules",
      "url": "https://github.com/PatrickJS/awesome-cursorrules.git",
      "target": "external/sources/awesome-cursorrules",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "cursor",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Cursor rule examples and discovery reference."
    },
    {
      "id": "cursor-security-rules",
      "name": "Cursor Security Rules",
      "url": "https://github.com/matank001/cursor-security-rules.git",
      "target": "external/sources/cursor-security-rules",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "security",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Security-focused Cursor rule examples."
    },
    {
      "id": "itgoyo-awesome-agent-skills",
      "name": "itgoyo Awesome Agent Skills",
      "url": "https://github.com/itgoyo/awesome-agent-skills.git",
      "target": "external/sources/itgoyo-awesome-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "optional",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Additional discovery index for popular agent-skills repositories."
    },
    {
      "id": "itgoyo-awesome-claude-code-skills",
      "name": "itgoyo Awesome Claude Code Skills",
      "url": "https://github.com/itgoyo/awesome-claude-code-skills.git",
      "target": "external/sources/itgoyo-awesome-claude-code-skills",
      "type": "git",
      "enabled": true,
      "priority": "optional",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Top-starred Claude Code ecosystem repository index."
    },
    {
      "id": "subinium-awesome-claude-code",
      "name": "subinium Awesome Claude Code",
      "url": "https://github.com/subinium/awesome-claude-code.git",
      "target": "external/sources/subinium-awesome-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "optional",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Additional curated Claude Code discovery list."
    },
    {
      "id": "modelcontextprotocol-servers-archived",
      "name": "Model Context Protocol Servers Archived",
      "url": "https://github.com/modelcontextprotocol/servers-archived.git",
      "target": "external/sources/modelcontextprotocol-servers-archived",
      "type": "git",
      "enabled": false,
      "priority": "archived",
      "tier": "historical",
      "quarantine": true,
      "import_policy": "never-import",
      "purpose": "Historical MCP reference only. Do not download or use by default because it is archived."
    }
  ]
}
```

---

## 5. 強制性的文件來源清單

有些相關工具雖然有官方文件，但不一定需要複製 GitHub 儲存庫。

編碼代理**必須**建立：

```text
sources/docs-manifest.json
```

with this content:

```json
{
  "schema_version": "1.0",
  "docs": [
    {
      "id": "claude-code-docs",
      "name": "Claude Code Docs",
      "url": "https://code.claude.com/docs/en/features-overview",
      "target": "external/docs/claude-code-features-overview.md",
      "enabled": true,
      "purpose": "Claude Code feature loading: CLAUDE.md, skills, MCP, subagents, hooks."
    },
    {
      "id": "cursor-rules-docs",
      "name": "Cursor Rules Docs",
      "url": "https://docs.cursor.com/context/rules-for-ai",
      "target": "external/docs/cursor-rules.md",
      "enabled": true,
      "purpose": "Cursor project rules, AGENTS.md support, and .cursorrules legacy behavior."
    },
    {
      "id": "xai-grok-build-docs",
      "name": "xAI Grok Build Docs",
      "url": "https://docs.x.ai/build/overview",
      "target": "external/docs/xai-grok-build-overview.md",
      "enabled": true,
      "purpose": "Grok Build install, TUI, headless mode, ACP, skills, plugins, hooks, and MCP references."
    },
    {
      "id": "github-copilot-custom-instructions-docs",
      "name": "GitHub Copilot Custom Instructions Docs",
      "url": "https://docs.github.com/en/copilot",
      "target": "external/docs/github-copilot-docs.md",
      "enabled": true,
      "purpose": "GitHub Copilot custom instructions and coding-agent workflow references."
    },
    {
      "id": "modelcontextprotocol-docs",
      "name": "Model Context Protocol Docs",
      "url": "https://modelcontextprotocol.io",
      "target": "external/docs/modelcontextprotocol.md",
      "enabled": true,
      "purpose": "MCP concepts, protocol docs, client/server design, and safety references."
    }
  ]
}
```

The first version may create this file without downloading docs. The second version should implement `docs:download`.

---

## 6. external 目錄政策

編碼代理**必須**建立：

```text
external/.gitignore
```

with this content:

```gitignore
# Downloaded upstream repositories are intentionally not committed.
sources/
docs/
```

下載回來的上游儲存庫**不得**提交到此專案中。

Only curated, audited, attributed files may be copied into first-party project directories such as:

```text
rules/
skills/
hooks/
mcp-configs/
docs/
```

---

## 7. 來源下載行為

The coding agent **MUST** implement:

```text
scripts/source-download.mjs
```

### 7.1 所需指令

The script must support:

```bash
npm run sources:download
npm run sources:update
npm run sources:check
node scripts/source-download.mjs --profile all
node scripts/source-download.mjs --profile core
node scripts/source-download.mjs --profile official
node scripts/source-download.mjs --profile discovery
node scripts/source-download.mjs --dry-run
node scripts/source-download.mjs --strict
```

### 7.2 預設行為

This command:

```bash
npm run sources:download
```

MUST:

1. Read `sources/manifest.json`.
2. Select every source with `"enabled": true`.
3. Create `external/sources/`.
4. For each selected source:
   - If target does not exist, run a shallow clone.
   - If target exists and is a git repo, fetch and fast-forward update.
   - If target exists and is not a git repo, fail.
5. Record metadata in `sources/source-lock.json`.
6. Generate a human-readable summary.

### 7.3 所需 Git 指令

For a missing repo:

```bash
git clone --depth 1 <url> <target>
```

For an existing repo:

```bash
git -C <target> fetch --depth 1 origin
git -C <target> pull --ff-only
```

For metadata:

```bash
git -C <target> remote get-url origin
git -C <target> rev-parse HEAD
git -C <target> branch --show-current
git -C <target> log -1 --format=%cI
git -C <target> log -1 --format=%s
```

### 7.4 失敗規則

For `"priority": "required"`:

- clone failure = fatal
- update failure = fatal
- missing `.git` = fatal
- invalid URL = fatal

For `"priority": "optional"`:

- clone failure = non-fatal unless `--strict` is used
- failure must still be recorded in `sources/source-lock.json`

For `"enabled": false"`:

- must not download by default

### 7.5 安全規則

The downloader **MUST NOT**:

- run install scripts from downloaded repos,
- run `npm install` inside downloaded repos,
- run `curl | bash`,
- execute hooks from downloaded repos,
- copy repo content into active agent config automatically,
- write outside the project root.

The downloader **MUST ONLY** clone/update and inspect metadata.

---

## 8. 所需的來源鎖定格式

The coding agent **MUST** generate:

```text
sources/source-lock.json
```

範例結構：

```json
{
  "schema_version": "1.0",
  "generated_at": "2026-06-09T00:00:00.000Z",
  "sources": [
    {
      "id": "ecc",
      "name": "ECC / Everything Claude Code",
      "url": "https://github.com/affaan-m/ECC.git",
      "resolved_url": "https://github.com/affaan-m/ECC.git",
      "target": "external/sources/ecc",
      "status": "downloaded",
      "commit": "abc123",
      "branch": "main",
      "last_commit_at": "2026-06-09T00:00:00Z",
      "last_commit_subject": "example commit subject",
      "license_files": ["LICENSE"],
      "package_files": ["package.json"],
      "quarantine": false,
      "import_policy": "curated-only"
    }
  ],
  "failures": []
}
```

---

## 9. 所需的來源審核行為

The coding agent **MUST** implement:

```text
scripts/source-audit.mjs
```

This script must read:

```text
sources/manifest.json
sources/source-lock.json
```

and generate:

```text
docs/source-audit.md
```

審核檔案必須為每個來源包含一個區段：

```md
## ecc

- 名稱：
- URL:
- Target:
- Status:
- Commit:
- Branch:
- License files:
- Package files:
- Priority:
- Tier:
- Quarantine:
- Import policy:
- 用途：
- Selected components:
- Rejected components:
- Security notes:
```

### 9.1 所需審核規則

The audit **MUST** mark a source as unsafe for automatic import if:

- no license file exists,
- the repo contains install scripts that run remote commands,
- the repo contains suspicious postinstall scripts,
- the source is archived,
- the source requires credentials,
- the source modifies global agent configuration,
- the source includes MCP servers that require broad filesystem/network access.

### 9.2 首輪選定元件

The first audit pass should mark most repos as:

```text
Selected components: none yet
Rejected components: bulk import rejected until human review
```

Exception: small rule-only repos such as `andrej-karpathy-skills` may be selected for curated extraction after license verification.

---

## 10. Bootstrap 路由器

The coding agent **MUST** implement:

```text
scripts/project-starter.mjs
```

### 10.1 所需指令

```bash
node scripts/project-starter.mjs bootstrap
node scripts/project-starter.mjs create --name demo --path ../demo
node scripts/project-starter.mjs init
node scripts/project-starter.mjs format
```

### 10.2 Bootstrap 必須執行

`bootstrap` must run, in order:

```bash
npm run doctor
npm run sources:download
npm run sources:audit
npm run security
npm run sync -- --dry-run
npm run test
```

If any required command fails, bootstrap must fail.

### 10.3 create 指令行為

The router must also support create-new-project mode either directly or by delegating to:

```text
scripts/create-project.mjs
```

Recommended commands:

```bash
npm run create -- --name demo --path ../demo
npm run create -- --name demo --path ../demo --purpose "Example project"
npm run create -- --name demo --path ../demo --stack "Node.js 20+, TypeScript"
npm run create -- --name demo --path ../demo --no-download
npm run create -- --name demo --path ../demo --force
```

所需行為：

1. Parse CLI arguments for project name, output path, purpose, stack, download behavior, and overwrite mode.
2. Validate project name and output path.
3. Refuse to overwrite a non-empty target directory unless `--force` is provided or the user explicitly approved it.
4. Create the required directory structure.
5. Copy `project_starter.md` into the new project root.
6. Replace boilerplate metadata with project-specific values where this specification requires it.
7. Generate all required files, manifests, scripts, rules, docs, tests, and agent configuration files.
8. Optionally run source downloading unless `--no-download` is used or downloads are blocked.
9. Print clear next steps for the human.

---

## 11. Doctor 腳本

The coding agent **MUST** implement:

```text
scripts/doctor.mjs
```

It must check:

- Node version >= 20
- Git availability
- Current working directory
- Write permissions
- `sources/manifest.json` exists
- `external/` exists or can be created
- `scripts/` exists
- OS platform
- Symlink support if sync wants symlink mode

It must print:

```text
project_starter doctor

Node: OK
Git: OK
Manifest: OK
External dir: OK
OS: <platform>
Result: OK
```

or fail with clear messages.

---

## 12. 同步層

The coding agent **MUST** implement a first working sync framework, even if adapters are initially minimal.

Required command:

```bash
npm run sync -- --dry-run
```

It must generate or preview:

```text
AGENTS.md
CLAUDE.md
GEMINI.md
docs/agents.md
.github/copilot-instructions.md
.cursor/rules/project-starter.mdc
.claude/settings.json
.gemini/settings.json
.codex/
.opencode/
```

Generated files must include this header:

```text
<!-- AUTO-GENERATED by project_starter. Do not edit directly.
Source: rules/, skills/, hooks/, mcp-configs/
Run: npm run sync
-->
```

The sync layer should preserve user-written content outside managed sections when practical. Managed blocks should use markers such as:

```md
<!-- BEGIN MANAGED AGENT RULES -->
Generated content here.
<!-- END MANAGED AGENT RULES -->
```

---

## 13. 安全檢查腳本

The coding agent **MUST** implement:

```text
scripts/security.mjs
```

The first version must:

1. Scan downloaded repos for suspicious root-level scripts.
2. Detect `.env`, private keys, tokens, or certificates accidentally committed into this project.
3. Report MCP configs with broad filesystem access.
4. Warn on `curl | bash`, `irm ... | iex`, and postinstall scripts in downloaded sources.
5. Never execute downloaded scripts.

The first implementation can be a simple Node.js static scanner.

---

## 14. 所需的初始規則檔案

編碼代理**必須**建立：

```text
rules/00-constitution.md
rules/10-karpathy.md
rules/20-sdd.md
rules/30-security.md
rules/40-testing.md
rules/50-token-efficiency.md
rules/60-human-approval.md
```

### 14.1 `rules/00-constitution.md`

Must include:

```md
# Constitution

- Follow the user's goal exactly.
- Prefer simple, maintainable solutions.
- Make surgical changes.
- Do not perform destructive actions without approval.
- Do not install, execute, or import downloaded third-party code until audited.
- Run relevant tests or explain why tests were not run.
- Update status after major work.
```

### 14.2 `rules/10-karpathy.md`

Must include:

```md
# Karpathy-Style Agent Rules

- Think before coding.
- Do not assume hidden requirements.
- Prefer the simplest working solution.
- Avoid speculative abstractions.
- Change only what is necessary.
- Keep the goal visible.
- Verify the result.
```

### 14.3 `rules/60-human-approval.md`

Must include:

```md
# Human Approval

Human approval is required before:

- installing global packages,
- running remote install scripts,
- enabling MCP servers with credentials,
- copying third-party repo code into active agent configs,
- modifying hooks,
- deleting files,
- applying self-generated skill/rule changes.
```

---

## 15. 匯入政策

Downloading sources is mandatory.

Importing sources is **not automatic**.

The project must separate:

```text
downloaded source
audited source
curated import
generated adapter output
```

### 15.1 Downloaded Source

Location:

```text
external/sources/<source-id>/
```

Status:

```text
untrusted, ignored by git, never executed
```

### 15.2 Audited Source

Recorded in:

```text
docs/source-audit.md
sources/source-lock.json
```

Status:

```text
reviewed metadata, not yet imported
```

### 15.3 Curated Import

Allowed locations:

```text
rules/
skills/
hooks/
mcp-configs/
docs/attribution/
```

Requirements:

- license verified,
- source commit recorded,
- file checksum recorded,
- human approval if high-impact,
- no hidden install behavior.

### 15.4 Generated Adapter Output

Allowed locations:

```text
AGENTS.md
CLAUDE.md
GEMINI.md
.cursor/
.claude/
.codex/
.gemini/
.opencode/
.github/copilot-instructions.md
```

Must be reproducible by:

```bash
npm run sync
```

---

## 16. 所需測試

The coding agent **MUST** create Node test files.

Minimum tests:

```text
tests/manifest.test.mjs
tests/source-download.test.mjs
tests/source-audit.test.mjs
tests/sync.test.mjs
```

Tests must verify:

- `sources/manifest.json` parses.
- Every enabled source has `id`, `url`, `target`, `priority`, `tier`, `import_policy`.
- No duplicate source IDs.
- Every target starts with `external/sources/`.
- Disabled archived sources are not selected by default.
- `source-lock.json` shape is valid after a mocked run or real run.
- generated files include the auto-generated header.

---

## 17. README 快速開始

The coding agent **MUST** create `README.md` with this quick start:

```md
# project_starter

> 繁體中文（香港）版本。為保留技術準確性，檔名、指令、JSON key 與大部分程式碼區塊維持原文。

Executable starter for downloading, auditing, curating, and syncing AI coding-agent harness sources.

## 快速開始

```bash
npm run bootstrap
```

This downloads approved upstream repositories into:

```text
external/sources/
```

Then it writes:

```text
sources/source-lock.json
docs/source-audit.md
```

## 重要

Downloaded repositories are untrusted until audited.

The project does not execute downloaded code and does not import third-party skills automatically.
```

### 17.1 Also create `docs/agents.md`

This file should summarize supported agents, shared rules, validation commands, and the policy that downloaded sources are reference material until audited.

### 17.2 Also create `docs/changelog.md`

The first version may contain a minimal initial entry documenting starter bootstrap creation.

---

## 18. `task.md`

編碼代理**必須**建立：

```md
# Task

Implement `project_starter.md` as an executable repository.

## Required first milestone

- [ ] Create package.json
- [ ] Create source manifests
- [ ] Create create-project flow
- [ ] Create downloader
- [ ] Download enabled GitHub sources
- [ ] Generate source lock
- [ ] Generate source audit
- [ ] Run doctor
- [ ] Run tests
```

---

## 19. `status.md`

編碼代理**必須**建立：

```md
# Status

## 目前階段

Bootstrap implementation.

## 最新更新

Not started.

## 阻礙因素

None yet.

## 要執行的指令

```bash
npm run bootstrap
```
```

---

## 20. 所需驗收標準

The implementation is accepted only when all of these pass:

```bash
npm run doctor
npm run sources:download
npm run sources:audit
npm run security
npm run sync -- --dry-run
npm run test
```

After `npm run sources:download`, these directories must exist unless an optional source failed and was recorded:

```text
external/sources/ecc
external/sources/anthropic-claude-code
external/sources/anthropic-claude-code-action
external/sources/anthropic-skills
external/sources/anthropic-claude-plugins-official
external/sources/openai-codex
external/sources/google-gemini-cli
external/sources/opencode
external/sources/modelcontextprotocol-servers
external/sources/modelcontextprotocol-registry
external/sources/github-mcp-server
external/sources/agents-md
external/sources/andrej-karpathy-skills
external/sources/andrej-karpathy-skills-cursor-vscode
external/sources/claude-mem
external/sources/superpowers
external/sources/claude-code-best-practice
external/sources/awesome-claude-code
external/sources/awesome-agent-skills
external/sources/wshobson-agents
external/sources/vercel-agent-skills
external/sources/awesome-cursorrules
external/sources/cursor-security-rules
```

The file below must exist:

```text
sources/source-lock.json
```

The file below must exist:

```text
docs/source-audit.md
```

The downloaded repositories must **not** be committed to git.

---

## 21. 編碼代理的精確實作順序

The coding agent **MUST** follow this order:

1. Read this file fully.
2. Create folder structure.
3. Create `package.json`.
4. Create `.gitignore`.
5. Create `external/.gitignore`.
6. Create `sources/manifest.json`.
7. Create `sources/docs-manifest.json`.
8. Implement `scripts/lib/fs-safe.mjs`.
9. Implement `scripts/lib/git.mjs`.
10. Implement `scripts/lib/manifest.mjs`.
11. Implement `scripts/source-download.mjs`.
12. Implement `scripts/source-audit.mjs`.
13. Implement `scripts/doctor.mjs`.
14. Implement `scripts/security.mjs`.
15. Implement `scripts/sync.mjs`.
16. Implement `scripts/project-starter.mjs`.
17. Implement `scripts/create-project.mjs`.
18. Create rule files.
19. Create README, task, status, docs.
20. Create tests.
21. Run:

```bash
npm run doctor
npm run sources:download
npm run sources:audit
npm run security
npm run sync -- --dry-run
npm run test
```

22. If all pass, update `status.md`.
23. Report final summary.

---

## 22. 不要做以下事情

The coding agent **MUST NOT**:

- merely rewrite this Markdown file,
- pretend downloads happened,
- skip source download silently,
- execute downloaded repository scripts,
- install global npm packages,
- run remote installer scripts,
- copy all downloaded skills into active config,
- overwrite user files without backup,
- overwrite a non-empty target project directory without permission,
- mutate global Claude/Cursor/Codex/Gemini/OpenCode config,
- put secrets in memory,
- log hidden chain-of-thought,
- auto-approve self-improvement suggestions.

---

## 23. 如果儲存庫已搬遷或發生重新導向

If a GitHub repo redirects, the downloader must:

1. allow git to clone it,
2. record the resolved remote URL from:

```bash
git -C <target> remote get-url origin
```

3. record a warning in `sources/source-lock.json`,
4. continue if the clone succeeded.

---

## 24. 如果儲存庫已不存在

For required repos:

```text
Fail bootstrap.
Write failure to sources/source-lock.json.
Tell the user exactly which source failed.
```

For optional repos:

```text
Continue.
Write failure to sources/source-lock.json.
Mention failure in docs/source-audit.md.
```

---

## 25. 完成定義

The project is done when:

- [ ] The repo is named `project_starter`.
- [ ] `npm run bootstrap` exists.
- [ ] `sources/manifest.json` contains exact GitHub repos.
- [ ] `npm run sources:download` downloads enabled repos.
- [ ] `external/sources/` contains downloaded upstream repos.
- [ ] `sources/source-lock.json` records commits.
- [ ] `docs/source-audit.md` is generated.
- [ ] downloaded repos are ignored by git.
- [ ] no downloaded code is executed.
- [ ] sync dry-run works.
- [ ] tests pass.
- [ ] `status.md` is updated with actual results.

### 25.1 非目標

This starter does not require:

1. A web app.
2. A backend server.
3. A database.
4. A frontend framework.
5. TypeScript.
6. Docker.
7. Kubernetes.
8. Cloud deployment.
9. Runtime third-party dependencies for the bootstrap implementation.
10. Automatic modification of global AI tool configuration.

### 25.2 延伸點

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

They may also add TypeScript, ESLint, Prettier, Vitest, Jest, Playwright, Docker, CI workflows, release workflows, or deployment configs as long as docs and validation are updated.

---

## 26. 面向使用者的最終成功訊息

When complete, the coding agent should report:

```text
project_starter bootstrap complete.

Downloaded sources:
- <count> succeeded
- <count> failed
- <count> skipped

Generated:
- sources/source-lock.json
- docs/source-audit.md

Validation:
- doct或： pass/fail
- security: pass/fail
- sync dry-run: pass/fail
- tests: pass/fail

Downloaded repositories are in external/sources/.
They are not imported or executed until audited.
```
