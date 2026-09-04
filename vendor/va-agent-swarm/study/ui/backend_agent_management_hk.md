# 後端 → 代理人管理：後端如何控制 114 個代理人

> 深入解析協調編排（orchestration）後端如何管理、派發、監控、重試，以及如何讓 AI 代理人工作者彼此溝通。

---

## 核心問題

```text
問：後端有 114 個代理人「定義」—— 但它到底如何
    建立、執行、溝通與控制它們？

答：每個代理人都「不是」一個獨立伺服器或 microservice。
    代理人是一份「設定」（system prompt + tools + rubric），
    當有任務時由某個 worker process 去「執行」。

    可以咁理解：
    - 後端係樂團指揮（CONDUCTOR）
    - 代理人係樂譜（SHEET MUSIC：指令）
    - Workers 係樂手（MUSICIANS：執行）
    - LLM 係樂器（INSTRUMENT：能力）
```

---

## 1. Runtime 角度：代理人到底「是甚麼」？

代理人 **不是** 一個長駐程序。它更像一個 **無狀態函式**，每次被呼叫時會帶入：

```python
# Pseudocode — what an "agent" actually is in LangGraph

class AgentDefinition:
    agent_id: int                    # 1-114
    name: str                        # "DirectorAgent"
    system_prompt: str               # "You are a film director who..."
    tools: list[Tool]                # [sora_api, veo_api, memory_recall]
    architecture_pattern: str        # "self_refine" | "reflexion" | "react" | ...
    quality_rubric: dict             # { "clip_t": { "threshold": 0.32 } }
    accepts_critique_from: list[int] # [3, 9, 82]  (agent IDs)
    comments_on: list[int]           # [9, 6, 3, 20]
    max_iterations: int              # 5 (for self-refine loop)
    model_preference: str            # "gemini-2.5-pro"
```

當後端需要 DirectorAgent 為 Shot #5 產生 shot intent 時，會做：

1. 載入這份定義
2. 組裝 LLM prompt（system prompt + 任務上下文 + critique 歷史）
3. 呼叫 LLM
4. LLM 決定要呼叫哪些 tools
5. 後端代替代理人執行 tool calls
6. 若架構模式需要 self-refine，則迴圈執行
7. 發佈結果 + events

---

## 2. 協調引擎（大腦）

```text
┌─────────────────────────────────────────────────────────────────────┐
│                       協調引擎（ORCHESTRATION ENGINE）                │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                        DAG 狀態機                            │    │
│  │                     （LangGraph Graph）                      │    │
│  │                                                             │    │
│  │  Nodes： [Brief] → [Plan] → [Route] → [Craft×N] → [Gate]     │    │
│  │  Edges： 條件式（例如 gate 通過 → 進入下一階段）               │    │
│  │  State： { phase, active_agents, pending_tasks, budget }     │    │
│  │  Checkpoint：每次 node 執行後都會持久化                        │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌───────────────────┐  ┌───────────────────┐                      │
│  │    任務派發器      │  │     任務佇列       │                      │
│  │  （TASK DISPATCHER）│  │    （TASK QUEUE） │                      │
│  │                   │  │                   │                      │
│  │  決定：            │  │  每個代理人一條佇列：│                     │
│  │  • 用邊個 agent    │  │  • agent_1: [t5]  │                      │
│  │  • 做乜 task        │  │  • agent_6: [t3]  │                      │
│  │  • 用邊個 model     │  │  • agent_9: []    │                      │
│  │  • 幾時 run         │  │  • agent_46: [t7] │                      │
│  │  • 優先次序         │  │  • ...            │                      │
│  └───────────────────┘  └───────────────────┘                      │
│                                                                     │
│  ┌───────────────────┐  ┌───────────────────┐                      │
│  │   Critique Router  │  │   Gate Evaluator  │                      │
│  │                   │  │                   │                      │
│  │  根據「accepts」   │  │  檢查 criteria     │                      │
│  │  關係路由 critique  │  │  觸發審批           │                      │
│  │  訊息（代理人互評） │  │  人類批准後推進 phase│                     │
│  └───────────────────┘  └───────────────────┘                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. 後端如何把任務派發給代理人

以下係 OrchestratorAgent 決定「DirectorAgent 應該處理 Shot #5」時會發生的事：

```text
Step 1：建立任務（TASK CREATION）
─────────────────────────────
Orchestrator 建立一個 task 物件：
{
  task_id: "task_042",
  agent_id: 1,                          // DirectorAgent
  task_type: "generate_shot_intent",
  inputs: {
    script: "artifact_id:screenplay_v4",
    storyboard: "artifact_id:panel_05",
    mood: "artifact_id:mood_board_act2",
    critiques: ["use wider lens", "scene 2 clarity low"]
  },
  constraints: {
    model: "gemini-2.5-pro",
    generation_tool: "veo-3.1",
    budget_remaining: 58,
    max_cost: 2.50
  }
}


Step 2：入佇列 + worker 取走（QUEUE + WORKER PICKUP）
────────────────────────────────────────
任務進入 agent_1 佇列。
一個空閒 worker process 取走它。

worker pool 就似一個 thread pool：
  - 10–50 個並行 workers（可配置）
  - 每個 worker 都可以執行任何 agent 的任務
  - workers 無狀態 — 每次任務按需載入 agent 設定


Step 3：代理人執行（在 worker 內）（AGENT EXECUTION）
──────────────────────────────────────────────────

worker 會做：

  a) 載入 agent_id=1 的 AgentDefinition（DirectorAgent）
  b) 從 Asset Store 取回輸入 artifacts
  c) 從 MemoryAgent 取回相關記憶（向量檢索）
  d) 組裝 LLM messages：

     messages = [
       { role: "system", content: director_system_prompt },
       { role: "user", content: f"""
         Task: Generate shot intent for Scene 2, Shot 5.
         Script context: {script_excerpt}
         Storyboard panel: {panel_description}
         Mood reference: melancholic neo-noir, rain motif
         Critiques to address:
           - EditorAgent: "Use wider lens for Scene 3"
           - AudienceSim: "Scene 2 clarity score 0.6, below 0.7"
         
         Output: JSON shot intent with camera, subject, style, duration.
       """ }
     ]

  e) 呼叫 LLM（Gemini 2.5 Pro）：
     response = await llm.chat(messages, tools=[veo_api, memory_store])

  f) LLM 回應 tool calls：
     → tool_call: veo_api.generate(prompt="slow dolly push...", seed=4412)
     → Worker 執行此 tool call（HTTP 呼叫 Veo 3.1 API）
     → 回傳：video URL + metadata

  g) LLM 評估結果（self-refine）：
     → tool_call: clip_scorer.evaluate(video_url, text_prompt)
     → Score: 0.34（threshold: 0.32）✓ PASS

  h) 若 score < threshold：帶同回饋回到 (e) 再跑一輪
     若 score ≥ threshold：任務完成


Step 4：發佈結果（RESULT PUBLICATION）
────────────────────────────────────────
worker 發佈到 Event Bus：
  • { type: "artifact_created", artifact_id: "art_043", ... }
  • { type: "agent_state_change", agent: 1, state: "complete" }
  • { type: "metric_update", agent: 1, metric: "clip_t", value: 0.34 }

Orchestrator 收到「task_042 complete」→ 決定下一個任務。
```

---

## 4. 後端如何管理代理人生命週期

```text
┌─────────────────────────────────────────────────────────────────┐
│                       代理人生命週期                              │
│                                                                 │
│   IDLE ──────► QUEUED ──────► RUNNING ──────► COMPLETE          │
│    │              │              │                │              │
│    │              │              │                ▼              │
│    │              │              │           (publish result)    │
│    │              │              │                               │
│    │              │              ├──► SELF-REFINE（迴圈）          │
│    │              │              │         │                     │
│    │              │              │         ▼                     │
│    │              │              │   （帶回饋再跑）                │
│    │              │              │                               │
│    │              │              ├──► WAITING_FOR_CRITIQUE        │
│    │              │              │         │                     │
│    │              │              │         ▼                     │
│    │              │              │   （收到 critique 後繼續）      │
│    │              │              │                               │
│    │              │              └──► FAILED                      │
│    │              │                       │                      │
│    │              │                       ▼                      │
│    │              │                   （retry logic）             │
│    │              │                       │                      │
│    │              ◄───────────────────────┘（重新入佇列）           │
│    │                                                            │
│    ◄─────────── BLOCKED（等待 gate 審批或人類輸入）               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

後端會為每個 production 的每個 agent 追蹤狀態：

```python
# Per-production agent state (stored in PostgreSQL)
class AgentState:
    production_id: str
    agent_id: int
    state: "idle" | "queued" | "running" | "complete" | "failed" | "blocked"
    current_task_id: str | None
    iteration: int              # Which self-refine iteration
    last_metrics: dict          # { "clip_t": 0.34, "beat_coverage": 1.0 }
    critiques_pending: list     # Unprocessed critiques from other agents
    retry_count: int
    total_cost: float           # $ spent by this agent so far
    started_at: datetime
    completed_at: datetime | None
```

---

## 5. 代理人如何互相溝通（經由後端）

代理人 **不會** 直接互相對話。後端會中介所有通訊：

```text
DirectorAgent                    Backend                      EditorAgent
     │                              │                              │
     │  (completes shot intent)     │                              │
     │──publish: artifact_created──►│                              │
     │                              │                              │
     │                              │──(checks: who comments on    │
     │                              │   DirectorAgent's output?)   │
     │                              │                              │
     │                              │──deliver critique task──────►│
     │                              │                              │
     │                              │                              │
     │                              │◄──critique: "pacing too fast"│
     │                              │                              │
     │                              │──(checks: DirectorAgent      │
     │                              │   accepts critique from       │
     │                              │   EditorAgent? YES)           │
     │                              │                              │
     │◄──deliver critique──────────│                              │
     │                              │                              │
     │  (on next iteration,         │                              │
     │   incorporates feedback)     │                              │
```

Critique 路由邏輯：

```python
# When an agent publishes an artifact:
def on_artifact_created(event):
    producer_agent = agents[event.agent_id]
    
    # Find all agents that are configured to critique this agent
    critics = [a for a in agents if event.agent_id in a.comments_on]
    
    for critic in critics:
        # Only deliver if the producer accepts critique from this critic
        if critic.agent_id in producer_agent.accepts_critique_from:
            enqueue_critique_task(
                critic_agent=critic.agent_id,
                artifact=event.artifact_id,
                producer_agent=event.agent_id
            )
```

---

## 6. 後端如何處理並行代理人

Production 階段，多個代理人可以同時運行：

```text
TIME ──────────────────────────────────────────────────►

Worker 1: ████ DirectorAgent（Shot 5）████
Worker 2:       ████ PromptEngineerAgent（optimizing）████
Worker 3:            ████ AIQAAgent（checking Shot 4）████
Worker 4:                 ████ MoodBoardAgent（reference）████
Worker 5: ████████ ComposerAgent（theme for Act 2）████████

                         │
                         ▼
              全部都會發佈 events 到 Event Bus
              Orchestrator 協調相依：
              「EditorAgent 需等 DirectorAgent
               完成此場景所有鏡頭先可以開始」
```

Orchestrator 會用 **相依圖（dependency graph）** 來知道幾時派發：

```python
# Dependency rules (encoded in the DAG)
dependencies = {
    "editor_assemble": {
        "requires": ["director_all_shots_complete", "composer_score_ready"],
        "gate": "production_gate_passed"
    },
    "colorist_grade": {
        "requires": ["editor_rough_cut_complete"],
    },
    "sound_mix": {
        "requires": ["sound_design_complete", "composer_final_mix"],
    }
}

# Orchestrator checks after every task completion:
def on_task_complete(task):
    for pending_task, deps in dependencies.items():
        if all(is_satisfied(dep) for dep in deps["requires"]):
            dispatch(pending_task)  # Now it can run!
```

---

## 7. 後端如何處理失敗

```text
代理人任務失敗（LLM error、tool timeout、品質低於 threshold）
    │
    ▼
重試邏輯（Orchestrator 內）：
    │
    ├── retry_count < max_retries（預設 3）？
    │     YES → 用 exponential backoff 重新入佇列
    │           （等 5s、15s、45s）
    │
    ├── 是否 transient error（API timeout、rate limit）？
    │     YES → 用相同參數重試
    │
    ├── 是否 quality failure（CLIP-T 太低）？
    │     YES → 交由 PromptOptimizerAgent 調整 prompt 再重試
    │
    ├── 是否 budget overrun？
    │     YES → 以更便宜模型重試（CostOptimizer fallback）
    │
    └── 重試已用盡？
          YES → 標記 agent FAILED
               → 透過 WebSocket 通知 UI（DAG 紅色節點）
               → 使用者可：[Retry] [Skip] [Modify & Retry]
```

---

## 8. 後端如何管理記憶（Memory）

MemoryAgent 不只是一個普通代理人 — 它更像一個 **共享服務**，其他代理人會呼叫它：

```text
┌─────────────────────────────────────────────────────────────────┐
│                         記憶系統（MEMORY）                        │
│                                                                 │
│  ┌─────────────────┐          ┌─────────────────────────────┐  │
│  │  Vector DB       │          │  Structured Store            │  │
│  │  （Pinecone）     │          │  （PostgreSQL）               │  │
│  │                  │          │                             │  │
│  │  Stores：         │          │  Stores：                    │  │
│  │  • Style locks    │          │  • Series bible entries     │  │
│  │  • Tone notes     │          │  • Character state          │  │
│  │  • Past decisions │          │  • Continuity log           │  │
│  │  • Critique hist  │          │  • Budget decisions         │  │
│  └────────┬─────────┘          └──────────────┬──────────────┘  │
│           │                                    │                 │
│           └──────────────┬─────────────────────┘                 │
│                          │                                       │
│                          ▼                                       │
│              ┌───────────────────────┐                           │
│              │      Memory API       │                           │
│              │                       │                           │
│              │   recall(query) →     │   任何 agent 都可以把       │
│              │     relevant entries  │   它當作一個 TOOL 於 LLM     │
│              │                       │   執行期間呼叫              │
│              │   store(entry) →      │                           │
│              │     persists fact     │                           │
│              └───────────────────────┘                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

例子：DirectorAgent 處理 Shot 5
────────────────────────────────
LLM 決定：「我需要查 Act 2 已鎖定的視覺風格」

→ tool_call: memory.recall("Act 2 visual style lock")
→ 回傳：「Style lock: Veo 3.1 seed #4412, melancholic neo-noir」

LLM 用呢啲資料生成一致的 prompt。
```

---

## 9. 完整後端控制流程圖

```text
使用者按 [▶ LAUNCH]
         │
         ▼
┌─────────────────────────────┐
│         API GATEWAY          │
│     POST /productions        │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│     PRODUCTION MANAGER       │
│  • 建立 DB 記錄              │
│  • 載入範本（A–J）            │
│  • 初始化預算                │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│     協調引擎（LangGraph）                                     │
│                                                             │
│  Phase 1：PLANNING                                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 1. 呼叫 PlannerAgent（agent_id=54）                  │    │
│  │    → LLM 拆解 brief 成分段 DAG                        │    │
│  │    → 輸出：{tasks: [...], gates: [...], deps: {}}     │    │
│  │                                                     │    │
│  │ 2. 呼叫 RouterAgent（agent_id=55）                   │    │
│  │    → 逐 task 指派 model + provider                   │    │
│  │    → 依照 budget constraints                          │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  Phase 2：EXECUTION（重覆直到所有 phases 完成）              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 3. 派發任務到 WORKER POOL：                           │    │
│  │    • 依相依可並行                                     │    │
│  │    • 需要順序的就依序                                  │    │
│  │                                                     │    │
│  │ 4. WORKER 執行 agent 任務：                           │    │
│  │    load_config → build_prompt → call_LLM →           │    │
│  │    execute_tools → self_refine → publish_result      │    │
│  │                                                     │    │
│  │ 5. 任務完成後：                                      │    │
│  │    • 更新 agent state                                │    │
│  │    • 檢查 critics 是否需要運行                        │    │
│  │    • 檢查相依是否已滿足                                │    │
│  │    • 派發下一批合格任務                                │    │
│  │                                                     │    │
│  │ 6. 到達 GATE 時：                                     │    │
│  │    • GateKeeperAgent 評估 criteria                    │    │
│  │    • JudgeAgent 按 rubric 評分                        │    │
│  │    • 若 auto-pass：推進                               │    │
│  │    • 若需要人類：PAUSE + 通知 UI                      │    │
│  │    • 等待人類決定                                     │    │
│  │    • 批准：進入下一 phase                              │    │
│  │    • 拒絕：把回饋派回 revision agents                  │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  Phase 3：DELIVERY（所有 gates 通過後）                      │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 7. DistributorAgent 逐渠道封裝                        │    │
│  │ 8. ComplianceAgent 簽署 C2PA                          │    │
│  │ 9. 發佈到目標平台                                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 10. 總結：後端的角色

| 後端責任 | 做法 |
|----------------------|----------------|
| **定義 agents** | agent configs 存於 DB（prompt、tools、rubric、關係） |
| **決定何時運行** | DAG 相依圖 — 只在前置完成後派發 |
| **決定用邊個 model** | RouterAgent + 成本規則 → 選最平但達標的模型 |
| **執行 agent 邏輯** | worker 載入 config → 組 prompt → 呼叫 LLM → 執行 tools |
| **Self-refine 迴圈** | worker 檢查品質指標 → 低於 threshold 就帶回饋重跑 |
| **路由 critiques** | 依「accepts_critique_from」設定把訊息派去目標佇列 |
| **管理狀態** | PostgreSQL 追蹤 agent 狀態、重試次數、成本、metrics |
| **處理失敗** | backoff 重試 → 便宜模型 fallback → 升級給人類處理 |
| **執行 gates** | 評估 criteria → 暫停等待人類 → 批准後推進 |
| **擴展 workers** | 水平擴展 worker pool — 增加並行能力 |
| **持久化一切** | event sourcing — 可回放每個決策、critique、artifact |

---

## 關鍵洞見：代理人不是獨立服務

```text
錯誤嘅 mental model：
  「每個 agent 係一個 24/7 運行嘅 microservice」

  DirectorAgent-service ──┐
  EditorAgent-service ────┤── 同時運行
  ComposerAgent-service ──┤
  ... 114 services ───────┘

正確嘅 mental model：
  「agents 係設定；workers 會按需實例化去執行」

  ┌─────────────────────────────┐
  │          WORKER POOL         │
  │        （10–50 processes）    │
  │                             │
  │  Worker 1：正執行 DirectorAgent 任務
  │  Worker 2：正執行 PromptEngineerAgent 任務
  │  Worker 3：idle（等下一個任務）
  │  Worker 4：正執行 AIQAAgent 任務
  │  ...                        │
  └─────────────────────────────┘

  每個 worker 都可以執行任何 agent。
  它會載入 agent 設定、跑 LLM、之後再去處理下一個任務。
  就好似同一個演員，可以按劇本飾演唔同角色。
```

因此，114 個代理人唔需要 114 部伺服器。一個 10–50 個 worker 的 pool 就可以處理全部，按佇列逐個取任務執行。
