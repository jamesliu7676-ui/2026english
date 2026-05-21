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
