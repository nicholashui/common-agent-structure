# 研究代理功能規範

## 1. 文件控制

- 文件標題：`Research Agent Functional Specification`
- 系統名稱：`grok-research-agent`
- 文檔類型：來自實施和測試的當前狀態功能規範
- 主要交付模型：本地 Python CLI 應用程式
- 本規範的真實來源：`grok_research_agent/` 套件實現、打包提示和自動化測試
- 規範意圖：描述系統目前實現的功能行為，包括工作流行為、文件契約、驗證規則、故障處理和整合點

## 2. 目的

該系統提供本地優先的研究自動化工作流程，透過範圍定義、來源發現、來源管理、內容提取、筆記本組裝、合成、可選的全源保存、最終拋光、知識編譯、鑽取包生成、圖像提示生成和 YouTube 腳本生成的分階段管道，將用户提供的主題轉換為詳細的 Markdown 研究報告。

此系統的設計目的是：

- 在關鍵決策點保持人為控制；
- 將所有研究工件本地儲存在可恢復會話目錄中；
- 透過 xAI OpenAI 相容 API 使用 Grok 來完成所有 LLM 生成任務；
- 支援選擇性地攝取外部本地文檔作為指導上下文；
- 產生可檢查的中間偽影，而不是單一不透明的結果。

## 3.範圍

### 3.1 範圍

- 命令列會話生命週期管理
- 持久會話狀態和工件存儲
- 八階段研究工作流程編排
- 可選無人值守執行模式
- 本地指導材料的外部文件預處理
- 知識庫編譯成超圖與核心概念
- 從編譯的概念產生鑽包
- 來自新輸入文件的超圖更新
- 超圖數據的美人魚渲染
- 根據最終報告內容產生圖像提示
- 根據最終報告或章節草稿產生 YouTube 腳本

### 3.2 超出範圍

- Web UI、API 伺服器或多用户協作
- 身份驗證、授權和基於角色的權限
- 資料庫支援的持久性
- 語意向量搜尋或檢索索引
- 超越直接 HTTP 取得的自動瀏覽器自動化或爬蟲編排
- 保證LLM輸出的事實驗證
- 超越盡力文字解碼的 `feed` 命令中的二進位文件饋送

## 4. 利害關係人、角色和外部參與者

### 4.1 人類使用者角色

- `Research Operator`：啟動會話，批准或修改工作流程輸出，選擇精選來源，可選擇完整離線收集，並執行輔助命令
- `Reviewer/Study User`：使用產生的報告、鑽取套件、超圖、Mermaid 輸出、圖像提示或 YouTube 腳本；該角色在技術上與操作員沒有區別

### 4.2 系統參與者

- `LLM Provider`：xAI Grok，透過 OpenAI 相容 API 訪問
- `Remote Content Hosts`：精選來源引用的公開網站和 PDF 端點
- `Local Filesystem`：儲存會話、狀態、輸出、外部文件工件和知識庫工件
- `Local Environment`：提供`.env`或環境變數、`EDITOR`和Python運行時

### 4.3 接取模型

- 系統沒有內部使用者帳户，也沒有權限模型。
- 任何可以執行 CLI 並讀取/寫入目標會話目錄的使用者都可以完全作業系統。

## 5. 系統上下文和架構

### 5.1 核心模組

- `grok_research_agent.cli`
  - 解析 CLI 參數
  - 創建`SessionManager` 和`WorkflowRunner`
  - 將命令失敗對應到處理退出程式碼
- `grok_research_agent.session_manager`
  - 建立並保留會話狀態
  - 建立唯一的運行目錄
  - 提供規範的會話和知識庫路徑
- `grok_research_agent.workflow_phases`
  - 實現工作流程狀態機
  - 處理來源獲取、提取、合成、編譯、鑽取包生成、提要、顯示、圖像生成和 YouTube 腳本生成
- `grok_research_agent.grok_client`
  - 載入環境配置
  - 使用 OpenAI 客户端呼叫 xAI Grok
  - 將 API 異常對應到特定於網域的執行時間錯誤
- `grok_research_agent.external_docs`
  - 遞歸攝取支援的本機文檔
  - 提取指導背景、約束、要求和相關訊號
- `grok_research_agent.prompts/*`
  - 定義 LLM 呼叫的輸出合約和行為指令

### 5.2 執行模型

- 該產品是一個單進程 CLI 應用程式。
- 每個指令都會在目標會話下建立一個新的運行目錄。
- 命令會對會話目錄中的檔案進行操作，並且還可以寫入執行本機副本以進行追蹤。
- 長期狀態是基於文件的；沒有後台守護程序。

## 6. 技術和運行時依賴性

- Python運行時間：`>=3.11`
- 所需包：
  - `openai`
  - `python-dotenv`
  - `rich`
  - `pydantic>=2`
  - `pypdf`
  - `python-docx`
  - `requests`
  - `beautifulsoup4`
  - `readability-lxml`
  - `chardet<6`
- 打包的 CLI 入口點：`grok-research-agent = grok_research_agent.cli:main`
- 便利包裝器：根級 `main.py` 和 `cli.py` 轉送到已打包的 CLI 入口點

## 七、配置説明

### 7.1 環境變數

- `GROK_API_KEY`
  - 對於實例化 `GrokClient` 的任何命令路徑都是必需的
  - 空格修剪後必須非空
  - 如果不存在，LLM 支援的操作將失敗並顯示明確的訊息
- `GROK_MODEL`
  - Optional
  - 預設為`grok-3`
  - 空白值應歸一化回 `grok-3`
- `GROK_MAX_OUTPUT_TOKENS`
  - 可選整數
  - 預設為`50000`
  - 無效或非數字值應恢復為`50000`
  - 低於 `1` 的值應箝位至 `1`
- `GROK_REQUEST_TIMEOUT_SECONDS`
  - 可選整數
  - 預設為`300`
  - 無效或非數字值應恢復為`300`
  - 低於 `1` 的值應箝位至 `1`
- `EDITOR`
  - Optional
  - 僅在階段 0 `edit` 流程中使用
  - 如果不存在，選擇 `edit` 仍將建立可編輯的臨時文件，但不會自動啟動外部編輯器

### 7.2`.env`分辨率

- 當工作流程建構預設`GrokClient`時，它應嘗試載入位於會話目錄上方兩級目錄的`.env`檔案。
- 如果那裡不存在`.env`，系統將只繼續使用進程環境變數。

## 8. 使用者介面規範

### 8.1 介面類型

- 主要接口：終端機/CLI
- 渲染庫：`rich`
- 輸出類型：
  - 簡單的狀態訊息
  - Markdown 內容在某些階段回顯到控制台
  - 用於發現和全集合選擇的預覽表

### 8.2 人機交互點

- H0：範圍確認
- H1：策劃源批准
- H2：草案批准或修訂指令
- H3：全源離線拷貝選擇

### 8.3 無人值守模式

- `--auto` 應繞過互動式提示並盡可能推動工作流程完成。
- 在自動模式下：
  - H0 自動確認
  - H1 來源選擇設定為`all`
  - H1 批准設定為 `approve`
  - H2 回饋設定為 `approve`
  - H3選擇由`--auto-full-collection`控制，預設為`all`
- 自動模式不應呼叫`input()`。

## 9. 使用者角色和權限規範

由於系統沒有身分或授權層，因此功能權限模型為：

- 任何操作員都可以執行任何命令；
- 任何操作員都可以創建、恢復、修改、編譯、鑽取、提供和完成他們可以在磁碟上存取的會話；
- 沒有僅限管理員的操作；
- 除了檔案時間戳記和工件存在之外，沒有稽核或歸因模型。

## 10. CLI 指令功能要求

### 10.1 常見命令行為

- `FR-CLI-001`：除`list-types` 之外的所有命令都需要`--sessions-dir`。
- `FR-CLI-002`：需要現有會話的命令應需要`--session-id`。
- `FR-CLI-003`：CLI 應返回退出代碼`0` 成功完成。
- `FR-CLI-004`：當`WorkflowRunner.run()`引發`GrokError`或`GrokQuotaError`時，CLI應返回退出代碼`1`。
- `FR-CLI-005`：對於無法識別的命令調度或`argparse` 驗證失敗，CLI 應返回退出代碼`2`。
- `FR-CLI-006`：當啟用`--trace-llm`時，請求和回應內容應以截斷的、控製字元清理的形式列印。

### 10.2`start`

- `FR-START-001`：系統應建立一個新會話，其中包含主題、可選焦點、可選外部文件目錄和持久的`mode`。
- `FR-START-002`：系統應列印已建立的會話ID。
- `FR-START-003`：系統應立即呼叫從會話目前階段（最初為階段 0）開始的工作流程執行。
- `FR-START-004`：接受的`--mode` 值為`report`、`compiler` 和`drill`。
- `FR-START-005`：所選`mode` 應儲存在會話狀態中，但不應改變目前實作中的執行時間工作流行為。

### 10.3`resume`

- `FR-RESUME-001`：系統應從`current_phase`載入會話並執行。
- `FR-RESUME-002`：在互動模式下，執行應在下一個人工檢查點或明確指示使用者再次復原的階段之後停止。
- `FR-RESUME-003`：如果`current_phase >= 8`，系統應列印`Session is complete.`

### 10.4`list-sessions`

- `FR-LIST-001`：系統應列出`--sessions-dir`下包含`session.json`的目錄。
- `FR-LIST-002`：清單應排除非目錄條目和缺少`session.json` 的目錄。
- `FR-LIST-003`：如果不存在會話，系統將列印`No sessions found.`

### 10.5`list-types`

- `FR-TYPES-001`：系統應列印`auto-hypergraph`。
- `FR-TYPES-002`：此指令不需要會話目錄參數。

### 10.6`update`

- `FR-UPDATE-001`：系統應使用`since_last_run=yes` 運行發現。
- `FR-UPDATE-002`：完成後，系統應設定`current_phase = 2`。
- `FR-UPDATE-003`：系統應指示使用者恢復以管理來源。

### 10.7`synthesize`

- `FR-SYNTH-001`：系統應強制執行第 5 階段綜合，無論目前階段為何。
- `FR-SYNTH-002`：第 5 階段的先決條件仍然適用；如果筆記本輸入遺失，合成將無法繼續。

### 10.8`compile`

- `FR-COMPILE-001`：CLI 應公開`--type auto-hypergraph`。
- `FR-COMPILE-002`：工作流程應接受`auto-hypergraph`並在內部容忍其他休眠自動類型字串，但只有`auto-hypergraph`公開並支援端到端。
- `FR-COMPILE-003`：系統應從`04_master_notebook.md`（如果存在）進行編譯，並附加任何`03_extracted/*.md`（如果存在）內容。
- `FR-COMPILE-004`：如果不存在筆記本或提取的內容，系統將列印`Missing notebook or extractions. Resume the session to generate them first.`並停止。

### 10.9`drill`

- `FR-DRILL-001`：唯一支援的模式應為`backward`。
- `FR-DRILL-002`：如果`core_concepts.json`不存在，系統會自動嘗試`compile`。
- `FR-DRILL-003`：如果編譯後仍然不存在核心概念，系統將列印`Missing core concepts. Run compile first.`

### 10.10`feed`

- `FR-FEED-001`：此指令需要`--new-doc`。
- `FR-FEED-002`：如果文件不存在或不是普通文件，系統將列印`File not found: <path>`並停止。
- `FR-FEED-003`：系統應將檔案複製到帶有時間戳前綴的`knowledge_base/feed_docs/`。
- `FR-FEED-004`：如果不存在`hypergraph.json`，系統將呼叫編譯，然後返回而不執行合併更新。

### 10.11`show`

- `FR-SHOW-001`：如果`knowledge_base/hypergraph.json`不存在，系統將列印`Missing hypergraph.json. Run compile first.`
- `FR-SHOW-002`：否則，系統應產生`knowledge_base/hypergraph.mmd`。

### 10.12`generate-images`

- `FR-IMG-001`：此指令需要`FINAL_REPORT.md`。
- `FR-IMG-002`：如果缺少`FINAL_REPORT.md`，系統將列印`Missing FINAL_REPORT.md`。
- `FR-IMG-003`：成功後，系統將在運行目錄和會話目錄中寫入`images_to_generate.md`。

### 10.13`youtube-script`

- `FR-YT-001`：此指令需要`FINAL_REPORT.md`。
- `FR-YT-002`：如果缺少`FINAL_REPORT.md`，系統將列印`Missing FINAL_REPORT.md`。
- `FR-YT-003`：成功後，系統將在運行目錄和會話目錄中寫入`Youtube_Script.md`。

## 11. 會話管理規範

### 11.1 會話身份

- `FR-SESSION-001`：會話 ID 應根據 `YYYYMMDD` 格式的 slugified 主題加上目前日期產生。
- `FR-SESSION-002`：slugification 應小寫主題，用 `-` 替換非字母數字字符，折疊重複的連字符，並刪除前導/尾隨連字符。
- `FR-SESSION-003`：如果slug超過配置的前綴長度，系統應修剪它並附加8個字元的SHA-1摘要後綴。
- `FR-SESSION-004`：如果產生的會話目錄已經存在，系統將附加`-2`、`-3`等，直到唯一。

### 11.2 會話狀態

持久化的`SessionState`應包含：

- `session_id`
- `topic`
- `focus`
- `mode`
- `external_docs_dir`
- `external_docs_status`
- `external_docs_summary`
- `external_docs_manifest_path`
- `external_docs_context_path`
- `external_docs_processed_files`
- `external_docs_total_files`
- `external_docs_completion_rate`
- `external_docs_relevance_score`
- `external_docs_last_error`
- `created_at`
- `grok_model`
- `current_phase`
- `run_history`
- `updated_at`

### 11.3 會話保持規則

- `FR-SESSION-005`：系統應將狀態持久保存為編碼為 UTF-8 JSON 的`session.json`。
- `FR-SESSION-006`：`updated_at` 應在每個`save_state()` 上刷新。
- `FR-SESSION-007`：儲存時會自動建立會話目錄和知識庫子目錄。
- `FR-SESSION-008`：`run_history` 應初始化為空列表，但不由目前工作流程程式碼填入。

### 11.4 運行目錄規則

- `FR-RUN-001`：建立`WorkflowContext`的每個命令執行都應在`runs/`下方建立新的運行目錄。
- `FR-RUN-002`：運行目錄名稱應使用時間戳格式`YYYYMMDD_HHMMSS_microseconds`。
- `FR-RUN-003`：如果發生時間戳衝突，系統將重試最多1000次。
- `FR-RUN-004`：如果在 1000 次嘗試內無法建立唯一的運行目錄，系統將引發`RuntimeError`。

## 12. 外部文件預處理規範

### 12.1 功能目的

外部文檔子系統在工作流程執行之前攝取本地參考文檔，並將其轉換為可以影響範圍、發現、管理、提取和規劃的強制指導上下文。

### 12.2 觸發規則

- `FR-EXT-001`：外部文件預處理應在工作流程命令之前自動執行，`generate-images`、`youtube-script`、`compile`、`drill`、`feed` 和`show` 除外。
- `FR-EXT-002`：如果`external_docs_dir`為空或不存在，則應跳過預處理。
- `FR-EXT-003`：如果會話狀態已將預處理標記為`completed` 並且存在摘要，則預處理不應自動重新運行。

### 12.3 支援的輸入

- 支援的字尾：`.pdf`、`.docx`、`.txt`、`.md`
- 發現行為：在提供的根目錄下遞歸
- 不支援的文件類型：忽略而不是出錯

### 12.4 處理規則

- `FR-EXT-004`：每個支援的檔案應使用類型適當的邏輯來讀取。
- `FR-EXT-005`：PDF提取應迭代頁面並跳過文字提取失敗的頁面。
- `FR-EXT-006`：DOCX 提取應連接非空白段落。
- `FR-EXT-007`：TXT 和 Markdown 應讀取為 UTF-8，並替換無效字元。
- `FR-EXT-008`：每個文件應根據文件名關鍵字分類為`guideline`、`background`、`steering` 或`general`。
- `FR-EXT-009`：處理器應從句子級啟發式中提取關鍵概念、約束、要求和演算法見解。
- `FR-EXT-010`：處理器應根據主題/焦點詞彙重疊加上相關術語、提取的約束和提取的要求的結構獎勵來計算相關性分數。

### 12.5 聚合輸出

- `FR-EXT-011`：系統要寫入：
  - `external_docs/manifest.json`
  - `external_docs/extracted.json`
  - `external_docs/context.md`
- `FR-EXT-012`：`manifest.json` 應包含每個檔案的處理結果和聚合成功指標。
- `FR-EXT-013`：`context.md` 應包括關鍵概念、限制、要求、可選演算法增強説明和工作流程指南等部分。
- `FR-EXT-014`：如果主題或焦點文字與面向演算法的關鍵字匹配，則應包含演算法增強註釋；否則應將其省略。

### 12.6 狀態規則

- `FR-EXT-015`：如果external-doc根目錄不存在或不是目錄，則狀態應設為`failed`，解釋性錯誤應儲存在會話狀態中，並且工作流程應繼續。
- `FR-EXT-016`：如果單一檔案失敗，這些檔案應標記為`failed`，但聚合處理應繼續。
- `FR-EXT-017`：聚合狀態應為：
  - `completed` 當所有發現的文件處理成功時
  - `partial` 當至少一個檔案成功且至少一個檔案失敗時
  - `failed` 當零文件成功時

### 12.7 快速注入規則

- `FR-EXT-018`：如果可用，外部文件摘要內容應作為強制性指導/背景資料附加到相關提示中。
- `FR-EXT-019`：外部文件上下文應被截斷為特定階段的字元預算，而不是導致失敗。

## 13. 研究工作流程狀態機

### 13.1 狀態定義

- 階段`0`：範圍產生與確認
- 階段`1`：發現
- 階段`2`：策展與差距分析
- 階段`3`：擷取
- 階段`4`：筆記本組裝
- 階段`5`：綜合與審查
- 階段`6`：完整的離線收藏選擇
- 階段`7`：最終拋光
- 階段`8`：完成

### 13.2 互動進展規則

- `FR-STATE-001`：在互動模式下，工作流程應根據`_run_until_human_step()`處理每個`resume`呼叫的一個階段或一個人工檢查點。
- `FR-STATE-002`：某些階段透過指示使用者稍後恢復而不是自動繼續來結束。
- `FR-STATE-003`：當代碼明確更新`current_phase`時，相變應立即保持。

### 13.3 自動模式進展規則

- `FR-STATE-004`：在自動模式下，工作流程將循環直到`current_phase >= 8`。
- `FR-STATE-005`：自動模式應立即跨階段繼續，無需單獨的`resume` 命令。

## 14. 分階段功能要求

### 14.1 階段 0 - 範圍確認

- `FR-P0-001`：系統應使用`scope_prompt.txt`產生Markdown範圍摘要。
- `FR-P0-002`：生成的範圍應寫入`<run>/00_scope.md`。
- `FR-P0-003`：生成的範圍應列印到控制台。
- `FR-P0-004`：自動模式下，範圍立即被接受，儲存為`00_scope_confirmed.md`，`current_phase`前進至`1`。
- `FR-P0-005`：在互動模式下，有效的使用者輸入為`yes`、`edit` 和`cancel`。
- `FR-P0-006`：`cancel`應終止該階段而不改變`current_phase`。
- `FR-P0-007`：`edit`應寫入臨時`00_scope_edit.md`，可選擇呼叫`EDITOR`，重新載入編輯的內容，列印它，並繼續提示。
- `FR-P0-008`：`yes`應儲存`00_scope_confirmed.md`，設定`current_phase = 1`，儲存狀態，並指示使用者恢復。
- `FR-P0-009`：如果Grok客户端建立失敗，系統將列印錯誤以及`.env`指導訊息並返回而不改變狀態。

### 14.2 第一階段－發現

- `FR-P1-001`：系統應渲染帶有主題、有效焦點和`since_last_run`的`discovery_prompt.txt`。
- `FR-P1-002`：發現輸出要寫入`<run>/01_discovery_table.md` 和`<session>/01_discovery_table.md`。
- `FR-P1-003`：系統在儲存前不會驗證發現表格式。
- `FR-P1-004`：在正常的互動進程中，第一階段的完成應設定`current_phase = 2`並指示使用者繼續進行管理。

### 14.3 第二階段—管理與差距分析

- `FR-P2-001`：第 2 階段需要`01_discovery_table.md`；如果遺失，系統將列印`Missing discovery table. Resume from Phase 1.`並停止。
- `FR-P2-002`：系統應列印預覽表，其中最多包含發現輸出的前 80 個非空白行。
- `FR-P2-003`：用户指令字串可以包含自由格式的來源選擇文本，包括數字、`all`、`add <urls>`、`remove <indexes>` 或`gap`；系統不會在本地解析這些命令，而是將它們傳遞給LLM。
- `FR-P2-004`：系統應嘗試產生最多 3 次精選來源。
- `FR-P2-005`：在第一次失敗後重試時，提示應添加更嚴格的僅 JSON 指令和前 20 個限制。
- `FR-P2-006`：策劃來源輸出應規範化為帶有鍵的物件清單：
  - `title`
  - `url`
  - `type`
  - `why_relevant`
  - `credibility`
  - `priority`
- `FR-P2-007`：應透過修剪引號/反引號並盡可能刪除尾隨標點符號來規範 URL。
- `FR-P2-008`：如果LLM在所有嘗試中都傳回無效的JSON或非規範結構，系統應從發現Markdown試探性地恢復URL並建立後備來源條目。
- `FR-P2-009`：運行本地管理輸出應逐字寫入`<run>/02_curated_sources.json`。
- `FR-P2-010`：會話本機管理輸出應重寫為 `<session>/02_curated_sources.json` 的規格 JSON。
- `FR-P2-011`：應始終使用策劃清單嘗試差距分析並將其儲存至`<run>/02_gap_report.md`。
- `FR-P2-012`：如果間隙分析逾時，保存的間隙報告應包含`# Gaps` 和明確的超時註釋。
- `FR-P2-013`：只有當批准輸入恰好是`approve` 時，才會發生到`3` 的階段推進。
- `FR-P2-014`：任何其他核准回應應在第 2 階段離開會話，並指示使用者稍後重複管理。

### 14.4 第 3 階段 - 提取

- `FR-P3-001`：第 3 階段需要`02_curated_sources.json`；如果缺失，系統將列印`Missing curated sources. Resume from Phase 2.`
- `FR-P3-002`：如果存在策劃來源 JSON 但規範化生成空列表，系統應列印 `Curated sources file is invalid or empty. Resume from Phase 2 to re-curate sources.`
- `FR-P3-003`：系統應在運行和會話範圍內建立以下適用的目錄：
  - `03_extracted/`
  - `03_source_snapshots/`
  - `03_extracted_chunks/`
- `FR-P3-004`：系統應請求提取計劃並將其儲存為`<run>/03_extraction_plan.md`。
- `FR-P3-005`：如果提取計劃產生逾時，系統將保存佔位計劃而不是失敗。
- `FR-P3-006`：系統應使用最多 `4` 取得工作執行緒同時預取來源套件。
- `FR-P3-007`：如果在預取期間單一來源提取失敗，系統將列印警告並繼續提取剩餘的來源。
- `FR-P3-008`：對於每個成功獲取的來源，系統應在運行和會話目錄中保存原始內容和標準化來源文字快照。
- `FR-P3-009`：快照標頭應保留標題、URL、主機、類型、優先權和可信度元資料。
- `FR-P3-010`：HTML來源包應使用`.html`保存原始快照； PDF 捆綁包`.pdf`；所有其他人都帶有`.txt`。
- `FR-P3-011`：來源文字應按以下內容分塊：
  - 最大塊大小`45000`字符
  - 重疊`5000`字符
- `FR-P3-012`：塊提取應使用最多 `2` 提取工作人員並行運行。
- `FR-P3-013`：每個區塊提示都需要嚴格的 Markdown 部分，用於涵蓋範圍摘要、術語、機制、工作流程、證據、限制、開放性問題、可引用段落和摘錄。
- `FR-P3-014`：如果提取區塊逾時，則應跳過該區塊並繼續提取其他區塊。
- `FR-P3-015`：每個成功提取的區塊都應寫入運行和會話`03_extracted_chunks/`。
- `FR-P3-016`：如果來源的所有區塊都失敗，系統將列印警告並跳過生成該來源檔案。
- `FR-P3-017`：成功的來源檔案應在運行和會話目錄中組裝到`03_extracted/<nnn>.md` 中。
- `FR-P3-018`：階段完成時，系統應使用生成標記寫入`<session>/03_extracted_index.txt`。

### 14.5 第 4 階段 - 筆記本組裝

- `FR-P4-001`：第 4 階段需要`<session>/03_extracted/` 的存在；否則它將列印`No extracted sources found in this run. Resume from Phase 3.`
- `FR-P4-002`：筆記本應包括：
  - 頂部標題`# Master Notebook`
  - 主題行
  - 筆記本用途部分
  - optional external documentation context section
  - 來源目錄部分
  - optional knowledge-base outline
  - 源檔案部分
- `FR-P4-003`：筆記本應使用`---`分隔符號連接各部分。
- `FR-P4-004`：筆記本應寫入`<run>/04_master_notebook.md` 和`<session>/04_master_notebook.md`。
- `FR-P4-005`：在互動過程中，成功的筆記本產生應設定`current_phase = 5`。

### 14.6 Phase 5 - Synthesis and Review

- `FR-P5-001`: Phase 5 shall require `04_master_notebook.md`;如果缺失，系統將列印`Missing notebook. Resume from Phase 4.`
- `FR-P5-002`：筆記本應分成最多`70000` 字元的區塊，並與`5000` 重疊。
- `FR-P5-003`：如果沒有產生筆記本區塊，系統將列印`Notebook is empty. Resume from Phase 4.`
- `FR-P5-004`：對於固定部分清單中的每個報告部分，系統應從筆記本區塊建立特定於部分的證據包。
- `FR-P5-005`: Standard report sections shall be:
  - `Core Definitions and Scope`
  - `Architecture and Technical Mechanisms`
  - `Workflows, Processes, and Operational Patterns`
  - `Evidence, Examples, and Case Studies`
  - `Limitations, Trade-offs, and Failure Modes`
  - `Open Questions and Future Directions`
- `FR-P5-006`：證據包產生應與每個部分最多 `2` 工作人員一起運行。
- `FR-P5-007`：證據包應保存在運行和會話`05_section_evidence/`目錄中。
- `FR-P5-008`：如果沒有為某個部分產生證據資料包，則應跳過該部分並發出警告。
- `FR-P5-009`：每個成功起草的部分都應寫入運行和會話`05_section_drafts/`。
- `FR-P5-010`：報告草案應包括範圍/覆蓋文本、來源目錄、起草的章節、可選的知識庫對齊和參考文獻。
- `FR-P5-011`：草稿版本應儲存為遞增`05_draft_vN.md`。
- `FR-P5-012`：審閲提示應告訴使用者他們可以輸入`approve | revise <section> <feedback> | add-section "Title" | gap-check`。
- `FR-P5-013`：只有準確的回應`approve`才能將會話推進到階段6。
- `FR-P5-014`：任何非`approve`回應應視為一般修訂回饋並傳遞至修訂提示而不進行本機解析。
- `FR-P5-015`：如果修訂產生逾時，先前的草案仍具有權威性，且階段狀態不會推進。
- `FR-P5-016`：成功的修訂輸出應儲存為下一個草稿版本，並需要另一個審核週期。

### 14.7 Phase 6 - Full Offline Collection

- `FR-P6-001`：第 6 階段應嘗試從 `02_curated_sources.json` 載入精選來源。
- `FR-P6-002`：如果缺少策劃來源，系統將嘗試從`01_discovery_table.md` 進行啟發式 URL 復原。
- `FR-P6-003`：如果沒有可恢復的規劃來源，系統應設定`current_phase = 7`，儲存狀態，列印跳過訊息，並要求後續恢復以完成確定。
- `FR-P6-004`：來源選擇 UI 應顯示每個精選來源的索引、標題和 URL。
- `FR-P6-005`：有效的實際輸入是`all`、`none`或逗號分隔的整數； non-numeric tokens shall be ignored.
- `FR-P6-006`：回應`none`應設定`current_phase = 7`，儲存狀態，列印跳過訊息，然後返回而不自動完成。
- `FR-P6-007`：回應`all` 應選擇所有來源。
- `FR-P6-008`：有效索引範圍之外的數字選擇將被忽略。
- `FR-P6-009`：在寫入完整的離線副本之前應預取選定的來源。
- `FR-P6-010`：對於每個成功取得的選定來源，系統應在運行目錄和會話目錄中寫入`06_full_sources/<nnn>.md`。
- `FR-P6-011`：如果無法取得所選來源，則應跳過該來源而不中止該階段。
- `FR-P6-012`：至少寫入嘗試的完整集合輸出後，系統應設定`current_phase = 7`，立即調用最終拋光，然後設定`current_phase = 8`。

### 14.8 Phase 7 - Final Polish

- `FR-P7-001`：最終拋光應同時需要`04_master_notebook.md`和至少一個`05_draft_v*.md`； otherwise it shall print `Missing notebook or draft.`
- `FR-P7-002`：以字典版本排序的最新草稿文件作為報告正文來源。
- `FR-P7-003`：系統應使用`final_polish_prompt.txt` 產生執行摘要。
- `FR-P7-004`：如果執行摘要產生逾時，系統應取代逾時佔位符訊息。
- `FR-P7-005`：系統應使用`glossary_prompt.txt`產生術語表。
- `FR-P7-006`：如果術語表產生逾時，系統應取代逾時佔位符項目符號。
- `FR-P7-007`：如果最新草稿以 1 級標題開頭，則應在最終報告彙編之前刪除該標題。
- `FR-P7-008`：系統應根據報告正文中的所有二級標題建立 Markdown 目錄。
- `FR-P7-009`：最終報告應包含：
  - 1級最終報告標題
  - 目錄
  - 執行摘要
  - 主體
  - 來源目錄
  - 可選知識庫概述
  - glossary
- `FR-P7-010`：如果需要，系統將嘗試重新定位字數兩次：
  - 一旦在身體上
  - 一旦完成完整的總結報告
- `FR-P7-011`：最終報告字數目標應為：
  - 最小值`9000`
  - 最大`10000`
  - 目標`9500`
- `FR-P7-012`：字數校正應在擴展或壓縮內容時保留標題和核心聲明。
- `FR-P7-013`：最終報告請寫給`<run>/FINAL_REPORT.md`和`<session>/FINAL_REPORT.md`。
- `FR-P7-014`：然後系統將嘗試產生圖像提示和生成 YouTube 腳本。

### 14.9 第 8 階段 - 完成

- `FR-P8-001`：與`current_phase >= 8` 的會話應視為完成。
- `FR-P8-002`：在完成的會話上恢復應列印`Session is complete.`

## 15. 源獲取與轉換規範

### 15.1 URL驗證

- `FR-FETCH-001`：URL 在驗證之前應進行標準化。
- `FR-FETCH-002`：僅接受網路位置的`http` 和`https` URL。
- `FR-FETCH-003`：無效的 URL 將引發 `ValueError`。

### 15.2 HTTP 取得規則

- `FR-FETCH-004`：HTTP 取得應使用使用者代理字串`grok-research-agent/0.1`。
- `FR-FETCH-005`：應遵循重定向。
- `FR-FETCH-006`：逾時分為連接逾時和讀取逾時。
- `FR-FETCH-007`：請求逾時應透過 URL 上下文引發`TimeoutError`。

### 15.3 內容類型處理

- `FR-FETCH-008`：PDF 檢測應使用`Content-Type: application/pdf` 或`.pdf` URL 後綴。
- `FR-FETCH-009`：PDF 包應將提取的文本作為原始文本、主要文本、完整文本和分析文本返回。
- `FR-FETCH-010`：非 HTML 非 PDF 回應應被視為純文字。
- `FR-FETCH-011`：HTML 回應應產生：
  - `main_text` 來自 `readability-lxml` 摘要（如果有）
  - `full_text` 從整頁 HTML 文字中擷取
  - `analysis_text` 作為合併的主/全文或後備內容

### 15.4 HTML 文字規範化

- `FR-FETCH-012`：HTML 提取應刪除`script`、`style`、`noscript` 和`svg` 標籤。
- `FR-FETCH-013`：重複的標準化行應刪除以減少重複的樣板。

## 16.知識編譯規範

### 16.1 編譯器輸入和輸出

- `FR-KB-001`：編譯請先使用筆記本內容，然後在可用時附加擷取的來源檔案。
- `FR-KB-002`：超圖編譯應僅使用內容的第一個`220000`字元。
- `FR-KB-003`：核心概念提取應使用：
  - 來源內容的前 `220000` 字符
  - 超圖 JSON 的第一個 `120000` 字符
- `FR-KB-004`：編譯輸出應寫入：
  - `knowledge_base/hypergraph.json`
  - `knowledge_base/auto_types/auto_hypergraph.json`
  - `knowledge_base/core_concepts.json`

### 16.2 超圖合約

- `FR-KB-005`：提示的超圖模式應為：

```json
{
  "nodes": [{"id": "N1", "label": "..."}],
  "hyperedges": [{"id": "E1", "nodes": ["N1", "N2", "N3"], "relation": "...", "evidence": "..."}]
}
```

- `FR-KB-006`：如果 LLM 未傳回有效的 JSON，系統應保留後備 JSON 包裝器（通常為`{ "raw": "<response>" }`），而不是使指令失敗。

### 16.3 核心概念契約

- `FR-KB-007`：提示的核心概念架構應為：

```json
{
  "core_concepts": [
    {
      "name": "...",
      "definition": "...",
      "why_load_bearing": "..."
    }
  ]
}
```

- `FR-KB-008`：提示需要剛好7個概念，但實作不會獨立強制產生後的計數。

### 16.4 鑽包合約

- `FR-KB-009`：Drill-pack提示輸出模式應為：

```json
{
  "drill_pack_markdown": "markdown string",
  "drill_questions": [
    {
      "concept": "...",
      "questions": [
        {
          "question": "...",
          "answer": "...",
          "pitfalls": ["...", "..."]
        }
      ]
    }
  ]
}
```

- `FR-KB-010`：如果 `drill_pack_markdown` 缺失或為空，系統應從原始回應中移除程式碼圍欄，並將剩餘部分用作 Markdown 輸出。
- `FR-KB-011`：如果解析的JSON缺少`drill_questions`，則整個解析物件應寫為`drill_questions.json`。

### 16.5 提要和超圖更新

- `FR-KB-012`：Feed 應使用 UTF-8 讀取新文件並替換解碼錯誤。
- `FR-KB-013`：提要合併提示應收到：
  - 現有超圖 JSON 的第一個 `160000` 字符
  - 新文檔內容的前`160000`字符
- `FR-KB-014`：更新的超圖輸出應涵蓋兩個規格超圖位置。

### 16.6 美人魚渲染

- `FR-KB-015`：美人魚輸出應以`graph TD`開頭。
- `FR-KB-016`：節點渲染應使用最多第一個`200`節點。
- `FR-KB-017`：邊緣渲染應使用最多第一個`400` 邊緣或超邊緣。
- `FR-KB-018`：對於具有兩個以上成員的超邊，美人魚渲染應僅連接前兩個列出的節點。
- `FR-KB-019`：邊緣標籤應使用`relation` 或`label`（如果存在）。

## 17. 最終報告、圖像提示和 YouTube 腳本規範

### 17.1 最終報告輸出合約

- `FR-OUT-001`：最終報告應為名為`FINAL_REPORT.md`的Markdown文件。
- `FR-OUT-002`：最終報告應包括明確的`## Executive Summary` 和`## Source Catalog` 部分。
- `FR-OUT-003`：如果存在知識庫內容，報告也應包括`## Knowledge Base Overview`。
- `FR-OUT-004`：即使術語表產生逾時，報告也應以術語表部分結束。

### 17.2 影像提示生成

- `FR-OUT-005`：圖像提示應從完整的最終報告中產生。
- `FR-OUT-006`：提示合約要求 5 到 10 個圖像提示，強調具體的機制、工作流程、架構、比較和證據，而不是通用的概念藝術。
- `FR-OUT-007`：如果在最終完善過程中影像提示產生逾時，報表建立仍將成功。

### 17.3 YouTube 腳本生成

- `FR-OUT-008`：系統應主要從 `05_section_drafts/`（如果可用）匯出 YouTube 部分；否則它應從`FINAL_REPORT.md`派生它們。
- `FR-OUT-009`：以下報告部分應排除在敍述來源選擇之外：
  - `Table of Contents`
  - `Source Catalog`
  - `Glossary`
  - `References`
  - `Knowledge Base Overview`
  - `Executive Summary`
- `FR-OUT-010`：產生的腳本應包含：
  - 頂部標題`# YouTube Script`
  - `## Introduction`
  - 每個選定部分一個 2 級標題
  - `## Conclusion`
- `FR-OUT-011`：如果開頭或結尾產生逾時，系統將插入後備佔位符旁白而不是失敗。
- `FR-OUT-012`：如果某個部分產生逾時，則該部分可能會被省略，而腳本的其餘部分將繼續進行。
- `FR-OUT-013`：簡短的介紹、部分或結尾輸出應透過輔助法學碩士調用進行擴展，以達到最低細節閾值。
- `FR-OUT-014`：如果產生的部分缺少 Markdown 標題，系統會自動在前面新增所需的標題。

## 18. 輸入輸出檔規範

### 18.1 會話根輸出

會話根可能包含：

- `session.json`
- `00_scope_confirmed.md`
- `01_discovery_table.md`
- `02_curated_sources.json`
- `03_extracted/`
- `03_source_snapshots/`
- `03_extracted_chunks/`
- `03_extracted_index.txt`
- `04_master_notebook.md`
- `05_section_evidence/`
- `05_section_drafts/`
- `05_draft_vN.md`
- `06_full_sources/`
- `FINAL_REPORT.md`
- `images_to_generate.md`
- `Youtube_Script.md`
- `external_docs/`
- `knowledge_base/`
- `runs/`

### 18.2 知識庫輸出

- `knowledge_base/hypergraph.json`
- `knowledge_base/core_concepts.json`
- `knowledge_base/drill_pack.md`
- `knowledge_base/drill_questions.json`
- `knowledge_base/hypergraph.mmd`
- `knowledge_base/auto_types/auto_hypergraph.json`
- `knowledge_base/feed_docs/<timestamp>_<original_name>`

### 18.3 運轉範圍的輸出

- 建置工作流程上下文的每個命令執行都可以建立生成的工件的運行本機副本，以進行可追蹤性和偵錯。

## 19. 驗證規則

### 19.1 CLI 驗證

- 所需的標誌應由 `argparse` 強制執行。
- 透過 CLI 公開的不受支援的 `compile --type` 值無法通過解析器驗證。
- 透過 CLI 公開的不受支援的 `drill --mode` 值無法通過解析器驗證。

### 19.2 語意驗證

- 策劃來源驗證是結構化的、盡力而為的，而不是透過專用驗證器進行的嚴格模式驗證。
- 發現輸出未經結構驗證。
- 最終報告內容未經過語義驗證以確保事實正確性。
- 核心概念計數受到提示限制，但未經事後驗證。

### 19.3 文件驗證

- `feed` 驗證文件存在和常規文件狀態。
- 外部文件驗證根目錄是否存在以及支援的後綴。
- 會話清單驗證`session.json` 的存在。

## 20. 錯誤處理與恢復規範

### 20.1 Grok API 錯誤

- `FR-ERR-001`：缺少 API 金鑰將引發 `GrokError("Missing GROK_API_KEY in .env or environment")`。
- `FR-ERR-002`：與配額/計費相關的 API 錯誤應使用可操作文字對應到 `GrokQuotaError`。
- `FR-ERR-003`：類似逾時的 API 錯誤應對應到 `GrokTimeoutError`，包括配置的逾時秒數。
- `FR-ERR-004`：非逾時非配額 API 故障應重試最多 `5` 次，指數退避上限為 `30` 秒。
- `FR-ERR-005`：映射後，`GrokClient.chat_text()` 中不會重試配額和超時錯誤。

### 20.2 LLM 超時容忍

- `FR-ERR-006`：選定的階段使用`_llm_optional()`將LLM逾時失敗轉換為警告並繼續：
  - 差距分析
  - 開採計劃
  - 提取區塊
  - 部分證據包
  - 部分草稿
  - revision
  - 執行摘要
  - glossary
  - 影像提示
  - YouTube 簡介/片段/結尾
  - 字數重定向
- `FR-ERR-007`：當`_llm_optional()`處理逾時時，系統應列印警告並繼續，除非呼叫功能需要明確輸出才能繼續。

### 20.3 來源獲取錯誤

- `FR-ERR-008`：來源獲取失敗不應中止整個提取或完整收集階段。
- `FR-ERR-009`：逾時取得應引發`TimeoutError`；呼叫者可以記錄並跳過來源。

### 20.4 JSON的穩健性

- `FR-ERR-010`：系統在嘗試解析類似 JSON 的模型輸出時應移除 Markdown 程式碼圍欄。
- `FR-ERR-011`：系統應在回退到原始包裝器 JSON 之前嘗試直接解析、括號切片解析和大括號切片解析。
- `FR-ERR-012`：無效的策劃來源 JSON 應觸發發現連結的啟發式復原。

### 20.5 非致命降級規則

- `FR-ERR-013`：缺少外部文件不應阻礙研究工作流程。
- `FR-ERR-014`：第 6 階段中缺少精選源應降級為跳過行為而不是致命失敗。
- `FR-ERR-015`：缺少超圖或核心概念應產生指導性控制台訊息，而不是未捕獲的故障。
- `FR-ERR-016`：缺少圖像或 YouTube 產生的最終報告應產生指導性控制台訊息。

## 21. 整合規範

### 21.1 xAI Grok 集成

- 協定：OpenAI 相容的聊天完成 API
- 基本網址：`https://api.x.ai/v1`
- Auth：透過環境提供的持有者 API 金鑰
- 訊息結構：每次調用一條系統訊息和一條用户訊息
- 回應處理：首先完成選擇訊息內容或空字串

### 21.2 遠端 Web 集成

- 協定：HTTP/HTTPS GET
- 重定向：已啟用
- 認證：無
- SSL 行為：委託`requests`
- 故障處理：錯誤向呼叫者冒泡或按階段捕獲並在設計時降級為警告

### 21.3 本地文檔集成

- 外部文件支援`.pdf`、`.docx`、`.txt`、`.md`
- Feed 命令支援在文件開啟層級更廣泛，但使用文字解碼並且適用於文字文檔

## 22. 安全和隱私要求

- `FR-SEC-001`：API金鑰應從環境或`.env`讀取；系統不應將它們寫入會話工件。
- `FR-SEC-002`：研究會話目錄可以儲存獲取的遠端內容和本地處理的外部文件；這些文件應被視為潛在敏感文件。
- `FR-SEC-003`：系統在儲存之前不對所取得的內容執行秘密編輯。
- `FR-SEC-004`：系統對會話目錄不進行存取控制。

## 23. 具有功能影響的非功能約束

- 本機優先持久性意味著在每個主要步驟之後都必須在磁碟上檢查所有關鍵工件。
- 可恢復性取決於 `current_phase` 和檔案存在，而不是交易日誌或資料庫狀態。
- 確定性是部分的：檔案名稱和工作流程轉換是確定性的，但內容是 LLM 產生的，因此是機率性的。
- 並發是有限的：
  - 獲取工人：`4`
  - 採掘工人：`2`
  - 科證人員：`2`
- 大型文字處理使用基於字元的截斷和分塊，而不是令牌精確分段。

## 24. 目前實施説明和已知的功能差距

- `mode` 儲存在會話狀態中，但目前不會變更系統行為。
- `run_history` 存在於會話模式中，但未填充。
- `list-types` 僅公開`auto-hypergraph`，即使內部常數列出了幾個休眠自動類型。
- 互動式指導字串提到`add-section`和`gap-check`，但沒有本地解析器強制執行這些命令；它們作為修訂回饋逐字傳遞。
- 最終報告包括僅源自 2 級標題的生成目錄。
- 美人魚生成僅使用前兩個成員將超邊簡化為成對連結。
- 發現和最終報告的事實準確性取決於模型輸出和來源品質；系統不執行自動事實驗證。

## 25. 驗收標準

當滿足以下所有條件時，當前實作應被視為在其預期範圍內功能完整：

- 可以使用唯一的會話 ID 建立新會話並保留 `session.json`。
- 互動式工作流程進展可以將會話從階段 0 移動到階段 8，並具有預期的人工檢查點。
- 自動模式無需呼叫`input()`即可完成工作流程。
- Discovery 創建`01_discovery_table.md`。
- 管理創建`02_curated_sources.json` 和差距報告。
- 提取建立來源快照、提取的區塊和來源達析報告。
- 筆記本程序集創建`04_master_notebook.md`。
- 合成至少創建一個`05_draft_vN.md`。
- 最後的拋光創建`FINAL_REPORT.md`。
- 最終的拋光或顯式命令可以創建`images_to_generate.md`和`Youtube_Script.md`。
- 編譯在 `knowledge_base/` 下方建立超圖和核心概念輸出。
- Drill 創建`drill_pack.md` 和`drill_questions.json`。
- Feed 儲存帶有時間戳記的文件副本，並且可以更新或初始化超圖輸出。
- 顯示創建`hypergraph.mmd`。
- 外部文件在提供時會被處理為清單、提取的摘要和上下文輸出，而不會因部分故障而阻塞工作流程。

## 26. 可追溯性總結

該規範反映了以下中實現的行為：

- `grok_research_agent/cli.py`
- `grok_research_agent/session_manager.py`
- `grok_research_agent/grok_client.py`
- `grok_research_agent/external_docs.py`
- `grok_research_agent/workflow_phases.py`
- `grok_research_agent/prompts/*.txt`
- `tests/test_cli.py`
- `tests/test_session_manager.py`
- `tests/test_external_docs.py`
- `tests/test_workflow_happy_path.py`
