# VA-Agent-Swarm — 系統參考與整合地圖

> **用途：** 本文檔為單一入口，將所有代理規格、工作流程、技術架構及支援資源串連成一個完整的系統視圖。它描繪每個組件與整體的關係，定義整合點，並為實施者提供導航。

---

## 目錄

1. [系統概覽](#1-系統概覽)
2. [架構層級](#2-架構層級)
3. [代理類別與規格地圖](#3-代理類別與規格地圖)
4. [基礎設施與支援代理](#4-基礎設施與支援代理)
5. [跨領域功能](#5-跨領域功能)
6. [工作流程整合](#6-工作流程整合)
7. [數據流與交接合約](#7-數據流與交接合約)
8. [UI 與通訊層](#8-ui-與通訊層)
9. [技術堆疊參考](#9-技術堆疊參考)
10. [參考材料索引](#10-參考材料索引)
11. [實施優先順序與依賴關係](#11-實施優先順序與依賴關係)

---

## 1. 系統概覽

**VA-Agent-Swarm** 是一個層級式多代理系統（MAS），旨在完全自動化（或增強）專業影片製作 — 從最初的創意簡報到最終交付至所有分發渠道。系統包含 **114 個專門代理**，組織為 10 個功能類別，由專用基礎設施代理、共享批評匯流排及統一編排執行環境支援。



### 核心設計原則

| 原則 | 描述 | 參考 |
|------|------|------|
| **代理圖** | 代理作為 DAG 節點，具有交接和審查閘門 | [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1 |
| **自我精煉 + 批評** | 每個代理起草 → 自我批評 → 按評分標準修訂 | Madaan et al., 2023 |
| **共享製品合約** | 機器可讀清單在所有階段間流動 | [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.3 |
| **人在迴圈閘門** | 關鍵決策升級至人工審批 | [agents.md](./agents.md) — ProducerAgent |
| **溯源（C2PA）** | 每個製品均已簽署；下游代理驗證鏈 | C2PA 規範 |
| **持續自我改進** | 代理從結果中學習，儲存情節記憶，提升品質 | Reflexion (Shinn 2023) |

### 系統邊界

```
┌─────────────────────────────────────────────────────────────────────────┐
│  用戶 / 客戶簡報                                                          │
└───────────┬─────────────────────────────────────────────────────────────┘
            ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  第一層：UI 前端 — React 19 + Next.js 15                                  │
│  （專案創建、代理管理、即時監控）                                           │
└───────────┬──────────────────────────────────┬──────────────────────────┘
            │ REST/GraphQL（指令）              │ WebSocket（即時串流）
            ▼                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  第二層：API 閘道 + 編排後端                                               │
│  FastAPI + LangGraph + Temporal + Redis 事件匯流排                        │
└───────────┬──────────────────────────────────┬──────────────────────────┘
            │ 代理任務佇列                      │ 工具 API 呼叫
            ▼                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  第三層：代理執行環境 — 114 個代理定義                                      │
│  LLM 供應商：Grok-4.x、Gemini 2.5 Pro、GPT-4o、Claude 4                  │
│  工具存取：Sora 2、Veo 3.1、Runway Gen-4、ElevenLabs、DaVinci 等          │
└─────────────────────────────────────────────────────────────────────────┘
```

> **完整架構詳情：** [ui/architecture_communication.md](./ui/architecture_communication.md)



---

## 2. 架構層級

系統組織為 **7 個執行層**，每個代理均參與其中：

| 層級 | 職責 | 主要代理 / 服務 |
|------|------|----------------|
| **編排** | 規劃、路由、排程、重試、升級 | PlannerAgent (#54)、OrchestratorAgent (#53)、RouterAgent (#55)、JudgeAgent (#56) |
| **資產與數據骨幹** | 不可變資產 ID、版本控制、依賴邊、權利 | 資產儲存（S3 + 元數據資料庫） |
| **訊息與狀態架構** | 批評匯流排、工作狀態、閘門決策 | Redis Streams / NATS、持久狀態儲存 |
| **品質與連續性網格** | 多輪 QC、連續性、無障礙、合規 | AIQAConsistencyAgent (#49)、ComplianceAgent (#37)、AccessibilityAgent |
| **可觀測性與重播** | 即時狀態、失敗原因、瓶頸、重播 | AgentOps 管道、LangSmith 追蹤 |
| **交付架構** | 將母帶打包為各渠道特定版本 | TrailerEditorAgent (#51)、SocialMediaStrategistAgent (#28) |
| **運算與儲存擴展** | GPU 自動擴展、分層儲存 | 基礎設施層（Docker/K8s） |

> **完整層級規格：** [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.2

---

## 3. 代理類別與規格地圖

114 個代理組織為 10 個類別。以下每個類別連結至主要名冊及任何提供實施級別詳情的深度規格文檔。

### 3.1 幕前代理（1–5）

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 1 | DirectorAgent | 掌管視覺；鏡頭意圖、節奏、審批 | — |
| 2 | ProducerAgent / EP | 預算、進度、階段閘門 | — |
| 3 | ScreenwriterAgent | 企劃書 → 劇本；對白；結構 | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| 4 | ShowrunnerAgent | 跨集弧線、編劇室編排 | — |
| 5 | CastingAgent | 聲音 + 形象選擇；試鏡 | — |

**名冊參考：** [agents.md](./agents.md) §1



### 3.2 攝影與燈光代理（6–8）

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 6 | CinematographerAgent (DoP) | 鏡頭、燈光、構圖、風格 | — |
| 7 | CameraOperatorAgent | 取景、對焦、運鏡 | — |
| 8 | DronePilotAgent | 航拍攝影 | — |

**名冊參考：** [agents.md](./agents.md) §2

### 3.3 剪輯與調色代理（9–18）

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 9 | EditorAgent | 組裝剪接；節奏 | — |
| 10 | ColoristAgent | 最終調色；風格一致性 | — |
| 11 | VFXSupervisorAgent | VFX 管線監督 | — |
| 12 | AnimatorAgent (2D/3D) | 角色動態、時間掌控 | — |
| 13 | MotionGraphicsAgent | 動態字體、資訊圖表 | — |
| 14 | StoryboardAgent | 劇本 → 分鏡圖 | — |
| 15 | ConceptArtistAgent | 世界觀/角色設計 | — |
| 16 | ProductionDesignAgent | 場景、外景、世界風格 | — |
| 17 | CostumeDesignAgent | 角色服裝 | — |
| 18 | MUAAgent | 化妝/髮型/特效化妝 | — |

**名冊參考：** [agents.md](./agents.md) §3

### 3.4 聲音與音樂代理（19–22）

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 19 | SoundDesignAgent | 環境音、擬音、音效 | — |
| 20 | ComposerAgent | 原創配樂 | — |
| 21 | VoiceOverAgent | 旁白、角色配音 | [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md)（共用模式） |
| 22 | SoundMixerAgent | 最終混音；5.1/Atmos 交付物 | — |

**名冊參考：** [agents.md](./agents.md) §4

### 3.5 表演與編舞代理（23–27）

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 23 | ChoreographyAgent | 動作設計 | — |
| 24 | MusicVideoDirectorAgent | 歌曲視覺概念 | — |
| 25 | ComedyWriterAgent | 短劇、惡搞、病毒式迷因 | — |
| 26 | TalentAgent（鏡頭前） | AI 渲染表演 | — |
| 27 | UGCCreatorAgent | 真實感廣告 | — |

**名冊參考：** [agents.md](./agents.md) §5



### 3.6 分發與行銷代理（28–31）

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 28 | SocialMediaStrategistAgent | 平台分發、趨勢 | — |
| 29 | CopywriterAgent | 腳本、字幕、鉤子 | — |
| 30 | CreativeDirectorAgent | 企劃概念 | — |
| 31 | PerformanceMarketerAgent | 優化廣告 ROAS | — |

**名冊參考：** [agents.md](./agents.md) §6

### 3.7 教育與領域專家代理（32–45）

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 32 | InstructionalDesignAgent | 學習目標 → 內容 | — |
| 33 | SMEAgent | 領域準確性 | — |
| 34 | FactCheckerAgent | 來源級別驗證每項聲明 | — |
| 35 | MedicalIllustratorAgent | 解剖與程序視覺化 | — |
| 36 | JournalistAgent | 報導 + 倫理 | — |
| 37 | ComplianceAgent（法律） | FTC、HIPAA、GDPR、IP 許可 | — |
| 38 | FinanceAgent | 市場/收益準確性 | — |
| 39 | FoodStylistAgent | 攝影就緒食物 | — |
| 40 | TravelCineAgent | 目的地攝影 | — |
| 41 | ChildrensAuthorAgent | 年齡適當內容 | — |
| 42 | AudiobookNarratorAgent | 持續敘述 | — |
| 43 | SignLanguageInterpreterAgent | ASL/BSL 手語翻譯 | — |
| 44 | LocalizationQAAgent | 翻譯 + 文化適配 | — |
| 45 | RealEstatePhotoAgent | 室內、3D 掃描 | — |

**名冊參考：** [agents.md](./agents.md) §7

### 3.8 AI 時代專家代理（46–52）

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 46 | PromptEngineerAgent | 製作提示詞；引導生成模型 | — |
| 47 | AvatarDesignAgent | 合成主持人身份 | — |
| 48 | VoiceCloneAgent / LipSync | 聲音克隆 + 唇形同步 | — |
| 49 | AIQAConsistencyAgent | 幀漂移、瑕疵、身份斷裂 | — |
| 50 | PersonalizationEngineerAgent | 可變模板（姓名/面部替換） | — |
| 51 | TrailerEditorAgent | 鉤子驅動預告片剪接 | — |
| 52 | SportsAnalystAgent | 戰術分析 + 圖表 | — |

**名冊參考：** [agents.md](./agents.md) §8



### 3.9 專家元代理（53–80）

這些代理管理編排、品質、連續性及系統級別事務：

| # | 代理 | 角色 | 深度規格 |
|---|------|------|----------|
| 53 | OrchestratorAgent | DAG 執行、重試、扇入/扇出 | — |
| 54 | PlannerAgent | 將簡報分解為分階段 DAG | — |
| 55 | RouterAgent | 為子任務選擇正確代理 + 模型 | — |
| 56 | JudgeAgent | 通過辯論裁決爭議 | — |
| 57–80 | （各種元代理） | 記憶、連續性、安全、升級等 | — |

**名冊參考：** [agents.md](./agents.md) §9

### 3.10 工作流程支援代理（81–114）

這些代理提供製作基礎設施服務：

| 範圍 | 功能 | 範例 |
|------|------|------|
| 81–90 | 資產管理、版本控制、渲染調度 | RenderFarmAgent、AssetManagerAgent |
| 91–100 | 品質閘門、交付打包、合規 | DeliveryAgent、QCGateAgent |
| 101–114 | 分析、回饋循環、重新訓練觸發 | AnalyticsAgent、FeedbackLoopAgent |

**名冊參考：** [agents.md](./agents.md) §10

---

## 4. 基礎設施與支援代理

這些跨領域代理擁有自己的**深度功能與技術規格**，因為它們服務於整個系統：

| 代理/系統 | 在 VA-Agent-Swarm 中的用途 | 規格文檔 |
|-----------|---------------------------|----------|
| **研究代理** | 為需要領域研究、來源發現和綜合的任何代理提供知識獲取能力 | [research_agent_functional_specification.md](./research_agent_functional_specification.md) + [research_agent_technical_specification.md](./research_agent_technical_specification.md) |
| **流程優化代理** | 使用 DMAIC + 精益 + 多代理共識持續優化生產工作流程 | [optimization_agent_functional_specification.md](./optimization_agent_functional_specification.md) + [optimization_agent_technical_specification.md](./optimization_agent_technical_specification.md) |
| **通用創意代理（GCA）** | 通過 SSOR 模型為 DirectorAgent、ScreenwriterAgent、ConceptArtistAgent 等提供創意構思 | [general_creative_agent_functional_specification.md](./general_creative_agent_functional_specification.md) + [general_creative_agent_technical_specification.md](./general_creative_agent_technical_specification.md) |
| **代理式 RAG 系統** | 共享知識骨幹 — 為所有代理檢索、複合和提供情境知識 | [agentic_rag_functional_specification.md](./agentic_rag_functional_specification.md) |
| **深度意圖分析（DIA）** | 分析用戶簡報、受眾意圖、隱藏議程 — 供給 IntentAnalysisAgent 和 DirectorAgent | [intent_analysis_agent_functional_specification.md](./intent_analysis_agent_functional_specification.md) |
| **編碼代理（N1ch01as Architect）** | 構建和維護系統自身的程式碼庫；實施新代理 | [coding_agent_functional_specification.md](./coding_agent_functional_specification.md) |
| **LLM 使用儀表板** | 監控群組使用的所有 LLM 供應商的 API 成本和令牌消耗 | [llm_usage_functional_specification.md](./llm_usage_functional_specification.md) |
| **播客代理** | 自動化播客/電台製作工作流程（準備 → 執行 → 結束 → 跟進） | [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md) |



---

## 5. 跨領域功能

這些規格定義了多個代理共享或全系統適用的功能：

| 功能 | 提供內容 | 使用者 | 規格 |
|------|----------|--------|------|
| **策略目標達成框架** | 6 階段自我詢問系統，將模糊目標轉化為可行計劃 | 所有規劃代理（PlannerAgent、ProducerAgent、DirectorAgent） | [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) |
| **編劇目標達成** | 目標框架在創意寫作中的實際演示 | ScreenwriterAgent、ShowrunnerAgent、ComedyWriterAgent | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| **心理側寫** | 100 個創作者側寫，包含 MBTI、動機、恐懼、創意參數 | CastingAgent、TalentAgent、PersonalizationEngineerAgent、UGCCreatorAgent | [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) |
| **心理推薦** | 基於心理學的偏好預測（大五人格、情緒狀態） | AudienceSimAgent、PerformanceMarketerAgent、PersonalizationEngineerAgent | [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) |
| **複雜問題解決** | WHAT/WHY/HOW/DO/REVIEW 結構化方法論 | 所有診斷代理（FactCheckerAgent、SMEAgent、JudgeAgent、OptimizationAgent） | [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) |
| **通用代理結構** | 所有代理的共享架構模式 | 全部 114 個代理 | [common-agent-structure.svg](./common-agent-structure.svg) + [common-agent-structure.html](./common-agent-structure.html) |

---

## 6. 工作流程整合

### 6.1 製作管線（端到端）

```
用戶簡報
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 第一階段：意圖與規劃                                                  │
│ IntentAnalysisAgent (DIA) → PlannerAgent → ProducerAgent             │
│ 輸出：已解析簡報、分階段 DAG、預算、進度                                │
│ 規格：intent_analysis_agent_functional_specification.md               │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 第二階段：創意開發                                                    │
│ DirectorAgent + ScreenwriterAgent + GCA (SSOR)                       │
│ 輸出：劇本、鏡頭表、風格指南、分鏡圖                                    │
│ 規格：general_creative_agent_*、screenwriter_*                       │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 第三階段：前期製作                                                    │
│ CastingAgent + ProductionDesignAgent + ConceptArtistAgent            │
│ + CostumeAgent + ResearchAgent（領域知識）                            │
│ 輸出：演員陣容、場景、服裝、世界觀聖經、研究檔案                          │
│ 規格：research_agent_functional_specification.md                     │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 第四階段：製作（生成）                                                 │
│ PromptEngineerAgent + CinematographerAgent + TalentAgent             │
│ + SoundDesignAgent + ComposerAgent + VoiceOverAgent                  │
│ 輸出：原始素材、音頻軌道、配音軌道、音效                                 │
│ 技術參考：video_generation_techology_should_learn_now.md             │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 第五階段：後期製作                                                    │
│ EditorAgent + ColoristAgent + VFXSupervisorAgent + AnimatorAgent      │
│ + SoundMixerAgent + AIQAConsistencyAgent                             │
│ 輸出：已調色母帶、已混音音頻、通過 QC 的最終版                           │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 第六階段：交付與優化                                                  │
│ SocialMediaStrategistAgent + PerformanceMarketerAgent                 │
│ + TrailerEditorAgent + PersonalizationEngineerAgent                   │
│ + OptimizationAgent（持續改進）                                       │
│ 輸出：平台特定包、企劃、分析                                           │
│ 規格：optimization_agent_functional_specification.md                 │
└─────────────────────────────────────────────────────────────────────┘
```



### 6.2 工作流程變體（按影片類型）

每種影片類型通過代理 DAG 的自訂路徑進行。視覺工作流程以 SVG 格式提供：

| 影片類型 | 工作流程圖 | 主要啟動代理 |
|----------|-----------|-------------|
| 病毒式鉤子 | [workflows/A-viral-hook.svg](./workflows/A-viral-hook.svg) | ComedyWriterAgent、UGCCreatorAgent、SocialMediaStrategistAgent |
| UGC 廣告 | [workflows/B-ugc-ad.svg](./workflows/B-ugc-ad.svg) | UGCCreatorAgent、PerformanceMarketerAgent、CopywriterAgent |
| 動畫解說 | [workflows/C-animated-explainer.svg](./workflows/C-animated-explainer.svg) | InstructionalDesignAgent、MotionGraphicsAgent、VoiceOverAgent |
| 個人化生日 | [workflows/D-personalized-birthday.svg](./workflows/D-personalized-birthday.svg) | PersonalizationEngineerAgent、AvatarDesignAgent、VoiceCloneAgent |
| AI 短片 | [workflows/E-ai-short-film.svg](./workflows/E-ai-short-film.svg) | DirectorAgent、ScreenwriterAgent、EditorAgent、ComposerAgent |
| 企業培訓 | [workflows/F-corporate-training.svg](./workflows/F-corporate-training.svg) | InstructionalDesignAgent、SMEAgent、ComplianceAgent |
| 音樂影片 | [workflows/G-music-video.svg](./workflows/G-music-video.svg) | MusicVideoDirectorAgent、ChoreographyAgent、ComposerAgent |
| AI 虛擬化身 | [workflows/H-ai-avatar.svg](./workflows/H-ai-avatar.svg) | AvatarDesignAgent、VoiceCloneAgent、LipSyncAgent |
| 紀錄片 | [workflows/I-documentary.svg](./workflows/I-documentary.svg) | JournalistAgent、ResearchAgent、FactCheckerAgent、EditorAgent |
| 劇情長片 | [workflows/J-feature-film.svg](./workflows/J-feature-film.svg) | 完整管線（全部 114 個代理） |

### 6.3 人類基準比較

系統設計為人類製作工作流程的直接 AI 替代/增強：

> **參考：** [human_video_production_workflow.md](./human_video_production_workflow.md) — 定義代理系統所對映並擴展的 52 個人類工藝角色。

---

## 7. 數據流與交接合約

每個代理通過**共享製品交接合約**（機器可讀 JSON 清單）進行通訊：

| 欄位 | 用途 |
|------|------|
| `artifact_id` / `version` | 每個輸出和修訂的唯一標識 |
| `parent_assets` | 至劇本、提示詞、底板、音軌的溯源連結 |
| `brief_scope` | 子任務、驗收標準、目標受眾 |
| `technical_spec` | 編解碼器、長寬比、時長、幀率、色彩空間、響度 |
| `rights_and_consent` | 許可狀態、肖像/聲音同意、地域限制 |
| `continuity_state` | 角色外觀、道具、服裝、環境、身份雜湊 |
| `qc_status` | 最新 L1/L2/L3 QC 結果 |
| `target_channels` | 院線、串流、廣播、社交、CRM、LMS |
| `provenance_manifest` | C2PA 參考、批評日誌指標、簽核鏈 |

> **完整合約規格：** [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.3

### 7.1 批評匯流排協議

所有代理通過結構化 JSON 匯流排進行批評通訊：

```json
{
  "from_agent": "EditorAgent",
  "to_agent": "DirectorAgent",
  "critique_type": "pacing_feedback",
  "severity": "suggestion",
  "artifact_ref": "artifact_id_123_v2",
  "message": "第三場戲節奏超出類型先驗 15%；建議裁剪。",
  "rubric_score": 0.72,
  "timestamp": "2026-05-27T10:30:00Z"
}
```



---

## 8. UI 與通訊層

前端為人類操作員提供代理群組的可見性和控制：

| UI 文檔 | 涵蓋內容 | 連結 |
|---------|----------|------|
| 架構與通訊 | 三層協議（REST、WebSocket、代理佇列） | [ui/architecture_communication.md](./ui/architecture_communication.md) |
| 代理管理 UI | 如何監控、配置和覆寫代理 | [ui/agent_management_ui.md](./ui/agent_management_ui.md) |
| 後端代理管理 | 伺服器端代理生命週期、擴展、健康狀態 | [ui/backend_agent_management.md](./ui/backend_agent_management.md) |
| UI 設計 | 視覺設計系統、元件、互動 | [ui/ui_design.md](./ui/ui_design.md) |
| 專案建立流程 | 從簡報到運行製作的用戶旅程 | [ui/project_creation_flow.md](./ui/project_creation_flow.md) |
| 製作規模發現 | 系統如何適應專案複雜性 | [ui/production_scale_discovery.md](./ui/production_scale_discovery.md) |
| 影片翻拍增強 | 改善現有影片的工作流程 | [ui/video_remake_enhancement.md](./ui/video_remake_enhancement.md) |
| 100 項改進再思考 | 全面的 UI 改進目錄 | [ui/RETHINK_100_IMPROVEMENTS.md](./ui/RETHINK_100_IMPROVEMENTS.md) |

---

## 9. 技術堆疊參考

### 9.1 LLM 供應商（用於代理推理）

| 供應商 | 模型 | 主要用途 |
|--------|------|----------|
| xAI | Grok-4.x | 主要推理、工具使用、研究 |
| Google DeepMind | Gemini 2.5 Pro（1M 上下文） | 長上下文分析、聖經搜索 |
| OpenAI | GPT-4o、o 系列 | 結構化輸出、共識採樣 |
| Anthropic | Claude 4 | 安全、憲政式 AI 代理 |
| 開源 | Qwen2.5、Wan 2.6 | 成本優化、本地推理 |

### 9.2 影片生成模型

> **完整參考（50 個模型排名）：** [video_generation_techology_should_learn_now.md](./video_generation_techology_should_learn_now.md)

| 排名 | 模型 | 在系統中的主要用途 |
|------|------|--------------------|
| 1 | Seedance 2.0（ByteDance） | 帶原生音頻的多模態生成 |
| 2 | Kling 3.0（Kuaishou） | 動作控制、多角色場景 |
| 3 | Veo 3.1（Google） | 電影品質、角色一致性 |
| 4 | Grok Imagine Video（xAI） | 快速迭代、社交優先輸出 |
| 6 | Sora 2（OpenAI） | 敘事/物理故事講述 |
| 8 | Runway Gen-4.5 | 專業創意控制、VFX |

### 9.3 音頻/語音工具

| 工具 | 用途 |
|------|------|
| ElevenLabs v3 | TTS、聲音克隆、音效 |
| Sync.so | 唇形同步對齊 |
| Udio/Suno | 音樂生成 |
| Dolby Atmos Renderer | 空間音頻混音 |

### 9.4 基礎設施

| 元件 | 技術 |
|------|------|
| 編排 | LangGraph + Temporal |
| 事件匯流排 | Redis Streams / NATS |
| 資產儲存 | S3 + 元數據資料庫 |
| 可觀測性 | LangSmith + AgentOps |
| 前端 | React 19 + Next.js 15 |
| 後端 | FastAPI（Python） |
| 向量資料庫 | Chroma + Pinecone/Weaviate |
| 圖資料庫 | LightRAG（OpenSearch） |



---

## 10. 參考材料索引

### 10.1 深度實施參考（68 章）

`reference/how_to_build_a_video_agent_system/` 目錄包含 68 章詳細的實施指南：

| 章節 | 可能涵蓋內容 |
|------|-------------|
| 01–10 | 系統基礎、架構模式、代理設計 |
| 11–20 | 個別代理實施、工具整合 |
| 21–30 | 品質保證、評估、測試模式 |
| 31–40 | 編排、狀態管理、訊息傳遞 |
| 41–50 | 影片生成、音頻、創意管線 |
| 51–60 | 交付、分發、優化循環 |
| 61–68 | 進階主題、擴展、未來方向 |

> **位置：** [reference/how_to_build_a_video_agent_system/](./reference/how_to_build_a_video_agent_system/)

### 10.2 完整文檔清單

#### 功能規格（英文）

| 文檔 | 代理/系統 | 狀態 |
|------|-----------|------|
| [agentic_rag_functional_specification.md](./agentic_rag_functional_specification.md) | 混合代理式 RAG 系統 | 完成 |
| [coding_agent_functional_specification.md](./coding_agent_functional_specification.md) | N1ch01as Architect v1.0（編碼代理） | 完成 |
| [general_creative_agent_functional_specification.md](./general_creative_agent_functional_specification.md) | 通用創意代理（SSOR） | 完成 |
| [intent_analysis_agent_functional_specification.md](./intent_analysis_agent_functional_specification.md) | 深度意圖分析 v2.0 | 完成 |
| [llm_usage_functional_specification.md](./llm_usage_functional_specification.md) | LLM 使用與成本儀表板 | 完成 |
| [optimization_agent_functional_specification.md](./optimization_agent_functional_specification.md) | 流程優化代理 v2.0 | 完成 |
| [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md) | 播客製作代理 | 完成 |
| [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) | 100 創作者心理側寫 | 完成 |
| [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) | 心理學導向推薦 | 完成 |
| [research_agent_functional_specification.md](./research_agent_functional_specification.md) | 研究代理（grok-research-agent） | 完成 |
| [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) | 編劇目標達成 | 完成 |
| [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) | 策略目標達成框架 | 完成 |

#### 技術規格（英文）

| 文檔 | 代理/系統 | 狀態 |
|------|-----------|------|
| [general_creative_agent_technical_specification.md](./general_creative_agent_technical_specification.md) | GCA 實施 | 完成 |
| [optimization_agent_technical_specification.md](./optimization_agent_technical_specification.md) | 優化代理架構 | 完成 |
| [research_agent_technical_specification.md](./research_agent_technical_specification.md) | 研究代理重新開發 | 完成 |

#### 系統級別文檔（英文）

| 文檔 | 涵蓋內容 | 狀態 |
|------|----------|------|
| [agents.md](./agents.md) | 完整 114 代理名冊（含類別） | 完成 |
| [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) | 完整製作工作流程 + 執行環境架構 | 完成 |
| [human_video_production_workflow.md](./human_video_production_workflow.md) | 人類基準（52 個團隊角色） | 完成 |
| [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) | WHAT/WHY/HOW/DO/REVIEW 方法論 | 完成 |
| [video_generation_techology_should_learn_now.md](./video_generation_techology_should_learn_now.md) | 50 個 AI 影片生成模型（2026 年 4 月） | 完成 |
| [lifes_quiet_redemption_agent_workflow.md](./lifes_quiet_redemption_agent_workflow.md) | 範例:代理對映 + 研究啟發的短片流程(含圖表) | 完成 |

#### 中文（香港繁體）翻譯

所有主要文檔均有 `_hk.md` 對應版本，提供香港繁體中文翻譯。命名模式相同（例如 `agents_hk.md`、`optimization_agent_functional_specification_hk.md`）。

### 10.3 工作流程圖表庫 —《人生的靜默救贖》(範例)

將本系統套用於一支 60 秒電影短片的端到端範例。下列六張圖表(位於 [`./workflows/`](./workflows/))視覺化呈現 114 代理 swarm、關卡階梯,以及 2026 引擎/研究升級如何協同運作。完整說明:[lifes_quiet_redemption_agent_workflow_hk.md](./lifes_quiet_redemption_agent_workflow_hk.md) ([English](./lifes_quiet_redemption_agent_workflow.md))。

<table>
  <tr>
    <td width="33%" align="center"><a href="./workflows/lqr-pipeline-overview.svg"><img src="./workflows/lqr-pipeline-overview.svg" width="260" alt="6 階段流程總覽"/></a><br/><b>D1 · 流程總覽</b><br/>6 階段 DAG、關卡、回饋迴圈</td>
    <td width="33%" align="center"><a href="./workflows/lqr-scene-flow.svg"><img src="./workflows/lqr-scene-flow.svg" width="260" alt="場景流、情緒弧線、留存帶"/></a><br/><b>D2 · 場景流</b><br/>弧線、留存帶、逐鏡引擎</td>
    <td width="33%" align="center"><a href="./workflows/lqr-per-shot-loop.svg"><img src="./workflows/lqr-per-shot-loop.svg" width="260" alt="逐鏡生成迴圈"/></a><br/><b>D3 · 逐鏡迴圈</b><br/>3E + 視覺錨定 + VBench + MCTS</td>
  </tr>
  <tr>
    <td width="33%" align="center"><a href="./workflows/lqr-character-consistency.svg"><img src="./workflows/lqr-character-consistency.svg" width="260" alt="角色一致性身分堆疊"/></a><br/><b>D4 · 一致性堆疊</b><br/>身分少年→成年</td>
    <td width="33%" align="center"><a href="./workflows/lqr-engine-routing.svg"><img src="./workflows/lqr-engine-routing.svg" width="260" alt="引擎路由層級"/></a><br/><b>D5 · 引擎路由</b><br/>Grok Imagine + 英雄引擎 + 成本</td>
    <td width="33%" align="center"><a href="./workflows/lqr-quality-gates.svg"><img src="./workflows/lqr-quality-gates.svg" width="260" alt="品質關卡階梯與 VBench 評分卡"/></a><br/><b>D6 · 品質關卡</b><br/>L1/L2/L3 + VBench 評分卡</td>
  </tr>
</table>

> 若縮圖未顯示,點擊即可開啟完整 SVG。圖表沿用與 [common-agent-structure.svg](./common-agent-structure.svg) 相同的視覺語言。



---

## 11. 實施優先順序與依賴關係

### 11.1 基礎層（首先構建）

這些必須在任何製作代理運作之前存在：

```
1. 代理式 RAG 系統              ← 所有代理的知識骨幹
   └── agentic_rag_functional_specification.md

2. 編排執行環境                  ← DAG 執行、路由、狀態
   └── agents.md §9（OrchestratorAgent、PlannerAgent、RouterAgent）

3. 研究代理                      ← 知識獲取服務
   └── research_agent_functional_specification.md
   └── research_agent_technical_specification.md

4. 編碼代理                      ← 構建所有其他代理
   └── coding_agent_functional_specification.md

5. LLM 使用儀表板               ← 從第一天起監控成本
   └── llm_usage_functional_specification.md
```

### 11.2 智能層（其次構建）

這些提供製作代理所使用的推理能力：

```
6. 深度意圖分析（DIA）           ← 將用戶簡報解析為結構化意圖
   └── intent_analysis_agent_functional_specification.md

7. 通用創意代理（GCA）           ← 創意構思引擎
   └── general_creative_agent_functional_specification.md
   └── general_creative_agent_technical_specification.md

8. 流程優化代理                  ← 工作流程改進引擎
   └── optimization_agent_functional_specification.md
   └── optimization_agent_technical_specification.md

9. 策略目標達成                  ← 所有規劃的目標澄清
   └── strategic_goal_achievement_agent_functional_specification.md

10. 複雜問題解決                 ← 診斷推理框架
    └── complex_problem_solution_process_model.md
```

### 11.3 製作層（第三構建）

主要名冊中的 52 個核心製作代理（1–52），按工作流程類型啟動。

### 11.4 增強層（第四構建）

```
11. 心理側寫                     ← 個人化創作者/受眾建模
    └── psychological_profile_agent_functional_specifications.md

12. 心理推薦                     ← 受眾偏好預測
    └── psychological_recommendation_agent_functional_specification.md

13. 播客代理                     ← 音頻優先的製作變體
    └── podcast_agent_functional_specifcation.md
```

### 11.5 依賴圖

```
                    ┌─────────────────┐
                    │    編碼代理     │ ← 構建一切
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
    ┌─────────────┐  ┌─────────────┐  ┌──────────────┐
    │ 代理式 RAG  │  │   編排器    │  │ LLM 儀表板  │
    └──────┬──────┘  └──────┬──────┘  └──────────────┘
           │                │
     ┌─────┴─────┐    ┌────┴────┐
     ▼           ▼    ▼         ▼
┌─────────┐ ┌──────┐ ┌──────┐ ┌──────────┐
│  研究   │ │ DIA  │ │ 路由 │ │   規劃   │
│  代理   │ │      │ │ 代理 │ │   代理   │
└────┬────┘ └──┬───┘ └──┬───┘ └────┬─────┘
     │         │         │          │
     └─────────┴─────────┴──────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │  52 個製作代理（1–52）        │
    │  + GCA + 優化代理             │
    │  + 目標框架                   │
    │  + 心理側寫                   │
    └───────────────────────────────┘
```

---

## 12. 如何使用本文檔

1. **開始新的實施？** → 從 §11（優先順序與依賴關係）開始，然後按照基礎 → 智能 → 製作 → 增強的順序進行。

2. **需要了解特定代理？** → 在 §3（代理類別）中找到它，然後跟隨「深度規格」連結。

3. **設計新的工作流程？** → 查看 §6（工作流程整合）了解管線階段，及 §6.2 了解現有工作流程變體。

4. **整合代理？** → 查看 §7（數據流與交接合約）了解共享清單格式和批評匯流排協議。

5. **構建 UI？** → 查看 §8 了解所有 UI/通訊文檔。

6. **需要參考材料？** → 查看 §10 了解完整清單，包括 68 章深度參考。

---

*文檔生成日期：2026 年 5 月 27 日*  
*涵蓋：114 個代理、12 個功能規格、3 個技術規格、10 個工作流程變體、68 章參考*
