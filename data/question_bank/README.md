# 高中學測英文題庫架構

此資料夾放正式可擴充題庫。每個題型獨立一個 JSON 檔，避免閱讀、文意選填、綜合測驗與寫作題混在一起。

## 題型檔案

| 檔案 | 題型 | 用途 |
|---|---|---|
| `reading.json` | 閱讀測驗 | 主旨、細節、推論、作者態度 |
| `discourse.json` | 篇章結構 | 句子插入、段落排序、文意銜接 |
| `cloze.json` | 文意選填 | 語境選字、搭配詞、篇章線索 |
| `fill_blank.json` | 填字/綜合測驗 | 詞性、片語、文法結構、語意判斷 |
| `translation.json` | 翻譯與寫作 | 中翻英、句型、段落表達 |

## 共用欄位

- `id`: 題目唯一代號。
- `moduleId`: 題型模組代號。
- `level`: `A1`, `A2`, `B1`, `B2`。
- `sourceType`: `past_exam`, `news`, `manual`, `diagnostic_error`。
- `sourceRef`: 來源說明或 URL。
- `topic`: 題目主題。
- `focus`: 訓練重點。
- `passage`: 題幹文章或語境，可留空。
- `question`: 題目。
- `options`: 選項陣列；非選題可留空陣列。
- `answer`: 正解。
- `explanation`: 解題說明。
- `tags`: 標籤陣列。

## 檢查

每次擴題後執行：

```powershell
py scripts\validate_question_bank.py
```
