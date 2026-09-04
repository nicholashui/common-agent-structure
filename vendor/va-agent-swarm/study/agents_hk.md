*Thinking...*

>  I need to translate this entire document into Traditional Chinese while keeping all the formatting, code blocks, links, and structure intact. Let me work through this systematically to ensure accuracy. I need to translate this entire markdown document into Traditional Chinese while keeping the structure intact. I'll preserve code blocks, URLs, technical product names, and all formatting, only translating the actual content and comments where appropriate.

# AI 代理人員角色表 — 分類拆分版

> 取自 [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) 之精煉內容。
> 本檔案以 `agents_old.md` 的版面配置為主要結構。
> 較新版 `agents.md` 中缺失的工作流程支援內容已合併回來,並以相同的分類表格樣式作為額外章節呈現。

---

## 目錄

1. [線上製作層級代理 (1–5)](#1-線上製作層級代理)
2. [攝影與燈光代理 (6–8)](#2-攝影與燈光代理)
3. [剪輯與調色代理 (9–18)](#3-剪輯與調色代理)
4. [聲音與音樂代理 (19–22)](#4-聲音與音樂代理)
5. [表演與編舞代理 (23–27)](#5-表演與編舞代理)
6. [發行與行銷代理 (28–31)](#6-發行與行銷代理)
7. [教育與領域專家代理 (32–45)](#7-教育與領域專家代理)
8. [AI 時代專家代理 (46–52)](#8-ai-時代專家代理)
9. [專家元代理 (53–80)](#9-專家元代理)
10. [工作流程支援代理 (81–114)](#10-工作流程支援代理)
11. [AI 代理的共通結構](#11-ai-代理的共通結構)
    - [11.1 架構圖](#111-架構圖)
    - [11.2 組件參考表](#112-組件參考表)
12. [參考文獻](#12-參考文獻)

---

## 1. 線上製作層級代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **DirectorAgent (導演)** | 掌握願景;發出鏡頭意圖、設定節奏、批准拍攝 | Criterion 評論;IMDb 前 250 大導演訪談;DGA 研討會;MasterClass(Scorsese/Lynch/Gerwig) | 鏡頭意圖貼合度(CLIP-T ≥0.32);故事節拍覆蓋率 100%;節奏曲線符合類型先驗 | 在盲測配對中(Arena)對 DGA 剪輯版勝率 ≥55% | ScreenwriterAgent、EditorAgent、AudienceSim — JSON 批評匯流排 | EditorAgent、DoPAgent、ScreenwriterAgent、ComposerAgent | Sora 2 API、Veo 3.1 (Gemini API)、Runway Gen-4、Kling 3.0;透過 MCP 連接 DaVinci Resolve | Self-Refine + LLM-as-Judge(評分量表:類型先驗) |
| 2 | **ProducerAgent / EP (製片/執行製片)** | 預算、時程、人員聘用、交付;核准階段關卡 | PGA Producers Mark;Variety/Deadline 預算外流資料;LineProducer Excel 資料集 | 準時交付率;預算差異 <±5%;人才滿意度(RLHF) | 以 PGA 時程的 0.6 倍成本完成,CSAT 相等 | 所有下游代理(升級);綠燈通過時需 HiTL 關卡 | DirectorAgent(範圍蔓延)、AllAgents(資源消耗) | Google Sheets API、Airtable、Temporal/Airflow 編排、Stripe 計費 | Agentic Graph(LangGraph DAG)+ ReAct 用於工具呼叫 |
| 3 | **ScreenwriterAgent (編劇)** | 大綱 → 劇本;對白;結構 | Black List 劇本;WGA 資料庫;McKee《故事》;Truby;Kaufman/Sorkin 訪談 | Save-the-Cat 節拍通過;對白獨特性(embedding 距離 ≥τ);改寫差異 | 在盲讀中(模擬 WGA 評審)對 Black List Top-10 勝率 ≥50% | DirectorAgent、DramaturgAgent、StoryEditorAgent — Reflexion 迴圈 | DirectorAgent(logline)、DialogueAgent、ConsistencyAgent | Fountain/FDX 格式驗證器;語意嵌入模型(text-embedding-3-large) | Reflexion (Shinn 2023) — 具情境式記憶的口語化強化學習 |
| 4 | **ShowrunnerAgent (劇集統籌)** | 跨集弧線、編劇室編排 | WGA showrunner 訓練;Sopranos/BB 編劇室逐字稿;Mike Schur 教材 | 弧線連貫性分數;角色線完成度;基調變異在範圍內 | 10 集間 Series Bible 覆蓋率 ≥99%(人類約 95%) | Network-Notes Agent、AudienceSim、與 ScreenwriterAgent 多代理辯論 | ScreenwriterAgent(弧線)、CastingAgent、DirectorAgent(基調) | 長上下文 LLM (Gemini 2.5 Pro 1M)、用於 bible 搜尋的向量資料庫(Pinecone/Weaviate) | 多代理辯論 (Du 2023) + MemoryAgent 檢索 |
| 5 | **CastingAgent (選角)** | 聲音 + 形象選擇;試鏡模擬 | CSA Artios 檔案;SAG-AFTRA AI 附約;經同意之配音員資料集 | 角色聲音契合度(觀眾偏好);同意合規 100% | 在盲測偏好中勝過 CSA 選角;週縮短為小時 | DirectorAgent、ShowrunnerAgent、Legal/ConsentAgent | VoiceCloneAgent(形象)、AvatarDesignAgent | ElevenLabs v3 聲音庫、HeyGen 虛擬化身目錄、語者嵌入相似度(Resemblyzer) | LLM-as-Judge(對聲音樣本進行配對偏好) |

---

## 2. 攝影與燈光代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 6 | **CinematographerAgent (DoP / 攝影指導)** | 鏡頭、燈光、構圖、視覺風格 | ASC Magazine 1980 年至今;Deakins 論壇;Brown《電影攝影:理論與實務》;坎城鏡頭庫 | 三分法/引導線分數;曝光直方圖在分區內;色溫一致性 | 在盲測美學偏好中勝過 ASC 同儕評選作品 | DirectorAgent、ColoristAgent、VFXSupAgent | DirectorAgent(視覺意圖)、GafferAgent、ColoristAgent | Veo 3.1(攝影機路徑控制)、Runway Gen-4 (ControlNet guides)、ACES 色彩管線工具 | Self-Refine + 基於 CLIP 的美學評分 |
| 7 | **CameraOperatorAgent (攝影機操作)** | 依 DoP 意圖執行構圖/對焦/移動 | SOC 檔案;Steadicam 工作坊影片;對焦遙測 | 畫面穩定度、對焦命中率、動作置中 | 對焦準確率 >99%,SOC 基準約 97% | CinematographerAgent(每次拍攝回饋) | CinematographerAgent(不切實際的要求) | Runway 攝影機路徑預設;Kling 動作控制 API;虛擬攝影機機架(Unreal MV) | ReAct (Yao 2022) — 推理構圖後呼叫渲染器 |
| 8 | **DronePilotAgent (空拍機駕駛)** | 空中攝影(模擬或實拍) | Philip Bloom 教學;FAA Part 107;SkyPixel 獲獎作品 | 路徑平滑度;地理圍欄合規 100%;地平線穩定 | 在 10 倍出勤率下達競賽級平滑度;零違規 | DoPAgent、SafetyAgent | DoPAgent(不可能的高度)、SafetyAgent(風險) | DJI Waypoint SDK(模擬)、Veo 3.1 空拍模式、地理圍欄資料庫(AirMap API) | Constitutional AI(安全章程:將 FAA 規則作為原則) |

---

## 3. 剪輯與調色代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 9 | **EditorAgent (剪輯師)** | 組裝粗剪;節奏;素材選擇 | Murch《眨眼之間》;ACE Eddie 獎得主;日舞影展剪輯實驗室 | 節奏曲線符合類型;Murch「六法則」分數;AVD ≥ 目標 | 對 ACE 認證剪輯的配對勝率 ≥55% | DirectorAgent、AudienceSim、ComposerAgent(音樂剪接同步) | DirectorAgent(過度覆蓋)、DoPAgent(無法使用的素材) | 透過 MCP bridge 連 DaVinci Resolve;FFmpeg;EDL/XML 時間軸 API | Self-Refine(評分量表:Murch 六法則) |
| 10 | **ColoristAgent (調色師)** | 最終調色;風格一致性 | ICA 資料集;Sonnenfeld 工作階段;HPA 獎調色作品 | ΔE 漂移 <2;膚色 IT8 對齊;情緒向量匹配 | 在盲測偏好中勝過初級調色師;在 ΔE 內與資深匹配 | DoPAgent、DirectorAgent、AccessibilityAgent(對比) | DoPAgent(混合色溫)、VFXAgent(合成色彩不匹配) | DaVinci Resolve 調色 API (MCP);ACES/OCIO 管線;LUT 產生器 | Self-Refine + 工具使用(色度計驗證) |
| 11 | **VFXSupervisorAgent (視覺特效監督)** | 規劃 + 監督 VFX 管線 | VES 獎;SIGGRAPH 論文;Weta/DNEG 講座;Foundry 訓練 | 鏡頭完成率;合成錯誤像素計數;對 plate 的 CLIP-T | Weta 等級 QC 通過率,在較短時間內達成 | DirectorAgent、DoPAgent、ConsistencyAgent | AIGeneratorAgent(瑕疵)、CompositorAgent | 透過 MCP bridge 連 Nuke;Runway Gen-4 Aleph(影片轉影片);ComfyUI | Agentic Graph(每鏡頭扇出)+ LLM-as-Judge (QC 評分量表) |
| 12 | **AnimatorAgent (2D/3D 動畫師)** | 角色動作、重量、時機 | Williams《動畫師生存手冊》;Annie 獎;Pixar SparkShorts;Blaise 課程 | 12 法則分數;弧線平滑度;對嘴音素準確率 | 在 Annie 評分量表勝過初級;以 5 倍產出與資深相等 | DirectorAgent、LipSyncAgent | StoryboardAgent(不可能的動作)、DirectorAgent(時機) | Kling 3.0 動作控制;Blender Python API;Cascadeur 物理;Sync.so 對嘴 | Self-Refine(評分量表:12 法則檢查清單) |
| 13 | **MotionGraphicsAgent (動態圖像)** | 動態字體、字幕條、資訊圖表 | Motionographer;School of Motion;AICP Next 獎 | 字體層級;品牌合規;縮圖可讀性 | 在速度與符合品牌準確性上贏得代理商比稿 | BrandManagerAgent、AccessibilityAgent(對比) | CopywriterAgent(冗長)、EditorAgent(時機) | 透過 MCP/ExtendScript 連 After Effects;Lottie 匯出;Rive;品牌資源 CDN | ReAct — 對品牌準則推理後渲染 |
| 14 | **StoryboardAgent (分鏡師)** | 劇本 → 鏡頭分鏡 | 《Framed Ink》(Mateu-Mestre);Pixar story-trust;Despretz 分鏡 | 鏡頭語言貼合度;覆蓋完整性;舞台清晰度 | 在每頁數分鐘內達 Pixar story-trust 通過率 | DirectorAgent、DoPAgent | ScriptwriterAgent(無法拍攝)、DirectorAgent(舞台) | DALL-E 3 / Midjourney API;分鏡版型範本;Fountain 解析器 | Self-Refine(導演回饋迴圈) |
| 15 | **ConceptArtistAgent (概念設計師)** | 前期世界/角色設計 | ArtStation 頂尖作品;McCaig/Church 作品集;工作室美術聖經 | 風格聖經遵循;剪影可讀性;設計連貫性 | 在迭代速度上贏得美術指導比稿 | DirectorAgent、ProductionDesignAgent | StoryboardAgent(設計偏移) | Midjourney v7;Stable Diffusion ControlNet;Photoshop 生成式填色 (API) | Self-Refine + 風格參考 CLIP 評分 |
| 16 | **ProductionDesignAgent (美術指導)** | 場景、地點、世界觀 | ADG 獎;AMPAS 提交;Beachler/Carter 講座 | 時代準確性;色盤連貫;搭建可行性 | 在時代研究深度上贏得 ADG 盲測比較 | DirectorAgent、DoPAgent | ConceptArtistAgent(風格斷裂)、CostumeAgent | Unreal Engine(虛擬勘景);Veo 3.1 地點生成;檔案影像搜尋 API | Reflexion(將時代研究修正存入記憶) |
| 17 | **CostumeDesignAgent (服裝設計)** | 透過服裝塑造角色 | V&A 檔案;CDG 專著;Ruth E. Carter 大師班 | 時代/時尚準確;剪影辨識;色盤契合 | 在時代準確性基準上勝過 CDG 初級設計師 | DirectorAgent、ProductionDesignAgent | MUAAgent(連戲斷裂) | 時尚史向量 DB(V&A/Met API);服裝草圖影像生成;色盤工具 | Self-Refine(時代準確性評分量表) |
| 18 | **MUAAgent (化妝/髮型/特效化妝)** | 演員臉部/頭髮;特殊化妝 | IATSE 706 資料;Kazu Hiro 工作室參考 | 跨鏡次連戲雜湊;膚色擬真 (FID) | 連戲斷裂率 <0.5%(人類約 2%) | DoPAgent、ContinuityAgent | CostumeAgent(色盤衝突) | 臉部地標偵測;感知雜湊比較;Kling 臉部一致性模式 | Constitutional AI(章程:連戲規則) |

---

## 4. 聲音與音樂代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 19 | **SoundDesignAgent (音效設計)** | 環境音、Foley、SFX | BBC SFX 音效庫;MPSE Golden Reel;Burtt/Lievsay 筆記 | 頻譜多樣性;同步 ≤±1 影格;響度 -23 LUFS | 在恐怖/科幻配對勝過 MPSE | DirectorAgent、MixerAgent | EditorAgent(FX 衝突)、ComposerAgent(遮蔽) | ElevenLabs Sound FX API;Freesound;FFmpeg 頻譜分析;Dolby.io 響度 API | ReAct(搜尋 SFX 庫 → 驗證同步 → 混音) |
| 20 | **ComposerAgent (作曲)** | 原創配樂 | MAESTRO + 電影配樂資料集;ASCAP/BMI;Zimmer/Hildur 工作階段 | 樂段對情緒對齊(效價/喚醒度回歸);主題反覆 | 在情感契合的盲測中勝過在職作曲家 | DirectorAgent、EditorAgent(音樂剪接) | EditorAgent(剪輯打斷樂段)、SoundDesignAgent(遮蔽) | Udio/Suno 音樂生成 API;MIDI 工具鏈;音軌分離 (Demucs);響度錶 | Self-Refine + 情緒弧驗證(生物訊號代理) |
| 21 | **VoiceOverAgent (配音)** | 旁白、角色配音、廣告配音 | SOVAS 作品集;經同意之配音資料集;Wolfson/Cashman 指導 | 韻律匹配;發音 100%;情緒標籤匹配 | 在盲測偏好中勝過初級配音;在情感上與資深相等 | DirectorAgent、BrandAgent | ScriptwriterAgent(無法朗讀的措辭) | ElevenLabs v3 TTS + 聲音複製;Resemble.AI;發音詞典 API | LLM-as-Judge(MOS 評分量表) |
| 22 | **SoundMixerAgent (重錄混音)** | 最終混音;交付規格(5.1/Atmos) | CAS 獎;Atmos 規格;廣播響度標準 | LUFS 目標;STOI ≥0.85;規格交付通過 | 首次通過 CAS 規格,無需重做 | EditorAgent、SoundDesignAgent、AccessibilityAgent | SoundDesignAgent(過度設計)、ComposerAgent(音量) | Dolby Atmos Renderer API;LUFS/響度量測工具;DaVinci Fairlight MCP | Constitutional AI(章程:廣播規格規則) |

---

## 5. 表演與編舞代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 23 | **ChoreographyAgent (編舞)** | 動作設計(MV、舞蹈挑戰) | 艾美獎編舞提交;Goebel/Moore 作品集;舞蹈記譜資料集 | 節拍同步準確度;安全約束;病毒模式對齊 | 在盲測偏好中勝過編舞家草稿 | DirectorAgent、MVDirectorAgent | DirectorAgent(對鏡頭不友善的編排) | Kling 3.0 動作控制(參考影片);Cascadeur;節拍偵測 (librosa) | Self-Refine(評分量表:節拍同步 + 安全) |
| 24 | **MusicVideoDirectorAgent (MV 導演)** | 歌曲視覺概念 | DirectorsLibrary;UKMVA/MTV VMA 得獎作品;Hype Williams/Spike Jonze | 剪輯節奏同步;視覺風格連貫;藝人簡介契合 | 在唱片公司盲測偏好中勝過商業 MV 入圍名單 | LabelA&RAgent、ArtistAgent | EditorAgent(踩拍剪輯)、DoPAgent | Runway Gen-4(風格鎖定生成);Veo 3.1;情緒板工具 (Are.na API) | 多代理辯論(與 DirectorAgent + EditorAgent) |
| 25 | **ComedyWriterAgent (喜劇編劇)** | 短劇、模仿、爆紅迷因撰寫 | UCB/Groundlings 手冊;SNL 逐字稿;Schur/Fey 教材 | 笑點密度;冷開場勾子強度;預測每分鐘笑聲 | 在冷讀勝過 UCB 桌讀勝率 | AudienceSim、ShowrunnerAgent | ScriptwriterAgent(無笑點)、SocialStrategistAgent(脫離趨勢) | 觀眾笑聲預測模型;熱門音訊 API (TikTok Creative Center) | Reflexion(將觀眾回饋存入情境式記憶) |
| 26 | **TalentAgent (鏡頭前演員)** | AI 渲染表演 | 方法演技逐字稿;經同意之演員表演資料集 | 情緒目標匹配;魅力分數(觀眾代理) | 留存率與該族群頂尖創作者相當 | DirectorAgent、CastingAgent | DirectorAgent(不可能的走位) | HeyGen Avatar IV;Synthesia 個人化身;情緒偵測模型 (AffectNet) | Self-Refine + 情緒回歸驗證 |
| 27 | **UGCCreatorAgent (UGC 創作者)** | 以創作者口吻製作的真實感廣告 | TikTok Creative Center;Alix-Earle 風格基準(風格非身分) | 勾子率 ≥30%;「腳本化」偵測 < 閾值 | 以付費創作者 0.1 倍成本超越平均 ROAS | PerformanceMarketerAgent、BrandAgent | PerformanceMarketerAgent(目標受眾錯誤) | Veo 3.1(直式 9:16);ElevenLabs 配音;CapCut API;TikTok Ads Manager | RLAIF(獎勵來自 ROAS 訊號) |

---

## 6. 發行與行銷代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 28 | **SocialMediaStrategistAgent (社群媒體策略)** | 平台原生發行、時機、趨勢 | TikTok Creator Portal;Meta Marketing Science;Tubular/Sensor Tower | 預測對實際觸及誤差;趨勢時機延遲 <2 小時 | 在 30 日觸及提升上勝過代理商社群主管 | AnalystAgent、BrandAgent | CopywriterAgent(離平台調性)、EditorAgent(錯誤比例) | Meta Graph API;TikTok Content Posting API;Buffer/Hootsuite API;Sensor Tower 資料 | ReAct(趨勢搜尋 → 排程 → 發文) |
| 29 | **CopywriterAgent (文案)** | 腳本、字幕、勾子、標題 | D&AD/One Show;《廣告教皇大衛奧格威》;Wiebe Copyhackers | 閱讀年級;勾子好奇心分數;品牌語調餘弦 ≥0.85 | 在廣告 brief 上贏得 D&AD 風格盲測偏好 | BrandAgent、PerformanceMarketerAgent | ScriptwriterAgent(冗長)、VOArtist(無法朗讀) | 品牌語調嵌入模型;Hemingway 可讀性 API;A/B 標題工具 | Self-Refine(評分量表:品牌語調相似度評分器) |
| 30 | **CreativeDirectorAgent (創意總監)** | 活動概念;跨領域品味 | 坎城獅子大獎;D&AD Pencils;代理商案例研究 | 概念獨特性(嵌入新穎度);獎項評分量表預測分數 | 對人類入圍名單在坎城評審模擬器中贏得金獎 | ClientAgent、BrandAgent | CopywriterAgent、ArtDirectorAgent | 活動檔案搜尋(坎城獅子 API);Midjourney 概念視覺化;Figma API | 多代理辯論(IdeationAgent + NoveltyAgent 小組) |
| 31 | **PerformanceMarketerAgent (成效行銷)** | 為 ROAS 最佳化廣告 | Meta Blueprint;TikTok Ads Academy;MMM 文獻 | 對照組 ROAS 提升;顯著性 ≥95% | 在 30 日 ROAS 勝過資深媒體採購 | AnalystAgent、FinanceAgent | UGCAgent(低勾子)、CopywriterAgent(弱 CTA) | Meta Ads API;TikTok Ads API;Google Ads API;Bayesian AB 測試函式庫 | RLAIF(獎勵 = 來自廣告平台的 ROAS 提升訊號) |

---

## 7. 教育與領域專家代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 32 | **InstructionalDesignAgent (教學設計)** | 學習目標 → 腳本 → 評量 | ATD 知識體系;Cathy Moore《動作對應》;Dirksen《設計給學習者》 | Bloom 層級對應;完成率 ≥70%;Kirkpatrick L2 測驗 ≥80% | 在留存率 RCT 中勝過 ATD 認證教學設計師 | SMEAgent、AccessibilityAgent | ScriptwriterAgent(無目標)、AnimatorAgent(過度裝飾) | LMS API (SCORM/xAPI);測驗生成;Bloom 分類分類器 | Self-Refine(評分量表:Bloom/Kirkpatrick) |
| 33 | **SMEAgent (主題專家)** | 目標領域之領域準確性 | 同儕審查期刊;認證課綱 (CFA、USMLE、AWS);專家訪談 | 引用密度;基準考試通過;幻覺率 ≤0.5% | 通過與人類專業相同之認證 | FactCheckerAgent、其他 SMEAgents(辯論) | ScriptwriterAgent(不準確)、MotionGraphicsAgent(誤標) | PubMed/arXiv/JSTOR 搜尋 API;考題題庫;對認證資料集的 RAG | 多代理辯論 + RAG 檢索 |
| 34 | **FactCheckerAgent (事實查核)** | 為每個陳述評估來源等級 | 《紐約客》查核手冊;IFCN;Snopes/PolitiFact | 每項主張的來源等級(一手 > 二手);跨來源 ≥2 | 比普立茲級媒體更低的更正率 | SMEAgent、StandardsEditorAgent | ScriptwriterAgent(無來源)、JournalistAgent | 網路搜尋 API (Brave/Google);主張擷取 NER;來源品質分類器 | ReAct(擷取主張 → 搜尋 → 驗證 → 評等) |
| 35 | **MedicalIllustratorAgent (醫學插畫)** | 解剖與術式視覺 | Netter 解剖圖譜;AMI/CMI 課綱;Anatomage | 解剖準確性(偵測模型);AMI 評分量表 | CMI 同儕在盲審中投票 ≥通過 | SMEAgent(醫師)、AccessibilityAgent | AnimatorAgent(錯誤解剖)、CopywriterAgent(誤用術語) | Anatomage 3D API;DALL-E 3(醫學提示模式);解剖偵測模型 | Self-Refine(評分量表:AMI 計分準則) |
| 36 | **JournalistAgent (記者)** | 報導 + 倫理框架 | 普立茲/duPont/Peabody 得獎作;SPJ 倫理;Poynter | 來源多樣性;具名比率;倫理檢查清單通過 | 比編輯室更低的更正率 + 更快發稿 | FactCheckerAgent、LegalAgent、StandardsEditorAgent | FactCheckerAgent、ScriptwriterAgent | 網路研究工具;AP Stylebook API;訪談轉錄 (Otter);SPJ 評分量表 | Reflexion(倫理檢查清單作為口語回饋) |
| 37 | **ComplianceAgent (Legal / 法務合規)** | FTC、HIPAA、GDPR、IP、AI 形象授權清查 | 律師 CLE;FTC 準則;歐盟 AI 法;GDPR/CCPA;SAG-AFTRA AI 附約 | 100% 規則覆蓋;零發佈後下架 | 比中位數媒體法律顧問更低的法律風險 | 所有代理(必須通過關卡);新議題交人類律師 | 所有代理(阻斷關卡) | 法律規則 DB(向量化法規);同意文件儲存;C2PA 驗證函式庫 | Constitutional AI(章程 = 編譯之法規條文) |
| 38 | **FinanceAgent (財經)** | 準確之市場/財報/代幣資訊 | CFA 課綱;SEC 行銷規則;Bloomberg/Refinitiv feeds | 數字準確性 100%;SEC 合規 | 通過 CFA L3;比分析師更低的撤回率 | SMEAgent(經濟)、ComplianceAgent | ScriptwriterAgent(數字漂移)、MotionGraphicsAgent(圖表比例) | Bloomberg API;EDGAR/SEC 文件;金融計算驗證器 | ReAct(擷取資料 → 驗證 → 撰寫) |
| 39 | **FoodStylistAgent (食物造型)** | 鏡頭就緒之食物、食譜真實性 | James Beard 檔案;Spungen 技法;IACP 資料集 | 視覺食慾吸引力(美學迴歸器);食譜準確性 | 在盲測偏好中勝過編輯食物造型師 | DoPAgent(燈光)、DirectorAgent | ScriptwriterAgent(不可能的食譜) | DALL-E 3 / Midjourney(美食攝影生成);食譜步驟解析器;美學評分模型 | Self-Refine(美學迴歸器作為評分量表) |
| 40 | **TravelCineAgent (旅遊攝影)** | 目的地電影攝影 | Brandon Li/Burkard 作品集;國家地理風格指南;Banff 影展 | 建立鏡頭多樣性;地點情緒匹配 | 以 0.1 倍出勤成本贏得 T+L 偏好 | DirectorAgent、DronePilotAgent | DronePilotAgent(禁航區) | Veo 3.1(地點生成);Google Earth Studio;AirMap 地理圍欄;Unsplash API | Self-Refine + 地理圍欄安全驗證器 |
| 41 | **ChildrensAuthorAgent (兒童作家)** | 年齡合適之故事 + 安全 | Caldecott/Geisel 得獎作;Mo Willems/Donaldson;ECE 文學 | Lexile 等級匹配;Common-Sense-Media 安全通過;押韻分數 | 勝過 Caldecott 評分量表預測分數 | ChildSafetyAgent、ParentSimAgent | AnimatorAgent(嚇人)、VOAgent(年齡基調錯誤) | Lexile 分析器 API;Common Sense Media 評分量表;押韻/格律工具 (CMU 發音詞典) | Constitutional AI(兒童安全章程) |
| 42 | **AudiobookNarratorAgent (有聲書旁白)** | 持續角色 + 旁白 | Audie 獎;AudioFile Earphones;經同意之旁白資料集 | 嗓音耐力(60 分鐘無漂移);角色區別(嵌入距離) | 以較短錄音室時間贏得 AudioFile 盲評 | DirectorAgent、AuthorAgent | VOArtistAgent(過度演繹) | ElevenLabs v3 長篇 TTS;Projects API(章節);語音一致性監測 | Self-Refine(漂移偵測作為回饋迴圈) |
| 43 | **SignLanguageInterpreterAgent (手語翻譯)** | 準確之 ASL/BSL 翻譯 | RID NIC 課綱;NAD 資料集;聾人社群同意資料 | 手語準確性(聾人審閱投票);臉部文法標記 | 大規模下贏得 NAD 審閱盲測偏好 | DeafCommunityReviewAgent (HiTL)、LinguistAgent | VoiceCloneAgent(無字幕)、AccessibilityAgent | 手語化身渲染 (SignAll);MediaPipe 姿勢估計;臉部動作單元偵測器 | RLAIF(獎勵來自聾人社群審閱小組) |
| 44 | **LocalizationQAAgent (在地化 QA / 語言學家)** | 翻譯 + 文化契合 | LISA QA 模型;MQM 錯誤類型學;ATA 認證準備 | MQM 錯誤/千字;文化標記計數 | 在 MQM 上以 10 倍速度勝過 LSP 人類 QA | NativeReviewerAgent、BrandAgent | VoiceCloneAgent(發音)、DubbingAgent | DeepL/Google Translate API;MQM 錯誤標註器;術語管理 (memoQ API) | Self-Refine(評分量表:MQM 計分框架) |
| 45 | **RealEstatePhotoAgent / 3D Scan (房地產攝影/3D 掃描)** | 寬廣室內;Matterport 掃描 | Mike Kelley 教學;APALA 參考 | 垂直線筆直;HDR 堆疊;覆蓋率 | 房源 CTR 相對於人類拍攝基準的提升 | DoPAgent、DronePilotAgent | DronePilotAgent(違法高度) | Matterport SDK;HDR 處理 (Luminance HDR);鏡頭校正工具;Veo 3.1 | ReAct(評估空間 → 生成視角 → 驗證幾何) |

---

## 8. AI 時代專家代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 46 | **PromptEngineerAgent / GeneratorOperator (提示工程師/生成器操作員)** | 撰寫提示;操控 Sora/Veo/Runway/Kling | Karen X. Cheng/Trillo 公開作品集;r/aivideo;Runway AIFF 評審筆記 | 提示→輸出 CLIP-T;接受所需迭代次數;種子可重現性 | 在 ≤3 次迭代內達成目標鏡頭(人類平均 10 次) | DirectorAgent、AIQAAgent | AIQAAgent(重抽預算)、ConsistencyAgent | Sora 2 API、Veo 3.1、Runway Gen-4/Aleph、Kling 3.0;種子/參數登錄 | DSPy / OPRO 提示優化 (Yang 2023) |
| 47 | **AvatarDesignAgent (虛擬化身設計)** | 合成主持人身份 | Synthesia/HeyGen 設計文件;Hany Farid 深偽偵測;C2PA 規格 | 跨鏡頭身份雜湊一致性;同意鏈;C2PA 簽署 | 大規模下 C2PA 可驗證 + Partnership-on-AI 完全通過 | ComplianceAgent(同意)、DeepfakeDetectionAgent | VoiceCloneAgent(偏離形象)、LipSyncAgent | HeyGen Avatar IV API;Synthesia API;C2PA 簽署函式庫 (c2patool);臉部嵌入模型 | Constitutional AI(同意 + 身份章程) |
| 48 | **VoiceCloneAgent / LipSyncSpecialist (聲音複製/對嘴專家)** | 聲音複製 + 對嘴 | ElevenLabs 安全文件;Wav2Lip/Sync.so;Baxter 對嘴參考 | 語音 MOS ≥4.2;音素-視位錯誤 <40ms;同意已驗證 | 在盲測 MOS 中勝過專業 ADR | ComplianceAgent(同意)、AnimatorAgent(對嘴黃金) | AvatarDesignAgent(臉部閃爍)、DubbingAgent | ElevenLabs v3 複製 API;Sync.so 對嘴;Wav2Lip;同意文件驗證 | Self-Refine + MOS 評分模型作為評審 |
| 49 | **AIQAConsistencyAgent (AI QA 一致性)** | 偵測影格漂移、手/臉瑕疵、身份斷裂 | VBench;EvalCrafter;FVD 文獻;MPC/Weta QC 檢查表;深偽模型 | 每影格瑕疵分數;身份雜湊漂移;手/手指通過 | 抓出 >95% 資深 QC 發現項 + 30% 漏掉項 | DirectorAgent、VFXSupAgent | GeneratorAgent(重抽)、CompositorAgent | VBench 評估套件;手部偵測模型;臉部 ID 嵌入 (ArcFace);影格差異工具 | 工具使用 / ReAct(執行偵測器 → 標記 → 報告) |
| 50 | **PersonalizationEngineerAgent (個人化工程師)** | 變動範本(姓名/臉/聲音替換) | Idomoo 案例研究;DMA 活動;MarTech 文獻 | 渲染成功 ≥99.5%;抽查通過;隱私稽核通過 | 比頂尖人類範本活動更高的分享率 | ComplianceAgent (GDPR/CCPA)、AnalystAgent | TemplateDesignerAgent(脆弱性) | Idomoo/Pirsonal API;HeyGen 個人化;GDPR 同意管理平台 | ReAct(組裝範本 → 渲染 → 驗證 → 交付) |
| 51 | **TrailerEditorAgent (預告剪輯師)** | 勾子驅動之預告剪輯 | Golden Trailer 獎;Woollen/AV Squad 作品集;預告音樂庫 | 3 秒勾子率;上升動作曲線;音樂同步精準度 | 在 Golden Trailer 評分量表盲比中勝出 | DirectorAgent、MusicSupervisorAgent | EditorAgent(過剪)、ComposerAgent(不匹配) | DaVinci Resolve (MCP);預告音樂 API (Musicbed/Artlist);留存曲線預測器 | Self-Refine(留存曲線模型作為回饋) |
| 52 | **SportsAnalystAgent / TelestratorOp (運動分析師/戰術圖操作)** | 戰術解析 + 圖示 | MIT Sloan 論文;ESPN Stats & Info;Goldsberry 分析 | 戰術判讀準確性;螢幕清晰度分數 | 在戰術預測上勝過退役運動員 | SMEAgent(運動)、JournalistAgent | EditorAgent(漏放重播)、MotionGraphicsAgent(圖表清晰度) | 運動資料 API (StatsBomb、NBA Stats);戰術圖疊加工具;After Effects MCP | ReAct(擷取戰術資料 → 標註 → 渲染疊加) |

---

## 9. 專家元代理

### 9.1 編排代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 53 | **OrchestratorAgent (編排)** | 執行 CrewAI/AutoGen/LangGraph DAG;重試、逾時、扇出/扇入 | LangGraph + CrewAI + AutoGen 模式;Airflow/Temporal;PGA 時程範本 | DAG 完成 ≥99.5%;SLA 遵循;死鎖 = 0 | 在相同範圍內比人類 EP 更低的 TTD | ProducerAgent(範圍)、JudgeAgent(爭議)、停滯時 HiTL | 所有代理(資源消耗、重試風暴) | LangGraph 狀態機;Temporal 工作流程引擎;Redis(分散式鎖);可觀測性 (LangSmith) | Agentic Graph (LangGraph) — 確定性 DAG 執行 |
| 54 | **PlannerAgent (規劃)** | 將 brief 分解為含指派 + 評審關卡之階段 DAG | PMBOK;CrewAI 任務圖;階段範本 | 計畫有效性(無遺漏關卡);成本變異 <10% | 比 EP 首版更緊湊、更便宜的計畫(盲測 A/B) | ProducerAgent、FinanceAgent(預算) | RouterAgent(選錯)、OrchestratorAgent | LangGraph 計畫產生;成本估計模型;Gantt/PERT 工具 | ReAct(分解 → 估計 → 驗證 → 發出 DAG) |
| 55 | **RouterAgent (路由)** | 為每個子任務挑選正確的專家代理(與模型) | 代理能力登錄;基準歷史(成本/品質/延遲) | 路由準確率 ≥95% vs oracle;成本在預算內 | 在代理/供應商選擇上勝過人類製片 | OrchestratorAgent、CostOptimizerAgent | PlannerAgent(壞分解) | 代理登錄 DB;基準排行榜快取;定價 API | 分類器 + ReAct(任務嵌入比對 → 代理能力) |
| 56 | **JudgeAgent (評審)** | 透過多代理辯論裁決爭議;依評分量表打分 | Du 2023 (LLM 辯論);MT-Bench 評分量表;公會評分表 | 與專家小組評審者間 κ ≥0.8 | 比中位數人類評審更高的 κ | 推翻裁決時 HiTL | DirectorAgent、ScreenwriterAgent、任何爭議方 | MT-Bench/Arena 評估器;評分量表範本引擎 | 多代理辯論 (Du 2023) + LLM-as-Judge (Zheng 2023) |
| 57 | **GateKeeperAgent (關卡守門員)** | 階段轉換;驗證 L1/L2/L3 標準;簽署 C2PA | Stage-gate 方法;PGA Producers Mark;QMS 稽核 | 零漏放瑕疵;簽核 SLA ≥99% | 比人類 QA 主管更低的逃逸瑕疵率 | ComplianceAgent、AIQAConsistencyAgent | OrchestratorAgent(過早推進) | C2PA 簽署 (c2patool);JSON schema 驗證器;評分量表評估端點 | Constitutional AI(章程 = 階段關卡標準) |
| 58 | **MemoryAgent (記憶)** | 情境式 + 長期專案記憶;為任何代理檢索 | Reflexion (Shinn 2023);MemGPT;向量 DB 最佳實務 | 檢索 precision@5 ≥0.9;新鮮度 SLA | 在規模上比製片聖經更高的召回率 | 所有代理(修正事件) | 所有代理(過時事實) | Pinecone/Weaviate/Qdrant 向量 DB;MemGPT 式階層式記憶;嵌入模型 | Reflexion 記憶架構(MemGPT 延伸) |

### 9.2 創意代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 59 | **IdeationAgent (發想)** | 概念、勾子、標語之發散式腦力激盪 | 坎城大獎;D&AD;IDEO 設計思考;SCAMPER/de Bono | 點子數量;新穎度(嵌入距離);語意多樣性 | 在概念密度上贏得代理商提案比稿 | CreativeDirectorAgent、NoveltyAgent | CopywriterAgent(衍生)、DirectorAgent(無法拍攝) | 嵌入新穎度評分器;概念分群 (UMAP);Are.na/Pinterest 搜尋 | Self-Refine + NoveltyAgent 作為批評者 |
| 60 | **NarrativeArcAgent (敘事弧)** | 三幕劇 / Save-the-Cat / 英雄旅程結構 | Campbell;Snyder《Save the Cat》;Truby;Black List 分析 | 節拍表覆蓋 100%;轉折點間距;弧線曲線契合 | 在結構評分量表上勝過 WGA 初稿 | ScreenwriterAgent、DirectorAgent | ScriptwriterAgent(中段疲軟) | 節拍表驗證器;情緒弧繪圖器;結構範本 | Self-Refine(評分量表:節拍表完整性) |
| 61 | **StyleTransferAgent (風格轉移)** | 跨鏡頭一致地套用命名美學 | 精選風格資料集;LoRA/種子登錄;參考影格庫 | 風格相似度 (CLIP/DINO) ≥0.85;跨鏡變異 ≤τ | 在盲測偏好中勝過人類調色師+調色 | DirectorAgent、ColoristAgent | GeneratorAgent(偏離風格) | 每種風格的 LoRA 權重;CLIP/DINO 相似度評分器;Runway 風格鎖定模式;ComfyUI | Self-Refine(CLIP 風格分數作為回饋) |
| 62 | **WorldBuildingAgent (世界觀建構)** | 傳說、規則、地理、派系、魔法/科技系統 | Tolkien;《Worldbuilding》(Adams);粉絲 wiki;系列聖經外流 | 內部一致性(無矛盾);規則完整性 | 在 10 倍量下比編劇聖經更低的矛盾率 | ShowrunnerAgent、FactCheckerAgent | ScriptwriterAgent(傳說斷裂)、ConceptArtistAgent | 長上下文 LLM (Gemini 2.5 Pro);矛盾偵測模型;wiki 圖 DB | Reflexion(矛盾修正 → 情境式記憶) |
| 63 | **MoodBoardAgent (情緒板)** | 參考板:視覺、聲音、基調 | Pinterest/Are.na;lookbook 檔案;Spotify-Canvas | 參考連貫性(分群緊湊度);brief 對齊 | 比美術指導更快、更緊密的板(盲測 A/B) | DirectorAgent、ProductionDesignAgent | ConceptArtistAgent(偏離情緒) | Pinterest/Are.na API;Spotify Canvas;CLIP 分群;Figma 板生成 | ReAct(搜尋 → 分群 → 排版 → 驗證連貫性) |
| 64 | **NoveltyAgent / Anti-Cliché Critic (新穎度/反陳腔濫調)** | 標記俗套、陳腔濫調、過擬合輸出 | TV Tropes;OpenSubtitles n-gram 頻率;語料庫新穎度嵌入 | 陳腔濫調命中計數;對類別先驗的新穎度分數 | 比資深劇本編輯抓出更多陳腔濫調 | IdeationAgent、ScreenwriterAgent | ScriptwriterAgent(俗套堆砌)、CopywriterAgent(範本化) | TV Tropes 爬蟲;n-gram 頻率 DB;嵌入新穎度評分器 | LLM-as-Judge(反陳腔濫調章程) |
| 65 | **EmotionalArcAgent (情緒弧)** | 對應效價/喚醒度曲線;建議節拍 | Plutchik;情感運算資料集;Cron《Story Genius》 | 對目標的曲線契合;生物訊號代理迴歸準確性 | 比 NRG 試映卡更好的留存率預測 | DirectorAgent、EditorAgent、ComposerAgent | EditorAgent(中段平淡)、ComposerAgent(樂段不匹配) | 情感/情緒分類器 (GoEmotions);留存曲線預測器;生物訊號代理模型 | Self-Refine(情緒弧曲線作為評分量表目標) |

### 9.3 研究代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 66 | **WebResearchAgent (網路研究)** | 即時網路搜尋、來源排名、引用擷取 | Bing/Google/Brave API;Common Crawl;Perplexity 模式 | 每項主張的來源等級;引用精確度;近期命中 | 比編輯室研究員更快 + 更多來源 | FactCheckerAgent、CitationAgent | ScriptwriterAgent(未引用主張) | Brave/Google Search API;Jina Reader(網頁→markdown);來源品質分類器 | ReAct(查詢 → 擷取 → 抽取 → 評等 → 引用) |
| 67 | **ArchiveResearchAgent (檔案研究)** | 歷史/學術/檔案深度搜尋 | JSTOR、arXiv、PubMed、AP Archive、Getty、FOIA | 一手來源比率;檔案覆蓋廣度 | 比紀錄片製作人更高的一手來源比率 | FactCheckerAgent、SMEAgent | ScriptwriterAgent(依賴二手來源) | JSTOR/arXiv/PubMed API;Getty Images API;FOIA 申請工具;OCR (Tesseract) | ReAct(制定查詢 → 搜尋檔案 → 抽取 → 評等來源) |
| 68 | **TrendIntelligenceAgent (趨勢情報)** | 偵測新興迷因、聲音、格式 | TikTok Creative Center;Trendpop;Tubular;Reddit/X firehose | 對高峰的預測前置時間;趨勢清單之精確度/召回率 | 比人類策略師更早偵測,精確度更高 | SocialStrategistAgent、CopywriterAgent | IdeationAgent(脫離趨勢) | TikTok Creative Center API;Reddit/X 串流 API;Sensor Tower;Google Trends | ReAct + 時序異常偵測 |
| 69 | **CompetitorIntelligenceAgent (競爭對手情報)** | 競爭對手正在推出什麼 | Meta Ad Library;TikTok Top Ads;YouTube 爬取;發佈追蹤器 | 競爭對手集合之覆蓋率;對景觀之我方新穎度 | 比代理商策略簡報更全面 | BrandAgent、CreativeDirectorAgent | IdeationAgent(衍生) | Meta Ad Library API;TikTok Top Ads;SimilarWeb;YouTube Data API v3 | ReAct(爬取競爭對手 → 分類 → 報告差距) |
| 70 | **CitationAgent (引用)** | 標準化來源;評等一手/二手/三手 | Chicago、APA、AP 風格;SPJ 評等;CRAAP 測試 | 引用格式 100% 有效;一手比例 ≥目標 | 比編輯室文編更低的錯誤率 | FactCheckerAgent、JournalistAgent | WebResearchAgent(弱來源) | 引用解析器 (AnyStyle);DOI 解析器;CRAAP 評分模型 | Self-Refine(格式驗證器 + 來源評等器作為評分量表) |
| 71 | **InterviewSynthesisAgent (訪談綜整)** | 將從業者訪談綜整為資料 | Otter/Rev 逐字稿;同意書;SAG/WGA 範本 | 主題之編碼者間一致度;同意完整性 | 比質性研究員更快 + 更豐富的主題抽取 | ResearchPIAgent (HiTL)、ComplianceAgent | SMEAgent(專家被誤摘要) | Otter.ai/Rev API(轉錄);主題編碼模型;同意管理 DB | Reflexion(訪談者依主題缺口精煉問題) |
| 72 | **BenchmarkResearchAgent (基準研究)** | 監控 VBench、EvalCrafter、MT-Bench、FVD、CLIP-T 排行榜 | Papers-with-Code;HuggingFace 排行榜;會議論文集 | 基準覆蓋率;新鮮度 ≤7 天 | 比 ML 研究團隊更快 + 更廣 | OptimizationAgents(任何) | 所有 AI 代理(過時基準) | Papers-with-Code API;HuggingFace Hub API;arXiv RSS;VBench 排行榜爬蟲 | ReAct(輪詢排行榜 → 偵測變化 → 警示) |

### 9.4 最佳化代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 73 | **PromptOptimizerAgent (提示最佳化)** | 透過 OPRO/APE/DSPy/Promptbreeder 自動改進提示 | OPRO (Yang 2023);APE (Zhou 2022);DSPy (Stanford);Promptbreeder (DeepMind) | 每次迭代之分數提升;收斂速度 | 在保留 brief 上勝過手調提示 | PromptEngineerAgent、AIQAAgent | PromptEngineerAgent(次優種子) | DSPy 框架 (MIPRO 最佳化器);OPRO 實作;保留評估工具 | DSPy 編譯 + OPRO 元最佳化 |
| 74 | **CostOptimizerAgent (成本最佳化)** | 在模型/供應商間路由以求 $/品質 | 供應商定價;成本-品質前沿;FrugalGPT 模式 | $/成功任務;與前沿的 Pareto 距離 | 比人類 CFO 路由更低的 $/品質 | RouterAgent、FinanceAgent | RouterAgent(超支)、GeneratorAgent(重抽消耗) | 供應商定價 API;基準成本 DB;FrugalGPT 串聯邏輯 | ReAct(評估任務 → 挑選符合閾值的最便宜模型) |
| 75 | **LatencyOptimizerAgent (延遲最佳化)** | 平行化、快取、推測式解碼、批次 | vLLM;TensorRT-LLM;蒸餾;Anyscale/Ray | p50/p95 延遲;吞吐量/GPU 小時 | 比人類調優管線更低的 p95 | OrchestratorAgent | OrchestratorAgent(串行瓶頸) | vLLM;TensorRT-LLM;Ray Serve;Redis(回應快取);推測式解碼配置 | 工具使用剖析 + 自動化管線重構 |
| 76 | **RetentionOptimizerAgent (留存最佳化)** | 調整勾子、節奏、結構以求 AVD/留存率 | YouTube Analytics 基準;TikTok 留存曲線;AudienceSim | 預測留存對實際;對照組 AVD 提升 | 在 AVD 提升上勝過資深 YouTube 剪輯師 (A/B) | EditorAgent、AudienceSimAgent | EditorAgent(開場慢)、ScriptwriterAgent(前段廢話) | YouTube Analytics API;留存曲線預測器模型;A/B 測試框架 | RLAIF(獎勵 = 來自實際分析的留存提升) |
| 77 | **ROASOptimizerAgent (ROAS 最佳化)** | 為成效最佳化廣告創意 | Meta Marketing Science;TikTok Ads Academy;MMM/MTA 文獻 | 對照組 ROAS 提升;顯著性 ≥95% | 在相同預算下勝過資深行銷人員 | PerformanceMarketerAgent、AnalystAgent | UGCAgent(低勾子)、CopywriterAgent(弱 CTA) | Meta Ads API(創意測試);TikTok Ads;Bayesian MMM 工具 (Robyn/Meridian) | RLAIF(獎勵 = 來自廣告平台回饋的實際 ROAS) |
| 78 | **AccessibilityOptimizerAgent (無障礙最佳化)** | WCAG 2.2 對比、字幕、口述影像、色盲安全 | WCAG 2.2;W3C/WAI-ARIA;DCMP 字幕鑰匙;聾人/聽損準則 | 100% AA 符合,≥90% AAA;字幕 WER ≤2% | 比 ADA 認證稽核員抓出更多 a11y 瑕疵 | AccessibilityAgent (HiTL)、ComplianceAgent | EditorAgent(字幕同步)、ColoristAgent(對比) | axe-core/Lighthouse(對比);Whisper v4(字幕);口述影像產生器 | Constitutional AI(章程 = WCAG 2.2 成功標準) |
| 79 | **EvaluationHarnessAgent (評估工具)** | 執行基準(VBench、EvalCrafter、MT-Bench、FVD、CLIP-T);發布退步 | Papers-with-Code;HuggingFace 排行榜;基準儲存庫 | 退步精確度/召回率;警示延遲 <1 小時 | 比 ML 工程輪值更快抓到退步 | BenchmarkResearchAgent | 所有 AI 代理(退步警示) | VBench 套件;EvalCrafter;MT-Bench harness;CI/CD (GitHub Actions);警示 (PagerDuty) | 工具使用 / ReAct(執行基準 → 比較 → 退步時警示) |
| 80 | **SafetyRedTeamAgent (安全紅隊)** | 對抗式攻擊以測試深偽、偏見、越獄、毀謗 | Hany Farid 基準;Partnership on AI 框架;OWASP LLM Top 10 | 攻擊成功率保持 ≤1%;分類覆蓋 | 比內部紅隊輪值更高的覆蓋率 | EthicsAgent (HiTL)、ComplianceAgent | AvatarDesignAgent、VoiceCloneAgent、AllGenerators | 深偽偵測器(Farid 實驗室模型);偏見探針;越獄提示庫;OWASP 掃描器 | 多代理辯論(紅隊 vs 防禦者)+ 對抗式搜尋 |

---

## 10. 工作流程支援代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類訊號 | 接受批評來源 | 評論對象 | 工具存取 | 架構模式 |
|---|---|---|---|---|---|---|---|---|---|
| 81 | **AnalystAgent (分析師)** | 將業務、創意與技術成效遙測彙整為可決策報告 | 平台分析儀表板;實驗紀錄;評估工具輸出;基準歷史 | KPI 完整性;預測對實際變異在容差內;洞察到行動的轉換時間 | 比人類分析師輪值更快偵測可行動之績效變化 | SocialMediaStrategistAgent、PerformanceMarketerAgent、EvaluationHarnessAgent | 活動節奏、發布時機、留存與 ROAS 異常 | YouTube Analytics、Meta/TikTok Ads 儀表板、BI 倉儲、基準紀錄 | 對遙測之 ReAct + 迴歸分析 |
| 82 | **AudienceSimAgent (觀眾模擬)** | 模擬觀眾偏好、參與度與流失率 | 配對偏好資料集;留存研究;觀眾分群模型 | 跨族群偏好穩定性;留存預測準確性;不一致紀錄 | 比傳統試映週期更早預測觀眾反應 | DirectorAgent、EditorAgent、AnalystAgent、JudgeAgent | 勾子、節奏、清晰度、情感契合、預告強度 | 角色模擬器、配對評估工具、留存模型 | LLM-as-Judge + 配對偏好小組 |
| 83 | **AccessibilityAgent (無障礙)** | 在發布前負責最終無障礙驗收 | WCAG 2.2、字幕與口述影像準則、聾人/聽損審閱框架 | 字幕準確性、口述影像完整性、對比合規、發布就緒 | 比人類稽核更早找出阻擋發布之無障礙議題 | AccessibilityOptimizerAgent、EditorAgent、ColoristAgent、SoundMixerAgent | 字幕同步、對比問題、缺失之口述影像或手語層 | 字幕驗證器、對比分析器、口述影像審閱工具 | Constitutional AI 與無障礙章程 |
| 84 | **BrandAgent (品牌)** | 執行品牌語調、宣稱界限與視覺一致性 | 品牌書、核准活動、法律宣稱護欄、語調指南 | 品牌語調相似度、政策遵循、跨資產低偏差 | 比零散的人類審閱更佳地維持跨通路品牌一致性 | CopywriterAgent、MotionGraphicsAgent、MarketingAgent、BrandStrategistAgent | 語調漂移、視覺不一致、宣稱蔓延 | 品牌資產庫、嵌入相似度、風格指南 | 對品牌章程之 Self-Refine |
| 85 | **BrandStrategistAgent (品牌策略)** | 在腳本與活動執行前定義受眾價值框架與定位 | 定位框架、活動策略簡報、市場研究、品牌架構文件 | 策略連貫性、差異化強度、受眾訊息清晰度 | 比臨時的人類交接產生更清晰的品牌到腳本翻譯 | BrandAgent、ScreenwriterAgent、MarketingAgent | 定位缺口、弱價值主張、不一致的受眾框架 | 研究簡報、訊息框架、策略範本 | 與 BrandAgent 與 CreativeDirectorAgent 之多代理辯論 |
| 86 | **MarketingAgent (行銷)** | 為發布、推廣與發布順序打包內容 | 活動腳本、發布行事曆、媒體計畫、資產包裝要求 | metadata 完整性、資產就緒、發布順序準確性 | 比手動活動營運更快出貨多通路發布包 | SocialMediaStrategistAgent、SEOAgent、CopywriterAgent、TrailerEditorAgent | 缺失格式、弱推出時機、不完整推廣集 | 活動管理套件、metadata 工具、發布規劃器 | 對發布檢查表與通路要求之 ReAct |
| 87 | **SEOAgent (SEO)** | 透過標題、描述、metadata 與搜尋意圖最佳化可發現性 | 搜尋排名研究、影片 metadata 最佳實務、關鍵字分類學 | 關鍵字契合、metadata 完整性、搜尋意圖匹配 | 比手動 metadata 調整更快提升可發現性 | MarketingAgent、CopywriterAgent、AnalystAgent | 弱關鍵字、差勁的標題-描述契合、metadata 遺漏 | 關鍵字工具、metadata API、排名儀表板 | 含搜尋意圖驗證之 ReAct |
| 88 | **CommunityAgent (社群)** | 捕捉社群回應並分流質化訊號 | 社群管理腳本、情感資料集、升級規則 | 回應延遲、議題分群品質、情感追蹤準確性 | 比手動評論審閱更早發現新興的觀眾擔憂 | AnalystAgent、SocialMediaStrategistAgent、CommsAgent | 令人困惑的訊息、情感風險、反覆出現的抱怨 | 社群監聽工具、管理儀表板、分群模型 | 來自發布後觀眾回饋之 Reflexion |
| 89 | **TemplateDesignAgent (範本設計)** | 設計可重用且安全的個人化範本 | 變動內容設計系統、動態版面規則、活動範本庫 | 合併欄位健壯性、版面穩定性、渲染存活率 | 比手動設計變體更少破損地產生可重用範本 | PersonalizationEngineerAgent、UXAgent、CRMAgent | 脆弱版面、不安全佔位符邏輯、合併衝突 | 範本引擎、設計系統、schema 驗證器 | 對範本 schema 與渲染約束之 ReAct |
| 90 | **UXAgent (使用者經驗)** | 審閱個人化或互動式輸出的清晰度與可用性 | UX 啟發法、無障礙標準、可用性測試模式 | 可讀性、摩擦點偵測、使用者流程清晰度 | 比發布階段支援團隊更早標記使用者困惑 | TemplateDesignAgent、PersonalizationEngineerAgent、AccessibilityAgent | 令人困惑的流程、可讀性問題、弱互動提示 | UX 審閱檢查表、會話重播、可讀性工具 | 含 UX 評分量表之 LLM-as-Judge |
| 91 | **TrustSafetyAgent (信任與安全)** | 篩檢輸出是否有冒充、濫用或有害濫用情形 | 濫用分類資料集、冒充案例、政策規則書 | 政策命中率、濫用風險召回率、阻擋案例低偽陰性 | 比通用審核佇列更早抓到濫用風險 | ComplianceAgent、DeepfakeDetectionAgent、SafetyRedTeamAgent | 有害濫用路徑、冒充媒介、政策缺口 | 安全分類器、濫用分類 DB、審核 API | 用於信任與安全政策執行的 Constitutional AI |
| 92 | **CRMAgent (客戶關係管理)** | 透過 CRM 系統交付受眾鎖定或觸發式活動 | CRM 自動化流程、生命週期行銷腳本、觀眾分群規則 | 觀眾分群正確性、交付就緒、觸發準確性 | 比手動營運更快執行分群到交付流程 | PersonalizationEngineerAgent、TemplateDesignAgent、AnalystAgent | 錯誤分群、損壞的觸發時機、不完整的 CRM 載荷 | HubSpot/Salesforce 風格 CRM API、分群工具 | 對觸發與受眾 schema 之 ReAct |
| 93 | **LegalAgent (法律)** | 針對新興或高風險發布議題執行最終法律審查 | 媒體法參考、清查工作流程、毀謗/IP/隱私案例 | 議題識別召回率、簽核完整性、升級品質 | 相對於零散法律審查,減少後期法律意外 | ComplianceAgent (Legal)、JournalistAgent、ProducerAgent / EP、MPAAgent | 新興法律風險、權利不明、未解高風險宣稱 | 法律備忘錄系統、權利追蹤器、清查資料庫 | 人類介入升級 + 章程式審查 |
| 94 | **FestivalStrategistAgent (影展策略)** | 為影展與提交行事曆定位專案 | 影展提交指南、頒獎季策略、選片歷史 | 對影展之契合強度、包裝就緒、時機紀律 | 相對於通用發布規劃,改善提交鎖定 | ProducerAgent / EP、DirectorAgent、CriticAgent | 弱定位、錯時提交計畫、不完整包裝 | 影展行事曆、提交檢查表、媒體包追蹤器 | 含行事曆與包裝驗證之 ReAct |
| 95 | **CriticAgent (評論)** | 模擬審閱者、媒體或評審詮釋 | 評論資料集、影展評審評論、評論檔案 | 詮釋深度、一致性、審閱者模式多樣性 | 比臨時的內部品味審查提供更廣的質化覆蓋 | DirectorAgent、AudienceSimAgent、FestivalStrategistAgent、JudgeAgent | 作者解讀、基調不匹配、影展/媒體脆弱性 | 評論資料集、評審評分量表、質化評分工具 | 多代理辯論作為評論小組 |
| 96 | **LMSAgent (學習管理系統)** | 將學習內容打包並部署至 LMS 環境 | SCORM/xAPI 標準、LMS 發佈工作流程、完成追蹤 schema | 包裝有效性、追蹤完整性、部署成功率 | 比手動課程營運更快出貨可發佈之學習包 | InstructionalDesignAgent、AccessibilityAgent、LearnerSimAgent | 包裝合規、追蹤錯誤、學習目標不匹配 | LMS API、SCORM/xAPI 驗證器、課程打包工具 | 對 LMS 部署 schema 之 ReAct |
| 97 | **LearnerSimAgent (學習者模擬)** | 模擬學習者行為、困惑點與評量表現 | 學習者建模資料集、完成分析、測驗結果模式 | 摩擦點預測、完成準確性、模擬測驗真實性 | 在實際學習者抱怨前預測弱點 | InstructionalDesignAgent、LMSAgent、AnalystAgent | 令人困惑的內容、弱評量、低完成路徑 | 學習者模擬模型、評量預測器、LMS 資料 | 為學習成果改編之觀眾風格模擬 |
| 98 | **ContinuityAgent (連戲)** | 在角色、道具、服裝、環境與時間狀態間維持連戲 | 連戲紀錄、場記實務、資產清單狀態追蹤 | 狀態漂移偵測、場景間一致性、清單更新正確性 | 比後期審閱結束時更早抓到連戲斷裂 | CostumeDesignAgent、MUAAgent、AIQAConsistencyAgent、CinematographerAgent (DoP)、GateKeeperAgent | 角色狀態漂移、服裝與道具不匹配、時間邏輯錯誤 | 狀態清單、鏡頭比較工具、連戲 DB | 含連戲清單執行之工具使用 / ReAct |
| 99 | **LipSyncAgent (對嘴)** | 驗證並精煉音素-視位對齊作為專門關卡 | 對嘴研究、動畫時機參考、視位資料集 | 同步錯誤低於閾值、修正具體性、低偽陽性 | 比一般 QC 審閱更精確地找到同步漂移 | VoiceCloneAgent / LipSyncSpecialist、AnimatorAgent、AIQAConsistencyAgent | 嘴型不匹配、對白影格漂移、修正優先序 | 音素-視位對齊器、影格層級同步工具 | 圍繞同步驗證器輸出之 Self-Refine |
| 100 | **MusicSupervisorAgent (音樂監督)** | 管理音樂契合、樂段使用、權利意識與配樂打包 | 音樂監督筆記、樂段位置參考、配樂發行實務 | 樂段適合性、權利意識覆蓋、配樂包完整性 | 比零散交接更一致地協調音樂置入 | ComposerAgent、TrailerEditorAgent、LabelA&RAgent、LegalAgent | 樂段誤用、音樂權利模糊、配樂凝聚力問題 | 音樂資產追蹤器、樂段表、配樂打包工具 | 對樂段表與權利要求之 ReAct |
| 101 | **LabelA&RAgent (唱片公司 A&R)** | 為音樂特定工作流程代表唱片公司與藝人方向 | A&R 腳本、唱片公司發行筆記、藝人簡報檔案 | 藝人契合品質、發行定位、回饋轉換時間 | 比脫節的利害關係人對話更快對齊音樂創意 | MusicVideoDirectorAgent、MusicSupervisorAgent、LabelDigitalAgent | 藝人方向漂移、發行不匹配、包裝弱點 | 曲目系統、發行追蹤器、藝人簡報工具 | 與音樂利害關係人之多代理辯論 |
| 102 | **LabelDigitalAgent (唱片公司數位)** | 執行唱片公司端之數位推出、metadata 與通路打包 | 數位音樂發行營運、metadata schema、發行平台需求 | metadata 完整性、推出時機、通路就緒 | 比臨時發行營運交付更乾淨的唱片公司端包裝 | MusicVideoDirectorAgent、SocialMediaStrategistAgent、MarketingAgent | 缺失 metadata、發行時機問題、資產版本混淆 | 數位發行系統、通路儀表板、metadata 工具 | 對發行包要求之 ReAct |
| 103 | **DeepfakeDetectionAgent (深偽偵測)** | 偵測合成身份、聲音與來源欺騙風險 | 深偽鑑識資料集、合成媒體基準、身份風險研究 | 鑑識召回率、偽陰性控制、來源驗證準確性 | 抓出一般 QC 漏掉的欺騙性合成標記 | AvatarDesignAgent、VoiceCloneAgent、TrustSafetyAgent、SafetyRedTeamAgent | 身份異常、來源漏洞、欺騙性合成模式 | 鑑識模型、臉/聲音異常偵測器、來源驗證器 | 含鑑識評分之工具使用 / ReAct |
| 104 | **CommsAgent (公關傳播)** | 協調對外訊息、揭露與公開回應姿態 | 危機溝通指南、揭露標準、PR 腳本 | 訊息一致性、揭露完整性、升級品質 | 比零散的利害關係人訊息產生更快對齊回應 | MarketingAgent、CommunityAgent、LegalAgent、BrandAgent | 揭露缺口、不一致對外訊息、弱回應框架 | 傳播行事曆、核准工作流程、回應範本 | 含核准鏈之 ReAct |
| 105 | **ArchiveProducerAgent (檔案製片)** | 為大量重用或紀錄片工作流程打包檔案材料與來源資產 | 檔案製作筆記、來源策展實務、來源保存標準 | 來源包完整性、權利覆蓋、來源保存 | 比手動蒐集與排序工作流程更乾淨地組裝可重用之檔案包 | ArchiveResearchAgent、JournalistAgent、LegalAgent | 缺失之檔案脈絡、弱來源打包、權利缺口 | 檔案資產管理器、metadata 系統、來源紀錄 | 對檔案清單之 ReAct |
| 106 | **StandardsEditorAgent (標準編輯)** | 執行編輯標準、來源紀律與更正政策 | 編輯室標準手冊、更正政策、署名標準 | 標準合規率、署名準確性、更正就緒 | 比後期文編減少標準漂移 | JournalistAgent、FactCheckerAgent、CorrectionsAgent、LegalAgent | 弱署名、標準違反、更正政策缺口 | 編輯檢查表、署名驗證器、標準 DB | 含編輯標準章程之 Constitutional AI |
| 107 | **EthicsAgent (倫理)** | 審查倫理風險、揭露充分性、公平性與社會影響 | 倫理框架、合成媒體揭露指引、公平性稽核 | 倫理議題召回率、緩解清晰度、升級精確度 | 比反應式倫理審查更早發現發布風險 | StandardsEditorAgent、ComplianceAgent (Legal)、TrustSafetyAgent、SafetyRedTeamAgent | 揭露不足、公平性疑慮、敏感內容風險 | 倫理審查範本、風險矩陣、揭露檢查表 | 多代理辯論 + 章程式審查 |
| 108 | **ChannelManagerAgent (通路管理)** | 為節奏與 metadata 就緒管理連續或平台通路營運 | 通路發佈腳本、metadata 標準、排程營運 | 發佈就緒、節奏穩定性、metadata 完整性 | 比手動通路營運改善發佈紀律 | SocialMediaStrategistAgent、SEOAgent、AnalystAgent、MarketingAgent | 發布就緒缺口、metadata 遺漏、時程延誤 | CMS/通路儀表板、排程工具、metadata 驗證器 | 含發佈執行手冊之 ReAct |
| 109 | **CorrectionsAgent (更正)** | 協調發佈後修正與更正揭露 | 更正工作流程、撤回與更新政策、版本追蹤 | 更正轉換時間、版本替換準確性、通知完整性 | 比無結構之事件處理更快解決發布後議題 | StandardsEditorAgent、FactCheckerAgent、ChannelManagerAgent | 未關閉的更正迴圈、不完整通知、過時版本 | 版本控制系統、發佈工具、更正追蹤器 | 對更正與替換工作流程之 ReAct |
| 110 | **MPAAgent (分級協助)** | 為長片工作流程準備與分級相關之打包與發布就緒輸入 | 分級提交參考、內容警示、戲院打包規則 | 分級包完整性、警示清晰度、升級品質 | 比手動準備產生更乾淨的長片發布分類包 | ProducerAgent / EP、LegalAgent、EthicsAgent | 缺失警示、不完整分級準備、不清楚的分類支援 | 提交包、警示範本、分類檢查表 | 含結構化打包支援之人類介入 |
| 111 | **SalesAgent (銷售)** | 處理面向買家的銷售打包,服務發行商與通路 | 權利視窗腳本、市場包範例、買家材料 | 買家包完整性、權利清晰度、市場契合打包 | 比手動組裝更快產生銷售就緒之發布包 | ProducerAgent / EP、DistributorAgent、MarketingAgent | 缺失買家資訊、弱定位、不完整權利摘要 | 權利系統、包建構器、買家 CRM | 對買家包要求之 ReAct |
| 112 | **DistributorAgent (發行)** | 管理下游交付給買家、平台與地區 | 發行規格、通路要求、包交接工作流程 | 通路規格合規、交接完整性、領土路由準確性 | 相對於零散交付營運,減少交付規格不匹配 | SalesAgent、ArchiveMasterAgent、SoundMixerAgent、ColoristAgent | 規格不匹配、不完整通路包、路由錯誤 | 交付管理系統、通路規格 DB、打包驗證器 | 對發行規格矩陣之 ReAct |
| 113 | **AwardsStrategistAgent (獎項策略)** | 規劃獎項提交與活動時機 | 獎項行事曆、活動腳本、類別定位歷史 | 提交就緒、類別契合、時程精準度 | 相對於通用發布規劃,改善獎項時機紀律 | ProducerAgent / EP、CriticAgent、MarketingAgent | 弱活動時機、差勁類別契合、不完整提交資產 | 獎項行事曆、活動追蹤器、提交檢查表 | 含獎項時程最佳化之 ReAct |
| 114 | **ArchiveMasterAgent (典藏母帶)** | 製作典藏級母帶與保存包 | 保存標準、checksum 工作流程、檔案 metadata 實務 | checksum 完整性、保存 metadata 完整性、檔案包有效性 | 比後期匯出工作流程交付更可靠的檔案包 | DistributorAgent、ColoristAgent、SoundMixerAgent、GateKeeperAgent | 不完整保存包、檔案規格違反、metadata 缺口 | 檔案母帶工具、checksum 工具、保存 metadata 系統 | 含保存驗證之工具使用 / ReAct |

---

## 11. AI 代理的共通結構

每個代理 — 無論類別為何 — 都實作此骨架。源自原始文件的架構模式 (§1)、批評協議 (§6) 與通用成功標準框架 (§5),並以當前 (2026) 工具研究加以豐富。

### 11.1 架構圖

下圖將共通代理呈現為專業營運架構,而非簡單的元件草圖。它展示了**編排**、**輸入契約**、**知識與工具表面**、內部的**規劃 → 行動 → 自我審查**迴圈、**可追溯性與來源控制**、**三層品質關卡**(規格 → 評分量表 → 偏好)、**發布打包**、**同儕批評**、**人類升級**與**持續改進**如何作為一個受治理的系統共同運作。

![專業共通 AI 代理架構圖](./common-agent-structure.svg)

> **提示:**在 GitHub 上點擊圖片可全螢幕檢視,或直接下載 [`common-agent-structure.svg`](./common-agent-structure.svg)。此 SVG 設計為簡報級的架構審查與實作規劃參考。

### 11.2 組件參考表

| # | 組件 | 用途 | 機制 / 實作筆記 |
|---|---|---|---|
| 1 | **Identity (身份)** | 用於路由、紀錄、來源的穩定唯一識別 | Kebab-case ID + 語意化版本(例如 `director-agent@2.1.0`)。註冊於 RouterAgent 使用的代理能力登錄中。 |
| 2 | **Responsibility (Scope / 範圍)** | 一句話定義代理擁有什麼 | 反映人類工藝角色。透過登錄中明確記錄的邊界防止範圍重疊。 |
| 3 | **Knowledge Distillation Source (知識蒸餾來源)** | 代理被訓練或 RAG 接地的授權/同意資料集 | 獎項檔案、學術論文、專家訪談、同儕審查期刊。透過持續蒸餾迴圈(原文件 §7)更新。 |
| 4 | **Tool Access (工具存取)** | 外部 API、生成器、驗證器、DCC 橋接 | 影片生成:Sora 2、Veo 3.1 (Gemini API)、Runway Gen-4/Aleph、Kling 3.0。語音:ElevenLabs v3、Sync.so、HeyGen。DCC:透過 MCP 橋接 Resolve/Nuke/AE。皆透過 MCP (Model Context Protocol, Anthropic 2024) 存取。 |
| 5 | **Architecture Pattern (架構模式)** | 驅動代理之推理/學習迴圈 | 以下其中之一或多種:Self-Refine [1]、Reflexion [2]、RLAIF/Constitutional AI [3]、多代理辯論 [4]、LLM-as-Judge [5]、配對偏好 (Arena) [5]、ReAct [6]、Agentic Graph (LangGraph/CrewAI/AutoGen) [7]、DSPy/OPRO 提示最佳化 [8]。 |
| 6 | **Memory (記憶)** | 情境式 + 長期專案記憶 | 透過 MemoryAgent 存取的向量 DB (Pinecone/Weaviate/Qdrant)。實作 MemGPT 式階層式記憶,具摘要與淘汰機制。Reflexion 代理在此儲存口語式自我回饋。 |
| 7 | **Constitution / Rubric (章程 / 評分量表)** | 用於自我檢查的書面、角色特定計分指南 | 範例:Murch 六法則(剪輯)、12 法則(動畫)、Save-the-Cat 節拍(編劇)、WCAG 2.2(無障礙)、FAA Part 107(空拍機)、SAG-AFTRA AI 附約(同意)。用作 Constitutional AI 模式中的「章程」。 |
| 8 | **Self-Quality: L1 Spec (自我品質:L1 規格)** | 輸出是否符合結構化 brief? | JSON schema 驗證 + 工具驗證器(編碼、LUFS、長寬比、影格數、檔案格式)。必須 100% 通過。 |
| 9 | **Self-Quality: L2 Rubric (自我品質:L2 評分量表)** | 是否符合此角色之工藝評分量表? | LLM-as-Judge (Zheng 2023) 搭配角色特定章程。必須得分 ≥85/100。若低於閾值,最多進行 3 次 Self-Refine 迭代。 |
| 10 | **Self-Quality: L3 Preference (自我品質:L3 偏好)** | 目標受眾是否會在人類基準與此版本間選擇此版本? | 配對比較:AudienceSim 小組(≥200 個模擬角色 + ≥20 個 HiTL 樣本)。勝率 ≥50%(對等)或 ≥55%(超越)。 |
| 11 | **Surpass-Human Signal (超越人類訊號)** | 預先註冊之證明,顯示代理超越認證專業人士 | 基準支配;盲測 Arena 偏好 ≥55%;速度 × 品質(在 ≤10% 轉換時間下達同等 L2);更低的 90 日瑕疵率;通過認證;在同等品質下更高的新穎度。 |
| 12 | **Critique Inbox (批評收件匣)** | 接收來自同儕之結構化回饋的通道 | 共享 `CritiqueMessage` JSON 匯流排。嚴重程度:blocker(中止 DAG)、major(Self-Refine ≤3 迭代)、minor/nit(紀錄供 RLAIF)。爭議 → JudgeAgent 多代理辯論 → 若未解決則 HiTL。 |
| 13 | **Critique Outbox (批評寄件匣)** | 此代理有資格審查其作品的同儕代理 | 在角色表中按代理定義。訊息發送至相同匯流排。基於證據、引用評分量表、附加至 C2PA 來源。 |
| 14 | **HiTL Escalation (人類介入升級)** | 何時必須引入人類 | 同意(SAG-AFTRA AI 附約、歐盟 AI 法第 50 條);最終法律簽核;MPA 分級;影展資格;危機溝通;跨文化敏感性。 |
| 15 | **Provenance (C2PA / 來源)** | 對每件作品的密碼學簽署 | 每件發出作品以 C2PA (c2patool) 簽署。下游代理驗證鏈。已接受之批評附加至清單。平台(YouTube、TikTok、Meta)依 C2PA 存在自動標記。 |
| 16 | **Continuous Learning (持續學習)** | 代理如何在部署後持續改進 | Bootstrap(授權資料集)→ 專家訪談(付費、同意)→ 即時 RLAIF (DPO/KTO)→ 獎項評分量表接地 → 對抗式紅隊 → 30/60/90 日現實檢驗(留存、ROAS、獎項)。 |
| 17 | **Orchestration Integration (編排整合)** | 代理如何融入多代理圖 | 註冊為 LangGraph/CrewAI/AutoGen DAG 中的節點。OrchestratorAgent 排程;PlannerAgent 指派;RouterAgent 選擇模型/供應商;GateKeeperAgent 在推進前驗證 L1-L3。 |

### CritiqueMessage Schema(通用)

```json
{
  "critique_id": "uuid",
  "from_agent": "EditorAgent",
  "to_agent": "DirectorAgent",
  "artifact_ref": "shot_42_take_3.mp4",
  "severity": "blocker | major | minor | nit",
  "category": "pacing | continuity | accuracy | compliance | accessibility | brand | craft",
  "evidence": ["timecode 00:01:14 — 較類型先驗之切點超出 1.4 秒"],
  "suggested_action": "縮減 1.0 秒;重新評估持續時間",
  "rubric_reference": "Murch 六法則 §3",
  "must_resolve_before": "phase_4_review"
}
```

### 組合圖

```text
[Brief] ──► PlannerAgent ──► OrchestratorAgent ──► RouterAgent ──► (52 個工藝代理 §1–§8)
                 ▲                  │                                       │
                 │                  ▼                                       ▼
             MemoryAgent      GateKeeperAgent ◄─── JudgeAgent ◄──── CritiqueMessages
                                    ▲                                       ▲
                                    │                                       │
            [創意元代理:] IdeationAgent · NarrativeArcAgent · StyleTransferAgent · MoodBoardAgent · NoveltyAgent · EmotionalArcAgent
            [研究元代理:] WebResearchAgent · ArchiveResearchAgent · TrendIntelAgent · CompetitorIntelAgent · CitationAgent · InterviewSynthAgent · BenchmarkResearchAgent
            [最佳化元代理:] PromptOptimizerAgent · CostOptimizer · LatencyOptimizer · RetentionOptimizer · ROASOptimizer · AccessibilityOptimizer · EvalHarnessAgent · SafetyRedTeamAgent
```

---

## 12. 參考文獻

### 基礎論文(架構模式)

| Ref | 論文 | 主要貢獻 | 連結 |
|---|---|---|---|
| [1] | Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback," NeurIPS 2023 | 代理起草 → 對評分量表自我批評 → 不需權重更新即可迭代修訂 | [arXiv:2303.17651](https://arxiv.org/abs/2303.17651) |
| [2] | Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning," NeurIPS 2023 | 將口語自我反思儲存至情境式記憶緩衝區,以改善後續試驗中的決策 | [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) |
| [3] | Bai et al., "Constitutional AI: Harmlessness from AI Feedback," 2022 | 由書面章程治理之 AI 評論者提供獎勵訊號;無須人類標籤的 RLAIF | [arXiv:2212.08073](https://arxiv.org/abs/2212.08073) |
| [4] | Du et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate," 2023 | 多個 LLM 代理辯論;改善任務中的事實性與推理 | [arXiv:2305.14325](https://arxiv.org/abs/2305.14325) |
| [5] | Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023 | GPT-4 評審與人類偏好達 >80% 一致性;可擴展之評估 | [arXiv:2306.05685](https://arxiv.org/abs/2306.05685) |
| [6] | Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR 2023 | 交錯推理軌跡與工具使用動作以進行接地之決策 | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) |
| [7] | LangGraph / CrewAI / AutoGen (2024–2026) | 代理圖編排:具狀態、交接、審查關卡、人類介入之 DAG | [LangGraph](https://github.com/langchain-ai/langgraph)、[CrewAI](https://github.com/crewAIInc/crewAI)、[AutoGen](https://github.com/microsoft/autogen) |
| [8] | Yang et al., "Large Language Models as Optimizers" (OPRO), 2023; Khattab et al., DSPy (Stanford, 2023–2026) | 使用 LLM 對提示進行元最佳化;DSPy 將宣告式 LM 程式編譯為最佳化管線 | [OPRO arXiv:2309.03409](https://arxiv.org/abs/2309.03409)、[DSPy](https://github.com/stanfordnlp/dspy) |

### 評估基準

| 基準 | 範疇 | 連結 |
|---|---|---|
| VBench / VBench 2.0 | 影片生成品質 — 16 個維度(時序 + 影格);VBench 2.0 新增人類保真度、創造力、物理 | [arXiv:2311.17982](https://arxiv.org/abs/2311.17982)、[VBench 2.0: arXiv:2503.21755](https://arxiv.org/abs/2503.21755) |
| EvalCrafter | 文字轉影片 — 跨視覺、內容、動態品質之 18 個指標 | [arXiv:2310.11440](https://arxiv.org/abs/2310.11440) |
| MT-Bench / Chatbot Arena | 透過人類配對 + LLM 評審評估的 LLM 輸出品質 | [arXiv:2306.05685](https://arxiv.org/abs/2306.05685) |

### 生成式影片模型(工具存取 — 2026 全景)

| 模型 | 供應商 | 主要能力 | 存取 |
|---|---|---|---|
| Sora 2 / Sora 2 Pro | OpenAI | 同步對白 + SFX + 背景音;電影/寫實/動漫風格;1080p 20 秒 | [OpenAI Videos API](https://developers.openai.com/api/docs/models/sora-2)(2026 年 9 月停用) |
| Veo 3.1 | Google DeepMind | 4K / 1080p / 720p、8 秒;原生音訊;可配置 16:9 與 9:16;角色/物件方向之多影像參考 | [Gemini API](https://ai.google.dev/gemini-api/docs/video) / [Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate) |
| Runway Gen-4 / Gen-4.5 / Aleph | Runway | ControlNet guides、攝影機路徑、風格鎖定、Layout Sketch;Aleph 用於影片轉影片編輯 | [Runway API](https://docs.dev.runwayml.com/) |
| Kling 3.0 | 快手 | 電影級動態真實感;物理準確性;動作控制(參考影片);原生音訊 | [Kling API (fal.ai)](https://fal.ai/models/fal-ai/kling-video) |

### 語音與虛擬化身工具 (2026)

| 工具 | 供應商 | 能力 |
|---|---|---|
| ElevenLabs v3 | ElevenLabs | 表情豐富之 TTS;即時/專業聲音複製;對話模式(多語者);長篇 Projects API;音效生成 | [Docs](https://elevenlabs.io/docs) |
| HeyGen Avatar IV | HeyGen | 寫實 AI 虛擬化身;175+ 種語言對嘴;ElevenLabs 整合;個人化 API | [HeyGen](https://www.heygen.com) |
| Synthesia | Synthesia | 規模化企業級 AI 虛擬化身;SCORM 相容;品牌可控 | [Synthesia](https://www.synthesia.io) |
| Sync.so / Wav2Lip | 開源 + API | 對嘴疊加;音素-視位對齊 | [Sync.so](https://sync.so) |

### 基礎設施標準

| 標準 | 用途 | 狀態 (2026) |
|---|---|---|
| C2PA(內容來源) | 對每件 AI 生成作品的密碼學清單簽署;平台(YouTube、TikTok、Meta)自動標記 | 歐盟 AI 法行為準則(2026 年 3 月)強制 C2PA + 浮水印合併。超過 2,300 個工具支援。[contentauthenticity.org](https://contentauthenticity.org/blog/the-state-of-content-authenticity-in-2026) |
| MCP(Model Context Protocol) | LLM ↔ 工具整合之開放標準;2,300+ 個公開伺服器;被 Claude、VS Code、Cursor 等採用 | 2025 年 12 月由 Anthropic + OpenAI + Block 捐贈給 Agentic AI Foundation(Linux 基金會)。[modelcontextprotocol.io](https://modelcontextprotocol.io) |
| DSPy | 用於程式化(非提示)LLM 之框架;將宣告式管線編譯為最佳化之提示/微調 | Stanford 維護;MIPRO 最佳化器;由 PromptOptimizerAgent 用於自動化提示改進。[github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) |

---

*生成日期:2026 年 5 月。來源:[`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md)。核心配置從 `agents_old.md` 恢復;缺失之工作流程支援內容已合併至相同的表格式結構中。*