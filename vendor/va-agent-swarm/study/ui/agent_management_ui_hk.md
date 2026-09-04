# 代理人管理 UI — 配置、測試與改進單一代理人

> 使用者如何檢視／編輯代理人配置、單獨測試代理人，並加入新知識讓代理人更聰明。

---

## 概覽：三種代理人管理模式

```text
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  代理人管理（從 Agent Registry 進入）                            │
│                                                                 │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐       │
│  │  1. CONFIGURE  │  │  2. PLAYGROUND │  │  3. KNOWLEDGE  │       │
│  │               │  │               │  │               │       │
│  │ 檢視／編輯      │  │ 以自訂輸入測試 │  │ 加入訓練資料、 │       │
│  │ system prompt  │  │ 代理人，觀察其 │  │ 參考、例子，   │       │
│  │ tools、rubric  │  │ 推理與輸出     │  │ 以提升表現     │       │
│  │ thresholds、   │  │               │  │               │       │
│  │ relationships  │  │               │  │               │       │
│  └───────────────┘  └───────────────┘  └───────────────┘       │
│                                                                 │
│  無需 production。除非跑 Playground，否則不會產生成本。            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1. CONFIGURE — 檢視與編輯代理人設定

### 入口：Agent Registry → 點任何 agent → Configuration 分頁

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  代理人配置：DirectorAgent（#1）                              [Save] [Reset] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  分頁： [Configuration] [Playground] [Knowledge] [History] [Metrics]        │
│                                                                             │
├─── 身份（IDENTITY） ────────────────────────────────────────────────────────┤
│                                                                             │
│  名稱： [DirectorAgent_______________]                                       │
│  類別： [Above-the-Line ▼]                                                  │
│  描述：                                                                     │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ 負責創意願景；發出 shot intents、設定節奏、批准 takes。                │   │
│  │ 是整個 production 的創意權威。                                          │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
├─── SYSTEM PROMPT ───────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ You are an elite film director with deep knowledge of visual         │   │
│  │ storytelling, derived from Criterion commentary tracks, DGA          │   │
│  │ seminars, and MasterClass material from Scorsese, Lynch, and         │   │
│  │ Gerwig. Your role is to:                                             │   │
│  │                                                                      │   │
│  │ 1. Translate screenplay scenes into precise shot intents             │   │
│  │ 2. Define camera movement, composition, lighting mood                │   │
│  │ 3. Set pacing that matches genre expectations                        │   │
│  │ 4. Review generated shots against your creative vision               │   │
│  │ 5. Issue creative-intent diffs to other agents                       │   │
│  │                                                                      │   │
│  │ When generating shot intents, output JSON with:                      │   │
│  │ - camera_move, framing, subject, style, duration, mood               │   │
│  │ ...                                                                  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  Characters：2,847 │ [Expand editor] [Version history ▼]                    │
│                                                                             │
├─── 架構模式（ARCHITECTURE PATTERN） ─────────────────────────────────────────┤
│                                                                             │
│  Pattern： [Self-Refine ▼]                                                  │
│  選項：Self-Refine │ Reflexion │ ReAct │ Constitutional AI │                │
│        Multi-agent Debate │ RLAIF │ DSPy/OPRO │ Agentic Graph               │
│                                                                             │
│  Max iterations： [5___]（self-refine 迴圈上限）                             │
│  Temperature： [0.7___]                                                    │
│  Max tokens： [4096__]                                                     │
│                                                                             │
├─── 模型指派（MODEL ASSIGNMENT） ────────────────────────────────────────────┤
│                                                                             │
│  Primary LLM： [Gemini 2.5 Pro ▼]                                           │
│  Fallback LLM： [GPT-4o ▼]                                                  │
│  Generation tool： [Veo 3.1 ▼]                                              │
│  Fallback gen： [Kling 3.0 ▼]                                               │
│                                                                             │
├─── TOOLS ───────────────────────────────────────────────────────────────────┤
│                                                                             │
│  已啟用 tools：                                                             │
│  ☑ veo_3_1_api        — Video generation（Veo 3.1）                         │
│  ☑ runway_gen4_api    — Video generation（Runway Gen-4）                    │
│  ☑ sora_2_api         — Video generation（Sora 2）                          │
│  ☑ memory_recall      — 從 MemoryAgent 檢索                                  │
│  ☑ memory_store       — 儲存決策到 MemoryAgent                               │
│  ☑ clip_scorer        — 評估 CLIP-T 對齊                                    │
│  ☐ dalle_3_api        — Image generation（此 agent 停用）                    │
│  ☐ elevenlabs_api     — Voice（director 通常不需要）                         │
│                                                                             │
│  [+ Add custom tool]                                                        │
│                                                                             │
├─── 品質 Rubric（QUALITY RUBRIC） ───────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┬───────────┬─────────────────────────────────────┐     │
│  │ Metric          │ Threshold │ Description                         │     │
│  ├─────────────────┼───────────┼─────────────────────────────────────┤     │
│  │ clip_t          │ ≥ 0.32    │ Text-video alignment score          │     │
│  │ beat_coverage   │ = 100%    │ All story beats addressed           │     │
│  │ pacing_match    │ ≥ 0.70    │ Pacing fits genre prior             │     │
│  │ style_consistency│ ≥ 0.85   │ Visual style matches across shots   │     │
│  └─────────────────┴───────────┴─────────────────────────────────────┘     │
│  [+ Add metric]  [Edit thresholds]                                          │
│                                                                             │
├─── 關係（RELATIONSHIPS） ───────────────────────────────────────────────────┤
│                                                                             │
│  接受 critique 自：                                                          │
│  [ScreenwriterAgent ×] [EditorAgent ×] [AudienceSimAgent ×] [+ Add]         │
│                                                                             │
│  會評論（critique）誰：                                                      │
│  [EditorAgent ×] [DoPAgent ×] [ScreenwriterAgent ×] [ComposerAgent ×]       │
│  [+ Add]                                                                     │
│                                                                             │
├─── 成本控制（COST CONTROLS） ───────────────────────────────────────────────┤
│                                                                             │
│  Max cost per task：$[2.50]                                                  │
│  Max concurrent instances： [3___]                                           │
│  Timeout per task： [300__] seconds                                          │
│  Max retries on failure： [3___]                                             │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [Save Changes]  [Reset to Default]  [Export as JSON]  [Clone Agent]        │
│                                                                             │
│  ⚠ 變更只會套用到「未來」的 productions。正在運行的 productions 會沿用原設定。 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. PLAYGROUND — 單獨測試代理人

### 概念：沙盒內給代理人一個任務，觀察它如何推理與產出

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  代理人 Playground：DirectorAgent（#1）                           [Run ▶]    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  分頁： [Configuration] [Playground] [Knowledge] [History] [Metrics]        │
│                                                                             │
├─── 左側：輸入面板（INPUT） ─────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── 任務輸入（TASK INPUT） ────────────────────────────────────────┐      │
│  │                                                                   │      │
│  │  Task type： [Generate shot intent ▼]                             │      │
│  │  其他選項：Critique artifact │ Review cut │ Custom prompt          │      │
│  │                                                                   │      │
│  │  Scene context：                                                   │      │
│  │  ┌────────────────────────────────────────────────────────────┐   │      │
│  │  │ INT. COFFEE SHOP - NIGHT. Rain streaks the window. MAYA    │   │      │
│  │  │ sits alone, staring at her phone. The last text reads:     │   │      │
│  │  │ "I'm not coming." She sets the phone face-down.            │   │      │
│  │  └────────────────────────────────────────────────────────────┘   │      │
│  │                                                                   │      │
│  │  Reference images： [Drop zone]  ┌────┐ ┌────┐                    │      │
│  │                                  │ref1│ │ref2│                    │      │
│  │                                  └────┘ └────┘                    │      │
│  │                                                                   │      │
│  │  Mock critiques（模擬其他代理人回饋）：                              │      │
│  │  ☐ Add EditorAgent critique： [________________]                   │      │
│  │  ☐ Add AudienceSim feedback： [________________]                   │      │
│  │                                                                   │      │
│  │  Style lock / memory context：                                     │      │
│  │  ☐ "Neo-noir melancholic, Veo seed #4412"                          │      │
│  │  ☐ Custom： [________________________________]                     │      │
│  │                                                                   │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 運行設定（RUN SETTINGS） ───────────────────────────────────────┐      │
│  │  Model： [Gemini 2.5 Pro ▼]（覆寫 agent 預設）                     │      │
│  │  Generate video：☑ Yes（約 $2.50）  ☐ Text-only（免費／極低成本）   │      │
│  │  Self-refine：☑ Enabled  Max iterations： [3]                       │      │
│  │  Estimated cost：~$3.20                                              │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  [▶ Run Agent]   [▶ Run Text-Only (free)]   [Compare with Another Agent]    │
│                                                                             │
├─── 右側：輸出面板（OUTPUT） ────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── THINKING TRACE（逐步推理軌跡） ─────────────────────────────────┐       │
│  │                                                                  │       │
│  │  Step 1：分析 scene context                                      │       │
│  │  > "Night scene, emotional isolation, rain motif..."             │       │
│  │                                                                  │       │
│  │  Step 2：記憶檢索                                                │       │
│  │  > tool_call: memory.recall("visual style for Maya scenes")      │       │
│  │  > result: "Neo-noir, cool tones, shallow DoF"                   │       │
│  │                                                                  │       │
│  │  Step 3：生成 shot intent                                        │       │
│  │  > {                                                             │       │
│  │  >   "camera_move": "slow push-in from medium to close-up",     │       │
│  │  >   "framing": "off-center left, empty chair right",           │       │
│  │  >   "lighting": "practicals only, neon through rain",          │       │
│  │  >   "mood": "loneliness, resignation",                         │       │
│  │  >   "duration": "8s"                                           │       │
│  │  > }                                                             │       │
│  │                                                                  │       │
│  │  Step 4：生成影片                                                │       │
│  │  > tool_call: veo_3_1.generate(prompt="Slow push-in...")         │       │
│  │  > Status: generating... (38s)                                   │       │
│  │                                                                  │       │
│  │  Step 5：自我評估                                                │       │
│  │  > tool_call: clip_scorer.evaluate(video, prompt)                │       │
│  │  > CLIP-T: 0.35 ✓ (threshold: 0.32)                              │       │
│  │  > PASS — accepting on iteration 1                               │       │
│  │                                                                  │       │
│  └──────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│  ┌─── OUTPUT ────────────────────────────────────────────────────────┐      │
│  │  ┌─────────────────────────────────┐                              │      │
│  │  │ ▶ Generated video（8s）         │  CLIP-T: 0.35 ✓              │      │
│  │  │   [Play] [Download] [Compare]   │  Aesthetic: 6.4               │      │
│  │  └─────────────────────────────────┘  Style: 0.87                 │      │
│  │                                                                   │      │
│  │  Shot Intent JSON：                                                │      │
│  │  { "camera_move": "slow push-in...", ... }  [Copy] [Export]        │      │
│  │                                                                   │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 成本與效能（COST & PERFORMANCE） ───────────────────────────────┐      │
│  │  Total cost: $2.87 │ Time: 42s │ LLM tokens: 3,241                │      │
│  │  Iterations: 1/3 │ Tool calls: 3 │ Model: Gemini 2.5 Pro          │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  [Save as Test Case]  [Add to Knowledge]  [Run Again]  [Try Different Model]│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Playground 功能：

| 功能 | 目的 |
|---------|---------|
| **Text-only mode** | 不生成影片只看推理（$0–$0.01） |
| **Video mode** | 真實端到端執行並生成影片 |
| **Mock critiques** | 模擬其他代理人提供回饋時會發生甚麼 |
| **Compare** | 同一輸入用 2 個不同代理人／設定對照 |
| **A/B model test** | 同一代理人同一輸入，用不同 LLM 對比品質／成本 |
| **Save as test case** | 把此輸入／輸出收藏作回歸測試 |
| **Thinking trace** | 看每一步：推理、tool calls、決策 |
| **History** | 每次 run 都會保存，可重跑或長期對比 |

---

## 3. KNOWLEDGE — 透過新增知識改進代理人

### 概念：餵代理人新參考、例子、糾正與領域知識，令它表現更好

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  代理人 Knowledge：DirectorAgent（#1）                       [Save All Changes]│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  分頁： [Configuration] [Playground] [Knowledge] [History] [Metrics]        │
│                                                                             │
├─── 知識來源（代理人知道甚麼） ───────────────────────────────────────────────┤
│                                                                             │
│  ┌─── 1. 參考文件（REFERENCE DOCUMENTS） ─────────────────────────────┐      │
│  │  將文件嵌入到代理人的知識庫（RAG 檢索）                             │      │
│  │                                                                   │      │
│  │  ┌────────────────────────────────────────────────────────────┐   │      │
│  │  │ 📄 criterion_commentary_notes.md       │ 45KB │ Active  │   │      │
│  │  │ 📄 dga_seminar_transcripts.pdf         │ 120KB│ Active  │   │      │
│  │  │ 📄 scorsese_masterclass_notes.md       │ 32KB │ Active  │   │      │
│  │  │ 📄 shot_composition_guidelines.pdf     │ 18KB │ Active  │   │      │
│  │  │ 📄 genre_pacing_priors.json            │ 5KB  │ Active  │   │      │
│  │  │ 📄 my_custom_style_guide.md            │ 8KB  │ NEW ✨  │   │      │
│  │  └────────────────────────────────────────────────────────────┘   │      │
│  │                                                                   │      │
│  │  [+ Upload Document]  [+ Paste Text]  [+ Import from URL]         │      │
│  │                                                                   │      │
│  │  ℹ️ 這些文件會被 chunk 化、做 embedding，並存入 vector DB。           │      │
│  │    agent 在執行任務時會檢索相關 chunks。                            │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 2. Few-shot 例子（FEW-SHOT EXAMPLES） ────────────────────────┐      │
│  │  用 input/output 對教代理人「例子」                                 │      │
│  │                                                                   │      │
│  │  ┌────────────────────────────────────────────────────────────┐   │      │
│  │  │ Example 1："Romantic comedy - park scene"                  │   │      │
│  │  │ Input：Scene description + mood reference                   │   │      │
│  │  │ Expected output：Shot intent JSON（golden example）          │   │      │
│  │  │ [View] [Edit] [Delete]                                      │   │      │
│  │  ├────────────────────────────────────────────────────────────┤   │      │
│  │  │ Example 2："Action sequence - car chase"                   │   │      │
│  │  │ Input：Scene + storyboard panels                            │   │      │
│  │  │ Expected output：Shot intent with rapid cuts                │   │      │
│  │  │ [View] [Edit] [Delete]                                      │   │      │
│  │  ├────────────────────────────────────────────────────────────┤   │      │
│  │  │ Example 3："Horror - reveal scene"                          │   │      │
│  │  │ Input：Script excerpt + tension notes                       │   │      │
│  │  │ Expected output：Slow build, static camera, minimal cuts     │   │      │
│  │  │ [View] [Edit] [Delete]                                      │   │      │
│  │  └────────────────────────────────────────────────────────────┘   │      │
│  │                                                                   │      │
│  │  [+ Add Example Manually]  [+ Import from Playground Run]         │      │
│  │  [+ Generate Examples from Document]                               │      │
│  │                                                                   │      │
│  │  ℹ️ few-shot examples 會在 task type 匹配時注入 prompt。             │      │
│  │    例子越多，一致性通常越好。                                       │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 3. 糾正與回饋（CORRECTIONS & FEEDBACK） ─────────────────────┐      │
│  │  過往錯誤 + 正確做法                                               │      │
│  │                                                                   │      │
│  │  ┌────────────────────────────────────────────────────────────┐   │      │
│  │  │ Correction 1：（Production "Luna"，Shot 3）                 │   │      │
│  │  │ ❌ Agent did：Used handheld camera for intimate scene       │   │      │
│  │  │ ✓ Should have：Static tripod with slow push for intimacy    │   │      │
│  │  │ Why："Handheld implies urgency, not intimacy..."            │   │      │
│  │  │ Source：User feedback │ Date：2 days ago                     │   │      │
│  │  ├────────────────────────────────────────────────────────────┤   │      │
│  │  │ Correction 2：（Production "Spark"，Shot 7）                │   │      │
│  │  │ ❌ Agent did：16:9 framing for TikTok content               │   │      │
│  │  │ ✓ Should have：9:16 vertical for social-first delivery      │   │      │
│  │  │ Why："Always check platform target..."                      │   │      │
│  │  │ Source：Auto-detected from gate rejection │ Date：5d ago     │   │      │
│  │  └────────────────────────────────────────────────────────────┘   │      │
│  │                                                                   │      │
│  │  [+ Add Correction Manually]  [+ Import from Production Failures] │      │
│  │                                                                   │      │
│  │  ℹ️ corrections 會以 Reflexion-style episodic memory 儲存。          │      │
│  │    agent 會在類似任務先回想「之前錯過乜」。                         │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 4. 自訂規則（Constitutional Additions） ───────────────────────┐      │
│  │  代理人必須遵守的硬性規則（超越 system prompt）                     │      │
│  │                                                                   │      │
│  │  Rule 1："Never use Dutch angle unless genre is horror/thriller"  │      │
│  │  Rule 2："Always include at least one establishing shot per scene"│      │
│  │  Rule 3："Maximum shot duration: 12 seconds for social content"   │      │
│  │  Rule 4："When budget < 20%, prefer static camera (cheaper gen)"  │      │
│  │                                                                   │      │
│  │  [+ Add Rule]                                                     │      │
│  │                                                                   │      │
│  │  ℹ️ rules 會作為 constitutional constraints 注入。                   │      │
│  │    agent 於每次 self-refine 都會自檢是否違反。                       │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 5. 評估基準（EVALUATION BENCHMARKS） ─────────────────────────┐      │
│  │  用 test cases 衡量 knowledge 改進是否有效                          │      │
│  │                                                                   │      │
│  │  Benchmark suite：12 個 test cases                                 │      │
│  │  上次運行：2 天前 │ 分數：9/12 passing（75%）                      │      │
│  │  加完新知識後：[▶ Run Benchmark] 檢查是否變好                       │      │
│  │                                                                   │      │
│  │  ┌─────────────────────────────────────────────────────────────┐  │      │
│  │  │ Test │ Input              │ Expected    │ Last Result │ Pass │  │      │
│  │  ├──────┼────────────────────┼─────────────┼─────────────┼──────┤  │      │
│  │  │ 1    │ Rom-com park scene │ Wide→Medium │ Wide→Medium │ ✓    │  │      │
│  │  │ 2    │ Horror reveal      │ Static, slow│ Static, slow│ ✓    │  │      │
│  │  │ 3    │ Action chase       │ Fast cuts   │ Fast cuts   │ ✓    │  │      │
│  │  │ 4    │ TikTok 9:16        │ Vertical    │ Horizontal  │ ✗    │  │      │
│  │  │ ...  │                    │             │             │      │  │      │
│  │  └─────────────────────────────────────────────────────────────┘  │      │
│  │                                                                   │      │
│  │  [+ Add Test Case]  [+ Import from Playground]  [▶ Run All Tests] │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Runtime 時知識如何流入代理人

```text
生產期間 — 當 DirectorAgent 收到一個 task：

┌─────────────────────────────────────────────────────────────────┐
│  PROMPT 組裝（LLM 實際收到的內容）                                 │
│                                                                 │
│  1. SYSTEM PROMPT（由 Configuration 分頁提供）                     │
│     "You are an elite film director..."                         │
│                                                                 │
│  2. CUSTOM RULES（由 Knowledge > Rules 提供）                      │
│     "RULES YOU MUST FOLLOW:                                     │
│      - Never use Dutch angle unless horror/thriller             │
│      - Always include establishing shot per scene               │
│      - Max 12s shot duration for social content"                │
│                                                                 │
│  3. 相關知識（由參考文件做 RAG 檢索）                               │
│     Query："intimate scene, static camera, emotional"           │
│     Retrieved："From criterion_commentary_notes.md: ..."        │
│                                                                 │
│  4. 相關 few-shot examples（按 task type 匹配）                    │
│     "Example: For romance/intimacy scenes: ..."                 │
│                                                                 │
│  5. Corrections 記憶（Reflexion 檢索）                             │
│     "PAST MISTAKES TO AVOID: ..."                               │
│                                                                 │
│  6. 任務上下文（由當前 production 提供）                            │
│     "Scene: INT. COFFEE SHOP - NIGHT. Maya alone..."            │
│     "Critiques: EditorAgent says pacing too slow"               │
│                                                                 │
│  以上全部合併 → 作為單一 prompt 發送給 LLM → agent 回應             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 知識改進工作流

```text
使用者如何長期改進一個 agent：

1. 觀察問題（production 期間）
   →「DirectorAgent 成日喺安靜場面用 handheld」
   → 或：agent 重覆失敗同一個 gate criterion

2. 加入 correction（Knowledge 分頁）
   → 記錄：它做錯乜 + 應該點做 + 點解

3. 用 Playground 測試
   → 餵相似 scene → 而家會唔會改用 static camera？
   → 會：改進有效 ✓
   → 唔會：需要更強 rule 或更多 examples

4. 加入 few-shot example（如果 correction 唔夠）
   → 提供「黃金」input/output 對
   → 令 agent 學到：「遇到呢類場景，要咁做」

5. 跑 Benchmark
   → 對所有已儲存 test cases 測試
   → 確保冇 regression（冇破壞其他行為）
   → 分數由 9/12 → 11/12 ✓

6. 部署（自動 — 下一個 production 會用更新後設定）
   → 新知識會對之後所有 tasks 生效
   → 正在運行的 productions 不受影響（穩定）
```

---

## 後端：知識如何儲存

```python
# Agent knowledge storage (per agent, per project or global)

class AgentKnowledge:
    agent_id: int
    scope: "global" | "project"      # Global = all projects, or project-specific
    project_id: str | None
    
    # Reference documents (chunked + embedded in vector DB)
    documents: [
        { id, name, content, chunks: [embedding_ids], active: bool }
    ]
    
    # Few-shot examples (injected into prompt)
    examples: [
        { id, task_type, input_text, expected_output, tags: [] }
    ]
    
    # Corrections (Reflexion memory)
    corrections: [
        { id, context, wrong_behavior, correct_behavior, explanation,
          source: "user" | "auto_detected", production_id, created_at }
    ]
    
    # Constitutional rules (hard constraints)
    rules: [
        { id, rule_text, priority: int, active: bool }
    ]
    
    # Benchmark test cases
    benchmarks: [
        { id, input, expected_output_criteria, last_result, passing: bool }
    ]
```

---

## 範圍：Global Knowledge vs. Project Knowledge

```text
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  GLOBAL KNOWLEDGE（套用到所有 projects）                          │
│  ─────────────────                                              │
│  • 預設 system prompt                                            │
│  • 核心參考文件（Criterion notes、DGA seminars）                 │
│  • 通用規則（例如「非恐怖片唔好用 Dutch angle」）                 │
│  • 基礎 few-shot examples                                        │
│  • 管理者：平台 admin／agent 維護者                               │
│                                                                 │
│  PROJECT-SPECIFIC KNOWLEDGE（只套用到單一 project）               │
│  ─────────────────────────                                      │
│  • 品牌專屬風格指引                                               │
│  • project 專屬 corrections（「呢個 project 一定要…」）             │
│  • 符合 project 類型／語氣的 examples                              │
│  • project 專屬 rules（例如「budget mode 優先 static camera」）     │
│  • 管理者：project owner／editor                                  │
│                                                                 │
│  Runtime（合併）：                                               │
│  ─────────────────────                                          │
│  agent 會收到：Global knowledge + Project knowledge              │
│  發生衝突時，Project knowledge 會覆寫 Global                      │
│  （例如 project rule 指定「一定直向」，會覆寫預設）                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 自動學習：由 Production 歷史提案知識改進

系統亦可自動建議 knowledge improvements：

```text
自動偵測：
═══════════

1. 模式：同一個 agent 跨 productions 重覆失敗同一個 criterion 3+ 次
   → 系統建議：「要唔要加一條關於 [偵測到模式] 嘅 rule？」
   → 使用者檢視後接受或忽略

2. 模式：使用者經常以相同方式手動覆寫 agent 輸出
   → 系統建議：「要唔要把你嘅覆寫模式變成一條 correction？」
   → 例如使用者總係拒絕近景用超廣角

3. 模式：某個 agent 輸出經常被同一種批評
   → 系統建議：「要唔要把呢個變成 few-shot example（負例）？」
   → 例如 EditorAgent 經常指出「開場節奏太慢」

4. 模式：gate rejection 反覆出現同一類回饋
   → 系統自動建立 correction entries
   → 標記為「auto-detected，待使用者審核」

┌─── 建議改進（通知） ─────────────────────────────────────────────┐
│                                                                 │
│  🧠 DirectorAgent 有 3 個知識建議：                              │
│                                                                 │
│  1.「代理人用 16:9 做 TikTok 內容 4 次 — 要唔要加 rule？」         │
│     [Accept: Add Rule] [Dismiss] [View instances]               │
│                                                                 │
│  2.「EditorAgent 批評 pacing 6 次 — 要唔要加 example？」          │
│     [Accept: Create Example] [Dismiss] [View critiques]         │
│                                                                 │
│  3.「夜景 CLIP-T 經常偏低 — 要唔要加參考文件？」                   │
│     [Accept: Upload night-scene guide] [Dismiss]                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 總結：三種代理人管理模式

| 模式 | 目的 | 成本 | 何時用 |
|------|---------|------|-------------|
| **Configure** | 檢視／編輯 prompt、tools、rubric、關係、模型 | $0 | 為你的 project 設定 agents |
| **Playground** | 單獨測試 agent（自訂輸入） | 每次 $0–$3 | 除錯、實驗、驗證變更 |
| **Knowledge** | 加入文件、例子、糾正、規則 | $0（只存儲） | 基於 production 經驗持續改進 |

三者配合：

```text
1. production 見到問題 →
2. Knowledge 加 correction →
3. Playground 測試修正 →
4. Benchmark 驗證 →
5. 下一次 production agent 更聰明
```
