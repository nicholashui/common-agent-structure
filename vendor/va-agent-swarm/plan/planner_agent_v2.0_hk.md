# SIPA — 軟件實作規劃代理
## 完整詳細規格與設計文件

**版本：** 2.0（完整擴展版）  
**日期：** 2026-06-03  
**狀態：** 可投入生產的設計規格  
**擁有者／上下文：** 為 Nicholas（N1ch01as）生態系統而設計，可整合現有 AI 編碼執行框架（Cursor、Kiro、Claude Code、Grok Build、自託管 OpenWebUI）、規格驅動開發工作流程、評論／精修循環，以及大型 Markdown 語料的 RAG 實務。  
**目的：** 一個分層式、經上下文工程設計的多代理系統，可吸收大型功能規格與支援文件，並產出高保真、細節層級恰當且可追溯的實作計劃與細粒度任務。它明確透過按組件類型自適應的抽象／細節層級、範圍化 RAG、分層記憶，以及內嵌質量閘門來解決上下文視窗限制。

本文件是**權威且完整的規格**。它可直接作為實作 SIPA（或演進既有 meta-agent 系統）的 source-of-truth 規格使用。文件整合了來自 arXiv 論文（MAAD、AgentOrchestra、LLM 多代理軟件工程調查等）、GitHub Spec Kit 的 SDD 模式、xAI Grok Build 多代理規劃／評估、上下文工程最佳實踐，以及與迭代式自我精修／執行框架工程原則一致的深度研究成果。

---

## 目錄
1. 執行摘要與問題陳述
2. 研究基礎與引用（深度解析）
3. 設計原則與核心創新
4. 組件分類法與自適應細節策略
5. 完整系統架構（分層多代理）
6. 詳細代理角色、職責、輸入／輸出
7. 完整端到端工作流程（分階段，附示例）
8. 資料模型、綱要與結構化輸出
9. RAG、上下文工程與記憶架構
10. 評論／評估子系統（評分規則、循環、質量閘門）
11. Prompt 工程與 Few-Shot 策略
12. 輸出工件模板（各類型完整示例）
13. 實作路線圖與技術指引
14. 與現有工具及執行框架整合
15. 指標、評估與成功準則
16. 風險、緩解措施與邊界情況
17. 未來擴展與路線圖
18. 參考資料與來源

---

## 1. 執行摘要與問題陳述

**挑戰**  
你正在維護，或正基於一套非常龐大的功能規格、需求文件、使用者故事、架構筆記、API 合約、UI 描述及相關工件進行開發，這些內容通常橫跨數百個 Markdown 檔案或等效資料來源。若直接把整個語料拿去提示編碼代理，通常會失敗，原因包括：

- 硬性的上下文長度限制（即使是 128k–200k+ token 的模型，也會在噪音中失去連貫性，或遺漏關鍵細節）。
- **統一處理方式不匹配**：高層架構計劃需要的是*戰略性摘要 + 決策記錄 + 視圖*。特定 UI 畫面需要的是*深入、範圍狹窄的功能摘錄 + 完整驗收標準 + 流程*。共用函式庫／組件需要的是*介面合約 + 擴展點 + 對共同行為的綜合*。一刀切的摘要方式會破壞價值。
- 可追溯性與意圖保真度流失（幻覺、遺漏交叉參照、偏離原始規格）。
- 無法支撐由多個 coder agents／人類進行的迭代開發或平行工作。

**解法 — SIPA（Software Implementation Planner Agent）**  
SIPA 是一個**分層式多代理規劃器**，具備：

- 針對整個語料的智能吸收與 hybrid RAG（語義分塊、可選 Knowledge Graph、動態範圍控制）。
- **組件類型分類**，會觸發專門的子規劃器，產出*恰好合適的抽象與細節層級*。
- 內嵌、多階段的**Critic/Evaluator**，具備可追溯性評分、一致性檢查、ATAM 風格分析，以及基於 patch 的迭代精修（「rethink」循環），直到通過質量閘門。
- 結構化、可版本化、對 git 友好的 Markdown 輸出（總計劃、按類型劃分的實作規格、細粒度任務清單），這些輸出本身可獨立閱讀，且尺寸適合下游編碼代理（Cursor、Kiro、Claude Code、Grok Build 等）直接消費。
- 活的規格哲學（與 SDD 對齊）：計劃會隨實作回饋演進；保有完整的雙向可追溯性。
- 與你現有實踐高度對齊：規格驅動開發、評論代理、自我精修、執行框架工程、詳細 `task.md` 輸出、xAI API／本地模型，以及增量式／可投入生產的工程方法。

**關鍵差異化能力**  
SIPA 不只是通用分解器。它使用明確的**組件分類法**（Architecture/Strategic、Feature/UI/Tactical、Common/Shared/Operational 等），來驅動根本不同的檢索、摘要、綜合與輸出結構。這正是你「軟件開發需要不同層次實作細節」洞見的實務化落地。

**預期影響**  
- 在**提高**保真度的同時，將 coder agents 的有效上下文大小降低 5–20 倍。
- 提高實作成功率，減少重工循環，並保留大型規格中的原始意圖。
- 支援可擴展的平行開發與可維護的活文件。
- 成為可整合進 N1ch01as Architect 或類似系統中的可重用 meta-capability。

---

## 2. 研究基礎與引用（深度解析）

SIPA 並非憑空發明，而是對 2025–2026 年 LLM 代理在軟件工程、分層規劃、需求到架構轉換，以及上下文工程方面最佳研究與工具的有原則綜合與延伸。

### 2.1 規格驅動開發（SDD）與結構化代理工作流程
- **GitHub Spec Kit**（2025，開源）：將規格設為核心且持續演進的事實來源。其四階段帶閘門工作流程為：
  1. **Specify** — 從高層意圖轉成詳細的「做什麼／為什麼」規格（使用者旅程、成果）。
  2. **Plan** — 由目標技術棧、架構與限制推導出技術計劃（變體、權衡、合規）。
  3. **Tasks** — 將規格與計劃拆成小型、可隔離、可審查的區塊（非常適合上下文視窗與安全 PR）。
  4. **Implement** — coder agents 逐個（或平行）執行任務，並設置人類檢查點與精修。
- 對大型／複雜專案的好處：集中分散知識、支持對舊系統或大型規格的安全迭代，並把穩定意圖與可靈活調整的「如何做」分離。SIPA 針對*既有大型語料*，透過 RAG 與類型感知細節策略，實作並擴展了 **Plan + Tasks** 階段。
- 相關工具：Kiro（spec-first，使用 requirements/design/tasks MD）、Tessl（以 spec 為 single source of truth 生成代碼）、DeepLearning.AI 的 SDD with coding agents 課程（Paul Everitt / JetBrains）。
- 對齊點：SIPA 的輸出被設計為可與 Spec Kit 工件完全同樣方式被消費。

### 2.2 分層多代理系統與規劃
- **AgentOrchestra**（arXiv:2506.12508，2025）：採用分層框架，最上層 Planning Agent 明確將複雜目標分解為子目標、維護動態計劃，並委派給專門的模組化子代理（Deep Researcher、Browser Use、Deep Analyzer 等）。使用標準化協作介面，強調可擴展性與多模態。SIPA 採納其 top-planner + specialized sub-planners 模式，以及明確子目標制定。
- **Self-Organized Agents（SoA）**：母代理管理高層抽象，並將細節子任務委派給子代理（適用於超大型代碼生成中的分層分解）。
- **GoalAct**（arXiv:2504.16563）：引入持續更新的全局規劃與分層執行（高層技能 → 工具選擇 → 細化精修），顯著提高複雜任務成功率。
- **ALMAS**（Autonomous LLM-based Multi-Agent Software Engineer）：Sprint／Planner agents 將高層任務拆解為帶有驗收標準、工作量估算與逐步計劃的 user stories，映射 agile 團隊角色。
- **HPTSA** 及類似的分層規劃 + 任務專用代理系統：在單一代理因上下文限制而失敗的複雜長期任務中已被證實有效。

### 2.3 需求工程 → 架構（MAAD — 最直接的影響來源）
- **MAAD**（Multi-Agent Architecture Design，arXiv:2606.01385，2026）：最先進的框架，可將 Software Requirements Specifications（SRS）轉換為完整、可追溯、多視角的架構藍圖，並內建質量評估。
  - **四個專門代理**：
    - **Analyst**：解析 SRS，提取與結構化 FR、NFR、Architecturally Significant Requirements（ASR），並對可追溯性進行分類與註記。
    - **Modeler**：將需求映射到「4+1」架構視圖（Kruchten），生成 PlantUML/UML 圖，並透過 RAG 檢索模式、策略與標準。
    - **Designer**：綜合產生可投入生產的文件（traceability matrices、API specs、deployment configs、設計 rationale、trade-off analysis）。
    - **Evaluator（Critic）**：嵌入每個階段，驗證完整性、一致性（跨視圖）、語法與 anti-patterns，並執行系統級 ATAM（Architecture Tradeoff Analysis Method）評估，產出帶嚴重度與修復建議的不匹配報告，觸發基於 patch 的迭代精修。
  - **Hierarchical Memory**：Working（當前工件 + 回饋）、Episodic（任務／迭代歷史與經驗）、Semantic（一般化模式、原則、rationale，並附 metadata 便於檢索）。
  - **RAG Integration**：注入外部知識庫（ISO/IEC 42010、Bass 等架構文獻、模式），以降低幻覺並強化嚴謹性（分層、stereotypes、關注點分離）。
  - **Results**：在 modularity、traceability、completeness 上優於 MetaGPT。實務者認為產出「結構清晰」且可減少工作量。RAG 可量化提升模式正當性與標準合規性。
- SIPA 直接借鑑 MAAD 流程（Analyst-Modeler-Designer-Evaluator）作為 **Architecture** 子規劃器基礎，並將 critic + memory + RAG 模式推廣到所有組件類型。

### 2.4 更廣泛的 LLM 多代理軟件工程系統
- 調查論文 **LLM-Based Multi-Agent Systems for Software Engineering**（arXiv:2404.04834v4，2025）：對 SDLC 各階段做全面綜述。指出分層設計（Mother/Child）、角色專業化（PM/Architect/Engineer/QA）、迭代回饋、記憶元件，以及針對大型代碼庫的 RAG／knowledge graphs 都是關鍵方向。文中提到 MARE（需求階段）、MetaGPT（瀑布角色）、ChatDev、Think-on-Process（動態流程生成）等。
- 其他值得注意者：MASAI（模組化軟件工程 AI 代理架構）、SWE-Search（Monte Carlo Tree Search + iterative refinement）、RepoSketcher / CodexGraph（基於圖的超大型代碼庫理解，相關原則同樣適用於規格）。

### 2.5 上下文工程、RAG 與大型語料處理
- 現代代理文獻強調應超越天真的 RAG，轉向 **Context Engineering**：動態的 write/select/compress/isolate 策略。
  - 語義分塊（依邏輯邊界：功能、章節、requirement IDs）+ hybrid retrieval（vector + BM25 + graph）。
  - 在組裝前先對檢索段落進行壓縮／摘要。
  - 綱要強制、metadata 注入、結構化 prompt。
  - 分層索引與記憶（working/episodic/semantic），以維持長時間規劃會話的一致性。
- 關於 code agents 的研究（SWE-agent harness、上下文持久化）顯示，聚焦、範圍受控的檢索，遠比把整份大型上下文全倒進去有效。
- SIPA 將規格語料視為大型代碼庫來處理：智能索引、依賴感知檢索，以及按任務隔離上下文。

### 2.6 xAI / Grok Build 啟發（2026）
- **Grok Build**（xAI beta，可透過 xAI API / SuperGrok Heavy 使用）：一種面向專業軟件工程的新型 coding agent。採用**多代理編排**（最多 8 個平行代理），並具備明確的 **plan → search → build** 工作流程，包含 **Arena Mode**（在人工審核前，自動評估與排名多個競爭輸出）。它高度強調複雜任務規劃、terminal/CLI 整合與 local-first 設計。SIPA 的規劃輸出即是為了直接餵給 Grok Build（或作為其補充）而設計，critic/evaluation 模式亦借鏡了 Arena 風格的自動評分。

這些基礎不是被照搬，而是經過綜合，並透過「按組件類型自適應細節」這一洞見進一步延伸，且根據你的具體限制進行工程化：大型既有規格語料、不同細節需求、可投入生產的執行框架整合，以及由評論驅動的質量控制。

---

## 3. 設計原則與核心創新

1. **分層式分解 + 類型感知專業化**  
   最上層 Orchestrator 執行專案級分解與組件分類。之後由專門子規劃器根據組件類型採用根本不同的策略。

2. **將上下文工程視為第一級能力**  
   範圍化檢索、目標式摘要／壓縮、分層記憶與隔離，使每個工件只使用最小但高訊號的上下文，而非整份語料。

3. **組件類型分類法驅動一切**（核心創新）  
   明確分類會觸發不同的檢索深度、摘要風格、綜合焦點與輸出結構。這正是 SIPA 在真實軟件開發場景中特別有效的原因。

4. **內嵌評論器與質量閘門 + 迭代精修**  
   沒有任何工件在通過多維度自動化與結構化檢查前算作最終版本（可追溯性、一致性、完整性、可實作性、anti-patterns）。基於 patch 的精修與記憶更新會形成「rethink」循環。這與你偏好的 critic agents 與自我改進高度一致。

5. **活的規格與完整可追溯性（與 SDD 對齊）**  
   計劃中的每個主張／決策都必須鏈回原始語料的來源章節。計劃以可版本化 Markdown 形式保存。實作回饋會反向更新計劃與記憶。規格因此成為可執行、會演進的工件。

6. **可投入生產的工程設計**  
   採用結構化輸出（YAML frontmatter + 一致章節）、盡可能確定性的元件、錯誤處理、推理軌跡日誌、增量式運作，以及對戰略性工件設置 human-in-the-loop 閘門。

7. **原生對接執行框架的輸出**  
   總計劃、按類型規格與任務清單，都被設計為可直接投入你的既有工作流程（Cursor/Kiro/Claude/Grok Build 對 `task.md` 的消費、`AGENTS.md` 規則等）。

8. **可自我改進且可擴展**  
   可對規劃器表現進行元反思、演化 prompt/template，並輕鬆加入新組件類型或子規劃器。

---

## 4. 組件分類法與自適應細節策略

SIPA 維護一套明確且可擴展的分類法。Master Orchestrator（或專門的 Classifier 子代理）會為每個 module/component 指派主要類型（以及可選的次級標籤）。這將驅動檢索策略、子規劃器選擇與輸出綱要。

### 主要類型與細節規則

| Type                  | Abstraction Level | Retrieval Strategy                          | Summarization Focus                     | Output Emphasis                              | Example Components                     |
|-----------------------|-------------------|---------------------------------------------|-----------------------------------------|----------------------------------------------|----------------------------------------|
| **Architecture / Strategic** | 高（戰略總覽） | 廣域語料掃描，尋找跨切面 concern + ASR；用 RAG 檢索 patterns/standards | 全域綜合 + 關鍵決策；壓縮非必要敘事 | 視圖（文字／Mermaid）、ADR、介面、質量屬性、rationale、技術選擇 | 系統／子系統架構、主要服務、部署拓撲、跨切面框架 |
| **Feature / UI / Tactical** | 中高（詳細但有範圍） | 針對功能名稱 + 相關 req IDs + UI 提及做窄範圍語義搜尋；拉取完整相關段落 | 保留最少全域上下文；深入局部細節 | 使用者故事、完整驗收標準、流程／狀態機、API 合約、邊界情況、驗證 | 單一畫面、使用者旅程、有界上下文功能、帶 UI 的特定端點 |
| **Common / Shared Component / Operational** | 中（介面與可重用性導向） | 搜尋介面定義、使用模式、設定、跨模組參照 | 綜合共同行為與擴展點；弱化終端用戶敘事 | 公開合約（types/methods/events）、config schemas、不變量、extension hooks、錯誤／效能策略、使用範例 | Auth service、notification lib、shared domain models、utils、caching layer、logging facade |
| **Data / Domain Model** | 中 | 聚焦 entity definitions、relationships、跨規格不變量 | 實體關係綜合 + 生命週期規則 | 綱要（概念／邏輯）、不變量、演進／遷移說明、查詢模式 | 核心實體、聚合、值物件 |
| **Integration / External** | 中 | API contracts、event schemas、第三方規格 | 合約 + 錯誤／相容性導向 | 介面規格、映射規則、retry/idempotency、monitoring | 第三方整合、event buses、舊系統 adapter |
| **Infrastructure / DevOps** | 高 | 非功能需求 + 部署／營運要求 | 約束與 patterns 摘要 | 部署視圖、IaC 考量、可觀測性、擴展策略 | CI/CD pipeline、容器化、監控棧 |

**次級標籤**（正交維度）：Security-critical、Performance-sensitive、High-availability、User-facing、Internal-only、Legacy-modernization 等。這些會影響 critic rubrics 與附加章節。

**分類啟發式**（透過 LLM classifier + 規則實作）：
- 關鍵字／片語如：`architecture decision`、`system overview`、`deployment`、`C4 model`、`4+1 views` → Architecture。
- `UI screen`、`user flow`、`acceptance criteria for [feature]`、`mockup`、`Figma` → Feature/UI。
- `shared`、`common`、`library`、`util`、`service interface`、`public API`、`extension point` → Common/Shared。
- 出現 class/entity diagrams、`domain model`、`aggregate root` → Data/Domain。
- 明確 requirement IDs 或 master plan 中的章節參照。

此分類法是可版本化的，也可擴展（新類型可繼承基底模板，再覆寫檢索／綜合／輸出規則）。

---

## 5. 完整系統架構（分層多代理）

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                              Master Orchestrator / Meta-Planner                               │
│  • 吸收高層目標 + 語料索引                                                                      │
│  • 將專案拆成 phases/epics/modules                                                               │
│  • 組件分類（taxonomy）+ 建立 dependency graph                                                   │
│  • 產出 master roadmap / plan（含工作量／優先級／風險估算）                                      │
│  • 啟動並協調專門 sub-planners；管理全局狀態與記憶                                                │
│  • 高層 critic pass + human gate（可選）                                                         │
│  Tools: Hybrid RAG retriever、classifier、graph builder、summarizer、structured output        │
└───────────────────────────────────────┬────────────────────────────────────────────────────────┘
                                        │ delegates (type-aware)
          ┌─────────────────────────────┼─────────────────────────────┐
          ▼                             ▼                             ▼
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│ Architecture        │     │ Feature/UI          │     │ Common/Shared       │
│ Sub-Planner         │     │ Sub-Planner         │     │ Component           │
│ (MAAD-inspired)     │     │ (SDD Task-style)    │     │ Sub-Planner         │
│                     │     │                     │     │ (Interface-focused) │
│ - Analyst           │     │ - Deep scoped       │     │ - Contract          │
│ - Modeler (views)   │     │   retrieval         │     │   synthesizer       │
│ - Designer (docs)   │     │ - Story/acceptance  │     │ - Config &          │
│                     │     │   expansion         │     │   extension points  │
│ + RAG patterns      │     │ - Flow/state gen    │     │ - Usage examples    │
└──────────┬──────────┘     └──────────┬──────────┘     └──────────┬──────────┘
           │                           │                           │
           └───────────────────────────┼───────────────────────────┘
                                       ▼
                            ┌──────────────────────────┐
                            │   Evaluator / Critic     │
                            │   （多階段、內嵌）         │
                            │   • 可追溯性評分          │
                            │   • 一致性檢查            │
                            │   • 對 ASR 的完整性       │
                            │   • anti-pattern 偵測     │
                            │   • ATAM / mismatch       │
                            │   • patch 精修            │
                            │   • 質量閘門              │
                            └───────────┬──────────────┘
                                        │ feedback（直到通過）
                                        ▼
                            ┌──────────────────────────┐
                            │ Task Decomposer /        │
                            │ Granular Task Generator  │
                            │ • 小型、可審查單元        │
                            │   供 coder agents 使用   │
                            │ • 驗收標準                │
                            │ • 上下文摘錄              │
                            │ • 排序與依賴              │
                            └──────────────────────────┘
```

**支援性基礎設施（共享服務）**：
- **Corpus Indexer & RAG Engine**（LlamaIndex/Haystack 或自訂）：語義分塊、embedding、hybrid search（vector + keyword + 可選 Knowledge Graph）、段落壓縮、metadata 標記（requirement IDs、component tags、section paths）。
- **Hierarchical Memory Manager**：
  - Working Memory：當前工件、回饋、活躍的 context packages。
  - Episodic Memory：按 module/iteration 儲存的歷史、決策、精修軌跡、經驗教訓。
  - Semantic Memory：一般化模式、詞彙表、跨切面原則、可重用 rationale（vector + structured metadata 便於檢索）。
- **Knowledge Graph**（可選但建議）：Nodes = requirements、components、decisions；Edges = traces_to、depends_on、refines、conflicts_with、implements。可用於 impact analysis 與更豐富的檢索。
- **Structured Output Enforcer**：Pydantic models / JSON mode + validation。所有代理都產出 typed artifacts。
- **Tooling Layer**：檔案系統存取（讀規格、寫計劃）、代碼執行（Mermaid/PlantUML 渲染、contract validation stubs）、圖表生成，以及針對 UI mock 的可選 vision 能力。

**編排風格**：可採用有狀態圖（LangGraph 風格）或具明確 handoff protocol 的 role-based crew。支援獨立子規劃器的平行執行，並在重要回饋出現時動態重規劃。

---

## 6. 詳細代理角色、職責、輸入／輸出

### 6.1 Master Orchestrator / Meta-Planner
**職責：**
- 吸收高層目標與已索引語料。
- 將專案拆解為 phases、epics、modules，並建立 dependency graph。
- 透過 taxonomy + heuristics/LLM 對組件分類。
- 生成 master roadmap/plan（高層摘要、優先級、風險、工作量估算）。
- 協調 sub-planners，管理全局記憶與 traceability matrix。
- 執行高層一致性與完整性 critic pass。
- 對戰略性工件設置 human review gate。

**輸入：** 高層 project prompt/goal、corpus index + summaries、可選的既有部分計劃。  
**輸出：** `master_plan.md`（或 `project_roadmap.md`）、依賴圖（Mermaid）、初始 traceability skeleton、已分類 module 清單、供 sub-planners 使用的 spawn commands。  
**Prompt Style：**「你是一位資深軟件專案經理與架構師。請分解以下專案……依 taxonomy 對每個 module 分類……為 MVP 排定優先順序……以嚴格結構化格式輸出。」

### 6.2 Architecture Sub-Planner（受 MAAD 啟發）
**職責：**
- Analyst 階段：提取／驗證與架構範圍相關的 FR/NFR/ASR，確保可追溯性。
- Modeler 階段：使用文字／Mermaid／PlantUML 生成多視圖架構（logical、process、development、physical/scenario），並透過 RAG 檢索 patterns。
- Designer 階段：綜合產生文件 —— rationale、interfaces/contracts、deployment considerations、trade-off analysis。
- 與 Critic 在每個子階段協作。

**輸入：** 針對架構邊界範圍化取得的語料摘錄 + master plan 上下文 + RAG 知識庫（patterns、standards）。  
**輸出：** `architecture_<module>.md`，帶 YAML frontmatter，內含 overview、views、decisions（ADR）、interfaces、quality attributes、deployment、rationale 等章節。  
**Special Tools：** 架構知識用 RAG；圖表生成。

### 6.3 Feature/UI Sub-Planner（SDD Task-style）
**職責：**
- 對特定 feature/UI 執行深度且窄範圍的檢索。
- 從源材料中精修／擴展 user stories 與 acceptance criteria。
- 綜合 interaction flows、state machines、UI behaviors。
- 提取或生成精確的 API contracts、payloads、validation rules、error/edge cases。
- 將全局上下文維持在最小範圍；專注於「這個畫面／功能的細節」。

**輸入：** 高度定向的檢索結果（feature name + 相關 req IDs + UI/acceptance 提及）+ master plan + 任何已關聯的 architecture contracts。  
**輸出：** `feature_spec_<name>.md` —— 詳盡、範圍清晰、可直接進入實作的功能規格。  
**Special：** 特別強調完整驗收標準（checklist 或 Gherkin），以便直接轉為測試。

### 6.4 Common/Shared Component Sub-Planner
**職責：**
- 從分散在整份語料中的提及內容中綜合出 interface contracts、types、methods/events。
- 定義 configuration points 與 defaults。
- 識別並文件化 extension points、hooks、plugin 機制。
- 捕捉 invariants、guarantees、error handling strategy、performance considerations。
- 提供 usage examples 與 testability notes。
- 聚焦於可重用性與可維護性，而不是終端用戶敘事。

**輸入：** 橫跨 interface definitions、usage patterns、config requirements、cross-module references 的檢索結果。  
**輸出：** `component_spec_<name>.md` —— 以 contract 為先、以擴展為導向的規格。  
**Special：** 通常是最需要「綜合」能力的類型之一；需要從大量零散片段中良好聚合。

### 6.5 Evaluator / Critic（內嵌、多階段）
**職責：**
- 可追溯性評分（每個主要元素都需鏈到來源章節並附證據）。
- 一致性檢查（計劃內部、與 master／其他 modules 之間不得矛盾）。
- 與語料中相關 ASR/NFR 比對的完整性檢查。
- Anti-pattern 偵測（God object、緊耦合、缺少 edge cases、合約不清晰等）。
- 在相關情況下執行 quality attribute / tradeoff analysis（受 ATAM 啟發）。
- 產出結構化回饋 + 嚴重度 + 建議 patch。
- 做出 gate 決策（pass / refine / escalate to human）。

**輸入：** 草稿計劃工件 + 所用來源摘錄 + 先前決策記憶 + rubric。  
**輸出：** 結構化 critique（JSON + 自然語言）+ patch 建議或 approval。  
**實作方式：** 可以是一個強大的 LLM 搭配 rubric + tools，也可以是一組專門評論代理（traceability critic、consistency critic 等）。可使用帶校準 rubric 的 LLM-as-judge + 規則式檢查。

### 6.6 Task Decomposer / Granular Task Generator
**職責：**
- 將已驗證的計劃拆成適合 coder agents 的小型、聚焦、可審查任務（單一上下文視窗、單一邏輯變更、明確 acceptance criteria）。
- 內嵌或鏈接父計劃／規格中的相關摘錄。
- 為任務排序、標示依賴、建議測試或審查焦點。
- 產出可直接使用的任務清單（例如 `tasks_<module>.md` 或個別 task cards）。

**輸入：** 已驗證的類型化計劃 + master dependencies。  
**輸出：** 帶優先級與執行順序的任務清單，並附完整執行上下文。

---

## 7. 完整端到端工作流程（分階段，附示例）

### Phase 0：吸收與索引（支援增量）
1. 掃描 spec 目錄與相關文件。
2. 智能分塊（標題層級、若存在則標記 requirement ID、語義邊界、feature/component 提及）。
3. 生成 embedding 並以豐富 metadata 儲存（file path、section、requirement IDs、component tags、last modified）。
4. 可選：提取 entities/relationships → 建立／更新 Knowledge Graph。
5. 生成／更新語料層級摘要、詞彙表，以及初始 component candidate list。
6. 輸出：可搜尋索引 + `corpus_index.md` / `glossary.md`。

**Tools：** LlamaIndex/Haystack pipeline 或自訂腳本。可在偵測變更時執行（git hooks 或 watcher）。

### Phase 1：高層分解與 Master Plan
1. Master Orchestrator 接收高層目標 + index。
2. 分解專案；對 modules 分類；建立 dependency/risk 視圖。
3. 產生 `master_plan.md`（epics/phases、各 module 高層摘要、優先級、critical path、初始 traceability matrix skeleton）。
4. 對 master plan 執行 critic pass。
5. 可選 human review gate。
6. 為高優先 module 啟動 sub-planners（若彼此獨立可平行）。

**Example Master Plan Excerpt**（簡化版）：
```markdown
---
type: master_plan
version: 1.0
---
# Project Roadmap — DeepTutor HKDSE xAI Edition (Example)

## Phases
### Phase 1: Core Domain & Auth (MVP Foundation)
- Architecture: [architecture_core_domain.md] (Strategic)
- Common: Auth Service, User Domain Model
- Features: Login/Register flows

### Phase 2: UI Features (Student/Teacher Dashboards)
- Feature: Student Profile Screen (Tactical)
- ...

## Dependencies
Core Domain → Auth Service → All UI features
...
```

### Phase 2：範圍化、類型感知規劃 + Critic 循環（核心循環）
對每個 module，依優先順序（或平行）執行：

1. **上下文組裝**：
   - Classifier 確認類型。
   - 依類型特定 query strategy + compression 執行 hybrid retrieval。
   - 組裝最小上下文封包 + 記憶檢索（與此 module 相關的 episodic/semantic 記憶）。

2. **Sub-Planner 執行**（類型特定模板 + few-shot）：
   - Architecture：Analyst → Modeler（RAG patterns）→ Designer。
   - Feature/UI：深度檢索 → story/acceptance 擴展 → flow/state/API 綜合。
   - Common：介面聚合 → contract 定義 → extension/config 綜合。

3. **內嵌 Critic 階段**（可在每個子階段後執行，也可在最後執行）：
   - Traceability 檢查（LLM + link validator）。
   - Consistency（與 master + sibling plans 對齊）。
   - Completeness 與 anti-patterns。
   - 結構化 feedback JSON。
   - 若低於 gate：sub-planner 接收 patch instructions + memory，只重新生成失敗章節。

4. **版本化與持久化**：
   - 寫入 `architecture_<name>.md` / `feature_spec_<name>.md` / `component_spec_<name>.md`，包含完整 frontmatter + traceability。
   - 更新全局 traceability matrix 與 episodic memory。

**Example Interaction Trace**（簡化架構示例）：
- 生成草稿。
- Critic：「`event-driven notifications` 的可追溯性只鏈到一個章節；缺少 NFR-089 對可靠性的支持。另外，deployment view 缺少來自標準 patterns 的 observability tactics。」
- Patch instruction：「明確鏈到 NFR-089 並透過 RAG 檢索 observability patterns；在 deployment view 章節加入 2–3 點策略。」
- 精修後草稿通過 gate。

### Phase 3：細粒度任務生成
- Task Decomposer 讀取已驗證計劃。
- 產出 `tasks_<module>.md`（或按 epic 的 task boards），其中包含：
  - 小型單元（例如：「根據 `feature_spec_user_profile.md` 第 3.2–3.4 節與 `architecture_user_domain.md` 合約，實作 `UserProfileHeader` 元件」）。
  - 內嵌相關摘錄，或精確鏈接 + 行參照。
  - 清楚的驗收標準（直接源自計劃）。
  - 建議測試、審查焦點、複雜度。
- 具備依賴感知與執行順序。

**Example Task**：
```markdown
- [ ] Task UI-042: Build StudentDashboardHeader component
  **From**: feature_spec_student_dashboard.md v1.3 (sections 2.1, 4.3) + architecture_core_ui.md contracts
  **Acceptance**:
  - Renders user avatar + notification bell per spec 2.1
  - Clicking avatar opens dropdown with profile/logout (state managed locally, no extra API call)
  - Responsive on mobile (Tailwind breakpoints)
  **Context Excerpt**: [paste or link key paragraphs]
  **Suggested Tests**: Unit for rendering states; E2E for dropdown interaction
```

### Phase 4：實作、回饋與活更新
- 將 tasks + plans 提供給 coder agents（你的執行框架、Grok Build 的 plan-search-build + Arena eval、平行 workers 等）。
- 捕捉結果（diffs、test results、review comments、runtime issues、例如「此計劃對 X 不夠清晰」）。
- 回灌到 SIPA：
  - 更新 episodic memory 與結果。
  - 對受影響計劃觸發定向重規劃或 patch（例如：「API response shape 改變 → 更新相關 UI plans 與 common contracts」）。
  - 演進 semantic memory（記錄實作中發現的新模式）。
- 對變更後工件重新執行 critic。
- 持續維護可追溯性。

**Incremental Mode**：當新增或改動 spec 時，透過 graph/index 偵測受影響 modules，僅對那些部分重規劃（並附 diff highlighting）。

---

## 8. 資料模型、綱要與結構化輸出

所有工件都使用一致的 YAML frontmatter + Markdown 章節，並透過 Pydantic 或等效工具強制驗證。

**核心 Frontmatter 綱要**（示例）：
```yaml
---
type: master_plan | architecture | feature_ui | common_component | task_list | critique
component: string
abstraction_level: strategic | tactical | operational
version: string (semver)
traceability: list of "file.md#section-or-anchor" or "req-ID"
dependencies: list of component names
critic_score: float (0-1)
last_refined: ISO date
status: draft | in_review | approved | implemented
tags: list (security-critical, etc.)
---
```

**完整輸出綱要**（高層）：
- Master Plan：roadmap 章節、phase breakdown、帶類型的 module inventory、dependency graph、risk register、初始 traceability matrix。
- Architecture Spec：executive summary、Mermaid 視圖（logical/component、deployment 等）、ADR 清單、interface catalog、quality attribute scenarios、deployment/IaC notes、rationale。
- Feature/UI Spec：精修後的 user stories、完整 acceptance criteria（checklist 或 Gherkin）、interaction flows（編號流程或 state diagram）、UI state & behavior、API contracts（request/response examples）、validation & error matrix、non-functional notes、wireframe prompts。
- Common Component Spec：purpose & scope、public interface（類似代碼或表格）、configuration schema（YAML/JSON）、extension points & hooks、invariants & guarantees、error handling strategy、performance considerations、usage examples、testability notes、migration notes。
- Task List：帶優先級與順序的任務，附 acceptance criteria、context excerpts/links、建議測試、複雜度、owner hints。
- Critique：結構化 JSON（traceability_score、consistency_issues、completeness_gaps、anti_patterns、suggested_patches、overall_verdict、confidence）。

所有輸出都設計為同時適合人類閱讀，也可被機器消費（供下游代理或工具使用）。

---

## 9. RAG、上下文工程與記憶架構

**吸收／分塊策略**：
- Primary：依 heading hierarchy + semantic boundaries（feature、requirement block、component description）分塊。
- Secondary：提取 requirement ID（regex 或 LLM），並標記 component mentions。
- 每個 chunk 的 metadata：file、section path、requirement IDs、component tags、last_modified、embedding。

**檢索（Hybrid + Type-Aware）**：
- Vector similarity（dense embeddings）。
- Keyword / BM25，用於精確 ID 或技術術語。
- 可選 Knowledge Graph traversal（例如：「找出所有追蹤到此 component 或依賴它的 requirements」）。
- 在組裝前對 top-k passages 做 reranking + compression（LLM summarizer 或 extractive）。
- 類型特定 query expansion（例如對 Architecture 加入 `ASR NFR pattern tactic`；對 UI 加入 `acceptance criteria flow edge case`）。

**上下文組裝**：
- 最小充分封包：retrieved passages + compressed summary + relevant memory（此 module 的 episodic decisions、semantic patterns）+ master plan excerpts。
- Isolation：每次 sub-planner 呼叫都使用自己聚焦的上下文；只有在明確需要時才加入全局上下文。

**分層記憶**：
- **Working**：當前 draft artifacts、活躍 retrieval results、進行中的 critic feedback。
- **Episodic**：按 module 記錄規劃會話（使用了什麼輸入、做了哪些決策、精修歷史、若已實作則其結果）。支援回答「與上一版相比改變了什麼？」。
- **Semantic**：一般化、可檢索知識 —— 有效的架構模式、此領域常見陷阱、詞彙表、跨切面原則、可重用 rationale 片段。帶 metadata 儲存，以利精確檢索。

**Knowledge Graph（建議）**：
- Nodes：單個 requirements、components、decisions、plans。
- Edges：traces_to（requirement → plan element）、depends_on、refines、conflicts_with、implements（之後可延伸到 plan → code）。
- 好處：支援 impact analysis（「改變此 requirement 會影響哪些 plans？」）、更豐富檢索，以及面向人類的視覺化。

---

## 10. 評論／評估子系統（評分規則、循環、質量閘門）

**多階段 Critic**（可平行或串行）：
1. **Traceability Critic**：對每個主要主張／決策／視圖／API，是否都帶有明確來源章節鏈接與證據？輸出分數與缺漏清單。
2. **Consistency Critic**：檢查計劃內部（無自相矛盾）、跨計劃（與 master 與兄弟 modules 對齊）、時間一致性（若與前一版本不一致，需有合理解釋）。
3. **Completeness Critic**：是否覆蓋此範圍內所有相關 ASR/NFR？是否漏掉 user stories／edge cases？
4. **Anti-Pattern & Quality Critic**：偵測 God object、tight coupling、缺少錯誤處理、擴展點不清、驗收標準不足等，並透過 RAG 知識判斷好模式。
5. **Implementability / Sizing Critic**：計劃是否能拆成適合 coder 上下文視窗的任務？驗收標準是否可測？是否有明顯阻塞？
6. **ATAM / Tradeoff Critic**（偏架構）：識別 quality attribute scenarios、trade-offs、risks，並產出輕量 mismatch 或 risk register。

**回饋格式**（可直接用於 patch 應用）：
```json
{
  "overall_verdict": "pass | refine | escalate",
  "traceability_score": 0.87,
  "issues": [
    {"severity": "high", "category": "traceability", "description": "...", "suggested_patch": "Add link to spec_v2.md#FR-112 and quote relevant sentence..."}
  ],
  "strengths": [...],
  "recommended_next_action": "..."
}
```

**Refinement Loop**：
- Critic feedback → Sub-planner 接收回饋 + 相關記憶 + 指令，只對有問題的章節做最小化 patch。
- 重新生成受影響章節。
- 再次執行 critic（為提升效率，也可只針對變更區域）。
- 當達到 gate 門檻（例如 traceability ≥ 0.90、無高嚴重度問題）或有 human override 時收斂。

**Gate Examples**：
- Architecture：至少要有 3 個視圖 + 2 個以上附 rationale 的 ADR，並可追溯到主要 ASR。
- Feature/UI：每個 user story 至少要有 3 項 acceptance criteria，覆蓋 happy path + 至少 2 個 edge/error cases；所有引用的 API/contracts 都必須存在於鏈接的 architecture plans 中。
- Common：public interface 必須完整指定（signatures + semantics）；至少文件化一個 extension point；需有 usage example。

---

## 11. Prompt 工程與 Few-Shot 策略

**System Prompts**（角色 + 原則 + taxonomy + output schema）：
- 「你是一位專精於 [type] 的資深軟件架構師／產品負責人／介面設計師。你遵守嚴格可追溯性，只產出要求的抽象層級，且絕不虛構任何未由所提供上下文或檢索來源支持的細節。請務必以精確結構化 Markdown + YAML frontmatter 格式輸出……」

**Chain-of-Thought /「Rethink」Instructions**：
- 內建於每個代理中：「在產出最終結果前，先在內部按 rubric 對草稿做自我評論：可追溯性、與提供上下文及 master plan 的一致性、對此組件類型的完整性、是否缺乏 anti-pattern。之後再套用改進。」

**Few-Shot Examples**：
- 為每種組件類型準備 2–4 個高質量範例（可來自你過往成功計劃，或合成的 gold-standard 範例）。
- 範例應包含完整輸入上下文片段 + 預期輸出。
- 可直接放入 prompt，或經由 semantic memory 動態檢索（例如「相似的過去規劃任務」）。

**Structured Output Enforcement**：
- 使用 Pydantic / instructor library 或 native JSON mode + post-validation。
- 對 Markdown 型重輸出：可先生成 JSON 結構，再渲染為 Markdown 模板（更可靠）。

**Temperature & Sampling**：
- 規劃／綜合：0.3–0.7（在創造性與保真度之間平衡）。
- 評論／評估：0.0–0.2（確定性、一致性較高）。
- Refinement patches：低 temperature。

**xAI Grok / 強推理模型**：
- 適用於 Master Orchestrator、Architecture sub-planner 與 top-level Critic（對複雜分解與 trade-off analysis 的推理最好）。
- 較輕量／較快的模型可用於檢索、簡單分類或高吞吐的任務分解。

---

## 12. 輸出工件模板（各類型完整示例）

（可參考先前的 `software_implementation_planner_agent.md`，其中有具體但簡化的示例。在完整實作中，應維護一個 `templates/` 目錄，存放由代理填充的完整骨架。）

各類型共通但可客製化的核心章節：
- YAML frontmatter（如上）
- Executive / Purpose summary（長度與焦點可依類型調整）
- Traceability & Source References
- 詳細主體（對架構是 views，對 UI 是 acceptance criteria + flows，對 common 是 contracts + extension points）
- Dependencies & Risks
- Open Questions / Assumptions（供 human review）
- Changelog / Refinement History（自動附加）

完整模板應與 SIPA 一同進行版本控制。

---

## 13. 實作路線圖與技術指引

**Phase 1（MVP — 1–2 週）**：
- Corpus indexer + 基礎 hybrid RAG（LlamaIndex 或簡單 embeddings + keyword）。
- Master Orchestrator（分解 + 分類）+ 一個 sub-planner（先從 Feature/UI 或 Architecture 開始）。
- 基礎 Critic（traceability + consistency）與簡單循環。
- Structured output + file writer。
- 在你規格中的一個小型有界 module 上做端到端測試。
- 將輸出整合進一個既有 coder workflow（例如把任務餵給 Cursor 或 Grok Build）。

**Phase 2（核心完整性）**：
- 加入所有主要 sub-planners + 完整 taxonomy。
- Hierarchical memory（working + episodic + semantic）。
- 進階 critic（所有階段、patch application、架構用的 ATAM-lite）。
- Knowledge Graph（輕量即可，例如 NetworkX + LLM 抽取或簡單 edges）。
- Incremental mode + change detection。
- 完整模板函式庫 + few-shot examples。

**Phase 3（生產強化）**：
- 可觀測性（推理軌跡、檢索日誌、critic score 隨時間變化）。
- Human-in-the-loop UI 或 CLI gates（審查 master plan、高風險 plans）。
- 成本／token 最佳化（快取、模型路由、壓縮）。
- 平行執行、重試邏輯、錯誤處理。
- 指標儀表板（traceability scores、refinement 次數、下游 task success rate）。
- 封裝為可重用的 agent/harness 元件（Docker 或 Python package）。

**技術棧建議**（與你的環境對齊）：
- **Orchestration**：LangGraph（非常適合有狀態分層圖與循環）或配合你現有模式的自訂方案。亦可選 CrewAI/AutoGen 作為 role-based 替代。
- **RAG/Memory**：LlamaIndex（先進索引、分層、圖能力）或 Haystack。Chroma/Weaviate/Pinecone 可本地部署。Knowledge Graph 可選 Neo4j 或記憶體內圖。
- **LLMs**：xAI Grok（規劃／評論主力 —— 強推理）；DeepSeek / Qwen / 本地模型用於高吞吐或控成本；Grok Build 用於 plan-search-build + Arena evaluation 有價值的場景。
- **Structured Outputs**：Pydantic + instructor 或 native tool-calling/JSON mode。
- **Diagrams**：Mermaid（Markdown 原生）+ 可選代碼執行來做 PlantUML 或驗證。
- **Storage**：所有 plans/artifacts 存於 Git repo（方便版本化、diff、協作）；可選持久化 vector DB。
- **Integration**：使用 file watcher 或 CLI commands，將輸出寫到 `plans/` 與 `tasks/` 目錄，供你的執行框架消費；如需多代理設置，可暴露為 MCP/tool 或簡單 API。

**Code Structure Sketch**（高層）：
```text
sipa/
├── indexer/          # corpus ingestion, chunking, embedding, graph
├── agents/
│   ├── orchestrator.py
│   ├── architecture_planner.py   # contains Analyst/Modeler/Designer logic
│   ├── feature_ui_planner.py
│   ├── common_component_planner.py
│   ├── critic.py                 # multi-stage or specialized critics
│   └── task_decomposer.py
├── memory/           # working, episodic, semantic managers
├── rag/              # hybrid retriever, compressors, type-specific strategies
├── schemas/          # Pydantic models for all artifacts
├── templates/        # Markdown skeletons + few-shot examples
├── prompts/          # system prompts, few-shot libraries
├── utils/            # diagram gen, traceability validator, patch applier
└── main.py / cli.py  # entrypoints, incremental runner
```

可先以 notebook 或單檔 prototype 快速迭代，再重構成 package。

---

## 14. 與現有工具及執行框架整合

- **輸入**：將 SIPA 指向你現有的大型 spec 資料夾（或一個整理好的索引檔）。它會遵守 `.gitignore` 或明確 include/exclude 清單。
- **輸出消費方式**：
  - 將 `master_plan.md`、按類型劃分的 specs，以及 `tasks_*.md` 放入你的專案 repo。
  - Coder agents（Cursor、Kiro、Claude Code、Grok Build）會像處理 Spec Kit 工件或你手寫的 `task.md` 一樣消費它們。
  - 為每個 module 生成或更新 `AGENTS.md` / Cursor rules，其中帶有來自 plans 的相關摘錄或指令。
- **回饋循環**：解析 coder agent session logs、test results 或 PR comments，然後將結構化結果回饋給 SIPA（可透過簡單腳本，或手動貼入 episodic memory）。
- **Grok Build 協同**：把 SIPA plans 作為 Grok Build plan-search-build 工作流程的高質量輸入；使用 Arena Mode 依照 plan 的 acceptance criteria 評估多種實作方案。
- **自託管／本地模式**：所有元件都可用本地模型 + 本地 vector DB 運行；重推理步驟則可用 xAI API。
- **CI/CD**：可選 hook，在 spec 變更時重建索引、重規劃受影響 modules，或驗證新代碼是否符合當前 plans（traceability 或 contract tests）。

---

## 15. 指標、評估與成功準則

**定量指標**：
- Traceability coverage（具已驗證來源鏈接的 plan elements 百分比）。
- 每個工件通過 gate 前的平均 refinement 次數。
- 與 naive full-corpus 方法相比，在達到相近下游任務成功率下的 context token 減少量。
- 下游 coder agent 在無重大規格偏離下的任務成功／完成率。
- 從 spec change 到更新 plans/tasks 的時間（incremental mode）。
- 專案生命周期中 critic score 的趨勢（模式是否持續改進）。

**定性指標**：
- Human review：「這份計劃是否讓人感覺它已完整且準確捕捉了原始大型規格對此 module 的意圖，而不需要我重新讀完整份文件？」
- 「與原始規格相比，coder agents（或 junior devs）根據這些 plans 實作時，速度是否更快、澄清次數是否更少？」
- 在實作過程中，「我原來不知道有這項需求」的情況是否減少。

**成功門檻（MVP）**：
- 已批准計劃的 traceability ≥ 85%。
- 大多數工件平均 refinement 次數 < 3。
- 在 coder sessions 中，可衡量地減少與上下文相關的失敗或來回澄清。
- 首個真實 module 的使用回饋為正面。

---

## 16. 風險、緩解措施與邊界情況

**風險與緩解措施**：
- **面對雜亂／大型語料時檢索品質差** → 先投資在分塊策略 + metadata + hybrid search。從結構較好的子集開始，並對關鍵索引檔做人工整理。
- **過度或不足分解** → 加入 critic sizing check + master plan 的 human gate。追求 Goldilocks task 尺寸（可在一次聚焦工作時段內完成）。
- **不同 modules 之間計劃不一致** → 加強 semantic memory + 對相關群組做全局 consistency critic pass。Knowledge Graph 會有幫助。
- **非確定性／幻覺** → Structured schemas + critic gates + 低溫 critic + 明確要求「只使用提供的上下文或檢索來源」。版本化使偏移可見。
- **大型專案 token/成本過高** → 範圍化檢索 + 壓縮 + 模型路由（便宜模型做 indexing/retrieval，強模型做 synthesis/critic）+ 常見上下文快取。
- **人工審核造成瓶頸** → 將 gates 設為可配置（對低風險 modules 且 critic score 很高時可自動批准）。提供良好的 diff 視圖與摘要，以加速人工審核。
- **舊系統或結構差的規格** → SIPA 仍有幫助，因為它會強迫進行明確分類與 traceability extraction；但初期可能需要更多人工 seed curation。

**邊界情況**：
- 非常小型專案：仍有助於維持一致結構與活的可追溯性。
- 高度視覺化／UI 密集規格（Figma、screenshots）：可加入 vision model 步驟，先描述 mocks，再將文字描述餵給 Feature/UI planner。
- 語料中存在衝突需求：Critic 會明確指出衝突，交由人類裁決；計劃中需記錄假設。
- 規格快速演進：透過 incremental mode + 強版本控制 + graph-based impact analysis 處理。

---

## 17. 未來擴展與路線圖

- 完整自動化的 **Knowledge Graph RAG**，支援 requirement dependency extraction 與即時 impact analysis。
- **多模態吸收**：利用 vision models 處理規格中的 UI mocks、圖表、白板內容，生成文字描述，甚至初始 wireframes/prompts。
- **自動測試與驗證工件生成**：從 acceptance criteria 生成 property-based tests、contract tests、E2E scenarios 或 monitoring assertions。
- **風險／複雜度評分 + 自動升級**：將高風險或高複雜度計劃標記為需要更多人工審核或更細粒度拆解。
- **Meta-Planner / Self-Optimizer**：分析歷史規劃執行（哪些組件類型需要最多 refinements？哪些 retrieval 策略最有效？）→ 演化 prompt templates、chunking rules，甚至 sub-planner personas。
- **Formal methods bridge**：對高保證模組，從 plans 生成 TLA+ specs、不變量或 model-checking 工件。
- **團隊／企業能力**：按角色控制 plan 存取、匯出到 Confluence/Jira/Notion、CI/CD 政策強制（「代碼若未滿足當前 plan acceptance criteria 則不得合併」）、多專案 semantic memory。
- **領域專用擴展**：為 edtech（HKDSE）、trading UIs、embedded/hardware（ESP32）、legacy modernization（COBOL → modern）等提供預設 taxonomy 與 patterns。

---

## 18. 參考資料與來源

**主要研究**：
- MAAD：arXiv:2606.01385 — "Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory"
- AgentOrchestra：arXiv:2506.12508 — 具最上層 planner + modular sub-agents 的分層多代理框架。
- LLM Multi-Agent Systems for SE survey：arXiv:2404.04834v4
- GoalAct、Self-Organized Agents、ALMAS、HPTSA 及相關分層規劃論文（2025–2026）。
- 上下文工程文獻（LangChain blog 系列、hybrid RAG、graph retrieval 論文）。

**工具與 SDD**：
- GitHub Spec Kit 與其關於 AI agents 規格驅動開發的 blog posts。
- Kiro、Tessl 及相關 spec-first 工具。
- xAI Grok Build 文件（plan-search-build + Arena Mode）。

**更廣泛來源**：
- SWE-agent、MASAI、MetaGPT、ChatDev、執行框架工程論文（awesome-agent-harness）。
- Kruchten 4+1 views、ATAM、ISO/IEC 42010 等架構基礎。

---

**結語**  
這份完整規格故意寫得非常詳盡，目的就是要讓它能作為實作或演進 SIPA 的唯一事實來源。它直接回應你對「將大型規格拆成可管理、細節層級恰當的部分，同時透過可追溯性、評論驅動質量控制與活更新來保留原始意圖」的要求。

你現在可以：
- 直接把這份 MD 當作高層規格，輸入你的 agent harness 來開始建構 SIPA。
- 按第 13 節所述先做 MVP prototype。
- 要求我根據此規格生成更具體的 prompt templates、Pydantic schemas、sample code skeletons，甚至 starter implementation notebook。
- 針對任何章節再做迭代（加入你實際規格中的領域示例、精修 rubrics、擴展模板等）。

此設計是基於你在 AI agent engineering、spec-driven development，以及嚴謹 harness building 方面既有優勢而刻意打造的。隨時可以進入下一步，不論是 refinement、prototyping，還是直接應用到你語料中的真實 module。

*本文件以你自己的系統哲學為基礎設計：深度 rethink、質量閘門、可追溯性，以及務實的生產導向。*
