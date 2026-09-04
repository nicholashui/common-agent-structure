# agent_loop_creator.md
**版本：** 2026-06-09 | **狀態：** 可直接投入實作的正式規格  
**用途：** 建構精煉版分層式 ReAct Agent Loop（如 `agent_loop.md` 所定義）的詳細且可執行實作指南。此文件已最佳化為程式撰寫代理的輸入（Grok Build、Claude Code、Cursor + xAI/DeepSeek、N1ch01as Architect harness 或同等工具）。內容整合了 MASFT taxonomy（arXiv:2503.13657）、AgentOrchestra/TEA Protocol（arXiv:2506.12508）、ReAct 增強方法（Reflexion、Prospector、ReflAct）、xAI 生產模式（grok-4.20-multi-agent 伺服器端協作、Grok Build CLI 子代理／先規劃後執行），以及 2025-2026 年 LLM agent 綜述研究的深度調研成果。  

**重新思考摘要（內部迭代 100 次）：**  
- **研究核心洞見**：約 42% 的 MAS 失敗源自**規格與設計問題**（MASFT）；另有約 21% 與驗證／終止有關。若沒有強健的 Phase 0 規格驗證、結構化觀察、明確的 `Done` + 多層 critic，以及進度追蹤，只是一味增加代理數量，往往只會帶來遞減甚至負面的效益。對長期任務而言，分層架構 + TEA 式版本化／自我演化可帶來極大增益（AgentOrchestra 在 GAIA 達 89%+）。  
- **xAI 對齊**：研究型子任務使用 `grok-4.20-multi-agent`（4/16 個代理、leader 綜合、具隱藏子狀態的伺服器端 ReAct）；在客戶端迴圈中模擬 Grok Build 模式（先顯式產生計畫、平行且隔離的子代理、todo 風格狀態）。此混合式方案可在能力、控制與成本效率之間取得最佳平衡。  
- **架構權衡已定案**：核心採自訂 Python 實作（Pydantic schema、嚴格 JSON 模式、完整 tracer），而非純 LangGraph，以獲得更好的透明性、可稽核性與教學價值（符合使用者的 harness 風格）。記憶體採混合策略（結構化 `todo.md` + 向量式長期記憶 + 積極摘要），遵循 TEA/MemGPT。自我演化採有界設計（受 TextGrad 啟發 + 在保留 trace 上驗證）以避免漂移。先維持最少依賴，再逐步加入可選 adapter。以本地優先、可觀測、沙箱化、經過生產級強化（熔斷器、重試、預算控管）為原則。Dogfood：這套 harness 應能協助建構並持續改善其自身。  
- **失敗模式覆蓋**：每個 MASFT 模式都已明確對應到特定階段／元件中的緩解機制（見第 3 節）。  
- **分階段建置**：MVP（可靠的平面式 ReAct）→ 分層委派 + 彙整 → TEA 版本化／演化 → xAI 混合整合 + 範例。每個階段都有明確的交付物、程式骨架與驗證關卡（critic 檢查點）。  
- **目標成果**：透過演化在複雜研究／程式撰寫基準上達成 >85% 成功率；在受控測試中將 MASFT 殘留失敗模式壓到 <5%；可由 trace 完整重播／除錯；能無縫整合至使用者的 Python/Node/xAI/DeepSeek/Cursor/Kiro/OpenWebUI 技術棧。  

這是一份**由規格驅動、可直接供 critic 使用的輸入文件**。程式撰寫代理應：解析各章節、逐模組產生程式碼、對輸出執行內部 critic／精煉迴圈，並在符合成功標準後才進入下一步。建置過程內部請採用 `task.md` / `todo.md` 風格。

---

## 1. 任務、成功標準與限制

### 主要目標
實作一套**受控、分層、受 ReAct 啟發的 agent loop 系統**，具備以下特性：
- 能可靠抵抗已知 MAS 失敗模式（MASFT 分類）。
- 可透過 TEA 啟發的版本化、追蹤與自我反思／TextGrad 式最佳化持續演進。
- 採混合式架構：客戶端完全掌控 + 可選擇將深度研究任務委派給 xAI 伺服器端多代理。
- 達到生產等級：可觀測、具成本意識、安全（沙箱化）、可測試、可擴充。
- 與使用者偏好一致：由規格驅動（可演進的 `TaskSpec`）、迭代式精煉／critic 迴圈、harness engineering、本地／最小 Docker、以 Python 為主且使用 Pydantic/JSON 契約，並為既有工具（xAI API、DeepSeek、Cursor/Kiro、自架服務）保留整合點。

### 可量測的成功標準（供 Coding Agent 驗證）
1. **可靠性**：在涵蓋全部 14 種 MASFT 模式的合成失敗注入測試中，緩解後殘留失敗率 <5%；可明確及早偵測規格／角色違規，循環偵測會觸發重新規劃／終止，驗證器會拒絕不完整或錯誤的 `Finish`。
2. **效能**：在保留的研究／程式任務集上（mini-GAIA 風格、網頁導航 + 綜整、多檔案程式碼生成 + 測試），基礎成功率 ≥70%；在相似任務分佈下進行 2-3 次自我演化後：成功率 ≥85%，且相較基線 ReAct 使用更少步數／token。
3. **可觀測性與可除錯性**：100% 的執行都會產生完整且可重播的 `Trace`（JSONL 或結構化格式），包含來源、版本、耗時、token 計數，以及 thought/action/obs tuple。支援視覺化（mermaid 匯出或 networkx 圖）與從任一步驟重播。
4. **可演化性（對齊 TEA）**：VersionManager 支援 register/rollback/select-best，用於 prompt、工具程式碼、agent 設定、子代理角色。SelfEvolver 可在保留 trace 上提出並驗證改善（TextGrad 風格）；在 3 次有界反思後能展示實質提升。
5. **混合式 xAI 整合**：可無縫將研究子任務委派給 `grok-4.20-multi-agent`（狹義子規格 + 啟用工具）；由 leader 綜整的結果帶著 provenance 整合回主軌跡。可選擇模擬 Grok Build 的先規劃後執行 + 平行子代理模式。
6. **生產級強化**：具備熔斷器（CLOSED/OPEN/HALF_OPEN 並有正確恢復）、指數退避重試、分階段 token／步數預算 + 提前退出、結構化錯誤觀察、沙箱化工具執行（受限 Python 或 subprocess 隔離）、輸入淨化、最小權限。
7. **對 Coding Agent／使用者的易用性**：提供乾淨的 Python 套件（`agent_loop/`）與 CLI（`python -m agent_loop.cli`），可選 FastAPI server mode，包含完整範例（研究代理、程式專案 harness、自我改進 meta-agent），具完整型別註記 + docstring，pytest 測試套件可通過，並附 MkDocs 或充實 README。
8. **整合性**：可透過 LiteLLM 或直接 client（xAI、DeepSeek、OpenAI-compatible）運作；可選 LangGraph adapter；可輸出結構化 plan/todo 供 Grok Build / Cursor 使用；若擴充到 server mode，也能相容於使用者的 OpenWebUI/Keycloak/Strapi 自架模式。

### 限制與非目標
- **語言／技術棧**：以 Python 3.11+ 為主（Pydantic v2、asyncio、httpx、dataclasses）。可選：chromadb/FAISS 作向量記憶，fastapi/uvicorn 作伺服器，langgraph 僅作 adapter。核心迴圈不得綁定重型框架。
- **先求精簡**：初期核心迴圈 + 狀態 + 可靠性 + 基本分層功能應控制在 <2k LOC。演化／xAI 混合功能於後續階段加入。
- **不得有失控迴圈**：必須設置硬性 `max_steps`、循環偵測（state hash）、基於進度的退出與熔斷器。所有 LLM 呼叫都需使用嚴格 output_schema（Pydantic/JSON mode 或受限解碼）。
- **安全性**：程式碼執行工具必須在沙箱中；絕不可盲信 LLM 生成的工具參數（須驗證 + 最小權限）；需監控異常模式（例如快速重複）。
- **成本控制**：token 預算、僅對獨立分支進行平行化、上下文壓力高時摘要、在符合條件時提早終止。
- **非目標（Phase 1-2）**：完整分散式執行（Ray/Celery 之後再說）、GUI dashboard（先 CLI + JSON 匯出）、原生多模態（先聚焦文字+程式碼；視覺由 xAI 或子代理處理）、生產級多租戶。

**活規格（Living Spec）**：`agent_loop_creator.md` 與 `agent_loop.md` 可由建置出的系統本身更新（對規格進行自我演化）。

---

## 2. 深度研究綜整與關鍵架構決策

### 2.1 MASFT 分類法（arXiv:2503.13657）— 主要失敗地圖
**「Why Do Multi-Agent LLM Systems Fail?」**（Cemri 等，2025；MAST-Data：來自 7 個框架的 1642 條 trace；14 種模式，人類 IAA κ=0.88；LLM judge o1 few-shot κ=0.77）。

**類別 1：系統設計問題（41.8% — 最大槓桿點）**
- FM-1.1 不遵守任務規格（11.8%）
- FM-1.2 不遵守角色規格（1.5%）
- FM-1.3 步驟重複（15.7%）
- FM-1.4 對話歷史遺失（2.8%）
- FM-1.5 未意識到終止條件（12.4%）

**類別 2：代理間失配（36.9%）**
- FM-2.1 對話重置（2.2%）
- FM-2.2 未提出澄清問題（6.8%）
- FM-2.3 任務偏離軌道（7.4%）
- FM-2.4 資訊隱匿（0.85%）
- FM-2.5 忽略其他代理輸入（1.9%）
- FM-2.6 推理與動作不一致（13.2%）

**類別 3：任務驗證與終止（21.3%）**
- FM-3.1 過早終止（6.2%）
- FM-3.2 無驗證或驗證不完整（8.2%）
- FM-3.3 錯誤驗證（9.1%）

**整合後的關鍵發現與緩解策略：**
- 設計／規格品質是最高 ROI。**Phase 0 為必須**：使用結構化 `TaskSpec`（Pydantic），明確包含 objective、success_criteria 清單、constraints（max_steps、budgets）、output_format、quality_gates。在迴圈開始前執行自動規格驗證器 + critic。委派時需有角色契約。
- 驗證即使在「成功」執行中也是弱點。**Phase 3 + 5**：設置專用 Verifier/Critic agent（嚴格 JSON：passes、score、issues、suggestions、confidence）。採多層驗證（底層 schema + 高層目標對齊）。明確的 `Done` 動作**必須**通過 verifier + 證據檢查。進度追蹤需包含（todo 完成百分比 + Thought 步驟中的條件對齊）。
- 上下文／歷史遺失與重複問題很常見。**Phase 1**：在上下文超過閾值時積極摘要，使用結構化狀態（`task.md` / `todo.md` + 只保留 key_facts，不做整段歷史傾倒），透過近期 action+obs hash（md5）進行循環偵測，並以 `max_steps` 硬上限 + 基於進度的提前退出控制。
- 代理間問題：使用強力中央 Orchestrator，明確進行分解／路由／契約管理 + 結構化交接 Observation schema（status、data、summary、confidence、issues、next_suggestions、provenance、trace_id）。針對每個工具／角色設置熔斷器。共享狀態採版本化。
- 論文中的介入方式（+9-15% 增益）：更好的 prompt／角色／拓撲 + 驗證區塊。我們的系統進一步加入**執行期關卡 + 演化**。

**Coding Agent 行動要求**：在 prompt 與 verifier 中明確引用這些模式（例如：「檢查是否違反 FM-1.1/1.5/3.1/3.2...」）。建立 failure_injection 測試套件，模擬各模式並斷言緩解機制有效。

### 2.2 AgentOrchestra + TEA Protocol（arXiv:2506.12508）
**「AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent (TEA) Protocol」**（Zhang 等，2025/2026）。GAIA Test 達 89.04%（在 Level 2/3 表現強勁），自我演化後進一步提升（驗證集 93.33%）。

**TEA 核心抽象（先實作最小版本）：**
- **Tool (TCP)**：一等公民、可版本化、具生命週期管理。註冊內容包含名稱、描述、schema（Pydantic/JSON）、程式碼／實作，以及供檢索使用的語意嵌入。支援動態生成（Tool Generator 子代理）。
- **Environment (ECP)**：觀察／動作空間與狀態一致性。（對我們而言：working_dir、檔案系統沙箱、程式執行狀態，若之後加入也可包括瀏覽器。）
- **Agent (ACP)**：角色、能力、metadata。支援分層、註冊、協作契約。支援 A2T/T2A 轉換（agent-as-tool 或 tool-as-agent，用於動態重配置 — Phase 4+）。

**需要實作的關鍵機制：**
- **Version Manager**：每個 prompt、工具程式碼、agent config、子代理角色、生成產物都要有 version + lineage（parent、timestamp、hash、metrics）。支援 register(new)、rollback(to_v)、select_best(metric)。
- **Tracer**：完整執行軌跡（step、thought、action_type、payload、observation、versions_used、token_usage、timings、sub_agent_id）。匯出 JSONL 供重播／除錯／反思。這能提供稽核與最佳化訊號。
- **Self-Evolution Module**：受 TextGrad 啟發 + 自我反思。
  1. 透過 Tracer 蒐集 trace。
  2. 診斷（LLM：root_cause、target_component，例如 `"planner_prompt_v3"`、proposed_edit）。
  3. 套用修改（對 prompt／工具程式碼做字串替換或結構化 patch）。
  4. 驗證（在保留 trace 或相似任務上重新執行；檢查成功率／步數／verifier score 是否提升）。
  5. 若符合改進標準：註冊新版本（含 provenance）。支援有界回合（`max_reflection_rounds`）。
- **Context Management**：以執行範圍 + 元件專屬為單位管理。為子代理提供 context slicing/provenance（絕不直接傾倒完整歷史）。使用語意檢索找回相關過往版本／知識。
- **Hierarchical Orchestration（AgentOrchestra 模式）**：中央 Planner（將 objective 拆解為依賴圖或編號步驟 + todo.md → 依狹義子規格 + context slice + success_criteria 路由給專家）。子代理執行自己的受控迴圈（或委派給 xAI）。結果向上回傳 → Consolidator（整合、去重、用交叉參照 + verifier 解決衝突）→ Reporter 輸出最終結構化結果。採樹狀路由 + 每個子代理擁有本地工具權限。任務失敗或方向偏移時重新規劃。

**Coding Agent 行動要求**：建立 `tea/` 模組，包含最小可行的 Protocol 類別／schema。將其用於註冊與上下文建構。讓 self_evolver.py 成為 Phase 4 的核心。Planner 需產生 `todo.md` 風格的結構化狀態（使用者偏好此模式）。

### 2.3 ReAct 基礎與增強
- **ReAct（Yao 等，ICLR 2023）**：Thought（推理軌跡）→ Action（tool/delegate/finish）→ Observation（具 grounding 的結果）迴圈。相較純 CoT 或純 action，在互動式任務上提升 10-34%。我們的核心做法：嚴格的結構化決策輸出（Pydantic：thought、action_type、payload），且 Observation 一律為結構化。
- **已納入的增強方法：**
  - **Reflexion**（Shinn 等）：對軌跡做語言式自我批判 → 產生改善計畫。用於輕量反思（每 N 步）與完整的 Phase 4。
  - **Prospector**（Kim 等）：Self-Asking + Trajectory Ranking。可選擇產生多條候選軌跡，再由 critic 排序並選擇最佳者。
  - **ReflAct**（近期）：在**推理步驟本身**加強 grounding（根據世界回饋重新修整推理）。需在 Thought prompt 中明確要求對照前一次 obs 與原始 objective 重新 grounding。
  - **Plan-and-Execute + LATS/MetaGPT 模式**：在迴圈前加入顯式高層計畫階段（Phase 0 可選）；在分層模式中可選擇以多個平行子分支加入 tree search 元素。
- **xAI 生產模式**：伺服器端 ReAct 迴圈（模型自行決定工具 → 內部執行 → 反覆迭代直到最終輸出）。多代理：即時平行專家 + leader 綜整（4 或 16 個代理，由 `reasoning.effort` 控制）。Grok Build：先規劃、平行子代理（隔離上下文／worktree）、結構化工作流、支援用 ACP 自訂協作。**我們的混合式方案**：客戶端 orchestrator 維護全域 state/trace/verifier；將研究型子問題委派給 xAI 多代理（狹義規格，接收綜整結果 + citation）；對程式任務則使用本地專家，或以隔離的 Python process/thread 和複製後的 state slice 模擬平行執行。

### 2.4 最終架構決策（100 次重新思考後）
- **迴圈風格**：以受控的自訂 ReAct（dataclass/Pydantic State + hash 循環偵測 + 熔斷器）為基礎。上層再疊加分層式架構（由 Orchestrator 決定 delegate、tool、synthesize 或 finish）。不採平面式多代理（根據研究，中央控制優於協調混亂）。
- **狀態**：`AgentState`（task_spec: TaskSpec、history: List[TraceEvent]、todo: List[TodoItem] 或 todo_md_content、plan: Optional[Plan]、memory_short: Summary + recent、memory_long: VectorStore + key_facts、versions: VersionRegistry、tracer: Tracer、budgets: Token/StepBudget、seen_hashes: set 用於循環偵測）。
- **記憶策略**：結構化 `todo.md` / key_facts（主要、低 token）+ 積極摘要（在上下文壓力或里程碑時）+ 可選向量庫（Chroma/FAISS）供語意檢索過往 trace／版本／知識。子代理僅取得**切片化上下文 + provenance**。
- **LLM 呼叫**：統一 client（支援 xAI direct、DeepSeek、OpenAI 相容介面，可透過 LiteLLM 或自訂）。所有呼叫皆使用：system + few-shot（研究任務偏密、embodied 任務偏疏）+ 嚴格 `output_schema`（Pydantic model_dump_json 或 JSON mode）。必須強制可解析。
- **工具**：帶驗證機制的 Registry。安全執行包裝器（熔斷 + 重試 + 結構化錯誤 obs）。code_execution 採沙箱（受限 globals 或 firejail/subprocess）。
- **xAI 混合細節**：為 `grok-4.20-multi-agent` 呼叫建立 `XAIClient` wrapper。payload 包含：狹義 sub_objective + success_criteria + enabled_tools 清單 + context_slice。解析 leader 最終答案 + 可選 reasoning。以特殊 Observation 記錄，包含 `source: "xai_multi_agent"`、`agent_count`、`synthesis_confidence`。
- **自我演化範圍（分階段）**：Phase 2+：prompt 與 verifier prompt。Phase 3+：工具程式碼（動態生成 + 驗證）。Phase 4：agent config／roles，甚至子規格生成啟發式。
- **Testing Dogfood**：建立可重播 MASFT 範例的 failure simulator；斷言緩解機制有效。開發期間使用這套 harness 在保留 trace 上改善自身的 prompt/verifier。
- **可擴充性**：可插拔的 LLM backend、Tool 類型、SubAgent 角色（registry + factory）、Memory backend、Evolution 策略。提供單次執行 CLI；提供 server mode（FastAPI）以支援多 session／與 OpenWebUI 風格前端整合。

**設計理由摘要**：此設計直接以 Phase 0 + 活 `TaskSpec` + critic 攻擊排名第一的失敗類別（規格／設計）。透過強制關卡 + 結構化 obs 補上驗證缺口。透過循環偵測 + 摘要 + 結構化狀態（使用者偏好的 todo.md 模式）防止迴圈失控與上下文腐化。再透過 TEA 式自我演化建立長期韌性。它運用 xAI 的強項，同時不放棄控制權，也符合使用者偏好的迭代式、規格驅動、生產級 harness 哲學。

---

## 3. 詳細系統架構與模組拆解

### 3.1 高層流程（來自 agent_loop.md 的強化版階段）
1. **Phase 0：初始化**
   - 解析指令 → 產生／驗證 `TaskSpec`（Pydantic：objective、success_criteria: List[str]、constraints: Dict、output_format、max_steps=50、token_budget=200k、quality_gates、initial_plan?）。
   - Spec Validator + Critic（LLM）：檢查完整性、歧義、角色清晰度、終止條件。若 FM-1.x 風險高則拒絕／修訂。
   - 建立 `AgentState`：task_spec、todo（由 plan 產生或為空）、memory、tracer、version_registry、budgets、seen_hashes=set()。
   - 可選：由 Planner LLM 產生高層 plan（編號步驟 + 相依關係）+ todo.md 內容。驗證 plan 是否符合 spec。
   - 決定架構：flat | hierarchical | hybrid_xai。

2. **Phase 1：核心受控 ReAct 迴圈**
   - 當尚未 terminate 時：
     - 建構上下文（若歷史過長則摘要 + key_facts + todo + task_spec + 最新 obs）。
     - LLM 決策（嚴格 schema）：`thought`（分析進度相對於 criteria、缺口、風險、策略；重新 grounding 到 objective）、`action_type`（"tool" | "delegate" | "synthesize" | "finish" | "reflect"）、`payload`（args 或 sub_spec）。
     - 循環檢查：對近期（action+obs）做 hash；若已看過 → 強制重新規劃或終止。
     - 執行：safe_tool（熔斷 + 重試 + 沙箱）或 safe_delegate（子迴圈或 xAI 呼叫）或內部動作。
     - 結構化 Observation：`{status, data, summary, confidence, issues, next_suggestions, provenance, trace_id, versions_used}`。
     - 將 TraceEvent 加入 history，並更新 todo／progress／memory。
     - 輕量反思（每 N 步或發生錯誤時）：快速自我批判並檢查對齊。
   - 對每個 tool_name／role 設置 CircuitBreaker（如附帶程式中的 CLOSED/OPEN/HALF_OPEN 邏輯；並追蹤 metrics）。
   - 終止訊號：success_criteria 達成 + verifier 通過、達到 max_steps/budget、明確且已驗證的 Finish、不可恢復失敗（升級處理），或在中間條件達成時提早退出。

3. **Phase 2：分層委派**
   - 由 Orchestrator（或 Planner）進行拆解 → 選擇／實例化專家（registry：Researcher、Coder、Verifier、Reporter、ToolGen、Browser、Analyzer...）。
   - 建立狹義 `SubTaskSpec`（部分 objective + success_criteria + context_slice + provenance）。
   - 呼叫子代理（自己的受控迴圈實例，或委派給 xAI 多代理）。
   - 子代理回傳 Structured Observation（附完整 sub_trace 摘要供稽核，向上冒泡）。
   - 父代理記錄、驗證／整合、更新全域 todo/plan，並決定下一步。

4. **Phase 3：彙整與品質關卡**
   - Aggregator 蒐集 observation 與 plan 進度。
   - Harmonizer/Reporter LLM：合併、去重、交叉參照、解決衝突（引用來源／版本），產出統一草稿。
   - Verifier/Critic：依 success_criteria 評分，檢查 hallucination／缺口／FM-3.x 問題，並提出修正建議。輸出為 JSON。
   - 若未通過關卡：觸發精煉（重新規劃特定分支、重新委派，或自我編修）。
   - 若通過：進入潤飾或最終輸出。

5. **Phase 4：反思與自我演化（進階）**
   - 在里程碑或結束時：將完整 trace 送至 SelfEvolver。
   - 診斷根因（具 MASFT 意識的 prompt）。
   - 提出有針對性的修改（prompt、工具程式碼、角色定義，甚至子規格啟發式）。
   - 在保留資料或 replay 上驗證改進。
   - 若更好則註冊新版本（由 VersionManager 保留 lineage）。
   - 採有界設計（`max_reflection_rounds=3`）。

6. **Phase 5：終止與輸出**
   - 依規格完成最終綜整 + 結構化輸出。
   - 持久化完整 trace + version + metrics。
   - 可選擇產生事後反思摘要。
   - 在高風險關卡或預算耗盡時提供 human-in-loop hook。

### 3.2 核心資料模型（Pydantic — 優先產生這些）
```python
from pydantic import BaseModel, Field
from typing import Literal, Optional, List, Dict, Any
from datetime import datetime
import hashlib

class TaskSpec(BaseModel):
    task_id: str
    objective: str
    success_criteria: List[str]
    constraints: Dict[str, Any] = Field(default_factory=dict)  # max_steps、token_budget 等
    output_format: str
    quality_gates: List[str] = Field(default_factory=list)
    initial_plan: Optional[List[str]] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class StructuredObservation(BaseModel):
    status: Literal["success", "partial", "failed", "error", "circuit_open"]
    data: Optional[Any] = None
    summary: str
    confidence: float = Field(ge=0.0, le=1.0)
    issues: List[str] = Field(default_factory=list)
    next_suggestions: List[str] = Field(default_factory=list)
    provenance: str  # 例如 "tool:web_search"、"sub_agent:researcher_v2" 或 "xai_multi:leader"
    trace_id: str
    versions_used: Dict[str, str] = Field(default_factory=dict)  # component -> version

class TraceEvent(BaseModel):
    step: int
    timestamp: datetime
    thought: str
    action_type: str
    payload: Dict[str, Any]
    observation: StructuredObservation
    token_usage: Optional[Dict[str, int]] = None
    versions: Dict[str, str] = Field(default_factory=dict)

class AgentState(BaseModel):
    task_spec: TaskSpec
    history: List[TraceEvent] = Field(default_factory=list)
    todo: List[str] = Field(default_factory=list)  # 或 todo_md: str
    plan: Optional[Dict[str, Any]] = None
    memory_short: Dict[str, Any] = Field(default_factory=dict)
    memory_long_ref: Optional[str] = None  # vector ids 或 summary
    seen_hashes: set = Field(default_factory=set)  # 用於循環偵測
    budgets: Dict[str, Any] = Field(default_factory=dict)
    versions: Dict[str, str] = Field(default_factory=dict)  # 目前啟用版本
    tracer: List[TraceEvent] = Field(default_factory=list)  # 或獨立的 Tracer 類別
```

（實際程式中還需擴充 VersionedComponent、Plan、TodoItem、CircuitBreakerState 等。）

### 3.3 需實作的關鍵模組（基於附帶骨架並加強）
- **core/loop.py**：`controlled_react_loop`（在附帶程式基礎上加入 Pydantic、完整狀態、具 MASFT 意識的 prompt、xAI 混合 hook、進度追蹤）。
- **reliability/circuit_breaker.py**：強化版類別，具 metrics、每個工具／角色獨立實例，並整合到 safe_execute。
- **reliability/verifier.py**：`verify_output` + `VERIFIER_PROMPT`，需調校以抓出 FM-1.x/2.x/3.x（例如：「是否遵守原始 task_spec 與角色？是否有過早終止或驗證不完整？請對照 observation 交叉檢查各項主張。」）。
- **hierarchical/orchestrator.py**：Planner 邏輯、委派路由、子代理工廠、consolidator。
- **evolution/self_evolver.py**：`self_evolve_component`（TextGrad 風格：由 trace 診斷、提出修改、驗證改善、VersionManager.register）。
- **tea/protocol.py**：最小 TCP/ECP/ACP schema、register_tool/register_agent、get_context_slice、VersionManager。
- **integrations/xai.py**：`call_grok_multi_agent(sub_spec, tools_enabled, context_slice)` → 將 leader 結果解析成 StructuredObservation。
- **memory/ 與 tracing/**：依上述設計實作。
- **prompts/**：版本化 JSON/YAML 或 .md 檔案，存放 system prompt、few-shot（ReAct decision、verifier、planner、reflector、sub-roles）。在 critic prompt 中納入 MASFT 失敗模式參照。

**熔斷器強化**（以附帶實作為基礎；新增 metrics 匯出與 tracer 整合）。

**自我演化範例骨架**（精煉附帶版本）：
```python
def self_evolve_component(component_name: str, trace: List[TraceEvent], llm, version_manager, held_out_traces: List = None):
    diagnosis = llm.generate(  # 具 MASFT 意識的 prompt
        f"分析此 trace 的根因（參考 MASFT 模式 FM-1.x 到 FM-3.x）。找出 target_component 與具體 proposed_edit（prompt 字串 patch 或 code diff）：\n{trace}",
        output_schema={"root_cause": str, "target_component": str, "proposed_edit": str, "expected_improvement": str}
    )
    if diagnosis.target_component == component_name:
        new_version = apply_structured_edit(component_name, diagnosis.proposed_edit)  # 安全 patch
        if validate_improvement(new_version, trace, held_out_traces or replay_subset(trace)):
            version_manager.register(new_version, parent=component_name, metrics=compute_metrics(new_version))
            return new_version
    return None
```

### 3.4 xAI 混合整合點
- 在 decision payload 或 orchestrator 中：若 action_type == "delegate_research" 或子規格複雜度偏高 → 改呼叫 call_xai_multi_agent，而非本地子迴圈。
- 設定：`enable_xai_hybrid=True`、`xai_research_threshold=0.7`（或在 spec 中顯式指定）。
- Logging：必須始終記錄 `source`、`agent_count`（來自 reasoning.effort），若有提供也要記錄 leader confidence。
- Fallback：若 xAI 呼叫失敗／熔斷器開啟 → 回退到本地子代理或直接使用工具。
- Grok Build 模擬（可選，Phase 3）：提供 plan/todo 匯出；對獨立分支用 asyncio.gather + 隔離狀態副本支援「parallel sub-agents」。

---

## 4. 給 Coding Agent 的分階段實作路線圖

**Phase 0（基礎建設 — 約 1-2 天工作量）**：建立專案骨架、Pydantic 模型（TaskSpec、StructuredObservation、TraceEvent、AgentState、VersionedComponent）、基礎 LLM client wrapper（xAI + fallback）、嚴格 JSON schema enforcement helper，以及一個在 mock LLM/tools 下可正常執行且不崩潰的簡易 ReAct loop skeleton。  
**驗證關卡**：在玩具任務（搜尋 + 摘要）上執行 10 步；始終產生合法的結構化 obs；對注入的重複行為能觸發循環偵測；spec validation 能抓出明顯的 FM-1.1/1.5 問題。

**Phase 1（受控核心 — 核心可靠性）**：完成完整的 controlled_react_loop，包含循環偵測、CircuitBreaker（完整狀態 + metrics）、safe_execute/safe_invoke、進度追蹤（todo 百分比 + Thought 中對 criteria 的對齊）、輕量反思、明確 Finish + 基礎 verifier 關卡、結構化狀態（todo list + key_facts）、積極上下文摘要。並以 MASFT 意識強化 prompt。加入基本 Tracer（append-only JSONL）。  
**驗證關卡**：FM-1.3（重複）、FM-1.4/2.1（模擬歷史遺失）、FM-3.1/3.2（過早／不完整）等 failure injection 測試通過。Verifier 能拒絕錯誤的 Finish 嘗試。token 用量會被記錄。不得出現無限迴圈。

**Phase 2（分層 + 彙整）**：建立 Orchestrator + SubAgentRegistry（可插拔角色，具狹義規格 + 契約）。完成委派路徑（本地子迴圈）。建立 Consolidator + Reporter（整合 + 結構化輸出）。加入多層 Verifier（schema + objective alignment + MASFT 檢查）。可選的 plan generation 階段。支援 context slicing + provenance。  
**驗證關卡**：在多步研究／程式任務上完成端到端委派；子結果能正確向上回傳並整合；衝突能被解決或標示；整體 success criteria 由 verifier 確認。

**Phase 3（TEA 版本化 + 基本演化 + xAI 混合）**：建立 VersionManager（支援 prompt/tool/role 的 register/rollback）。完成最小 TEA protocol schema + registration。實作 SelfEvolver（diagnose → propose → validate on held-out → commit）。整合 xAI 多代理 client（供研究子任務呼叫；結果以特殊 obs 形式整合）。在 planner 中加入基本 todo.md 生成。  
**驗證關卡**：在 3 個相似任務上的自我演化能顯示可量測改善（success/steps/verifier_score）。xAI 委派可端到端運作（研究子任務會回傳含 citation 的綜整結果）。可查詢版本歷史。

**Phase 4（潤飾、範例、生產化、Dogfood）**：提供完整範例（使用 xAI 混合 + 本地工具的 Deep Research Agent；具 plan/todo + 子代理分工的 Coding Project Agent，涵蓋 research/analyze/code/test/verify；可自我演化 verifier/prompts 的 Self-Improving Harness）。建立沙箱化 code tool。提供 CLI + 可選 FastAPI server。完整測試套件（unit + integration + failure_injection + mini-benchmark）。可觀測性匯出（mermaid trace viz、replay function）。在 tracer 中提供成本／token dashboard。文件化（README 含 quickstart、架構圖、MASFT 對應）。Dogfood：使用已建系統在保留 trace 上精煉自身 prompt/verifier，並透過 VersionManager 提交改善。  
**驗證關卡**：全部成功標準達成或超越。Coding agent 可乾淨跑完整個測試套件。使用者可直接拿 `agent_loop/` 套件穩定執行複雜任務。自我演化可明確改善某個保留元件。

**Coding Agent 建置流程**：每完成一個 phase/module，就執行：產生程式碼 → 執行內部 critic（可沿用 verifier 邏輯或獨立 reflection prompt）→ 修正問題 → 依關卡標準重新驗證 → 再往下進行。內部持續維護 `build_task.md` / `todo.md`。所有過程都記錄到 tracer，供之後讓 builder 本身進行自我演化。

---

## 5. 生產級強化、安全性、可觀測性與可擴充性

- **可靠性**：熔斷器 + 重試 + backoff（依附帶的 safe_* wrapper 模式）。永遠產生結構化錯誤 obs。預算強制執行 + 優雅降級。基於進度的提前退出。
- **安全性**：工具沙箱（受限 Python exec，或對 code_execution 使用隔離 subprocess/Docker；瀏覽器工具透過受控函式庫）。所有 LLM 生成參數在執行前都必須驗證／淨化。工具存取遵循最小權限。對迴圈模式做異常偵測（例如快速重複同一 action → 熔斷器開啟 + 告警）。
- **可觀測性**：Tracer 為一等公民。每個事件都可記錄：完整上下文快照（可配置）、version、token 計數、耗時、sub-call。支援匯出 JSONL / Parquet。重播函式：`replay_trace(trace_id, from_step=5)`。可選 OpenTelemetry 匯出或整合使用者的 Jenkins/OpenWebUI logging。
- **成本／可擴展性**：依 phase 設置預算。僅平行化獨立分支（asyncio）。以 context 長度 + 語意重要性作為摘要訊號。並行時需做 session 隔離。
- **可擴充性**： 
  - LLM backend 透過抽象 client 或 LiteLLM。
  - Tools：簡單 registry + Pydantic schema 驗證。
  - Sub-agents：factory + registry 中的角色 prompt。
  - Memory：可插拔（in-memory dict、vector store、persistent DB）。
  - Evolution strategies：可將 TextGrad 換成其他方法（例如僅用 Reflexion）。
  - Adapters：LangGraph state machine wrapper；匯出到 Grok Build ACP/MCP skills；提供 FastAPI endpoint 供遠端協作調度。
- **部署**：`pyproject.toml` 以 optional deps 管理。Docker 保持精簡（Python + venv）。預設本地優先。若需要多使用者／整合，可開啟 server mode（延續使用者技術棧中的 Keycloak OIDC-ready 模式）。

---

## 6. 測試與驗證策略（對 Coding Agent 至關重要）

1. **單元測試**：schema validation、cycle hash 正確性、CircuitBreaker 狀態機（測試所有狀態轉移，包含 HALF_OPEN 恢復）、Verifier JSON parsing 與邊界情況邏輯。
2. **整合測試**：在玩具任務上跑完整迴圈（事實查找、多步驟計算、簡單程式生成）。分層委派端到端。xAI 混合模式（mock 或實際但受預算限制的呼叫）。
3. **Failure Injection（MASFT 覆蓋）**：建立 simulator 強制觸發 FM-1.1（模糊規格）、FM-1.3（重複動作）、FM-1.5（忽略完成條件）、FM-2.6（不匹配）、FM-3.1/3.2/3.3（不良終止／驗證）。斷言：可及早偵測、採取正確緩解（重新規劃、verifier 拒絕、升級處理），且不得默默失敗。
4. **Benchmark**：建立迷你測試集（網路研究 + 綜整、多檔案程式專案含測試、GAIA 風格的事實 + 推理任務）。衡量成功率、效率（步數／token）、演化增益（3 回合前後）。
5. **Property-Based（Hypothesis）**：對隨機合法／非法 TaskSpec/obs 斷言不變條件（永遠輸出結構化資料、confidence 不得為 NaN、必須遵守 budget、version 一致）。
6. **Dogfood/Evolution Test**：使用真實 trace 對 verifier 或 planner prompt 執行自我演化；驗證改進版本在保留資料集上的分數較高，且不會讓基線任務退化。

**Coding Agent 強制要求**：在相關測試通過前，不得宣告某個階段完成。請在撰寫程式的同時產生測試。

---

## 7. 參考文獻與來源（深度研究）

- **MASFT/MAST**：Cemri 等，"Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657（2025）。MAST-Data、14 種模式、設計問題占主導（41.8%）、LLM judge、介入方法。GitHub：multi-agent-systems-failure-taxonomy/MAST。
- **AgentOrchestra/TEA**：Zhang 等，"AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool–Environment–Agent (TEA) Protocol" arXiv:2506.12508（2025/2026）。GAIA 89.04%、分層 planner + specialists、自我演化（TextGrad + reflection）、版本化、生命週期、protocols（TCP/ECP/ACP）、轉換機制。
- **ReAct**：Yao 等，arXiv:2210.03629（ICLR 2023）。
- **增強方法**：Reflexion（arXiv:2303.11366）、Prospector（Self-Asking + Ranking）、ReflAct（grounded reasoning）、Plan-and-Execute、LATS、MetaGPT、ReST meets ReAct。
- **綜述**："Large Language Model Agent: A Survey on Methodology, Applications and Challenges" arXiv:2503.21460（2025）；以及其他 2025-2026 的 agent 架構綜述。
- **xAI 生產模式**：docs.x.ai — grok-4.20-multi-agent（伺服器端 ReAct、4/16 代理、leader 綜整、內建工具、以 reasoning.effort 控制代理數量）；Grok Build CLI（先規劃、平行子代理、本地／agentic coding、ACP 支援）。屬於伺服器端 agentic tool calling 模式。
- **原始規格**：`agent_loop.md`（Hierarchical ReAct、生產模式、circuit breaker 程式碼、verifier/self-evolve 骨架）。

所有模式皆已綜合整理，以追求最大化的可靠性、可演化性，並同時對齊研究成果、xAI 能力與使用者的工程風格。

---

## 8. 交接與 Coding Agent 的立即下一步

**這份規格已完整且可執行。** 請**立即**從 Phase 0 骨架 + 核心模型開始實作（先產生 Pydantic 類別 — 它們就是契約）。 

**建議給 Coding Agent 的第一個 Prompt（可直接複製貼上）**：
"完整閱讀 `agent_loop_creator.md` 與 `agent_loop.md`。建立 `agent_loop/` Python 套件骨架，包含 pyproject.toml、核心 Pydantic 模型（TaskSpec、StructuredObservation 等）、基礎 LLM client，以及一個可運作的最小 controlled ReAct loop，並通過 Phase 0/1 的驗證關卡。使用嚴格 JSON schema。加入針對 MASFT 模式的初始 failure_injection 測試骨架。在工作過程中維護 todo.md，並對每個生成模組執行 critic/refinement。"

在核心迴圈穩定後，依階段逐步推進。於 Phase 4 的 dogfood 階段，使用建置出的系統協助其自身 prompt 與 verifier 的演化。

**預期交付物**：完整可用、已測試、已文件化的 `agent_loop/` 套件 + 範例 + CLI，讓使用者（或更高層的 meta-agent）可匯入／執行可靠的分層式 agent workflow，並具備清楚的 xAI 混合、自訂工具與自我演化擴充點。

**需進一步釐清的問題（若實作前需要）**：預期不需要 — 此規格已自洽完整。若建置過程中出現歧義，應透過內部 critic 解決，或帶著具體 trace 升級處理。

至此，深度研究 + 實作規格文件已完成。請以生產級標準建置它，搭配 critics 持續迭代，並使其成為進階 agent harness 的核心基石。

**本檔案已建立供交接給 coding agent。** 可立即執行。
