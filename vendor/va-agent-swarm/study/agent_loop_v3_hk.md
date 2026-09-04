# 精煉版 Agent Loop：分層式、受 ReAct 啟發、生產級設計

**版本：** 2026-06-10（v3 — 認知增強版：整合 `thinking_model.md` 的優先採用排序分析中高優先的人類傳統思考模型（Cynefin、Premortem、AAR、Double-Loop Learning、RPD、Dual Process、Metacognition、5 Whys/Fishbone、Red Team、Paul-Elder 等），用於自適應情境路由、行動前風險緩解、快／慢思考路徑、結構化反思與更深層的自我演化。完整保留 v2 的所有細節；新增機制皆為可疊加、可配置，並映射到既有階段。）  
**研究來源**：〈Why Do Multi-Agent LLM Systems Fail?〉（MASFT taxonomy，14-18 種失敗模式）、Reflexion、Prospector、CGI、記憶體相關論文、xAI 文件、開發者對無限迴圈／上下文問題的報告，以及對 40+ 種人類認知框架的系統性審視（依 agent loop 採用優先度排序）。  
**用途：** 一份可執行的參考文件，用於建構可靠、可擴展、以 LLM 為基礎的 agent 系統。結合學術基礎（ReAct 中推理 + 行動的協同效應）、xAI 的伺服器端 agentic 實作（面向深度研究的多代理協作）、以及進階分層模式（planner + specialists + 自我演化）。  
**目標讀者：** harness、多代理系統、coding agents、research agents 的建構者（例如帶 critic／自我精煉迴圈的 N1ch01as 風格 Architect）。  
**核心原則：** 受控迴圈，具備明確狀態、結構化輸出、品質關卡與分層委派。不是失控的連鎖反應，而是帶有向上彙整與刻意綜合的受管理協作。

## 1. 核心原則（根據研究精煉）

### 1.1 基礎：ReAct 範式（Yao 等，ICLR 2023）
- **定義**：交錯進行**語言推理軌跡（Thoughts）**與**行動（actions）**（工具呼叫、環境互動或委派）。行動的 observation 會為推理提供 grounding 並更新推理。
- **它為何有效：**
  - 純 Chain-of-Thought（CoT）：靜態，容易產生幻覺與錯誤傳播（缺乏外部 grounding）。
  - 純行動：缺少高層規劃、例外處理能力差、軌跡效率低。
  - **ReAct 協同效應**：Thought 拆解目標、追蹤進度、處理例外並重新規劃。Action 提供真實 observation，可修正推理並支持適應性調整。使互動式任務提升 10-34%，並降低知識型任務中的幻覺。
- **基本循環**（單次迭代）：
  1. **Thought**：LLM 針對當前狀態、目標、進度、下一步或例外狀況進行推理。（內部步驟，會更新上下文。）
  2. **Action**：決定並輸出可執行步驟（含參數的工具呼叫、子代理委派，或 `Finish`/`Done`）。
  3. **Observation**：環境／工具／子代理回傳結構化結果（資料 + metadata：status、confidence、summary、issues）。
  4. 附加到歷史／狀態 → 重複。
- **Prompt 結構**（few-shot 範例非常重要）：對推理密集任務（QA/research）使用較密集的 thoughts；對 embodied/decision 任務使用較稀疏的 thoughts。使用明確標籤或 JSON schema 以確保可解析。
- **例外處理**：Thought 步驟偵測失敗（「Nothing useful returned」）→ 在下一次迭代重新規劃或調整 action。

**xAI 對齊方式**：Grok 的伺服器端 agentic tool calling 在內部實作了生產級的 ReAct 風格迴圈。模型自行決定工具、在伺服器端執行（web_search、x_search、code_execution、collections_search），反覆迭代直到能產生最終答案。客戶端只會看到最終輸出（或串流輸出）+ 可選的 reasoning tokens。

### 1.2 生產級 xAI 多代理協作（2026）
- **grok-4.20-multi-agent**（或等效模型）：可啟動可配置的團隊（4 個代理用於快速／聚焦；16 個代理用於深入／全面）。
- **迴圈如何運作**：
  - 伺服器端**即時協作**：多個專門代理平行運作。
  - 每個代理都提供推理、工具呼叫與發現。
  - **Leader agent** 綜合討論內容、交叉參照並輸出最終結構化答案。
  - 基於中間發現進行平行工具呼叫與迭代。
  - 子代理內部狀態預設加密／隱藏（控制 + 安全）；只有 leader 輸出 +（可選）加密內容對外可見。
- **優勢**：深度多步研究、結構化輸出（表格、比較）、即時精煉，以及在無需客戶端介入迴圈的情況下自動使用工具。
- **先規劃元素**：xAI 工具（如 Grok Build CLI）中的互補模式：先顯式產生計畫，然後平行執行子代理（例如在隔離的 Git worktree 中最多 8 個子代理）。

### 1.3 分層式 + 可自我演化（AgentOrchestra / 2025-2026 綜述）
- 置於最上層的**中央 Planner / Orchestrator / Supervisor**。
- 將任務拆解為子任務 → 委派給**專門子代理**（Deep Researcher、Analyzer、Browser/Tool agents、Reporter 等）。
- 每個子代理執行其**自己的迴圈**（ReAct 風格或領域最佳化版本）。
- **樹狀路由** + 結果向上冒泡。
- **TEA Protocol 啟發**（Tool-Environment-Agent）：將工具、環境與代理視為一等公民、可版本化、具生命週期管理的實體，並以標準化協議處理上下文、呼叫與演化。
- **閉環回饋／自我演化**：
  - Reflection（對 trace 進行語言式自我批判）。
  - 基於 trace 的最佳化（例如 TextGrad 風格：attribute errors → propose edits → validate on held-out → version/register）。
  - Version manager：註冊改進後的 prompts/tools/agents；支援 rollback／選最佳版本。
  - Tracer：完整執行軌跡（可稽核性 + 最佳化訊號）。
- **彙整**：Planner 聚合子結果、協調證據、解決衝突、更新全域 plan/state，或觸發精煉。最終綜合通常由專門的 Reporter agent 處理，並負責 citations／去重。
- **效能證據**：AgentOrchestra 風格系統在 GAIA benchmark 可達 89%+；子代理 + 自我演化可帶來雙位數提升；相較平面式多代理，分層路由更具擴展性。

**整體精煉模型**：先從 ReAct 核心迴圈開始。面對複雜度時疊加分層委派。加入顯式規劃階段 + reflection/critique 關卡 + 結構化狀態／版本管理，以達生產級可靠性。xAI 已展示此模式可在伺服器端，透過強大的協作原語穩定運行。

### 1.4 來自排序後人類思考模型的認知架構增強（v3 新增）

為了進一步強化迴圈對第 1.5 節所述失敗模式的抵抗力，v3 明確納入高採用優先度的人類傳統思考模型（依同伴文件 `thinking_model.md` 中針對 agent loop 的採用優先度排序 — 內含 40 種模型的完整表格：各自階段、相似度、優勢與分數）。這些模型在 v3 中以一等機制的形式融入，而非事後補丁，從而帶來**自適應智能**（情境感知路由）、**主動韌性**（行動前風險）、**高效認知**（快／慢路徑），以及**更深層的組織式學習**（雙迴圈 + 結構化反思）。高分優先模型（9–10）會被最深度整合；其餘模型則用於加強特定子元件（verifier、ideation、harmonization）。

**v3 迴圈中的關鍵映射與操作化**：

| 思考模型（排名／分數） | 主要整合點 | 如何操作化（v3 增強） | 相對於 v2 基線的主要收益 |
|-------------------------------|---------------------------|--------------------------------------|----------------------------|
| **Cynefin Framework**（1 / 10） | Phase 0（規格之後）+ Phase 1 進入／重新規劃決策 | 將任務情境分類為：Simple（因果清晰）／Complicated（需專家分析）／Complex（具湧現性）／Chaotic（危機）。動態配置迴圈參數：對 Simple/Complicated 啟用 Fast Recognition Path + 較輕量關卡；對 Complex/Chaotic 強制 Full 審慎模式 + 更重的反思／critics + 更深診斷。 | 讓迴圈強度可自適應（Fast vs Full）— 在效率 + 可靠性方面槓桿最高的加成。 |
| **Premortem Analysis**（2 / 10） | Phase 0（計畫生成後、狀態提交前） | 強制執行「假設 6-12 個月後發生災難性失敗 → 倒推找出主要原因／風險 → 在 living spec、success criteria、todo items 或 agent roles 中顯式緩解」。可由 orchestrator LLM 或專用 Red Team critic 執行。 | 以行動前風險模擬與 critic 直接強化 Phase 0 規劃；成本近乎為零。 |
| **After-Action Review（AAR）**（3 / 10） | Phase 4（每個里程碑反思或終止） | 結構化四問模板：(1) 原本應發生什麼？（對照原始 spec/plan）(2) 實際發生什麼？（來自 tracer/obs）(3) 為什麼？（診斷）(4) 下一步？（教訓 → 具體演化行動）。作為自我演化輸入。 | 是 Phase 4 反思 + 自我演化的完美升級；結構化學習極其實用。 |
| **Double-Loop Learning**（4 / 9.5） | Phase 4（AAR 的單迴圈修正之後） | 在戰術修正後，顯式詢問：「哪些支配變數／假設（prompt templates、success criteria 定義、agent role 邊界、memory schema、verification thresholds，甚至 task decomposition 策略）導致我們走到這一步？是否應在 meta 層面更改？」只有在此之後才提交版本化更新。 | 讓自我演化真正強大（雙迴圈），避免只做症狀修補。 |
| **Recognition-Primed Decision（RPD）**（5 / 9.5）+ **Dual Process Theory（System 1 & 2）**（8 / 9） | Phase 1（Thought/Decide 步驟）+ Memory 層 | **Fast Recognition Path（新增）**：在進入冗長 ReAct 前，先查詢 Pattern Store（長期記憶中成功且高品質 trace + outcome metadata + embeddings）。如果相似度強（且 Cynefin 情境允許），就做輕量心智模擬（「與 trace #47 類似，預期用 action Z 可得到好結果」）後，以極少 token 直接行動。System 1 = fast/intuitive/RPD（適用於例行／專家任務）；System 2 = slow/deliberate（適用於新穎／高風險／不確定情境）。由下方 Metacognition 決定切換。低信心則回退到 full loop。 | 為專家領域／重複任務提供高價值 Fast Recognition Path；是自適應快／慢思考的基礎。 |
| **Metacognition Cycle**（7 / 9） | 與所有 Phase 1 迭代並行的輕量流程 | 持續進行：Planning（意圖對齊 spec）→ Monitoring（偏誤偵測、Cynefin 情境適配、todo/success criteria 進度、confidence 漂移）→ Evaluating（快速嚴謹度脈搏檢查）→ Adjust（即時或在下一次決策時觸發模式切換、提前重新規劃或提升關卡）。 | 與狀態管理高度平行；很容易以輕量 meta-prompt 或獨立小型 LLM 呼叫落地。 |
| **5 Whys + Ishikawa Fishbone + Fault Tree**（6 / 9） | Phase 4（AAR 的「Why?」診斷）+ Verifier/Critic 問題分析 | 在持續失敗或低信心 observation 時：用 5 Whys 逐層深挖；用 Fishbone（People/Prompts、Process/Methods、Models/Tools、Data/Material、Environment/Context、Metrics）或簡單 fault tree 對根因分類。結果用於驅動 Double-Loop 變更與 spec 加固。 | 對複雜問題提供更強的 Thought + Reflection；系統化、可視化且深入的因果分析。 |
| **Red Team Thinking**（12 / 8） | Verifier / Phase 3 品質關卡 + Premortem | 專用 critic 模式或獨立輕量 agent：「以對抗方式攻擊此 plan/draft/output，找出隱藏弱點、邊界情況或單點失效。」補充標準 verifier schema。 | 內建強力 devil’s advocate；很容易以專用 critic agent 角色落地。 |
| **Paul-Elder Critical Thinking Framework**（9 / 8.5） | Verifier prompt + Thought 步驟增強 | 以 Thought 要素（purpose、question at issue、information、concepts、assumptions、inferences、implications、point of view）+ 智識標準檢查表（clarity、accuracy、precision、relevance、depth、breadth、logic、significance、fairness、sufficiency）強化 `verify_output` 與 decision prompts。 | 顯著提升 Thought 與 Verifier 的品質；強力偏誤與嚴謹度偵測。 |
| **Theory of Constraints（TOC）**（10 / 8.5）+ **TRIZ**（14 / 8） | Phase 3（Harmonize/Consolidation）+ 自我演化中的衝突解決 | 當子結果互相衝突或目標矛盾：用 TOC Evaporating Cloud 揭示並解決核心矛盾；用 TRIZ 矛盾原則產生創新解法。輸出回饋到版本化 prompt/agent edits。 | 對矛盾目標的解決能力強；與 TRIZ、自我演化高度協同。 |
| **Six Thinking Hats**（13 / 8）+ **SCAMPER / Osborn-Parnes CPS**（15/11） | Phase 3 彙整或創意子代理 ideation | 可選的多視角檢查（White=事實/資料、Red=直覺/情緒、Black=風險/批判、Yellow=收益/機會、Green=創意/替代、Blue=流程/元認知）或 SCAMPER 檢查表（Substitute/Combine/Adapt/Modify/Put to other uses/Eliminate/Reverse），用於綜合或面向創意寫作／設計的子代理。 | 有效減少盲點；直接升級 ideation 與創意子代理。 |

**其他實作細節（v3）**：
- **記憶體架構升級**：新增「Pattern Store」（成功／失敗 traces 的向量 + outcome 分數等 metadata），以支援 RPD 的快速匹配。分層記憶體現在也會顯式為 traces 標記 Cynefin 情境類型，以提升檢索品質。
- **Verifier / Critic 增強**：`verify_output` 現在接受 `critic_mode`（或以 ensemble 方式執行）：`"standard"` | `"red_team"` | `"paul_elder"` | `"six_hats"`。回傳聚合後的 issues + suggestions。可並行以提升深度。
- **Task Spec 的可配置性**：新增欄位，例如 `"cognitive_profile": {"enable_fast_path": true, "reflection_style": "aar_double_loop_5whys", "critic_modes": ["red_team", "paul_elder"], "cynefin_classification": "complex"}`，亦可自動偵測。
- **Metacognition 實作**：每 N 步或在信心下降／情境改變時，執行輕量並行 prompt 或小型 LLM 呼叫。更新共享狀態旗標（例如 `current_mode: "fast" | "full"`、`bias_flags: [...]`）。
- **提前退出／效率**：Cynefin + RPD + Metacognition 的組合，能在對已掌握的子問題採取安全的提前終止或 fast-path，而不犧牲難題部分的嚴格關卡，直接降低 token 浪費與無限迴圈風險。

這些新增機制以**生產環境**為前提：所有新步驟皆有界、可版本化、會被 tracer 記錄，並可依任務切換或限制深度。它們讓 agent 從 v2 的強 ReAct／分層引擎，進一步成為更完整的認知系統：能反思自己的思考、預判失敗、在多個層面學習，並依情境調整審慎風格 — 同時完整保留 v2 的所有機制、程式碼範例與緩解策略。

### 1.5 已知問題、失敗模式與對應緩解方法（有研究支持）

近期系統性研究（尤其是基於熱門多代理框架 150+ 條 trace 分析所得的 **MASFT taxonomy**）指出，**大多數失敗來自設計／規格問題（約 40%+）**、協調失效，以及薄弱的驗證／終止控制，**而不是模型本身的原始智能不足**。單代理 ReAct 迴圈也會面對相似問題，並額外承受上下文膨脹與重複行為。以下整理出最常見、已有充分記錄的問題類型，並將**可執行的緩解方法**直接對應到本文件的各個階段。

### 主要問題類別與頻率／重要性
1. **規格與設計歧義（最大類別）**
   - 不遵守或誤解任務規格、角色模糊、缺少成功標準或輸出契約。
   - **影響**：代理很早偏離方向；錯誤在下游持續放大。
   - **緩解方法**：
     - Phase 0：強制使用結構化 Task Specification，明確 success criteria、constraints、output schema 與 quality thresholds。使用可更新的「living spec」。
     - 在迴圈開始前加入自動 spec validation（critic 或 schema check）。
     - 為 orchestrator 與子代理之間建立清楚角色定義與資訊契約。

2. **無限迴圈、重複動作與空轉**
   - 代理重複相同（或相似）動作卻沒有進展；在 ReAct 中很常見，通常源自例外處理差或資訊不足，也可能被 prompt injection 誘發。
   - **影響**：浪費 tokens／成本、timeouts、挫折（真實世界常見抱怨）。
   - **緩解方法**：
     - Phase 1：加入**循環偵測**（對近期 actions + observations 進行 state hashing；若相似度 > 閾值，強制重新規劃或終止）。
     - 明確設置 `max_steps`、`max_reflection_rounds`，以及基於進度的提前退出（例如 todo 完成百分比）。
     - 有界 reflection：限制「improve this」類迭代次數。
     - `Done` / `Finish` 工具：接受前必須通過強制驗證。
     - 分層模式中：Orchestrator 監控子代理進度，必要時終止／重新分派卡住分支。

3. **Context Window 爆炸 / Context Rot / 歷史膨脹**
   - 長軌跡導致早期關鍵資訊或指令被擠出上下文，造成不一致、重複與目標漂移。
   - **影響**：長時間或多輪任務的表現下降。
   - **緩解方法**：
     - 積極分層記憶體：短期工作記憶 + 長期持久儲存（vector search、semantic caching、MemGPT 風格）。
     - 在里程碑或上下文 > 閾值時做摘要（signal-aware truncation）。
     - 使用結構化狀態（`task.md`、todo list、僅保留 key facts），而不是每輪傾倒完整歷史。
     - 子代理只接收相關 context slices + provenance。

4. **幻覺、錯誤累積與驗證薄弱**
   - 虛構事實、誤解工具結果，或未驗證的主張一路傳播（多代理情境更嚴重）。
   - **影響**：最終輸出不可靠；錯誤級聯。
   - **緩解方法**：
     - **Verifier / Critic agents** 作為強制品質關卡（Phase 3 彙整後，以及子結果返回後）。
     - 結構化 observation schema（status、confidence、issues list）+ 交叉驗證（跨代理／跨來源比對）。
     - 多形式驗證（觀察 grounding + 外部檢查）。
     - Trajectory ranking（例如 Prospector 風格 critic 在多個嘗試中選最佳）。
     - 自我演化時：只允許提交已在 held-out traces 上驗證過的修改。

5. **代理間失配與協調失敗（多代理特有）**
   - 角色越界、目標衝突、共享狀態過舊、溝通缺口、錯誤傳播。
   - **影響**：協作品質差；有時單一強代理勝過複雜 MAS。
   - **緩解方法**：
     - 強力中央 **Orchestrator/Planner** 進行明確拆解與路由（分層控制優於平面結構）。
     - 資訊契約 + 結構化交接格式。
     - 共享狀態版本化 + 持久化協調原語（streams、pub/sub）。
     - 熔斷器：偵測不一致 → 暫停、調和或升級處理。
     - 明確的「極端分層分工」（清楚定義 specialist roles）。

6. **終止與目標漂移問題**
   - 過早停止（未完成工作）或無法辨識已完成；代理可能錯誤繼續或錯誤放棄。
   - **影響**：錯誤或部分結果。
   - **緩解方法**：
     - 在 spec 中明確 success criteria，並對其進行進度追蹤。
     - 專用終止 action（`Done` tool）且必須通過 verifier。
     - 在 Thought 步驟定期對照原始 objective 進行對齊檢查。
     - 當中間結果已符合目標時，給出提前終止訊號。

7. **其他值得注意的問題**
   - **狀態過時與記憶體失效**：採用混合記憶體（快速短期 + 可檢索長期持久儲存）。
   - **安全性（prompt injection → 造成迴圈或濫用）**：工具沙箱、輸入淨化、最小權限工具存取、監控異常循環。
   - **成本與擴展負擔**：只有當收益 > 協調成本時才用多代理；依 phase 監控 token 用量；在安全前提下並行。
   - **可除錯性**：完整 tracer + 結構化 logs 不可妥協。

### 緩解方法如何整合到迴圈階段
- **Phase 0（Init）**：規格工程 + 驗證是單一最高 ROI 的修正點。
- **Phase 1（Core Loop）**：循環偵測、有界步數／反思、結構化 observations、進度追蹤。
- **Phase 2（Delegation）**：狹義子規格 + 契約；由 orchestrator 監控。
- **Phase 3（Consolidation）**：verifier/critic 關卡、交叉驗證、協調整合。
- **Phase 4（Reflection/Self-evolution）**：套用修改前先驗證；維持有界迴圈。
- **Phase 5（Termination）**：verifier + 帶證據的顯式 Done。

**研究關鍵洞見**：修正**規格品質 + 驗證層 + 明確終止控制**能帶來最大的可靠性增益。缺少這些，單純增加代理數或模型能力通常只會得到遞減或負回報。

## 2. 完整 Agent Loop 流程（可執行）

### Phase 0：初始化（Spec-Driven Setup）
**目標**：在任何迴圈迭代前建立清楚契約。
1. 解析人類指令 → 產生／驗證**Task Specification**（結構化：objective、success criteria、constraints、output format、最大 budget/steps/tokens、quality thresholds）。
2. 建立**初始狀態**：
   - `task.md` 或結構化 scratchpad（當前計畫、todo list、進度、待釐清問題）。
   - 記憶體：短期（近期 observations）、長期（檢索到的知識、過往版本）。
   - Tracer / execution log（供後續反思使用）。
   - Version registry（若會演化 prompts/tools/agents）。
3. **可選的計畫生成**（Plan-and-Execute 風格，複雜任務建議使用）：
   - Orchestrator LLM 產生高層 plan（編號步驟或 dependency graph）。
   - 針對 spec 驗證此 plan（自我批判或專用 critic）。
   - 存入 state。
4. **v3 認知增強（Cynefin + Premortem）**：
   - **Cynefin 分類**（情境感知路由）：LLM 或輕量分類器依因果清晰度、是否需專家知識、是否具湧現性、是否危機等，為任務打標籤（Simple / Complicated / Complex / Chaotic）。存入 task_spec，並用於自動配置迴圈行為（見 1.4 表格）：例如 Simple/Complicated → 偏好 Fast Recognition Path + 降低反思深度；Complex/Chaotic → 強制 Full mode + AAR/Double-Loop + multi-critic ensemble。
   - **Premortem Analysis**（行動前風險 critic）：在最終確定 state 前，執行專用步驟（由 orchestrator 或 Red Team critic）：「想像此計畫與規格在部署後發生災難性失敗。列出最可能的 5-7 個原因。對每個原因提出具體緩解措施（更新 success_criteria、加入 todo 風險項、收緊 constraints、調整 agent roles，或新增 verification gates）。」將緩解內容合併到 living spec 與初始 todo。除了最簡單任務外，建議作為必經關卡。
5. 決定架構：Flat ReAct（簡單）vs Hierarchical（複雜 research/coding）vs Hybrid。同時根據 Cynefin + 任務類型設定初始 `cognitive_profile`（enable_fast_path、reflection_style 等）。

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
在尚未終止時：
**v3 模式選擇（Cynefin + RPD + Dual Process + Metacognition）**：在迴圈開始或每次重大 observation 後，決定操作模式：
- 若 Cynefin 情境為 Simple/Complicated **且** Pattern Store（RPD）找到高相似匹配 **且** metacognition 信心高 → 進入 **Fast Recognition Path**：只做輕量 Thought（僅心智模擬）、跳過冗長推理，以極少 token 直接行動。以 `"fast_path"` 記錄於 tracer，供後續 AAR 檢視。
- 否則（Complex/Chaotic、低 pattern match，或顯式配置）→ 進入 **Full Deliberative Mode**（標準詳細 ReAct Thought + 完整關卡）。Metacognition 以輕量並行監控（偏誤掃描、進度脈搏、情境漂移檢查），可在不確定性飆升時強制於迭代中切換模式。

1. **觀察目前狀態**：載入完整／相關歷史 + task spec + 當前 plan/todo + 最新 observations。（上下文過長時積極摘要，交由 memory manager；同時檢索 Pattern Store 供 RPD 匹配。）
2. **推理（Thought）**：
   - **Metacognitive overlay**（並行）：「我是否處於正確模式？有否偵測到偏誤（依 Paul-Elder）？success criteria 與 todo 的進度如何？情境是否仍符合 Cynefin 標籤？有否需要在之後 Double-Loop 旗標的支配假設？」
   - 分析相對於 success criteria 的進度。
   - 識別缺口、風險、例外狀況。
   - 決定策略：直接用工具、委派子任務、先行綜合、反思／批判或結束。（Fast mode 下保持極度精簡。）
   - 如有需要，更新內部 plan 或 todo。
3. **行動／決定下一步**（必須是嚴格結構化輸出，可解析）：
   - **選項 A（Tool）**：呼叫內建或自訂工具（含 args）。xAI 風格下，伺服器在迴圈內處理執行。
   - **選項 B（Delegate）**：以狹義子指令 + context slice + 該子任務 success criteria 呼叫子代理。（分層式）
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
5. **輕量反思**（每 N 步或失敗時）：快速自我批判 —「這條軌跡仍對齊嗎？有沒有明顯可修正之處？」

**Circuit Breaker 模式（生產環境建議使用）**

熔斷器可在工具、LLM 呼叫或子代理反覆失敗時防止級聯失敗。它有三種狀態：
- **CLOSED**：正常運作，請求可通過。
- **OPEN**：失敗過多 → 立即 fast-fail（保護系統）。
- **HALF_OPEN**：等待 timeout 後允許有限測試請求，檢查是否恢復。

建議每種工具類型或每種子代理角色各使用一個熔斷器，並與下方重試包裝器整合。

**Code Example: Minimal Controlled ReAct Loop with Cycle Detection (Python)**

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

**Code Example: Lightweight Verifier / Critic Agent (Prompt + Schema) — v3 Enhanced with Critic Modes + Paul-Elder Standards**

```python
VERIFIER_PROMPT = """
You are a strict, skeptical Verifier / Critic Agent operating in {critic_mode} mode.
Given the original task_spec and the candidate_output, 
return ONLY valid JSON with the schema below.

**Mode-specific instructions**:
- standard: Focus on factual grounding, completeness vs success_criteria, hallucination detection, format compliance.
- red_team: Adversarially attack the output — actively hunt for weaknesses, edge cases, hidden assumptions, single points of failure, or ways it could be misinterpreted/misused. Be creative and ruthless but evidence-based.
- paul_elder: Explicitly apply Paul-Elder Critical Thinking: evaluate Elements of Thought (purpose, question, information, concepts, assumptions, inferences, implications, point of view) and Intellectual Standards (clarity, accuracy, precision, relevance, depth, breadth, logic, significance, fairness, sufficiency). Flag violations with specific quotes/references.
- six_hats or ensemble: Incorporate multiple perspectives (or run sub-checks) and aggregate.

{
  "passes": true | false,
  "score": 0.0-1.0,
  "issues": ["list of concrete problems with evidence"],
  "suggestions": ["actionable fixes"],
  "confidence": 0.0-1.0,
  "critic_mode_used": "{critic_mode}",
  "paul_elder_violations": ["optional list if mode includes it"]
}

Task Spec: {task_spec}
Candidate Output: {candidate_output}
"""

def verify_output(candidate: dict, task_spec: dict, llm, critic_mode: str = "standard") -> dict:
    """v3 enhanced: Supports multiple critic modes. 'ensemble' runs 2-3 modes in parallel and merges results."""
    prompt = VERIFIER_PROMPT.format(
        task_spec=task_spec, 
        candidate_output=candidate,
        critic_mode=critic_mode
    )
    result = llm.generate(prompt, output_schema=...)  # force JSON
    # Optional: if critic_mode == "ensemble": run red_team + paul_elder in parallel and aggregate
    return result
```

**Code Example: Simple Self-Evolution / Reflection Step (Trace → Edit → Validate)**

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

**Termination Conditions**（每次迭代或關卡時檢查）：
- Success criteria 達成 + 通過 quality gate。
- 已達 max steps / token budget / time。
- 顯式 `Done` / `Finish` action 且輸出已驗證。
- 不可恢復失敗（升級給 human 或更高層 orchestrator）。
- 若中間結果已滿足 objective，則提早退出。

### Phase 2：分層委派與子迴圈
當 orchestrator 決定委派時：
1. **拆解與路由**：
   - Planner 選擇或實例化適當子代理類型（specialist role、toolset、prompt template）。
   - 建立狹義子任務規格（父目標子集 + 相關 context slice）。
   - 呼叫子代理（可用同一 LLM 但不同 system prompt/role，或使用不同模型）。
2. **子代理執行獨立迴圈**：
   - 子代理根據子規格執行自己的 ReAct 風格迭代（或最佳化變體）。
   - 維護本地 state/memory。
   - 可再委派（樹狀）或呼叫工具。
3. **回傳結構化結果**給父代理（向上冒泡）：
   - 使用前述 structured observation 格式。
   - 包含 provenance（哪個子代理、trace summary）。
4. **父代理處理**：
   - 記錄到全域 state/tracer。
   - 驗證／整合（與其他分支合併，並透過 harmonization 解決衝突）。
   - 更新全域 plan/todo。
   - 決定下一步：更多委派、直接行動、彙整或批判。

**平行性**：在依賴關係允許時（例如相互獨立的研究分支），可並行執行多個子代理／工具（xAI 多代理風格，或如 Grok Build 的 worktree 隔離）。

### Phase 3：彙整、綜合與重組
取得子結果或達到重大里程碑後：
1. **聚合**：收集所有相關 observations + plan progress。
2. **協調整合**：LLM（或專用 Reporter agent）合併、去重、交叉參照、解決矛盾，產生統一視圖。
3. **重組**：轉換成目標輸出形狀（report、code、answer、updated plan），並強制符合初始 spec 的格式。
4. **品質關卡**：
   - 執行 critic/refiner：對照 success criteria 評分、檢查幻覺／缺口、提出修正。
   - 若未通過：觸發精煉（重新規劃、重新委派特定部分，或自我編修）。
   - 若通過：繼續（或最後潤飾）。
5. **更新狀態**：將彙整後知識持久化到 long-term memory／versioned artifacts。

**Consolidator Prompt 片段範例**：
「你是一名綜合專家。給定原始 task spec、目前 plan，以及這些子結果 [structured list]，請輸出：1）更新後的進度摘要。2）已解決的衝突。3）最終輸出區塊草稿。4）剩餘缺口與建議下一步行動。」

### Phase 4：反思、批判與自我演化（進階）
**v3 結構化反思（AAR + Double-Loop + 5 Whys / Ishikawa + Paul-Elder / Red Team）**：所有反思都遵循顯式、多層協議（可透過 task_spec.reflection_style 配置）。這把原本的語言式自我批判，升級為嚴謹的多模型認知流程。

- **強制 AAR 模板**（每個里程碑、失敗或終止都必用；直接採用 After-Action Review 最佳實務）：
  1. **原本應發生什麼？** — 重述原始 task_spec、success criteria、plan 與預期 observations 的相關部分。
  2. **實際發生什麼？** — 由 tracer + structured observations 進行摘要（success、partial、errors、關鍵 metrics）。如適用，包含 Fast vs Full mode 使用統計。
  3. **為什麼？（診斷）** —
     - 第一層：標準歸因（TextGrad 風格或 LLM）。
     - 深層（若有問題或 Cynefin=Complex）：對 2-3 個最主要問題迭代執行 **5 Whys**。再用 **Ishikawa Fishbone**（或輕量 fault tree）分類，例如：Prompts/Methods、Models/Tools/Agents、Data/Observations、Context/Environment、State/Memory、Verification Gates、Human Spec。
     - 用 **Paul-Elder** 視角交叉檢查：哪些 thought elements 薄弱？哪些智識標準被違反（accuracy？depth？fairness？）？
  4. **下一步？（可執行教訓）** — 具體、可版本化的改動，按 impact/effort 排序。

- **Double-Loop Learning 層**（總是在 AAR 單迴圈診斷後、提交變更前執行）：
  - 「除了修正即時症狀之外：哪些*支配變數*或基礎假設造成這種結果？例如：我們對『品質輸出』的定義是否過鬆？agent role 邊界是否允許漂移？memory retrieval 策略是否與任務類型不匹配？success criteria 本身是否需要演化？是否要新增 critic roles 或改變迴圈路由邏輯？」
  - 只有通過這層 meta 問題的改動，才會進入 validation + registration。這能避免表面修補，帶來真正的架構式自我改進。

- **每條軌跡或里程碑的反思**（原有）："LLM summarizes trace, diagnoses failures/successes, proposes improvements" 現在會被包裹在上述 AAR + Double-Loop 結構中。

- **自我演化迴圈**（受 AgentOrchestra 啟發，並增強）：
  1. 透過 tracer + AAR output 蒐集 trace。
  2. 在 **AAR/Double-Loop 框架內**歸因錯誤／機會（LLM 或 TextGrad）。
  3. 提出有針對性的改動（prompts、tools、agent configs、success criteria，甚至生成程式碼／memory schemas）。
  4. 驗證改動（在 held-out 或相似任務上重跑；檢查 metrics；可選擇對新版本再跑一次 Premortem）。
  5. 若有改善（且 Double-Loop 批准）：註冊新版本（含 lineage + AAR justification）。支援 rollback。更新 Pattern Store 的 outcome metadata，供未來 RPD 使用。
  6. 可選：若變更屬 meta（例如新增 critic mode 或路由規則），同步推進到 cognitive_profile 預設值。

- **Critic Agent 角色**（增強）：一個獨立、輕量 agent，只負責審查草稿／計畫而不執行完整流程，可在關卡時呼叫。現在支援多種模式（standard | red_team | paul_elder | six_hats | ensemble），如第 1.4 節所定義。Red Team 模式特別建議用於 Premortem 與高風險彙整。

- **收益**：執行期持續改進；在相似任務分佈上重複使用時，生產系統會變得更穩健。AAR 的結構、Double-Loop 的深度、系統化根因（5 Whys/Fishbone）、以及多視角 critics（Paul-Elder/Red Team）的組合，讓 Phase 4 成為可累積智能的引擎，而不只是小修小補。fast-path traces 仍會被（較輕量）AAR 檢視，以便系統學會何時可相信 RPD 匹配。

**Implementation Tip**：將 AAR 輸出存為結構化 artifacts，並在 registry 中與版本建立連結。這會形成可稽核的「學習歷史」，讓未來代理（或同一系統在相似任務上）可用於 RPD 風格匹配與決策。

### Phase 5：終止與輸出
- 當通過關卡或達到終止條件：
  1. 最終綜合。
  2. 產出結構化最終輸出（符合 spec）。
  3. 可選：為使用者或 logging 產生事後反思摘要。
  4. 持久化完整 trace + versions，以供 audit/replay/debug。
- **Human-in-loop hooks**：在品質關卡失敗、高風險行動或預算耗盡時觸發。

## 3. 狀態、記憶體與基礎設施建議

- **State Schema**：task_spec + current_plan/todo + history（thought/action/observation tuples）+ memory（key-value 或 vector）+ versions + tracer。
- **Memory Management**：分層式（每個子代理本地 + 全域）。上下文壓力高時摘要。並行時做 session isolation。
- **Tracing**：完整執行圖（誰呼叫了什麼、結果、耗時、版本），支援除錯、反思與最佳化。
- **Versioning**（受 TEA 啟發）：prompts、tools、agent roles、generated artifacts — 全部版本化，保留語意 lineage 與 rollback。
- **xAI Integration Tips**：
  - 對研究密集的頂層任務使用 Grok multi-agent mode。
  - 混合使用伺服器端 agentic tools 與客戶端自訂 tools（hybrid）。
  - 對 coding agents：採用先規劃 + 在隔離環境（worktrees）中平行子代理。
  - 在可行時串流 reasoning tokens，以提升透明度。
- **Production Hardening**：
  - 嚴格輸出 schemas（JSON mode 或 constrained decoding）。
  - Timeouts、帶 backoff 的重試、對失敗 tools/sub-agents 使用熔斷器。
  - 成本／token budgets + 監控。
  - Logging + observability（每個 thought/action/observation 都要記錄）。
  - 對 tools/code 的執行採用沙箱。

## 4. 決策框架（何時使用哪種模式）

| 任務複雜度 | 建議模式 | 建議啟用的關鍵能力 | 使用範例 |
|-----------------------|--------------------------------------|---------------------------------|------------------|
| 簡單事實查找 | Flat ReAct（單一迴圈） | 工具呼叫、基本 thought | 快速搜尋 + 回答 |
| 多步研究 | xAI Multi-Agent 或 Hierarchical | 平行代理、leader 綜合 | 帶來源的深度分析 |
| Coding／長專案 | 先規劃 + Hierarchical + Worktrees | 隔離子代理、todo.md | 完整應用生成 + 除錯 |
| 開放式／創意型 | ReAct + Reflection + Self-evolution | Critic 關卡、版本化 prompts | 迭代式設計精煉 |
| 高風險／高可靠性 | 以上全部 + 強品質關卡 | 結構化結果、驗證 | 企業級自動化 |

## 5. 常見陷阱與緩解方法（來自研究）

**主要參考：請參閱上方第 1.5 節，其中包含完整 MASFT 風格分類法、失敗模式與對應階段的緩解策略。** 下列要點保留作快速掃描，並補充近期研究中的其他模式。

- **上下文爆炸**：積極摘要 + 分層狀態（本地子記憶）。
- **無限迴圈／空轉**：硬性 max iterations + 在 todo 中追蹤進度 + 能強制重新規劃或升級處理的 critic。
- **彙整品質差**：強制使用結構化子結果 + 專門 harmonization/reporter 步驟。
- **計畫中的幻覺**：每個重大主張都必須 grounding 到 observations；在提交 plan 前先跑 critic。
- **委派脆弱**：使用明確子任務 specs + success criteria；驗證返回結果。
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

- **ReAct 基礎**：Yao 等，"ReAct: Synergizing Reasoning and Acting in Language Models"（arXiv:2210.03629，ICLR 2023）。
- **xAI 生產實作**：xAI Developer Docs（Multi-Agent orchestration、伺服器端 agentic tool calling、Grok Build CLI patterns）— 以 leader synthesis 為核心的即時多代理研究；4/16 代理團隊。
- **分層式與進階方法**：
  - "AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool–Environment–Agent (TEA) Protocol"（arXiv ~2026）— 分層 planner、TEA protocols、透過 reflection/TextGrad 風格自我演化，在 GAIA 上有強勁成果。
  - 綜述："The Landscape of Emerging AI Agent Architectures..."（2024）；"Large Language Model Agent: A Survey..."（2025）；"LLM-based Agentic Reasoning Frameworks: A Survey"（2025）。
- 其他模式：Reflexion（自我反思）、Plan-and-Execute 變體、LATS（樹狀搜尋）、MetaGPT / AgentVerse / DyLAN（多代理協作）。

---

**實作下一步**：
1. 先用你偏好的框架（LangGraph、自訂迴圈，或 xAI SDK）建立最小 ReAct harness。
2. 加入結構化 observation schema 與 todo/state 管理。
3. 疊加分層委派 + 彙整。
4. 裝設 tracing + quality gates。
5. 對重複出現的任務類型實驗 reflection/self-evolution。
6. 將 xAI multi-agent mode 整合到研究型子任務。

本文件設計為**可直接執行的指引** — 複製模式、改寫偽代碼並迭代。若需要更進一步的精煉、Python/Node 具體程式碼範例，或與既有 harness（例如 critic loops、spec-driven task.md）整合，請提供你目前使用的技術棧細節。

**檔案建立於**：`/home/workdir/artifacts/agent_loop_v3.md`（v3 認知增強版：整合 `thinking_model.md` 的排序人類思考模型表；在完整保留 v2 的內容、程式碼範例、緩解策略與結構之上延伸）
