  
```
# project_starter.md：建立「終極編碼代理執行框架」起手式專案


```
```
**目標**  
建立一個乾淨、可投入生產的**初始專案**（repo + 安裝腳本 + 設定檔 + 配置），命名為 `ultimate-agent-harness-starter`（或你偏好的名稱），用於啟動一個強大、跨工具的編碼代理環境。  

它會把截至 2026 年 6 月在 GitHub 排名最前的編碼代理專案設定／執行框架的**最佳要素**整合在一起，並在任何重疊之處以 **ECC 作為首要基礎**。最終結果應是一個可用一個命令（或少數命令）安裝的 starter，能立即為 Claude Code、Cursor、Codex、OpenCode、Gemini CLI 與類似工具帶來高生產力的代理式工作流程。

**背景與原則**  
- **規格驅動開發（SDD）** 優先：一切由清晰規格驅動。  
- 在功能／技能／規則重疊時優先採用**排名最高**者（ECC #1 > Karpathy rules #2 > claude-mem #3 > shanraisshan best-practice #4 > antigravity-awesome-skills #5 等）。  
- 盡可能保持**可攜、少 Docker、local-first**，並具備優秀的安全性、記憶管理與 token 效率。  
- 輸出必須**對代理友善**：清晰的階段、檢查清單、驗收標準，以及 critic/review 代理的掛鈎點。  
- 支援迭代精修（plan → implement → review → improve 循環）。  
- 目標使用者：獨立開發者、小團隊或想打造自訂 AI 編碼工作流的進階用戶（對齊 harness engineering + N1ch01as 風格的 meta-systems）。

**成功準則**  
- 新專案資料夾可在 < 5 分鐘內用一個主腳本初始化。  
- ECC 完整安裝並作為核心執行框架配置完成。  
- Karpathy 行為規則預設啟用。  
- 啟用持久記憶（claude-mem 或同等方案）。  
- 從高價值技能庫選擇性合併（不重複、不堆砌）。  
- 內含最佳實踐設定、hooks、規則與示例工作流程。  
- 啟用安全基線（AgentShield 或同等方案）。  
- 文檔清晰，且提供可延伸的 task.md。  
- 盡可能跨平台（macOS/Linux/Windows）並支援多代理。  
- 內含質量閘門（lint、tests、review prompts）。
- **所有支援的編碼代理**透過自動化或文件化的同步機制，從單一事實來源共享完全一致的精選技能、規則與 hooks。

---

## 跨代理技能與規則同步層（新增核心功能）

**目標**：確保**每一個編碼代理**（Claude Code、Cursor、Codex、OpenCode、Gemini CLI 等）都「知道」**同一套高品質技能與規則**，方法是讓各自的設定資料夾／檔案從一個中央的事實來源同步。

這解決了不同代理各自為政、技能破碎或過時的常見問題。我們先優先採用 **ECC 的跨執行框架方法**，再補充輕量 adapter/sync 腳本以達到完整覆蓋。

**設計原則**（ECC-first）：
- 單一事實來源：在 repo root 使用 `./skills/`、`./rules/`、`./hooks/`、`./mcp-configs/`。
- 若目標代理支援，優先使用 symlink（快速、永遠同步）。
- 若代理的資料夾結構或檔案格式不同，則使用「智能複製 + 輕量轉換」作為 fallback。
- 盡可能利用 ECC 既有的跨工具相容性與 adapters。
- 同步流程要簡單、可腳本化且安全（idempotent、提供 backup/restore）。

**更新後資料夾結構**（新增以下內容）：

```
ultimate-agent-harness-starter/ ├── skills/ # ← 單一事實來源（Markdown skills） ├── rules/ # ← 單一事實來源（行為 + coding standards） ├── hooks/ # ← 共用自動化 hooks ├── mcp-configs/ # ← 共用 MCP 定義 ├── .claude/ # Claude Code（skills、commands、hooks、rules）← 同步 ├── .cursor/ # Cursor rules & settings ← 同步/轉換 ├── agents/ # 自訂 sub-agents ├── scripts/ │ ├── sync-skills.sh # ← 主同步腳本（或 Node.js 等效） │ ├── sync-to-claude.sh │ ├── sync-to-cursor.sh │ └── … ├── docs/ └── …  
```
**實作同步層任務**：
1. [ ] 建立中央 `skills/`、`rules/`、`hooks/`、`mcp-configs/` 作為**權威來源**。
2. [ ] 建立或調整同步腳本（`scripts/sync-skills.sh`）：
   - 對 **Claude Code**（`.claude/`）：複製或 symlink skills/commands/hooks/rules，並盡可能使用 ECC 的 plugin/marketplace 模式。
   - 對 **Cursor**：從中央 `rules/` 產生或更新 `.cursor/rules/` 或相關設定檔。
   - 對 **其他代理**（Codex、OpenCode、Gemini CLI 等）：依需要產生 root files（例如彙總的 `AGENTS.md`、`CLAUDE.md`）或工具專屬資料夾，方式是組合中央內容 + ECC adapters。
   - 支援**完整同步**與**選擇性同步**（例如只同步 planning + review skills）。
   - 保持 idempotent 且安全（dry-run、衝突偵測）。
3. [ ] 優先整合 ECC 的既有 cross-harness 功能與 MCP configs（最高優先）。
4. [ ] 加入 `sync` 命令或 npm script，使使用者／代理可在技能更新後執行 `npm run sync` 或 `./scripts/sync-skills.sh`。
5. [ ] 在 `docs/installation.md` 與 `docs/usage.md` 清楚記錄同步流程。
6. [ ] 加入 `.claude/commands/sync-skills.md`（或類似）讓代理可自行觸發同步。
7. [ ] 加入版本釘選或 manifest（`skills/manifest.json`），確保各處使用相同技能版本。
8. [ ] 至少在 Claude Code + Cursor + 另一個代理上測試同步。

**驗收標準**：
- 更新中央 `./skills/` 的某個 skill 並執行同步腳本後，所有支援的代理都能立即使用該 skill。
- 不需要在資料夾之間手動複製。
- 代理行為一致，因為它們引用同一套精選內容（優先 ECC + Karpathy + best practices）。
- 同步快速、安全且有文件說明。

此同步層可令整個 starter 在你的編碼代理堆疊中**真正可攜且一致**。

---

## 自我評估與 Critic 例行程序（代理自我質量評估）— 研究強化版

**目標**：加入內建例行程序，讓編碼代理能**評估自身輸出品質**（self-critique / self-review）。這建立一個閉環改進系統：plan → implement → self-evaluate → refine。

本章節基於 xAI 的深度研究（Grok 多代理能力、Grok Build 的 agentic coding 取向、透明/可稽核推理）與 2025–2026 高質量研究（Reflexion、Self-Refine、SAGE multi-agent self-evolution、SCALAR Structured Critic–Actor Loop、human-in-the-loop 自我改進框架、context folding/記憶架構）做了顯著強化。

**研究支持的設計原則**
- **多代理 critic 模式**（xAI Grok Multi-Agent + SAGE）：使用專門角色（Actor/Solver + Critic/Challenger + 可選 Judge）並行工作。每個子代理展示其推理以便完整稽核與透明度。
- **結構化自我批判**（SCALAR、Reflexion、Self-Refine）：避免含糊回饋。加入前置條件驗證、狀態追蹤、rubric 評分與對過往反思/批判的情節記憶。
- **Human-in-the-loop 安全**（研究共識）：所有高影響變更都需要人類確認；當領域知識快速演進時可選擇加入人類指導。
- **記憶與上下文管理**：支援分層摘要、反思儲存與 long-horizon 任務的 context folding（在 claude-mem 基礎上引入 AgentFold / Recursive Language Models 研究概念）。
- **透明與可稽核性**（xAI 核心哲學）：每個子代理的推理步驟、批判與決策都要可被記錄與審查。
- **ECC-first + 研究層**：先以 ECC 既有的 review/critique 能力作為基礎，再疊加更強的多代理 critic 循環與結構化反思。

**強化的自我評估維度**（rubric）
1. **正確性與功能性**（含明確的前置條件與狀態驗證）
2. **簡潔性與 Karpathy 對齊**
3. **Spec / SDD 遵循**
4. **安全性與安全防護**
5. **效能、效率與 Token 使用**
6. **可維護性與清晰度**
7. **推理品質與可稽核性**（新增維度 — 思路透明與可驗證）
8. **自我改進潛力**（批判對精修的可操作性）

**核心例行流程**（Actor → 多代理 Critic → 精修 + 記憶循環）
- **Actor/Solver**：使用 ECC skills + Karpathy rules 產出實作或解法。
- **Critic/Challenger**（可多代理）：按強化 rubric 執行結構化自我批判。可為不同維度啟動平行子代理（例如安全、簡潔性）。輸出分數 + 具體問題 + 可操作改進建議。
- **反思儲存**：把批判、教訓與成功模式寫入情節記憶（以 claude-mem 為基礎，或加入專門的結構化反思儲存與分層摘要）。
- **精修循環**：Actor 使用批判 + 已儲存反思改進輸出；支援多輪迭代並具智能上下文管理。
- **人類確認閘門**：高影響建議（尤其技能／規則變更）走人類確認流程。
- **完整稽核日誌**：記錄推理軌跡、批判與決策以支援透明與後續審查（xAI 風格可稽核）。

**為何重要**
- 防止「vibe coding」漂移。
- 強制遵循規格（SDD）。
- 早期捕捉問題（正確性、安全、複雜度、token 浪費、可維護性）。
- 讓代理隨時間更自主且更可靠。

**設計（ECC-first + 可擴展）**
- 在 `./skills/critic/` 建立中央 critic skill（或重用/擴展 ECC 既有 review/critique 能力）。
- 結構化 self-evaluation prompt/template 輸出：
  - 整體品質分數（例如 1–10 或 rubric-based）
  - 各維度拆解（Correctness、Simplicity/Karpathy alignment、Spec adherence、Security、Performance、Maintainability、Token efficiency）
  - 具體發現問題
  - 具體改進建議（轉成新任務或 diff 建議）
- 觸發方式：
  - 透過 post-completion hook 自動觸發
  - 使用 `/self-review` 或 `/critic` 命令手動觸發
  - 作為多步工作流程的一部分（例如實作完 feature spec）
- 輸出儲存在工作附近（例如 `review.md`，或附加到 `task.md` / `status.md`）
- 回饋進循環（代理可根據自身批判再次精修）

**自我評估維度**（可自訂 rubric）
1. **正確性與功能性** — 是否符合 spec/task 要求？測試是否通過？
2. **簡潔性與 Karpathy 對齊** — 變更是否最小且外科手術式？是否避免不必要抽象？
3. **Spec / SDD 遵循** — 是否忠實原始規格與任務拆解？
4. **安全性與安全防護** — 是否有明顯漏洞、洩密或不安全模式？
5. **效能與效率** — 複雜度與 token 使用是否合理？
6. **可維護性與清晰度** — 代碼是否乾淨、文件化良好、符合專案規則？
7. **整體信心** — 代理對此輸出有多大把握？

**實作任務**
1. [ ] 在 `./skills/critic/self-review.md` 建立或調整核心 **critic / self-review skill**（以 ECC review 能力為基底，加入 Karpathy + best-practice 模式）。
2. [ ] 定義可重用的 **self-evaluation prompt template**（放在 `rules/` 或 `skills/critic/`）供代理呼叫。
3. [ ] 在 `.claude/commands/` 新增 **slash command**（例如 `/self-review` 或 `/critic`），對當前上下文或最近變更做結構化自評。
4. [ ] 建立 **post-completion hook**：在重大代碼變更或任務完成後可選擇自動觸發 self-review。
5. [ ] 讓例行輸出同時產生結構化資料（Markdown + 可選 JSON），可被其他代理或腳本解析。
6. [ ] 與既有編排整合（例如 dmux 平行工作或按規格實作功能後）。
7. [ ] 在 `docs/usage.md` 與 `examples/self-review-workflow/` 加入示例用法。
8. [ ] 支援 rubric 自訂（例如專案權重，或加入 accessibility、i18n 等維度）。
9. [ ] 確保 critic routine 本身也可被評估（meta 層），以持續改進執行框架。

**驗收標準**
- 代理可對其最近工作執行自我評估並產出清晰、可操作的批判。
- Self-review 可手動或透過 hook 自動觸發。
- 輸出包含分數 + 可回餵到工作流程的具體改進任務。
- 在任何重疊時優先採用最高排名來源（ECC review skills + Karpathy + best practices）。
- 變成 starter 工作流程的標準品質閘門。

此例行程序可將編碼代理從一次性產生器轉為**自我改進系統** — 這是高階 harness engineering 的關鍵特徵。

---

## 技能生命週期：自動建議新增／更新／移除（需人類確認）

**目標**：讓系統能**自動提出建議**新增技能、更新既有技能或移除低價值／過時技能，但**任何變更都不得在未獲人類明確確認前自動套用**。這建立一個安全、可控的技能集合自我演化循環。

此功能直接建立在 Self-Evaluation & Critic Routine 與中央 `skills/` 事實來源之上。

**核心工作流程（Human-in-the-Loop）**
1. **分析階段**（由 critic、定期審查或完成重大工作後觸發）：
   - 代理分析當前技能使用情況、self-review 質量分數、與近期任務的相關性、重複性或缺口。
   - 優先使用高排名來源（先 ECC patterns，再 best-practice 洞見）。
2. **生成建議**：
   - 產出清晰、結構化建議：
     - **Add**：新技能提案（名稱、目的、來源或草稿內容、價值理由）。
     - **Update**：對既有技能的具體改進（附 diff 或 before/after 摘要）。
     - **Remove**：移除原因（低使用率、被取代、質量問題）+ 影響評估。
   - 建議保存到 `suggestions/` 或 `pending-skill-changes.md`，並附唯一 ID。
3. **人類審查與確認**：
   - 人類透過檔案、儀表板，或 `/review-suggestions` 命令審查建議。
   - 人類確認、拒絕或修改（例如直接編輯建議檔，或回覆批准）。
   - 只有被確認的項目才會進入下一步。
4. **安全套用**：
   - 確認後，變更套用到中央 `skills/`（必要時也更新 `rules/`）。
   - Cross-Agent Sync Layer 將更新傳播到所有代理資料夾（`.claude/`、`.cursor/` 等）。
5. **稽核與回滾**：
   - 所有變更都記錄時間戳、原因與人類批准者。
   - 可透過 git 或專用 undo 機制快速回滾。

**設計原則**
- **不得自動套用**：任何新增／更新／移除技能都必須由人類確認。
- **ECC-first**：盡可能利用 ECC 的 continuous learning / instinct promotion 模式，再擴展為顯式的 suggestion + confirmation 流程。
- **透明與可稽核**：每個建議都需包含清晰 rationale、預期收益與風險／影響。
- **不阻塞工作**：建議不應打斷工作；可以按需或定期集中審查。
- **可擴展**：未來同樣模式可套用到 rules、hooks，甚至專案層級改進。

**實作任務**
1. [ ] 建立 **suggestion generator skill**（或擴展 critic routine），可基於分析提出 add/update/remove 建議。
2. [ ] 定義標準 **suggestion format**（Markdown 模板：Action、Skill Name、Rationale、Impact、Proposed Content/Diff、Confidence）。
3. [ ] 建立 pending suggestions 的儲存（`suggestions/` + manifest，或 `pending-skill-changes.md`）。
4. [ ] 建立 slash commands：
   - `/suggest-skills` — 觸發分析並生成新建議。
   - `/review-suggestions` — 列出待審建議與細節。
   - `/approve-suggestion` 或 `/confirm-changes` — 人類確認步驟。
5. [ ] 與 Self-Evaluation 例行整合，讓強烈批判能自動觸發相關建議。
6. [ ] 人類確認後，自動套用變更到中央 `skills/`，並觸發同步層。
7. [ ] 為所有已確認變更新增 logging/audit trail。
8. [ ] 在 `docs/usage.md` 文件化完整流程並附示例。
9. [ ] 讓建議系統本身可被自評（meta-critic）。

**驗收標準**
- 代理可生成清晰、可操作的新增／更新／移除技能建議。
- 沒有任何技能會在未經人類明確確認前被新增、更新或移除。
- 確認後的變更會安全套用到中央事實來源並透過同步層傳播。
- 存在完整稽核軌跡。
- 工作流程自然且不侵入（代理提案 → 人類決策 → 系統套用）。

此流程完成一個強大的**安全自我改進循環**，同時保持人類牢牢掌控 — 正是先進編碼代理配置所需的穩健、可投入生產的設計。

---

## Phase 0：研究與最終選型（高層，一次性）

**目標**：確認最新版本，並按排名優先級解決任何重疊。

**任務**：
1. [ ] 驗證目前的頂級 repo（使用 web search 或直接 GitHub）：
   - ECC（affaan-m/ECC）— 主要執行框架（skills、agents、hooks、rules、security、MCP）。
   - Karpathy rules（forrestchang/andrej-karpathy-skills 或 multica-ai mirror）— 行為層 CLAUDE.md。
   - claude-mem（thedotmack/claude-mem）— 持久記憶。
   - shanraisshan/claude-code-best-practice — workflows & patterns。
   - sickn33/antigravity-awesome-skills — 大型技能庫（只選擇性安裝高價值 bundle）。
2. [ ] 識別重疊並做決策：
   - 核心 harness/rules/hooks/security/MCP → **ECC 優先**（排名最高且最完整）。
   - 行為指引 → **Karpathy rules**（作為基礎層或合併到 ECC rules，視相容性）。
   - 記憶 → **claude-mem**（或 ECC 內建 memory/instincts 若足夠；若 dedicated persistence 更佳則優先）。
   - 規劃／best-practice workflows → 合併 shanraisshan + ECC 規劃 skills。
   - 大型技能庫 → 使用 antigravity-awesome-skills installer，但必須**精選**最有用的 20–50 項（planning、TDD、review、security、frontend 等），避免全量安裝。
3. [ ] 檢查是否有 Anthropic 官方 skills 或自上次審查後新增的高排名來源。
4. [ ] 在 `docs/decisions.md` 記錄決策（採 ECC research-first 風格）。

**驗收標準**：
- 存在清晰的決策日誌。
- 最終設定中沒有互相衝突的重複 rules/skills。

---

## Phase 1：專案腳手架與 ECC 基礎（核心 — 最高優先）

**目標**：建立 repo 骨架並將 ECC 作為完整基底執行框架安裝。

**任務**：
1. [ ] 初始化新 Git repo：`ultimate-agent-harness-starter`（或使用者指定名稱）。
2. [ ] 建立標準結構：

```
ultimate-agent-harness-starter/ ├── .claude/ # Claude Code 專用（commands、skills、hooks、rules） ├── .cursor/ # Cursor rules（如需要） ├── agents/ # 自訂 sub-agents 或擴展 ├── skills/ # 精選高價值 skills（合併） ├── rules/ # 合併行為 + coding standards ├── hooks/ # 自動化 hooks ├── mcp-configs/ # MCP server 設定 ├── docs/ │ ├── README.md │ ├── decisions.md │ ├── installation.md │ └── usage.md ├── scripts/ # bootstrap & helper scripts（bash/node） ├── examples/ # 示例專案或工作流程 ├── task.md # 本文件 + 後續任務追蹤 └── .gitignore  
```
3. [ ] **以 ECC 作為基礎安裝**（排名最高）：
- 依 ECC 官方安裝流程（plugin 或手動拷貝元件）。
- 複製／調整核心 agents（63）、skills（251+ 精選）、rules、hooks 與 security（AgentShield）。
- 啟用 ECC 關鍵功能：token optimization、session persistence、instinct learning、MCP。
4. [ ] 加入 ECC 的 dmux-workflows 或平行編排支援（含 task.md / handoff.md 生成）。
5. [ ] 建立初始 `CLAUDE.md` 或 repo root rules file，引用 ECC 並合併 Karpathy 原則（見 Phase 2）。

**驗收標準**：
- `npx` 或 `/plugin` 風格的一鍵命令可啟動 ECC 核心。
- 基本 agent commands（`/plan`、`/review`、security scan 等）可立即使用。
- repo 通過基本 lint/security 檢查。

---

## Phase 2：加入 Karpathy 行為規則 + Best Practices（優先級 #2 與 #4）

**目標**：注入嚴謹的行為護欄與可投入生產的模式。

**任務**：
1. [ ] 整合 **Karpathy rules**（4 個核心原則）作為**基礎行為層**：
- Think Before Coding
- Simplicity First
- Surgical Changes
- Goal-Driven Execution
- 與 ECC 的 rules/CLAUDE.md 無衝突地合併（任何重疊以 ECC 優先）。
2. [ ] 從 `shanraisshan/claude-code-best-practice` 引入高價值模式：
- 規劃工作流程、sub-agent 使用、上下文管理、slash commands、MCP 模式。
- 只選取不重複項（ECC 已涵蓋許多）。
3. [ ] 建立或加強 repo root 的 `CLAUDE.md` / `AGENTS.md`，整合行為與 best-practice 指引。
4. [ ] 在 `docs/` 加入「constitution」或專案規格模板（SDD 風格）。

**驗收標準**：
- 代理預設就能一致遵循 Karpathy + best-practice 模式。
- 不存在規則衝突。
- 文件清楚說明規則如何被載入。

---

## Phase 3：記憶、技能與選擇性技能庫整合（優先級 #3 與 #5）

**目標**：加入持久記憶與精選高影響力 skills。

**任務**：
1. [ ] 安裝 **claude-mem**（或若 ECC 方案更強則選 ECC）以支援跨 session 持久上下文。
- 配置以捕捉工具使用、做摘要，並注入相關 spec/task 上下文。
2. [ ] 選擇性使用 `sickn33/antigravity-awesome-skills`（或同等高排名技能庫）：
- 只安裝 top bundles：planning、TDD、code review、security、frontend/backend patterns、orchestration。
- 避免全量 1500+ 安裝造成膨脹（透過腳本或 manifest 精選）。
3. [ ] 將任何獨特且高價值的 skills 合併到 `./skills/`，並清楚標註來源。
4. [ ] 建立 `skills/manifest.json` 或索引，便於發現與更新。
5. [ ] 若 ECC 尚未提供，加入 SDD 專用 skills（spec analysis、feature spec generation、roadmap tasks、validation gates）。

**驗收標準**：
- 記憶可跨 session 保存並改善長任務上下文。
- 精選 skill set 精簡但強大（文件化選型與理由）。
- 後續可輕鬆新增／移除 skills。

---

## Phase 4：安全、Hooks、MCP、Token 最佳化與收尾

**目標**：利用 ECC 優勢做生產級強化。

**任務**：
1. [ ] 啟用 **AgentShield**（或 ECC security）+ secret detection、vulnerability scanning。
2. [ ] 配置關鍵 **hooks**（pre-commit validation、post-completion review、context compaction、cost tracking）。
3. [ ] 建立常用工具的 **MCP configs**（GitHub、file system 等）— 先從最小且安全的集合開始。
4. [ ] 套用 ECC token optimization 設定（MAX_THINKING_TOKENS、compact thresholds 等）。
5. [ ] 加入 `.gitignore`、license（MIT）與 contributor guidelines。
6. [ ] 在 `scripts/` 建立 bootstrap 腳本：
- `bootstrap.sh` 或 `install.js`，負責 ECC install + memory + curated skills + config copy。
- 支援不同代理的 flags（Claude Code、Cursor 等）。

**驗收標準**：
- 安全基線啟用且有文件。
- hooks 可正確觸發。
- token 使用可見地被最佳化。
- 一個主 bootstrap 命令可可靠運作。

---

## Phase 5：文件、示例、驗證與質量閘門

**目標**：使 starter 易用且可擴展。

**任務**：
1. [ ] 撰寫高品質 `docs/`：
- `README.md`：quick start、架構總覽、排名/選型理由。
- `installation.md`：精確指令。
- `usage.md`：示例工作流程（用 SDD 規劃功能、用 task.md 平行 agents、做 security review 等）。
2. [ ] 在 `examples/` 加入 2–3 個示例 mini-project 或 workflow demos。
3. [ ] 實作質量閘門：
- 變更時自動 lint / security scan。
- PR/變更的 review prompt 或 agent command。
- 自測腳本，驗證核心命令可運作。
4. [ ] 加入本 `task.md`（以及後續任務追蹤）作為活規格。
5. [ ] 為持續改進執行框架本身建立 critic/review agent prompt 或 skill。

**驗收標準**：
- 新用戶可在 <10 分鐘內從零進入高生產力代理式工作流。
- 文件清晰且與 SDD 對齊。
- repo 乾淨、安全，適合上 GitHub。

---

## Phase 6：未來可擴展性與迭代掛鈎

**目標**：為持續演進做設計（你的 N1ch01as Architect 風格）。

**任務**：
1. [ ] 加入自我改進循環 skill（研究新 skills → 提案新增 → critic 審查 → 合併）。
2. [ ] 透過腳本支援從上游（ECC、技能庫）做簡易更新。
3. [ ] 提供領域專用擴展的 placeholder（例如 trading skills、frontend design、Django/TS stacks）。
4. [ ] 提供使用 ECC dmux + task.md 模式的多代理編排示例。

**驗收標準**：
- 有清晰路徑可演進 starter 而不破壞既有配置。
- 支援你偏好的迭代精修 + critic agent 工作流程。

---

## 給代理的整體執行備註

- **永遠先做 planning/spec 階段**（使用 ECC planning skills 或新的 SDD skills）。
- 任何重疊時**優先採用高排名來源**。
- 對複雜子任務生成 `task.md` / `status.md`（依 ECC dmux pattern）。
- 在主要階段後執行 critic/review。
- 全程追蹤 cost/token 使用。
- 在任何合併或發布前做 security scan。
- 在 `docs/decisions.md` 記錄決策。

**初始實作優先順序**：
1. ECC 基礎（Phase 1）
2. Karpathy + best practices（Phase 2）
3. 記憶 + 精選 skills（Phase 3）
4. Security/hooks/MCP（Phase 4）
5. Docs + validation（Phase 5）

---

**下一個立即行動**  
先執行 Phase 0 research，然後完成 Phase 1 腳手架 + ECC 安裝。以 skeleton + 本 task.md 建立第一個 commit。

本 task.md 本身就是此專案的活 **spec**。隨進度更新它（或讓 critic agent 提案改進）。

**Status**：可開始執行。  
**Owner**：你（或你的 coding agent harness）  
**Created**：2026-06-07

---

*本 task.md 遵循 SDD 原則與來自頂級來源的 harness engineering 最佳實踐。*

```
  
  
