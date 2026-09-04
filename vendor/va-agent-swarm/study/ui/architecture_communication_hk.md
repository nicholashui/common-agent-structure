# UI ↔ 代理人通訊架構

> 前端如何同後端溝通，以及後端如何協調編排 114 個代理人。

---

## 概覽：三層架構

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   TIER 1：UI 前端（Browser）                                                 │
│   React 19 + Next.js 15                                                     │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  使用者操作（點擊、輸入、審批、上載）                                 │    │
│   │  即時狀態訂閱（代理人狀態、critiques、artifacts）                     │    │
│   └──────────┬─────────────────────────────────┬───────────────────────┘    │
│              │ REST / GraphQL                    │ WebSocket                  │
│              │（指令 commands）                   │（即時 streams）            │
│              ▼                                   ▼                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TIER 2：API Gateway + 協調編排後端                                         │
│   Node.js / Python（FastAPI）+ LangGraph + Temporal                          │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Production Manager Service（CRUD、auth、permissions）              │    │
│   │  Orchestration Engine（LangGraph DAG 執行）                          │    │
│   │  Event Bus（Redis Streams / NATS）                                   │    │
│   │  Asset Store（S3 + metadata DB）                                      │    │
│   │  WebSocket Gateway（推送即時狀態到前端）                              │    │
│   └──────────┬─────────────────────────────────┬───────────────────────┘    │
│              │ Agent Task Queue                  │ Tool API Calls             │
│              │（派發 tasks）                      │（Sora、Veo、ElevenLabs...） │
│              ▼                                   ▼                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TIER 3：代理人 Runtime（LLM Workers）                                      │
│   LangGraph Nodes / CrewAI Agents / AutoGen Actors                          │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  114 個代理人定義（system prompts、tools、rubrics）                 │    │
│   │  LLM providers（Gemini 2.5 Pro、GPT-4o、Claude 4）                  │    │
│   │  生成工具（Sora 2、Veo 3.1、Runway、Kling、ElevenLabs）             │    │
│   │  評估工具（VBench、CLIP-T、ArcFace、響度量度）                      │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 詳細通訊流程

### 1. 使用者啟動 Production（Brief → Agents）

```text
使用者（Browser）
    │
    │  1. 填寫 Brief Studio 表單
    │  2. 按 [▶ LAUNCH PRODUCTION]
    │
    ▼
前端（React）
    │
    │  POST /api/productions
    │  Body：{ template: "E", title: "Luna", vision: "...",
    │          genre: "sci-fi", duration: 600, budget: 100, ... }
    │
    ▼
API Gateway（Backend）
    │
    │  3. 在 DB 建立 Production 記錄
    │  4. 入佇列「start_production」job
    │
    ▼
Orchestration Engine（LangGraph）
    │
    │  5. PlannerAgent 收到 brief
    │     - LLM 呼叫（Gemini 2.5 Pro）：拆解 brief → 分段 DAG
    │     - 回傳：task 清單、agent 指派、gate criteria
    │
    │  6. OrchestratorAgent 初始化 DAG 執行
    │     - 在 LangGraph 建立狀態機
    │     - 註冊所有 agent nodes
    │
    │  7. RouterAgent 為每個 task 指派 model + provider
    │     - 檢查 config 內的成本／品質規則
    │
    ▼
Agent Workers（並行）
    │
    │  8. DirectorAgent 收到「generate shot intent」任務
    │     - LLM 呼叫：Gemini 2.5 Pro（創意推理）
    │     - Tool call：Veo 3.1 API（影片生成）
    │     - Self-Refine：用 CLIP-T 評分，低於 threshold 就迭代
    │
    │  9. 每步完成後：
    │     - Agent → 發佈 event 到 Event Bus
    │     - Event Bus → WebSocket Gateway → 前端（即時更新）
    │
    ▼
前端收到 WebSocket events
    │
    │  10. DAG Canvas 節點轉換：○ → ● → ✓
    │  11. Artifact 出現在 Gallery
    │  12. Critique 訊息出現在 Feed
    │  13. 狀態列更新（運行中代理人、已花預算）
```

---

### 2. 即時狀態更新（Agents → UI）

```text
Agent（例如 DirectorAgent）
    │
    │  工作期間會發佈 events：
    │  • { type: "agent_state_change", agent: 1, state: "running", task: "shot_5" }
    │  • { type: "tool_call_start", agent: 1, tool: "veo_3.1", params: {...} }
    │  • { type: "artifact_created", id: "art_042", type: "video", version: 1 }
    │  • { type: "critique_sent", from: 1, to: 9, content: "..." }
    │  • { type: "metric_update", agent: 1, metric: "clip_t", value: 0.34 }
    │
    ▼
Event Bus（Redis Streams / NATS）
    │
    │  持久化 events 供回放 + 轉發給訂閱者
    │
    ▼
WebSocket Gateway
    │
    │  按 production_id 過濾 events
    │  推送到已連線的前端 clients
    │
    ▼
前端（React + Zustand）
    │
    │  更新本地 state store
    │  React components 重新 render：
    │  • DAG 節點顏色／符號變化（藍色跳動）
    │  • Gallery 出現新 artifact 卡片
    │  • Critique Feed 插入新訊息、badge 增加
    │  • 狀態列 counter 更新
    │  • Budget gauge 動畫更新
```

---

### 3. Human-in-the-Loop（UI → Agent）

```text
使用者見到 Gate Approval Dialog
    │
    │  檢視 criteria checklist + artifacts
    │  按 [✓ APPROVE] 或 [↩ REQUEST CHANGES]
    │
    ▼
前端
    │
    │  POST /api/productions/{id}/gates/{gate_id}/decision
    │  Body：{ decision: "approve", comment: "...", c2pa_sign: true }
    │
    ▼
API Gateway
    │
    │  驗證使用者權限
    │  簽署 C2PA provenance manifest
    │  發佈「gate_decision」event 到 Event Bus
    │
    ▼
Orchestration Engine（LangGraph）
    │
    │  GateKeeperAgent 收到 decision
    │  若批准：推進 DAG 到下一 phase
    │  若拒絕：把回饋路由到相關 agents 做 revision
    │
    ▼
下一階段 agents 啟動
    │
    │  （循環繼續）
```

---

### 4. 使用者向代理人發送 Critique

```text
使用者在 Critique Feed 輸入：
    "@DirectorAgent Use wider lens for Scene 3, it feels too claustrophobic"
    │
    ▼
前端
    │
    │  POST /api/productions/{id}/critiques
    │  Body：{ to_agent: 1, content: "Use wider lens...", priority: "normal" }
    │
    ▼
API Gateway
    │
    │  建立 CritiqueMessage 記錄
    │  發佈到 Event Bus（帶目標 agent）
    │
    ▼
Orchestration Engine
    │
    │  把 critique 派到 DirectorAgent 的 input queue
    │  DirectorAgent 在下一輪迭代處理：
    │    - 透過 MemoryAgent 讀取 critique
    │    - 調整 shot intent 參數
    │    - 用更新後 prompt 再生成
    │    - 發佈回應 critique
    │
    ▼
Event Bus → WebSocket → 前端
    │
    │  Critique Feed 出現 agent 回覆
    │  Gallery 出現更新後 artifact
```

---

## API 合約總覽

### REST Endpoints（Commands — 使用者主動觸發）

| Method | Endpoint | 目的 | 由誰呼叫 |
|--------|----------|---------|-----------|
| POST | `/api/productions` | 由 brief 建立 + 啟動 production | Brief Studio |
| GET | `/api/productions` | 列出所有 productions | Dashboard |
| GET | `/api/productions/{id}` | 取得 production 狀態 | Production Console |
| POST | `/api/productions/{id}/gates/{gid}/decision` | 批准／拒絕 gate | Gate Dialog |
| POST | `/api/productions/{id}/critiques` | 發送人類 critique | Critique Feed |
| POST | `/api/productions/{id}/agents/{aid}/retry` | 重試失敗 agent | Agent Inspector |
| POST | `/api/productions/{id}/agents/{aid}/skip` | 跳過 agent 任務 | Agent Inspector |
| PUT | `/api/settings/router-config` | 更新模型路由規則 | Router Config |
| GET | `/api/agents` | 列出 114 個 agent 定義 | Agent Registry |
| GET | `/api/productions/{id}/artifacts` | 列出 artifacts | Artifact Gallery |
| GET | `/api/productions/{id}/artifacts/{aid}` | 取得 artifact + 溯源 | Artifact Viewer |
| POST | `/api/productions/{id}/delivery/package` | 觸發交付封裝 | Delivery Hub |

### WebSocket Events（Streams — 系統推送到 UI）

| Event Type | Payload | 更新哪裡 |
|-----------|---------|---------|
| `agent_state_change` | `{ agent_id, state, task, progress }` | DAG Canvas 節點 |
| `artifact_created` | `{ artifact_id, type, version, producer, thumbnail_url }` | Gallery |
| `artifact_updated` | `{ artifact_id, version, quality_scores }` | Gallery + Quality |
| `critique_message` | `{ from, to, content, severity, attachments }` | Critique Feed |
| `gate_ready` | `{ gate_id, criteria, judge_score, artifacts }` | Gate Dialog + Notification |
| `gate_resolved` | `{ gate_id, decision, next_phase }` | DAG Canvas + Timeline |
| `budget_update` | `{ spent, remaining, per_agent_breakdown }` | Budget Tracker + Status Bar |
| `metric_update` | `{ agent_id, metric_name, value, threshold, pass }` | Quality Dashboard |
| `memory_entry` | `{ entry_id, content, accessed_by }` | Memory Panel |
| `tool_call` | `{ agent_id, tool, params, status, duration }` | Agent Inspector |
| `production_phase_change` | `{ production_id, new_phase }` | Context Bar + Timeline |
| `error` | `{ agent_id, error_type, message, recoverable }` | Notification + DAG（紅色節點） |

---

## 後端架構細節

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                          API GATEWAY LAYER                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │
│  │  Auth / RBAC │  │  Rate Limit  │  │  Validation  │                  │
│  └──────────────┘  └──────────────┘  └──────────────┘                  │
├─────────────────────────────────────────────────────────────────────────┤
│                          SERVICE LAYER                                   │
│                                                                         │
│  ┌──────────────────┐     ┌──────────────────┐                          │
│  │ Production       │     │ WebSocket        │                          │
│  │ Manager Service  │     │ Gateway Service  │                          │
│  │                  │     │                  │                          │
│  │ • CRUD           │     │ • Client mgmt    │                          │
│  │ • Brief parsing  │     │ • Event routing  │                          │
│  │ • Permissions    │     │ • Filtering      │                          │
│  └────────┬─────────┘     └────────┬─────────┘                          │
│           │                         │                                    │
│           ▼                         ▼                                    │
│  ┌──────────────────────────────────────────────┐                       │
│  │                 EVENT BUS                      │                       │
│  │            （Redis Streams / NATS）             │                       │
│  │                                              │                       │
│  │  Topics：                                     │                       │
│  │  • production.{id}.agent_events               │                       │
│  │  • production.{id}.critiques                 │                       │
│  │  • production.{id}.gates                     │                       │
│  │  • production.{id}.artifacts                 │                       │
│  │  • system.alerts                             │                       │
│  └──────────────────────┬───────────────────────┘                       │
│                         │                                               │
│                         ▼                                               │
│  ┌──────────────────────────────────────────────┐                       │
│  │            ORCHESTRATION ENGINE              │                       │
│  │              （LangGraph + Temporal）         │                       │
│  │                                              │                       │
│  │  ┌────────────┐  ┌────────────┐              │                       │
│  │  │ DAG State  │  │ Task Queue │              │                       │
│  │  │ Machine    │  │（per agent）│              │                       │
│  │  └────────────┘  └────────────┘              │                       │
│  │                                              │                       │
│  │  ┌────────────┐  ┌────────────┐              │                       │
│  │  │ Retry /    │  │ Gate       │              │                       │
│  │  │ Timeout    │  │ Evaluator  │              │                       │
│  │  └────────────┘  └────────────┘              │                       │
│  └──────────────────────┬───────────────────────┘                       │
│                         │                                               │
│                         ▼                                               │
│  ┌──────────────────────────────────────────────┐                       │
│  │               AGENT WORKER POOL               │                       │
│  │                                              │                       │
│  │  每個 agent worker：                          │                       │
│  │  1. 從 queue 取走 task                        │                       │
│  │  2. 載入 agent config（prompt、tools、rubric） │                       │
│  │  3. 呼叫 LLM（推理任務）                       │                       │
│  │  4. 呼叫 tools（生成影片、評估）               │                       │
│  │  5. 低於 threshold 就 self-refine              │                       │
│  │  6. 發佈結果 + events 到 Event Bus             │                       │
│  │                                              │                       │
│  │  擴展：水平擴展 worker pool                     │                       │
│  │  生成任務用 GPU workers                         │                       │
│  │  LLM-only 任務用 CPU workers                    │                       │
│  └──────────────────────────────────────────────┘                       │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                            DATA LAYER                                   │
│                                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │PostgreSQL│  │ S3/R2    │  │ Pinecone │  │ Redis    │               │
│  │          │  │          │  │ /Weaviate│  │          │               │
│  │Production│  │ Artifacts│  │ Memory   │  │ Cache +  │               │
│  │metadata  │  │（video,  │  │（vector  │  │ Sessions │               │
│  │Gate state│  │  audio,  │  │  DB for  │  │ Event    │               │
│  │Critiques │  │  images）│  │  Memory  │  │ Streams  │               │
│  │Configs   │  │          │  │  Agent） │  │          │               │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 主要設計決策

### 點解 agent→UI 用 WebSocket（唔用 polling）？

- 114 個代理人於活躍 production 期間，每 1–5 秒就可能產生 events
- polling 會導致每秒 10+ requests → 成本高、延遲大
- WebSocket 可即時更新（< 50ms latency）呈現 DAG 狀態變化
- 每個 production 一條連線，server 會按相關性過濾 events

### 點解後端服務之間用 Event Bus（唔直接互 call）？

- agents 係非同步、並行工作 — request/response 模式唔合適
- event sourcing 令任何 production 決策都可完整回放
- 解耦 agent 執行與 UI 推送
- 多個 consumer 可同時訂閱（UI、analytics、compliance logger、alerting）

### 點解用 LangGraph 協調（唔寫自訂 orchestration code）？

- DAG + 條件邊能直接映射 Composition Diagram
- 內建長流程 state 管理
- human-in-the-loop gates 係 LangGraph 一級概念
- checkpointing：後端重啟後可繼續

### 點解用 Temporal 做持久性？

- Productions 可能由幾分鐘（Viral Hook）到幾小時（Feature Film）
- 需要保證交付：workers crash 都唔會遺失 tasks
- 內建 retry + backoff
- 有 workflow history 方便除錯與審計

---

## Sequence Diagram：完整請求生命週期

```text
User          Frontend       API Gateway    Event Bus    Orchestrator    Agent Worker    LLM/Tool
 │               │               │              │             │               │             │
 │─click node──►│               │              │             │               │             │
 │               │─GET /agent───►│              │             │               │             │
 │               │◄──agent data──│              │             │               │             │
 │◄──render─────│               │              │             │               │             │
 │               │               │              │             │               │             │
 │─approve gate─►│              │              │             │               │             │
 │               │─POST /gate───►│              │             │               │             │
 │               │               │─publish──────►│            │               │             │
 │               │               │              │─gate_ok────►│               │             │
 │               │               │              │             │─dispatch──────►│             │
 │               │               │              │             │               │─LLM call───►│
 │               │               │              │             │               │◄──response──│
 │               │               │              │             │               │─tool call──►│
 │               │               │              │             │               │◄──video─────│
 │               │               │              │             │               │             │
 │               │               │              │◄─artifact_created───────────│             │
 │               │               │              │◄─state_change───────────────│             │
 │               │◄─────ws push──│◄─subscribe───│             │               │             │
 │◄──re-render──│               │              │             │               │             │
```

---

## 總結：回答「UI 點樣同 agents 傾計？」

```text
係 —— 你個直覺完全啱：

   UI 前端  ──（REST/WebSocket）──►  後端  ──（Task Queue）──►  Agents

具體而言：

1. COMMANDS 流向：UI → REST API → 後端 → Task Queue → Agent
   （使用者操作：launch、approve、critique、retry、configure）

2. EVENTS 流向：Agent → Event Bus → WebSocket Gateway → UI
   （即時更新：狀態變化、artifacts、critiques、metrics）

3. 後端唔係簡單 pass-through。它提供：
   • Orchestration（DAG 執行、排程、重試）
   • State 管理（啟動哪些 agents、處於哪個 phase）
   • 資產管理（儲存 artifacts、追蹤版本）
   • Gate 邏輯（評估 criteria、收集審批）
   • 安全（auth、permissions、C2PA 簽署）
   • 可觀測性（logging、metrics、replay）

4. Agents 永遠唔會直接同 UI 對話。
   它們只會發佈 events 到 Event Bus，再由 WebSocket Gateway
   把相關 events 派到正確的前端 client。
```

---

## 技術對應表

| 角色 | 技術 | 原因 |
|------|-----------|-----|
| 前端框架 | React 19 + Next.js 15 | Dashboard 用 SSR，Console 用 client-side 即時互動 |
| 狀態管理 | Zustand + React Query | 輕量；WebSocket 同步即時 DAG state |
| WebSocket client | Socket.io-client | 自動重連、room-based filtering |
| API Gateway | FastAPI（Python）或 Express（Node.js） | 快、typed、middleware 生態 |
| 協調引擎 | LangGraph（Python） | DAG 執行 + state + HiTL gates |
| 工作流持久性 | Temporal | 長流程可靠保證 |
| Event Bus | Redis Streams 或 NATS JetStream | Pub/sub + 持久化 + 可回放 |
| 代理人 runtime | LangGraph nodes / CrewAI agents | 可 tool-calling 的 LLM agents |
| LLM providers | Gemini 2.5 Pro、GPT-4o、Claude 4 | 經 litellm 統一介面 |
| 生成工具 | Veo 3.1、Sora 2、Runway、Kling、ElevenLabs | 由 agent workers 直接呼叫 API |
| 資料庫 | PostgreSQL + Drizzle ORM | production state、configs、audit log |
| 物件儲存 | S3 / Cloudflare R2 | 影片、音訊、圖片 artifacts |
| Vector DB | Pinecone / Weaviate | MemoryAgent 語意檢索 |
| Cache | Redis | session state、rate limiting、hot data |
| Observability | LangSmith + Grafana | agent tracing、效能儀表板 |
