**技術規格：通用創意代理商 (GCA) – 版本 1.0**
**日期：** 2026 年 5 月 26 日
**基於：** 完整的對話歷史記錄（使用者原始統計離群值模型→迭代細化→戰略稀疏離群值重組（SSOR）模型）
**目標：** 實施系統的高級 AI/ML 工程師或編碼代理
**許可證：** 開放供內部使用；所有組件均模組化且可擴展

---

### 1. 系統概述及目的
**通用創意代理程式 (GCA)** 是一個 **有狀態、模組化、LLM 協調的多代理系統**，可操作 **戰略稀疏異常重組 (SSOR) 創造力模型**。

**核心目標**
透過系統地將任何輸入情況/問題轉化為**新穎但有用的**創意輸出：
- 透過多個統計觀點 (POV) 繪製情況圖。
- 策略性地對**稀疏**（1-4）個離群維度進行抽樣。
- 將它們重新組合成新的模式。
- 採用嚴格的價值門控選擇（倒U型新穎性平衡+實用性+連貫性+可行性）。

**關鍵差異化因素**
- SSOR 公式的明確實作（請參閲第 3 節）。
- 用於零代碼域特定代理的內建 **CreativeAgentFactory**。
- **人工智慧原生 POV** 源自人類自然語言自動編碼器（NLAE，2026）。
- 每個輸出的完全可追溯性、驚喜向量和創造力評分。
- 對學習到的分佈和成功模式的持久記憶。

**支援的模式**
- 一般創意任務。
- 特定領域的代理（科學、藝術、商業創新、工程、教育等）。
- 互動式多輪會話與人機互動優化。

---

### 2. 高層架構（美人魚圖）

```mermaid
graph TD
    subgraph User_Input
        Problem[Problem + Context + Domain]
    end

    User_Input --> GCA[GeneralCreativeAgent Orchestrator]

    subgraph Factory
        Factory[CreativeAgentFactory] --> DomainAgent[DomainSpecificAgent]
    end

    GCA --> Factory

    GCA --> SSOR[SSOR Engine]

    subgraph Phases
        SSOR --> P1[Phase 1: Multi-POV Mapping]
        SSOR --> P2[Phase 2: Normal Range Definition]
        SSOR --> P3[Phase 3: Sparse Outlier Sampling]
        SSOR --> P4[Phase 4: Cross-Dimensional Recombination]
        SSOR --> P5[Phase 5: Value-Gated Selection]
        SSOR --> P6[Phase 6: Integration & Refinement]
        SSOR --> P7[Phase 7: Output & Model Update]
    end

    subgraph Storage
        VectorDB[FAISS/Chroma Vector Store + Semantic Graph]
        Memory[Session + Long-Term Memory]
    end

    Phases --> VectorDB
    Phases --> Memory

    subgraph LLM_Layer
        LLM[Pluggable LLM Backend<br>Grok / Claude / GPT-4o / Ollama]
    end

    Phases <--> LLM
    GCA <--> Visualization[Plotly / Matplotlib Surprise Vectors & Pareto Fronts]
```

---

### 3. SSOR模型－正式且可實施的定義

**創造力得分**
\[
\operatorname{Cr}(y \mid c, v, g) = B\bigl(N(y), K(y)\bigr) \cdot U(y) \cdot Q(y) \cdot F(y)
\]

**元件實作（Python 風格的偽代碼）**
```python
def novelty_score(y, distributions) -> float:
    # Negative log joint probability or Mahalanobis distance across POVs
    ...

def combination_score(y, semantic_graph) -> float:
    # Semantic distance × co-occurrence rarity
    ...

def balance_function(total_surprise: float) -> float:
    # Inverted-U (Gaussian centered ~moderate surprise)
    return math.exp(-((total_surprise - 0.5)**2) / (2 * 0.15**2))

def usefulness(y, context_metrics) -> float: ...
def coherence(y, semantic_graph) -> float: ...
def feasibility(y, constraints) -> float: ...
```

**稀疏約束（硬編碼）**：每次重組最多 4 個離群值維度（在第 3 和第 4 階段強制執行）。  
**轉型標誌**：當倖存的想法重寫任何原始 POV 分佈時檢測到。

---

### 4. 核心資料模型（Pydantic v2）

```python
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
import numpy as np

class POV(BaseModel):
    name: str
    description: str
    expected_distribution: Dict[str, Any]  # features → stats or embedding cluster
    ai_native_mode: Optional[str] = None   # e.g., "anticipatory_planning"

class SurpriseVector(BaseModel):
    pov_scores: Dict[str, float]  # POV name → surprise score (0-1)
    total_surprise: float
    outlier_dimensions: List[str]

class CandidateIdea(BaseModel):
    title: str
    description: str
    surprise_vector: SurpriseVector
    novelty: float
    value: float
    coherence: float
    feasibility: float
    overall_cr: float
    trace: List[Dict]          # full SSOR phase trace
    transformational: bool = False
    prototype_plan: str
    risks_mitigations: str
```

---

### 5. 7階段詳細實施

**階段 1：多 POV 映射**
- 輸入：情況
- 產出：8–12 個 POV（混合人類角色 + 來自 NLAE 的 AI 原生角色）
- AI 原生 POV（來自人類 NLAE 研究的完整清單）：預期規劃、評估意識、欺騙避免、隱藏動機、語言切換、元模型意識、古怪行為、重建保真度、激活方向、往返一致性、錯位根本原因、潛在特徵集成。  
- 實施：`POVGenerator.generate(situation, num_povs=12, include_ai_native=True)`

**階段 2：正常範圍定義**
- 對於每個 POV：LLM 產生常規/高機率特徵/後果。

**階段 3：戰略稀疏異常值抽樣**
- 受控温度 + 負面提示，將每個 POV **僅 1-4** 維度採樣為離群值尾部。  
- 透過組合約束強制稀疏性。

**第四階段：跨維度重組**
- 使用語意圖遍歷（Chroma/FAISS）來確保可達性。  
- 生成組合（受稀疏性限制的笛卡爾積）。

**階段 5：價值門控選擇**
- 計算每位考生的完整 SSOR 分數。  
- 如果 > N 個候選者，則倒 U 型平衡 + Pareto 前緣排名。  
- 每個域可配置的過濾器閾值。

**階段 6：整合與細化**
- 自我批評循環（執行控制風格提示）。  
- 檢查轉型潛力。

**階段 7：輸出與模型更新**
- 豐富的 Markdown + JSON 輸出。
- 將獲勝的想法作為新的「傳統」模式保留在記憶中。

---

### 6. CreativeAgentFactory實現

```python
class CreativeAgentFactory:
    def create(
        self,
        domain: str,
        domain_knowledge: str | VectorStore,
        custom_povs: List[str] = None,
        custom_value_metrics: Dict[str, callable] = None,
        few_shot_examples: int = 5,
        **kwargs
    ) -> DomainSpecificAgent:
        # Clone base GCA
        # Inject domain-specific POVs, metrics, knowledge base, constraints
        # Override phases as needed via dependency injection
        ...
```

**預裝領域**：科學研究、藝術/創意寫作、商業/產品創新、工程/設計、教育/教育學。

---

### 7. 技術堆疊和依賴關係
- **語言**：Python 3.11+
- **代理框架**：LangGraph（首選）或 CrewAI/AutoGen 用於編排
- **LLM 整合**：LangChain LLM 抽象（Grok、Claude 3.5/4、GPT-4o、透過 Ollama 本地）
- **向量儲存**：FAISS（快速）或 Chroma（持久）
- **数据验证**：Pydantic v2
- **Visualization**: Plotly + Matplotlib
- **非同步**：asyncio +並發.futures
- **测试**：pytest + LangChain 评估工具
- **日誌記錄**：具有全階段追蹤的結構日誌

---

### 8. 介面和API
- **Python 類別 API**（初級）
- **CLI** (`gca --problem "..." --domain "science"`)
- **REST/Streaming API**（FastAPI 可選包裝器）
- **LangChain Tool** 導出供外部代理使用

---

### 9. 評估、測試和指標
- **內部指標**：新穎性、實用性、連貫性、總體 Cr 分數（與 CreativityPrism / Hou 等人 2025 年一致）
- **基準**：LiveIdeaBench、CreativeBench-Combo/Explore（arXiv 2025–2026 論文）
- **單元測試**：每個階段+端到端的歷史創意案例研究
- **人類/人工智慧盲評估**：新穎性+有用性評級

---

### 10. Security, Ethics & Guardrails
- 内置拒绝有害/非法想法
- POV 產生中的偏差檢測
- 審計的可追溯性
- 每个域可配置的安全层

---

### 11.相关研究与实施参考（2024-2026）
- **顧等人。 (2024)** arXiv:2412.14141 – “LLM 可以實現組合創造力” – 與 GCA 核心直接相當的基於代理的架構。
- **夏皮羅等人。 (2025)** arXiv:2509.21043 – 組合創造力基準與縮放法則。
- **CREA (2025)** NeurIPS – 多智能體協作創意影像框架。
- **Anthropic NLAE (2026)** – 用於 AI 原生 POV 的自然語言自動編碼器。
- **烏齊等人。 (2013)** *Science* + **SciSciNet (2023)** – 稀疏異常值的經驗基礎。
- **Boden (2004/2009)** – 理论支柱。

---

**本技術規格完整、獨立且可直接實施。 **

它將對話歷史的每個元素（使用者的原始統計直覺+所有改進）轉化為精確的工程工件。  

**編碼代理的下一步**：使用本文檔+之前的`task.md`開始實作。  

如果您需要，请告诉我：
- 代码中的完整类骨架
- 每个阶段的详细提示模板
- Mermaid architecture expansions
- BibTeX 參考文獻

GCA 现已完全指定用于生产级开发。