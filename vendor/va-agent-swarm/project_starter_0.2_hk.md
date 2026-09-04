# Project Starter — 改良版活任務規格（Living Task Spec）
  
**專案名稱：** `project_starter`    
**Package/repo 名稱：** `project_starter`    
**版本：** `0.2.0-rethink`    
**狀態：** 已準備好執行 Phase 0    
**建立日期：** 2026-06-07    
**主要目標：** 建立一個可投入生產的 starter repo，用於安裝、同步、稽核並演進跨代理編碼執行框架，涵蓋 Claude Code、Cursor、Codex、OpenCode、Gemini CLI、Grok Build 與類似工具。  
  
---  
  
## 0. 重要重思摘要（Key Rethink Summary）  
  
原始計劃方向很強，但範圍偏廣、部分重複，而且略帶風險：它假設可以「完整安裝」以及在設定系統各異的工具之間達成「完全一致」。此改良版規格透過以下方式讓專案更可執行：  
  
1. 以 **ECC 作為基礎**，但先安裝「精選 profile」，而不是盲目拷貝所有內容。  
2. 把 Bash-first 同步改為**跨平台 Node.js CLI**。  
3. 定義**單一事實來源**與由其生成的 adapters，並加入 drift checks。  
4. 將「所有地方都一樣的 skills/rules」定義為**語義一致（semantic parity）**，而非檔案格式的完全一致。  
5. 新增 license、source、checksum 與 version manifests。  
6. 分離 **instructions**、**skills**、**memory**、**hooks**、**MCP** 與 **生成的工具設定**。  
7. 加入明確的**安全威脅模型（threat model）**。  
8. 以**可稽核摘要、證據、決策、diff、命令、測試結果與審查輸出**取代「記錄所有推理軌跡」。不要請求或儲存隱藏的 chain-of-thought。  
9. 讓自我改進維持在**只提案**，直到人類批准。  
10. 加入可量測的質量閘門、同步測試與安裝時間預算。  
  
---  
  
## 1. 來源驗證快照（Source Verification Snapshot）  
  
Phase 0 必須在實作前重新檢查所有來源。當前預期來源優先級：  
  
1. **ECC** — 主要跨代理執行框架基礎。  
2. **Karpathy 風格行為規則** — 精簡的行為層。  
3. **claude-mem 或同等方案** — 若相容且安全，則用於持久記憶。  
4. **Claude Code 最佳實踐 repo** — 選取的規劃／工作流程模式。  
5. **精選技能庫** — 僅選擇性匯入；預設不做大量安裝。  
6. **官方代理文件** — Claude Code、Cursor、Codex、OpenCode、Gemini CLI、Grok Build、GitHub Copilot。  
  
Phase 0 必須驗證：  
  
- 最新版本、commit、tag 或 release。  
- License。  
- 安裝方式。  
- 支援的設定路徑。  
- 安全影響。  
- 內容哪些會被採用、轉換或拒絕。  
  
---  
  
## 2. 不可妥協原則（Non-Negotiable Principles）  
  
1. **SDD 優先：** 規格驅動實作。  
2. **重疊時 ECC 優先：** 除非來源稽核證明更適合，否則在重疊項上優先採用 ECC 的元件、命名、慣例、安全與跨執行框架架構。  
3. **Karpathy 行為層：** 先思考再編碼、簡潔優先、外科手術式變更、以目標驅動執行。  
4. **單一事實來源：** 中央 `skills/`、`rules/`、`hooks/`、`mcp-configs/` 與 manifests 為權威來源。  
5. **生成的 adapters：** `.claude/`、`.cursor/`、`.gemini/`、`.codex/`、`AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 等需由事實來源生成或以文件化方式同步。  
6. **預設安全：** 不做破壞性自動化、遠端 MCP 或技能變更，除非獲人類明確批准。  
7. **Local-first：** 優先本地腳本、本地記憶、本地稽核日誌，外部服務為可選。  
8. **精簡核心、可選 bundle：** Starter 必須輕量；大型技能庫需精選而非全裝。  
9. **跨平台：** macOS、Linux、Windows/PowerShell/WSL 盡可能支援。  
10. **可稽核而非不透明：** 儲存精簡的 rationale、證據、決策、diff、執行過的命令、測試結果與審查摘要。**不要**要求隱藏 chain-of-thought。  
  
---  
  
## 3. 目標交付物（Target Deliverables）  
  
- [ ] 新 repo：`project_starter`。  
- [ ] 一個主 CLI：`node scripts/project-starter.mjs`。  
- [ ] NPM scripts：  
  - `npm run init`  
  - `npm run sync`  
  - `npm run sync:check`  
  - `npm run doctor`  
  - `npm run security`  
  - `npm run review`  
  - `npm run test`  
  - `npm run format`  
- [ ] 基於 ECC 的 starter profile。  
- [ ] 跨代理同步引擎。  
- [ ] 精選 skills/rules/hooks/MCP manifests。  
- [ ] Claude Code、Cursor、Codex、OpenCode、Gemini CLI、Grok Build adapters。  
- [ ] 可選 GitHub Copilot、Zed、Windsurf adapters。  
- [ ] Self-review/critic 例行程序。  
- [ ] 技能生命週期的提案／批准流程。  
- [ ] 以 AgentShield 或同等方案構建的安全基線。  
- [ ] 文件、示例、測試與驗收檢查。  
  
---  
  
## 4. 建議 Repo 結構（Proposed Repository Structure）  
  
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
  
## 5. 生成檔案政策（Generated File Policy）  
  
每個生成／轉換檔案都必須包含以下 header：  
  
```text  
<!-- 由 project_starter 自動生成。請勿直接編輯。  
Source: skills/, rules/, hooks/, mcp-configs/  
Run: npm run sync  
-->  
```  
  
規則：  
  
- [ ] 中央檔案為權威來源。  
- [ ] 生成檔案僅在衝突檢查後才覆寫。  
- [ ] 覆寫前需先備份本地使用者檔案。  
- [ ] `--dry-run` 必須顯示精確的寫入／刪除內容。  
- [ ] `--check` 若生成檔案過期必須失敗。  
- [ ] 僅在安全且支援時才使用 symlink。  
- [ ] Windows 預設使用 copy mode，除非偵測到 Developer Mode/admin 的 symlink 支援。  
  
---  
  
## 6. Phase 0 — 研究、鎖定範圍與來源稽核（Source Audit）  
  
**目標：** 在生成檔案前確認最新來源、安裝指令、licenses 與相容性。  
  
### 任務  
  
- [ ] 驗證最新 ECC release、installer commands、profiles 與 license。  
- [ ] 驗證 Karpathy 風格規則來源與 Cursor 規則變體。  
- [ ] 驗證 `claude-mem` 或同等持久記憶方案。  
- [ ] 驗證 best-practice workflow repos，並只選取不重複模式。  
- [ ] 驗證精選技能庫並只選高價值 bundles。  
- [ ] 驗證 Claude Code、Cursor、Codex、OpenCode、Gemini CLI、Grok Build、GitHub Copilot 的官方文件。  
- [ ] 建立 `docs/source-audit.md`，包含：  
  - source name  
  - URL  
  - version/commit/tag  
  - license  
  - install command  
  - selected components  
  - rejected components  
  - rationale  
- [ ] 建立 `docs/decisions.md`（ADR 風格）。  
- [ ] 定義 starter profiles：  
  - **Core profile：** 最小、安全、5 分鐘內 init。  
  - **Power profile：** 更完整的 ECC 安裝 + memory + 精選 skills。  
  - **Experimental profile：** Grok Build、更多 MCP、多代理 demos。  
  
### 驗收標準  
  
- [ ] 未記錄 license 與 version/commit 的 source 不得使用。  
- [ ] 不接受互相衝突的重複 skills/rules。  
- [ ] 存在清晰優先順序：ECC > Karpathy > memory > best-practice > curated libraries。  
- [ ] 安裝指令在 scripting 前已被驗證。  
  
---  
  
## 7. Phase 1 — Repo 骨架與 CLI 基礎  
  
**目標：** 建立乾淨 starter repo 與可攜腳本。  
  
### 任務  
  
- [ ] 初始化 Git repo：`project_starter`。  
- [ ] 新增 `package.json` scripts：  
  - `init`  
  - `sync`  
  - `sync:check`  
  - `doctor`  
  - `security`  
  - `review`  
  - `test`  
  - `format`  
- [ ] 實作 `scripts/project-starter.mjs` 命令路由。  
- [ ] 實作 `scripts/doctor.mjs` 檢查：  
  - Node 版本  
  - Git 可用性  
  - OS  
  - symlink 能力  
  - Claude/Cursor/Codex/Gemini/OpenCode/Grok 是否可用（如已安裝）  
  - 必要目錄  
- [ ] 新增 `.editorconfig`、`.gitignore`、`README.md` 與基礎 docs。  
- [ ] 新增空的 manifests 與 JSON schemas。  
- [ ] 新增第一版 `task.md` 與 `status.md`。  
  
### 驗收標準  
  
- [ ] `npm run doctor` 可在乾淨機器上運行。  
- [ ] `npm run test` 可在 placeholder tests 下通過。  
- [ ] Repo 骨架可在 1 分鐘內建立。  
- [ ] 所有 docs 與 generated headers 一致使用 `project_starter`。  
  
---  
  
## 8. Phase 2 — ECC 基礎  
  
**目標：** 安裝／轉換 ECC 作為主要 harness 層。  
  
### 任務  
  
- [ ] 新增 `scripts/adapters/ecc.mjs` 或 installer wrapper。  
- [ ] 支援 profiles：  
  - `--profile core`  
  - `--profile minimal`  
  - `--profile power`  
  - `--profile experimental`  
- [ ] 安裝／選取 ECC components：  
  - core rules  
  - planning/review/security skills  
  - AgentShield/security scan  
  - token/context optimization  
  - memory/instinct learning（在安全前提下）  
  - dmux 或平行編排 patterns  
  - MCP conventions  
- [ ] 預設避免盲目 full copy。  
- [ ] 在 `docs/source-audit.md` 記錄 ECC source version。  
- [ ] 為匯入／衍生檔案加入 attribution。  
- [ ] ECC setup 後執行 AgentShield/security scan。  
  
### 驗收標準  
  
- [ ] ECC core profile 可重現安裝或可重現引用。  
- [ ] 可執行 security scan。  
- [ ] 預設不載入超大量 skills。  
- [ ] ECC 為預設衝突勝者。  
  
---  
  
## 9. Phase 3 — 行為規則與 SDD 憲章（Constitution）  
  
**目標：** 建立每個代理都會收到的精簡高影響規則。  
  
### 中央規則檔案  
  
- [ ] `rules/00-constitution.md`  
- [ ] `rules/10-karpathy.md`  
- [ ] `rules/20-sdd.md`  
- [ ] `rules/30-security.md`  
- [ ] `rules/40-testing.md`  
- [ ] `rules/50-token-efficiency.md`  
- [ ] `rules/60-human-approval.md`  
  
### 必要行為層  
  
- [ ] 先思考再編碼。  
- [ ] 優先簡單方案。  
- [ ] 外科手術式變更。  
- [ ] 依照明確目標執行。  
- [ ] 只有在被有意義的歧義阻塞時才提問。  
- [ ] 多檔案修改前先規劃。  
- [ ] 執行測試，或解釋為何未執行。  
- [ ] 重大工作後更新 `status.md`。  
- [ ] 未經人類批准，不得自動套用 skills/rules/hooks 變更。  
  
### 驗收標準  
  
- [ ] `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`.cursor/rules/*.mdc` 與各工具 adapters 行為語義一致。  
- [ ] 規則保持精簡且不重複。  
- [ ] 所有規則衝突都有文件記錄。  
  
---  
  
## 10. Phase 4 — 精選技能（Curated Skills）  
  
**目標：** 建立精簡的 skill set，覆蓋高價值工作流且避免膨脹。  
  
### 核心技能分類  
  
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
  
### Manifest 要求  
  
`skills/manifest.json` 的每個 skill entry 必須包含：  
  
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
  
### 驗收標準  
  
- [ ] Core profile 大約 15–30 個 skills，而不是數百個。  
- [ ] 可選 bundles 可被選取。  
- [ ] 每個 skill 都有 attribution 與版本化。  
- [ ] skills 透過 sync adapters 進行測試。  
  
---  
  
## 11. Phase 5 — 跨代理同步層（Cross-Agent Synchronization Layer）  
  
**目標：** 讓每個支援的代理在各自工具能力範圍內收到同一套精選 skills、rules、hooks 與 MCP 設定。  
  
### CLI  
  
實作：  
  
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
  
- [ ] Claude Code：  
  - `.claude/skills/<skill>/SKILL.md`  
  - `.claude/rules/*.md`  
  - `.claude/settings.json`  
  - `.claude/commands/`（可用時加入相容 shim）  
  - root `CLAUDE.md`  
- [ ] Cursor：  
  - `.cursor/rules/*.mdc`  
  - `.cursor/mcp.json`  
  - 可選 `.cursor/skills/`（若選定的 ECC pattern 支援）  
- [ ] Codex：  
  - `AGENTS.md`  
  - `.codex/`（若支援）  
  - 若無原生 skills，生成 skills index  
- [ ] OpenCode：  
  - `AGENTS.md`  
  - `opencode.json`  
  - 可選 agent definitions  
- [ ] Gemini CLI：  
  - `GEMINI.md`  
  - `.gemini/settings.json`  
  - 可選 context filename config  
- [ ] Grok Build：  
  - `AGENTS.md`  
  - 在支援範圍內引用相容的 skills/hooks/MCP  
- [ ] GitHub Copilot：  
  - `.github/copilot-instructions.md`  
  
### 同步安全性（Sync Safety）  
  
- [ ] 備份被修改的生成檔案。  
- [ ] 偵測生成檔案上的手動編輯。  
- [ ] 產出 sync report。  
- [ ] manifest/schema 錯誤時失敗。  
- [ ] 支援 CI drift check。  
  
### 驗收標準  
  
- [ ] 修改中央 skill → 執行 sync → 所有支援代理更新。  
- [ ] `npm run sync -- --check` 能偵測生成檔案過期。  
- [ ] 至少完成 Claude Code + Cursor + Codex/Gemini 的測試。  
- [ ] 不需要手動複製。  
  
---  
  
## 12. Phase 6 — 記憶與交接（Memory and Handoff）  
  
**目標：** 在不造成上下文膨脹的前提下提供持久、注重私隱的記憶。  
  
### 記憶分層  
  
- [ ] `status.md`：當前進度。  
- [ ] `task.md`：活規格。  
- [ ] `memory/project.md`：穩定專案上下文。  
- [ ] `memory/handoff.md`：精簡續航摘要。  
- [ ] `memory/reflections/`：審查教訓與可重用模式。  
- [ ] 可選 `claude-mem` 或 ECC memory/instinct layer。  
  
### 規則  
  
- [ ] 不得儲存 secrets。  
- [ ] 遮罩 credentials 與個人資料。  
- [ ] 用摘要取代原始 log 傾倒。  
- [ ] 只載入相關記憶。  
- [ ] 優先使用 handoff 檔案做 session 延續。  
- [ ] 將自動注入的上下文保持精簡。  
  
### 驗收標準  
  
- [ ] 新 session 可從 `task.md`、`status.md`、`memory/handoff.md` 恢復。  
- [ ] self-review 輸出可產生 reflection entries。  
- [ ] 記憶可被停用。  
  
---  
  
## 13. Phase 7 — 自我評估與 Critic 例行程序（Self-Evaluation and Critic Routine）  
  
**目標：** 建立結構化的 plan → implement → review → refine 循環。  
  
### 角色  
  
- **Actor/Solver：** 實作任務。  
- **Critic：** 審查正確性、簡潔性、規格遵循、安全、效能、可維護性。  
- **Security Critic：** 可選的安全專注審查。  
- **Test Critic：** 可選的測試與驗證審查。  
- **Judge：** 彙總 blocking 與 non-blocking 發現。  
  
### Rubric  
  
每個維度 1–5 分：  
  
1. Correctness  
2. Spec adherence  
3. Simplicity / Karpathy alignment  
4. Security  
5. Test coverage  
6. Maintainability  
7. Performance/token efficiency  
8. Auditability  
9. Self-improvement value  
  
### 輸出  
  
- [ ] `reviews/<timestamp>-<task>.review.md`  
- [ ] `reviews/<timestamp>-<task>.review.json`  
- [ ] Blocking findings  
- [ ] Non-blocking suggestions  
- [ ] Tests run  
- [ ] Files changed  
- [ ] Recommended next tasks  
  
### 命令  
  
- [ ] Claude skill/command：`/self-review`  
- [ ] Claude skill/command：`/critic`  
- [ ] CLI：`npm run review`  
- [ ] 可選 hook：post-task self-review  
  
### 護欄（Guardrails）  
  
- [ ] 不記錄隱藏 chain-of-thought。  
- [ ] 只儲存精簡 rationale 與 evidence。  
- [ ] 預設最多 2 次 refine loops。  
- [ ] 高影響變更需人類確認。  
  
### 驗收標準  
  
- [ ] 代理可對自身工作做批判。  
- [ ] 批判包含可操作修正。  
- [ ] 若存在嚴重問題，審查可阻止完成。  
- [ ] 審查輸出可安全回饋到 memory/reflection。  
  
---  
  
## 14. Phase 8 — 技能生命週期建議（需人類批准）  
  
**目標：** 只透過「建議」安全地自我演進 skills/rules/hooks。  
  
### 工作流程  
  
1. 分析 skill 使用、reviews、失敗、缺口與重複。  
2. 生成 suggestion 檔案。  
3. 人類審查。  
4. 人類批准／拒絕／修改。  
5. 已批准變更套用到中央事實來源。  
6. sync 將變更傳播。  
7. audit log 記錄決策。  
  
### Suggestion Template  
  
每個 suggestion 必須包含：  
  
- ID  
- Action：add/update/remove  
- Target skill/rule/hook  
- Rationale  
- Evidence  
- Proposed diff/content  
- Risk assessment  
- Rollback plan  
- Confidence  
- Human approval field  
  
### 命令  
  
- [ ] `/suggest-skills`  
- [ ] `/review-suggestions`  
- [ ] `/approve-suggestion`  
- [ ] CLI：`npm run suggest-skills`  
- [ ] CLI：`npm run apply-suggestion -- --id <id>`  
  
### 驗收標準  
  
- [ ] 未經明確批准不得變更 skills/rules/hooks。  
- [ ] 已批准變更皆有日誌。  
- [ ] 被拒絕的建議保留以供稽核。  
- [ ] 存在回滾路徑。  
  
---  
  
## 15. Phase 9 — 安全基線（Security Baseline）  
  
**目標：** 讓執行框架在真實本地使用場景中是安全的。  
  
### Threat Model  
  
防護對象：  
  
- [ ] 透過 docs、issues、網頁、MCP 輸出造成的 prompt injection。  
- [ ] Secret 外洩。  
- [ ] 破壞性 shell commands。  
- [ ] 權限過大的 hooks。  
- [ ] 不安全的 MCP servers。  
- [ ] 來自技能庫的供應鏈風險。  
- [ ] 生成檔案漂移。  
- [ ] 隱藏的遠端 telemetry。  
- [ ] 意外覆寫全局設定。  
  
### Controls  
  
- [ ] AgentShield 或同等方案掃描。  
- [ ] Secret scanner。  
- [ ] MCP allowlist。  
- [ ] Hook command allowlist。  
- [ ] `.env`、key、cert、token 檔保護。  
- [ ] 破壞性命令需人類批准。  
- [ ] CI security check。  
- [ ] Dependency audit。  
- [ ] 預設不包含任何遠端 MCP credentials。  
- [ ] 腳本中不得出現 `curl | bash`，除非明確批准並文件化。  
  
### 驗收標準  
  
- [ ] `npm run security` 可在本地執行。  
- [ ] critical findings 會使 CI 失敗。  
- [ ] 敏感檔案受保護。  
- [ ] 安全文件說明威脅模型。  
  
---  
  
## 16. Phase 10 — 文件與示例（Docs and Examples）  
  
**目標：** 令 starter 可在 10 分鐘內上手。  
  
### 文件  
  
- [ ] `README.md`：總覽與 quick start。  
- [ ] `docs/installation.md`：精確安裝指令。  
- [ ] `docs/usage.md`：日常工作流。  
- [ ] `docs/architecture.md`：事實來源與 adapters。  
- [ ] `docs/sync.md`：同步行為與疑難排解。  
- [ ] `docs/security.md`：安全模型。  
- [ ] `docs/decisions.md`：ADRs。  
- [ ] `docs/source-audit.md`：來源版本與 licenses。  
  
### 示例  
  
- [ ] SDD feature workflow。  
- [ ] Cross-agent sync workflow。  
- [ ] Self-review workflow。  
- [ ] Skill suggestion workflow。  
- [ ] Security scan workflow。  
  
### 驗收標準  
  
- [ ] 新用戶可在 10 分鐘內 init + sync。  
- [ ] 文件說明 Claude/Cursor/Codex/Gemini/OpenCode 的差異。  
- [ ] 示例可執行。  
  
---  
  
## 17. Phase 11 — 驗證與 CI（Validation and CI）  
  
**目標：** 防止回歸並證明 starter 可運作。  
  
### Tests  
  
- [ ] Manifest schema validation。  
- [ ] Adapter snapshot tests。  
- [ ] Sync dry-run tests。  
- [ ] Generated file drift tests。  
- [ ] Security scan smoke test。  
- [ ] Windows path handling tests。  
- [ ] 無重複 skill IDs。  
- [ ] 所有生成檔案都包含 headers。  
  
### CI  
  
- [ ] Lint JS。  
- [ ] Validate JSON。  
- [ ] 盡可能驗證 Markdown links。  
- [ ] Run tests。  
- [ ] Run `sync --check`。  
- [ ] Run security scan。  
- [ ] 上傳 review/security artifacts。  
  
### 驗收標準  
  
- [ ] CI 綠燈。  
- [ ] fresh clone 後可通過 `npm install && npm test`。  
- [ ] 生成後 `npm run sync -- --check` 通過。  
  
---  
  
## 18. 完成定義（Definition of Done）  
  
專案完成條件：  
  
- [ ] `npm run init` 產生可用 starter。  
- [ ] `npm run sync` 更新所有支援代理設定。  
- [ ] 已驗證 Claude Code、Cursor，且至少驗證 Codex/Gemini/OpenCode 其中之一。  
- [ ] ECC foundation 已安裝／轉換並文件化。  
- [ ] Karpathy 行為規則啟用。  
- [ ] Self-review workflow 可運作。  
- [ ] Skill suggestions 必須由人類批准。  
- [ ] 安全掃描可運作並會阻擋 critical issues。  
- [ ] 文件足以讓新用戶使用。  
- [ ] 所有生成檔案可重現。  
- [ ] Source audit 與 decisions 完整。  
- [ ] 所有專案名稱、文件、生成 header、scripts 與 examples 一致使用 `project_starter`。  
  
---  
  
## 19. 立即下一步（Immediate Next Actions）  
  
1. 建立名為 `project_starter` 的 repo 骨架。  
2. 執行 Phase 0 source audit。  
3. 實作 `scripts/project-starter.mjs`、`doctor.mjs` 與空的 sync framework。  
4. 新增中央 rules 與 manifests。  
5. 先實作 Claude + Cursor adapters。  
6. 再加入 Codex/Gemini/OpenCode adapters。  
7. 安裝／轉換 ECC core profile。  
8. 執行 security scan。  
9. 撰寫 docs 與 examples。  
10. 以以下 commit 訊息提交：  
  
```text  
chore: initialize project_starter  
```  
  
---  
  
## 20. 實作優先順序（Implementation Priority）  
  
1. **Foundation：** repo、CLI、manifests、docs skeleton。  
2. **Sync：** central source → Claude/Cursor/Codex。  
3. **ECC：** install/adapt core。  
4. **Rules：** constitution + Karpathy + SDD。  
5. **Skills：** curated core。  
6. **Security：** AgentShield + secret protections。  
7. **Memory：** handoff + reflection。  
8. **Critic：** self-review workflow。  
9. **Lifecycle：** suggestions + human approval。  
10. **Polish：** examples、CI、docs。  
