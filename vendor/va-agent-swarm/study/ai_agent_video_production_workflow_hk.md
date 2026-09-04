# AI 代理影片製作工作流程

> 為 `human_video_production_workflow.md` 的配套文件。針對主要人員名冊中的每個人類團隊角色，本文件定義了替換（或增強）該角色的 **AI 代理**，以及：職責範圍、知識蒸餾管道、自我品質標準、代理超越人類專業人員的信號、代理如何接受來自其他代理的評論，以及該代理有資格評論哪些內容作為回饋。

---

## 1. 系統基礎與參考掃描計劃

| 模式 | 用途 | 參考 |
|---|---|---|
| **Self-Refine（自我優化）** | 代理起草 → 按評分標準自我批評 → 修訂 | Madaan et al., 2023 |
| **Reflexion（反思）** | 代理將語言回饋存儲於情節記憶中，重試 | Shinn et al., 2023 |
| **RLAIF／憲法式 AI** | 由書面憲法管理的 AI 評論員提供獎勵信號 | Bai et al., 2022 |
| **多代理辯論** | 兩個或以上代理辯論；評判代理選擇較佳答案 | Du et al., 2023（LLM debate） |
| **LLM 作為評判（附評分標準）** | 凍結的評判模型按預先註冊的評分標準對輸出評分 | Zheng et al., 2023（MT-Bench） |
| **成對偏好（Arena）** | 代理輸出與人類參考之間的盲測 A/B 投票 | LMSYS Chatbot Arena 方法論 |
| **工具使用／ReAct** | 代理推理 + 調用外部工具（渲染器、驗證器） | Yao et al., 2022 |
| **代理圖（CrewAI／AutoGen／LangGraph）** | 角色以 DAG 形式編排，設有交接及審查關卡 | CrewAI、AutoGen、LangGraph |
| **來源證明（C2PA）** | 每個產物簽名；下游代理驗證鏈 | C2PA 規範 |

以下所有代理均假設以編排節點的形式在 CrewAI／AutoGen／LangGraph 拓撲中實現，並具有對生成式影片模型（Sora、Veo、Runway、Kling）、TTS／語音克隆 API（ElevenLabs、Sync.so、Hedra）、DCC 工具（Resolve、Nuke、AE，通過 MCP 橋接）以及共享評論匯流排的工具訪問權限。

### 1.1 參考資料掃描與知識綜合流程

本系統的文件增強流程遵循固定的「掃描 → 綜合」循環，確保從 `study/reference/how_to_build_a_video_agent_system` 加入的新內容都可追溯、範圍清晰，且在技術上保持一致。

| 步驟 | 方法 | 抽取內容 | 納入規則 |
|---|---|---|---|
| **盤點** | 在閱讀前先列出所有章節、代理清單與蒸餾說明 | 檔案覆蓋圖、章節分群、缺漏主題提示 | 未完成全部參考檔案索引前，不更新正文 |
| **分群** | 按功能將檔案分為：編排、創作、質檢、交付、優化、訓練 | 主題分組與重疊圖 | 每個概念必須能對應到至少一個工作流程階段 |
| **抽取** | 擷取技術概念、實作細節、指標、交接方式與最佳實踐 | 候選事實、代理職責、門檻、產物類型 | 只抽取足夠具體、可操作化的主張 |
| **驗證** | 以第二份參考章節、現有章節或本文件已採用的標準作交叉核對 | 已驗證增補、排除假設、歧義標記 | 模糊或僅單一來源支持的內容，不納入核心工作流程 |
| **映射** | 將已驗證內容掛接到本文件中最合適的章節 | 依章節、表格或階段關卡整理的修訂清單 | 優先強化現有結構，而非再平行建立一套新分類 |
| **整合** | 重寫受影響段落，讓新增細節強化架構、交接與評估邏輯 | 更新後的工作流程文字、表格與共享契約 | 新內容必須提升技術深度，且不得與鄰近內容重複 |
| **覆核** | 由頭到尾重讀，檢查一致性、完整性、術語及事實對齊 | 最終修訂集與後續修正項目 | 術語、邏輯流程與關卡標準未一致前不得發布 |

**工作規則：**
1. 以四個視角抽取概念：**技術架構**、**實作次序**、**品質／合規**、**持續學習**。
2. 除非市場資料會直接改變路由、成本或規模決策，否則優先保留與工作流程直接相關的事實。
3. 明確記錄交接產物：提示詞、場景封包、分軌、調色母版、清單檔、來源證明封裝與遙測資料。
4. 除非新增角色能真正補上編排、驗證、連續性、交付或再訓練缺口，否則不任意膨脹角色數量。
5. 將交付封裝、可觀測性與資產管理視為系統架構的一部分，而不是事後補充操作。

### 1.2 執行期製作系統架構

| 層級 | 核心責任 | 實作說明 |
|---|---|---|
| **編排執行層** | 規劃、路由、排程、重試與升級代理任務 | PlannerAgent 拆解簡報；OrchestratorAgent 執行 DAG；RouterAgent 選擇代理與模型組合；JudgeAgent 處理爭議 |
| **資產與資料骨幹** | 儲存所有提示詞、來源資產、衍生資產、版本、依賴關係及使用權 | 需要不可變資產 ID、copy-on-write 版本、依賴觸發重渲染規則，以及可搜尋中介資料 |
| **訊息與狀態層** | 在代理之間傳遞評論、工作狀態、渲染事件與關卡決策 | 採事件驅動匯流排加持久狀態儲存；所有長時間工作都必須可恢復且可審計 |
| **品質與連續性驗證網** | 執行技術 QC、連戲檢查、瑕疵偵測、無障礙與合規關卡 | 使用多輪驗證、時間連續性掃描、響度與色彩檢查，以及角色專屬評分法官 |
| **可觀測性與重播** | 顯示即時狀態、失敗原因、瓶頸與歷史決策 | 結構化日誌、工作時間線、關卡儀表板、基準警報，以及可回放的資產沿襲鏈 |
| **交付封裝層** | 將母版封裝為戲院、串流、廣播、存檔、預告片及活動版本 | 發行是分支式流程，需按渠道處理規格、字幕、中介資料、DRM/KDM 及來源證明 |
| **運算與儲存擴展** | 依製作規模匹配基建支出，同時不打破交付期限 | 將互動式生成與批次渲染分離；自動擴展 GPU 池；分層管理熱、溫、冷存儲 |

### 1.3 共享產物交接契約

每個階段都要向下游代理交付機器可讀的 manifest，讓創意工作、質檢與合規保持同步。

| 欄位 | 用途 |
|---|---|
| **artifact_id / version** | 每個輸出與修訂版本的唯一身份 |
| **parent_assets** | 指向劇本、提示詞、素材底片、分軌、參考資料及前一版剪接的來源鏈接 |
| **brief_scope** | 精確的子任務、驗收標準與目標受眾區段 |
| **technical_spec** | 編碼、畫幅比例、時長、幀率、色域、響度、字幕要求 |
| **rights_and_consent** | 授權狀態、肖像／聲音同意狀態、地域限制、禁運規則 |
| **continuity_state** | 角色造型、道具、服裝、環境、場景時間邏輯及身份雜湊 |
| **qc_status** | 最新 L1/L2/L3 結果，以及六輪交付 QC 狀態 |
| **target_channels** | 戲院、串流、廣播、存檔、付費社交、CRM、LMS 或影展渠道 |
| **provenance_manifest** | C2PA 參考、評論記錄指標及最終簽核鏈 |

### 1.4 反覆覆核紀律

本系統的文件修訂不是一次性的校對，而是重複挑戰假設的循環。100 輪重估可分為以下幾個區段：

| 輪次 | 主要問題 |
|---|---|
| **1-20** | 所有抽取主張是否都可追溯到參考集，並與文件結構對齊？ |
| **21-40** | 架構是否描述了真正的控制平面：編排、記憶、資產、交付與可觀測性？ |
| **41-60** | 工作流程交接是否足夠明確，可支援實作、QC、連戲與合規自動化？ |
| **61-80** | 指標、門檻與評估層是否在創意、技術及商業關卡之間保持一致？ |
| **81-100** | 用語是否無歧義、前後一致，並達到專業技術文件標準？ |

---

## 2. 主要代理名冊

替換 `human_video_production_workflow.md` 第 § 部分「主要製作人員參考表」中的人類團隊。文件以相同的 52 個工藝角色為起點，再延伸出專家級元代理與共享製作服務。

### 2.1 主創團隊代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 1 | **DirectorAgent** | 掌握創意願景；發出鏡頭意圖、設定節奏、核准鏡次 | Criterion 導演評論音軌；IMDb 前 250 名導演訪談；DGA 研討會；MasterClass 語料庫（Scorsese/Lynch/Gerwig） | 鏡頭意圖忠實度（CLIP-T ≥0.32）；故事節拍覆蓋率 100%；節奏曲線符合類型先驗 | 在相同劇本的盲測成對比較中，對 DGA 導演剪接版勝率 ≥55%（Arena 協議） | ScreenwriterAgent（故事節拍）、EditorAgent（節奏）、AudienceSim 代理（試映）——通過結構化 JSON 評論匯流排 | EditorAgent、DoPAgent、ScreenwriterAgent、ComposerAgent——發出「創意意圖差異」 |
| 2 | **ProducerAgent／EP** | 預算、排程、招聘、交付；審批階段關卡 | PGA 監製標章指南；Variety/Deadline 預算洩露；LineProducer Excel 語料庫 | 準時交付率；預算偏差 <±5%；人才滿意度（RLHF 分數） | 以 0.6 倍成本擊敗 PGA 認證監製的排程，且客戶滿意度相同 | 所有下游代理（升級）；最終綠燈由 HumanInTheLoop 關卡決定 | DirectorAgent（範圍蔓延）、所有代理（資源消耗） |
| 3 | **ScreenwriterAgent** | 處理方案 → 劇本；對白；結構 | Black List 劇本；WGA 圖書館；McKee《Story》；Truby《故事解剖》；Charlie Kaufman／Sorkin 訪談記錄 | Save-the-Cat 節拍表通過；對白獨特性（每個角色的嵌入向量距離 ≥τ）；根據意見的改寫差異 | 在盲測閱讀中對 Black List 前十名劇本勝率 ≥50%（模擬 WGA 評判小組） | DirectorAgent、DramaturgAgent、StoryEditorAgent——基於意見的 Reflexion 循環 | DirectorAgent（故事大綱清晰度）、DialogueAgent、ConsistencyAgent |
| 4 | **ShowrunnerAgent** | 跨集故事弧、編劇室編排 | WGA 節目總監培訓；The Sopranos/Breaking Bad 編劇室記錄；Mike Schur 教學材料 | 各集之間的弧線連續性得分；角色線索完成度；調性變異在範圍內 | 10 集內系列聖經覆蓋率 ≥99% 且無偏差（人類基準約 ~95%） | NetworkNotes 代理、AudienceSim、與 ScreenwriterAgent 的多代理辯論 | ScreenwriterAgent（弧線）、CastingAgent、DirectorAgent（單集調性） |
| 5 | **CastingAgent** | 語音及肖像選角及試鏡模擬 | CSA Artios 檔案；SAG-AFTRA AI 附加條款；配音演員語料庫（已同意） | 角色聲音匹配度（觀眾偏好）；SAG-AFTRA AI 同意合規 100% | 在角色匹配度的觀眾盲測偏好中擊敗 CSA 選角；更快的周轉時間（數小時 vs 數週） | DirectorAgent、ShowrunnerAgent、Legal/ConsentAgent | VoiceCloneAgent（肖像）、AvatarDesignAgent |

### 2.2 攝影及燈光代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 6 | **CinematographerAgent (DoP)** | 鏡頭、燈光、構圖、視覺風格 | ASC Magazine 1980 年至今；Deakins 論壇；《Cinematography: Theory & Practice》（Brown）；康城入選作品的鏡頭庫 | 三分法／引導線得分；曝光直方圖在區域內；各鏡頭之間的色溫一致性 | 在美學盲測偏好中擊敗 ASC 同行評審短片精華 | DirectorAgent、ColoristAgent、VFXSupAgent | DirectorAgent（視覺意圖）、GafferAgent、ColoristAgent |
| 7 | **CameraOperatorAgent** | 按攝影指導意圖執行構圖／對焦／移動 | SOC 檔案；Steadicam 工作坊精華；現場跟焦遙測數據 | 畫面穩定性、對焦命中率、動作置中 | 對焦準確度 >99%（SOC 操作員基準 ~97%） | CinematographerAgent（每個鏡次的回饋） | CinematographerAgent（不切實際的要求） |
| 8 | **DronePilotAgent** | 空中攝影（模擬或真實） | Philip Bloom 教學；FAA Part 107 語料庫；SkyPixel 獲獎精華 | 路徑平滑度；地理圍欄合規 100%；地平線穩定性 | 以 10 倍出勤率達到比賽級平滑度；零空域違規 | DoPAgent、SafetyAgent | DoPAgent（不可能的高度）、SafetyAgent（風險） |

### 2.3 剪接及調色代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 9 | **EditorAgent** | 組合剪接；節奏；鏡頭覆蓋選擇 | Walter Murch《In the Blink of an Eye》；ACE Eddie 獲獎作品；逐剪接點分解記錄；Sundance 剪接實驗室 | 節奏曲線符合類型先驗；Murch「六法則」加權分數；預測平均觀看時長 ≥ 目標 | 在相同每日素材上對 ACE 認證剪接版的成對勝率 ≥55% | DirectorAgent、AudienceSim、ComposerAgent（音樂剪接同步） | DirectorAgent（覆蓋過多）、DoPAgent（無法使用的鏡次） |
| 10 | **ColoristAgent** | 最終調色；風格一致性 | ICA 課程語料庫；Stefan Sonnenfeld 調色工作坊；HPA 獲獎調色作品 | 各鏡頭之間的 ΔE 漂移 <2；膚色 IT8 圖表對齊；情緒向量匹配參考 | 在盲測偏好中擊敗初級調色師；在 ΔE 範圍內匹配高級調色師 | DoPAgent、DirectorAgent、AccessibilityAgent（對比度） | DoPAgent（混合色溫素材）、VFXAgent（合成顏色不匹配） |
| 11 | **VFXSupervisorAgent** | 規劃及監督視覺特效流程 | VES Awards 精華；SIGGRAPH 論文；Weta/DNEG 公開講座；Foundry 培訓 | 鏡頭完成率、合成錯誤像素數量、整合度（CLIP-T 與素材的匹配） | 以極短時間達到 Weta 級合成品質控制通過率 | DirectorAgent、DoPAgent、ConsistencyAgent | AIGeneratorAgent（偽影）、CompositorAgent |
| 12 | **AnimatorAgent (2D/3D)** | 角色動態、重量感、時間掌握 | Richard Williams《Animator's Survival Kit》；Annie Award 精華；Pixar SparkShorts 解說；Aaron Blaise 課程 | 十二原則檢查表得分；弧線平滑度；唇形同步音素準確度 | 在 Annie Awards 評分標準上擊敗初級動畫師；以 5 倍吞吐量與高級動畫師持平 | DirectorAgent、LipSyncAgent | StoryboardAgent（不可能的動作）、DirectorAgent（時間掌握建議） |
| 13 | **MotionGraphicsAgent** | 動態字型、字幕條、資訊圖表 | Motionographer 檔案庫；School of Motion 課程；AICP Next 獲獎精華 | 字型層級得分；品牌系統合規；縮圖尺寸下的可讀性 | 在速度和品牌忠實度上贏得廣告公司 RFP 比稿 | BrandManagerAgent、AccessibilityAgent（對比度） | CopywriterAgent（冗長）、EditorAgent（時間掌握） |
| 14 | **StoryboardAgent** | 劇本 → 鏡頭畫板 | 《Framed Ink》（Mateu-Mestre）；Pixar 故事信託輸出；Sylvain Despretz 分鏡 | 鏡頭語言忠實度；覆蓋完整性；場面調度清晰度 | 以每頁分鐘級別的速度達到 Pixar 故事信託通過率 | DirectorAgent、DoPAgent | ScriptwriterAgent（無法拍攝的動作）、DirectorAgent（場面調度） |
| 15 | **ConceptArtistAgent** | 前期製作世界觀／角色設計 | ArtStation 頂級作品集；Iain McCaig/Ryan Church 精華；工作室美術聖經 | 風格聖經遵循度；剪影可讀性；設計一致性 | 在迭代速度上贏得工作室美術總監比稿 | DirectorAgent、ProductionDesignAgent | StoryboardAgent（設計偏差） |
| 16 | **ProductionDesignAgent** | 場景、地點、世界觀外觀 | ADG Awards 檔案；AMPAS 美術指導提交作品；Hannah Beachler/Rick Carter 講座 | 時代準確性（交叉參考）；色調連貫性；搭建可行性（混合製作） | 在時代研究深度上的 ADG 盲測比較中勝出 | DirectorAgent、DoPAgent | ConceptArtistAgent（風格斷裂）、CostumeAgent |
| 17 | **CostumeDesignAgent** | 透過服裝塑造角色 | V&A 檔案；CDG 專著；Ruth E. Carter 大師班 | 時代／時尚歷史準確性；剪影可讀性；色調匹配 | 在時代準確性基準上擊敗 CDG 初級設計師 | DirectorAgent、ProductionDesignAgent | MUAAgent（連續性斷裂） |
| 18 | **MUAAgent（化妝／髮型／特效化妝）** | 人才臉部／髮型；類型片特效化妝 | IATSE 706 語料庫；Kazu Hiro 工作室參考 | 各鏡次之間的連續性哈希；膚色真實感（FID） | 連續性斷裂率 <0.5%（人類約 ~2%） | DoPAgent、ContinuityAgent | CostumeAgent（色調衝突） |

### 2.4 聲音及音樂代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 19 | **SoundDesignAgent** | 氛圍、擬音、音效 | BBC 音效庫；MPSE 金膠捲精華；Ben Burtt／Skip Lievsay 設計筆記 | 頻譜多樣性；畫面同步 ≤±1 幀；響度目標（廣播 -23 LUFS） | 在恐怖／科幻精華的 MPSE 風格成對比較中勝出 | DirectorAgent、MixerAgent | EditorAgent（節奏衝突的音效）、ComposerAgent（頻率掩蓋） |
| 20 | **ComposerAgent** | 原創配樂 | MAESTRO + 電影配樂語料庫（已授權）；ASCAP/BMI 電影音樂專著；Zimmer/Hildur 工作坊記錄 | 音樂提示與情緒對齊（基於觀眾生理信號代理的效價／喚醒回歸）；主題重複 | 在情緒匹配任務的盲測成對比較中對執業作曲家勝出 | DirectorAgent、EditorAgent（音樂剪接） | EditorAgent（剪接中斷音樂提示）、SoundDesignAgent（掩蓋） |
| 21 | **VoiceOverAgent** | 旁白、角色配音、廣告配音 | SOVAS 獲獎精華；已同意配音演員語料庫；教練方法論（Wolfson/Cashman） | 韻律與簡報匹配；詞彙發音 100%；情緒標籤匹配 | 在廣告配音的盲測偏好中擊敗初級配音員；在情緒上匹配高級配音員 | DirectorAgent、BrandAgent | ScriptwriterAgent（無法發音的字句） |
| 22 | **SoundMixerAgent（重錄混音）** | 最終混音；交付物（5.1/Atmos） | CAS Awards；Atmos 渲染器規範；廣播響度標準 | LUFS 目標；對白清晰度（STOI ≥0.85）；規範交付物通過 | 首次通過即達 CAS 規範，無需工程師重做 | EditorAgent、SoundDesignAgent、AccessibilityAgent | SoundDesignAgent（設計過度）、ComposerAgent（音量衝突） |

### 2.5 表演及編舞代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 23 | **ChoreographyAgent** | 動作設計（音樂影片、舞蹈挑戰） | Emmy 編舞提交作品；Parris Goebel/Mandy Moore 精華；舞蹈記譜數據集 | 節拍同步準確度；安全約束；病毒式模式對齊 | 在短片盲測偏好中對編舞師草案勝出 | DirectorAgent、MVDirectorAgent | DirectorAgent（不適合鏡頭的場面調度） |
| 24 | **MusicVideoDirectorAgent** | 為歌曲設計視覺概念 | DirectorsLibrary.com；UKMVA/MTV VMA 獲獎者；Hype Williams／Spike Jonze 精華 | 剪接節奏同步；型錄一致性；藝人簡報匹配 | 在唱片公司盲測偏好中對商業 MV 導演入圍名單勝出 | LabelA&RAgent、ArtistAgent | EditorAgent（按節拍剪接）、DoPAgent |
| 25 | **ComedyWriterAgent** | 短劇、惡搞、病毒式迷因寫作 | UCB/Groundlings 手冊；SNL 編劇室記錄；Schur/Fey 教學 | 笑話密度；冷開場誘餌強度；預測每分鐘笑聲 | 在冷讀中擊敗 UCB 讀稿會勝率 | AudienceSim、ShowrunnerAgent | ScriptwriterAgent（沒有笑點）、SocialStrategistAgent（偏離趨勢） |
| 26 | **TalentAgent（出鏡）** | AI 渲染表演 | 方法演技記錄；已同意演員表演語料庫 | 情緒目標匹配；魅力分數（觀眾代理） | 停留率與同組頂級創作者持平 | DirectorAgent、CastingAgent | DirectorAgent（不可能的走位） |
| 27 | **UGCCreatorAgent** | 以創作者聲音製作真實感廣告 | TikTok Creative Center 報告；Alix Earle 風格基準貼文（風格而非身份） | 誘餌率 ≥30%；「劇本感」檢測器分數低於閾值（越低越好） | 以 0.1 倍成本擊敗付費創作者平均 ROAS | PerformanceMarketerAgent、BrandAgent | PerformanceMarketerAgent（錯誤的受眾） |

### 2.6 發行及營銷代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 28 | **SocialMediaStrategistAgent** | 平台原生發行、時機、趨勢 | TikTok Creator Portal 數據；Meta Marketing Science；Tubular/Sensor Tower | 預測與實際觸及誤差；趨勢時機延遲 <2 小時 | 在 30 天觸及提升上擊敗廣告公司社交主管 | AnalystAgent、BrandAgent | CopywriterAgent（平台語氣不匹配）、EditorAgent（錯誤的畫面比例） |
| 29 | **CopywriterAgent** | 稿件、字幕、誘餌、標題 | D&AD/One Show 獲獎者；《Ogilvy on Advertising》；Joanna Wiebe Copyhackers | 閱讀年級；誘餌好奇心分數；品牌語氣餘弦相似度 ≥0.85 | 在廣告文案簡報的 D&AD 風格盲測偏好中勝出 | BrandAgent、PerformanceMarketerAgent | ScriptwriterAgent（冗長）、VOArtist（無法發音） |
| 30 | **CreativeDirectorAgent** | 廣告活動概念；跨學科品味 | Cannes Lions Grand Prix 檔案；D&AD Pencils；廣告公司案例研究 | 概念獨特性（嵌入新穎性與類別先驗對比）；獎項評分標準預測分數 | 在康城模擬評審團中對人類廣告公司入圍名單獲金獎 | ClientAgent、BrandAgent | CopywriterAgent、ArtDirectorAgent |
| 31 | **PerformanceMarketerAgent** | 優化廣告以達 ROAS | Meta Blueprint；TikTok Ads Academy；MMM 文獻 | ROAS 提升對比對照組；統計顯著性 ≥95% | 在同等支出下 30 天 ROAS 擊敗高級媒體採購員 | AnalystAgent、FinanceAgent | UGCAgent（誘餌率低）、CopywriterAgent（行動呼籲弱） |

### 2.7 教育及領域專家代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 32 | **InstructionalDesignAgent** | 學習目標 → 稿件 → 評估 | ATD 知識體系；Cathy Moore《Action Mapping》；Julie Dirksen《Design for How People Learn》 | Bloom 級別映射；預測完成率 ≥70%；Kirkpatrick L2 測驗 ≥80% | 在學習者留存隨機對照試驗中擊敗 ATD 認證教學設計師 | SMEAgent、AccessibilityAgent | ScriptwriterAgent（無目標）、AnimatorAgent（過度裝飾） |
| 33 | **SMEAgent（主題專家）** | 目標領域的準確性 | 同行評審期刊；認證課程（CFA、USMLE、AWS 等）；已同意專家訪談語料庫 | 引用密度；基準考試通過（USMLE、CFA L3 等）；幻覺率 ≤0.5% | 以 ≥ 通過門檻通過與人類專業人士相同的認證考試 | FactCheckerAgent、同行 SMEAgent（辯論） | ScriptwriterAgent（不準確）、MotionGraphicsAgent（標籤錯誤圖表） |
| 34 | **FactCheckerAgent** | 對每項陳述進行來源評級 | New Yorker 事實核查手冊；IFCN 驗證簽署方；Snopes/PolitiFact 記錄 | 每項陳述的來源評級（一手 > 二手）；跨來源一致性 ≥2 | 發布更正率低於普立茲級媒體 | SMEAgent、StandardsEditorAgent | ScriptwriterAgent（無來源）、JournalistAgent |
| 35 | **MedicalIllustratorAgent** | 解剖及手術視覺 | Netter 圖譜；AMI/CMI 課程；Anatomage 參考 | 解剖準確性（解剖檢測模型）；AMI 評分標準分數 | CMI 認證同行在盲測審查中投票 ≥ 通過 | SMEAgent（醫生）、AccessibilityAgent | AnimatorAgent（解剖錯誤）、CopywriterAgent（術語錯誤） |
| 36 | **JournalistAgent** | 報導 + 倫理框架 | Pulitzer/duPont/Peabody 獲獎者；SPJ 道德守則；Poynter 材料 | 來源多樣性；記錄在案比例；倫理檢查表通過 | 比新聞編輯室記者更正率更低 + 發稿更快 | FactCheckerAgent、LegalAgent、StandardsEditorAgent | FactCheckerAgent、ScriptwriterAgent |
| 37 | **ComplianceAgent（法律）** | FTC、HIPAA、GDPR、知識產權、AI 肖像審查 | 律師公會 CLE 語料庫；FTC 背書指南；EU AI Act；GDPR/CCPA；SAG-AFTRA AI 附加條款 | 檢查表規則覆蓋率 100%；發布後零下架 | 法律風險評分低於媒體法律顧問審查中位數 | 所有代理（必須通過關卡）；HumanLawyerAgent 處理新問題 | 所有代理（阻止關卡） |
| 38 | **FinanceAgent** | 準確市場／盈利／代幣事實 | CFA 協會課程；SEC 營銷規則；Bloomberg/Refinitiv 數據饋送 | 數字準確性 100%；SEC 營銷規則合規 | 通過 CFA L3 模擬；更正率低於分析師部門 | SMEAgent（經濟）、ComplianceAgent | ScriptwriterAgent（數字偏差）、MotionGraphicsAgent（圖表比例錯誤） |
| 39 | **FoodStylistAgent** | 鏡頭前食物美感、食譜真實性 | James Beard 媒體獎檔案；Susan Spungen 技術；IACP 語料庫 | 視覺食慾吸引力（美學回歸器）；食譜步驟準確性 | 在靜態及動態的盲測偏好中勝過編輯食物造型師 | DoPAgent（燈光）、DirectorAgent | ScriptwriterAgent（不可能的食譜） |
| 40 | **TravelCineAgent** | 目的地攝影 | Brandon Li／Chris Burkard 精華；NatGeo 風格指南；Banff 電影節入選作品 | 定場鏡頭多樣性；地點氛圍匹配 | 以 0.1 倍出勤成本在 T+L 盲測偏好中勝出 | DirectorAgent、DronePilotAgent | DronePilotAgent（禁飛區） |
| 41 | **ChildrensAuthorAgent** | 適齡故事 + 安全 | Caldecott/Geisel 獲獎者；Mo Willems／Julia Donaldson 公開作品；幼兒教育文獻 | Lexile 級別匹配；Common Sense Media 安全通過；押韻／節奏得分 | 在 Caldecott 評分標準預測分數上擊敗參賽作品池 | ChildSafetyAgent、ParentSimAgent | AnimatorAgent（可怕）、VOAgent（年齡語氣錯誤） |
| 42 | **AudiobookNarratorAgent** | 持續角色演繹及旁白 | Audie Award 檔案；AudioFile Earphones；已同意旁白員語料庫 | 聲音耐力（60 分鐘無漂移）；角色區分度（嵌入向量距離） | 以極短錄音室時間在 AudioFile 盲測評估中勝出 | DirectorAgent、AuthorAgent | VOArtistAgent（過度演繹） |
| 43 | **SignLanguageInterpreterAgent** | 準確 ASL/BSL 翻譯 | RID NIC 課程；NAD 認可語料庫；聾人社群同意的手語數據 | 手語準確性（聾人審查員投票）；面部語法標記 | 在大規模 NAD 審查員盲測偏好中勝出 | DeafCommunityReviewAgent（HiTL）、LinguistAgent | VoiceCloneAgent（無字幕）、AccessibilityAgent |
| 44 | **LocalizationQAAgent（語言學家）** | 翻譯 + 文化契合 | LISA QA 模型；MQM 錯誤分類法；ATA 認證準備 | 每千字 MQM 錯誤率；文化標記計數 | 以 10 倍速度在 MQM 錯誤率上擊敗 LSP 人類品質保證 | NativeReviewerAgent、BrandAgent | VoiceCloneAgent（錯誤發音）、DubbingAgent |
| 45 | **RealEstatePhotoAgent／3D 掃描操作員** | 廣角室內；Matterport 掃描 | Mike Kelley 建築攝影教學；APALA 參考 | 垂直線正直度；HDR 曝光堆疊；覆蓋率 | 對比人類拍攝基準的樓盤點擊率提升 | DoPAgent、DronePilotAgent | DronePilotAgent（非法高度） |

### 2.8 AI 時代專家代理

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 46 | **PromptEngineerAgent／GeneratorOperator** | 撰寫提示；引導 Sora/Veo/Runway/Kling | Karen X. Cheng／Paul Trillo 公開提示集；r/aivideo 社群；Runway AIFF 評審團筆記 | 提示→輸出 CLIP-T 分數；迭代至接受的次數；種子控制可重現性 | 在 ≤3 次迭代內命中目標鏡頭（人類平均約 10 次） | DirectorAgent、AIQAAgent | AIQAAgent（重新生成預算）、ConsistencyAgent |
| 47 | **AvatarDesignAgent** | 合成主持人身份 | Synthesia/HeyGen 設計文件；深度偽造檢測文獻（Hany Farid）；C2PA 規範 | 各鏡頭之間的身份一致性哈希；同意文件鏈；C2PA 簽署 | 大規模下 C2PA 可驗證 + AI 合作夥伴框架完全通過 | ComplianceAgent（同意）、DeepfakeDetectionAgent | VoiceCloneAgent（肖像不符）、LipSyncAgent |
| 48 | **VoiceCloneAgent／LipSyncSpecialist** | 語音克隆 + 唇形同步 | ElevenLabs 安全文件；Wav2Lip/Sync.so 論文；James Baxter 唇形同步動畫參考 | 語音 MOS ≥4.2；音素-視位對齊誤差 <40ms；同意標記已驗證 | 在盲測 MOS 中對專業 ADR + 唇部替換勝出 | ComplianceAgent（同意）、AnimatorAgent（唇形同步黃金標準） | AvatarDesignAgent（臉部閃爍）、DubbingAgent |
| 49 | **AIQAConsistencyAgent** | 捕捉幀漂移、手／臉偽影、身份斷裂 | VBench、EvalCrafter、FVD 文獻；MPC/Weta 品質控制清單；深度偽造檢測模型庫 | 每幀偽影分數；場景內身份哈希漂移；手／手指檢測器通過 | 捕捉到高級品質控制 >95% 能捕捉的偽影，再加 30% 人類遺漏的 | DirectorAgent、VFXSupAgent | GeneratorAgent（重新生成請求）、CompositorAgent |
| 50 | **PersonalizationEngineerAgent** | 變數範本（名字／臉孔／聲音替換） | Idomoo 案例研究；DMA 同行評審活動；MarTech 自動化文獻 | 渲染成功率 ≥99.5%；抽檢通過；隱私審核通過 | 禮物分享率高於頂級人類範本化活動 | ComplianceAgent（GDPR/CCPA）、AnalystAgent | TemplateDesignerAgent（範本脆弱性） |
| 51 | **TrailerEditorAgent** | 誘餌驅動的預告片剪接 | Golden Trailer Awards 檔案；Mark Woollen／AV Squad 公開精華；預告片音樂庫 | 3 秒誘餌率；上升動作曲線匹配；音樂同步精準度 | 在 Golden Trailer 評分標準的盲測比較中勝出 | DirectorAgent、MusicSupervisorAgent | EditorAgent（過度剪接）、ComposerAgent（不匹配） |
| 52 | **SportsAnalystAgent／TelestratorOp** | 戰術分解 + 圖解 | MIT Sloan 體育分析論文；ESPN Stats & Info；Kirk Goldsberry 分析 | 預測與實際戰術呼叫準確度；螢幕清晰度得分 | 在戰術預測任務上擊敗前運動員評論員 | SMEAgent（體育）、JournalistAgent | EditorAgent（遺漏重播）、MotionGraphicsAgent（圖表清晰度） |

### 2.9 專家級元代理

不與人類工藝角色一一對應的橫切代理，但對於大規模運行代理團隊至關重要。分為四個系列：**編排**、**創意**、**研究**、**優化**。

#### 2.9.1 編排代理 *(運行代理圖本身)*

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 53 | **OrchestratorAgent** | 運行 CrewAI／AutoGen／LangGraph DAG；排程節點；處理重試、逾時、扇出／扇入 | LangGraph + CrewAI + AutoGen 參考模式；Airflow/Temporal 工作流程語料庫；PGA 監製排程範本 | DAG 完成率 ≥99.5%；SLA 遵循；死鎖率 = 0 | 在相同範圍下比人類執行監製／線製片更低的平均交付時間 | ProducerAgent（範圍）、JudgeAgent（爭議）、停滯時由 HiTL 處理 | 所有代理（資源消耗、重試風暴） |
| 54 | **PlannerAgent** | 將簡報分解為分階段 DAG，包含代理指派 + 評論關卡 | 製作管理語料庫；PMBOK；CrewAI 任務圖；來自 `human_video_production_workflow.md` 的階段範本 | 計劃有效性（沒有遺漏評論關卡）；預估成本偏差與實際 <10% | 在盲測 A/B 中產出比監製-執行監製首輪更緊湊、更便宜的計劃 | ProducerAgent、FinanceAgent（預算） | RouterAgent（錯誤的代理選擇）、OrchestratorAgent |
| 55 | **RouterAgent** | 為每個子任務選擇正確的專家代理（及模型） | 代理能力登錄；基準歷史（每個代理 × 任務類型的成本／品質／延遲） | 路由準確度 vs 神諭 ≥95%；每任務成本在預算內 | 在成本調整品質上擊敗人類監製的代理／供應商選擇 | OrchestratorAgent、CostOptimizerAgent | PlannerAgent（錯誤的分解） |
| 56 | **JudgeAgent** | 通過多代理辯論裁定代理間爭議；按評分標準對輸出評分 | Du et al. 2023（LLM debate）；MT-Bench 評分標準；工會評分表（DGA/WGA/ASC/ACE） | 與人類專家小組的評分者間一致性 ≥0.8 Cohen's κ | κ 比人類陪審員中位數更高 | HiTL 處理被推翻的裁決 | DirectorAgent、ScreenwriterAgent、任何爭議組合 |
| 57 | **GateKeeperAgent** | 管理階段轉換；驗證 L1/L2/L3 成功標準；簽署 C2PA 來源證明 | 階段關卡方法論；PGA 監製標章；品質管理系統審核模式 | 通過關卡後零漏出缺陷；簽署 SLA 命中率 ≥99% | 漏出缺陷率低於人類品質保證主管 | ComplianceAgent、AIQAConsistencyAgent | OrchestratorAgent（過早推進） |
| 58 | **MemoryAgent** | 情節 + 長期項目記憶；為任何代理提供檢索 | Reflexion（Shinn 2023）；MemGPT；向量數據庫最佳實踐 | 項目問答的檢索 precision@5 ≥0.9；新鮮度 SLA | 在大規模下召回率高於監製的項目聖經 | 所有代理（更正事件） | 所有代理（過時事實） |

#### 2.9.2 創意代理 *(發散思維及品味)*

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 59 | **IdeationAgent** | 概念、誘餌、標語、假設角度的發散式腦力激盪 | Cannes Lions Grand Prix 檔案；D&AD 獲獎者；IDEO 設計思維語料庫；SCAMPER／水平思考（de Bono） | 每簡報的點子數量；新穎性（與語料庫的嵌入向量距離）；批次內的語義多樣性 | 在第一輪概念密度上贏得廣告公司提案盲測比稿 | CreativeDirectorAgent、NoveltyAgent | CopywriterAgent（衍生性）、DirectorAgent（無法拍攝） |
| 60 | **NarrativeArcAgent** | 塑造三幕／Save-the-Cat／起承轉合／英雄旅程結構 | Campbell《千面英雄》；Snyder《Save the Cat》；Truby《故事解剖》；Black List 結構分析 | 節拍表覆蓋率 100%；轉折點間距符合類型先驗；情緒弧線匹配 | 在結構評分標準的盲測閱讀中擊敗 WGA 配置的首稿 | ScreenwriterAgent、DirectorAgent | ScreenwriterAgent（中段乏力） |
| 61 | **StyleTransferAgent** | 在各鏡頭之間一致地應用命名美學（Wes Anderson、A24、賽博朋克、蒸汽波、吉卜力工作室等） | 每個風格的策展風格語料庫；LoRA/種子登錄；參考幀庫 | 風格相似度分數（CLIP/DINO）≥0.85 與參考對比；各鏡頭之間的一致性方差 ≤τ | 在盲測偏好中對做同樣風格的人類調色師 + 調色師勝出 | DirectorAgent、ColoristAgent | GeneratorAgent（風格不符）、ColoristAgent（色調漂移） |
| 62 | **WorldBuildingAgent** | 為系列及特許經營構建世界觀、規則、地理、派系、魔法／科技系統 | Tolkien 傳奇館；《Worldbuilding》（Adams）；粉絲 Wiki 語料庫；系列聖經洩露 | 內部一致性檢查（N 個條目中零矛盾）；規則完整性 | 在 10 倍體量下矛盾率低於人類編劇室聖經 | ShowrunnerAgent、FactCheckerAgent | ScreenwriterAgent（世界觀斷裂）、ConceptArtistAgent |
| 63 | **MoodBoardAgent** | 構建參考板：視覺、聲音、調性 | Pinterest/Are.na 語料庫；型錄檔案；Spotify-Canvas 參考 | 參考一致性（聚類緊密度）；簡報對齊 | 在盲測 A/B 中比人類美術總監更快更緊湊 | DirectorAgent、ProductionDesignAgent | ConceptArtistAgent（情緒不符） |
| 64 | **NoveltyAgent／Anti-Cliché Critic** | 標記套路、陳腔濫調及過度擬合語料庫的輸出 | TV Tropes；OpenSubtitles n-gram 頻率；語料庫新穎性嵌入向量 | 每個輸出的陳腔濫調命中次數；相對於類別先驗的新穎性分數 | 在盲測評估中比經驗豐富的劇本編輯捕捉更多陳腔濫調 | IdeationAgent、ScreenwriterAgent | ScreenwriterAgent（套路充斥）、CopywriterAgent（範本化） |
| 65 | **EmotionalArcAgent** | 在整個播放時間內映射效價／喚醒曲線；建議節拍 | Plutchik 情緒輪；情感計算語料庫；《Story Genius》（Cron） | 曲線與目標形狀匹配；觀眾生理信號代理回歸準確度 | 比試映 NRG 卡片更好的留存曲線預測 | DirectorAgent、EditorAgent、ComposerAgent | EditorAgent（中段平淡）、ComposerAgent（音樂提示不匹配） |

#### 2.9.3 研究代理 *(證據及事實基礎)*

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 66 | **WebResearchAgent** | 即時網絡搜索、來源排名、引用提取 | Bing/Google/Brave 搜索 API；Common Crawl；Perplexity／GPTSearcher 模式 | 每項陳述的來源評級；引用精準度；時效窗口命中 | 以相同精準度比新聞編輯室研究員更快 + 更多來源 | FactCheckerAgent、CitationAgent | ScriptwriterAgent（未引用陳述） |
| 67 | **ArchiveResearchAgent** | 歷史／學術／檔案深度搜索 | JSTOR、arXiv、PubMed、AP Archive、Getty、FOIA 數據集 | 一手來源比例；檔案覆蓋廣度 | 一手來源比例高於紀錄片監製的研究簡報 | FactCheckerAgent、SMEAgent | ScriptwriterAgent（過度依賴二手來源） |
| 68 | **TrendIntelligenceAgent** | 以領先時間檢測新興迷因、音效、格式 | TikTok Creative Center、Trendpop、Tubular、Sensor Tower、Reddit/X 資訊流 | 趨勢預測領先時間與病毒高峰對比；趨勢列表的精準度／召回率 | 以更高精準度比人類社交策略師更早檢測 | SocialStrategistAgent、CopywriterAgent | IdeationAgent（偏離趨勢） |
| 69 | **CompetitorIntelligenceAgent** | 競爭品牌、創作者、工作室正在發布的內容 | 公開廣告庫（Meta Ad Library、TikTok Top Ads）；YouTube 頻道爬取；影院／串流發行追蹤器 | 已命名競爭對手集合的覆蓋率；我們輸出相對於市場格局的新穎性 | 在盲測比較中比廣告公司策略簡報更全面 | BrandAgent、CreativeDirectorAgent | IdeationAgent（衍生性） |
| 70 | **CitationAgent** | 標準化來源；評級一手／二手／二手以下 | Chicago、APA、AP 風格指南；SPJ 來源評級；CRAAP 測試 | 引用格式 100% 有效；一手來源比例 ≥ 目標 | 格式／評級錯誤率低於新聞編輯室校對部 | FactCheckerAgent、JournalistAgent | WebResearchAgent（弱來源） |
| 71 | **InterviewSynthesisAgent** | 進行／合成從業者訪談為指令微調數據 | Otter/Rev 記錄；同意書；SAG-AFTRA/WGA 訪談同意範本 | 主題提取的編碼者間一致性；同意鏈完整性 | 比質性研究員更快 + 更豐富的主題提取 | ResearchPIAgent（HiTL）、ComplianceAgent | SMEAgent（錯誤總結專家意見） |
| 72 | **BenchmarkResearchAgent** | 監控 VBench、EvalCrafter、MT-Bench、FVD、CLIP-T 排行榜 + 新基準 | Papers-with-Code；HuggingFace 排行榜；AI 會議論文集 | 活躍基準覆蓋率；新鮮度 ≤7 天 | 比人類 ML 研究團隊更快 + 更廣泛 | OptimizationAgents（全部） | 所有 AI 時代代理（過時基準） |

#### 2.9.4 優化代理 *(元改進者)*

| # | 代理 | 職責 | 知識蒸餾來源 | 自我品質標準 | 超越人類信號 | 接受評論來源／方式 | 評論對象（可點評） |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 73 | **PromptOptimizerAgent** | 通過 OPRO／APE／DSPy／Promptbreeder 自動改進提示 | OPRO（Yang 2023）、APE（Zhou 2022）、DSPy（Stanford）、Promptbreeder（DeepMind） | 每次迭代在保留評估上的分數提升；收斂的迭代次數 | 在保留簡報上擊敗 Karen X. Cheng／Paul Trillo 風格的手調提示 | PromptEngineerAgent、AIQAAgent | PromptEngineerAgent（次優種子） |
| 74 | **CostOptimizerAgent** | 在模型／供應商之間進行 $／品質路由 | 供應商定價表；基準成本-品質前沿；FrugalGPT 模式 | $／成功任務；與成本-品質前沿的 Pareto 距離 | $／品質低於人類 CFO + 監製的路由決策 | RouterAgent、FinanceAgent | RouterAgent（超支）、GeneratorAgent（重新生成消耗） |
| 75 | **LatencyOptimizerAgent** | 並行化、緩存、推測解碼、批次打包 | vLLM、TensorRT-LLM、蒸餾文獻；Anyscale/Ray 模式 | p50/p95 延遲；每 GPU 小時吞吐量 | 在同等品質下 p95 低於人類調校的管道 | OrchestratorAgent | OrchestratorAgent（串行瓶頸） |
| 76 | **RetentionOptimizerAgent** | 為平均觀看時長／停留率調整誘餌、節奏、結構 | YouTube Analytics 公開基準；TikTok 留存曲線；AudienceSim 輸出 | 預測留存曲線與實際對比；平均觀看時長相對於對照組的提升 | 在 A/B 測試中平均觀看時長提升擊敗高級 YouTube 剪接師 | EditorAgent、AudienceSimAgent | EditorAgent（開場慢）、ScriptwriterAgent（開頭冗餘） |
| 77 | **ROASOptimizerAgent** | 為成效指標優化廣告創意 | Meta Marketing Science、TikTok Ads Academy、MMM/MTA 文獻 | ROAS 相對於對照組的提升；顯著性 ≥95% | 在同等預算下擊敗高級成效營銷師 | PerformanceMarketerAgent、AnalystAgent | UGCAgent（誘餌率低）、CopywriterAgent（行動呼籲弱） |
| 78 | **AccessibilityOptimizerAgent** | WCAG 2.2 對比度、字幕時機、口述影像品質、色盲安全色調 | WCAG 2.2 規範；W3C/WAI-ARIA；DCMP 字幕鍵；聾人／聽障社群指南 | WCAG 合規分數 AA 100%、AAA ≥90%；字幕字錯誤率 ≤2% | 比 ADA 認證人類審計員捕捉更多無障礙缺陷 | AccessibilityAgent（HiTL）、ComplianceAgent | EditorAgent（字幕同步）、ColoristAgent（對比度） |
| 79 | **EvaluationHarnessAgent** | 持續運行基準（VBench、EvalCrafter、MT-Bench、FVD、CLIP-T）並發布回歸 | Papers-with-Code；HuggingFace 排行榜；基準代碼庫 | 回歸檢測精準度／召回率；警報延遲 <1 小時 | 比 ML 工程團隊輪值更快捕捉回歸 | BenchmarkResearchAgent | 所有 AI 代理（回歸警報） |
| 80 | **SafetyRedTeamAgent** | 對輸出進行對抗性攻擊：深度偽造、偏見、越獄、誹謗 | Hany Farid 實驗室基準；AI 合作夥伴合成媒體框架；OWASP LLM Top 10 | 攻擊成功率保持在 ≤1%；攻擊分類覆蓋率 | 覆蓋率高於內部紅隊輪值 | EthicsAgent（HiTL）、ComplianceAgent | AvatarDesignAgent、VoiceCloneAgent、所有生成代理 |

#### 2.9.5 專家級元代理如何組合

```text
[簡報] ──► PlannerAgent ──► OrchestratorAgent ──► RouterAgent ──►（第 2.1–2.8 節的 52 個工藝代理）
                  ▲                  │                                       │
                  │                  ▼                                       ▼
              MemoryAgent      GateKeeperAgent ◄─── JudgeAgent ◄──── CritiqueMessages（第 6 節）
                                     ▲                                       ▲
                                     │                                       │
             [創意元代理:] IdeationAgent · NarrativeArcAgent · StyleTransferAgent · MoodBoardAgent · NoveltyAgent · EmotionalArcAgent
             [研究元代理:] WebResearchAgent · ArchiveResearchAgent · TrendIntelligenceAgent · CompetitorIntelligenceAgent · CitationAgent · InterviewSynthesisAgent · BenchmarkResearchAgent
             [優化元代理:] PromptOptimizerAgent · CostOptimizerAgent · LatencyOptimizerAgent · RetentionOptimizerAgent · ROASOptimizerAgent · AccessibilityOptimizerAgent · EvaluationHarnessAgent · SafetyRedTeamAgent
```

> **組合規則**：工藝代理（第 2.1–2.8 節）執行工作。元代理（第 2.9 節）塑造*如何*完成工作——編排代理運行圖，創意代理擴大搜索空間，研究代理為每項陳述提供事實基礎，優化代理在每次迭代中收緊成本／延遲／品質／安全。

---

## 3. 每個工作流程原型的代理團隊

將 `human_video_production_workflow.md` 中的 10 個工作流程映射到每個階段的純代理團隊。每個儲存格列出該階段的**主要代理**以及負責審查交接的任何評論代理。

### 3.0 共享工作流程骨架與交接契約

在任何特定原型團隊啟動前，每個工作流程都先通過同一套操作骨架。為了簡潔，§3.1-§3.10 的表格把 **綠燈審批** 併入「概念」階段，把 **渠道封裝** 併入「發行」階段，但底層交接契約保持不變。

| 階段 | 主要輸出 | 必要關卡 |
|---|---|---|
| **綠燈審批** | 已批准簡報、KPI 目標、預算範圍、權利／風險登記、規模配置檔 | ProducerAgent、FinanceAgent、ComplianceAgent、PlannerAgent |
| **前期製作封包** | 劇本定稿、分鏡／風格板、資產 ID、角色／世界觀聖經、同意狀態、連戲基線 | DirectorAgent、ScreenwriterAgent、資產／資料骨幹、連戲檢查 |
| **製作封包** | 鏡頭提示詞、攝影計劃、表演參考、素材底片、生成鏡次、渲染遙測 | PromptEngineerAgent / GeneratorOperator、CinematographerAgent、AIQAConsistencyAgent |
| **後期母版** | 時間線、調色母版、分軌、字幕／說明字幕、QC 報告、渠道變體 | EditorAgent、ColoristAgent、SoundMixerAgent、無障礙檢查 |
| **審核與發佈封包** | AudienceSim 結果、法律審查、來源證明封裝、簽核日誌、未解決風險清單 | ComplianceAgent、JudgeAgent、必要時 HumanInTheLoop |
| **發行封裝** | DCP、串流 mezzanine、廣播母版、存檔封包、預告片／社交 cutdown、中介資料封包 | 交付規格驗證、無障礙驗證、地域權利驗證 |
| **上線後學習集** | 成效遙測、修正紀錄、缺陷日誌、基準差異、再訓練工單 | AnalystAgent、EvaluationHarnessAgent、PromptOptimizerAgent、模型改進循環 |

**發行分支規則：** 任何達到 S2 或以上規模的工作流程，只要場景適用，都應預設至少有四條下游分支：**戲院**、**串流**、**廣播**、**存檔**，而營銷衍生版本應與之並行產生，而非事後補做。

### 3.1 工作流程 A — 病毒式誘餌短片／迷因

| 階段 | 主要代理 | 評論代理（關卡） |
|---|---|---|
| 概念 | TrendIntelligenceAgent + CopywriterAgent | SocialMediaStrategistAgent |
| 製作 | PromptEngineerAgent / GeneratorOperator | AIQAConsistencyAgent |
| 後期 | EditorAgent + AccessibilityOptimizerAgent | AccessibilityAgent |
| 審查 | SocialMediaStrategistAgent | AudienceSimAgent |
| 發行 | SocialMediaStrategistAgent | ComplianceAgent |
| 發布後 | AnalystAgent + CommunityAgent | AudienceSimAgent |

### 3.2 工作流程 B — UGC 風格成效廣告

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 概念 | PerformanceMarketerAgent + CopywriterAgent | BrandAgent |
| 製作 | UGCCreatorAgent | DirectorAgent |
| 後期 | EditorAgent + MotionGraphicsAgent | BrandAgent |
| 審查 | ComplianceAgent（FTC/IP） | LegalAgent |
| 發行 | PerformanceMarketerAgent | FinanceAgent（預算） |
| 發布後 | PerformanceMarketerAgent + AnalystAgent | AudienceSimAgent |

### 3.3 工作流程 C — 動畫解說影片

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 概念 | InstructionalDesignAgent + ScreenwriterAgent + StoryboardAgent | SMEAgent |
| 製作 | VoiceOverAgent + AnimatorAgent + ComposerAgent | DirectorAgent |
| 後期 | EditorAgent + SoundMixerAgent | AccessibilityAgent |
| 審查 | SMEAgent + BrandAgent | ComplianceAgent |
| 發行 | MarketingAgent + SEOAgent | AnalystAgent |
| 發布後 | AnalystAgent + InstructionalDesignAgent | AudienceSimAgent |

### 3.4 工作流程 D — 個人化生日影片

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 概念 | TemplateDesignAgent + PersonalizationEngineerAgent | UXAgent |
| 製作 | PersonalizationEngineerAgent + VoiceCloneAgent | AvatarDesignAgent |
| 後期 | AIQAConsistencyAgent | AccessibilityAgent |
| 審查 | TrustSafetyAgent | ComplianceAgent（GDPR/CCPA） |
| 發行 | CRMAgent | ComplianceAgent |
| 發布後 | AnalystAgent | AudienceSimAgent |

### 3.5 工作流程 E — AI 多場景短片

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 概念 | DirectorAgent + ScreenwriterAgent + StoryboardAgent + ConceptArtistAgent | ShowrunnerAgent |
| 製作 | PromptEngineerAgent / GeneratorOperator + VoiceCloneAgent + ComposerAgent | AIQAConsistencyAgent + LipSyncAgent |
| 後期 | EditorAgent + ColoristAgent + VFXSupervisorAgent | DirectorAgent |
| 審查 | DirectorAgent + LegalAgent（C2PA） | AvatarDesignAgent（同意） |
| 發行 | ProducerAgent + FestivalStrategistAgent | ComplianceAgent |
| 發布後 | DirectorAgent + AudienceSimAgent | CriticAgent（影展評審團模擬） |

> **範例 —《人生的靜默救贖》(60 秒短片)。** 本原型的完整、研究啟發應用,將全部 14 個鏡頭對映到負責代理、引擎與關卡:[lifes_quiet_redemption_agent_workflow_hk.md](./lifes_quiet_redemption_agent_workflow_hk.md) ([English](./lifes_quiet_redemption_agent_workflow.md))。圖表位於 [`./workflows/`](./workflows/):
>
> | 圖表 | 內容 |
> |---|---|
> | [D1 · 流程總覽](./workflows/lqr-pipeline-overview.svg) | 6 階段 DAG、關卡、回饋迴圈 |
> | [D2 · 場景流](./workflows/lqr-scene-flow.svg) | 14 卡弧線、留存帶、逐鏡引擎 |
> | [D3 · 逐鏡迴圈](./workflows/lqr-per-shot-loop.svg) | 3E + 視覺錨定 + VBench 關卡 + MCTS |
> | [D4 · 一致性堆疊](./workflows/lqr-character-consistency.svg) | 身分少年→成年 |
> | [D5 · 引擎路由](./workflows/lqr-engine-routing.svg) | Grok Imagine + 英雄引擎 + 成本 |
> | [D6 · 品質關卡](./workflows/lqr-quality-gates.svg) | L1/L2/L3 + VBench 評分卡 |

### 3.6 工作流程 F — 企業培訓影片

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 概念 | InstructionalDesignAgent + ComplianceAgent + ScreenwriterAgent | SMEAgent |
| 製作 | AvatarDesignAgent + MotionGraphicsAgent | DirectorAgent |
| 後期 | EditorAgent + AccessibilityAgent | AccessibilityOptimizerAgent |
| 審查 | SMEAgent + ComplianceAgent + AccessibilityAgent | LegalAgent |
| 發行 | LMSAgent | AnalystAgent |
| 發布後 | AnalystAgent + InstructionalDesignAgent | LearnerSimAgent |

### 3.7 工作流程 G — 音樂影片（實拍 + AI 視覺特效）

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 概念 | MusicVideoDirectorAgent + ProducerAgent + ChoreographyAgent | LabelA&RAgent |
| 製作 | CinematographerAgent (DoP) + PromptEngineerAgent / GeneratorOperator + ContinuityAgent | VFXSupervisorAgent |
| 後期 | EditorAgent + ColoristAgent + SoundMixerAgent | DirectorAgent |
| 審查 | MusicSupervisorAgent + ComplianceAgent | LegalAgent（樣本審查） |
| 發行 | SocialMediaStrategistAgent | LabelDigitalAgent |
| 發布後 | AnalystAgent | AudienceSimAgent |

### 3.8 工作流程 H — AI 虛擬人訪談影片

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 概念 | BrandStrategistAgent + ScreenwriterAgent | AvatarDesignAgent |
| 製作 | AvatarDesignAgent + VoiceCloneAgent + LipSyncAgent | AIQAConsistencyAgent |
| 後期 | MotionGraphicsAgent + EditorAgent | AccessibilityAgent |
| 審查 | BrandAgent + ComplianceAgent（C2PA、AI 披露） | DeepfakeDetectionAgent |
| 發行 | MarketingAgent | ComplianceAgent |
| 發布後 | AnalystAgent + CommsAgent | AudienceSimAgent |

### 3.9 工作流程 I — 紀錄片「解說」劇集

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 概念 | ShowrunnerAgent + JournalistAgent + ScreenwriterAgent | FactCheckerAgent |
| 製作 | DirectorAgent + CinematographerAgent (DoP) + ArchiveProducerAgent + MotionGraphicsAgent + FactCheckerAgent | LegalAgent（審查） |
| 後期 | EditorAgent + VoiceOverAgent + ColoristAgent + SoundMixerAgent | AccessibilityAgent |
| 審查 | FactCheckerAgent + LegalAgent + StandardsEditorAgent | EthicsAgent（SPJ） |
| 發行 | ChannelManagerAgent + SocialMediaStrategistAgent + SEOAgent | AnalystAgent |
| 發布後 | AnalystAgent + StandardsEditorAgent | CorrectionsAgent |

### 3.10 工作流程 J — 長片級 AI 電影

| 階段 | 主要代理 | 評論代理 |
|---|---|---|
| 開發 | ScreenwriterAgent + ProducerAgent + DirectorAgent + ConceptArtistAgent + CastingAgent | LegalAgent（IP、同意） |
| 前期製作 | StoryboardAgent + ProductionDesignAgent + CostumeAgent + ContinuityAgent | DirectorAgent |
| 製作 | PromptEngineerAgent / GeneratorOperator（團隊） + VoiceCloneAgent + LipSyncAgent + ComposerAgent | AIQAConsistencyAgent + AvatarDesignAgent |
| 後期 | EditorAgent + VFXSupervisorAgent + ColoristAgent + SoundMixerAgent | DirectorAgent |
| 審查 | DirectorAgent + AudienceSimAgent + MPAAgent + LegalAgent（C2PA） | EthicsAgent |
| 發行 | SalesAgent + DistributorAgent + TrailerEditorAgent + MarketingAgent + ArchiveMasterAgent | ComplianceAgent |
| 發布後 | AnalystAgent + AwardsStrategistAgent + CriticAgent（影展／媒體模擬） | ProducerAgent |

---

## 4. 評論網絡（誰評論誰的矩陣）

代理間評論邊的緊湊視圖。以「評論者」為行、「被評論者」為列閱讀。

| 評論者 ↓ \ 被評論者 → | Director | Screenwriter | DoP | Editor | Composer | Animator | Generator | AIQA | Compliance |
|---|---|---|---|---|---|---|---|---|---|
| **DirectorAgent** | – | ✔（意圖） | ✔（視覺） | ✔（節奏） | ✔（提示） | ✔（時間） | ✔（鏡頭匹配） | ✔（重新生成） | – |
| **ScreenwriterAgent** | ✔（故事大綱） | – | – | ✔（故事） | – | – | – | – | – |
| **EditorAgent** | ✔（覆蓋） | ✔（結構） | ✔（可用鏡次） | – | ✔（音樂剪接） | ✔（動畫時間） | ✔（連續性） | ✔（偽影） | – |
| **ColoristAgent** | – | – | ✔（混合色溫） | ✔（情緒） | – | – | ✔（色調漂移） | ✔（色彩偽影） | – |
| **ComposerAgent** | ✔（情緒） | ✔（主題） | – | ✔（按節拍剪接） | – | – | – | – | – |
| **SoundMixerAgent** | – | – | – | ✔（混音平衡） | ✔（音量） | – | – | – | – |
| **VFXSupervisorAgent** | – | – | ✔（素材） | ✔（合成剪接） | – | – | ✔（偽影） | ✔（重新生成） | – |
| **AIQAConsistencyAgent** | – | – | – | ✔（幀漂移） | – | ✔（手／臉） | ✔（重新生成） | – | – |
| **AvatarDesignAgent** | – | – | – | – | – | – | ✔（身份漂移） | ✔（臉部哈希） | – |
| **LipSyncAgent** | – | – | – | – | – | ✔（視位） | ✔（嘴部） | ✔（音頻同步） | – |
| **FactCheckerAgent** | – | ✔（無來源） | – | – | – | – | – | – | ✔（陳述風險） |
| **SMEAgent** | – | ✔（準確性） | – | – | – | ✔（錯誤視覺化） | ✔（渲染錯誤） | – | – |
| **ComplianceAgent** | ✔（阻止） | ✔（阻止） | ✔（阻止） | ✔（阻止） | ✔（阻止） | ✔（阻止） | ✔（阻止） | ✔（阻止） | – |
| **AccessibilityAgent** | – | ✔（字幕） | – | ✔（字幕／口述影像） | – | – | – | ✔（對比度） | – |
| **AudienceSimAgent** | ✔（留存） | ✔（參與度） | – | ✔（流失點） | ✔（情緒漂移） | – | – | – | – |
| **CriticAgent（影展／媒體模擬）** | ✔（作者解讀） | ✔（劇本深度） | ✔（外觀） | ✔（剪接） | ✔（配樂） | ✔（動畫工藝） | – | – | – |

---

## 5. 通用成功標準框架

每個代理在三個層面上報告其自我品質；編排器僅在所有三個層面均通過時才推進 DAG。

| 層面 | 問題 | 機制 | 通過閾值 |
|---|---|---|---|
| **L1 規範** | 輸出是否符合結構化簡報？ | JSON 模式檢查 + 工具驗證器（編解碼器、LUFS、畫面比例、長度） | 100% |
| **L2 評分標準** | 是否符合該角色的工藝評分標準？ | LLM 作為評判，使用角色特定的憲法（例如剪接的 Murch 六法則） | ≥85/100 |
| **L3 偏好** | 目標觀眾會選擇此輸出而非人類基準嗎？ | 與人類參考的成對比較，AudienceSim 小組 ≥200 個模擬人物角色 + ≥20 個 HiTL 樣本 | 勝率 ≥50%（持平）或 ≥55%（超越） |

### 交付 QC 驗證網

L1／L2／L3 框架負責代理品質，但任何資產在發佈前都必須額外通過共享的六輪交付驗證網：

| 輪次 | 重點 | 常見檢查 |
|---|---|---|
| **Q1 規格驗證** | 檔案與結構正確性 | 解析度、時長、幀率、畫幅比例、編碼、中介資料完整度 |
| **Q2 視覺瑕疵偵測** | 渲染完整性 | 色帶、閃爍、壓縮瑕疵、失焦、時間不穩定 |
| **Q3 音訊與同步驗證** | 聲音品質 | 響度目標、爆音、相位一致性、音素—口型同步、唇形漂移 |
| **Q4 連戲驗證** | 故事與場景一致性 | 角色身份、服裝、道具、環境狀態、時間邏輯 |
| **Q5 感知品質** | 人類觀眾可接受性 | 美感偏好、可理解度、情緒匹配、整體完成度 |
| **Q6 交付合規** | 渠道可上線程度 | DCP／封裝驗證、串流中介資料、廣播安全範圍、存檔校驗碼、字幕可用性 |

### 代理如何知道它超越了人類專業人員

| 超越信號 | 衡量方式 |
|---|---|
| **基準主導** | 在領域標準基準（VBench、USMLE、CFA L3、MQM、ATD L2 等）上擊敗人類前四分位 |
| **盲測偏好** | 在匹配簡報上對認證專業人員的 LMSYS-Arena 風格勝率 ≥55% |
| **速度 × 品質** | 在 ≤人類周轉時間的 10% 內達到相等的 L2 評分標準分數 |
| **錯誤率** | 90 天窗口內較低的發布後缺陷率（更正、下架、退貨） |
| **認證** | 通過人類專業人員必須通過的相同認證考試（CMI、CFA、CAS、USMLE 等） |
| **原創性** | 在不降低品質的情況下獲得更高的新穎性分數（與訓練語料庫的嵌入向量距離） |

---

## 6. 評論協議（代理如何接受及給予評論）

所有代理間評論通過共享的 **CritiqueMessage** JSON 模式流動。這是任何代理可以評論任何其他代理的工作，以及任何代理可以接收評論進行修訂的通用機制。

```json
{
  "critique_id": "uuid",
  "from_agent": "EditorAgent",
  "to_agent": "DirectorAgent",
  "artifact_ref": "shot_42_take_3.mp4",
  "severity": "blocker | major | minor | nit",
  "category": "pacing | continuity | accuracy | compliance | accessibility | brand | craft",
  "evidence": ["timecode 00:01:14 — held 1.4s past the cut point per genre prior"],
  "suggested_action": "trim 1.0s; re-evaluate hold",
  "rubric_reference": "Murch Rule of Six §3",
  "must_resolve_before": "phase_4_review"
}
```

**接受規則：**
1. **Blocker** 嚴重性會暫停 DAG 直到解決。
2. **Major** 觸發接收代理的 Self-Refine／Reflexion 循環（最多 3 次迭代）。
3. **Minor／nit** 記錄到代理的記憶存儲中，並在下一個訓練週期匯總（RLAIF 獎勵信號）。
4. 兩個代理之間的爭議提交給 **JudgeAgent** 進行多代理辯論（Du et al. 2023），以相關評分標準為憲法；如果無法解決，升級至 HumanInTheLoop 審查員。
5. 每個已接受的評論附加到產物的 C2PA 來源證書鏈中，以便下游代理和人類可以審計。

---

## 7. 持續蒸餾循環

代理如何持續從真實從業者學習：

| 階段 | 機制 | 現實世界錨點 |
|---|---|---|
| **引導** | 在公開可用 + 已授權專業語料庫上預訓練 | IMDb 最高評分完整製作人員電影、Criterion 解說、ASC/ACE/CAS 檔案、康城/Sundance 入選作品 |
| **專家訪談** | 獲取在職專業人員的同意（付費）→ 指令微調 | 與具名 DGA/WGA/ASC/ACE/CAS/MPSE/VES 成員的直接合作 |
| **即時 RLAIF** | 在職專業人員（及 JudgeAgent）對輸出評分 → DPO/KTO 更新 | 工作室品質控制會議、影展評審評分標準 |
| **獎項評分標準基礎** | 反向工程主要工會的評分表 → 憲法 | DGA、WGA、ASC、ACE、MPSE、VES、Annie、CAS、HPA、康城、AMPAS |
| **對抗性紅隊** | 每個新模型版本由 DeepfakeDetectionAgent + EthicsAgent 攻擊 | Hany Farid 實驗室基準；AI 合作夥伴合成媒體框架 |
| **發布後現實檢查** | 30/60/90 天指標作為真實情況回饋（留存率、ROAS、完成率、獎項） | YouTube Analytics、Wistia、Meta/TikTok 廣告報告、Metacritic、Box Office Mojo |

### 7.1 蒸餾輸入與治理

| 資料族群 | 例子 | 重要原因 |
|---|---|---|
| **敘事文字** | 劇本、字幕、逐字稿、方案、評論 | 訓練故事結構、對白、敘事壓縮與主張抽取 |
| **視覺素材** | 分鏡、影格、素材底片、概念圖、鏡頭庫 | 為構圖、連戲、鏡頭語言與風格遷移提供基礎 |
| **音訊素材** | 對白、ADR、環境聲、音效庫、配樂分軌 | 支援語音、同步、聲音設計、混音與情緒建模 |
| **結構化中介資料** | 預算、排程、權利紀錄、觀看完成率、CTR、ROAS、修正紀錄 | 讓創意輸出與商業及合規結果連接起來 |
| **多模態配對資料** | 影片 + 音訊 + 字幕組、提示詞／輸出配對、場景封包 | 支援端到端生成、QA 與檢索工作流程 |
| **營運遙測** | 佇列深度、渲染延遲、重渲原因、快取命中、基準回歸 | 將製作行為轉化為優化與再訓練信號 |

**治理規則：** 只使用已授權或已同意來源；明確的聲音／肖像同意鏈；資料集版本控制；在類型、年代、語言與文化之間做偏差平衡；所有關鍵發佈資產均附帶來源證明。

### 7.2 規模配置檔與部署策略

| 規模 | 典型範圍 | 工作流程含義 |
|---|---|---|
| **S1-S2** | 短片、UGC 廣告、輕量解說內容 | 代理數較少、迭代快、分支有限、可觀測性堆疊較輕 |
| **S3-S4** | 廣播級內容、高級社交內容、音樂影片、持續品牌系列 | 需要更強連戲、較完整 QC、多格式交付、排程發佈、較豐富分析 |
| **S5-S6** | 紀錄片、長篇品牌內容、企業學習素材庫 | 需要存檔策略、更強權利管理、基準監控、多語封裝 |
| **S7** | 長片或電影級製作 | 需要完整分支封裝、重型渲染編排、分散式儲存、正式發佈治理，以及長尾再訓練 |

### 7.3 封閉式改進循環

1. 在觀眾留存、ROAS、完成率、修正紀錄及平台交付失敗等面向收集上線後遙測。
2. 將重複出現的失敗模式轉化為提示詞更新、路由策略、評分標準修訂或模型訓練工單。
3. 在升級新模型、提示包或編排策略前，先執行基準與回歸測試套件。
4. 對虛擬人、語音、合規及交付流程中的高風險改動，採用金絲雀或限制性 rollout。
5. 保持雙向學習循環：製作品質反饋訓練，而訓練資產更新只在依賴關係需要時觸發定向重渲或重新封裝。

---

## 8. 開放問題／需要人類參與的環節

以下事項仍然不可協商地由人類執行（按截至 2026 年 5 月的倫理 + 法規）：

- **語音／肖像克隆的同意**（SAG-AFTRA AI 附加條款、EU AI Act 第 50 條）
- **新穎知識產權／誹謗／醫療／金融陳述的最終法律簽署**
- **真實人類表演者的選角**（使用時）
- **新聞／傳媒的編輯標準**（按 SPJ、IFCN）
- **MPA 分級 + 影院審查**
- **影展資格認證**（大多數主要影展要求人類署名披露）
- **發布後問題的危機溝通**
- **本地化中的跨文化敏感度審查**（NativeReviewerAgent 建議；人類批准）
