# 精煉版 Agent Loop：分層式、受 ReAct 啟發、生產級設計

**版本：** 2026-06-07（已根據 MASFT 分類法與相關研究中已知 agent loop 失敗模式的全面研究更新，並整合來自 Reflexion、critic 框架、結構化規格、記憶體架構與生產模式的針對性緩解方法）  
**研究來源**：〈Why Do Multi-Agent LLM Systems Fail?〉（MASFT 分類法，14-18 種失敗模式）、Reflexion、Prospector、CGI、記憶體論文、xAI 文件，以及開發者對無限迴圈／上下文問題的實務報告。  
**用途：** 這是一份可執行的參考文件，用於建構可靠、可擴展、以 LLM 為基礎的 agent 系統。它結合了學術基礎（ReAct 中推理 + 行動的協同作用）、xAI 的伺服器端 agentic 實作（面向深度研究的多代理協作），以及進階分層模式（planner + specialists + 自我演化）。  
**目標讀者：** harness、多代理系統、coding agent、research agent 的建構者（例如帶 critic／自我精煉迴圈的 N1ch01as 風格 Architect）。  
**核心原則：** 受控迴圈，具備明確狀態、結構化輸出、品質關卡與分層委派。不是失控的連鎖反應，而是帶有向上彙整與有意識綜合的受管理協作。

## 1. 核心原則（根據研究精煉）

### 1.1 基礎：ReAct 範式（Yao 等，ICLR 2023）
- **定義**：交錯進行**語言推理軌跡（Thoughts）**與**行動（actions）**（工具呼叫、環境互動或委派）。來自行動的 observation 會為推理提供 grounding 並更新推理。
- **它為何有效：**
  - 純 Chain-of-Thought（CoT）：靜態，容易產生幻覺與錯誤傳播（因為缺少外部 grounding）。
  - 純行動：缺少高層規劃、例外處理能力差、軌跡效率低。
  - **ReAct 協同效應**：Thought 可拆解目標、追蹤進度、處理例外並重新規劃。Action 提供真實 observation，以修正推理並支持適應性調整。結果是在互動式任務上有 10-34% 提升，並降低知識型任務中的幻覺。
- **基本循環**（單次迭代）：
  1. **Thought**：LLM 針對當前狀態、目標、進度、下一步或例外狀況進行推理。（內部步驟，會更新上下文。）
  2. **Action**：決定並輸出可執行步驟（含參數的工具呼叫、子代理委派，或 `Finish`/`Done`）。
  3. **Observation**：環境／工具／子代理回傳結構化結果（資料 + metadata：status、confidence、summary、issues）。
  4. 附加到歷史／狀態 → 重複。
- **Prompt 結構**（few-shot 範例非常重要）：對推理密集任務（QA／research）使用較密集的 thoughts；對 embodied／decision 類任務使用較稀疏的 thoughts。用明確標籤或 JSON schema 確保可解析。
- **例外處理**：Thought 步驟偵測失敗（「沒有返回任何有用結果」）→ 在下一輪重新規劃或調整 action。

**xAI 對齊方式**：Grok 的伺服器端 agentic tool calling 在內部實作了生產級的 ReAct 風格迴圈。模型自行決定工具、在伺服器端執行（web_search、x_search、code_execution、collections_search），反覆迭代直到能產生最終答案。客戶端只會看到最終輸出（或串流輸出）+ 可選的 reasoning token。

### 1.2 生產級 xAI 多代理協作（2026）
- **grok-4.20-multi-agent**（或等效模型）：可啟動可配置的代理團隊（4 個代理適合快速／聚焦；16 個代理適合深入／全面）。
- **此迴圈如何運作：**
  - 伺服器端**即時協作**：多個專門代理平行運作。
  - 每個代理都提供推理、工具呼叫與發現。
  - **Leader agent** 綜合討論內容、進行交叉比對，並輸出最終結構化答案。
  - 根據中間發現進行平行工具呼叫與持續迭代。
  - 子代理內部狀態預設加密／隱藏（兼顧控制與安全）；僅 leader 輸出 +（可選）加密內容對外可見。
- **優勢**：適合深度多步研究、結構化輸出（表格、比較）、即時精煉，以及在無須客戶端介入迴圈的情況下自動使用工具。
- **先規劃元素**：xAI 工具如 Grok Build CLI 的互補模式，是先明確產生計畫，再進行平行子代理執行（例如在隔離 Git worktree 中最多 8 個子代理）。

### 1.3 分層式 + 可自我演化（AgentOrchestra / 2025-2026 綜述）
- 最上層設置**中央 Planner / Orchestrator / Supervisor**。
- 將任務拆解為子任務 → 委派給**專業子代理**（Deep Researcher、Analyzer、Browser/Tool agents、Reporter 等）。
- 每個子代理執行其**自己的迴圈**（ReAct 風格或領域最佳化版本）。
- 採用**樹狀路由** + 結果向上冒泡。
- **TEA Protocol 啟發**（Tool-Environment-Agent）：將工具、環境與代理視為一等公民、可版本化、具生命週期管理的實體，並以標準化協議處理上下文、呼叫與演化。
- **閉環回饋／自我演化**：
  - Reflection（對 trace 進行語言式自我批判）。
  - 基於 trace 的最佳化（例如 TextGrad 風格：歸因錯誤 → 提出修改 → 在保留資料上驗證 → 建立版本／註冊）。
  - Version manager：註冊改善後的 prompts/tools/agents；支援 rollback／選最佳版本。
  - Tracer：記錄完整執行軌跡（可稽核性 + 最佳化訊號）。
- **彙整**：Planner 聚合子結果、協調證據、解決衝突、更新全域 plan/state，或觸發進一步精煉。最終綜合通常由專門的 Reporter agent 處理，並負責 citations／去重。
- **效能證據**：AgentOrchestra 風格系統在 GAIA benchmark 上可達 89%+；子代理 + 自我演化能帶來雙位數提升；相較平面式多代理，分層路由有更好的可擴展性。

**整體精煉模型**：先從 ReAct 核心迴圈開始。面對複雜度時疊加分層委派。再加入顯式規劃階段 + reflection/critique 關卡 + 結構化狀態／版本管理，以提升生產級可靠性。xAI 已證明這類模式可在伺服器端藉由強大的協作原語穩定執行。

## 1.4 已知問題、失敗模式與對應緩解方法（有研究支持）

近期系統性研究（尤其是基於熱門多代理框架 150+ 條 trace 分析所得的 **MASFT taxonomy**）指出，**大多數失敗來自設計／規格問題（約 40%+）**、協調失效，以及薄弱的驗證／終止控制，**而不是模型本身的原始智能不足**。單代理 ReAct 迴圈也會遇到相似問題，並額外面對上下文膨脹與重複行為。以下整理出最常見、已有充分記錄的問題類型，並將**可執行的緩解方法**直接對應到本文件的各個階段。

### 主要問題類別與頻率／重要性
1. **規格與設計歧義（最大類別）**
   - 不遵守或誤解任務規格、角色模糊、缺少成功標準或輸出契約。
   - **影響**：代理會很早偏離方向，錯誤沿下游持續放大。
   - **緩解方法**：
     - Phase 0：強制使用結構化 Task Specification，明確列出 success criteria、constraints、output schema 與 quality thresholds。使用可更新的「living spec」。
     - 在迴圈開始前加入自動 spec validation（critic 或 schema check）。
     - 為 orchestrator 與子代理之間建立清楚的角色定義與資訊契約。

2. **無限迴圈、重複動作與空轉**
   - 代理重複相同（或相似）動作卻沒有進展；這在 ReAct 中很常見，通常源自例外處理差或資訊不足，也可能被 prompt injection 誘發。
   - **影響**：浪費 token／成本、造成 timeout、引發挫折（真實世界中非常常見的抱怨）。
   - **緩解方法**：
     - Phase 1 迴圈：加入**循環偵測**（對近期 actions + observations 進行 state hashing；若相似度超過閾值，強制重新規劃或終止）。
     - 明確設置 `max_steps`、`max_reflection_rounds`，以及基於進度的提前退出（例如 todo 完成百分比）。
     - 有界 reflection：限制「再改善一次」這類迭代次數。
     - 設置 `Done` / `Finish` 工具，且在接受前必須經過強制驗證。
     - 在分層架構中，由 Orchestrator 監控子代理進度，並可終止／重新分派卡住的分支。

3. **Context Window 爆炸 / Context Rot / 歷史膨脹**
   - 長軌跡會導致早期關鍵資訊或指令被遺失，進而造成不一致、重複與目標漂移。
   - **影響**：長時間執行或多輪任務中的表現劣化。
   - **緩解方法**：
     - 積極使用分層式記憶體：短期工作記憶 + 長期持久儲存（vector search、semantic caching、MemGPT 風格）。
     - 在里程碑或上下文超過閾值時進行摘要（signal-aware truncation）。
     - 使用結構化狀態（`task.md`、todo list、僅保留 key facts），而不是每輪都灌入完整歷史。
     - 子代理只接收相關的 context slice + provenance。

4. **幻覺、錯誤累積與驗證薄弱**
   - 虛構事實、誤解工具結果，或未驗證的主張一路傳播（在多代理中更嚴重）。
   - **影響**：最終輸出不可靠；錯誤級聯失控。
   - **緩解方法**：
     - 將 **Verifier / Critic agents** 設為強制品質關卡（Phase 3 彙整後，以及子結果返回後）。
     - 使用結構化 observation schema（status、confidence、issues list）+ 交叉驗證（跨代理／跨來源比對）。
     - 採用多形式驗證（既要求 observation grounding，也要求外部檢查）。
     - 進行 trajectory ranking（例如 Prospector 風格，由 critic 在多個候選結果中選最佳者）。
     - 在自我演化時：只允許提交已在 held-out trace 上驗證過的修改。

5. **代理間失配與協調失敗（多代理特有）**
   - 角色越界、目標衝突、共享狀態過舊、溝通缺口、錯誤在代理間傳播。
   - **影響**：協作品質差；有時單一強代理反而勝過複雜 MAS。
   - **緩解方法**：
     - 使用強力中央 **Orchestrator/Planner** 進行明確拆解與路由（分層控制優於平面式結構）。
     - 建立資訊契約 + 結構化交接格式。
     - 共享狀態採版本化 + 使用持久化協調原語（例如 streams、pub/sub）。
     - 使用熔斷器：偵測不一致 → 暫停、調和或升級處理。
     - 明確的「極端分層分工」（清楚定義 specialist roles）。

6. **終止與目標漂移問題**
   - 過早停止（工作未完成）或無法辨識已完成；代理可能錯誤地繼續執行或提早放棄。
   - **影響**：得到錯誤或不完整結果。
   - **緩解方法**：
     - 在 spec 中明確列出 success criteria，並對其進行進度追蹤。
     - 設置專用終止 action（`Done` tool），且必須通過 verifier。
     - 在 Thought 步驟定期檢查是否仍對齊原始 objective。
     - 當中間結果已符合條件時，提供提前終止訊號。

7. **其他值得注意的問題**
   - **狀態過時與記憶體失效**：採用混合式記憶體（快速短期 + 可檢索的持久長期）。
   - **安全性（prompt injection → 造成迴圈或濫用）**：工具沙箱、輸入淨化、最小權限工具存取、監控異常循環模式。
   - **成本與可擴展性負擔**：只有在收益 > 協調成本時才使用多代理；按 phase 監控 token 用量；在安全前提下進行平行化。
   - **可除錯性**：完整 tracer + 結構化 logs 是不可妥協的要求。

### 緩解方法如何整合到迴圈階段中
- **Phase 0（初始化）**：規格工程 + 驗證是投資報酬率最高的修正點。
- **Phase 1（核心迴圈）**：循環偵測、有界步數／反思、結構化 observation、進度追蹤。
- **Phase 2（委派）**：狹義子規格 + 契約；由 orchestrator 監控。
- **Phase 3（彙整）**：verifier/critic 關卡、交叉驗證、協調整合。
- **Phase 4（反思／自我演化）**：先驗證再套用修改；維持有界迴圈。
- **Phase 5（終止）**：verifier + 帶證據的顯式 Done。

**研究關鍵洞見**：修正**規格品質 + 驗證層 + 明確終止控制**，能帶來最大的可靠性提升。如果缺少這些保護措施，只是一味增加代理數量或模型能力，通常只會得到遞減甚至負面回報。

## 2. 完整 Agent Loop 流程（可執行）

### Phase 0：初始化（Spec-Driven Setup）
**目標**：在任何迴圈迭代開始前先建立清楚契約。
1. 解析人類指令 → 產生／驗證**Task Specification**（結構化：objective、success criteria、constraints、output format、最大 budget/steps/tokens、quality thresholds）。
2. 建立**初始狀態**：
   - `task.md` 或結構化 scratchpad（目前計畫、todo list、進度、待釐清問題）。
   - 記憶體：短期（近期 observations）、長期（檢索到的知識、過往版本）。
   - Tracer / execution log（供之後反思使用）。
   - Version registry（若會演化 prompts/tools/agents）。
3. **可選的計畫生成**（Plan-and-Execute 風格，對複雜任務建議開啟）：
   - Orchestrator LLM 產生高層 plan（編號步驟或 dependency graph）。
   - 針對 spec 驗證此 plan（自我批判或專用 critic）。
   - 存入 state。
4. 決定架構：Flat ReAct（簡單）vs Hierarchical（複雜研究／coding）vs Hybrid。

**可執行輸出格式**（JSON 或 Markdown 區塊範例）：
```json
{
  "task_id": "...",
  "objective": "...",
  "success_criteria": ["...", "..."],
  "constraints": ["max_steps: 50", "budget_tokens: 200k"],
  "output_format": "structured report with citations",
  "initial_plan": ["Step 1: ...", "Step 2: ..."],
  "quality_gates": ["completeness > 90%", "no hallucinations", "structured output"]
}
```

### Phase 1：核心迭代迴圈（受 ReAct 啟發，且受控）
在尚未終止前持續執行：
1. **觀察目前狀態**：載入完整／相關歷史 + task spec + 當前 plan/todo + 最新 observations。（如果上下文過長要積極摘要，交由 memory manager 處理。）
2. **推理（Thought）**：
   - 分析當前進度相對於 success criteria 的位置。
   - 識別缺口、風險、例外狀況。
   - 決定策略：直接用工具、委派子任務、先行綜合、反思／批判，或結束。
   - 如有需要，更新內部 plan 或 todo。
3. **行動／決定下一步**（必須是嚴格結構化輸出，可解析）：
   - **選項 A（Tool）**：呼叫內建或自訂工具（含 args）。xAI 風格下，伺服器會在迴圈內處理執行。
   - **選項 B（Delegate）**：以狹義子指令 + context slice + 該子任務的 success criteria 呼叫子代理。（分層式）
   - **選項 C（Internal）**：只更新 state/plan，或對草稿執行 critic。
   - **選項 D（Finish）**：若品質關卡已通過，輸出最終答案。
4. **執行並觀察**：
   - 執行 action（工具或子代理迴圈）。
   - 蒐集**結構化 observation**：
     ```json
     {
       "status": "success | partial | failed",
       "data": {...},
       "summary": "concise natural language",
       "confidence": 0.85,
       "issues": ["list of problems"],
       "next_suggestions": ["..."],
       "trace_id": "..."
     }
     ```
   - 附加到 history + 更新 todo/state。
5. **輕量反思**（每 N 步或失敗時）：快速自我批判 —「目前這條軌跡是否仍然對齊？有沒有明顯可修正之處？」

**熔斷器模式（生產環境建議使用）**

熔斷器可在工具、LLM 呼叫或子代理反覆失敗時，防止級聯失敗。它有三種狀態：
- **CLOSED**：正常運作，請求可通過。
- **OPEN**：失敗過多 → 立即 fast-fail（保護系統）。
- **HALF_OPEN**：等待 timeout 後，允許有限測試請求，以確認是否恢復。

建議每種工具類型或每種子代理角色各使用一個熔斷器，並與下方重試包裝器整合。

**程式碼範例：含循環偵測的最小受控 ReAct 迴圈（Python）**

```python
import hashlib
from typing import Any, Dict, List
from dataclasses import dataclass, field

@dataclass
class AgentState:
    task_spec: Dict[str, Any]
    history: List[Dict] = field(default_factory=list)
    todo: List[str] = field(default_factory=list)
    max_steps: int = 50
    seen_states: set = field(default_factory=set)  # for cycle detection

def hash_state(state: AgentState) -> str:
    """Simple cycle detection via recent action+obs hash"""
    recent = state.history[-3:] if len(state.history) > 3 else state.history
    return hashlib.md5(str(recent).encode()).hexdigest()

def controlled_react_loop(llm, tools, state: AgentState, max_retries: int = 3):
    import time
    import traceback

    step = 0
    while step < state.max_steps:
        step += 1
        current_hash = hash_state(state)
        if current_hash in state.seen_states:
            print("Cycle detected — forcing replan or terminate")
            # In production: trigger critic or escalate to human
            break
        state.seen_states.add(current_hash)

        try:
            # 1. Observe + build context (summarize if long)
            context = build_context(state)

            # 2. Reason + Decide (strict structured output)
            decision = llm.generate(
                prompt=build_decision_prompt(context, state.task_spec),
                output_schema={"thought": str, "action_type": str, "payload": dict}
            )

            if decision.action_type == "finish":
                if verify_output(decision.payload, state.task_spec):
                    return decision.payload
                else:
                    continue

            # 3. Execute with robust error handling
            obs = None
            if decision.action_type == "tool":
                obs = safe_execute_tool(decision.payload, tools, max_retries=max_retries)
            elif decision.action_type == "delegate":
                obs = safe_invoke_sub_agent(decision.payload, max_retries=max_retries)
            else:
                obs = {"status": "internal", "data": None}

        except Exception as e:
            # Structured error observation
            obs = {
                "status": "error",
                "error_type": type(e).__name__,
                "error_message": str(e),
                "traceback": traceback.format_exc(),
                "step": step
            }
            print(f"Error at step {step}: {e}")  # or send to tracer

        # 4. Structured observation + update state
        state.history.append({
            "thought": getattr(decision, 'thought', 'N/A'),
            "action": getattr(decision, 'action_type', 'error'),
            "observation": obs
        })
        update_todo(state, obs)

        # Optional: exponential backoff on errors
        if obs.get("status") == "error":
            time.sleep(min(2 ** (step % 5), 30))  # simple backoff

    return {"status": "max_steps_reached_or_error", "partial_result": state.history[-1]}


class CircuitBreaker:
    """
    Production-grade circuit breaker with proper Half-Open logic.

    States:
    - CLOSED: Normal operation. All calls go through.
    - OPEN: Too many failures. Fast-fail immediately to protect downstream systems.
    - HALF_OPEN: Recovery testing phase. Allow a limited number of test calls.
      - Success → back to CLOSED.
      - Failure → back to OPEN.
    """
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 30, half_open_max_calls: int = 1):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls

        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"
        self.half_open_calls_made = 0  # track test calls in HALF_OPEN

    def _should_allow_request(self) -> bool:
        import time
        now = time.time()

        if self.state == "CLOSED":
            return True

        if self.state == "OPEN":
            if now - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
                self.half_open_calls_made = 0
                return True
            return False

        if self.state == "HALF_OPEN":
            if self.half_open_calls_made < self.half_open_max_calls:
                self.half_open_calls_made += 1
                return True
            return False

        return False

    def call(self, func, *args, **kwargs):
        import time

        if not self._should_allow_request():
            return {
                "status": "circuit_open",
                "error": f"Circuit breaker is {self.state} - fast failing",
                "circuit_state": self.state
            }

        try:
            result = func(*args, **kwargs)

            # Success path
            if self.state == "HALF_OPEN":
                # Successful test call in recovery → fully recover
                self.state = "CLOSED"
                self.failure_count = 0
                self.half_open_calls_made = 0
            elif self.state == "CLOSED":
                self.failure_count = 0

            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.state == "HALF_OPEN":
                # Test call failed during recovery → go back to OPEN
                self.state = "OPEN"
                self.half_open_calls_made = 0
            elif self.failure_count >= self.failure_threshold:
                self.state = "OPEN"

            raise e

    def should_retry(self) -> bool:
        """
        Returns True if we should attempt (or re-attempt) the operation.
        Useful for explicit "repeat if needed" logic outside the breaker.
        """
        return self.state in ("CLOSED", "HALF_OPEN")

    def reset(self):
        """Manually reset the circuit breaker to CLOSED state."""
        self.state = "CLOSED"
        self.failure_count = 0
        self.half_open_calls_made = 0
        self.last_failure_time = 0


def safe_execute_tool(payload: dict, tools: dict, max_retries: int = 3, circuit_breaker: CircuitBreaker = None) -> dict:
    """Retry wrapper for tool execution with structured error output + circuit breaker"""
    cb = circuit_breaker or CircuitBreaker()

    for attempt in range(max_retries):
        try:
            def _call():
                tool_name = payload.get("tool_name")
                args = payload.get("args", {})
                if tool_name not in tools:
                    return {"status": "error", "error": f"Unknown tool: {tool_name}"}
                result = tools[tool_name](**args)
                return {"status": "success", "data": result}

            result = cb.call(_call)
            return result
        except Exception as e:
            if attempt == max_retries - 1:
                return {
                    "status": "error",
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                    "attempts": attempt + 1,
                    "circuit_state": cb.state
                }
            time.sleep(0.5 * (attempt + 1))
    return {"status": "error", "error": "Max retries exceeded", "circuit_state": cb.state}


def safe_invoke_sub_agent(payload: dict, max_retries: int = 2, circuit_breaker: CircuitBreaker = None) -> dict:
    """Wrapper for sub-agent delegation with retry, structured result + circuit breaker"""
    cb = circuit_breaker or CircuitBreaker(failure_threshold=3, recovery_timeout=60)

    for attempt in range(max_retries):
        try:
            def _call():
                result = invoke_sub_agent(payload)
                if result.get("status") in ["success", "partial"]:
                    return result
                raise RuntimeError(f"Sub-agent returned non-success: {result.get('status')}")

            result = cb.call(_call)
            return result
        except Exception as e:
            if attempt == max_retries - 1:
                return {
                    "status": "error",
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                    "attempts": attempt + 1,
                    "sub_agent_payload": payload,
                    "circuit_state": cb.state
                }
            time.sleep(1)
    return {"status": "error", "error": "Sub-agent max retries exceeded", "circuit_state": cb.state}
```

**程式碼範例：輕量 Verifier / Critic Agent（Prompt + Schema）**

```python
VERIFIER_PROMPT = """
You are a strict, skeptical Verifier Agent. 
Given the original task_spec and the candidate_output, 
return ONLY valid JSON:

{
  "passes": true | false,
  "score": 0.0-1.0,
  "issues": ["list of concrete problems"],
  "suggestions": ["actionable fixes"],
  "confidence": 0.0-1.0
}

Task Spec: {task_spec}
Candidate Output: {candidate_output}
"""

def verify_output(candidate: dict, task_spec: dict, llm) -> dict:
    prompt = VERIFIER_PROMPT.format(
        task_spec=task_spec, 
        candidate_output=candidate
    )
    result = llm.generate(prompt, output_schema=...)  # force JSON
    return result
```

**程式碼範例：簡單的自我演化 / Reflection 步驟（Trace → Edit → Validate）**

```python
def self_evolve_component(component_name: str, trace: List[dict], llm, version_manager):
    """Minimal TextGrad / reflection-style evolution"""
    diagnosis = llm.generate(
        f"Analyze this execution trace and identify the root cause of any failures or inefficiencies:\n{trace}",
        output_schema={"root_cause": str, "target_component": str, "proposed_edit": str}
    )
    
    if diagnosis.target_component == component_name:
        new_version = apply_edit(component_name, diagnosis.proposed_edit)
        # Validate on held-out or re-execution
        if validate_improvement(new_version, trace):
            version_manager.register(new_version, parent=component_name)
            return new_version
    return None  # no change or rollback
```

**終止條件**（每次迭代或在關卡時檢查）：
- 已達成 success criteria + 通過 quality gate。
- 已達最大步數／token 預算／時間上限。
- 顯式 `Done` / `Finish` action，且輸出已驗證。
- 不可恢復失敗（升級給 human 或更高層 orchestrator）。
- 若中間結果已符合 objective，則提早退出。

### Phase 2：分層委派與子迴圈
當 orchestrator 決定委派時：
1. **拆解與路由**：
   - Planner 選擇或實例化適當的子代理類型（specialist role、toolset、prompt template）。
   - 建立狹義子任務規格（父目標的子集 + 相關 context slice）。
   - 呼叫子代理（可以是同一個 LLM 搭配不同 system prompt/role，也可以是不同模型）。
2. **子代理執行獨立迴圈**：
   - 子代理根據自己的子規格，執行自己的 ReAct 風格迭代（或最佳化變體）。
   - 維護本地 state/memory。
   - 可再進一步委派（樹狀結構）或呼叫工具。
3. **將結構化結果回傳**給父代理（向上冒泡）：
   - 使用與前文相同的 structured observation 格式。
   - 內含 provenance（由哪個子代理產生、trace summary）。
4. **父代理處理**：
   - 記錄到全域 state/tracer。
   - 驗證／整合（與其他分支合併，並透過 harmonization step 解決衝突）。
   - 更新全域 plan/todo。
   - 決定下一步：更多委派、直接行動、彙整或批判檢查。

**平行性**：若依賴關係允許（例如彼此獨立的研究分支），可同時執行多個子代理／工具（如 xAI 多代理模式，或像 Grok Build 一樣使用 worktree 隔離）。

### Phase 3：彙整、綜合與重組
在取得子結果或達到重要里程碑後：
1. **聚合**：收集所有相關 observations + plan progress。
2. **協調整合**：透過 LLM（或專用 Reporter agent）進行合併、去重、交叉參照與衝突解決，產生統一視圖。
3. **重組**：轉換成目標輸出形狀（report、code、answer、updated plan）。強制符合初始 spec 中要求的格式。
4. **品質關卡**：
   - 執行 critic/refiner：對照 success criteria 評分、檢查幻覺／缺口、提出修正建議。
   - 若未通過：觸發精煉迴圈（重新規劃、重新委派特定部分，或自我編修）。
   - 若通過：繼續推進（或進行最後潤飾）。
5. **更新狀態**：將彙整後的知識持久化到 long-term memory／versioned artifacts。

**Consolidator Prompt 片段範例**：
「你是一名綜合專家。給定原始 task spec、目前 plan，以及這些子結果 [structured list]，請輸出：1）更新後的進度摘要。2）已解決的衝突。3）最終輸出區塊草稿。4）剩餘缺口與建議下一步行動。」

### Phase 4：反思、批判與自我演化（進階）
- **每條軌跡或每個里程碑的反思**：LLM 摘要 trace、診斷失敗／成功、提出改進（prompt edits、tool patches、新的子代理類型）。
- **自我演化迴圈**（受 AgentOrchestra 啟發）：
  1. 透過 tracer 蒐集 trace。
  2. 歸因錯誤／發現機會點（LLM 或 TextGrad 風格方法）。
  3. 提出有針對性的修改（prompts、tools、agent configs，甚至是生成程式碼）。
  4. 驗證修改（在 held-out 或相似任務上重新執行；檢查 metrics）。
  5. 如果有改善：註冊新版本（保留 lineage）。支援 rollback。
- **Critic Agent 角色**：一個獨立、較輕量的代理，只負責審查草稿／計畫，而不執行完整流程。可在關卡時被呼叫。
- **優點**：系統可在執行期間持續改善；對於反覆出現的相似任務分佈，生產系統會變得越來越穩健。

### Phase 5：終止與輸出
- 當通過關卡或達到終止條件時：
  1. 執行最後一次綜合。
  2. 產出結構化最終輸出（符合 spec）。
  3. 可選：為使用者或 log 產生事後 reflection 摘要。
  4. 持久化完整 trace + 版本，用於 audit/replay/debug。
- **Human-in-loop hooks**：在品質關卡失敗、高風險行動，或預算耗盡時觸發。

## 3. 狀態、記憶體與基礎設施建議

- **State Schema**：task_spec + current_plan/todo + history（thought/action/observation tuples）+ memory（key-value 或 vector）+ versions + tracer。
- **記憶體管理**：分層式（每個子代理本地 + 全域）。上下文壓力高時做摘要。並行執行時要做 session isolation。
- **Tracing**：完整執行圖（誰呼叫了什麼、結果、耗時、版本）。這是除錯、反思與最佳化的基礎。
- **Versioning**（受 TEA 啟發）：prompts、tools、agent roles、generated artifacts — 全部都需要可追溯 lineage 與 rollback 的版本管理。
- **xAI 整合建議**：
  - 對研究密集型頂層任務使用 Grok multi-agent mode。
  - 混合使用伺服器端 agentic tools 與客戶端自訂工具（hybrid）。
  - 對 coding agents：採用先規劃 + 在隔離環境（worktrees）中平行子代理的方式。
  - 在可能情況下串流 reasoning tokens，以提升透明度。
- **生產級強化**：
  - 嚴格輸出 schema（JSON mode 或 constrained decoding）。
  - Timeout、帶 backoff 的重試、對失敗工具／子代理使用熔斷器。
  - 成本／token 預算與監控。
  - Logging + observability（每個 thought/action/observation 都要記錄）。
  - 對工具／程式碼執行採用沙箱。

## 4. 決策框架（何時使用哪種模式）

| 任務複雜度 | 建議模式 | 建議啟用的關鍵能力 | 使用範例 |
|-----------------------|--------------------------------------|---------------------------------|------------------|
| 簡單事實查找 | Flat ReAct（單一迴圈） | 工具呼叫、基本 thought | 快速搜尋 + 回答 |
| 多步研究 | xAI Multi-Agent 或 Hierarchical | 平行代理、leader 綜合 | 帶來源的深度分析 |
| Coding / 長專案 | 先規劃 + Hierarchical + Worktrees | 隔離子代理、todo.md | 完整應用生成 + 除錯 |
| 開放式 / 創意型 | ReAct + Reflection + Self-evolution | Critic 關卡、版本化 prompts | 迭代式設計精煉 |
| 高風險 / 高可靠性 | 以上全部 + 強品質關卡 | 結構化結果、驗證 | 企業級自動化 |

## 5. 常見陷阱與緩解方法（來自研究）

**主要參考：請參閱上方新的第 1.4 節，其中包含完整 MASFT 風格分類法、失敗模式與對應階段的緩解策略。** 下列要點保留作快速掃描，並補充了近期研究中的其他模式。

- **上下文爆炸**：積極摘要 + 分層狀態（本地子記憶）。
- **無限迴圈 / 空轉**：硬性最大迭代數 + 在 todo 中追蹤進度 + 能強制重新規劃或升級處理的 critic。
- **彙整品質差**：強制使用結構化子結果 + 專門 harmonization/reporter 步驟。
- **計畫中的幻覺**：每個重大主張都必須 grounding 到 observation；在提交計畫前先跑 critic。
- **委派脆弱**：使用明確子任務 spec + success criteria；對返回結果進行驗證。
- **缺乏可見性**：完整 tracing + 可選 reasoning 串流。

## 6. 快速開始偽代碼骨架（類 Python）

```python
def agent_loop(task_instruction, tools, sub_agent_registry, max_steps=50):
    state = initialize_state(task_instruction)  # spec, plan, todo, memory, tracer
    orchestrator = get_llm(role="orchestrator")
    
    while not should_terminate(state, max_steps):
        # 1. Observe
        context = build_context(state)
        
        # 2. Reason + Decide
        decision = orchestrator.generate(
            prompt=build_decision_prompt(context, state.spec),
            output_schema=DECISION_SCHEMA  # thought, action_type, payload
        )
        
        if decision.action_type == "tool":
            obs = execute_tool(decision.payload, tools)
        elif decision.action_type == "delegate":
            sub_result = invoke_sub_agent(decision.payload, sub_agent_registry)  # runs its own loop
            obs = structured_observation_from(sub_result)
        elif decision.action_type == "synthesize":
            obs = consolidate_and_gate(state)
        elif decision.action_type == "finish":
            return finalize_output(state, decision)
        
        # 3. Update state
        state.history.append(decision.thought, decision, obs)
        state = update_todo_and_plan(state, obs)
        
        # 4. Optional light reflection or full self-evolution pass
        if should_reflect(state):
            state = reflect_and_evolve(state)  # critique + version updates
    
    return handle_termination(state)
```

子代理呼叫會以相同模式遞迴執行（只是範圍更窄）。

## 7. 參考文獻與來源

- **ReAct 基礎論文**：Yao 等，〈ReAct: Synergizing Reasoning and Acting in Language Models〉（arXiv:2210.03629，ICLR 2023）。
- **xAI 生產實作**：xAI Developer Docs（Multi-Agent 協作、伺服器端 agentic tool calling、Grok Build CLI 模式）— 以 leader synthesis 為核心的即時多代理研究；4/16 代理團隊。
- **分層式與進階方法**：
  - 〈AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool–Environment–Agent (TEA) Protocol〉（約 arXiv 2026）— 分層 planner、TEA protocols、透過 reflection/TextGrad 風格進行自我演化，在 GAIA 上有強勁成果。
  - 綜述：〈The Landscape of Emerging AI Agent Architectures...〉（2024）；〈Large Language Model Agent: A Survey...〉（2025）；〈LLM-based Agentic Reasoning Frameworks: A Survey〉（2025）。
- 其他模式：Reflexion（自我反思）、Plan-and-Execute 變體、LATS（樹狀搜尋）、MetaGPT / AgentVerse / DyLAN（多代理協作）。

---

**實作下一步**：
1. 先用你偏好的框架（LangGraph、自訂迴圈，或 xAI SDK）建立最小 ReAct harness。
2. 加入結構化 observation schema 與 todo/state 管理。
3. 疊加分層委派 + 彙整能力。
4. 裝設 tracing + quality gates。
5. 對重複出現的任務類型實驗 reflection/self-evolution。
6. 將 xAI multi-agent mode 整合到研究型子任務中。

本文件設計為**可直接執行的指引** — 你可以直接複用這些模式、改寫偽代碼並持續迭代。如果你想要更進一步的精煉、Python/Node 的具體程式碼範例，或與你既有 harness（例如 critic loops、由 spec 驅動的 task.md）整合，請提供你目前使用的技術棧細節。

**檔案建立於**：`/home/workdir/artifacts/agent_loop.md`
