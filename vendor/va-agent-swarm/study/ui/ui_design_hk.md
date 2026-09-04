# VA Agent Swarm — 完整 UI 版面設計

> 覆蓋 [Composition Diagram](../agents.md#composition-diagram) 內的每個操作，並提供所有 10 種工作流類型（A–J）的完整「由啟動製作」使用者旅程。

---

## 目錄

1. [設計理念](#1-設計理念)
2. [資訊架構](#2-資訊架構)
3. [主殼版面（Master Shell）](#3-主殼版面master-shell)
4. [介面面板清單（Surface Inventory）](#4-介面面板清單surface-inventory)
5. [逐頁拆解（Page-by-Page）](#5-逐頁拆解page-by-page)
6. [製作啟動流程（Production Start Flow）](#6-製作啟動流程production-start-flow)
7. [Composition Diagram 覆蓋地圖](#7-composition-diagram-覆蓋地圖)
8. [響應式與無障礙重點](#8-響應式與無障礙重點)
9. [元件庫摘要](#9-元件庫摘要)
10. [互動模式](#10-互動模式)

---

## 1. 設計理念

### 1.1 核心原則

| 原則 | 理由 |
|-----------|-----------|
| **Brief-First** | 每次 production 都由人類 brief 開始；UI 以 brief 輸入為重心 |
| **Progressive Disclosure** | 114 個代理人資訊量太大；只顯示當前階段需要的內容 |
| **Live DAG Visibility** | Composition Diagram 會即時運行；使用者必須一眼看到各代理人狀態 |
| **Gate-Driven Confidence** | GateKeeperAgent 的階段切換，於 UI 以清晰的「審批時刻」呈現 |
| **Critique Transparency** | 每條代理人 critique 訊息都可檢視、搜尋、並可採取行動 |
| **Production-Type Aware** | 10 個工作流範本（A–J）決定啟用哪些代理人與顯示哪些面板 |

### 1.2 目標使用者

| Persona | 需要 |
|---------|-------|
| **Creator** | 快速啟動製作、審閱輸出、批准 gates |
| **Producer** | 監控預算／排程、解決升級事件、管理團隊 |
| **Technical Operator** | 調整 prompts、檢查 agent logs、管理模型路由 |
| **Reviewer/Client** | 檢視交付物、留下回饋、批准最終版本 |

---

## 2. 資訊架構

```text
ROOT
├── Dashboard（Home）
│   ├── Active Productions Grid
│   ├── Quick-Start Brief Wizard
│   └── System Health Banner
│
├── Brief Studio
│   ├── Template Selector（A–J workflows）
│   ├── Brief Editor（structured + freeform）
│   ├── Reference Upload（mood boards、scripts、assets）
│   └── Launch Confirmation（→ PlannerAgent）
│
├── Production Console（每個 production）
│   ├── DAG Canvas（即時 Composition Diagram）
│   │   ├── Agent Nodes（state：idle/running/blocked/done）
│   │   ├── Edge Flows（artifact handoffs）
│   │   └── Gate Checkpoints（approve/reject/comment）
│   │
│   ├── Timeline View
│   │   ├── Phase Swimlanes（Pre-pro → Production → Post → Delivery）
│   │   ├── Milestone Markers
│   │   └── Budget Burn Overlay
│   │
│   ├── Agent Inspector（細節面板）
│   │   ├── Agent Identity & Role
│   │   ├── Current Task & Progress
│   │   ├── Input/Output Artifacts
│   │   ├── Critique Bus（sent/received）
│   │   ├── Quality Metrics（self-score vs threshold）
│   │   └── Tool Calls Log
│   │
│   ├── Artifact Gallery
│   │   ├── Grid/List Toggle
│   │   ├── Version History per Artifact
│   │   ├── Preview（video/audio/image/text）
│   │   ├── Provenance Chain（C2PA）
│   │   └── Compare Mode（A/B side-by-side）
│   │
│   ├── Critique Feed
│   │   ├── Chronological Message Stream
│   │   ├── Filter by Agent / Phase / Severity
│   │   └── Human Intervention Slot
│   │
│   └── Gate Control Panel
│       ├── Pending Approvals Queue
│       ├── Gate Criteria Checklist（L1/L2/L3）
│       ├── Approve / Reject / Request Changes
│       └── C2PA Sign-off Confirmation
│
├── Agent Registry
│   ├── All 114 Agents（searchable、filterable by category）
│   ├── Agent Detail Card（capabilities、tools、patterns）
│   ├── Dependency Graph
│   └── Performance Benchmarks
│
├── Memory & Knowledge
│   ├── Project Memory（MemoryAgent contents）
│   ├── Episodic Log（Reflexion entries）
│   ├── Series Bible / World-Building DB
│   └── Brand Asset Library
│
├── Delivery Hub
│   ├── Master Package Builder
│   ├── Channel-Specific Variants
│   ├── QC Status Matrix
│   ├── Distribution Tracker
│   └── Analytics Dashboard（post-release）
│
├── Settings & Admin
│   ├── Model Routing Config（RouterAgent rules）
│   ├── Cost/Latency Budgets
│   ├── API Key Management
│   ├── Team & Permissions
│   └── Compliance Config（constitutions、consent DB）
│
└── Help & Docs
    ├── Agent Glossary
    ├── Workflow Templates Guide
    └── API Reference
```

---

## 3. 主殼版面（Master Shell）

### 3.1 Shell 結構

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  TOP BAR（64px）                                                              │
│  ┌──────┬──────────────────────────────┬───────────────────────────────────┐ │
│  │ Logo │  Global Search（Cmd+K）      │  Notifications │ User │ Settings │ │
│  └──────┴──────────────────────────────┴───────────────────────────────────┘ │
├────────┬─────────────────────────────────────────────────────────────────────┤
│  SIDE  │  MAIN CANVAS                                                        │
│  NAV   │                                                                     │
│（72px） │  ┌─────────────────────────────────────────────────────────────┐    │
│        │  │  CONTEXT BAR（production 名稱、phase、budget、health）        │    │
│  ○ Dash│  ├─────────────────────────────────────────────────────────────┤    │
│  ○ Brief│ │                                                             │    │
│  ○ Prod │ │                 主要工作區（PRIMARY VIEW）                   │    │
│  ○ Agents│ │            （DAG / Timeline / Gallery / Feed）              │    │
│  ○ Memory│ │                                                            │    │
│  ○ Deliver│ │                                                           │    │
│  ○ Settings│ │                                                          │    │
│        │  │                                                             │    │
│        │  ├─────────────────────────────────────────────────────────────┤    │
│        │  │  DETAIL DRAWER（向上滑：Agent Inspector / Artifact View）    │    │
│        │  └─────────────────────────────────────────────────────────────┘    │
│        │                                                                     │
├────────┴─────────────────────────────────────────────────────────────────────┤
│  STATUS BAR（32px）                                                           │
│  Running Agents：12/27 │ Phase：Production │ Budget：$42/$100 │ ETA：3m      │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 版面分區

| 區域 | 高度／寬度 | 目的 |
|------|-------------|---------|
| Top Bar | 固定 64px | 全域導航、搜尋（agents、artifacts、critiques）、通知 |
| Side Nav | 72px 寬，icon-only（hover 展開到 240px 顯示標籤） | 主導航 |
| Context Bar | 固定 48px | 當前 production 的上下文麵包屑 |
| Primary View | 自動伸縮 | 當前工作區 |
| Detail Drawer | 由底部 0–50%，可調整 | 不離開上下文就可檢視／預覽 |
| Status Bar | 固定 32px | 一眼看 production 遙測資訊 |

### 3.3 導航模型

| 層級 | 機制 | 例子 |
|-------|-----------|---------|
| L0 — App sections | Side Nav icons | Dashboard → Brief Studio → Production Console |
| L1 — 內部 views | Primary View 內 tab bar | DAG Canvas │ Timeline │ Gallery │ Critique Feed |
| L2 — 詳細視圖 | Drawer（底部）或 Modal | Agent Inspector、Artifact Viewer、Gate Approval Dialog |
| L3 — 情境操作 | 右鍵選單／Command Palette（Cmd+K） | Retry agent、Compare versions、Export artifact |

---

## 4. 介面面板清單（Surface Inventory）

每個 UI 面板都對應 Composition Diagram 的一個或多個操作：

| # | 面板 | Composition Diagram 操作 | 主要服務的 Agent |
|---|---------|----------------------------------|------------------------|
| S1 | Brief Wizard | `[Brief]` 入口 | User → PlannerAgent |
| S2 | Template Selector | 選擇工作流類型（A–J） | PlannerAgent |
| S3 | DAG Canvas | 完整 `PlannerAgent → OrchestratorAgent → RouterAgent → Craft Agents` 流程 | OrchestratorAgent、RouterAgent |
| S4 | Agent Node Card | DAG 內單一 agent 狀態 | 任意 114 agents |
| S5 | Gate Approval Dialog | `GateKeeperAgent` phase transitions | GateKeeperAgent、JudgeAgent |
| S6 | Critique Feed | `CritiqueMessages` bus | 所有 agents（雙向） |
| S7 | Memory Panel | `MemoryAgent` 檢索／存儲 | MemoryAgent |
| S8 | Agent Inspector | agent 深入檢視（tools、metrics、I/O） | 任意 agent |
| S9 | Artifact Gallery | 所有 craft agents 的輸出 | 52 craft agents（§1–§8） |
| S10 | Artifact Viewer | 預覽 + 對照 + 溯源 | 所有產出 agents |
| S11 | Timeline View | 排程／phase 可視化 | ProducerAgent、OrchestratorAgent |
| S12 | Budget Tracker | 成本監控 | ProducerAgent、CostOptimizerAgent |
| S13 | Router Config | 模型／agent 路由規則 | RouterAgent、CostOptimizerAgent |
| S14 | Prompt Lab | prompt 編輯 + 優化 | PromptEngineerAgent、PromptOptimizerAgent |
| S15 | Quality Dashboard | VBench/EvalCrafter/CLIP-T 分數 | AIQAConsistencyAgent、EvalHarnessAgent |
| S16 | Delivery Packager | 各渠道 export | DistributorAgent、SoundMixerAgent、ColoristAgent |
| S17 | Analytics Panel | 發佈後表現 | AnalystAgent、RetentionOptimizerAgent |
| S18 | Compliance Checker | 法務／同意／C2PA | ComplianceAgent、TrustSafetyAgent |
| S19 | Creative Meta Panel | 構思／敘事／風格／情緒／新穎度 | Creative meta-agents（§9.2） |
| S20 | Research Panel | Web／檔案庫／趨勢／競品／引用 | Research meta-agents（§9.3） |
| S21 | Optimization Panel | Prompt／成本／延遲／留存／ROAS／A11y | Optimization meta-agents（§9.4） |
| S22 | Notification Center | 升級、審批、警示 | ProducerAgent、所有 gate agents |
| S23 | Team / Permissions | 人類介入配置 | Admin |
| S24 | Series Bible Editor | 長期劇集記憶 | ShowrunnerAgent、WorldBuildingAgent |

---

## 5. 逐頁拆解（Page-by-Page）

### 5.1 Dashboard（Home）

```text
┌─────────────────────────────────────────────────────────────────────┐
│  DASHBOARD                                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─── QUICK START ──────────────────────────────────────────────┐   │
│  │  [+ New Production]  "Describe what you want to create..."   │   │
│  │  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ...       │   │
│  │  │ A  │ │ B  │ │ C  │ │ D  │ │ E  │ │ F  │ │ G  │           │   │
│  │  │Hook│ │UGC │ │Expl│ │Bday│ │Film│ │Corp│ │ MV │           │   │
│  │  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘           │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─── ACTIVE PRODUCTIONS ──────────────────────────────────────┐    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │    │
│  │  │ Proj "Luna"  │  │ Proj "Spark" │  │ Proj "Atlas" │      │    │
│  │  │ Type: E      │  │ Type: B      │  │ Type: I      │      │    │
│  │  │ Phase: Post  │  │ Phase: Prod  │  │ Phase: Pre   │      │    │
│  │  │ ████████░░   │  │ ██████░░░░   │  │ ██░░░░░░░░   │      │    │
│  │  │ 80% · $62    │  │ 55% · $28    │  │ 15% · $8     │      │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘      │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── SYSTEM HEALTH ──────────────────────────────────────────┐     │
│  │  Agents Online: 114/114  │  Pending Gates: 3  │  Alerts: 1 │     │
│  └─────────────────────────────────────────────────────────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**關鍵互動：**
- 點範本卡（A–J）→ 開啟 Brief Studio（預載該 workflow）
- 點 production 卡 → 開啟該 project 的 Production Console
- 「+ New Production」或直接搜尋 → Brief Studio（空白）

### 5.2 Brief Studio

```text
┌─────────────────────────────────────────────────────────────────────┐
│  BRIEF STUDIO                                          [Launch ▶]   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─── STEP 1：範本 ─────────────────────────────────────────────┐    │
│  │  已選： [E] AI Short Film                                   │    │
│  │  （預覽：此範本會啟用哪些 agents）                            │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── STEP 2：BRIEF 詳情 ───────────────────────────────────────┐    │
│  │                                                             │    │
│  │  Title: ___________________________                         │    │
│  │  Vision Statement:（freeform，2–5 句）                       │    │
│  │  ┌──────────────────────────────────────────────┐           │    │
│  │  │                                              │           │    │
│  │  └──────────────────────────────────────────────┘           │    │
│  │                                                             │    │
│  │  Genre: [Dropdown]    Duration: [Slider 15s–120min]         │    │
│  │  Aspect Ratio: ○16:9 ○9:16 ○1:1 ○4:3                        │    │
│  │  Tone: [Tag input: cinematic, moody, ...]                   │    │
│  │  Target Audience: [Dropdown + custom]                       │    │
│  │  Budget Cap: [$___]   Deadline: [Date picker]               │    │
│  │                                                             │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── STEP 3：參考資料 ─────────────────────────────────────────┐    │
│  │                                                             │    │
│  │  [Drop Zone: scripts, mood images, reference videos, audio] │    │
│  │  ┌────┐ ┌────┐ ┌────┐ ┌──────────────────────────┐         │    │
│  │  │.fdx│ │.png│ │.mp4│ │  + Add from Brand Library │         │    │
│  │  └────┘ └────┘ └────┘ └──────────────────────────┘         │    │
│  │                                                             │    │
│  │  Style References: [Paste URL or upload]                     │    │
│  │  Voice/Talent Preferences: [Select from library]             │    │
│  │                                                             │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── STEP 4：約束與合規 ───────────────────────────────────────┐    │
│  │  ☑ Require C2PA provenance signing                           │    │
│  │  ☑ WCAG 2.2 AA accessibility                                 │    │
│  │  ☐ SAG-AFTRA AI consent verification                          │    │
│  │  ☐ GDPR/CCPA personal data handling                           │    │
│  │  Platform targets: ☑YouTube ☑TikTok ☐Meta ☐Broadcast         │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── STEP 5：檢視與啟動 ───────────────────────────────────────┐    │
│  │  Plan Preview: PlannerAgent 會拆解成 ~N phases                │    │
│  │  Estimated agents: 34 │ Est. cost: $XX │ Est. time: Xm       │    │
│  │                                                             │    │
│  │       [ Save Draft ]    [ ▶ LAUNCH PRODUCTION ]              │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**範本特定預設：**

| 範本 | 預填欄位 | 啟用代理人群組 |
|----------|-------------------|----------------------|
| A — Viral Hook | 15–60s、9:16、TikTok/Reels | Hook、UGC、Trend、Social、Retention |
| B — UGC Ad | 15–45s、9:16、成效目標 | UGC、Performance、Brand、Copy、A/B |
| C — Animated Explainer | 60–180s、16:9、教育 | Animator、MotionGraphics、Instructional、VO |
| D — Personalized Birthday | 30–60s、個人化變數 | Personalization、Template、Avatar、Voice |
| E — AI Short Film | 3–15min、16:9、電影感 | Above-the-Line + Camera + Editorial + Sound |
| F — Corporate Training | 5–30min、16:9、SCORM/xAPI | Instructional、LMS、Avatar、SME、Assessment |
| G — Music Video | 3–5min、16:9/9:16、beat-sync | MV Director、Choreography、Editor、Label A&R |
| H — AI Avatar | 1–10min、主持人風格 | Avatar、Voice Clone、Lip Sync、Brand |
| I — Documentary | 10–90min、16:9、檔案素材 | Journalist、Archive、Fact-Check、Standards |
| J — Feature Film | 90–180min、電影感 | 全 114 agents，所有 gates 啟用 |

### 5.3 Production Console — DAG Canvas

UI 核心：把即時 Composition Diagram 以可互動 node graph 呈現。

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODUCTION："Luna"（Type E: AI Short Film）  Phase: Production  ⏱ 12m       │
├──────────────────┬──────────────────────────────────────────────────────────┤
│  VIEW TABS:      │                                                          │
│  [DAG] Timeline  │                                                          │
│  Gallery Critique│            ┌─────────────┐                               │
│                  │            │  [Brief]    │                               │
│  FILTER:         │            └──────┬──────┘                               │
│  ○ All           │                   │                                      │
│  ○ Active        │                   ▼                                      │
│  ○ Blocked       │        ┌──────────────────┐                              │
│  ○ Completed     │        │  PlannerAgent    │                              │
│                  │        │  ✓ Complete      │                              │
│  ZOOM: [─────●]  │        └────────┬─────────┘                              │
│                  │                 │                                       │
│  LAYERS:         │                 ▼                                       │
│  ☑ Orchestration │     ┌─────────────────────┐                              │
│  ☑ Craft         │     │  OrchestratorAgent  │                              │
│  ☑ Meta-Creative │     │  ● Running          │                              │
│  ☑ Meta-Research │     └────┬───────────┬────┘                              │
│  ☑ Meta-Optimize │          │           │                                   │
│  ☑ Critique      │          ▼           ▼                                   │
│                  │   ┌───────────┐  ┌──────────────┐                        │
│                  │   │RouterAgent│  │MemoryAgent   │                        │
│                  │   │ ● Running │  │ ● Listening  │                        │
│                  │   └─────┬─────┘  └──────────────┘                        │
│                  │         │                                                 │
│                  │    ┌────┼────┬────────┬──────────┐                       │
│                  │    ▼    ▼    ▼        ▼          ▼                       │
│                  │ ┌────┐┌────┐┌────┐┌────────┐┌────────┐                  │
│                  │ │Dir ││DoP ││Edit││Composer││VFX Sup │                  │
│                  │ │ ●  ││ ○  ││ ○  ││  ○     ││  ○     │                  │
│                  │ └────┘└────┘└────┘└────────┘└────────┘                  │
│                  │         │         ▲                                       │
│                  │         ▼         │                                       │
│                  │  ┌──────────────────────┐                                │
│                  │  │   GateKeeperAgent    │                                │
│                  │  │   ⚠ Awaiting Approval │                               │
│                  │  └──────────────────────┘                                │
│                  │         ▲                                                 │
│                  │         │                                                 │
│                  │  ┌──────────────┐                                        │
│                  │  │  JudgeAgent  │                                        │
│                  │  │  ● Scoring   │                                        │
│                  │  └──────────────┘                                        │
│                  │                                                          │
├──────────────────┴──────────────────────────────────────────────────────────┤
│  DETAIL DRAWER ▲                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ DirectorAgent │ Task: Shot Intent #4 │ Score: CLIP-T 0.34 (✓≥0.32)  │   │
│  │ Input: Scene 2 script │ Output: shot_intent_04.json │ Critiques: 2   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**DAG 節點狀態：**
| 符號 | 狀態 | 顏色 |
|--------|-------|-------|
| ✓ | Complete | 綠 |
| ● | Running | 藍（跳動） |
| ○ | Idle/Queued | 灰 |
| ⚠ | Blocked/Needs Approval | 橙 |
| ✗ | Failed | 紅 |

**DAG 互動：**
- 點 node → Detail Drawer 開 Agent Inspector
- Double-click node → 全螢幕 Agent Inspector
- 點 edge → 顯示傳遞中的 artifact
- 點 GateKeeper → 開 Gate Approval Dialog
- 右鍵 node → Retry / Skip / Inspect / View Critiques
- 拖動平移、滾輪縮放、Ctrl+click 多選

### 5.4 Production Console — Timeline View

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  TIMELINE VIEW                                                    Budget: $42│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  t=0          t=2m        t=5m        t=8m       t=12m       t=15m (est)    │
│  │            │           │           │          │           │              │
│  ├────────────┼───────────┼───────────┼──────────┼───────────┤              │
│  │            │           │           │          │           │              │
│  │ PRE-PRODUCTION         │           │          │           │              │
│  │ ████████████████       │           │          │           │              │
│  │ Plan│Screen│Story│Cast │           │          │           │              │
│  │            │           │           │          │           │              │
│  │            │ PRODUCTION            │          │           │              │
│  │            │ ░░░░░░░░░░████████████│          │           │              │
│  │            │ Dir│DoP│Camera│Gen│VFX│          │           │              │
│  │            │           │           │          │           │              │
│  │            │           │    POST-PRODUCTION   │           │              │
│  │            │           │    ░░░░░░░░░░░░░░░░░░████         │              │
│  │            │           │    Edit│Color│Sound│Mix│          │              │
│  │            │           │           │          │           │              │
│  │            │           │           │    DELIVERY           │              │
│  │            │           │           │    ░░░░░░░░░░░░░░░░░░│              │
│  │            │           │           │    QC│Package│Dist    │              │
│  │            │           │           │          │           │              │
│  ├──Gate 1────┼──Gate 2───┼──Gate 3───┼──Gate 4──┼───────────┤              │
│  │  ✓ Pass    │  ✓ Pass   │  ⚠ Review │  ○ Pend  │  ○ Pend   │              │
│  │            │           │           │          │           │              │
│  │─── Budget Burn Line ─────────────────────────────$42──────│              │
│  │ $8         │ $22       │ $35       │ $42       │           │              │
│  └────────────┴───────────┴───────────┴───────────┴───────────┘              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.5 Production Console — Artifact Gallery

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  ARTIFACT GALLERY                      [Grid ▣] [List ≡]  Filter: [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ ▶ ░░░░░░░░░  │  │ ▶ ░░░░░░░░░  │  │   ┌─────┐   │  │  📄           │   │
│  │   Shot 1     │  │   Shot 2     │  │   │mood │   │  │  screenplay   │   │
│  │   v3 ✓       │  │   v2 ●       │  │   │board│   │  │  v4 ✓         │   │
│  │   by DoP     │  │   by DoP     │  │   └─────┘   │  │  by Writer    │   │
│  │   CLIP: 0.35 │  │   CLIP: 0.31 │  │  Concept v2 │  │  Beats: 12/12 │   │
│  │  [C2PA ✓]    │  │  [C2PA ✓]    │  │  by Concept │  │  [C2PA ✓]     │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ 🎵 ─────      │  │ 🎵 ─────      │  │ ▶ ░░░░░░░░░  │  │  📊 Chart    │   │
│  │  Score Cue 1  │  │  SFX Pack     │  │  Rough Cut   │  │  Quality     │   │
│  │  v1 ●         │  │  v2 ✓         │  │  v1 ⚠        │  │  Report      │   │
│  │  by Composer  │  │  by SoundDes  │  │  by Editor   │  │  by QA       │   │
│  │  Mood: 0.88   │  │  Sync: ✓      │  │  Pacing: B+  │  │  VBench: 0.8 │   │
│  │  [C2PA ✓]     │  │  [C2PA ✓]     │  │  [C2PA ✓]    │  │              │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                                             │
│  Showing 8 of 47 artifacts │ Page [1] 2 3 4 5 ►                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Artifact 卡片包含：**
- 縮圖預覽（影片幀／波形／圖片／文件圖示）
- 版本徽章 + 狀態
- 產出代理人
- 關鍵品質指標
- C2PA 溯源徽章
- 點一下 → Drawer 開 Artifact Viewer（對照、版本歷史、完整溯源鏈）

### 5.6 Production Console — Critique Feed

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  CRITIQUE FEED              Filter: [All Agents ▼] [All Phases ▼] [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  12:04:32 │ EditorAgent → DirectorAgent                          Severity: │
│  ─────────┼──────────────────────────────────────────────────────── Info   │
│           │ "Pacing in Scene 3 exceeds genre prior by 1.2σ.                │
│           │  Suggest trimming B-roll between beats 7–8."                   │
│           │  📎 Attached: pacing_curve_s3.json                             │
│           │  [Accept] [Reject] [Discuss] [View Artifact]                   │
│           │                                                                │
│  12:03:58 │ AIQAConsistencyAgent → GeneratorAgent               Severity:  │
│  ─────────┼──────────────────────────────────────────────────── Warning   │
│           │ "Frame 142–148: hand artifact detected (confidence 0.91).      │
│           │  Recommend re-roll with seed+1."                               │
│           │  📎 Attached: frame_142_annotated.png                          │
│           │  [Auto-Fix] [Manual Review] [Dismiss]                          │
│           │                                                                │
│  12:03:22 │ ComplianceAgent → ALL                               Severity: │
│  ─────────┼──────────────────────────────────────────────────── Critical  │
│           │ "Voice clone consent for talent #3 expires in 48h.             │
│           │  Block delivery until renewal confirmed."                      │
│           │  [Resolve] [Escalate to Human] [Extend Deadline]               │
│           │                                                                │
│  12:02:45 │ JudgeAgent → ScreenwriterAgent + DirectorAgent      Severity: │
│  ─────────┼──────────────────────────────────────────────────────── Info  │
│           │ "Debate resolved: Act 2 midpoint placement at 52%              │
│           │  (DirectorAgent position) wins by rubric score 0.82 vs 0.71."  │
│           │  [View Debate Log] [View Rubric]                               │
│           │                                                                │
│  ── HUMAN INTERVENTION SLOT ────────────────────────────────────────────    │
│  │  💬 Type your critique or instruction to any agent...          [Send] │  │
│  │  @Agent: [autocomplete]  Priority: [Normal ▼]                         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.7 Gate Approval Dialog

```text
┌──────────────────────────────────────────────────────────┐
│  GATE APPROVAL — Phase: Pre-Production → Production       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Gate: #2（Script Lock + Storyboard Approval）            │
│  GateKeeperAgent Assessment: READY FOR REVIEW            │
│  JudgeAgent Score: 0.87/1.00                             │
│                                                          │
│  ┌─── CRITERIA CHECKLIST ──────────────────────────────┐ │
│  │  ✓ Script beat-sheet coverage: 12/12 (100%)         │ │
│  │  ✓ Dialogue distinctiveness: 0.42 (≥0.35)          │ │
│  │  ✓ Storyboard shot coverage: 24/24 (100%)          │ │
│  │  ✓ Budget estimate within cap: $85 ≤ $100          │ │
│  │  ⚠ Style consistency: 0.83 (target ≥0.85)          │ │
│  │  ✓ Compliance pre-check: PASS                       │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌─── ARTIFACTS FOR REVIEW ────────────────────────────┐ │
│  │  📄 screenplay_v4.fdx    [Preview]                  │ │
│  │  🖼  storyboard_panels/  [Preview Gallery]          │ │
│  │  📊 budget_estimate.json [View]                     │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  Comments: ________________________________________      │
│                                                          │
│  [ ✓ APPROVE ]  [ ✗ REJECT ]  [ ↩ REQUEST CHANGES ]      │
│                                                          │
│  C2PA: Signing as [user@org]  ☑ Attach provenance        │
└──────────────────────────────────────────────────────────┘
```

### 5.8 Agent Inspector（Detail Drawer）

```text
┌──────────────────────────────────────────────────────────────────────────┐
│  AGENT INSPECTOR: DirectorAgent (#1)                        [Full Screen] │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─── IDENTITY ──────────┐  ┌─── CURRENT TASK ──────────────────────┐   │
│  │ Category: Above-Line  │  │ Task: Generate Shot Intent #5          │   │
│  │ Pattern: Self-Refine  │  │ Status: ● Running (iteration 2/5)     │   │
│  │ Accepts from: 3 agents│  │ Started: 12:03:22                      │   │
│  │ Comments on: 4 agents │  │ Est. complete: 12:04:50                │   │
│  └───────────────────────┘  └────────────────────────────────────────┘   │
│                                                                          │
│  ┌─── QUALITY METRICS ──────────────────────────────────────────────┐    │
│  │  CLIP-T Score:  ████████████████░░░░  0.34 / 0.32 threshold ✓   │    │
│  │  Beat Coverage: ████████████████████  12/12 (100%) ✓            │    │
│  │  Pacing Match:  ██████████████░░░░░░  0.78 / 0.70 threshold ✓   │    │
│  │  Self-Refine Iterations: [2] of max [5]                          │    │
│  └──────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─── I/O ARTIFACTS ──────────────┐  ┌─── TOOL CALLS ───────────────┐    │
│  │ INPUT:                         │  │ 12:03:25 Sora 2 API          │    │
│  │  • screenplay_v4.fdx          │  │   prompt: "Close-up, rain..." │    │
│  │  • storyboard_panel_05.png    │  │   → generating (45s)          │    │
│  │  • mood_board_act2.json       │  │                               │    │
│  │                               │  │ 12:03:22 MemoryAgent.recall   │    │
│  │ OUTPUT:                        │  │   query: "Act 2 visual tone"  │    │
│  │  • shot_intent_05.json (v2)   │  │   → 3 results returned        │    │
│  │  • reference_frame_05.png     │  │                               │    │
│  └────────────────────────────────┘  └───────────────────────────────┘    │
│                                                                          │
│  ┌─── CRITIQUE BUS ────────────────────────────────────────────────┐      │
│  │ RECEIVED:                                                       │      │
│  │  • EditorAgent: "Shot 4 transition too abrupt" (12:02:58)      │      │
│  │  • AudienceSim: "Scene 2 clarity score 0.6, below 0.7" (12:01) │      │
│  │ SENT:                                                           │      │
│  │  • → EditorAgent: "Approved cut on beat 6" (12:03:10)          │      │
│  │  • → DoPAgent: "Use wider lens for Scene 3" (12:02:45)         │      │
│  └─────────────────────────────────────────────────────────────────┘      │
│                                                                          │
│  [Retry Task] [Skip] [Send Critique] [View Full History]                 │
└──────────────────────────────────────────────────────────────────────────┘
```

### 5.9 Agent Registry

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT REGISTRY                    Search: [____________]  Filter: [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CATEGORIES:                                                                │
│  [All 114] [Above-Line 5] [Camera 3] [Editorial 10] [Sound 4]              │
│  [Performance 5] [Distribution 4] [Education 14] [AI-Specialist 7]         │
│  [Meta-Orchestration 6] [Meta-Creative 7] [Meta-Research 7]                │
│  [Meta-Optimization 8] [Workflow Support 34]                                │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ # │ Agent               │ Pattern        │ Tools        │ Status    │   │
│  ├───┼─────────────────────┼────────────────┼──────────────┼───────────┤   │
│  │ 1 │ DirectorAgent       │ Self-Refine    │ Sora,Veo,Run │ ● Active  │   │
│  │ 2 │ ProducerAgent       │ Agentic Graph  │ Sheets,Tempo │ ● Active  │   │
│  │ 3 │ ScreenwriterAgent   │ Reflexion      │ Fountain,Emb │ ○ Idle    │   │
│  │ 4 │ ShowrunnerAgent     │ Multi-Debate   │ LongCtx,Vec  │ ○ Idle    │   │
│  │ ...│                    │                │              │           │   │
│  │46 │ PromptEngineerAgent │ DSPy/OPRO      │ Sora,Veo,Kli │ ● Active  │   │
│  │53 │ OrchestratorAgent   │ Agentic Graph  │ LangGraph    │ ● Active  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  點任何一行 → 開 Agent Detail Card（完整 capabilities 表）                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.10 Memory & Knowledge Panel

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  MEMORY & KNOWLEDGE                                                         │
├─────────────┬───────────────────────────────────────────────────────────────┤
│  SECTIONS:  │                                                               │
│             │  ┌─── PROJECT MEMORY（MemoryAgent） ─────────────────────┐    │
│  ● Project  │  │                                                       │    │
│    Memory   │  │  Search: [________________________] [Semantic] [Exact]│    │
│             │  │                                                       │    │
│  ○ Episodic │  │  Recent Entries:                                      │    │
│    Log      │  │  • "Act 2 tone: melancholic, rain motif" (12:02)     │    │
│             │  │  • "Character A wears blue in all exteriors" (11:58) │    │
│  ○ Series   │  │  • "Budget revised: VFX cap at $30" (11:45)          │    │
│    Bible    │  │  • "Style lock: Veo 3.1 seed #4412" (11:40)          │    │
│             │  │                                                       │    │
│  ○ Brand    │  │  Accessed by: DirectorAgent (6×), EditorAgent (3×),  │    │
│    Library  │  │              ScreenwriterAgent (2×)                   │    │
│             │  │                                                       │    │
│  ○ World    │  │  [+ Add Manual Entry]  [Export]  [Clear Stale]       │    │
│    DB       │  └───────────────────────────────────────────────────────┘    │
│             │                                                               │
└─────────────┴───────────────────────────────────────────────────────────────┘
```

### 5.11 Delivery Hub

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  DELIVERY HUB — "Luna"                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MASTER STATUS:  ⚠ 4/6 channels ready                                       │
│                                                                             │
│  ┌─── CHANNEL MATRIX ─────────────────────────────────────────────────┐     │
│  │ Channel    │ Format   │ QC     │ Captions │ A11y  │ C2PA  │ Status │     │
│  ├────────────┼──────────┼────────┼──────────┼───────┼───────┼────────┤     │
│  │ YouTube    │ H.264 4K │ ✓ Pass │ ✓ EN,ES  │ ✓ AA  │ ✓     │ Ready  │     │
│  │ TikTok     │ H.265 9:16│ ✓ Pass│ ✓ EN     │ ✓ AA  │ ✓     │ Ready  │     │
│  │ Meta       │ H.264 1080│ ✓ Pass│ ⚠ Pend   │ ✓ AA  │ ✓     │ ⚠ Pend │     │
│  │ Broadcast  │ ProRes 422│ ✓ Pass│ ✓ CC     │ ✓ AAA │ ✓     │ Ready  │     │
│  │ Theatrical │ DCP       │ ○ N/A │ ○ N/A    │ ○ N/A │ ✓     │ N/A    │     │
│  │ Archive    │ Master+Stems│✓ Pass│ ✓ All   │ ✓ AAA │ ✓     │ Ready  │     │
│  └────────────┴──────────┴────────┴──────────┴───────┴───────┴────────┘     │
│                                                                             │
│  ┌─── QC SUMMARY ─────────────────────────────────────────────────────┐     │
│  │  L1（Technical）：✓ Pass   Loudness -23 LUFS │ Color ΔE<2 │ Res ✓  │     │
│  │  L2（Creative）： ✓ Pass   Pacing B+ │ Beat-sync ✓ │ Style 0.87    │     │
│  │  L3（Compliance）：⚠ 1 issue  Caption lang gap（Meta - Spanish）    │     │
│  └─────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  [ Package All Ready ]  [ Fix Pending Issues ]  [ View Full QC Report ]     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.12 Settings — Router Configuration

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  ROUTER CONFIGURATION                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── MODEL ROUTING RULES ────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  Task Type           │ Primary Model  │ Fallback    │ Max $/task   │     │
│  │  ────────────────────┼────────────────┼─────────────┼──────────── │     │
│  │  Video Generation    │ Veo 3.1 (4K)   │ Kling 3.0   │ $2.50       │     │
│  │  Video (Budget)      │ Kling 3.0      │ Runway Gen-4│ $0.80       │     │
│  │  Voice Synthesis     │ ElevenLabs v3  │ —           │ $0.15       │     │
│  │  Avatar Rendering    │ HeyGen IV      │ Synthesia   │ $1.00       │     │
│  │  Image Generation    │ DALL-E 3       │ Midjourney  │ $0.08       │     │
│  │  LLM (Creative)      │ Gemini 2.5 Pro │ GPT-4o      │ $0.05       │     │
│  │  LLM (Judge/QA)      │ GPT-4o         │ Claude 4    │ $0.03       │     │
│  │  Music Generation    │ Udio           │ Suno        │ $0.50       │     │
│  │                                                                    │     │
│  │  [+ Add Rule]  [Import Preset]  [Optimize (CostOptimizerAgent)]    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── COST GUARDRAILS ───────────────────────────────────────────────┐      │
│  │  Global budget cap：$[___] per production                          │      │
│  │  Alert at： [80]% spend                                             │      │
│  │  Auto-downgrade quality at： [90]% spend                            │      │
│  │  Hard stop at： [100]% spend（需人類 override）                      │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.13 Prompt Lab（PromptEngineerAgent + PromptOptimizerAgent 介面）

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROMPT LAB                                              Production: "Luna" │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── PROMPT EDITOR ──────────────────────────────────────────────────┐     │
│  │  Agent: [DirectorAgent ▼]  Model: [Veo 3.1 ▼]  Shot: [#5 ▼]        │     │
│  │                                                                    │     │
│  │  ┌────────────────────────────────────────────────────────────┐    │     │
│  │  │ A slow dolly push through rain-slicked streets at golden   │    │     │
│  │  │ hour. Camera height: eye-level. Subject walks away from    │    │     │
│  │  │ camera, coat billowing. Style: melancholic neo-noir.       │    │     │
│  │  │ Aspect: 16:9, 1080p, 8s duration.                          │    │     │
│  │  └────────────────────────────────────────────────────────────┘    │     │
│  │                                                                    │     │
│  │  Parameters:                                                       │     │
│  │  Seed: [4412]  CFG: [7.5]  Steps: [50]  Neg: [artifacts, text]    │     │
│  │                                                                    │     │
│  │  [Generate ▶]  [Optimize (OPRO)]  [A/B Test]  [Seed Walk]          │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── OPTIMIZATION HISTORY ───────────────────────────────────────────┐     │
│  │  Iter │ CLIP-T │ Aesthetic │ Change Summary             │ Accepted │     │
│  │  ─────┼────────┼───────────┼────────────────────────────┼──────── │     │
│  │  1    │ 0.29   │ 5.8       │ Original prompt            │ No       │     │
│  │  2    │ 0.32   │ 6.2       │ Added "golden hour" time   │ No       │     │
│  │  3    │ 0.34   │ 6.5       │ Added camera motion detail │ ✓ Yes    │     │
│  │  4    │ 0.33   │ 6.4       │ Tried "steady" (regressed) │ No       │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── GENERATED OUTPUTS ──────────────────────────────────────────────┐     │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │     │
│  │  │ ▶ Iter 1    │  │ ▶ Iter 2    │  │ ▶ Iter 3 ✓  │                │     │
│  │  │ CLIP: 0.29  │  │ CLIP: 0.32  │  │ CLIP: 0.34  │                │     │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                │     │
│  │                                                                    │     │
│  │  [Compare Side-by-Side]  [Send to Director for Approval]          │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.14 Quality & Evaluation Dashboard

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  QUALITY DASHBOARD                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── OVERALL SCORES ─────────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  VBench:       ████████████████░░░░  0.82  (threshold: 0.75) ✓    │     │
│  │  CLIP-T avg:   █████████████████░░░  0.34  (threshold: 0.32) ✓    │     │
│  │  FVD:          ██████████████░░░░░░  142   (threshold: <180) ✓    │     │
│  │  Aesthetic:    ████████████████████  6.5/7 (threshold: 5.5) ✓     │     │
│  │  Audio STOI:   ██████████████████░░  0.88  (threshold: 0.85) ✓    │     │
│  │  Loudness:     ████████████████████  -23.1 LUFS (target: -23) ✓   │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── PER-SHOT BREAKDOWN ─────────────────────────────────────────────┐     │
│  │  Shot │ CLIP-T │ Hands │ Face-ID │ Temporal │ Style │ Status       │     │
│  │  ─────┼────────┼───────┼─────────┼──────────┼───────┼──────────── │     │
│  │  1    │ 0.35   │ ✓     │ 0.98    │ ✓        │ 0.87  │ ✓ Pass      │     │
│  │  2    │ 0.31   │ ⚠     │ 0.96    │ ✓        │ 0.85  │ ⚠ Review    │     │
│  │  3    │ 0.34   │ ✓     │ 0.97    │ ✓        │ 0.88  │ ✓ Pass      │     │
│  │  4    │ 0.36   │ ✓     │ 0.95    │ ⚠        │ 0.84  │ ⚠ Review    │     │
│  │  5    │ 0.34   │ ✓     │ 0.98    │ ✓        │ 0.86  │ ✓ Pass      │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── REGRESSION ALERTS ──────────────────────────────────────────────┐     │
│  │  ⚠ Shot 2: Hand artifact at frame 142 (score dropped 0.03)        │     │
│  │  ⚠ Shot 4: Temporal flicker at transition (score: 0.71 < 0.75)    │     │
│  │  [Auto-Fix All]  [Manual Review]  [Dismiss Non-Critical]          │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. 製作啟動流程（Production Start Flow）

由 idea 到 production 運行的完整旅程：

```text
使用者旅程：Brief → Launch → Monitor → Approve → Deliver

Step 1：到達 Dashboard
   │
   ├── 選項 A：點範本卡（A–J）→ Brief Studio（預填）
   ├── 選項 B：點「+ New Production」→ Brief Studio（空白）
   └── 選項 C：在全域搜尋輸入 → AI 建議範本
   │
   ▼
Step 2：Brief Studio
   │
   ├── 2a. 選擇／確認範本（啟動該 workflow 的 agent set）
   ├── 2b. 填寫 brief（title、vision、genre、duration、aspect、tone）
   ├── 2c. 上載參考（scripts、mood boards、audio refs、brand assets）
   ├── 2d. 設定約束（合規、平台、A11y、預算、deadline）
   └── 2e. 檢視 plan preview（PlannerAgent 預拆解估算）
   │
   ▼
Step 3：LAUNCH
   │
   ├── Brief → PlannerAgent（拆解成分段 DAG）
   ├── PlannerAgent → OrchestratorAgent（初始化執行）
   ├── OrchestratorAgent → RouterAgent（指派模型 + 代理人）
   ├── MemoryAgent 用 brief + refs 初始化
   └── UI 切換到 Production Console（DAG Canvas）
   │
   ▼
Step 4：PRE-PRODUCTION（自動）
   │
   ├── ScreenwriterAgent → script
   ├── StoryboardAgent → panels
   ├── ConceptArtistAgent → look dev
   ├── CastingAgent → voice/talent selection
   ├── ComposerAgent → initial themes
   ├── Creative meta-agents 協助（Ideation、NarrativeArc、Mood、Style）
   ├── Research meta-agents 提供上下文（Web、Archive、Trend）
   │
   ├── GateKeeperAgent 檢查 L1 criteria
   └── Gate Approval Dialog 出現 → 使用者批准 → 下一階段
   │
   ▼
Step 5：PRODUCTION（自動，可選 HiTL）
   │
   ├── DirectorAgent 發出 shot intents
   ├── PromptEngineerAgent 編寫生成 prompts
   ├── RouterAgent 路由到 Veo/Sora/Runway/Kling
   ├── CinematographerAgent 驗證構圖
   ├── AIQAConsistencyAgent 做逐幀 QC
   ├── Optimization agents 調整（Prompt、Cost、Latency）
   │
   ├── critique 訊息流動（Critique Feed 可見）
   ├── artifacts 生成後出現在 Gallery
   ├── 使用者可於 Critique Feed 的 human slot 介入
   │
   ├── GateKeeperAgent 檢查 L2 criteria
   └── Gate Approval Dialog → 使用者批准 → 下一階段
   │
   ▼
Step 6：POST-PRODUCTION（自動，可選 HiTL）
   │
   ├── EditorAgent 組裝剪輯
   ├── ColoristAgent 調色
   ├── SoundDesignAgent + ComposerAgent 鋪音訊
   ├── SoundMixerAgent 最終混音
   ├── VFXSupervisorAgent 合成
   ├── AccessibilityOptimizerAgent 加字幕／口述影像
   │
   ├── JudgeAgent 按 rubric 評分
   ├── GateKeeperAgent 檢查 L3 criteria
   └── Gate Approval Dialog → 使用者批准 → 交付
   │
   ▼
Step 7：DELIVERY
   │
   ├── Delivery Hub 顯示 channel matrix
   ├── DistributorAgent 按 outlet specs 封裝
   ├── ComplianceAgent 最終法務簽核
   ├── C2PA 溯源於所有輸出簽署
   ├── 使用者檢視最終 QC，批准發佈
   └── 資產發佈到目標渠道
   │
   ▼
Step 8：POST-RELEASE（可選）
   │
   ├── AnalystAgent 收集成效資料
   ├── RetentionOptimizerAgent / ROASOptimizerAgent 分析
   ├── Analytics Panel 顯示結果
   └── learning 回寫到 MemoryAgent，供未來 productions 使用
```

### 6.1 工作流差異（範本特定）

| 範本 | UI 差異重點 |
|----------|----------------------|
| A — Viral Hook | 壓縮時間線（2–5 分鐘完成）；TrendIntel 面板突出；留存曲線預覽 |
| B — UGC Ad | 成效目標面板；A/B 變體網格；ROAS 預測可見 |
| C — Animated Explainer | brief 內加入學習目標；assessment builder；Bloom-level tagger |
| D — Personalized Birthday | 變數範本編輯器；merge-field 預覽；批次渲染佇列 |
| E — AI Short Film | 完整 DAG 可見；52 craft agents 啟用；多次 gate 審批 |
| F — Corporate Training | LMS 封裝面板；SCORM 預覽；learner simulation 結果 |
| G — Music Video | beat-grid 時間線；音訊波形疊加；舞蹈參考 |
| H — AI Avatar | Avatar 設計工作室；聲線同意流程；lip-sync 驗證 |
| I — Documentary | 檔案研究面板；來源分級追蹤；訪談綜合 |
| J — Feature Film | episode/act 導航；series bible；全 114 agents；festival 策略 |

---

## 7. Composition Diagram 覆蓋地圖

Composition Diagram 每個 node/edge 都對應到特定 UI 面板：

```text
COMPOSITION DIAGRAM                          UI SURFACE(S)
═══════════════════                          ═════════════

[Brief]                                      S1: Brief Wizard
    │                                        S2: Template Selector
    ▼
PlannerAgent                                 S3: DAG Canvas（node）
    │                                        S11: Timeline View（plan → schedule）
    │                                        S8: Agent Inspector（drill-down）
    ▼
OrchestratorAgent                            S3: DAG Canvas（核心 orchestrator node）
    │                                        S11: Timeline View（phase progression）
    │                                        S22: Notification Center（escalations）
    │                                        S12: Budget Tracker（resource allocation）
    ▼
RouterAgent                                  S3: DAG Canvas（routing node）
    │                                        S13: Router Config（model selection rules）
    │                                        S21: Optimization Panel（cost/latency routing）
    ▼
52 Craft Agents（§1–§8）                      S3: DAG Canvas（all craft nodes）
    │                                        S4: Agent Node Cards
    │                                        S8: Agent Inspector（per-agent）
    │                                        S9: Artifact Gallery（outputs）
    │                                        S10: Artifact Viewer（preview/compare）
    │                                        S14: Prompt Lab（generation prompts）
    │                                        S15: Quality Dashboard（scores）
    │
    ├── CritiqueMessages ◄──────────────►    S6: Critique Feed（full stream）
    │                                        S8: Agent Inspector → Critique Bus tab
    │
    ▼
JudgeAgent                                   S3: DAG Canvas（judge node）
    │                                        S5: Gate Approval Dialog（scores）
    │                                        S6: Critique Feed（debate outcomes）
    ▼
GateKeeperAgent                              S3: DAG Canvas（gate node, amber）
    │                                        S5: Gate Approval Dialog（criteria checklist）
    │                                        S18: Compliance Checker（legal gates）
    ▲
    │
MemoryAgent                                  S7: Memory Panel
                                             S24: Series Bible Editor
                                             S8: Agent Inspector → recalls shown

Creative Meta-Agents                         S19: Creative Meta Panel
  IdeationAgent                                   Brainstorm cards
  NarrativeArcAgent                               Beat-sheet visualizer
  StyleTransferAgent                              Style-lock controls
  MoodBoardAgent                                  Mood board composer
  NoveltyAgent                                    Cliché warnings
  EmotionalArcAgent                               Emotion curve graph

Research Meta-Agents                         S20: Research Panel
  WebResearchAgent                                Live search results
  ArchiveResearchAgent                            Source cards
  TrendIntelligenceAgent                          Trend timeline
  CompetitorIntelligenceAgent                     Competitor grid
  CitationAgent                                   Source-grade badges
  InterviewSynthesisAgent                         Theme clusters
  BenchmarkResearchAgent                          Leaderboard diffs

Optimization Meta-Agents                     S21: Optimization Panel
  PromptOptimizerAgent                            S14: Prompt Lab（OPRO controls）
  CostOptimizerAgent                              S12: Budget Tracker + S13: Router Config
  LatencyOptimizerAgent                           Pipeline timing view
  RetentionOptimizerAgent                         Retention curve predictor
  ROASOptimizerAgent                              ROAS projection chart
  AccessibilityOptimizerAgent                     A11y compliance checklist
  EvaluationHarnessAgent                          S15: Quality Dashboard（benchmark runner）
  SafetyRedTeamAgent                              S18: Compliance → Red Team tab
```

---

## 8. 響應式與無障礙重點

### 8.1 Breakpoints

| Breakpoint | 版面適配 |
|-----------|-------------------|
| ≥1440px（Desktop XL） | 全殼：side nav + canvas + drawer 同時可見 |
| 1024–1439px（Desktop） | side nav 收納為 icon-only；drawer 覆蓋 canvas |
| 768–1023px（Tablet） | 單面板；tabs 切換 canvas/gallery/critique；drawer 全屏 |
| <768px（Mobile） | Dashboard + brief studio 可用；Production Console 只讀（監控） |

### 8.2 無障礙要求（WCAG 2.2 AA）

| 要求 | 實作 |
|-------------|---------------|
| 色彩對比 | 一般文字 ≥4.5:1；大字 ≥3:1；狀態用「形狀+顏色」 |
| 鍵盤導航 | 全鍵盤可用；focus rings；Cmd+K command palette |
| Screen reader | ARIA landmarks、live regions、agent 狀態播報 |
| 動作敏感 | Reduced motion 模式：DAG 動畫 → 靜態轉場 |
| 色盲友善 | 節點狀態以形狀（✓●○⚠✗）+ 顏色呈現；不只靠顏色 |

### 8.3 深色／淺色模式

兩個主題都支援。DAG canvas 在兩個模式都用柔和背景，確保節點可見性。

---

## 9. 元件庫摘要

### 9.1 核心元件

| 元件 | 用途 | 變體 |
|-----------|-------|----------|
| `AgentNodeCard` | DAG canvas 節點 | mini（DAG）、expanded（inspector）、list-row（registry） |
| `ArtifactCard` | Gallery 項目 | thumbnail、detail、compare |
| `CritiqueMessage` | Feed 項目 | info、warning、critical、resolved |
| `GateCheckpoint` | DAG + timeline | pending、reviewing、approved、rejected |
| `MetricBar` | 品質儀表板 | pass（綠）、warning（橙）、fail（紅） |
| `TimelineSwim` | phase swimlanes | pre-pro、production、post、delivery |
| `BriefField` | Brief Studio 輸入 | text、dropdown、slider、tag-input、file-drop、toggle |
| `DrawerPanel` | 詳細視圖容器 | bottom-slide、side-slide、full-screen |
| `CommandPalette` | 全域搜尋／操作 | Cmd+K |
| `NotificationBadge` | Top bar + nav | count badge、priority indicator |
| `ProvBadge` | C2PA 溯源 | verified、pending、unsigned |
| `BudgetGauge` | 成本追蹤 | 線性進度 + threshold markers |

### 9.2 複合模式（Composite Patterns）

| Pattern | 組合自 | 用於 |
|---------|--------------|---------|
| Agent Inspector | NodeCard + MetricBars + CritiqueMessages + ArtifactCards | Drawer / Full-screen |
| Gate Dialog | GateCheckpoint + checklist + ArtifactCards + action buttons | Modal overlay |
| Prompt Editor | Code editor + parameter sliders + output gallery + optimization history | Prompt Lab |
| Channel Row | Status badges + QC indicators + action buttons | Delivery Hub |
| Timeline Phase | TimelineSwim + milestone markers + budget overlay + gate markers | Timeline View |

---

## 10. 互動模式

### 10.1 Command Palette（Cmd+K）

任何位置都可用的全域搜尋 + 操作 launcher：

```text
┌───────────────────────────────────────────────┐
│  🔍 Search agents, artifacts, actions...       │
├───────────────────────────────────────────────┤
│  RECENT                                       │
│  → DirectorAgent Inspector                    │
│  → Shot Intent #5 artifact                    │
│  → Gate #2 approval                           │
│                                               │
│  ACTIONS                                      │
│  → New Production                             │
│  → Retry failed agents                        │
│  → Export all artifacts                       │
│  → Open Router Config                         │
│                                               │
│  AGENTS（type 時即時過濾）                      │
│  → DirectorAgent（● running）                  │
│  → EditorAgent（○ idle）                       │
│  → AIQAConsistencyAgent（● running）           │
└───────────────────────────────────────────────┘
```

### 10.2 Human-in-the-Loop 模式

| Trigger | UI 回應 | 使用者動作 |
|---------|-------------|-------------|
| 到達 gate checkpoint | Gate Approval Dialog + 通知 | Approve / Reject / Request Changes |
| Agent 要求人類輸入 | Critique Feed 突出 + 通知 badge | 在 critique feed 回覆 |
| 到達預算閾值 | Banner alert + 成本對話框 | Override / Downgrade / Stop |
| 合規阻塞 | 顯示包含法務細節的 modal | Resolve / Escalate |
| 品質回歸 | Quality Dashboard 警示 + 高亮受影響鏡頭 | Auto-fix / Manual review |

### 10.3 即時更新

| 資料 | 更新頻率 | UI 行為 |
|------|-----------------|-------------|
| Agent 狀態 | 1–5s | 節點顏色／符號平滑轉換 |
| Critique 訊息 | event-driven（websocket） | 新訊息滑入、badge 增加 |
| Artifacts | 完成時 | Gallery 出現卡片並動畫提示 |
| Budget burn | 每個 task 完成 | gauge 動畫、status bar 更新 |
| 品質分數 | 每次 evaluation | MetricBar 變化，回歸即警示 |
| Gate 狀態 | criteria 達成時 | GateCheckpoint 橙色跳動，觸發通知 |

### 10.4 批次操作（Bulk Operations）

| 操作 | 位置 | 範圍 |
|-----------|-------------|-------|
| Retry all failed | DAG Canvas 右鍵選單 | 所有失敗 agents |
| Approve all pending | Gate panel | 所有達標 gates |
| Export artifacts | Gallery 工具列 | 已選或全部 |
| Compare versions | Artifact viewer | 任意兩個版本 |
| Clear stale memory | Memory panel | N 日前舊 entries |

---

## 11. 通知與警示系統

### 11.1 優先級

| Priority | Trigger | 通知樣式 | 需要動作 |
|----------|---------|-------------------|-----------------|
| Critical | 合規阻塞、預算超支、法務到期 | 全屏 modal + 音效 | 是（不可關閉） |
| High | gate 待審、品質失敗 | toast + badge + status bar 閃爍 | 是（需在 5 分鐘內） |
| Medium | agent 完成、收到新 critique | badge + feed highlight | 否（資訊） |
| Low | 優化建議、記憶新增 | 只顯示 badge | 否 |

### 11.2 Notification Center

```text
┌────────────────────────────────────────────┐
│  NOTIFICATIONS（3 unread）                 │
├────────────────────────────────────────────┤
│  🔴 Compliance：Voice consent expiring     │
│     2 min ago · [Resolve]                  │
│                                            │
│  🟡 Gate #3 ready for review               │
│     5 min ago · [Open Gate]                │
│                                            │
│  🟡 AIQAAgent：Hand artifact in Shot 2     │
│     8 min ago · [View Shot]                │
│                                            │
│  ── Read ─────────────────────────────     │
│  🔵 EditorAgent completed rough cut        │
│  🔵 PromptOptimizer improved CLIP-T +0.02  │
│  🔵 BudgetAgent：42% spent                 │
└────────────────────────────────────────────┘
```

---

## 12. Data Model（UI State）

UI 會維護以下 state objects（由後端 WebSocket 同步）：

```typescript
interface Production {
  id: string;
  title: string;
  template: 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J';
  phase: 'brief'|'pre_production'|'production'|'post_production'|'delivery'|'released';
  brief: Brief;
  dag: DAGState;
  budget: BudgetState;
  gates: GateState[];
  artifacts: Artifact[];
  critiques: CritiqueMessage[];
  memory: MemoryEntry[];
  delivery: DeliveryState;
  analytics?: AnalyticsState;
}

interface DAGState {
  nodes: AgentNode[];        // All active agents with state
  edges: ArtifactEdge[];     // Handoff connections
  activePhase: string;
  completionPercent: number;
}

interface AgentNode {
  agentId: number;           // 1–114
  name: string;
  category: string;
  state: 'idle'|'running'|'blocked'|'complete'|'failed';
  currentTask?: Task;
  metrics: MetricScore[];
  critiquesReceived: CritiqueRef[];
  critiquesSent: CritiqueRef[];
  toolCalls: ToolCall[];
  artifacts: ArtifactRef[];
}

interface GateState {
  gateId: string;
  phase: string;
  criteria: GateCriterion[];
  judgeScore: number;
  status: 'pending'|'reviewing'|'approved'|'rejected';
  approvedBy?: string;
  c2paSigned: boolean;
}

interface Artifact {
  id: string;
  version: number;
  type: 'video'|'audio'|'image'|'text'|'data'|'package';
  producedBy: number;       // Agent ID
  qualityScores: Record<string, number>;
  c2paStatus: 'signed'|'pending'|'unsigned';
  parentAssets: string[];
  thumbnailUrl?: string;
}

interface CritiqueMessage {
  id: string;
  timestamp: string;
  fromAgent: number;
  toAgent: number | 'ALL';
  severity: 'info'|'warning'|'critical';
  content: string;
  attachments: ArtifactRef[];
  status: 'open'|'accepted'|'rejected'|'resolved';
  humanResponse?: string;
}
```

---

## 13. 技術棧建議

| 層 | 技術 | 理由 |
|-------|-----------|-----------|
| Framework | React 19 + Next.js 15 | Dashboard 用 SSR，Console 用 client-side 即時互動 |
| State Management | Zustand + React Query | 輕量；WebSocket 同步即時 DAG state |
| DAG Rendering | React Flow（xyflow） | 專為 node graph；支援 custom nodes |
| Timeline | 自訂 SVG + D3.js | swimlane + budget overlay |
| Video Preview | Shaka Player / Video.js | 多 codec + adaptive streaming |
| Audio Waveform | WaveSurfer.js | 輕量波形 |
| Real-time | WebSocket（Socket.io） | 狀態更新、critique bus、通知 |
| Styling | Tailwind CSS + Radix UI | 無障礙 primitives + utility-first |
| Charts | Recharts / Nivo | 品質指標、budget burn、analytics |
| Command Palette | cmdk | 成熟的 Cmd+K |
| Icons | Lucide React | 乾淨一致 |
| Code Editor | Monaco（prompt lab） | prompt/JSON 語法高亮 |

---

## 14. Wireframe 參考

參考配套 SVG 檔：
- [`master-shell.svg`](./master-shell.svg) — 全應用殼 wireframe
- [`surface-map.svg`](./surface-map.svg) — 覆蓋地圖：Composition Diagram → UI surfaces

---

*UI 設計文件完*
