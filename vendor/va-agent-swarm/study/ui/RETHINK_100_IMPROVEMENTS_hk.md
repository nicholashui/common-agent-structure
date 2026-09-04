# 100 點深度重構 — 有研究支持的改進建議

> 基於 arXiv 論文（FilmAgent、MovieAgent、OmniAgent、AnimAgents、Sima 1.0）、2026 模型版圖（Seedance 2.0、Wan 2.6、Vidu Q2/Q3、Grok Imagine Video、Hailuo 2.3）、LangGraph 1.0 的生產級模式，以及 Generative UI 趨勢。2026 年 5 月。

---

## 研究來源

| 來源 | 核心洞見 | 連結 |
|--------|------------|------|
| FilmAgent（2025） | 以迭代回饋迴路做劇本校驗與減少幻覺的多代理人電影自動化 | [arXiv:2501.12909](https://arxiv.org/abs/2501.12909) |
| MovieAgent（2025） | 階層式 CoT 規劃 + 角色庫，可達到最佳劇本忠實度與角色一致性 | [arXiv:2503.07314](https://arxiv.org/abs/2503.07314) |
| OmniAgent | 以電影製作啟發的階層式圖（graph）多代理人，用於長影片 | [arXiv:2510.22431](https://arxiv.org/html/2510.22431v1) |
| AnimAgents（2025） | 人類 + 多代理人協作；每個前期製作階段都有專屬看板 | [arXiv:2511.17906](https://arxiv.org/abs/2511.17906) |
| Sima 1.0（2025） | 11 步混合人力管線，用於紀錄片影片製作 | [arXiv:2604.07721](https://arxiv.org/html/2604.07721) |
| Seedance 2.0（2026 年 4 月） | 同時輸入 9 張圖片 + 3 段影片 + 3 段音訊；原生聲畫同步 | [ByteDance](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0) |
| Wan 2.6（2026） | 以 IP 錨定的角色一致性；多鏡頭敘事連貫性強 | [Comparison](https://wanvideogenerator.com/blog/seedance-2-vs-wan-2-6) |
| Veo 3.1（2026） | 4K + 參考圖可控角色／物件；可配置畫面比例 | [Google AI](https://ai.google.dev/gemini-api/docs/video) |
| Kling 2.6/3.0 | 動作更符合物理；可用參考影片做動作控制 | [fal.ai](https://fal.ai/models/fal-ai/kling-video) |
| Grok Imagine Video（xAI） | 新入局者，I2V 能力強 | [wavespeed.ai](https://wavespeed.ai/blog/posts/grok-imagine-video-vs-sora-2-veo-3-seedance-wan-vidu-comparison-2026/) |
| LangGraph 1.0 生產模式 | 節點快取、延遲節點、前／後置 hooks、共識機制 | [LangChain](https://www.langchain.com/blog/building-langgraph) |
| 2026 代理人架構 | 將協調（orchestration）與執行（execution）分離；事件驅動避免連鎖故障 | [markaicode](https://markaicode.com/architecture/agent-architecture-best-practices-2026/) |
| Supervisor vs Swarm | Supervisor 更準（路由是唯一工作）；Swarm 更快（少一層中介） | [focused.io](https://focused.io/lab/multi-agent-orchestration-in-langgraph-supervisor-vs-swarm-tradeoffs-and-architecture) |
| Generative UI 2026 | AI 代理人動態生成豐富互動介面 | [Medium](https://medium.com/@akshaychame2/the-complete-guide-to-generative-ui-frameworks-in-2026-fde71c4fa8cc) |
| 2026 六模型對比 | 依目標選擇：轉化、寫實、鏡頭控制、敘事、IP、成本 | [opencreator.io](https://opencreator.io/blog/ai-video-models-comparison-2026) |

---

## Top 20 關鍵改進（P0 + P1）

### 要新增的模型（需更新 agents.md 的工具可用性）

1. **Seedance 2.0** — 同時輸入 9 圖 + 3 影片 + 3 音訊；首尾幀控制；原生多鏡頭敘事
2. **Wan 2.6** — IP 錨定角色一致性；多鏡頭敘事連貫性最強
3. **Vidu Q2/Q3** — 時序一致性專長；I2V 具競爭力
4. **Grok Imagine Video**（xAI）— 新入局者；I2V 能力強
5. **Hailuo 2.3**（MiniMax）— 快速的低成本層級生成

### 架構（需更新後端文件）

6. **Supervisor + Swarm 混合** — 創意決策用 Supervisor（重準確）；並行 QA 用 Swarm（重速度）
7. **節點快取**（LangGraph 1.0）— 快取相同輸出；可降 30–50% 成本
8. **每個 API 的斷路器** — Veo/Sora/Kling 等 API 故障時可優雅降級
9. **協調與執行分離** — 以不同程序避免連鎖故障
10. **模型退役處理** — Sora 2 於 2026 年 9 月退役；需要平滑遷移

### 工作流（源自 FilmAgent/MovieAgent 研究）

11. **角色庫（Character Bank）** — 持久化角色定義（臉部參考、聲線、服裝）供所有鏡頭共享
12. **迭代式劇本驗證** — 在往下走之前驗證中間稿（降低幻覺）
13. **階層式 CoT 規劃** — 複雜故事更佳拆解
14. **鏡頭鄰接感知** — 生成時同時考慮上一鏡與下一鏡
15. **參考畫面庫** — 早期鏡頭批准的畫面可指導後續生成（保持一致）
16. **首尾幀生成** — Seedance 2.0 特性；精準場面控制
17. **多模型集成** — 同一鏡頭用 2 個模型生成，再用 CLIP 選最佳

### UI/UX（源自 Generative UI 研究）

18. **漸進式結果** — 代理人工作中就顯示部分輸出（鏡頭 1 可先於鏡頭 5 完成時出現）
19. **只重生成指定片段** — 保留鏡頭 1–4，只重做鏡頭 5
20. **AI 副駕駛對話** — 自然語言觸發任何操作：「把鏡頭 3 延長 2 秒」

---

## 全部 100 項改進（按類別）

### A. 模型版圖（1–15）
### B. 架構（16–30）
### C. 有研究支持的工作流（31–50）
### D. UI/UX（51–70）
### E. 新能力（71–85）
### F. 品質與評估（86–95）
### G. 商業與規模化（96–100）

（詳細拆解見下）

---

## A. 模型版圖更新（1–15）

| # | 模型／特性 | 狀態 | 影響 | 行動 |
|---|--------------|--------|--------|--------|
| 1 | Seedance 2.0（ByteDance） | 2026 年 4 月上線 | 重大 | 加入 agents.md + Router + Tool 區 |
| 2 | Wan 2.6（Alibaba） | 2026 上線 | 重大 | 加入 — 角色一致性最佳 |
| 3 | Vidu Q2/Q3 | 2026 上線 | 中等 | 加入 — 時序一致性專家 |
| 4 | Grok Imagine Video（xAI） | 2026 上線 | 中等 | 加入 — I2V 具競爭力 |
| 5 | Hailuo 2.3（MiniMax） | 2026 上線 | 中等 | 加入 — 低成本／高速度選項 |
| 6 | Kling 2.6 變體感知 | 更新 | 輕微 | 更新模型卡 |
| 7 | Seedance 1.5 Pro 多鏡頭 | 2025 上線 | 重大 | 加入 — 原生場景切換 |
| 8 | Flux 1.1 Pro Ultra | 2026 上線 | 中等 | 用於圖片生成 |
| 9 | SD 3.5 自架 | 上線 | 中等 | 用於降成本 |
| 10 | RouterAgent 的模型優勢矩陣 | 新 | 重大 | 在路由邏輯實作 |
| 11 | 多模型集成生成 | 新 | 重大 | 可選，按製作啟用 |
| 12 | 首尾幀控制 | Seedance 2.0 | 重大 | 整合到 DirectorAgent |
| 13 | 參考影片的動作轉移 | Kling + Seedance | 中等 | ChoreographyAgent 整合 |
| 14 | 原生音訊生成感知 | Veo 3.1、Seedance | 中等 | 簡單場景可跳過音訊代理人 |
| 15 | 模型退役處理 | 重大 | 重大 | 平滑遷移系統 |

## B. 架構改進（16–30）

| # | 改進 | 來源 | 影響 |
|---|------------|--------|--------|
| 16 | Supervisor + Swarm 混合 | focused.io 研究 | 重大 |
| 17 | 節點快取（LangGraph 1.0） | langchain.com 文章 | 重大 |
| 18 | Map-reduce 的延遲節點 | LangGraph 1.0 | 中等 |
| 19 | 每個節點都有前／後置 hooks | LangGraph 1.0 | 中等 |
| 20 | 超越 JudgeAgent 的共識機制 | LangGraph 模式 | 中等 |
| 21 | 協調與執行分離 | markaicode.com | 關鍵 |
| 22 | 推測式執行與回滾 | 生產模式 | 中等 |
| 23 | 長製作的 checkpoint 壓縮 | 規模化優化 | 中等 |
| 24 | 代理人池化與 warm-start | 延遲優化 | 中等 |
| 25 | 具防飢餓（starvation prevention）的優先隊列 | 公平性 | 中等 |
| 26 | 每個外部 API 的斷路器 | 可靠性 | 關鍵 |
| 27 | 事件回放與時間旅行除錯 | 可觀測性 | 中等 |
| 28 | 代理人設定的金絲雀部署 | 安全性 | 中等 |
| 29 | 新設定的影子模式 | 安全性 | 中等 |
| 30 | 多租戶隔離 | 企業 | 中等 |

## C. 有研究支持的工作流改進（31–50）

| # | 改進 | 來源論文 | 影響 |
|---|------------|-------------|--------|
| 31 | 迭代式劇本驗證 | FilmAgent | 重大 |
| 32 | 階層式 CoT 規劃 | MovieAgent | 重大 |
| 33 | 跨鏡頭角色庫 | MovieAgent | 重大 |
| 34 | 共享世界模型 | ShareVerse | 重大 |
| 35 | 電影語言語法（鏡頭轉場） | arXiv:2604.09195 | 中等 |
| 36 | 每階段專屬看板 | AnimAgents | 中等 |
| 37 | 混合人力 checkpoint | Sima 1.0 | 已有（gates） |
| 38 | 多輪代理人對話 | FilmAgent 修訂版 | 重大 |
| 39 | Sound Director 監督迴路 | arXiv:2503.07217 | 中等 |
| 40 | 跨模態時序狀態共享 | OmniAgent | 重大 |
| 41 | 圖式記憶（不只向量） | 知識圖譜 | 中等 |
| 42 | DAG 的幕／段／節拍層級 | MovieAgent 結構 | 中等 |
| 43 | 鏡頭鄰接感知 | 電影語言論文 | 重大 |
| 44 | 取景／場景勘景聚焦 | MovieAgent | 已有（ProductionDesign） |
| 45 | 角色感知字幕生成 | MovieAgent | 中等 |
| 46 | 多場景 vs 單鏡頭的獨立管線 | OmniAgent | 重大 |
| 47 | 以 storyboard panels 作為生成控制圖 | AnimAgents + ControlNet | 重大 |
| 48 | 參考畫面庫（早期批准畫面指導後續） | 角色一致性 | 重大 |
| 49 | 組裝後的情緒曲線驗證 | EmotionalArcAgent 迴路 | 中等 |
| 50 | 交付前在最終剪輯上做留存預測 | RetentionOptimizer 時機 | 中等 |

## D. UI/UX 改進（51–70）

| # | 改進 | 來源 | 影響 |
|---|------------|--------|--------|
| 51 | Generative UI — 代理人生成介面組件 | Generative UI 2026 | 重大 |
| 52 | 無限畫布（節點式工作流編輯器） | TwitCanva | 重大 |
| 53 | 即時多人協作 | 企業需求 | 中等 |
| 54 | AI 副駕駛對話介面 | 自然語言控制 | 重大 |
| 55 | 版本分支（在任何 gate 分叉） | 非破壞式實驗 | 重大 |
| 56 | 每個決策都有並排對照 | 更佳審閱體驗 | 中等 |
| 57 | 懸停即顯示情境幫助 | 新手導覽 | 輕微 |
| 58 | 製作時間線回放（可拖動歷史） | 除錯 + 學習 | 中等 |
| 59 | 代理人推理以白話解釋 | 信任 + 透明 | 中等 |
| 60 | 變更設定前先預覽影響 | 更安全的變更 | 中等 |
| 61 | 範本市集（發佈／販售） | 社群 + 變現 | 中等 |
| 62 | 漸進載入（代理人工作中顯示部分結果） | 體感更快 | 重大 |
| 63 | 與人類基準對比 | 價值主張 | 中等 |
| 64 | 成本預測信心區間 | 更佳預期管理 | 輕微 |
| 65 | 手機監控 + gate 審批 | 便利 | 中等 |
| 66 | Webhook/API 整合（CRM、行事曆觸發） | 企業工作流 | 中等 |
| 67 | 批次模式（由 1 個 brief 產生 50 個變體） | 成效行銷 | 重大 |
| 68 | White-label 模式 | 代理商部署 | 中等 |
| 69 | 離線下載（所有素材 + metadata） | 互通性 | 輕微 |
| 70 | 自動生成 WCAG 合規報告 | 企業合規 | 輕微 |

## E. 新能力（71–85）

| # | 能力 | 影響 |
|---|-----------|--------|
| 71 | 多語言製作（brief 可用任何語言） | 重大 |
| 72 | 從上載過往影片學習品牌 DNA | 重大 |
| 73 | 競品影片分析整合 | 中等 |
| 74 | A/B 變體生成（同時 3–5 個變體） | 重大 |
| 75 | 互動式影片輸出（分支、可點擊） | 中等 |
| 76 | 生成即時預覽（串流部分幀） | 中等 |
| 77 | 只重生成指定片段 | 重大 |
| 78 | 升頻／增強流程（先低成本生成再拋光） | 中等 |
| 79 | 音樂優先工作流（由音訊開始） | 重大 |
| 80 | 劇本優先工作流（由 screenplay 開始） | 重大 |
| 81 | 參考影片分析（從上載影片擷取風格） | 重大 |
| 82 | 季節性內容日曆（按日期自動建議） | 中等 |
| 83 | 成效回饋迴路（發佈後分析 → 下一次製作） | 重大 |
| 84 | 跨製作一致性（角色跨製作保持一致） | 重大 |
| 85 | 即時趨勢整合到進行中製作 | 中等 |

## F. 品質與評估（86–95）

| # | 改進 | 影響 |
|---|------------|--------|
| 86 | VBench 2.0 整合（人類逼真度、創意、物理） | 中等 |
| 87 | 人類偏好學習（由使用者接受／拒絕做 RLHF） | 重大 |
| 88 | 設定變更的自動回歸測試 | 中等 |
| 89 | 跨模型品質標準化 | 中等 |
| 90 | 時序連貫性評分（多鏡頭一致性指標） | 重大 |
| 91 | 聲畫同步評分（唇形 + 節拍同步驗證） | 中等 |
| 92 | 觀眾分眾模擬（多 persona 集群） | 中等 |
| 93 | 倫理審查自動化（刻板印象／傷害標記） | 中等 |
| 94 | 溯源鏈可視化（完整決策譜系） | 中等 |
| 95 | 品質趨勢儀表板（製作是否在變好？） | 中等 |

## G. 商業與規模化（96–100）

| # | 改進 | 影響 |
|---|------------|--------|
| 96 | 按用量計價分層（free/pro/enterprise） | 重大 |
| 97 | 讓使用者自建代理人 | 重大 |
| 98 | 代理人市集（分享／販售設定 + 知識） | 重大 |
| 99 | 企業 SSO + 稽核紀錄（SAML、SCIM、SOC 2） | 中等 |
| 100 | 自架部署（Docker/K8s 套件） | 中等 |

---

## 優先落地順序

| 階段 | 項目 | Timeline |
|-------|-------|----------|
| **階段 1（基礎）** | 15、21、26、6–9、17 | Week 1–2 |
| **階段 2（品質躍升）** | 1–3、10–12、31–33、43、47–48 | Week 3–4 |
| **階段 3（UX 拋光）** | 18–20、54、55、62、77 | Week 5–6 |
| **階段 4（規模化）** | 46、67、71、74、83、87 | Week 7–8 |
| **階段 5（商業）** | 96–100、51–52、61 | Week 9–12 |

---

*重構文件完。所有既有檔案保持不變。此文件是「新增」到設計之上，並非取代。*
