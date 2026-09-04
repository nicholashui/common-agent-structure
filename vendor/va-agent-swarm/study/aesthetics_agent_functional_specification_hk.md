**綜合功能規格：美學代理 — 為 VA-Agent-Swarm 提供運算「藝術家感知 (Artiste Sense)」的評審與對齊服務**

**文件版本：** 1.0（最終版 - 完整且詳盡）
**日期：** 2026 年 5 月 29 日
**作者：** Grok (xAI) + 與使用者 Nicholas (nicholas_hui) 的協同迭代
**目標受眾：** 高級人工智慧工程/編碼代理（立即實施）
**目的：** 這是用於構建 **美學代理 (Aesthetics Agent)** 的 **最終生產級規範** — 一個有狀態的、多模態的評估與對齊服務，為整個 VA-Agent-Swarm 操作化一種模擬的 **「藝術家感知」**（藝術/美學直覺）。它是對 [`aesthetics_agents.md`](./aesthetics_agents.md) 的深度重新思考：該文件是一份 *方法綜述*，而本文件是一份 *可建構的代理契約*。它將「教 AI 藝術感知」從單一圖像評分器重新建構為一個 **共享的美學神經系統** — 一個每個生成代理都會諮詢的評審、一個每個微調迴圈都信任的獎勵訊號，以及一個將導演、品牌或藝術家的品味貫穿整條生產線的個人化引擎。

---

### 1. 執行摘要

**美學代理** 是整個 swarm 對「藝術家感知」的運算化體現。它並非 *取代* 人類品味 — 而是在 114 個代理之間以超人速度 **放大、編碼與傳播** 它。

它提供三項各自獨立、可組合的功能：

1. **評審者 (The Critic，感知)。** 一個多模態、多頭 (multi-head) 的評估器，依據一套分解後的美學評分標準（構圖、色彩和諧、光影、深度、情感共鳴、技術品質、風格忠實度、新穎性）為任何視覺產物 — 單一畫格、圖像或完整影片片段 — 評分。這是 swarm 共享的「眼睛」。
2. **對齊者 (The Aligner，精煉)。** 一個偏好與獎勵服務，把評審者的判斷轉化為可執行的回饋與訓練訊號 — 驅動自我精煉迴圈、偏好最佳化 (DPO/RLHF/RLAIF) 以及對 `PromptEngineerAgent`、`CinematographerAgent`、`ColoristAgent` 等的提示導引。
3. **品味守護者 (The Taste-Keeper，個人化)。** 一個設定檔儲存庫，記錄 *誰的* 美學主導一個專案 — 導演的 lookbook、品牌指引、藝術家的作品集、受眾族群的偏好 — 並以該設定檔為所有評分與對齊提供條件。

**為何這是「深度重新思考」而非一層包裝：**

| 樸素綜述說…… | 美學代理實際做的…… |
|---|---|
| 「訓練一個美學評分器（例如 NIMA、LAION）。」 | 視單一純量分數為 *不足且危險*。將美學分解為可審計的子屬性 + 影片的時間軸 (temporal) 軌道，並附帶校準後的不確定度。 |
| 「用評審者作為獎勵來微調生成器。」 | 把每次獎勵使用都包裹在 **防獎勵駭客 (anti-reward-hacking)** 護欄中（獎勵變異監控、集成分歧、OOD 偵測、KL 錨定）。 |
| 「在某一位藝術家的評分上做個人化。」 | 讓品味成為 **一等的、版本化的、受同意治理的設定檔**，流經 swarm 的交接契約與評論匯流排。 |
| 在靜態圖像上運作。 | **以影片為先 (video-native)**：時間連貫性、運動美學、剪輯節奏，以及逐鏡 vs 序列的評分。 |
| 美學感知 = 美感預測。 | 美學感知 = 美感 **+ 意圖忠實度 + 情感目標 + 品牌/風格契合 + 新穎性**，並加上閘控，使高分絕不來自泛泛的「漂亮垃圾 (pretty slop)」。 |

最終結果是一個其他代理 *無法在缺少它的情況下完成工作* 的單一代理：它在 `agents.md` 的第 #6、#10、#14、#15、#16、#39、#46、#49 等條目中被引用為「美學回歸器 / 基於 CLIP 的美學評分」，而本文件就是它的權威定義。

---

### 2. 背景：從「藝術家感知」到運算美學

來源文件 [`aesthetics_agents.md`](./aesthetics_agents.md) 將 **「藝術家感知」** 定義為藝術家培養出的直覺、感知與表達敏感度 — 對構圖、色彩和諧、節奏、比例、光影、深度與情感共鳴的「眼力」；一種結構性（3D）的觀看方式；一種表達的心理驅動力；以及一種務實、迭代的創作實踐。

其核心論點（本規範全盤採納）：

> AI 無法擁有 *真正的* 親歷式藝術感知（沒有意識、沒有情感），但它可以透過以下三者培養出一個 **高度成熟的模擬版本**：(a) 在人類美學判斷上訓練的評估器，(b) 偏好對齊回饋迴圈，以及 (c) 運算創造力的延伸。最強的結果來自 **人機共生 (human–AI symbiosis)**，而非自主的 AI 藝術家。

本規範把該框架視為基本事實，並回答綜述未解的唯一問題：**在一個 114 代理的影片生產系統內，能交付它的精確、可實作的代理契約究竟是什麼？**

---

### 3. 深度重新思考 — 五項重構

「深度重新思考」這份綜述產生了五項架構承諾。每一項都是對樸素「訓練一個評分器」配方的刻意背離。

**3.1 美學是向量，不是純量。** 單一 1–10 分既無法問責，又極易被獎勵駭客攻破。評審者輸出一個 **分解後的 AestheticVector** — 構圖、色彩、光影、深度、主體處理、技術品質、情感共鳴、風格忠實度與新穎性各自獨立的頭，並各帶一個校準後的信心值。純量只是 *閘控後的聚合*，永遠不是事實來源。

**3.2 美學是時間性的。** 這是一個影片 swarm。一組各自漂亮的畫格拼成的蒙太奇，可能在美學上並不連貫。評審者同時做 **逐畫格** 與 **逐序列** 評分：運動平順度、時間上的色彩/曝光穩定性、相對於類型先驗的剪輯節奏，以及「該片段是否讀起來像一個被作者統一過的姿態」。

**3.3 美學是「誰的」。** 依循 LAION-Aesthetics 審計對「一刀切」美感模型編碼了狹隘、未經審視品味的批評（[arXiv:2601.09896](https://arxiv.org/html/2601.09896v1)），本代理拒絕假裝存在一種普世美感。每個分數都以一個明確的 **AestheticProfile**（導演／品牌／藝術家／受眾族群／「中性基準」）為條件。個人化是預設，而非附加。近期研究顯示，由 LLM 訪談所引出的個人化美學模型，在預測個人判斷上可勝過泛用模型（[arXiv:2605.14761](https://arxiv.org/html/2605.14761v1)）。

**3.4 美學不可被駭。** 一旦評審者成為獎勵，生成器就會學會利用它（高頻紋理灌水、飽和度爆掉、「AI 油亮」光澤）。因此對齊者隨附一等的 **防獎勵駭客** 機制 — 集成分歧、獎勵變異監控（大型/多樣的獎勵模型保有高變異並抗崩潰，見 [arXiv:2509.08826](https://arxiv.org/html/2509.08826v1)）、對參考模型的 KL 錨定、OOD 偽影偵測器，以及推論時緩解（[arXiv:2510.01549](https://arxiv.org/abs/2510.01549)）。偏好富含理由 (rationale-bearing) 的偏好，而非不透明的純量（[arXiv:2503.11720](https://arxiv.org/html/2503.11720)）。

**3.5 美學由意圖閘控。** 脫離 brief 的美感就是噪音。聚合品質會乘上 **意圖忠實度**（是否符合鏡頭意圖／提示／品牌？）與 **情感目標契合**（是否擊中目標的情緒效價／喚起度？）。一張無視導演意圖的華麗圖像得分很低。這呼應了 [通用創意代理](./general_creative_agent_functional_specification.md) (SSOR) 的價值閘控選擇。

---

### 4. 正式美學模型

設一個產物 \( x \)（圖像或影片片段）在美學設定檔 \( p \)、意圖／brief \( b \) 與情感目標 \( e \) 之下被評估。

評審者產生一個 **分解後的美學向量**：

\[
\mathbf{A}(x \mid p) = \bigl[\, a_1, a_2, \dots, a_k \,\bigr], \quad a_i \in [0,1], \; \text{with confidence } \sigma_i
\]

涵蓋 \( k \) 個子屬性（即 **美學維度**，見 §6）。**閘控後的美學品質** 為：

\[
\operatorname{AQ}(x \mid p,b,e) \;=\; \underbrace{G\!\left(\mathbf{A}(x\mid p), \mathbf{w}_p\right)}_{\text{設定檔加權聚合}} \;\cdot\; \underbrace{I(x,b)}_{\text{意圖忠實度}} \;\cdot\; \underbrace{E(x,e)}_{\text{情感契合}} \;\cdot\; \underbrace{\big(1 - H(x)\big)}_{\text{防駭懲罰}}
\]

其中：
- \( G(\cdot, \mathbf{w}_p) \)：對屬性向量的設定檔加權聚合（權重 \( \mathbf{w}_p \) 來自當前作用中的 `AestheticProfile`；品牌可能重壓色彩／品牌契合，恐怖片 DoP 可能重壓光影／對比）。
- \( I(x,b) \in [0,1] \)：意圖忠實度（例如以 CLIP-T／VLM 將產物對照鏡頭意圖文字或參考做接地；依 `DirectorAgent` 評分標準目標 ≥ 0.32）。
- \( E(x,e) \in [0,1] \)：情感目標契合（相對目標的效價／喚起度回歸，與 `ComposerAgent` 情感弧驗證器共用）。
- \( H(x) \in [0,1] \)：駭客／偽影可能性（OOD 分數、集成分歧、偽影偵測器）— 高 \( H \) 會壓垮分數，無論表面多漂亮。

對影片，AQ 同時在逐畫格 **與** 序列層級計算，再合併：

\[
\operatorname{AQ}_{\text{clip}} = \alpha \cdot \operatorname{mean}_t \operatorname{AQ}(x_t) \;+\; \beta \cdot \operatorname{AQ}_{\text{temporal}}(x_{1:T}) \;-\; \gamma \cdot \operatorname{Var}_t\!\big[\text{exposure, color, identity}\big]
\]

懲罰時間上的不穩定（閃爍、色彩漂移、身分斷裂 — 與 `AIQAConsistencyAgent` #49 重疊）。

**硬性原則（寫進程式碼）：**
- **不得有裸純量。** 任何只請求 `AQ` 的消費者也會同時收到 \( \mathbf{A} \)、\( H \) 與最大失分維度。
- **不確定度隨行。** 每個分數都附信心值；低信心分數必須升級至 HiTL（人類介入）或第二個模型，絕不靜默放行。
- **要嘛有設定檔，要嘛拒絕。** 若未提供設定檔，代理使用一個明確標記的 `neutral_baseline_v{n}` 設定檔，並標示結果為品味無關 (taste-agnostic)。

---

### 5. 架構

美學代理是一個三子系統服務，共用同一個設定檔儲存庫與同一個模型註冊表。

```
                         ┌───────────────────────────────────────────────┐
                         │              AESTHETICS AGENT                   │
                         │                                                 │
  Artifact (img/video) ─▶│  ┌──────────────┐   ┌──────────────┐           │
  + Profile + Intent     │  │  THE CRITIC  │   │ THE ALIGNER  │           │
  + Emotion target       │  │  (Perceive)  │──▶│  (Refine)    │──┐        │
                         │  │ multi-head   │   │ reward +     │  │        │
                         │  │ evaluator    │   │ preference + │  │        │
                         │  └──────┬───────┘   │ critique gen │  │        │
                         │         │           └──────────────┘  │        │
                         │         ▼                              ▼        │
                         │  ┌──────────────┐          ┌────────────────┐  │
                         │  │ ANTI-HACK    │          │ THE TASTE-KEEPER│  │
                         │  │ guardrails   │◀────────▶│ (Personalize)   │  │
                         │  │ (ensemble,   │          │ AestheticProfile│  │
                         │  │ OOD, KL)     │          │ store (versioned)│ │
                         │  └──────────────┘          └────────────────┘  │
                         └───────────────────────────────────────────────┘
                                   │                          │
                          AestheticVerdict (JSON)     Profile updates
                                   ▼                          ▼
                          CRITIQUE BUS  ──────▶  consuming agents (#6,#10,#15,#39,#46,#49…)
```

**5.1 評審者（感知）。** 互補骨幹的集成：
- 在視覺骨幹（SigLIP / CLIP-ViT）上的快速 **回歸頭** — Aesthetic-Predictor-V2.5 風格的 MLP，用於大規模初篩。
- 一個 **VLM 評審**（Grok-4.x vision、Gemini 2.5 Pro、GPT-4o-vision），產出細粒度、屬性層級的自然語言評論 + 分數 — 即「可解釋的眼睛」。
- 專用偵測器：偽影／手部／臉部變形偵測器、ΔE 色彩漂移、曝光直方圖/區域分析、三分法與引導線幾何、相對風格參考的 FID/FVD、時間平順度（光流）、VBench 風格的影片指標。

**5.2 對齊者（精煉）。** 把判斷轉化為行動：
- **自我精煉回饋**：一份排序好的、可被機器讀取的評論（「場景 3 在 zone IV 曝光不足；主體與右緣相撞；跨剪輯色彩漂移 +6 ΔE」）。
- **獎勵訊號**：用於 RLHF / RLAIF / DPO / ReFL 風格擴散微調的純量／向量獎勵，永遠附帶變異與集成一致度的中繼資料。
- **偏好配對**：用於 DPO 風格訓練，附理由（富理由偏好）而非僅 A≻B。
- **提示導引提示**：交給 `PromptEngineerAgent` (#46) 的具體提示增量，以在 ≤3 次迭代內達標。

**5.3 品味守護者（個人化）。** 版本化、受同意治理的 `AestheticProfile` 儲存庫（見 §10），透過作品集匯入、成對偏好收集，以及 LLM 訪談引出（[arXiv:2605.14761](https://arxiv.org/html/2605.14761v1)）來建立。

**5.4 防駭護欄。** 包裹每一次獎勵發放的跨切面安全層（見 §11）。

---

### 6. 美學維度（分解後的評分標準）

評審者為每個維度發出分數 + 信心值。設定檔會重新加權它們；它們在被記錄前 *永不* 被壓平。

| # | 維度 | 衡量什麼 | 主要訊號 |
|---|------|---------|---------|
| D1 | **構圖 (Composition)** | 平衡、三分法、引導線、留白、取景、舞台清晰度 | 幾何偵測器 + VLM |
| D2 | **色彩和諧 (Color Harmony)** | 色盤連貫、對比、色溫一致、情緒向量 | 色彩直方圖、ΔE、色盤擷取 |
| D3 | **光影 (Light & Shadow)** | 曝光區域、主光/補光比、方向、動態範圍、情緒 | 直方圖/區域分析、VLM |
| D4 | **深度與形體 (Depth & Form)** | 3D 可讀性、層次、焦點深度、結構性「觀看」（依藝術家感知） | 深度估計 + VLM |
| D5 | **主體處理 (Subject Treatment)** | 主體突出度、視線、手勢、剪影可讀性 | 顯著性 + 姿態/特徵點 |
| D6 | **技術品質 (Technical Quality)** | 銳利度、雜訊、色帶、偽影、解析度充足度 | 偵測器 + IQA 模型 |
| D7 | **情感共鳴 (Emotional Resonance)** | 相對目標所喚起的效價/喚起度 | 情感回歸器（與 ComposerAgent 共用） |
| D8 | **風格忠實度 (Style Fidelity)** | 對 style bible / lookbook / 品牌的遵循 | 對參考集的 CLIP/嵌入距離 |
| D9 | **新穎性／辨識度 (Novelty)** | 相對「泛用 AI 垃圾」的原創性；倒 U（非最大化） | 相對語料庫的嵌入稀有度 |
| D10 | **時間美學 (Temporal Aesthetics)** *(影片)* | 運動平順、剪輯節奏、時間穩定、「一個作者化的姿態」 | 光流、VBench 風格、節拍同步 |

**新穎性註記 (D9)：** 依循 GCA 規範的 SSOR 倒 U 原則，新穎性在 *中等* 區帶被獎勵 — 太低 = 陳腔濫調/衍生；太高 = 不連貫。這正是防止代理獎勵平庸、統計上「漂亮」輸出的機制。

---

### 7. 功能需求

**7.1 輸入 (JSON)。**
```json
{
  "artifact_ref": "asset_id_or_uri",
  "media_type": "image | video_clip | frame_sequence",
  "profile_id": "director_lynchian_v3 | brand_acme_v2 | neutral_baseline_v4",
  "intent": { "shot_intent_text": "...", "reference_refs": ["..."], "genre_prior": "noir" },
  "emotional_target": { "valence": -0.4, "arousal": 0.7 },
  "mode": "screen | score | align | compare | refine",
  "constraints": { "aspect_ratio": "2.39:1", "color_space": "ACEScct", "deliverable": "HDR" },
  "budget": { "max_latency_ms": 800, "tier": "fast | deep" }
}
```

**7.2 輸出 — `AestheticVerdict` (JSON + Markdown)。**
```json
{
  "artifact_ref": "asset_id_v2",
  "profile_id": "director_lynchian_v3",
  "aesthetic_vector": { "composition": 0.81, "color_harmony": 0.74, "light": 0.62,
                        "depth": 0.70, "subject": 0.88, "technical": 0.91,
                        "emotion": 0.66, "style_fidelity": 0.79, "novelty": 0.55,
                        "temporal": 0.83 },
  "confidence": { "composition": 0.9, "light": 0.6, "...": "..." },
  "intent_fidelity": 0.79,
  "emotion_match": 0.71,
  "hack_likelihood": 0.04,
  "aesthetic_quality": 0.73,
  "top_failing_dimensions": ["light", "novelty"],
  "actionable_critique": [
    "Underexposed in zone IV; lift key +1/3 stop on subject left.",
    "Palette is conventional for genre; consider one strategic outlier hue."
  ],
  "prompt_steer_hints": ["add 'low-key chiaroscuro, single practical source'"],
  "uncertainty_flag": false,
  "escalate_to_hitl": false,
  "provenance": { "models": ["aesV2.5","grok-vision-4.x"], "ensemble_agreement": 0.86 }
}
```

**7.3 模式。**
- `screen` — 高量候選初篩的快速純量閘（僅回歸頭）。
- `score` — 完整分解向量 + 判斷。
- `align` — 為訓練／精煉迴圈發出獎勵／偏好訊號。
- `compare` — 對 N 個候選做成對／列表排序（用於「選出最佳一條 take」）。
- `refine` — 生成 → 評分 → 評論 → 建議，迭代（模仿藝術家的迭代迴圈）。

**7.4 有狀態性。** 對已接受／已拒絕產物的逐專案記憶會棘輪式 (ratchet) 收緊設定檔，並餵入 Reflexion 風格的情節記憶（與 swarm 原則「持續自我改進」一致）。

**7.5 非功能性。** 快速層初篩 ≤ 800 ms/產物；深層 ≤ 8 s；GPU 水平自動擴展；在固定設定檔 + 模型版本下具決定性（以利審計重現）。

---

### 8. 與 VA-Agent-Swarm 的整合

本代理是 **跨切面基礎設施**，在 [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md) §4 中與 Research Agent、GCA 及 Optimization Agent 一同註冊。

**8.1 消費者（誰呼叫它、為什麼）。**

| 代理（出自 `agents.md`） | 對美學代理的使用 |
|---|---|
| #6 CinematographerAgent (DoP) | 取代臨時的「基於 CLIP 的美學評分」— 構圖/光影/色彩自我精煉評分標準 |
| #10 ColoristAgent | ΔE 漂移、情緒向量契合、色盤連貫評分 |
| #14 StoryboardAgent / #15 ConceptArtistAgent / #16 ProductionDesignAgent | style-bible 遵循 + 構圖評分 |
| #39 FoodStylistAgent / #40 TravelCineAgent / #45 RealEstatePhotoAgent | 這些規範所引用的共享「美學回歸器」 |
| #46 PromptEngineerAgent | `refine` 模式 + `prompt_steer_hints`，在 ≤3 次迭代內達標 |
| #49 AIQAConsistencyAgent | 時間穩定性 / 偽影 (`hack_likelihood`) 交叉檢查 |
| #1 DirectorAgent / #56 JudgeAgent | 對候選 take 的平手裁決與盲測偏好裁決 |
| 交付與行銷 (#27, #28, #31) | 縮圖／鉤子美學評分以預測互動率 |

**8.2 評論匯流排 (Critique Bus)。** 判斷以 `critique_type: "aesthetic_feedback"`、`severity`、`rubric_score`、`artifact_ref` 發佈到 swarm 的結構化評論匯流排（`SYSTEM_REFERENCE.md` §7.1），讓任何代理都能非同步反應。

**8.3 交接契約 (Handoff Contract)。** `AestheticVerdict` 附加到產物的 `qc_status` 欄位（**共享產物交接契約**，`SYSTEM_REFERENCE.md` §7），使美學狀態隨著來源 (provenance) 流經每個階段。

**8.4 與鄰居的關係。**
- **vs. GCA（創造力）：** GCA *生成* 新穎而有用的候選；美學代理 *評斷與精煉* 它們。GCA 的新穎性分數 (D9) 由本代理供給。二者構成生成↔評估迴圈。
- **vs. AIQAConsistencyAgent (#49)：** AIQA 抓 *錯誤*（漂移、壞手、身分斷裂）；美學代理評斷 *品味*。`hack_likelihood` 是共享邊界 — 共同訓練、去重。
- **vs. 心理推薦 / AudienceSim：** 它們預測 *受眾* 偏好；美學代理編碼 *作者/品牌* 品味。一個設定檔可以是受眾族群設定檔，從而橋接兩者。

---

### 9. 三條運作迴圈

**9.1 評審迴圈（評估）。** `artifact → 集成評分 → 分解 → 以意圖/情感閘控 → 防駭檢查 → AestheticVerdict`。

**9.2 對齊迴圈（教生成器）。** 鏡像來源綜述的流程，加以強化：
1. 生成 N 個候選（基礎模型）。
2. `compare` 模式排序；`score` 模式分解。
3. 人類評審抽樣抽查一個子集（共生，而非完全自主）。
4. 建立 **富理由偏好配對** → DPO / RLHF / RLAIF / ReFL 更新。
5. 監控獎勵變異與集成一致度；若變異崩潰 → 懷疑駭客攻擊，凍結並升級。
6. 重複；生成器內化該品味並「直覺地」挑出更強的輸出。

**9.3 個人化迴圈（捕捉誰的品味）。**
1. 匯入作品集 / lookbook / 品牌指引 → 種子化嵌入設定檔。
2. 收集成對偏好和／或執行 **LLM 訪談引出**（[arXiv:2605.14761](https://arxiv.org/html/2605.14761v1)）以浮現潛在準則。
3. 擬合設定檔權重 \( \mathbf{w}_p \)；對保留判斷做驗證。
4. 版本化、簽署並儲存；向 swarm 公開 `profile_id`。

---

### 10. 個人化：`AestheticProfile`

一個一等的、版本化的、受同意治理的物件。

```json
{
  "profile_id": "director_lynchian_v3",
  "owner": "consenting_entity_id",
  "consent": { "scope": "project_x", "expires": "2027-01-01", "c2pa_signed": true },
  "weights": { "light": 0.22, "color_harmony": 0.18, "novelty": 0.15, "...": "..." },
  "exemplars": ["asset_uri_1", "..."],
  "anti_exemplars": ["asset_uri_9", "..."],
  "elicited_criteria": ["prefers low-key contrast", "avoids saturated reds", "..."],
  "embedding_centroid": "vec://...",
  "version": 3,
  "lineage": ["v1","v2","v3"]
}
```

設定檔類型：**Director**、**Brand**、**Artist**、**Audience-Cohort**（連結至 [心理推薦](./psychological_recommendation_agent_functional_specification.md)）、**Genre-prior**、**Neutral-baseline**。設定檔可組合（例如 `brand_acme ⊕ genre_noir`）並有明文化的優先序。

**治理：** 在具名人類的品味／作品集上做個人化，須在設定檔中記錄同意，並經 `ComplianceAgent` (#37) 核可 — 與聲音/肖像複製同等嚴格。

---

### 11. 獎勵駭客、失效模式與防禦

最大的單一風險：當評審者成為獎勵，生成器會學會 *欺騙眼睛*，而非 *取悅它*。

| 失效模式 | 症狀 | 防禦 |
|---|---|---|
| **紋理/細節灌水** | 高分、忙亂的高頻雜訊 | 偽影偵測器；頻域合理性檢查；人類抽查 |
| **飽和/對比爆掉** | 「AI 油亮」過飽和外觀 | ΔE 與色域界限；逐維度上限；品牌設定檔約束 |
| **模式崩潰 (Mode collapse)** | 所有輸出收斂到同一「安全」外觀 | 獎勵變異監控；大型/多樣獎勵集成保有變異（[arXiv:2509.08826](https://arxiv.org/html/2509.08826v1)） |
| **離群利用 (OOD)** | 在不像訓練資料的輸入上得高分 | OOD 偵測器 → 強制 `escalate_to_hitl`，絕不自動放行 |
| **意圖漂移** | 漂亮但無視 brief | 意圖忠實度閘 \( I(x,b) \) 乘上 AQ |
| **不透明純量過擬合** | 生成器鑽單一數字漏洞 | 富理由偏好（[arXiv:2503.11720](https://arxiv.org/html/2503.11720)）；分解向量永不壓平 |
| **品味單一化／偏誤** | 把一種狹隘美學編碼為「普世」 | 強制明確設定檔；依 LAION 批評做偏誤審計（[arXiv:2601.09896](https://arxiv.org/html/2601.09896v1)） |

**核心機制：** (1) **集成分歧** — 回歸頭、VLM 評審與偵測器必須一致；高分歧提高 \( H(x) \) 並觸發 HiTL。(2) 對齊期間對參考生成器做 **KL 錨定**，防止失控利用。(3) **推論時緩解**，無需完整微調即可對齊（[arXiv:2510.01549](https://arxiv.org/abs/2510.01549)）。(4) **保留人類評估** 作為不可妥協的事實基準 — 代理與人類評審的相關性本身被持續監控，並作為發佈閘門。

---

### 12. 技術架構與實作指南

- **核心類別：** `AestheticCritic`、`AttributeHead[]`、`EnsembleScorer`、`IntentGate`、`EmotionGate`、`AntiHackGuard`、`Aligner`、`PreferenceBuilder`、`TasteKeeper`、`AestheticProfile`、`AestheticsAgent`（門面）。
- **模型：** SigLIP/CLIP-ViT 骨幹 + MLP 回歸頭（快速層，Aesthetic-Predictor-V2.5 血統）；透過 swarm LLM 供應商的 VLM 評審（Grok-4.x vision / Gemini 2.5 Pro / GPT-4o）；偵測器集（偽影、ΔE、深度、光流、FID/FVD、VBench 風格）。
- **框架：** PyTorch + `diffusers`（用於 ReFL/DPO 掛鉤）；LangGraph 節點做編排；FastAPI 服務；Redis Streams 做評論匯流排發佈。
- **儲存：** 向量 DB（Chroma/Pinecone）存範例與嵌入；設定檔 DB（版本化、簽署）；情節記憶供 refine 迴圈學習。
- **來源 (Provenance)：** 每個判斷都記錄模型版本、集成一致度、設定檔版本 → 對齊 C2PA 的審計軌跡。
- **交付物：** repo 骨架、`AestheticVerdict` schema、設定檔 schema、範例 notebook（圖像評分、影片評分、DPO 對齊迴圈、設定檔引出）、給 #6/#10/#46/#49 的整合轉接器。

---

### 13. 評估與成功標準

| 標準 | 目標 |
|---|---|
| 與人類美學評分的相關性（保留集） | 基準上 Spearman ρ ≥ 0.75；個人化設定檔上 ≥ 0.85 |
| 個人化 > 泛用 | 設定檔模型在預測擁有者成對選擇上勝過 `neutral_baseline`（依 [arXiv:2605.14761](https://arxiv.org/html/2605.14761v1)） |
| 盲測偏好（下游） | 經本代理對齊的輸出在盲測成對中勝過未對齊者 ≥ 55%（Arena 風格） |
| 抗獎勵駭客 | 在一次微調過程中維持獎勵變異；模式崩潰率低於門檻 |
| 防駭召回率 | 人類標記的「欺騙眼睛」案例中 ≥ 95% 被 `hack_likelihood` 抓到 |
| 延遲 | 快速層 ≤ 800 ms；深層 ≤ 8 s |
| 校準 | 信心校準良好（ECE 低於門檻）；低信心可靠升級 |
| 可追溯性 | 100% 判斷攜帶分解向量 + 來源 |

---

### 14. 限制與未來方向

- **沒有真正的親歷式美學。** 代理的「感知」是統計性與衍生性的；它沒有自發性或個人衝動。它是人類品味的 *放大器* — 最佳用法是共生，並在新穎或低信心判斷上加入 HiTL。
- **品味是有爭議的。** 即使有明確設定檔，語料庫與評審群仍帶偏誤；代理會浮現它所編碼的是 *誰的* 品味，而非宣稱普世性。
- **獎勵駭客是軍備競賽。** 防禦只能降低、無法消除利用；保留人類評估仍是事實基準與發佈閘門。
- **未來：** 更大的多模態評審；以腦活動／生理訊號代理情感共鳴；具身／3D 結構性「觀看」；更緊密的藝術家共訓迴圈；與 `ComposerAgent`、`ChoreographyAgent` 共享的跨模態美學（圖像↔音樂↔運動）。

---

### 15. 參考文獻（精選，2024–2026）

基礎與綜述（出自 [`aesthetics_agents.md`](./aesthetics_agents.md)）：
- NIMA — Neural Image Assessment（CNN 美學分佈預測）。
- LAION-Aesthetics / CLIP+MLP improved aesthetic predictor；Aesthetic Predictor V2.5（SigLIP 基礎）。
- 多任務／統一美學模型（UniQA、HumanAesExpert 血統）；VBench（影片美學/品質基準）。
- 擴散模型的美學後訓練；擴散的 RLHF（DDPO、ReFL、DPOK、RewardDance）。

當前接地（2026 年 5 月經網路驗證；*內容為符合授權限制已改寫*）：
- 透過 LLM 訪談 + 語意特徵的個人化美學 — [arXiv:2605.14761](https://arxiv.org/html/2605.14761v1)。
- LAION-Aesthetics 預測器的審計/民族誌（「誰的品味」）— [arXiv:2601.09896](https://arxiv.org/html/2601.09896v1)。
- 視覺生成中的獎勵縮放（大型 RM 透過保有變異抗獎勵駭客）— [arXiv:2509.08826](https://arxiv.org/html/2509.08826v1)。
- 緩解 T2I 擴散推論時對齊的獎勵駭客 — [arXiv:2510.01549](https://arxiv.org/abs/2510.01549)。
- 擴散微調的富偏好最佳化（富理由偏好）— [arXiv:2503.11720](https://arxiv.org/html/2503.11720)。
- 重新思考擴散模型中的 DPO — [arXiv:2505.18736](https://arxiv.org/abs/2505.18736)。
- 透過 RL + 獎勵建模的擴散對齊與安全 — [arXiv:2505.17352](https://arxiv.org/abs/2505.17352)。

系統內參考：
- [`aesthetics_agents.md`](./aesthetics_agents.md) — 藝術家感知的來源綜述。
- [`general_creative_agent_functional_specification.md`](./general_creative_agent_functional_specification.md) — SSOR 創造力（迴圈的生成側；新穎性倒 U）。
- [`agents.md`](./agents.md) — 消費代理（#6、#10、#14–16、#39、#46、#49）。
- [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md) — 評論匯流排 (§7.1)、交接契約 (§7)、跨切面註冊 (§4)。
- [`psychological_recommendation_agent_functional_specification.md`](./psychological_recommendation_agent_functional_specification.md) — 受眾族群設定檔。

---

**本規範完整、自足，可立即進入編碼。** 它把「藝術家感知」綜述轉化為一個可建構、與 swarm 整合的代理：一個分解式多模態評審者、一個抗駭對齊者，以及一個受同意治理的品味守護者 — VA-Agent-Swarm 的共享美學神經系統。

請完全照寫實作。最終的美學代理將賦予全部 114 個代理一隻單一、可信、可個人化的「眼睛」。

**規範結束**
*存為 `aesthetics_agent_functional_specification_hk.md`。*
