# 專案建立與管理流程

> 定義位於 productions 之上的 Project 層 — 讓使用者在任何代理人啟動、任何費用產生之前，就可以先規劃、迭代與協作。

---

## 核心概念：Project vs. Production

```text
PROJECT = 容器（免費、持久、可協作）
PRODUCTION = 執行（要花錢、會跑代理人、會產出素材）

┌─────────────────────────────────────────────────────────────────┐
│  PROJECT「Brand Campaign Q3」                                   │
│  （建立免費、保留免費、規劃免費）                               │
│                                                                 │
│  ├── 共享資產：品牌套件、聲線、風格參考                          │
│  ├── 團隊：擁有人 + 編輯 + 審閱者                                │
│  ├── 預算池：已分配 $240                                         │
│  ├── 預設設定：合規、模型、平台                                  │
│  │                                                              │
│  ├── Production 1：「Hero Video」（類型 E，已完成 ✓，$62）       │
│  ├── Production 2：「TikTok Cut」（類型 A，進行中 ●，$28）       │
│  └── Production 3：「Training」（類型 F，草稿 ○，$0）            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

關鍵規則：在使用者明確按下 [▶ Launch] 前，不會花任何錢。
          之前的一切都是免費準備。
```

---

## 使用者旅程：由零到開始運行 Production

```text
Step 1：建立 Project ─────────────────── $0（即時、免費）
Step 2：準備（資產、團隊、設定） ─────── $0（可用數天／數週）
Step 3：建立 Production 草稿 ─────────── $0（brief 已儲存，可編輯）
Step 4：取得成本估算 ────────────────── $0（PlannerAgent 預覽）
Step 5：啟動 Production ─────────────── $$$（代理人從這裡才開始）
Step 6：監控 + 審批 ───────────────────（production 運行中）
Step 7：交付 ─────────────────────────（完成）
Step 8：建立下一個 Production ───────── 重覆 Step 3
```

---

## 第 1 頁：Dashboard（加入 Projects）

```text
┌─────────────────────────────────────────────────────────────────────┐
│  DASHBOARD                                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─── 我的 Projects ────────────────────────────────────────────┐    │
│  │                                                             │    │
│  │  [+ New Project]                                            │    │
│  │                                                             │    │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌───────────┐ │    │
│  │  │ Brand Q3         │  │ Luna Short Film  │  │ + New     │ │    │
│  │  │ 3 productions    │  │ 1 production     │  │ Project   │ │    │
│  │  │ 2 running · $90  │  │ completed · $95  │  │           │ │    │
│  │  │ Updated: 2m ago  │  │ Updated: 3d ago  │  │           │ │    │
│  │  └──────────────────┘  └──────────────────┘  └───────────┘ │    │
│  │                                                             │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── 進行中 Productions（跨所有 Projects） ────────────────────┐    │
│  │  ┌─────────────┐  ┌─────────────┐                          │    │
│  │  │ Hero Video  │  │ TikTok Cut  │                          │    │
│  │  │ Brand Q3    │  │ Brand Q3    │                          │    │
│  │  │ ████████░░  │  │ ██████░░░░  │                          │    │
│  │  └─────────────┘  └─────────────┘                          │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌─── 快速開始（略過 project 設定） ────────────────────────────┐    │
│  │  「只想快手做一個？」→ 選範本，自動建立 project              │    │
│  │  [A Hook] [B UGC] [C Explainer] [D Birthday] [E Film] ...    │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 第 2 頁：建立 Project 對話框

```text
┌──────────────────────────────────────────────────────────────────┐
│  建立新 Project                                         [×]       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Project 名稱： [________________________________]               │
│                                                                  │
│  描述（可選）：                                                   │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ 例如：「Q3 品牌曝光活動，涵蓋社交 + 官網」                 │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── 預算池 ───────────────────────────────────────────────┐    │
│  │  所有 productions 的總預算：$[_____]                     │    │
│  │  ☐ 無上限（按用量付款）                                   │    │
│  │  付款方式： [Credit card ending 4242 ▼]                   │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── 團隊（可選 — 可之後再加） ────────────────────────────┐    │
│  │  你：Owner                                                │    │
│  │  [+ Invite]  ______@email.com  角色： [Editor ▼]           │    │
│  │                                                           │    │
│  │  角色：                                                   │    │
│  │  • Owner — 完整控制、付款、刪除                           │    │
│  │  • Editor — 建立／啟動 productions、管理資產               │    │
│  │  • Reviewer — 檢視、評論、審批 gates                       │    │
│  │  • Viewer — 只讀                                          │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── 預設值（套用到所有 productions，除非另外覆寫） ───────┐    │
│  │  合規：☑ C2PA  ☑ WCAG AA  ☐ SAG-AFTRA  ☐ GDPR           │    │
│  │  模型偏好： [Cost-optimized ▼]                            │    │
│  │    選項：Cost-optimized │ Quality-first │ Speed-first     │    │
│  │  品牌套件： [Upload now ▼] 或 [Add later]                 │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│              [ Cancel ]           [ Create Project ]             │
│                                                                  │
│  ℹ️ 建立 project 是免費的。只有在你啟動 production 時才會收費。 │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 第 3 頁：Project 工作區

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROJECT：「Brand Campaign Q3」                      [Archive] [Settings ⚙]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  分頁： [Overview] [Productions] [Assets] [Team] [Settings] [Activity]      │
│                                                                             │
├─── OVERVIEW 分頁 ───────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── 狀態卡片 ────────────────────────────────────────────────────────┐    │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐   │    │
│  │  │Productions │  │  Budget    │  │   Team     │  │  Assets    │   │    │
│  │  │     3      │  │ $90/$240   │  │  3 members │  │  12 files  │   │    │
│  │  │ 1✓ 1● 1○  │  │ 38% used   │  │            │  │            │   │    │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── Productions ─────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  [+ New Production]     排序： [Recent ▼]     篩選： [All ▼]          │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ✓「Hero Video」       │ 類型 E │ 2 天前完成                  │    │    │
│  │  │   成本：$62 │ 時長：5:20 │ 交付：YouTube、TikTok           │    │    │
│  │  │   [View Artifacts]  [View Analytics]  [Duplicate as Draft]  │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ●「TikTok Cut」       │ 類型 A │ 運行中 — Production 階段     │    │    │
│  │  │   成本：$28 │ 進度：55% │ ETA：2 分鐘                       │    │    │
│  │  │   [Open Console]  [Pause]                                   │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ○「Training Module」  │ 類型 F │ 草稿 — 未啟動               │    │    │
│  │  │   成本：$0 │ Brief：完成 80% │ 預估成本：約 $35            │    │    │
│  │  │   [Edit Brief]  [Get Estimate]  [▶ Launch]  [Delete]        │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── 最近活動 ─────────────────────────────────────────────────────────┐    │
│  │  • 2 分鐘前：「TikTok Cut」— EditorAgent 完成 rough cut              │    │
│  │  • 5 分鐘前：「TikTok Cut」— Gate #1 由你審批通過                    │    │
│  │  • 2 天前：「Hero Video」— 已交付到 YouTube + TikTok                 │    │
│  │  • 3 天前：Sarah 以 Reviewer 身份加入                                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第 4 頁：Assets 分頁（共享資產庫）

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROJECT：「Brand Campaign Q3」> ASSETS                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [+ Upload Assets]   [Connect Brand Kit]                                    │
│                                                                             │
│  ┌─── 品牌套件（Brand Kit） ───────────────────────────────────────────┐    │
│  │  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐                                  │    │
│  │  │logo│ │font│ │color│ │guide│ │tone│                                 │    │
│  │  │.svg│ │.otf│ │.json│ │.pdf│ │.md │                                 │    │
│  │  └────┘ └────┘ └────┘ └────┘ └────┘                                  │    │
│  │  會自動載入每個 production 的 BrandAgent                               │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── 聲線庫（Voice Library） ─────────────────────────────────────────┐    │
│  │  🎤「Brand Voice A」— 有活力、年輕、ElevenLabs clone                  │    │
│  │  🎤「Brand Voice B」— 權威、成熟、自訂訓練                            │    │
│  │  🎤「Narrator」— 中性、清晰、標準 TTS                                 │    │
│  │  [+ Add Voice]                                                        │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── 風格參考（Style References） ───────────────────────────────────┐    │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                   │    │
│  │  │ ref_mood1.jpg│ │ ref_style.mp4│ │ ref_comp.png│                  │    │
│  │  │「Neo-noir」  │ │「Pacing ref」│ │「Framing」  │                  │    │
│  │  └─────────────┘ └─────────────┘ └─────────────┘                   │    │
│  │  [+ Add Reference]                                                   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── 劇本與文件（Scripts & Documents） ───────────────────────────────┐    │
│  │  📄 brand_messaging_guide.md                                         │    │
│  │  📄 target_audience_research.pdf                                     │    │
│  │  📄 competitor_analysis.xlsx                                         │    │
│  │  [+ Upload Document]                                                 │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ℹ️ 這裡的所有資產都會自動可供此 project 的每個 production 使用。            │
│    代理人會引用它們而毋須重覆上載。                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第 5 頁：Production 草稿（啟動前可編輯）

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODUCTION 草稿：「Training Module」    狀態：DRAFT（未啟動）               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── BRIEF 編輯器 ───────────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  範本： [F] Corporate Training   [Change]                          │     │
│  │                                                                    │     │
│  │  標題： [Training Module: Product Onboarding___]                   │     │
│  │                                                                    │     │
│  │  願景：                                                            │     │
│  │  ┌──────────────────────────────────────────────────────────────┐  │     │
│  │  │ 一段 10 分鐘互動式訓練影片，教新員工如何使用我們的儀表板。      │  │     │
│  │  │ 風格要現代、友善，並包含知識檢核。                              │  │     │
│  │  └──────────────────────────────────────────────────────────────┘  │     │
│  │                                                                    │     │
│  │  時長： [10 min]  格式： [16:9]  語氣： [friendly, professional]   │     │
│  │  學習目標： [Tag: navigate dashboard, create report, ...]          │     │
│  │  評量方式： [Quiz after each section ▼]                            │     │
│  │  交付： ☑ SCORM  ☑ xAPI  ☐ Standalone video                        │     │
│  │                                                                    │     │
│  │  來自 project 的參考： ☑ Brand Kit  ☑ Voice「Brand Voice A」        │     │
│  │  另外：已上載 [product_screenshots.zip]                             │     │
│  │                                                                    │     │
│  │  此 production 的預算： $[35___]                                    │     │
│  │  （Project 預算池尚餘：$150 / $240）                                │     │
│  │                                                                    │     │
│  │  最後儲存：2 分鐘前（自動儲存）                                     │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── 成本估算預覽 ───────────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  [🔄 Refresh Estimate]   上次估算：10 分鐘前                        │     │
│  │                                                                    │     │
│  │  預計拆解：                                                        │     │
│  │  • 劇本 + 教學設計：~$3                                            │     │
│  │  • Avatar 渲染（10 分鐘）：~$12                                    │     │
│  │  • 聲音合成：~$4                                                   │     │
│  │  • 動態圖形：~$6                                                   │     │
│  │  • 評量生成：~$2                                                   │     │
│  │  • QC + 合規：~$3                                                  │     │
│  │  • LMS 封裝：~$1                                                   │     │
│  │  ─────────────────────────────                                    │     │
│  │  總估算：~$31（±15%）                                              │     │
│  │                                                                    │     │
│  │  需要代理人：18 │ 預計時長：約 8 分鐘                               │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── 團隊對草稿的評論 ───────────────────────────────────────────────┐     │
│  │  Sarah（Reviewer）：「可否加一節講報表匯出？」                      │     │
│  │  你：「好主意，已加到學習目標」                                     │     │
│  │  [+ Add comment]                                                   │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── 操作 ───────────────────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  [ Save Draft ]   [ Share for Review ]   [ ▶ Launch Production ]    │     │
│  │                                                                    │     │
│  │  ▶ Launch 會：                                                      │     │
│  │    • 從 project 預算池扣除最多 $35                                  │     │
│  │    • 啟動 18 個代理人（Instructional、Avatar、Voice、LMS、...）     │     │
│  │    • 開始 production — 你會在 Production Console 監控                │     │
│  │    • 預計完成：約 8 分鐘                                            │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 啟動確認對話框

```text
┌──────────────────────────────────────────────────────────┐
│  啟動 Production                                          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Production：「Training Module」                           │
│  範本：F（Corporate Training）                             │
│  Project：「Brand Campaign Q3」                            │
│                                                          │
│  ┌─── 成本總結 ───────────────────────────────────────┐   │
│  │  預計成本：~$31（預算上限：$35）                    │   │
│  │  Project 剩餘預算：$150                              │   │
│  │  此次啟動後：~$119 剩餘                             │   │
│  └────────────────────────────────────────────────────┘   │
│                                                          │
│  ┌─── 將會發生甚麼 ───────────────────────────────────┐   │
│  │  1. PlannerAgent 拆解你的 brief                      │   │
│  │  2. 啟動 18 個代理人（InstructionalDesign、         │   │
│  │     Avatar、Voice、MotionGraphics、LMS、...）        │   │
│  │  3. 你會在 Production Console 看到進度               │   │
│  │  4. Gate 審批會暫停等待你檢視                         │   │
│  │  5. 預計完成：約 8 分鐘                              │   │
│  └────────────────────────────────────────────────────┘   │
│                                                          │
│  ☑ 我明白這會扣除我的 project 預算                        │
│                                                          │
│         [ Cancel ]          [ ▶ Launch Now ]             │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 更新後的資訊架構

```text
ROOT
├── Dashboard
│   ├── My Projects（網格）
│   ├── Active Productions（跨所有 projects）
│   └── Quick Start（範本選擇器 → 自動 project）
│
├── Project Workspace（每個 project）             ← 新增
│   ├── Overview（狀態卡、productions 列表、活動）
│   ├── Productions（列表：draft/running/complete）
│   ├── Assets（共享品牌套件、聲線、參考、文件）
│   ├── Team（成員、角色、邀請）
│   ├── Settings（預算、預設、合規、模型）
│   └── Activity（project 事件記錄）
│
├── Production Draft（每個 production，啟動前）     ← 新增
│   ├── Brief Editor（完整可編輯表單）
│   ├── Cost Estimate Preview
│   ├── Team Comments
│   └── Launch Button
│
├── Production Console（每個 production，啟動後）    ← 既有
│   ├── DAG Canvas
│   ├── Timeline View
│   ├── Artifact Gallery
│   ├── Critique Feed
│   ├── Gate Control
│   └── Agent Inspector
│
├── Agent Registry                                  ← 既有
├── Memory & Knowledge                               ← 既有
├── Delivery Hub                                     ← 既有
├── Settings & Admin                                 ← 既有
└── Help & Docs                                      ← 既有
```

---

## API：Project 層（後端）

```text
不涉及代理人 — 純 CRUD 操作：

POST   /api/projects                                   建立 project
GET    /api/projects                                   列出 projects
GET    /api/projects/{id}                              取得 project
PUT    /api/projects/{id}                              更新 project
DELETE /api/projects/{id}                              封存 project

POST   /api/projects/{id}/assets                       上載共享資產
GET    /api/projects/{id}/assets                       列出資產
DELETE /api/projects/{id}/assets/{aid}                 移除資產

POST   /api/projects/{id}/members                      邀請成員
PUT    /api/projects/{id}/members/{uid}                變更角色
DELETE /api/projects/{id}/members/{uid}                移除成員

POST   /api/projects/{id}/productions                  建立草稿（$0）
GET    /api/projects/{id}/productions                  列出 productions
PUT    /api/projects/{id}/productions/{pid}/brief      編輯 brief（僅草稿）
POST   /api/projects/{id}/productions/{pid}/estimate   預覽成本
POST   /api/projects/{id}/productions/{pid}/launch     ← 代理人從這裡才開始
POST   /api/projects/{id}/productions/{pid}/pause      暫停運行中
POST   /api/projects/{id}/productions/{pid}/resume     恢復暫停
POST   /api/projects/{id}/productions/{pid}/duplicate  複製為新草稿
DELETE /api/projects/{id}/productions/{pid}            刪除草稿
```

---

## 資料模型

```typescript
interface Project {
  id: string;
  name: string;
  description?: string;
  owner_id: string;
  status: "active" | "archived";
  
  // Budget
  budget_pool: number | null;      // null = no limit
  budget_spent: number;            // sum of all production spending
  billing_method_id: string;
  
  // Team
  members: {
    user_id: string;
    role: "owner" | "editor" | "reviewer" | "viewer";
    joined_at: Date;
  }[];
  
  // Shared resources
  shared_assets: {
    id: string;
    type: "brand_kit" | "voice" | "style_ref" | "document" | "script";
    name: string;
    url: string;
    metadata: object;
  }[];
  
  // Defaults
  default_settings: {
    compliance: string[];
    model_strategy: "cost_optimized" | "quality_first" | "speed_first";
    platform_targets: string[];
  };
  
  // Metadata
  created_at: Date;
  updated_at: Date;
}

interface Production {
  id: string;
  project_id: string;
  title: string;
  template: 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J';
  
  // Lifecycle
  status: "draft" | "launching" | "running" | "paused" | "completed" | "failed";
  
  // Brief (editable while draft)
  brief: {
    vision: string;
    genre?: string;
    duration: number;
    aspect_ratio: string;
    tone: string[];
    target_audience: string;
    references: string[];          // asset IDs (shared + production-specific)
    constraints: object;
    platform_targets: string[];
    template_specific: object;     // learning objectives, beat count, etc.
  };
  
  // Budget
  budget_cap: number;
  budget_spent: number;
  
  // Estimate (from PlannerAgent preview)
  estimate?: {
    cost_low: number;
    cost_mid: number;
    cost_high: number;
    agents_needed: number;
    estimated_duration_seconds: number;
    breakdown: { category: string; cost: number }[];
    generated_at: Date;
  };
  
  // Team comments on draft
  comments: {
    user_id: string;
    content: string;
    created_at: Date;
  }[];
  
  // Only populated after launch
  dag?: DAGState;
  artifacts?: Artifact[];
  launched_at?: Date;
  completed_at?: Date;
  
  created_at: Date;
  updated_at: Date;
}
```

---

## 快速開始路徑（給沒有耐性的人）

不想先設好 project 的使用者仍可以走捷徑：

```text
Dashboard → 按範本 [A Viral Hook] →

系統自動建立：
  • Project：「Untitled Project」（之後可改名）
  • Production：「Viral Hook」（預填 brief）
  • 進入草稿模式的 Brief Editor
  
使用者填最少資料 → 按 [▶ Launch] → 代理人開始

這個「project」仍然存在 — 之後可以加更多 productions、
改名、邀請團隊，但初始阻力接近零。
```

---

## 總結：改了甚麼

| 之前（原設計） | 之後（加入 Project 層） |
|--------------------------|---------------------------|
| Dashboard → Brief Studio → Launch（即刻） | Dashboard → Project → Draft → Edit → Launch（準備好才啟動） |
| 每個 production 都是獨立 | Productions 都在 Projects 之內 |
| 每個 production 各自上載資產 | 每個 project 有共享資產庫 |
| 啟動前無法團隊協作 | 團隊可審閱草稿、留下評論 |
| 承諾之前看不到成本 | 草稿可免費估算成本 |
| 想改 brief 就要先花錢 | 草稿模式 = 無限次免費編輯 |
| 沒有方式把相關影片分組 | Project 把活動／變體聚合 |
| 只有每個 production 的預算 | Project 預算池 + 每個 production 預算上限 |
