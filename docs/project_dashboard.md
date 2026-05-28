# 2026english 專案駕駛艙

## 專案定位

2026 高中學測英文診斷、補強與練習工具專案。

第一個具體用途：把診斷界面放到網頁上，協助準備高中學測英文的學生快速找出弱點，並產生優先補強方向。

## 今日初始化紀錄

- 日期：2026-05-21
- 工作資料夾：`G:\我的雲端硬碟\2026english`
- 狀態：新資料夾，本地初始化
- 已建立：
  - `AGENTS.md`
  - `README.md`
  - `.gitignore`
  - `docs/project_dashboard.md`
  - `web/index.html`
  - `data/vocabulary_seed.csv`
  - `data/exam_frequency_seed.csv`
  - `data/news_keyword_seed.csv`
  - `data/question_type_stats.csv`
  - `data/question_module_seed.csv`
  - `data/question_module_examples.json`
  - `data/question_bank/README.md`
  - `data/question_bank/schema.json`
  - `data/question_bank/reading.json`
  - `data/question_bank/discourse.json`
  - `data/question_bank/cloze.json`
  - `data/question_bank/fill_blank.json`
  - `data/question_bank/translation.json`
  - `data/question_bank/expansion_plan.md`
  - `data/source_strategy.md`
  - `data/error_log.csv`
  - `templates/daily_practice.md`
  - `templates/weekly_review.md`
  - `web/frequency-data.js`
  - `web/news-keywords.js`
  - `web/question-type-stats.js`
  - `web/question-modules.js`
  - `scripts/validate_question_bank.py`
  - `scripts/generate_practice_plan.py`
  - `docs/practice_plans/2026-05-25_SAMPLE_7_day_practice.md`
- Git：
  - 已執行本地 `git init`
  - 已設定 `windows.appendAtomically=false`
  - 尚未建立第一次 commit
  - 尚未設定 GitHub 遠端

## 固定規則摘要

- 先檢查現況，再補缺口。
- 不自動 pull、commit、push。
- 固定規則放 `AGENTS.md`。
- 進度、決策、下一步放本檔。
- 不保存學生真實姓名；學生資料需匿名化。
- 不提交秘密資訊、`.env`、`.codex/`、`.claude/`。

## 待確認

- 是否要把快篩題目改成特定考試版本，例如會考、學測或校內段考？
- 是否需要儲存診斷結果，或目前先維持瀏覽器內即時計算？
- 是否需要建立 GitHub 遠端？
- 是否要把專案駕駛艙移到 Obsidian vault，或維持在 repo 內？
- 是否要把診斷結果串成單字表、錯題本與每日練習產生器？
- 是否要擴充成正式學測題型包：綜合測驗、文意選填、篇章結構、閱讀測驗、翻譯、英文作文？
- 是否要把已抓取的近五年歷屆試題統計匯入 `data/exam_frequency_seed.csv` 與 `web/frequency-data.js`，取代目前示範資料？

## 診斷頁設計

- 題目已改成題庫抽題，不再固定同一組。
- 每次重新整理頁面會重新抽 20 題。
- 可在頁面上按「重新抽題」立即換題。
- 題庫位置：`web/question-bank.js`
- 抽題方式：單字、文法句構、閱讀、作文輸出、考試策略各抽 4 題。
- 分級方式：
  - A1：只抽學測基礎補洞題。
  - A2：抽 A1-A2 學測核心題。
  - B1：抽 A1-A2-B1 學測閱讀推論題。
  - B2：抽 A1-A2-B1-B2 學測高分挑戰題。

## 歷屆試題頻率分級

- 頁面已加入近五年歷屆試題高頻項目區塊。
- 可切換單字、片語、文法。
- 單字、片語、文法卡片可按「已熟悉，換下一個」。
- 已熟悉項目會存在瀏覽器本機，畫面自動補下一個項目。
- 可按「復原熟悉項目」重置目前分類。
- 顏色分級：
  - 紅色：高頻
  - 橘色：中頻
  - 綠色：低頻
- 目前資料檔：
  - `data/exam_frequency_seed.csv`
  - `web/frequency-data.js`
- 目前已接入來源：`G:\我的雲端硬碟\歷屆試題\分析輸出\文字抽取`
- 統計範圍：111-115 學年度英文試題文字抽取，共 5 份。
- 產生腳本：`scripts/build_exam_frequency.py`
- 統計口徑：
  - 單字：從抽取文字計數，且至少出現在兩個學年度。
  - 片語：依學測常見片語清單做字面比對。
  - 文法：依規則線索估算，非官方文法標註。

## 單字題庫組成規則

- 第一來源：111-115 學年度高中學測英文試題高頻單字、片語與文法。
- 第二來源：近兩個月重大英文新聞時事關鍵字。
- 新聞來源優先順序：
  - 英文雜誌：TIME、The Economist 等。
  - 英文報導/郵報/新聞：Reuters、The Guardian、CommonWealth English 等。
- 題庫目的：
  - 補強學測基礎單字與高頻語意。
  - 加入時事常見用字，提高閱讀素養題與作文可用詞彙。
- 題庫比例第一版：
  - 60%：考古題高頻單字與片語
  - 30%：近兩個月英文新聞關鍵字
  - 10%：學生診斷錯題回收
- 來源策略檔：`data/source_strategy.md`

## 題型統計出題參考

來源：`G:\我的雲端硬碟\歷屆試題\分析輸出\單元頻率.csv`

111-115 學年度英文題型統計：

- 詞彙與語意：123 題段，約 71.1%
- 閱讀理解：35 題段，約 20.2%
- 寫作表達：9 題段，約 5.2%
- 篇章與文意：6 題段，約 3.5%

用途：作為題庫擴充比例參考，不視為官方命題藍圖。

## 題型訓練模組

已建立五個可擴充模組：

- 閱讀測驗：主旨、細節、推論、作者態度。
- 篇章結構：句子插入、段落排序、文意銜接、轉折線索。
- 文意選填：語境選字、搭配詞、轉折詞、語意一致。
- 填字/綜合測驗：詞性、片語、文法結構、語意判斷。
- 翻譯與寫作：中翻英、句型、連接詞、段落表達。

目前已建立模組規格與種子題；下一步是把每個模組擴成可抽題的題庫。

## 正式題庫架構

正式題庫已建立於 `data/question_bank/`：

- `reading.json`
- `discourse.json`
- `cloze.json`
- `fill_blank.json`
- `translation.json`

每題共用欄位定義在 `data/question_bank/schema.json`。

每次擴題後執行：

```powershell
py scripts\validate_question_bank.py
```

目前驗證結果：通過，50 題。

第一輪充實題庫：

- 文意選填：已擴充到 10 題。
- 填字/綜合測驗：已擴充到 10 題。
- 閱讀測驗：已擴充到 10 題。
- 篇章結構：已擴充到 10 題。
- 翻譯與寫作：已擴充到 10 題。

## 7 天練習計畫產生器

已建立 `scripts/generate_practice_plan.py`，可把開放中錯題、近五年高頻單字/片語、近兩個月新聞關鍵字與正式題庫整合成 Markdown 練習計畫。

範例指令：

```powershell
py scripts\generate_practice_plan.py --student-id SAMPLE --start-date 2026-05-25
```

目前範例輸出：

- `docs/practice_plans/2026-05-25_SAMPLE_7_day_practice.md`

產生器規則：

- 只使用匿名學生 ID。
- 依 `data/error_log.csv` 的開放中錯題排序弱點。
- 每天安排高頻單字、片語、新聞關鍵字、正式題庫題目、錯題回收與短寫作。
- 若沒有開放中錯題，會以單字、閱讀、文法、寫作、策略作為預設補強順序。

## 網頁練習計畫區塊

已把 7 天練習計畫範例放到 `web/index.html`：

- 區塊標題：`7 天練習計畫範例`
- 可切換 Day 1-Day 7。
- 每天顯示補強重點、題型主軸、高頻單字/片語/新聞關鍵字、題型練習、錯題回收與寫作輸出。
- 診斷完成後的個人化 7 天安排仍保留在診斷結果區。
- 本機預覽：`http://localhost:8765/index.html`

## 每日英文影片分享

首頁已移除「近五年題型統計出題參考」與「題型訓練模組」兩個可見區塊，原位置改放「每日英文影片分享」。

目前來源入口：

- `https://www.facebook.com/profile.php?id=100089836585396&sk=reels_tab`
- 前端來源資料庫：`web/daily-video-sources.js`

使用方式：

- 保留原始 Facebook Reel 連結，不下載或重傳影片。
- 網頁每次重新載入時，會從 `window.dailyVideoSources` 隨機挑選一筆可分享內容。
- 每日可新增一支影片直接連結到 `web/daily-video-sources.js`。
- 搭配今日英文重點、3 個單字、1 個句型與 3 句仿寫任務。
- 單支 Facebook Reel 會直接以 iframe 內嵌在首頁播放；來源頁入口保留在資料庫但不參與內嵌抽選。
- 影片預設依 Reel 使用直式比例；若加入橫式影片，可在該筆資料加上 `orientation: "horizontal"`。

## 下一步建議

1. 以高中學測英文作為 `2026english` 的核心用途。
2. 用 `web/index.html` 跑一次學生快篩。
3. 把診斷摘要轉入 `data/error_log.csv` 與每日練習模板。
4. 依快篩結果擴充學測核心單字與題型題庫。
5. 擴充片語與文法規則清單，使頻率表更接近正式學測題型。
6. 建立新聞關鍵字定期更新流程。
7. 逐步擴充閱讀測驗、篇章結構、文意選填、填字/綜合測驗、翻譯與寫作題庫。
8. 擴充題庫產生器，依 60/30/10 與題型比例規則自動抽題。
9. 若需要版本管理，完成第一次本地 commit。

## 2026-05-25 收工紀錄

今日完成：

- 建立 7 天學測英文練習計畫產生器，並產出 SAMPLE 範例。
- 將 7 天練習計畫範例放入首頁。
- 將首頁「近五年題型統計出題參考」與「題型訓練模組」可見區塊替換成「每日英文影片分享」。
- 建立 `web/daily-video-sources.js`，目前共 51 筆來源，其中 50 支為單一 Facebook Reel。
- 首頁每日影片分享會從單支 Reel 中隨機抽選，並以 Facebook iframe 內嵌播放。
- GitHub repository 已改為 Public，GitHub Pages 已啟用並部署成功。

目前狀態：

- 本機預覽：`http://localhost:8765/index.html`
- 外部網址：`https://jamesliu7676-ui.github.io/2026english/`
- Git 狀態：`master...origin/master` 已同步。
- 最新主要 commits：
  - `d8ae126 Enable GitHub Pages deployment`
  - `bb0b692 Add daily Reel video embeds`
  - `415080d Add practice plan preview to web page`

注意事項：

- Facebook Reel 內嵌播放仍受 Facebook 登入、隱私、地區與嵌入權限限制；若某支無法內嵌，頁面仍保留「開啟原始影片」連結。
- Reel 預設直式比例；若未來新增橫式影片，該筆來源需加 `orientation: "horizontal"`。
- Git 操作仍偶爾出現 `.git/packed-refs.lock` 殘留訊息，但 commit/push 已可正常完成。

下次建議：

1. 在外部網址實際測試多次重新整理，確認隨機 Reel 與 iframe 顯示狀態。
2. 逐步替每支 Reel 補更精準的 `topic`、`keywords`、`sentencePattern` 與 `writingPrompt`。
3. 若要讓學生每日固定同一支影片，可把隨機抽選改成依日期選片。

後續追加：

- 診斷送出後，若學生答錯，會在該題下方顯示「講解」欄位。
- 題庫若有 `explanation` 會優先使用；沒有時依題型產生基本講解，提示正解與解題方向。
- 講解已加入答案中文翻譯：顯示學生答案中文、正解中文與解題方向；未收錄的選項會標示「待補中文翻譯」。
- 講解已加入題目整句中文翻譯；未收錄的題幹會標示「待補題目中文翻譯」。
- 首頁已新增「克漏字練習」與「閱讀測驗練習」兩個獨立區塊，從 `web/practice-question-bank.js` 各抽 3 題，可重新抽題並在檢查後顯示正解與解析。

最後同步狀態：

- 講解格式已依範例調整為「題目翻譯 / 你的選項是 / 答案是 / 解題方向」。
- 已 commit 並 push：`f1c0b3c Add translated answer explanations`
- Reel 來源資料庫已擴充並 push：`c87f80d Expand daily Reel source database`
- 克漏字練習與閱讀測驗練習區塊已新增並 push：`c3f557d Add cloze and reading practice sections`
- GitHub Pages 部署成功，外部網址回應 `200`。
- 目前 Git 狀態：`master...origin/master`。

## 2026-05-28 收工記錄

本次完成：

- 新增 `reading_tests/` 短篇閱讀測驗題庫資料夾。
- 建立閱讀題庫格式說明、來源登錄、短版與標準版模板。
- 新增閱讀測驗樣本：`reading_001.md`、`reading_002_sample_full.md`、`reading_003_standard.md`。
- 建立結構化題庫 `reading_tests/question_bank.json`，目前 5 篇閱讀文本、41 題。
- 建立互動頁面 `reading_tests/quiz.html`，可讀取題庫並更新題目。
- 建立免伺服器預覽頁 `reading_tests/quiz_preview.html`，方便直接看版面。
- 寫入補題計劃 `reading_tests/replenishment_plan.md`，目標擴充到 200 題以上。
- 已建立每週一 09:00 的補題排程：每批新增 5 篇、約 40 題，可加入經查證的時事題。
- 已 commit 並 push：`0e00f3c Add reading test question bank`。

目前狀態：

- 題型已覆蓋：主旨題、細節題、推論題、字彙題、代名詞指涉題、句意理解題、段落排序、多文本整合題、圖表閱讀題、混合題。
- `question_bank.json` 已用 UTF-8 JSON 解析檢查通過。
- `quiz.html` 若直接用 `file://` 開啟，可能無法讀取 JSON；正式預覽建議用本機伺服器。
- wmux 右側瀏覽器目前未啟動，無法用 wmux 預覽。
- Git 遠端已同步到 `origin/master`；但 `docs/project_dashboard.md` 有本收工紀錄，尚未提交。

下一步建議：

1. 啟動本機伺服器預覽 `reading_tests/quiz.html`。
2. 每週補題排程先跑 1-2 次後，檢查題目品質、時事題來源標記與重複率。
3. 題庫達 120 題後，再調整抽題邏輯，加入主題篩選與題型篩選。
4. 題庫達 200 題後，整理成學生練習版與教師答案版。
