# VA-Agent-Swarm — 系統建構計劃

**文件版本：** 1.0（超詳盡、可立即實施）
**日期：** 2026 年 5 月 29 日
**目標建構代理：** **Claude Code**（Anthropic CLI 編碼代理）
**作者：** 為 Nicholas (nicholas_hui) 自完整的 `study/` 規範語料庫綜合而成
**目的：** 這是一份 **單一、權威、逐步** 的計劃，供一個 AI 編碼代理（Claude Code）從一個空的儲存庫開始，把整個 **VA-Agent-Swarm** — 一個 114 代理、階層式的多代理影片生產系統 — 建構為一個強固、可觀測、生產級的平台。

> **範圍契約：** 本文件 *不* 重新推導系統設計。它假設設計已在 `study/` 中被規範（見 [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md)、[`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md)、[`agents.md`](./agents.md) 以及各代理的功能/技術規範）。本計劃告訴 Claude Code **要建什麼、以何種順序建、有哪些驗收閘門，以及如何運用它自身的工具來可靠地完成。**

---

## 0. 如何使用本文件（先讀 — 本節是給 Claude Code 的）

### 0.1 你在整個建構過程的運作迴圈

你（Claude Code）將把本計劃當作一連串 **里程碑 (Milestones M0–M12)** 執行。對於 *每一個* 里程碑與其中 *每一項* 任務：

1. **先進入 Plan Mode**（`Shift+Tab` → plan mode）。讀取被引用的規範、重述目標、列出你將建立/修改的檔案，並浮現未知項。**在 plan mode 中不要編輯程式碼。**
2. **核對計劃** 是否對齊該里程碑的 *驗收閘門 (Acceptance Gate)* 與 *完成定義 (DoD)*。若有任何含糊，提出一個整合過的問題，而非猜測。
3. **先寫測試**（TDD）。每一個行為單元在實作前都要先有一個失敗的測試。見 §9。
4. **實作** 能讓測試通過的最小增量。
5. **跑本地閘門**：`make verify`（lint + type + unit）。閘門紅燈時絕不前進。
6. **自我審查**，使用 `code-reviewer` 子代理（§2.3）與該里程碑的檢查清單。
7. **提交**，使用引用里程碑的 Conventional Commit 訊息（§11.3，例如 `feat(m2-orchestrator): ...`）。
8. **更新進度**：在 `BUILD_PROGRESS.md` 中勾選該里程碑的檢查項（此檔由你維護 — 見 §0.4）。
9. **`/clear` 情境**，在不相關任務之間清空以保持視窗乾淨。僅在任務中途使用 `/compact`。

### 0.2 「重新思考 100 次」的指令，操作化

使用者要求一份「以全力重新思考 100 次」的計劃。這份強度是結構性地被編碼，而非口號：

- **§14** 是一份字面意義上的 **100 點強化檢查清單**（10 主題 × 10 檢查）。系統在全部 100 點通過前都不算「完成」。
- 參考工作流程已定義一套 **100 遍重新評估紀律**（[`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §1.4）。本建構計劃繼承它：每個里程碑的驗收都會跨五個帶（可追溯性 → 架構 → 交接 → 指標 → 措辭）被重新挑戰。
- 你建的每個代理都必須通過系統自身的 **L1/L2/L3 品質框架** 與 **Q1–Q6 交付 QC 網**（§5.5）。品質是遞迴的：評斷影片的系統本身也必須被評斷。

### 0.3 黃金法則（違反即為缺陷，即使測試通過）

| # | 法則 | 為何 |
|---|------|------|
| G1 | **契約先於程式碼。** 共享 Pydantic 契約（§5）在任何代理之前建好並凍結。每個代理都匯入它們；無人重新定義。 | 防止 114 個分歧的訊息格式。 |
| G2 | **垂直切片先於廣度。** 一條工作流程（Viral Hook，原型 A）在建其餘 108 個代理之前，先端到端跑過真實基礎設施。 | 在規模化前以低成本驗證架構。 |
| G3 | **每個代理都是同一基底類別的實例。** 沒有客製化代理迴圈。新代理是 *設定 + 評分標準 + 工具*，由 Agent Factory（§8）產生。 | 114 個代理必須共用一套生命週期。 |
| G4 | **沒有代理直接與 UI 對話。** 代理發佈到 Event Bus；WebSocket Gateway 扇出。 | 依 [`ui/architecture_communication.md`](./ui/architecture_communication.md)。 |
| G5 | **盡可能決定性。** 釘住 seed、模型版本與提示版本。記入 provenance。 | 重現性 + 審計。 |
| G6 | **成本與安全是閘門，不是事後補。** LLM gateway 自 M3 起計量每個 token；ComplianceAgent 自其存在那刻起即可 BLOCK。 | 依規範；失控的成本/安全會殺死專案。 |
| G7 | **第一天起就把外部生成模型放在介面之後。** 真實的 Sora/Veo/Kling 呼叫昂貴且受速率限制；`MediaGenProvider` 介面讓你能用便宜的樁 (stub) 在 CI 中跑整個 DAG。 | 可測試性 + 成本控制。 |

### 0.4 你在整個建構過程中維護的產物

- `BUILD_PROGRESS.md` — 鏡像 §6 里程碑與 §14 強化的活檢查清單；你隨完成隨勾選。
- `DECISIONS.md` — 一份 ADR（架構決策紀錄）日誌；每個非顯而易見的選擇都有一條註明日期的條目。
- `CLAUDE.md`（根 + 各套件）— 你的持久專案記憶（範本見 Appendix A）。
- `.claude/` — 你的子代理、斜線指令、設定與 hooks（Appendices B–D）。

---

## 1. 使命與建構哲學

### 1.1 在建什麼（一段話）

一個 **多代理系統 (MAS)**，把專業影片生產從客戶 brief 自動化/增強到多通路交付。**114 個專業代理**（10 類別）作為 **LangGraph DAG** 中的節點運行，由 **Temporal** 賦予持久性，透過 **共享產物交接契約** 傳遞創意產物、透過 **CritiqueMessage 匯流排** 傳遞評論，由 **L1/L2/L3 + Q1–Q6 品質網** 閘控，透過 **LangSmith/Grafana** 觀測，並透過 REST + WebSocket 上的 **Next.js 15 控制台** 呈現給人類。跨切面服務（Agentic RAG、Research、GCA、Optimization、DIA、Aesthetics、LLM 成本儀表板）為每個代理提供推理、知識、創造力與品味。

### 1.2 建構哲學

1. **先走骨架 (Walking skeleton)。** 在加肌肉前，先讓最薄的端到端路徑活起來（brief → 1 個代理 → 產物 → UI 事件）。
2. **先平台、後代理。** 約 70% 的硬工程是 *平台*（編排、契約、QC、可觀測性、gateway）。一旦平台對了，代理大多是宣告式的。
3. **工廠勝過手工。** 在平台與 5 個參考代理之後，其餘約 109 個代理由 Agent Factory 從規範產生並審查，而非逐迴圈手寫。
4. **吃自己的狗糧：Coding Agent 規範。** 預期中那個自我建構的「N1ch01as Architect」編碼代理（[`coding_agent_functional_specification.md`](./coding_agent_functional_specification.md)）*正是 Claude Code 在此建構中扮演的角色*。該規範定義的慣例，照辦。
5. **品質是遞迴且可量測的。** 對系統自身套用系統自身的評估哲學：規範符合性 (L1)、評分標準 (L2)、偏好/行為 (L3)。

---

## 2. 目標建構代理：Claude Code 運作模型

本節設定 Claude Code，使它可靠地建構系統，具高度情境衛生與最少返工。**在 M0 中、寫產品程式碼之前就完成此設定。**

### 2.1 `CLAUDE.md` 策略（專案記憶）

Claude Code 會自動從 repo 根（及巢狀套件目錄）載入 `CLAUDE.md` 到情境。把它當作恆常開啟的「憲法」。

- **根 `CLAUDE.md`**（範本見 Appendix A）：技術堆疊 + 釘住版本、monorepo 地圖、7 條黃金法則（§0.3）、build/test/lint 指令、程式風格規則、契約位置，以及「X 的規範在哪裡找」。
- **各套件 `CLAUDE.md`**：每個 `packages/*` 與 `services/*` 都有一份簡短 `CLAUDE.md`，描述其職責、公開 API 與本地測試指令。在該子樹工作時才載入巢狀檔案，使情境緊湊。
- **保持精簡。** `CLAUDE.md` 與任務情境競爭。連結到規範，而非貼上整份。用 `/memory` 檢視；積極修剪。
- 以 `/init` 啟動，再手改以對齊 Appendix A。

### 2.2 模式紀律

| 模式 | 何時 | 觸發 |
|------|------|------|
| **Plan mode** | 每個里程碑/任務之始；任何觸及 >2 檔案或一個契約的變更 | `Shift+Tab` 切 plan mode |
| **Normal（逐次詢問）** | 預設實作 | — |
| **Auto-accept edits** | 僅在單一檔案、有綠色安全網的緊湊 TDD 迴圈內 | `Shift+Tab` |
| **Extended thinking** | 架構、契約設計、除錯並行性、§14 強化遍 | 在提示中說 "think hard" / "ultrathink" |

### 2.3 要建立的子代理 (`.claude/agents/`)

子代理有隔離的情境視窗與受限工具 — 非常適合保持主執行緒乾淨。在 M0 建立（完整定義見 Appendix B）：

| 子代理 | 工作 | 工具（受限） |
|--------|------|--------------|
| `spec-reader` | 讀一份 `study/*.md` 規範，回傳緊湊的結構化摘要 + 當前任務的確切需求/驗收標準。免去主執行緒載入整份規範。 | Read, Grep, Glob |
| `contract-guardian` | 驗證一項變更不會違反或靜默分叉凍結的共享契約（§5）。任何觸及 `packages/contracts` 的提交前執行。 | Read, Grep |
| `test-author` | 給定一個模組 + 其規範段落，先寫失敗的測試套件（unit + 契約測試）。 | Read, Write, Edit |
| `test-runner` | 跑相關測試子集、解析失敗、回傳最小診斷。把冗長測試日誌排除在主視窗外。 | Bash(make test:*), Read |
| `code-reviewer` | 對照里程碑 DoD + §14 檢查清單 + 風格審查 diff；回傳 blocking/major/minor 發現。 | Read, Grep, Bash(git diff:*) |
| `agent-factory-smith` | 專供 M6–M9：把 `agents.md` 中一列 + 其規範，用工廠範本轉成具體的 `AgentConfig`（prompt、rubric、tools、QC）。 | Read, Write, Edit, Grep |

> **使用規則：** 把 *閱讀* 與 *驗證* 委派給子代理；把 *決策* 與 *整合* 留在主執行緒。每個里程碑開頭呼叫 `spec-reader`，而非貼上規範。

### 2.4 要建立的斜線指令 (`.claude/commands/`)

把可重複的工作流程做成受版本控管的提示（完整內容見 Appendix C）：

| 指令 | 目的 |
|------|------|
| `/milestone <id>` | 從本計劃載入里程碑、對其引用規範呼叫 `spec-reader`、進入 plan mode，並草擬任務分解 + 驗收清單。 |
| `/new-agent <number>` | 對 `agents.md` 的一個代理編號執行代理實作手冊（§8）。 |
| `/verify` | 跑 `make verify` 並摘要失敗與建議修法。 |
| `/contract-check` | 對暫存 diff 呼叫 `contract-guardian`。 |
| `/gate <Q1..Q6\|L1..L3>` | 對給定產物/模組跑指名的 QC 層並報告通過/失敗與證據。 |
| `/adr <title>` | 從當前討論把一條註明日期的新 ADR 追加到 `DECISIONS.md`。 |
| `/harden <theme>` | 把 §14 100 點清單的 10 主題之一作為聚焦稽核執行。 |

### 2.5 要設定的 MCP 伺服器 (`.mcp.json`，專案範圍)

漸進式設定 — 只在里程碑需要時：

| MCP 伺服器 | 里程碑 | 用途 |
|------------|--------|------|
| **Postgres**（唯讀角色） | M2 | 除錯 orchestrator 時讓 Claude Code 檢視 schema/狀態。 |
| **Filesystem**（限於 repo） | M0 | 已由原生工具涵蓋；僅在需要處理大型資產目錄時加入。 |
| **GitHub** | M0 | CI 中的 PR/issue 自動化（headless 模式）。 |
| **LangSmith / 可觀測性**（若可用） | M8+ | 除錯代理執行時拉取 traces。 |
| **Temporal**（自訂，選用） | M2 | 檢視 workflow 歷史。 |

> 讓 MCP 最小化。每個伺服器都增加工具表面與情境負擔。盡量偏好 repo 自身的 `make` 目標與型別化 SDK，而非臨時 MCP。

### 2.6 Hooks (`.claude/settings.json`)

圍繞你動作的決定性自動化（事件：`PreToolUse`、`PostToolUse`、`UserPromptSubmit`、`Stop`、`SubagentStop`、`PreCompact`、`SessionStart`）：

| Hook | 事件 | 動作 |
|------|------|------|
| **自動格式化** | `PostToolUse` 對 `*.py`/`*.ts` 的 Edit/Write | 對變更檔跑 `ruff format` / `prettier`。 |
| **封鎖受保護路徑** | `PreToolUse` 對 Edit/Write | 拒絕對 `packages/contracts/**` 的編輯，除非提示明確說「contract change」且 ADR 存在。執行 G1。 |
| **type/lint 閘** | `Stop` | 跑 `make verify`；若紅燈，浮現失敗，使該回合不在破損樹上結束。 |
| **密鑰掃描** | `PreToolUse` 對 Bash | 封鎖會列印/提交 `.env` 或金鑰的指令。 |
| **進度提醒** | `Stop` | 若完成一項里程碑任務，提醒更新 `BUILD_PROGRESS.md`。 |

### 2.7 權限與沙盒

- 在 `.claude/settings.json` 維護安全、高頻指令的允許清單（`make *`、`pytest`、`pnpm *`、`git status/diff/add/commit`、`docker compose *`）。
- **絕不** 允許破壞性/不可逆指令（`git push --force`、`rm -rf`、prod 部署）。那些需要明確的人類確認。
- 在 CI/headless（`claude -p`）中，於容器內以 `--dangerously-skip-permissions` 執行 *僅僅因為* 容器即沙盒 — 絕不在有憑證的開發機上。

### 2.8 情境衛生與並行

- **`/clear`** 在里程碑與不相關任務之間。臃腫的視窗會導致回歸與自相矛盾。
- **`/compact`** 在長任務的自然斷點；compact 前把一行狀態摘要寫進 `BUILD_PROGRESS.md`，以免遺失。
- **Git worktrees** 供安全的並行軌道（例如 UI 一個 worktree、meta-agents 另一個），免去分支抖動：`git worktree add ../swarm-ui feature/m10-ui`。
- 任何會把大量輸出（測試日誌、規範文本、grep 掃描）倒進主執行緒的子調查，偏好用 **子代理**。

### 2.9 完成定義（適用每項任務）

一項任務只有在 **全部** 成立時才算 **完成**：
1. 行為由 *先於程式碼* 寫好的測試覆蓋；全綠。
2. `make verify` 通過（ruff + mypy/pyright + eslint + tsc + unit）。
3. 公開型別/契約未變，或經 ADR + `contract-guardian` 簽核後變更。
4. `code-reviewer` 子代理回傳無 blocking/major 發現。
5. 相關里程碑驗收閘門標準達成並附證據（記於 `BUILD_PROGRESS.md`）。
6. 已做 Conventional Commit；無密鑰、無除錯殘渣、無未追蹤 `TODO`。
7. 文件已更新：若公開表面改變，更新套件 `CLAUDE.md`/README。


---

## 3. 技術堆疊決策（已釘住）

這些是 **決策，不是選項**。任何偏離記為一條 ADR。版本在建構開始時釘住；`dependency-upgrade` 里程碑 (M12) 是唯一移動它們的地方。

### 3.1 語言與執行期

| 關注點 | 選擇 | 備註 |
|--------|------|------|
| 後端 / 代理 | **Python 3.12** | LangGraph、Temporal SDK、litellm、ML 工具皆 Python 優先。 |
| Python 環境與相依 | **uv**（lockfile 驅動） | 快速、可重現；單一 workspace lock。 |
| 前端 | **TypeScript 5.x, React 19, Next.js 15 (App Router)** | 依 [`ui/architecture_communication.md`](./ui/architecture_communication.md)。 |
| JS 套件管理 / monorepo | **pnpm workspaces + Turborepo** | 跨 `apps/*` + `packages/*`（TS 側）快取建置。 |
| Lint/格式 | **ruff** (Py), **eslint + prettier** (TS) | 由 hooks + CI 強制。 |
| 型別 | **pyright/mypy (strict)** (Py), **tsc strict** (TS) | 公開表面不得無型別。 |
| 測試 | **pytest + pytest-asyncio + hypothesis** (Py), **vitest + Playwright** (TS) | 契約用屬性測試；UI E2E 用 Playwright。 |

### 3.2 平台服務

| 關注點 | 選擇 | 理由（出自規範） |
|--------|------|------------------|
| 代理編排 (DAG) | **LangGraph** | DAG + 條件邊 + 一等 HiTL 閘 + checkpointing。 |
| 持久 workflow 引擎 | **Temporal (Python SDK)** | 生產跑數分鐘→數小時；保證交付、重試、replay。 |
| Event bus | **Redis Streams**（dev/MVP）→ **NATS JetStream**（規模） | pub/sub + 持久化 + replay；每生產一 topic。 |
| 關聯式儲存 | **PostgreSQL 16** + **SQLModel/SQLAlchemy 2 + Alembic** | 生產 metadata、閘狀態、評論、設定、審計日誌。（規範提及 Drizzle；因 gateway 是 FastAPI，我們統一用 Python ORM。TS 型別由 Pydantic 生成 — 見 §5.6。ADR-001。） |
| 物件儲存 | **S3 / Cloudflare R2**（經 `boto3`/S3 API） | 影片/音訊/圖像產物；內容定址鍵。 |
| 向量 DB | **Chroma**（dev）→ **Pinecone/Weaviate**（prod） | MemoryAgent + Agentic RAG 檢索。 |
| 圖/混合 RAG | **LightRAG over OpenSearch** | 依 [`agentic_rag_functional_specification.md`](./agentic_rag_functional_specification.md)。 |
| 快取 / session / 限流 | **Redis** | 熱資料、鎖、token bucket。 |
| API gateway | **FastAPI** + **uvicorn/gunicorn** | REST + WebSocket gateway。 |
| LLM 存取 | **litellm** 統一客戶端 | 對 Grok-4.x、Gemini 2.5 Pro、GPT-4o、Claude 4、OSS 的單一介面。 |
| 可觀測性 | **LangSmith**（代理 trace）+ **OpenTelemetry → Grafana/Tempo/Loki** | trace、指標、日誌、replay。 |
| Provenance | **C2PA**（`c2pa-python`） | 簽署每個產物；下游驗證鏈。 |
| 容器化 | **Docker** + **docker-compose**（dev）→ **Kubernetes + Helm**（prod） | 生成任務用 GPU 節點池；純 LLM 用 CPU 池。 |
| 密鑰 | **Doppler/Vault**（prod），`.env` + `direnv`（dev，gitignored） | 絕不入 repo。 |

### 3.3 外部工具供應商（在介面之後 — 代理絕不直接呼叫）

| 能力 | 供應商 | 要建的介面 |
|------|--------|-----------|
| 文字/影片生成 | Sora 2, Veo 3.1, Runway Gen-4.5, Kling 3.0, Seedance 2.0, Grok Imagine | `MediaGenProvider`（§5.4）並附 CI 用的 `MockGenProvider` |
| TTS / 聲音複製 | ElevenLabs v3 | `VoiceProvider` |
| 對嘴 | Sync.so | `LipSyncProvider` |
| 音樂 | Udio / Suno | `MusicProvider` |
| 空間音訊 | Dolby Atmos Renderer | `MixProvider` |
| 評估指標 | VBench, EvalCrafter, CLIP-T, ArcFace, FVD, loudness (ITU-R BS.1770) | `EvalToolProvider` |

> **決策 (ADR-002)：** 所有供應商實作一個共同 `Provider` 協定，含 `capabilities()`、`estimate_cost()`、`invoke()`、`health()`。`RouterAgent` 依成本/品質/延遲在供應商間選擇。CI 全程僅用 mock 供應商。

---

## 4. Monorepo 拓樸與儲存庫骨架

### 4.1 頂層佈局

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

### 4.2 骨架建構順序（M0 產出此骨架，空但可編譯）

1. `packages/contracts`（憲法）→ 2. `packages/observability` + `packages/eventbus` → 3. `packages/agent-core` → 4. 其餘皆為匯入契約且能通過 `make verify` 的樁。

> **規則：** 每個套件自存在那刻起就附 `__init__.py`/`index.ts`、一份 `CLAUDE.md`、一個 `tests/` 目錄，以及至少一個通過的瑣碎測試，使 `make verify` 在每次提交都綠燈。

---

## 5. 跨切面契約（先建這些 — 它們被凍結）

這是最重要的一節。**下游一切皆匯入自 `packages/contracts`。** 在 M0–M1 建好、凍結，並把變更閘控在 ADR + `contract-guardian`（G1）之後。事實來源：[`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §1.3、§6 與 [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md) §7。

### 5.1 共享產物交接契約

一個單一 Pydantic v2 模型，隨每個產物在階段間攜帶。欄位與規範表 1:1 對應。

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

**契約測試（先寫）：** JSON 來回序列化；向後相容 schema 快照測試（若移除/改名欄位而無版本升版則失敗）；`parent_assets` 構成有效 DAG（無環）；每個已發佈產物都有非空的 `provenance_manifest`。

### 5.2 CritiqueMessage 匯流排 schema

逐字出自 [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §6。這是任何代理對任何其他代理評論的方式。

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

**驗收規則（在 `agent-core` 實作，徹底測試）：**
- `blocker` → 暫停該 DAG 節點直到解決（Temporal signal / LangGraph interrupt）。
- `major` → 在接收者上觸發 Self-Refine/Reflexion 迴圈，**最多 3 次迭代**，然後升級至 JudgeAgent。
- `minor`/`nit` → 記入 MemoryAgent；聚合為下一訓練週期的 RLAIF 獎勵訊號。
- 兩代理爭議 → 路由至 JudgeAgent（多代理辯論）。ComplianceAgent 的評論永遠是 `blocker`（BLOCK 閘）。

### 5.3 共同代理基底類別

114 個代理中的每一個都是 `BaseAgent` 的實例 (G3)。來源：[`common-agent-structure.svg/html`](./common-agent-structure.html) 與各代理規範表（職責、知識來源、自我品質、超越訊號、評論進/出）。

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

基底類別接入：LLM gateway（計量）、RAG 客戶端、MemoryAgent、event-bus 發佈、provenance 簽署、OTel span。**任何代理子類別都不重新實作這些。** 特化只在 `AgentConfig` 上不同。

### 5.4 供應商介面（可 mock）

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

**規則：** CI 與所有 unit/integration 測試使用 mock。單一的每夜「live-smoke」工作在預算上限後方才打真實供應商（§10.2）。

### 5.5 品質網 — L1/L2/L3 + Q1–Q6

出自 [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §5。在 `packages/qc` 實作。orchestrator 僅在節點所需 QC 層通過時才推進。

| API | 層 | 機制 | 通過 |
|-----|-----|------|------|
| `qc.l1_spec(artifact)` | Spec | JSON-schema + 工具驗證器（codec/LUFS/aspect/length） | 100% |
| `qc.l2_rubric(artifact, rubric)` | Rubric | LLM-as-judge 配角色憲法 | ≥85/100 |
| `qc.l3_preference(artifact, baseline)` | Preference | 對人類參考成對 + AudienceSim ≥200 personas + ≥20 HiTL | ≥0.50 平手 / ≥0.55 超越 |
| `qc.delivery(artifact)` | Q1–Q6 | spec / artifact / audio-sync / continuity / perceptual / outlet-readiness | 6 項全過 |

**建構備註：** L1 與 Q1/Q3/Q6 是決定性驗證器（先建，完全可測）。L2/L3/Q5 用 LLM/sim 評審（以 frozen-judge + golden set 建，使其穩定；切勿讓評審模型未釘住漂移）。

### 5.6 型別傳播到前端

從 Pydantic 契約生成 TS 型別，使 UI 永不漂移：`datamodel-code-generator`/`pydantic2ts` → `packages/contracts/ts/`。Turborepo 任務 `contracts:gen` 在 CI 執行；若生成型別過期則 build 失敗。這使 WebSocket 事件 payload 與 REST body（出自 [`ui/architecture_communication.md`](./ui/architecture_communication.md)）端到端型別安全。

### 5.7 Event-bus topic 契約

Topics（出自 `ui/architecture_communication.md`）：`production.{id}.agent_events`、`.critiques`、`.gates`、`.artifacts`，外加 `system.alerts`。每個事件都是型別化 WebSocket 事件模型之一（`agent_state_change`、`artifact_created`、`critique_message`、`gate_ready`、`gate_resolved`、`budget_update`、`metric_update`、`memory_entry`、`tool_call`、`production_phase_change`、`error`）。它們住在 `packages/contracts/events.py`，且是匯流排上 *唯一* 允許的形狀。


---

## 6. 分階段建構路線圖（里程碑 M0–M12）

**排序原則**（出自 [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md) §11）：Foundation → Intelligence → Production → Enhancement，但早在 M6 就打穿一條 **垂直切片 (G2)**，使架構在廣度之前獲得驗證。

以下每個里程碑指明：**目標 · 相依 · 建構（檔案）· Claude Code 工作流 · 測試 · 驗收閘門**。把驗收閘門當作硬停止 — 在它綠燈並記錄於 `BUILD_PROGRESS.md` 之前，不要開始下一個里程碑。

> **工作量註記：**「週」是用於排序的 *相對規模*，非承諾。單一 Claude Code session 可完成多項小任務；大里程碑（M2、M7、M10）跨多個 session，任務間 `/clear`。

### 里程碑相依圖

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

### M0 — Bootstrap、基礎設施與 Claude Code 設定

**目標：** 一個可編譯、綠燈、工具齊備的空 monorepo，所有 Claude Code 設定就位。尚無功能 — 但 `make verify` 通過，且 `docker compose up` 帶起每個後端服務。

**相依：** 無。

**建構：**
- §4.1 的 repo 骨架（每個 package/service 為可匯入的樁，附一個通過測試）。
- `Makefile` 目標：`bootstrap`、`verify`（lint+type+unit）、`test`、`test-int`、`dev`、`fmt`、`contracts:gen`、`up`、`down`、`clean`。
- `docker-compose.yml`：postgres、redis、temporal（+UI）、opensearch、chroma、minio（S3 相容）。
- `pyproject.toml`（uv workspace）+ `pnpm-workspace.yaml` + `turbo.json`，版本全釘住（§3）。
- CI 流水線（§11）：lint → type → unit → contract-snapshot → build。
- **Claude Code 設定：** 根 + 各套件 `CLAUDE.md`（Appendix A）、`.claude/agents/*`（Appendix B）、`.claude/commands/*`（Appendix C）、`.claude/settings.json` hooks/權限（Appendix D）、`.mcp.json`（僅 Postgres+GitHub）。
- 種下 `BUILD_PROGRESS.md` 與 `DECISIONS.md`（ADR-001、ADR-002）。

**Claude Code 工作流：** 以 `/init` 起手；手改 `CLAUDE.md` 到 Appendix A。建立子代理/指令。用 plan mode 鋪設骨架；逐套件生成，每次後跑 `make verify` 以維持連續綠燈。

**測試：** 每套件一個瑣碎測試；CI 證明矩陣（Py 3.12、Node 20）綠燈；`docker compose up` 健康檢查通過。

**驗收閘門 G-M0：** 自乾淨 clone，`make bootstrap && make up && make verify` 全綠；`.claude/` 子代理可呼叫；ADR 日誌已起。M1 前 ✅。

---

### M1 — Foundation：Agentic RAG（知識骨幹）

**目標：** 每個代理都會呼叫的共享知識服務。規範：[`agentic_rag_functional_specification.md`](./agentic_rag_functional_specification.md)。

**相依：** M0。

**建構 (`packages/rag`)：**
- 匯入流水線：chunk → embed → 索引進 Chroma（dev）+ LightRAG/OpenSearch 圖層。
- 混合檢索：vector + graph + keyword，含 rerank；查詢規劃（決定取什麼的「agentic」檢索）。
- `RAGClient` API：`retrieve(query, filters, k)`、`compound(query)`（多跳）、`ingest(doc)`、`cite()`（為 FactChecker/Citation 代理回傳來源分級的 provenance）。
- 知識命名空間：每專案、每領域、全域（使專案的 world-bible 被隔離）。
- 新鮮度/逐出 + CI 用的決定性離線嵌入模型選項。

**Claude Code 工作流：** 對 RAG 規範用 `spec-reader` → 規劃命名空間 + 檢索模式 → 對小 golden 語料庫（5 文件）TDD `RAGClient` → 在介面後整合 Chroma/OpenSearch（unit 測試 mock 嵌入，`make test-int` 用真實）。

**測試：** golden 語料庫 Q&A 集上 precision@5 ≥ 0.9；引用分級正確回傳 primary/secondary/tertiary；多跳 compound 查詢回傳連結證據；命名空間隔離（專案 A 看不到專案 B）。

**驗收閘門 G-M1：** `RAGClient` 在 golden set 通過 precision 目標；graph + vector 皆查詢；回傳 provenance 分級引用。✅

---

### M2 — Foundation：編排執行期（控制平面）

**目標：** 跳動的心臟 — 由 Temporal 賦予持久性的 LangGraph DAG 執行，接到 Event Bus 與 Asset/State 儲存。這是最大的平台里程碑。

**相依：** M0（契約）、M1（使節點能呼叫 RAG）。

**建構：**
- `packages/eventbus`：型別化 Redis Streams pub/sub；topic 契約（§5.7）；可 replay；at-least-once + 冪等鍵。
- `packages/observability`：OTel tracing + 結構化日誌 + LangSmith 接入；每次節點執行是一個 span。
- `services/orchestrator`：
  - **LangGraph graph 執行期**：節點=代理任務；條件邊；**HiTL interrupt** 點（閘）；以 Postgres 為後盾的 checkpointer。
  - **Temporal workflows/activities**：每個代理任務是一個 Temporal activity（retry/backoff/timeout）；生產是一個 Temporal workflow（跨重啟可恢復）。
  - **OrchestratorAgent / PlannerAgent / RouterAgent / JudgeAgent / GateKeeperAgent / MemoryAgent** 骨架（代理 #53–58）— 這些是 *平台* 代理，此處建好，M8 精煉。
  - DAG 基本元件：fan-out/fan-in、相依觸發重渲染、死鎖偵測、SLA 計時器。
- `packages/memory`：在向量 DB 上的情節 + 長期專案記憶（Reflexion/MemGPT 模式）；`MemoryAgent` 檢索 API。
- Asset/Data 骨幹：不可變 `artifact_id`、copy-on-write 版本、相依邊、可搜尋 metadata（Postgres + S3/MinIO），經 `packages/provenance` 做 C2PA 簽署。
- 狀態儲存：生產狀態機；閘狀態；持久、可審計、可恢復。

**Claude Code 工作流：** 這是個 "think hard" 里程碑。明確規劃 LangGraph↔Temporal 邊界（ADR-003：*什麼住在 LangGraph vs Temporal*）。先建 event bus + 2 節點玩具圖（echo → echo），藉中途砍掉 worker 並恢復來證明持久性。再加 HiTL interrupt，再加平台代理骨架。除錯時用 Postgres MCP 檢視 checkpoint。

**測試：** 砍-恢復整合測試（DAG 中途 worker 崩潰 → 自 checkpoint 恢復，無遺失/重複任務）；fan-out/fan-in 正確性；blocker 評論暫停節點；閘 interrupt 等外部 signal 後續行；事件 replay 重建完整狀態；死鎖偵測器在循環計劃上跳脫。

**驗收閘門 G-M2：** 一個硬編碼 3 節點 DAG（`Planner → echo-agent → GateKeeper`）在真實 Temporal+Redis+Postgres 上端到端執行、在中途 worker 砍掉後存活、發出正確型別化事件，並以 C2PA 簽署產物。✅ 這是 *走骨架*。

---

### M3 — Foundation：LLM Gateway、Router 與成本儀表板

**目標：** 自第一天起每個 token 都被計量與路由（G6）。規範：[`llm_usage_functional_specification.md`](./llm_usage_functional_specification.md)；RouterAgent 見 [`agents.md`](./agents.md) §9。

**相依：** M2。

**建構：**
- `packages/llm-gateway`：litellm 包裝，公開 `complete()/stream()/embed()`，含：供應商/模型抽象（Grok-4.x、Gemini 2.5 Pro、GPT-4o、Claude 4、OSS）、自動 retry/fallback、**每次呼叫的 token+成本計量** 發到匯流排（`budget_update`）、把 prompt+模型 **版本標記** 入 provenance（G5）、回應快取，以及供 QC 用的 **frozen-judge** 模式。
- **RouterAgent (#55)** 真實實作：能力註冊表 + 基準歷史 → 依成本/品質/延遲挑代理/模型；預算感知。**CostOptimizerAgent (#74)** 掛鉤。
- **LLM 使用儀表板** 後端：聚合每生產/代理/供應商的花費；警示門檻；公開 `/api/llm-usage`。
- 預算護欄：每生產預算信封；超支時硬停止 + 升級（ProducerAgent 閘）。

**Claude Code 工作流：** 先 TDD 計量數學（依各供應商價目表的 golden token→cost fixture）。把註冊表做成資料（`agents/_registry.yaml` + 一張基準表），使路由可設定而非硬編碼。

**測試：** 每供應商成本正確計算；供應商錯誤時 fallback；超支暫停 + 發升級；router 在 fixture 矩陣上挑 Pareto 最佳供應商；快取命中免去呼叫；每次呼叫把模型+prompt 版本寫入 provenance。

**驗收閘門 G-M3：** 任何代理呼叫皆被計量、路由、版本標記，並在成本儀表板可見；預算突破觸發真實停止。✅

---

### M4 — Foundation：Research Agent + Coding Agent 工具組

**目標：** 知識取得服務與自我建構慣例。規範：[`research_agent_functional_specification.md`](./research_agent_functional_specification.md)（+技術規範）、[`coding_agent_functional_specification.md`](./coding_agent_functional_specification.md)。

**相依：** M1（RAG）、M3（gateway）。

**建構：**
- **Research Agent**（`agents/crosscutting/research/`）：查詢規劃 → 多源檢索（web + archive，經供應商）→ 綜合 → 來源分級、附引用的 dossier（寫入 RAG 命名空間）。子能力對應 meta-agents #66–72（M8 完整建構；此處建它們共用的核心服務）。
- **Coding Agent 工具組**：把 [`coding_agent_functional_specification.md`](./coding_agent_functional_specification.md) 慣例編碼為專案自身的 `.claude/` 標準（這 *正是* Claude Code 的劇本）。建它依賴的 `agent-factory` 骨架（範本、驗證器）— 雖然工廠廣度在 M6 才來。

**Claude Code 工作流：** 注意 Coding Agent 規範描述的是 *你自己的角色*。把其慣例（命名、結構、審查標準）擷取進 `CLAUDE.md` 與 `code-reviewer` 子代理，使其在後續建構中被強制執行。

**測試：** Research Agent 回傳一份 dossier，其每個論點都帶分級來源；拒絕斷言無引用的論點（FactChecker 式守衛）；dossier 被匯入並可經 RAG 檢索。

**驗收閘門 G-M4：** Research Agent 對測試主題產出分級、附引用的 dossier 並存入 RAG；編碼慣例由 `code-reviewer` 強制。✅

---

### M5 — Intelligence 層（推理服務）

**目標：** 每個生產代理消費的共享「大腦」。規範：[`intent_analysis_agent_functional_specification.md`](./intent_analysis_agent_functional_specification.md) (DIA)、[`general_creative_agent_functional_specification.md`](./general_creative_agent_functional_specification.md)+技術 (GCA/SSOR)、[`optimization_agent_functional_specification.md`](./optimization_agent_functional_specification.md)+技術、[`strategic_goal_achievement_agent_functional_specification.md`](./strategic_goal_achievement_agent_functional_specification.md)、[`complex_problem_solution_process_model.md`](./complex_problem_solution_process_model.md)、[`aesthetics_agent_functional_specification.md`](./aesthetics_agent_functional_specification.md)。

**相依：** M1–M4。

**建構（各為一個跨切面服務代理，皆在 `BaseAgent` 上）：**
1. **DIA（深度意圖分析）** — 解析 brief → 結構化意圖（目標、受眾、隱藏議程、約束）。每個生產的進入點。
2. **GCA (SSOR)** — 創意 ideation 引擎；7 階段 SSOR 流水線 + 領域工廠。由 Director/Screenwriter/ConceptArtist/Ideation 消費。
3. **Process Optimization Agent** — 在工作流遙測上的 DMAIC + Lean + 多代理共識。
4. **Strategic Goal Achievement** — 所有規劃代理使用的 6 階段目標釐清框架。
5. **Complex Problem Solving** — 供診斷代理用的 WHAT/WHY/HOW/DO/REVIEW 方法論。
6. **Aesthetics Agent** — 分解式多模態評審 + 對齊者 + 品味守護者（依你撰寫的規範）；供給 `qc.l2`/感知評分、給 GCA 的新穎性 (D9)，以及 `aesthetic` 評論。把其 `AestheticVerdict` 接入 `packages/qc` 與評論匯流排。

**Claude Code 工作流：** 每服務一個子任務；之間 `/clear`。每個遵循代理實作手冊（§8）。GCA 與 Aesthetics 構成生成↔評估迴圈 — 建 GCA 的新穎性分數去 *呼叫* Aesthetics Agent（勿重複）。

**測試：** DIA 從樣本 brief 擷取結構化意圖 schema（golden set）；GCA 產出帶逐維度分數的可追溯 SSOR 輸出；Aesthetics 回傳分解 `AestheticVector` + `hack_likelihood` 並對低信心升級；Optimization 在遙測 fixture 上提出可量測的工作流增量。

**驗收閘門 G-M5：** 六項推理服務皆可經 gateway 呼叫，各通過其 golden-set 行為測試；展示 GCA↔Aesthetics 迴圈。✅

---

### M6 — Agent Factory + 垂直切片（Workflow A，端到端）⭐

**目標：** 在建另外 109 個代理之前，用最便宜的真實工作流證明 *整個* 架構（G2）。實作 **Agent Factory** 與剛好足夠的工藝代理，以在真實基礎設施上（用 mock 生成供應商）端到端跑 **Workflow A — Viral Hook Clip**。

**相依：** M2–M5。

**建構：**
- **Agent Factory**（`packages/agent-factory`）：`AgentConfig (YAML) → 可執行 BaseAgent`。驗證 prompt/rubric/tools/QC 引用；註冊進 `agents/_registry.yaml`；生成各代理測試骨架。這是 M7–M9 的引擎。
- **Workflow A 工藝代理**（子集，經工廠）：TrendIntelligenceAgent、CopywriterAgent、SocialMediaStrategistAgent、PromptEngineerAgent/GeneratorOperator、AIQAConsistencyAgent、EditorAgent、AccessibilityOptimizerAgent、AudienceSimAgent、AnalystAgent — 正是 [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3.1 的班底。
- **Workflow A DAG**（`workflows/A_viral_hook.py`）：Concept → Production → Post → Review → Distribution → Post-launch，含規範的評審閘。
- 端到端執行：brief → DIA → Planner 建 A-DAG → 代理執行（mock 生成）→ 產物帶交接契約流動 → 評論匯流排啟動 → QC 網閘控 → C2PA 簽署交付物 → 事件上匯流排。

**Claude Code 工作流：** "ultrathink" 工廠設計 — 它日後必須產出全部 114 代理，故其 `AgentConfig` schema 現在就要完整。建工廠 + 一個代理 + 其測試，再建其餘班底，再建 DAG，再建 E2E 測試。每個代理 config 用 `agent-factory-smith` 子代理。

**測試：** Workflow A 在 mock 上的完整 E2E 整合測試（決定性）；每個代理在 golden 輸入通過 L1+L2；一個 `blocker` 評論暫停並重新路由；端到端計量預算；可從最終產物驗證 provenance 鏈回到 brief。

**驗收閘門 G-M6（關鍵）：** `make e2e-workflow-a` 從一個 brief 產出簽署交付物，每個交接契約皆填妥、每個閘皆強制、所有事件皆發出、完整 provenance、預算內 — 使用 mock 供應商。**此閘證明平台。在它穩如磐石前，不要進入廣度。** ✅

---

### M7 — 生產代理 1–52（經工廠的廣度）

**目標：** 把其餘工藝代理（類別 1–8：代理 #1–52）實作為工廠產出的 config + rubric + prompt。規範：[`agents.md`](./agents.md) §1–8 與 [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §2.1–2.8；Screenwriter 深規範（[`screenwriter_strategic_goal_achievement_agent_functional_specification.md`](./screenwriter_strategic_goal_achievement_agent_functional_specification.md)）與共享 VO/podcast 模式。

**相依：** M6。

**建構：** 對每個代理，手冊（§8）產出：`AgentConfig`、版本化 system prompt、L2 rubric/憲法（在 `eval/rubrics/`）、自我品質指標接線（如 DoP：rule-of-thirds + exposure-zone + color-temp；Colorist：ΔE<2；SoundMixer：LUFS+STOI 等 — 規範表已逐一列舉）、工具允許清單，以及評論進/出邊（出自 §4 評論矩陣）。按類別分批以共享 rubric 骨架。

**Claude Code 工作流：** 每代理用 `/new-agent <n>`。逐類別處理（camera 6–8、editorial/color 9–18、sound 19–22、performance 23–27、marketing 28–31、domain 32–45、AI-era 46–52）。類別間 `/clear`。每代理由 `spec-reader` 拉其確切列（自我品質、超越訊號、評論邊）→ 工廠 config → 測試 → 審查。

**測試：** 每代理：L1 schema 符合；其 golden 輸入上 L2 rubric ≥85；依矩陣發/收評論；遵守工具允許清單；被計量。類別級整合測試（如 DoP→Colorist→Editor 交接保留 continuity_state）。

**驗收閘門 G-M7：** 全部 52 工藝代理註冊，各在 L1+L2 golden 測試與評論矩陣測試綠燈；至少 3 個額外工作流原型（如 C Animated Explainer、E AI Short Film、B UGC Ad）在 mock 上端到端執行。✅

---

### M8 — Meta-Agents 53–80 + 完整 QC 網 + 閘控

**目標：** 把 M2 平台代理骨架升級為完整實作，並加入「塑造工作如何完成」的創意/研究/最佳化 meta-agents。規範：[`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §2.9。

**相依：** M7。

**建構：**
- **Orchestration (53–58)：** 強化 Orchestrator/Planner/Router/Judge/GateKeeper/Memory，具完整爭議解決（多代理辯論）、stage-gate 簽核，以及 escaped-defect=0 紀律。
- **Creative (59–65)：** Ideation、NarrativeArc、StyleTransfer、MoodBoard、Novelty/Anti-Cliché、EmotionalArc、WorldBuilding — 多數委派給 GCA/Aesthetics（不重複）。
- **Research (66–72)：** Web/Archive/Trend/Competitor/Citation/InterviewSynthesis/Benchmark — 建在 M4 Research Agent 核心上。
- **Optimization (73–80)：** Prompt/Cost/Latency/Retention/ROAS/Accessibility 最佳化器 + EvaluationHarness + SafetyRedTeam。
- **完整 QC 網**：完成 L3（AudienceSim ≥200 personas + HiTL 抽樣）與 Q1–Q6 交付驗證器；`GateKeeperAgent` 強制「零洩漏缺陷」。

**Claude Code 工作流：** 按家族建。`EvaluationHarnessAgent` (#79) 與 `SafetyRedTeamAgent` (#80) 是力量倍增器 — 在 M8 早期就建，使其持續測試其餘一切（回歸警示、對抗探測）。

**測試：** Judge 對 fixture 人類面板 inter-rater 一致度 κ≥0.8；GateKeeper 封鎖一個種下的缺陷；SafetyRedTeam 在種下攻擊集上 attack-success ≤1%；EvaluationHarness 在 <1h 偵測注入的回歸；AudienceSim L3 win-rate 在 golden 配對上計算。

**驗收閘門 G-M8：** 全部 80 代理上線；每條發佈路徑強制完整 L1/L2/L3 + Q1–Q6；red-team + eval-harness 在 CI 每夜持續執行。✅

---

### M9 — 工作流支援代理 81–114 + 交付織體

**目標：** 生產基礎設施代理與多通路交付。規範：[`agents.md`](./agents.md) §10；交付分支見 [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3.0。

**相依：** M8。

**建構：**
- **81–90** 資產管理/版本控管/render 派發：RenderFarmAgent（GPU 批次派發 + 自動擴展）、AssetManagerAgent、VersioningAgent、DependencyRerenderAgent。
- **91–100** 品質閘/交付封裝/合規：DeliveryAgent、QCGateAgent，封裝為 DCP / streaming mezzanine / broadcast master / archive / trailer / social cutdowns，含 outlet 專屬規格、字幕、metadata、DRM/KDM、C2PA payload。
- **101–114** 分析/回饋/再訓練：AnalyticsAgent、FeedbackLoopAgent、RetrainingTriggerAgent（自 minor/nit 評論聚合 RLAIF 獎勵）、CorrectionsAgent。
- **交付織體**：分支流水線（theatrical/streaming/broadcast/archive + 行銷衍生並行）含每 outlet 驗證。

**Claude Code 工作流：** 代理用工廠 config；RenderFarm 自動擴展與交付封裝驗證器做真實工程（決定性 — 重度 TDD）。把 post-launch 學習迴圈接到 Optimization Agent (M5) 與 RetrainingTrigger。

**測試：** 交付封裝器發出每個 outlet 變體並通過 Q6；RenderFarm 在排隊作業 fixture 下自動擴展；相依變更觸發正確重渲染集；RLAIF 聚合從已記錄 nit 評論產出獎勵增量。

**驗收閘門 G-M9：** 一個生產產出全部四條交付分支 + 行銷衍生，各 Q6 有效且帶 provenance；post-launch 遙測回流進一張再訓練工單。✅


---

### M10 — UI：控制台、API Gateway 與 WebSocket 層

**目標：** 人類操作者介面。規範：全部 [`ui/`](./ui/) — [`architecture_communication.md`](./ui/architecture_communication.md)、[`agent_management_ui.md`](./ui/agent_management_ui.md)、[`backend_agent_management.md`](./ui/backend_agent_management.md)、[`ui_design.md`](./ui/ui_design.md)、[`project_creation_flow.md`](./ui/project_creation_flow.md)、[`production_scale_discovery.md`](./ui/production_scale_discovery.md)、[`video_remake_enhancement.md`](./ui/video_remake_enhancement.md)、[`RETHINK_100_IMPROVEMENTS.md`](./ui/RETHINK_100_IMPROVEMENTS.md)。

**相依：** M3（事件已存在）；**可在 M3 後於 git worktree 並行啟動**，先對假事件發射器開發，再整合。

**建構：**
- `services/api-gateway` (FastAPI)：REST 端點 + WebSocket gateway，完全依 [`architecture_communication.md`](./ui/architecture_communication.md) 的 API 契約表（`POST /api/productions`、gate decisions、critiques、retry/skip、router-config、artifacts、delivery）。Auth/RBAC、限流、驗證、閘核可時的 C2PA 簽署。訂閱 Event Bus，依 `production_id` 過濾，經 WebSocket 扇出。
- `apps/web` (Next.js 15 + React 19)：Brief Studio、DAG Canvas（即時節點狀態）、Artifact Gallery、Critique Feed、Gate Approval Dialog、Budget Tracker、Quality Dashboard、Agent Inspector、Memory Panel、Delivery Hub。狀態用 Zustand + React Query；WebSocket 用 socket.io-client（自動重連、每生產一房間）。型別匯入自生成的 `packages/contracts/ts`（§5.6）。
- 專案建立流程 + 生產規模探索（S0–S? 規模設定檔）+ 影片重製/增強流程。

**Claude Code 工作流：** 先建 gateway（型別化、測試），使 UI 有真實契約。再建 UI 元件，由 WebSocket 事件型別驅動。關鍵旅程用 Playwright。把 `RETHINK_100_IMPROVEMENTS.md` 當作 UI 強化待辦。

**測試：** gateway 契約測試（REST + WS payload 與 `packages/contracts` 一致）；Playwright E2E：自 Brief Studio 啟動 Workflow A → 即時看 DAG 節點轉換 → 核可一個閘 → 在 Gallery 看到產物 → 觸發交付。WebSocket 重連恢復狀態。RBAC 拒絕未授權的閘核可。

**驗收閘門 G-M10：** 人類可完全透過瀏覽器為 Workflow A 啟動、即時監看、評論、核可閘並下載交付物，具 <50ms 級即時更新，且無代理→UI 直接呼叫。✅

---

### M11 — Enhancement 層

**目標：** 個人化與音訊優先變體。規範：[`psychological_profile_agent_functional_specifications.md`](./psychological_profile_agent_functional_specifications.md)、[`psychological_recommendation_agent_functional_specification.md`](./psychological_recommendation_agent_functional_specification.md)、[`podcast_agent_functional_specifcation.md`](./podcast_agent_functional_specifcation.md)。

**相依：** M7–M9。

**建構：**
- **心理剖析**（100 個創作者設定檔：MBTI、動機、恐懼、創意參數）→ 餵 Casting/Talent/Personalization/UGC 代理，以及 Aesthetics Agent 的 *受眾族群設定檔*。
- **心理推薦**（Big Five / 情緒狀態偏好預測）→ AudienceSim、PerformanceMarketer、Personalization。
- **PersonalizationEngineerAgent** 模板（name/face/voice swap）含隱私/同意審計（GDPR/CCPA 經 ComplianceAgent）。
- **Podcast Agent** 音訊優先工作流（preparation → execution → ending → follow-up），重用 VO/SoundMixer/Editor。

**測試：** 設定檔條件化生成可量測且可追溯地改變輸出；個人化 render 成功率 ≥99.5%（批次 fixture）；同意審計封鎖未同意肖像；podcast 工作流在 mock 上端到端執行。

**驗收閘門 G-M11：** 個人化 + 受眾族群條件化變體在同意閘下生成；podcast 原型端到端執行。✅

---

### M12 — 強化、規模、安全與發佈（100 點遍）

**目標：** 把一切帶到生產級。此里程碑 *即是* §14 的 100 點清單，逐主題執行。

**相依：** M0–M11。

**建構/執行：**
- **規模：** 對 orchestrator 做負載測試（並行生產）、GPU 自動擴展調校、若 Redis Streams 成瓶頸則遷移 NATS、熱/溫/封存儲存分層、LatencyOptimizer 遍（快取、批次、推測解碼）。
- **安全：** 密鑰管理強化、RBAC 審查、相依 CVE 掃描、SBOM、對每個攝入外部內容的代理做 prompt-injection 防禦、SafetyRedTeam 全面掃描。
- **可靠性：** 混沌測試（砍 worker、斷 Redis、讓供應商失敗）→ 優雅降級；Postgres + 資產儲存的備份/還原；DR runbook。
- **合規：** 100% 可發佈產物 C2PA；FTC/HIPAA/GDPR/IP 清單接入 ComplianceAgent 封鎖閘；審計軌跡完整性。
- **成本：** 在現實負載下驗證成本儀表板 + 預算警示；CostOptimizer Pareto 前沿檢查。
- **文件：** 操作 runbook、on-call 劇本、重生架構圖、`CLAUDE.md` 最新。
- **發佈：** 分階段推出（內部 → 受限 → GA）含 feature flag；對真實供應商於預算上限後做 live-smoke。

**Claude Code 工作流：** 對 §14 的 10 主題各跑 `/harden <theme>`；修每個發現；唯有全部 100 格勾選，系統才算「完成」。混沌/安全分析用 extended thinking。

**驗收閘門 G-M12（最終）：** 全部 100 強化檢查通過；一次完整的 **Workflow J（Feature Film）** 演練動用全部 114 代理，在 mock 上以完整 QC/provenance/可觀測性完成；對真實供應商的 live-smoke 於預算內成功；DR runbook 已驗證。✅ **出貨。**

---

### 6.1 垂直切片優先策略（為何 M6 落在此處）

在端到端證明一條工作流之前就建 114 個代理，將是經典的分散式系統錯誤：在 80% 程式碼已假設某架構之後，才發現該架構有瑕疵。本計劃刻意：

1. 先建 **平台**（M0–M5）— 契約、編排、gateway、智慧。
2. 在真實基礎設施上（mock 生成供應商）打穿 **一條薄垂直切片**（M6，Workflow A）。選 Workflow A 因其代理最少、執行時間最短，是最便宜的完整證明。
3. 之後才經工廠擴展 **廣度**（M7–M9），此時架構已歷經實戰。
4. 再加 **表面**（M10 UI）與 **豐富化**（M11），再 **強化**（M12）。

若 M6 閘揭露架構問題（如交接契約缺一欄位，或 Temporal↔LangGraph 邊界錯誤），你在僅有 9 個代理在飛時於平台修它 — 而非 114 個。這是計劃中最重要的單一排序決策。

---

## 7. 可重複的模式：一個工作流原型 = 一個 DAG

[`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3 的 10 個原型 (A–J) 各成為 `workflows/` 中一個 LangGraph 圖。它們共用 §3.0 骨架（Greenlight → Pre-production → Production → Post → Review/Release → Distribution → Post-launch），只在各階段由哪些代理領銜、哪些評審閘控交接上不同。

**工作流建構順序：** A (M6) → C、E、B (M7) → F、G、H、I (M8) → D（M11，需個人化）→ J（M12，全系統演練）。一條工作流在其 DAG 於 mock 供應商端到端執行、每個階段閘強制其評審集、最終產物帶完整 provenance 鏈時，即「完成」。

---

## 8. 代理實作手冊（對 114 代理每一個執行）

這是 `/new-agent <n>` 指令自動化的確切、可重複配方。**沒有代理在此配方外手工建構**（G3）。

**輸入：** 代理編號及其在 [`agents.md`](./agents.md) + [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §2 的列（Responsibility、Knowledge Distillation Source、Self-Quality Criteria、Surpass-Human Signal、Accepts Critique From、Comments On）加任何深規範。

**步驟：**
1. **讀（子代理）。** `spec-reader` 把上述六欄擷取為結構化 `AgentBrief`。
2. **自我品質 → 指標。** 把「Self-Quality Criteria」轉成具門檻的具體 `MetricSpec`（如 DoP `rule_of_thirds>=τ, exposure_zone∈[III,VII], color_temp_var<=ΔK`；Colorist `deltaE<2`；SoundMixer `lufs==target, stoi>=0.85`）。許多對應到既有 `packages/qc` 驗證器或 Aesthetics Agent。
3. **撰寫 L2 rubric/憲法。** 把「Surpass-Human Signal」+ 工藝來源轉成 `eval/rubrics/<agent>.yaml` 中的角色憲法（這是 LLM-as-judge 評分的依據）。引用規範指名的工藝權威（Editor 的 Murch's Rule of Six、Animator 的 12 原則等）。
4. **定義工具。** 僅允許此代理可呼叫的供應商/工具（如 PromptEngineer → MediaGenProvider；Colorist → grade 工具；FactChecker → RAG + WebResearch）。由 `agent-core` 強制。
5. **接線評論邊。** 自 §4 評論矩陣：`critiques_from` 與 `critiques_on`。ComplianceAgent 邊永遠封鎖。
6. **撰寫 AgentConfig (YAML)** 並註冊進 `agents/_registry.yaml`。
7. **撰寫版本化 system prompt**（`agents/.../prompt.vN.md`），嵌入角色、憲法摘要、self-refine 指令與輸出 schema（必須發出有效 `Artifact`）。
8. **TDD（子代理 `test-author`）：** golden 輸入 fixture → 斷言 L1 schema 通過、L2 rubric ≥85、正確評論發/收、工具允許清單強制、計量存在、provenance 填妥。
9. **實作 = 實例化。** `AgentFactory.build(config)` — 無新程式碼路徑；若你發現自己在寫客製邏輯，那邏輯屬於 `agent-core` 或一個工具，而非代理。
10. **審查（子代理 `code-reviewer`）** 對照 DoD + §14 主題；修；提交 `feat(agent-<n>): <Name>`。
11. **註冊進使用它的工作流**；擴展相關原型整合測試。

**應拒絕的反模式：** 無 L2 rubric 的代理；直接呼叫供應商而非經工具介面的代理；竄改別代理產物而非發評論的代理；其「自我品質」是不可量測散文的代理。

---

## 9. 測試與評估策略

系統本身是個 *評估引擎*；它自己的測試套件必須堪為典範。五層：

### 9.1 Unit（每套件/代理）
純邏輯測試，全 mock、決定性、快（每套件 <5s）。含契約的屬性測試（hypothesis）（序列化來回、DAG 無環、計量數學）。

### 9.2 契約測試
對每個 `packages/contracts` 模型的 JSON schema 做快照。移除/改名欄位的變更 **使 CI 失敗**，除非有版本升版 + ADR + `contract-guardian` 簽核（G1）。生成 TS 型別必須同步（`contracts:gen` diff 檢查）。

### 9.3 Integration（真實後端服務、mock 生成供應商）
對 `docker compose`（Postgres/Redis/Temporal/OpenSearch/Chroma/MinIO）執行。涵蓋：DAG 執行、砍-恢復持久性、事件 replay、閘 interrupt、跨階段交接契約傳播、評論匯流排路由、預算強制。

### 9.4 行為/golden-set 評估（對系統自身套用 L1/L2/L3 網）
- `eval/golden/` 的 **golden set**：每代理與每工作流的凍結 brief→expected fixture。輸入與期望結構化輸出皆受版本控管。
- **L2 評審凍結 + 釘住**（特定模型 + prompt 版本），使分數跨執行穩定；切勿讓評審模型漂移（回歸噪音殺手）。
- **L3 AudienceSim**：≥200 模擬 personas（來自心理剖析，M11）+ ≥20 HiTL 樣本；報告對儲存人類/基準參考的 win-rate。
- **`EvaluationHarnessAgent` (#79)** 每夜及每個觸及代理的 PR 執行這些；把回歸貼到 `system.alerts`。

### 9.5 對抗/安全（`SafetyRedTeamAgent` #80）
持續攻擊：深偽/肖像濫用、經攝入 web 內容的 prompt injection、越獄、誹謗、偏誤。目標 attack-success ≤1%。每夜 + 發佈前執行。

### 9.6 E2E（UI）
Playwright 旅程（M10）：launch → 即時監看 → critique → gate-approve → deliver，加 WebSocket 重連與 RBAC。

> **CI 測試金字塔：** PR 跑 unit + 契約 + 受影響代理的 golden L1/L2 + lint/type（數分鐘）。每夜跑完整 integration + L3 + red-team + benchmark harness + live-smoke（預算上限）。

---

## 10. 可觀測性、成本、安全與合規閘

### 10.1 可觀測性（自 M2，於 M8/M12 深化）
- **Tracing：** 每次代理執行、工具呼叫、LLM 呼叫與閘決策都是一個 OTel span；LangSmith 捕捉代理推理 trace。一個生產從 brief 到交付有一棵 trace 樹。
- **Metrics → Grafana：** DAG 完成率、節點延遲 p50/p95、retry/死鎖計數、佇列深度、GPU 利用率、每代理 L2 分數趨勢、escaped-defect 率。
- **Replay：** 事件溯源匯流排 + Temporal 歷史 → 重建任何生產的完整決策路徑供除錯/審計（「可觀測性與 Replay」層）。
- **結構化日誌：** JSON，依 `production_id` + `artifact_id` + `trace_id` 關聯。

### 10.2 成本（自 M3）
- 每次呼叫計量 → `budget_update` 事件 → 每生產/代理/供應商的成本儀表板。
- 每生產 **預算信封**；突破時硬停止 + ProducerAgent 升級（G6）。
- **CostOptimizerAgent** 使路由保持在成本/品質 Pareto 前沿。
- **Live-smoke 預算上限**：每夜真實供應商工作在固定金額上限中止。

### 10.3 安全與合規（ComplianceAgent 自 M6 起可 BLOCK）
- **ComplianceAgent (#37)** 是每條發佈路徑上的封鎖閘：FTC、HIPAA、GDPR/CCPA、IP/肖像清除、EU AI Act、AI 揭露。
- **同意鏈**：任何肖像/聲音複製需 `rights_and_consent` 中的已驗證同意紀錄；AvatarDesign/VoiceClone 代理無同意不得進行。
- **C2PA**：100% 可發佈產物簽署；下游驗證鏈。
- **Provenance/審計**：每個產物追溯回 brief + prompts + 模型版本 + 簽核。
- **內容安全**：對任何攝入外部/使用者內容的代理做 SafetyRedTeam + 輸入消毒。

### 10.4 不可妥協的發佈判定式
一個產物可發佈 **若且唯若**：`L1==pass AND L2>=85 AND L3>=threshold AND all(Q1..Q6) AND compliance==clear AND c2pa_signed AND budget_ok`。把它編碼為單一 `qc.release_ok(artifact)` 函式；GateKeeperAgent 只呼叫它。

---

## 11. CI/CD 與環境

### 11.1 環境
- **dev**（docker-compose、mock 供應商、direnv 本地密鑰）。
- **staging**（K8s、mock+受限真實供應商、合成負載）。
- **prod**（K8s、真實供應商、Vault 完整密鑰、GPU 池自動擴展）。

### 11.2 流水線（GitHub Actions）
- **PR 流水線：** `make verify`（lint+type+unit）→ contract-snapshot → 受影響代理 golden L1/L2 → build images。合併必需。
- **Main 流水線：** 完整 integration（compose 服務）→ 發佈 images → 部署 staging → smoke。
- **每夜：** 完整 L3 + red-team + benchmark harness + 相依 CVE 掃描 + live-smoke（預算上限）。
- **發佈：** tag → SBOM → 分階段推出（feature-flag）→ canary → GA。

### 11.3 慣例
- **Conventional Commits**，里程碑範圍化（`feat(m7-colorist): ...`、`fix(m2-orchestrator): ...`）。
- **Trunk-based**，短命分支；PR 小且里程碑標記。
- **不直接推 main**；每項變更經 PR，含綠燈檢查 + `code-reviewer` 通過。
- Claude Code 於 headless 模式（`claude -p`）僅可在沙盒化 runner 內跑受限 CI 修補。

---

## 12. 資料、模型與提示管理

- **Prompt 註冊表：** 每個代理 system prompt 版本化（`prompt.vN.md`）；作用版本由 `AgentConfig` 引用並記入 provenance（G5）。Prompt 變更經 PromptOptimizer (#73) 評估後方可晉升。
- **模型註冊表：** 每代理策略釘住模型+版本；升級受評估閘控（升級前後跑 golden L2/L3；不容回歸）。
- **Seed/LoRA/style 註冊表：** StyleTransfer (#61) 與生成代理引用版本化 seed/LoRA/參考畫格庫，以利重現與外觀一致。
- **Golden-set 治理：** golden fixture 凍結並審查；變更期望輸出需理由（可能暗示 rubric 漂移）。
- **美學設定檔：** 受同意治理、版本化的 `AestheticProfile`（依 Aesthetics Agent 規範）儲存並簽署；受眾族群設定檔連結至心理推薦。
- **評估資料集：** VBench/EvalCrafter/MT-Bench/FVD/CLIP-T runner 包在 `EvalToolProvider` 之後；基準基線由 BenchmarkResearch (#72) + EvaluationHarness (#79) 隨時間追蹤。

---

## 13. 風險登錄簿與緩解

| # | 風險 | 可能性 | 衝擊 | 緩解（計劃中位置） |
|---|------|--------|------|--------------------|
| R1 | 廣度代理建好後才發現架構瑕疵 | 中 | 高 | 廣度前先垂直切片 M6（G2、§6.1） |
| R2 | 114 代理間契約漂移 | 高 | 高 | 凍結契約 + `contract-guardian` + 快照測試（§5、§9.2） |
| R3 | 失控 LLM/生成成本 | 高 | 高 | 自 M3 計量+預算閘；CI 用 mock；live-smoke 上限（§10.2） |
| R4 | Temporal↔LangGraph 邊界混淆 | 中 | 高 | ADR-003 + M2 砍/恢復測試（§6 M2） |
| R5 | LLM 評審分數噪音動搖閘 | 高 | 中 | 凍結、釘住評審 + golden set（§9.4） |
| R6 | 美學獎勵導致獎勵駭客/「漂亮垃圾」 | 中 | 中 | Aesthetics Agent 防駭層；集成分歧；低信心 HiTL |
| R7 | 供應商斷線/限速使生產卡住 | 中 | 中 | 供應商抽象 + Router fallback + retry（§3.3、RouterAgent） |
| R8 | 生成肖像/聲音的同意/IP 違規 | 低 | 嚴重 | ComplianceAgent 封鎖閘 + 同意鏈 + C2PA（§10.3） |
| R9 | 情境臃腫導致建構期 Claude Code 回歸 | 高 | 中 | `/clear`+`/compact`+子代理+各套件 CLAUDE.md（§2.8） |
| R10 | 經攝入 web/research 內容的 prompt injection | 中 | 高 | 輸入消毒 + SafetyRedTeam + 最小工具權限（§10.3、§9.5） |
| R11 | Redis Streams 規模瓶頸 | 中 | 中 | 自 M2 設計好 NATS 遷移路徑（§3.2、M12） |
| R12 | 非決定性測試使 CI flaky | 中 | 中 | 決定性 mock + 釘住 seed/評審；隔離 flaky 測試（§9） |
| R13 | 範圍蔓延（角色膨脹：新增無實質缺口的代理） | 中 | 中 | 依 workflow doc 規則 §1.1 工作規則 #4 拒絕；114 之外任何代理需 ADR |


---

## 14. 100 點強化檢查清單（「重新思考 100 次」，操作化）

系統在全部 100 格勾選前 **不算完成**。組織為 **10 主題 × 10 檢查**。在 M12（以及任何表面改變的主題重跑時）用 `/harden <theme>` 跑每個主題。這是「重新思考 100 次」指令的字面、結構化形式。活狀態維護於 `BUILD_PROGRESS.md`。

### 主題 1 — 契約與 Schema 完整性 (1–10)
1. 每個代理間訊息都是型別化 `packages/contracts` 模型；匯流排上零臨時 dict。
2. 交接 `Artifact` 在每個階段邊界填妥（無空的必填欄位）。
3. 契約快照測試守護所有模型；移除/改名需版本升版 + ADR。
4. 生成 TS 型別與 Pydantic 同步（CI diff 檢查綠燈）。
5. `parent_assets` 永遠構成無環 provenance DAG。
6. CritiqueMessage severity 語意強制（blocker 暫停、major→3 迭代精煉、minor/nit→記憶）。
7. Event-bus payload 對照 `events.py` 驗證；無效事件被拒，非靜默丟棄。
8. 版本控管為 copy-on-write；任何地方都無就地產物竄改。
9. 可發佈產物的 `qc_status` 與 `provenance_manifest` 永不為 null。
10. 無套件本地重新定義共享契約（grep 可證單一來源）。

### 主題 2 — 編排與狀態 (11–20)
11. 砍-恢復：DAG 中途 worker 崩潰自 checkpoint 恢復，無遺失/重複工作。
12. fan-out/fan-in 正確性在並行下驗證。
13. 死鎖偵測器在循環/阻塞計劃上跳脫；無靜默掛起。
14. 每節點皆有 SLA 計時器 + timeout；卡住升級至 HiTL。
15. Temporal↔LangGraph 邊界已文件化 (ADR-003) 且程式碼遵循。
16. 閘 interrupt 確實阻塞直到外部 signal；無提前推進的 race。
17. 冪等鍵防止重試時重複執行。
18. 事件溯源可決定性 replay 一個完整生產。
19. 匯流排/佇列飽和時處理 backpressure。
20. 後端服務（Redis/Postgres/OpenSearch）短暫不可用時優雅降級。

### 主題 3 — 代理正確性 (21–30)
21. 全部 114 代理經工廠實例化（無客製迴圈）。
22. 每代理在其 golden 輸入通過 L1 schema 符合。
23. 每代理在其 L2 rubric（凍結評審）得分 ≥85。
24. 評論邊與 §4 矩陣完全相符（無缺/多餘邊）。
25. 工具允許清單強制；代理呼叫不允許工具會 fail closed。
26. Self-Refine 上限於 `max_refine_iters`；失控迴圈不可能。
27. Reflexion 記憶寫/讀已驗證；教訓跨重試持久。
28. 無代理竄改他人產物；改為發評論。
29. 每代理自我品質標準是 *可量測* 指標，非散文。
30. ComplianceAgent BLOCK 邊在每條發佈路徑驗證。

### 主題 4 — 品質網 (31–40)
31. `qc.release_ok()` 是單一發佈判定式；GateKeeper 只呼叫它。
32. L1 決定性驗證器涵蓋 codec/aspect/duration/frame-rate/LUFS/captions。
33. L2 評審釘住（模型+prompt 版本）；分數變異跨重跑在容差內。
34. L3 AudienceSim 用 ≥200 personas + ≥20 HiTL；win-rate 計算正確。
35. Q1–Q6 交付網各自實作並閘控。
36. 連續性 (Q4) 經 `identity_hash` 偵測身分/服裝/道具漂移。
37. 美學評分回傳分解向量 + `hack_likelihood`；低信心升級。
38. 防獎勵駭客防禦啟動（集成分歧、變異監控）。
39. 任何面向人類的輸出閘控可及性（WCAG 2.2 AA 最低）。
40. 種下的缺陷被可靠抓到並在發佈前封鎖。

### 主題 5 — 成本與效能 (41–50)
41. 每次 LLM/生成呼叫計量；成本在 fixture 上與供應商價目表相符。
42. 每生產預算信封強制，含硬停止 + 升級。
43. CostOptimizer 使路由保持在成本/品質 Pareto 前沿。
44. 回應/嵌入快取減少冗餘呼叫（cache-hit 測試）。
45. p95 節點延遲在標稱負載下達標。
46. GPU 池在排隊 render 負載下自動擴展；閒置時縮減。
47. 儲存分層（熱/溫/封存）已設定並測試。
48. 批次/互動工作負載分離；批次絕不餓死互動。
49. Live-smoke 真實供應商工作在其預算上限中止。
50. 負載測試：N 個並行生產在 SLA 內完成。

### 主題 6 — 安全、保安與合規 (51–60)
51. SafetyRedTeam attack-success 在攻擊分類學上 ≤1%。
52. 對每個攝入外部/使用者內容的代理做 prompt-injection 防禦。
53. 任何肖像/聲音生成前驗證同意鏈。
54. C2PA 簽署 100% 可發佈產物；下游驗證通過。
55. FTC/HIPAA/GDPR-CCPA/IP/EU-AI-Act 清單接入 ComplianceAgent。
56. 密鑰永不入 repo/日誌；secret-scan hook + CI 閘啟動。
57. RBAC 強制於所有 gateway 變更（閘核可、retry、config）。
58. 每次發佈產出相依 CVE 掃描 + SBOM；critical 封鎖。
59. 需要時套用 AI 揭露（avatar/合成內容）。
60. 樣本中 PII 用通用佔位符；真實 PII 僅在受同意專案資料中。

### 主題 7 — 可觀測性與可操作性 (61–70)
61. 每生產一棵 trace 樹（brief→delivery）於 LangSmith/Tempo。
62. Grafana 儀表板：完成率、延遲、retry、死鎖、佇列深度、GPU、L2 趨勢、escaped-defect 率。
63. 日誌為結構化 JSON，依 production/artifact/trace id 關聯。
64. 任何生產可自事件日誌 + Temporal 歷史完整 replay。
65. `system.alerts` 警示對回歸、預算突破、安全、SLA 觸發。
66. EvaluationHarness 回歸偵測延遲 <1h。
67. 前幾大失效模式有 runbook；on-call 劇本最新。
68. Postgres + 資產儲存的備份/還原已驗證。
69. DR 演練：全區失效在 RTO/RPO 目標內復原。
70. Feature flag 允許安全分階段推出 + 即時回滾。

### 主題 8 — 前端與人類體驗 (71–80)
71. UI 端到端啟動/監看/評論/核可/交付 Workflow A。
72. WebSocket 即時更新為 <50ms 級；DAG 節點狀態準確。
73. 無代理→UI 直接呼叫（全經 event bus + gateway）。
74. WebSocket 重連恢復完整狀態，無重複。
75. Gate Approval Dialog 核可時簽 C2PA；拒絕正確路由回饋。
76. 預算/品質儀表板即時反映後端真相。
77. Playwright E2E 涵蓋關鍵旅程；CI 綠燈。
78. RBAC 在 UI 與 gateway 拒絕未授權動作。
79. `RETHINK_100_IMPROVEMENTS.md` 項目已分流；critical 已處理。
80. 生產規模探索使 DAG 適應專案複雜度（S 層）。

### 主題 9 — 建構流程與 Claude Code 衛生 (81–90)
81. 根 + 各套件 `CLAUDE.md` 最新且精簡。
82. 子代理（`spec-reader`、`contract-guardian`、`test-author`、`test-runner`、`code-reviewer`、`agent-factory-smith`）已定義並使用。
83. 斜線指令（`/milestone`、`/new-agent`、`/verify`、`/contract-check`、`/gate`、`/adr`、`/harden`）已定義。
84. Hooks 強制自動格式化、受保護路徑封鎖、type/lint 閘、密鑰掃描。
85. `DECISIONS.md` 對每個非顯而易見選擇有 ADR（含 ADR-001/002/003）。
86. `BUILD_PROGRESS.md` 反映真實里程碑 + 強化狀態。
87. 每次提交為 Conventional + 里程碑範圍；無密鑰/除錯殘渣。
88. `make verify` 每次提交綠燈；CI 必需檢查強制。
89. 實踐情境衛生（任務間 `/clear`；無矛盾的陳舊情境）。
90. 遵循 TDD：測試先於實作（抽查 git 歷史）。

### 主題 10 — 端到端系統驗證 (91–100)
91. 全部 10 工作流原型 (A–J) 在 mock 供應商端到端執行。
92. Workflow J（Feature Film）演練成功動用全部 114 代理。
93. provenance 鏈可自任何最終產物驗證回 brief。
94. 多通路交付（theatrical/streaming/broadcast/archive + 行銷）全 Q6 有效。
95. Post-launch 遙測流入再訓練工單（RLAIF 迴圈閉合）。
96. Optimization Agent 可證地把一個工作流指標改善過基線。
97. GCA↔Aesthetics 生成↔評估迴圈產出可量測更佳的候選。
98. Research/FactChecker 路徑只產出來源分級、附引用的論點。
99. 真實供應商上的 live-smoke 在預算內完成並通過 QC。
100. 一位冷讀者（新工程師）能僅憑本計劃 + 規範建構，無需口耳相傳知識。

> **完成規則：** 「完成」= `BUILD_PROGRESS.md` 中 100/100 勾選，每項旁附證據（測試名稱、儀表板連結或 artifact id）。

---

## 15. 排序摘要與關鍵路徑

### 15.1 里程碑 → 驗收閘門 → 規範對應

| M | 里程碑 | 驗收閘門（一行） | 主要規範 |
|---|--------|------------------|----------|
| M0 | Bootstrap + Claude config | 乾淨 clone → `make verify` 綠燈；`.claude/` 上線 | SYSTEM_REFERENCE §11 |
| M1 | Agentic RAG | golden 語料庫 precision@5 ≥0.9；分級引用 | agentic_rag |
| M2 | 編排執行期 | 3 節點 DAG 在 worker 砍掉後存活；型別化事件；C2PA | workflow §1.2；ui/architecture |
| M3 | LLM gateway + Router + Cost | 每次呼叫計量/路由/版本標記；預算停止 | llm_usage；agents §9 |
| M4 | Research + Coding 工具組 | RAG 中有附引用 dossier；慣例被強制 | research_*；coding_agent |
| M5 | Intelligence 層 | 6 推理服務通過 golden 行為測試 | intent/gca/optimization/goal/cps/aesthetics |
| M6 | 工廠 + 垂直切片 A | `make e2e-workflow-a` 在 mock 上簽署交付物 | workflow §3.1 |
| M7 | 生產代理 1–52 | 全 52 在 L1+L2+評論綠燈；再 3 個工作流 E2E | agents §1–8 |
| M8 | Meta-agents 53–80 + QC | 全 80 上線；完整 L1/L2/L3+Q1–Q6；red-team+harness 每夜 | workflow §2.9、§5 |
| M9 | 支援 81–114 + 交付 | 4 交付分支 Q6 有效；學習迴圈閉合 | agents §10；workflow §3.0 |
| M10 | UI + gateway + WS | 人類在瀏覽器完整跑 Workflow A，即時 | 全 ui/ |
| M11 | Enhancement | 個人化/族群變體在同意下；podcast E2E | psych_*；podcast |
| M12 | 強化 + 發佈 | 100/100 檢查；Workflow J 全-114 演練；live-smoke | §14 |

### 15.2 關鍵路徑
`M0 → M2 → M3 → M5 → M6 → M7 → M8 → M9 → M12`。M1 餵 M2/M4；M4 支援 M8；**M10 可自 M3 起於 worktree 並行**；M11 排在 M9 後。最高槓桿的單一檢查點是 **G-M6**（垂直切片）— 它把架構風險轉化為已驗證的基礎。

### 15.3 此處「全力」的意義
起初深度勝於廣度（平台 + 契約 + 一條完美切片），再經工廠做機械式廣度，再遞迴品質（系統把影片評到 L1/L2/L3 — 故它必須把 *自己* 評到 L1/L2/L3），再做字面的 100 點強化掃描。本計劃經設計，使瑕疵恰在最可能被發現之時最便宜修復。

---

## 16. 附錄（給 Claude Code 的可複製貼上起手物）

### Appendix A — 根 `CLAUDE.md` 範本

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

### Appendix B — 子代理定義 (`.claude/agents/*.md`)

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

> 同理建立 `test-author`、`test-runner` 與 `agent-factory-smith`（受限工具、單一職責）。

### Appendix C — 斜線指令定義 (`.claude/commands/*.md`)

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

> 另：`/verify`（跑 `make verify`、摘要失敗）、`/contract-check`（對暫存 diff 呼叫 contract-guardian）、`/gate <Q1..Q6|L1..L3>`（跑一個 QC 層 + 報告）、`/adr <title>`（追加註明日期的 ADR）。

### Appendix D — `.claude/settings.json`（權限 + hooks）

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

> `protect_contracts.sh` 在目標位於 `packages/contracts/**` 且該 session 缺少明確「contract change」+ ADR 標記時，以非零退出（封鎖該編輯）— 機械式執行 G1。

### Appendix E — 完成定義（釘在每個 PR 範本）

- [ ] 測試先於程式碼；全綠；`make verify` 通過。
- [ ] 契約未變，或經 ADR + contract-guardian PASS 後變更。
- [ ] code-reviewer：無 blocker/major 發現。
- [ ] 里程碑驗收閘門標準達成（證據在 `BUILD_PROGRESS.md`）。
- [ ] Conventional、里程碑範圍提交；無密鑰/殘渣/未追蹤 TODO。
- [ ] 若公開表面改變，更新套件 `CLAUDE.md`/README。
- [ ] 若表面改變，重新驗證相關 §14 強化檢查。

### Appendix F — 詞彙表

| 術語 | 意義 |
|------|------|
| **Handoff Contract** | 在階段間攜帶的 `Artifact` manifest（§5.1）。 |
| **CritiqueMessage** | 型別化代理間回饋（§5.2）。 |
| **L1/L2/L3** | Spec / Rubric / Preference 品質層（§5.5）。 |
| **Q1–Q6** | 六遍交付 QC 網（§5.5）。 |
| **垂直切片** | 廣度之前先端到端建好一條工作流（M6、G2）。 |
| **工廠 (Factory)** | 把 `AgentConfig` 變成可執行 `BaseAgent`（§8）。 |
| **凍結評審 (Frozen judge)** | 釘住模型+prompt 的 LLM 評估器，以穩定分數（§9.4）。 |
| **發佈判定式** | `qc.release_ok()` — 可發佈性的單一閘（§10.4）。 |
| **GCA / SSOR** | General Creative Agent / Strategic Sparse Outlier Recombination。 |
| **DIA** | Deep Intent Analysis（brief→結構化意圖）。 |
| **C2PA** | 套用於每個產物的 provenance 簽署標準。 |

---

## 17. 結語

本計劃環繞一個信念：**在廣度之前建好平台與一條完美切片，再讓工廠與遞迴品質網去做規模化。** 契約先凍結，使 114 代理無法分歧。垂直切片 (M6) 把系統最大的風險 — 太晚才發現架構瑕疵 — 轉化為便宜、早期、可證的檢查點。品質是遞迴的：把影片評到 L1/L2/L3 的系統，自己也必須通過 L1/L2/L3。而「重新思考 100 次」的指令不是修辭 — 它就是 §14 中那道字面 100 點閘門，橫亙在「在我機器上能跑」與「生產」之間。

Claude Code：自 **M0** 起步，跑 `/milestone M0`，在其驗收閘門綠燈並記錄前，不要推進任何里程碑。把它建成它本來的樣子 — 經規劃、經測試、經觀測、經簽署。

**建構計劃結束。**
*存為 `study/system_build_plan_hk.md`。`SYSTEM_REFERENCE.md` 的同伴。自 M0 起步。*
