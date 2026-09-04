# 任務：建構超生產級混合代理 RAG 系統 - 詳盡的架構和實施規範（2026 年 4 月）

** 從 Creator 到 task.md 的初始提示 **
```
# How to create backend services
FIRST:
Conduct a comprehensive analysis and research of the task.md file to fully understand all requirements, specifications, 
and technical details. Based on this analysis, design and implement a complete backend server architecture that fulfills 
all outlined requirements. The backend server must be created within a dedicated 'backend' folder structure. Ensure the 
implementation includes proper API endpoints, database schema design, authentication mechanisms, error handling, logging 
systems, and follows RESTful principles. Document all API endpoints with clear specifications, implement comprehensive 
unit and integration tests, and verify that the server handles all edge cases and scalability requirements mentioned in 
task.md.
THEN:
Configure the application to integrate with GROK from x.ai by utilizing the environment variables defined in backend/.env  . 
Update all relevant codebase components to establish GROK as the primary Large Language Model (LLM) provider. This includes 
modifying API connection configurations, authentication parameters, model endpoints, and any existing LLM integration code 
to ensure seamless communication with GROK services. Implement proper error handling, rate limiting, and fallback mechanisms.
Verify the integration by testing all LLM-dependent features including text generation, chat completions, and any custom 
model interactions. Document the configuration changes and ensure backward compatibility where applicable.

# How to create frontend services
Conduct comprehensive research and analysis of the task.md requirements document to architect and implement a complete 
frontend application with integrated backend services and knowledge-base functionality. Design and develop the frontend 
solution with the following specifications: analyze all functional requirements from task.md, create responsive UI 
components with modern frameworks, implement state management for complex data flows, establish API integrations with 
backend services, incorporate knowledge-base search and retrieval features, optimize performance for fast load times, 
implement accessibility standards (WCAG 2.1), create intuitive navigation patterns, add comprehensive error handling and 
user feedback mechanisms, ensure cross-browser compatibility, implement proper security measures for data handling, write 
unit and integration tests for all components, document the codebase with clear comments and README files, and save the 
complete frontend project structure to the designated frontend folder. The final deliverable must provide exceptional user 
experience through thoughtful interaction design, consistent visual hierarchy, smooth animations, mobile-first responsive 
design, and intuitive user workflows that minimize cognitive load while maximizing task completion efficiency.

```
**任務負責人：** 編碼代理
**優先：** 關鍵
**預計工作量：** 10–14 天（6 天完成 MVP 核心；剩餘幾天內完成全面、混合集成、wiki 複合、可觀察性和基準測試）
**目標：**交付一個**完整的、生產就緒的、可觀察的、可評估的、可擴展的和基準化的 Agentic RAG 系統**，該系統**精確地**實現了調查論文“Agentic Retrieval-Augmented Generation: A Survey on 36設計模式** 和 **7 個架構元素**以及 YouTube 影片“Agentic RAG 概述：4 個核心原則和 7 個架構元素！” （https://youtu.be/MT3DM82PRLc).

系統**必須**：
- 使用**分層分塊**和記憶體安全、增量、可恢復處理，以本機方式攝取和索引您的 **~65,000 個 Markdown 檔案（~500 MB 語料庫）**。
- 支援**混合知識表示**：Chroma 向量儲存 + **LightRAG**（最新 2026 版本，支援 OpenSearch 後端），用於實體關係圖和雙層檢索。
- 透過可選的 Karpathy 風格的 LLM Wiki 輸出（`wiki_output/`Vault with `index.md`、`log.md`、concepts/、frontmatter、[[links]]`）包括**持久性知識複合**。
- 完全本地優先、Docker 化、可追蹤 (LangSmith) 和生產強化。

該規範是經過 10 多次細化迭代後對整個對話歷史進行的**最終的、經過深思熟慮的綜合**：原始 Agentic RAG 請求 → Karpathy Wiki 比較表 → LightRAG 增強 → 65k MD 的規模 → 重複調用更深層次的設計細節。

## 1. 論文中的核心概念（精確映射－不可協商）

**4 核心代理設計模式**（必須以明確圖形循環/條件邊可見）：
1. **反思** - 代理人使用評分標準和迭代（Self-RAG 風格的反思標記或評分器循環）自我評估輸出（相關性、忠誠度、幻覺）。
2. **規劃** — 將複雜查詢自主分解為子任務或多跳計劃。
3. **工具使用** — 動態、交錯的工具呼叫（ReAct 風格：思考 → 行動 → 觀察）。
4. **多代理協作** - 具有共享狀態、分層監督或平面對等協調的專業代理。

**7個架構元素**（設計中明確實現）：
1. 單一代理路由+多代理委託。
2. 分層/基於圖形的控制流（LangGraph Pregel 執行）。
3. 自適應檢索（查詢複雜度→策略選擇）。
4. 狀態記憶（對話+長期索引+檢查點）。
5. 混合知識（向量+輕量級KG+持久Markdown）。
6. 透過質量門和最大迭代進行迭代細化。
7. 評估感知（內建指標、追蹤、健康檢查）。

**關鍵區別**（包括 README.md 中更新的比較表）：
- 優於天真的 RAG（添加代理）。
- 優於純 Karpathy Wiki（查詢時代理推理 + 可選回寫）。
- LightRAG 增加了快速的關係能力，而無需沉重的 GraphRAG 重建成本。

## 2. 完整的系統架構（Mermaid – 包含並渲染在 README 中）

```mermaid
graph TD
    User[User Query via CLI/Streamlit] --> Router[Query Analyzer Router<br/>Adaptive Strategy Selection]
    Router --> Planner[Planner Agent<br/>Decompose + Multi-Hop Plan]
    Planner --> ToolRouter[Tool Router<br/>Structured Decision: Vector | LightRAG | Web | Wiki]
    ToolRouter --> Vector[Vector Retriever<br/>Chroma MMR + Hierarchical + Rerank]
    ToolRouter --> LightRAGNode[LightRAG Dual-Level Retriever<br/>Entity + Relation Graph]
    ToolRouter --> Web[Tavily Web Search Tool]
    Vector & LightRAGNode & Web --> Researcher[Researcher + Grader Agent<br/>Reflection Loop + Doc Rubric Scoring]
    Researcher -->|grade < 0.85 & iterations < 3| Planner
    Researcher --> Generator[Generator Agent<br/>Synthesize with Citations]
    Generator --> Critic[Critic Agent<br/>Faithfulness + Hallucination Check]
    Critic -->|fail| Researcher
    Critic --> Final[Final Answer + Citations]
    Final --> WikiSynth[Optional Wiki Synthesizer Agent<br/>Karpathy-style Persistent Output]
    subgraph "State & Memory"
        State[AgentState + MemorySaver Checkpoints<br/>Conversation Summary + Long-term Index]
    end
    subgraph "Hybrid Knowledge Layer"
        Chroma[Chroma Vector DB<br/>Parent/Child Hierarchical Chunks]
        LRAG[LightRAG KG<br/>Entities, Relations, OpenSearch Backend]
    end
    WikiSynth --> WikiVault[wiki_output/ Vault<br/>index.md + log.md + concepts/]
```

## 3. 詳細的資料模型（Pydantic v2 – 必需）

創建`src/graph/state.py`：

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Annotated, Literal
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from langchain_core.documents import Document

class RetrievedDoc(BaseModel):
    doc: Document
    relevance_score: float = Field(..., ge=0.0, le=1.0)
    source: str
    chunk_type: Literal["parent", "child"]
    headers: List[str] = Field(default_factory=list)
    lightrag_entities: List[str] = Field(default_factory=list)
    lightrag_relations: List[Dict] = Field(default_factory=list)

class AgentState(BaseModel):
    messages: Annotated[List[BaseMessage], add_messages]
    query: str
    plan: Optional[List[str]] = None
    retrieved_docs: List[RetrievedDoc] = Field(default_factory=list)
    critique: Optional[str] = None
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    iterations: int = Field(default=0, ge=0, le=3)
    final_answer: Optional[str] = None
    citations: List[Dict[str, str]] = Field(default_factory=list)
    wiki_output_path: Optional[str] = None
    lightrag_context: Optional[Dict] = None
    metadata: Dict = Field(default_factory=dict)  # tracing, timestamps, etc.
```

使用`checkpointer = MemorySaver()`（或用於生產持久性的AsyncSqliteSaver）。

## 4. 每個節點的詳細設計（合約、輸入/輸出、提示）

`src/agents/`中的所有節點；每個都接受`state: AgentState`並返回`partial dict`以進行狀態更新。

1. **query_analyzer**：將複雜性分類（簡單/事實與多跳/關係）。決定路線。提示：`prompts/analyzer.md`（基於標題的分類）。

2. **規劃器**：輸出編號計畫或子查詢。多跳的少量範例（例如，「比較 X 和 Y」→ 每個 + 合成的子查詢）。

3. **tool_router**：結構化輸出（Pydantic 模型）選擇工具+參數。在安全的情況下支援並行工具呼叫。

4. **研究員_評分者**：
   - 執行選定的檢索器（向量+可選的 LightRAG）。
   - 使用詳細的評分標準（相關性、完整性、新近度、權威性）對每個文件進行評分。
   - 過濾（閾值 0.75）並反映收集是否較弱。
   - 反射循環的條件邊。

5. **生成器**：使用過濾後的文件、計劃和批評來產生帶有內嵌引用的接地答案。

6. **評論家**：獨立評分（使用 RAGAS 風格或自訂 LLM 評判的忠實度 0-1）。如果低，則觸發循環。

7. **wiki_synthesizer**：產生黑曜石相容的 Markdown（YAML frontmatter：`source`、`date`、`tags`、`confidence`;明確 [[WikiLinks]]；更新 `index.md` 和 `log.md`）。

**提示庫** (`src/prompts/`)：每個節點一個 `.md` 文件，其中包含：
- 嚴格的系統角色+任務。
- 詳細的標題或輸出格式（首選 JSON 模式）。
- 2-4 個少數樣本（正面 + 負面）。
- 鼓勵反思/計劃的思想鏈。

## 5. 混合檢索和索引設計（65k MD 規模 - 關鍵）

**攝取管道**（`src/ingestion/pipeline.py` – 記憶體安全，增量）：

- **載入器**：`DirectoryLoader` 和 `**/*.md`，multiprocessing.Pool（16-32 個工作線程，批次大小 2000-5000 個檔案）。
- **分層分塊**（2026 年 Markdown 最佳實踐）：
  1. `MarkdownHeaderTextSplitter`（標頭層級 1–4）→ 父區塊（~2000–4000 個標記），在元資料中具有完整的標頭路徑。
  2. `RecursiveCharacterTextSplitter(chunk_size=400–512, chunk_overlap=50–100)` 父親內容 → 子區塊。
  3. 透過`parent_id` UUID 連結。
- **向量索引**：Chroma.from_documents（父/子的單獨集合或元資料標誌）。使用 MMR 檢索。
- **LightRAG 索引**：向量之後，`lightrag.insert_batch(parent_chunks)`（非同步，實體/關係提取）。使用 OpenSearch 後端進行擴充（包括 Docker compose）。支援透過哈希/時間戳檢查進行增量。
- **可恢復性**：帶有已處理檔案雜湊值的 JSON 檢查點。每批後進行 GC。
- **目標效能**：在 32 GB RAM 機器上完全攝取 <45 分鐘；對於小變化，增量<1分鐘。

**檢索邏輯**：
- 向量：`k=15`、`fetch_k=50`、重新排序器（可選 Cohere 或交叉編碼器）。
- LightRAG：`mode="hybrid"`（低階實體+高階關係）。
- 自適應：路由器更喜歡 LightRAG 來查詢「比較」、「如何」、「關係」、「誰連接到」。

## 6. 工具（動態和可擴展）

- `hybrid_retrieve(query: str, use_lightrag: bool = True)`
- `web_search_tavily`
- `wiki_writer(markdown_content: str, title: str)`
- 計算器、arXiv fetcher（獎勵）。

## 7.圖構建(`src/graph/agentic_rag_graph.py`)

- `StateGraph(AgentState)`
- 新增節點+條件邊進行反射（`should_continue_reflection`基於置信度/迭代）。
- 盡可能並行工具執行。
- 每個節點上的完整 LangSmith 追蹤（回調）。

## 8. UI、CLI、評估和生產功能

- **Streamlit** (`app.py`)：聊天介面 + 可擴展的推理追蹤（帶有分數、文件、評論的逐節點）+「儲存到 Wiki」按鈕。
- **Typer CLI** (`cli.py`)：`ingest --resume`、`query "..." [--hybrid] [--wiki] [--trace]`、`lint-corpus`、`eval`、`build-wiki`。
- **評估工具** (`src/evaluation/`)：RAGAS（忠誠度、答案相關性、上下文精確度）+ 自訂反射分數。 50+ 黃金查詢測試集。使用 JSON 報告自動運行。
- **可觀察性**：每次運行的 LangSmith 專案；代理指標的自訂元資料。
- **Docker**：多容器組合（應用程式 + Chroma + LightRAG OpenSearch + 可選的 PostgreSQL）。
- **錯誤處理**：優雅的回退、重試邏輯、速率限制。

## 9. 分階段實施計畫（嚴格順序－有檢查點）

**階段 0**：專案框架、requirements.txt、設定、資料模型、提示範本、Docker 撰寫。  
**階段 1**：攝取管路 – 完整的 65k MD 基準測試 + 增量模式 + LightRAG 索引。  
**階段 2**：混合檢索器 + 工具實作。  
**階段 3**：LangGraph 核心（狀態、節點、邊、反射/規劃循環、記憶體）。
**階段 4**：多主體協作 + 評論家 + wiki 合成器。  
**階段 5**：Streamlit UI + CLI + 追蹤視覺化 + 評估工具。  
**第 6 階段**：Docker、測試、日誌記錄、安全性（API 金鑰）、自述文件（圖表、比較表、基準測試）。  
**階段 7**：端對端壓力測試（100 個複雜查詢）、延遲/品質基準、最終完善。

## 10. 成功標準（可衡量和可驗證）

1. 增量攝取完整 65k MD 語料庫，不會出現 OOM 或崩潰；記錄基準。
2. 每個複雜的查詢追蹤都明顯地展示了**所有 4 種模式**和 **7 個元素**。
3. 反射循環會觸發 ≥30% 的查詢，並顯著提高置信度/品質。
4. 與純向量相比，LightRAG 混合模式在關係/多跳查詢方面表現出卓越的效能。
5. Wiki 合成生成乾淨的、黑曜石就緒的庫，並具有適當的標題和連結。
6. 評估：忠誠度≥0.92，答案相關性≥0.90，消費性硬體上的平均延遲<4秒。
7. 程式碼乾淨、類型齊全（Pydantic + mypy）、文件化、每階段 git 提交。

## 11. 參考資料與推薦入門

- 論文PDF：https://arxiv.org/pdf/2501.09136
- YouTube 影片：https://youtu.be/MT3DM82PRLc
- LightRAG GitHub（2026 功能）：https://github.com/hkuds/lightrag（OpenSearch 支援）
- Karpathy LLM Wiki Gist（用於 wiki_output 樣式）：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- LangGraph Agentic RAG 範例（2026 版）

**立即行動**：立即從**階段 0 + 階段 1** 開始。首先關注 65k MD 語料庫的穩健、可恢復攝取。

當攝取完成並進行基準測試後，請聯繫我以獲取詳細的提示審查和圖形連接會話。

這是**規格、超細緻的生產級 Agentic RAG 實作**，具有混合 LightRAG 和持久的 Karpathy 風格複合。交付它乾淨、可觀察且高性能。 🚀
