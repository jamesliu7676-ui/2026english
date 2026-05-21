# AGENTS.md instructions for G:\我的雲端硬碟\2026english

<INSTRUCTIONS>
<!-- wmux:start — AUTO-MANAGED BY wmux. Do not edit this section manually. -->

# wmux

You are running inside wmux v2.6.0, a terminal multiplexer with a browser panel on the right side that the user can see in real-time.

## Browser

For any web browsing task, use the wmux MCP tools so the user can watch in the browser panel. Do NOT use Playwright, Firecrawl, or WebSearch — they open invisible windows the user cannot see. If the user explicitly asks for one of those tools, use it.

| 動作 | MCP 工具 |
|------|----------|
| 開啟網頁 | `browser_navigate` (url) |
| 取得頁面結構 | `browser_snapshot` 或 `browser_smart_snapshot` |
| 點擊元素 | `browser_click` (ref) |
| 輸入文字 | `browser_type` (ref, text) |
| 填入表單 | `browser_fill` (fields) |
| 取得頁面文字 | `browser_extract_text` |
| 截圖 | `browser_screenshot` |
| 執行 JS | `browser_evaluate` (expression) |
| 上一頁 | `browser_navigate_back` |
| 重新整理 | `browser_navigate` (same url) |

Workflow: `browser_navigate` → `browser_smart_snapshot` → read refs → `browser_click/type` → `browser_smart_snapshot` again.

Refs expire after page changes — always re-snapshot.

<!-- wmux:end -->

## Obsidian 筆記本固定路徑

主要 Obsidian Vault：

`G:\我的雲端硬碟\secondbrain`

當我說「Obsidian」、「Secondbrain」、「我的筆記本」、「第二大腦」時，預設指這個資料夾。

若任務涉及筆記、教學素材、專案駕駛艙、工作流程、索引整理，請優先參考：

- `G:\我的雲端硬碟\secondbrain\AGENTS.md`
- `G:\我的雲端硬碟\secondbrain\知識庫\index.md`
- `G:\我的雲端硬碟\secondbrain\知識庫\log.md`

可協助讀取、整理、建立、修改 `.md` 筆記；但實際寫入權限以 Codex App 當次工作區授權與 MCP 設定為準。

## 知識重整提醒

如果今天是週日，且本週尚未做過知識重整，請在對話開始時提醒使用者：
「今天要不要跑一次 Obsidian 每週知識重整？」

只有在使用者同意後才執行。

## 本專案固定規則

- 專案資料夾：`G:\我的雲端硬碟\2026english`
- 預設工作語言：繁體中文；英文內容依任務需要保留英文。
- 預設定位：2026 英文學習、教學素材與練習工具專案；若使用者提供更精確用途，以使用者新定義為準。
- 先檢查現況，再補缺口；不得覆蓋既有 `AGENTS.md`、`README.md`、`.gitignore`、Git 歷史或教材資料。
- 固定規則放在 `AGENTS.md`；進度、待辦、決策放在 `docs/project_dashboard.md`。
- 不自動 pull、commit、push；只有使用者明確要求時才提交或推送。
- 不保存學生真實姓名；若需要學生資料，使用班級代碼、座號或匿名 ID。
- 不提交秘密資訊、帳密、API key、`.env`、`.codex/`、`.claude/`。
- Google Drive 同步資料夾內的 Git 專案，使用 `git config windows.appendAtomically false`。
</INSTRUCTIONS>
