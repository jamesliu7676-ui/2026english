# 2026english

2026 高中學測英文診斷、補強與練習工具專案。

## Project Status

This repository is currently focused on helping a student prepare for Taiwan's 高中學測英文 through diagnostic testing, targeted vocabulary review, wrong-answer recovery, and short daily practice.

## Working Files

- `AGENTS.md`: fixed project rules and Codex operating instructions.
- `docs/project_dashboard.md`: project progress, decisions, and next steps.
- `web/index.html`: browser-based 高中學測英文 diagnostic interface.
- `web/question-bank.js`: randomized 高中學測英文 diagnostic question bank with A1, A2, B1, and B2 levels.
- `web/frequency-data.js`: frequency-ranked words, phrases, and grammar points for the web interface.
- `web/news-keywords.js`: recent news keyword set for current-affairs vocabulary.
- `web/question-type-stats.js`: past five-year English question-type statistics for item design.
- `web/question-modules.js`: web data for question-type training modules.
- `scripts/build_exam_frequency.py`: rebuilds frequency data from the external past-exam text extraction project.
- `scripts/validate_question_bank.py`: validates formal question bank files.
- `scripts/generate_practice_plan.py`: generates a 7-day GSAT English practice plan from open errors, frequency data, news keywords, and the formal question bank.
- `data/vocabulary_seed.csv`: starter vocabulary list for high-frequency practice.
- `data/exam_frequency_seed.csv`: import-ready frequency table for past exam words, phrases, and grammar points.
- `data/news_keyword_seed.csv`: recent English news keyword seed list.
- `data/question_type_stats.csv`: 111-115 GSAT English question-type statistics.
- `data/question_module_seed.csv`: module plan for reading, discourse, cloze, fill-in, and writing practice.
- `data/question_module_examples.json`: first seed examples for each question module.
- `data/question_bank/`: formal expandable question bank split by module.
- `data/source_strategy.md`: source expansion rules for the vocabulary and question pool.
- `data/error_log.csv`: starter wrong-answer tracking table.
- `templates/daily_practice.md`: daily 30-minute practice template.
- `templates/weekly_review.md`: weekly review template.
- `docs/practice_plans/`: generated student practice plans.
- `.gitignore`: local secrets, tooling caches, and generated files that should not be committed.

## Current Assumptions

- Primary working language is Traditional Chinese.
- English content should prioritize 高中學測英文: vocabulary in context, grammar and cloze-style judgment, reading comprehension, translation/writing output, and test strategy.
- Student-identifying data should be anonymized.

## Web Preview

Open `web/index.html` directly, or run a local static server from the project root and visit the preview URL.

The diagnostic page targets 高中學測英文 and redraws a new 20-question set on every page load. It samples 4 questions from each skill area:

- vocabulary
- grammar
- reading
- writing
- strategy

The difficulty selector controls the question pool. For example, A2 samples from A1-A2, while B2 samples from A1-B2. In this project, the levels mean:

- A1: 學測基礎補洞
- A2: 學測核心題
- B1: 學測閱讀推論
- B2: 學測高分挑戰

In the past-exam frequency section, students can mark a word, phrase, or grammar point as familiar. The page hides that item, shows the next item in the queue, and stores the familiar list in the browser's local storage.

## Next Step

Use the diagnostic interface with a student, then turn the weakest categories into a 7-day 高中學測英文 practice set.

Generate a sample practice plan:

```powershell
py scripts\generate_practice_plan.py --student-id SAMPLE --start-date 2026-05-25
```

The generated Markdown file is written to `docs/practice_plans/`. Use anonymous student IDs only.

## Frequency Data

The current frequency data is generated from:

`G:\我的雲端硬碟\歷屆試題\分析輸出\文字抽取`

Included source files:

- `111-英文.txt`
- `112-英文.txt`
- `113-英文.txt`
- `114-英文.txt`
- `115-英文.txt`

Rebuild command:

```powershell
py scripts\build_exam_frequency.py
```

The frequency table uses these fields:

- `type`: `word`, `phrase`, or `grammar`
- `text`: target word, phrase, or grammar point
- `frequency`: observed count in the past exam set
- `level`: `high`, `medium`, or `low`
- `meaning`: Traditional Chinese explanation
- `example`: exam-style example

The web page color-codes the levels: red for high frequency, orange for medium frequency, and green for low frequency.

Current method:

- Words: counted from extracted exam text, filtered to terms appearing in at least two academic years.
- Phrases: counted from a curated GSAT-relevant phrase pattern list.
- Grammar: estimated from rule-based text patterns, not official grammar tagging.

## Vocabulary Pool Design

The vocabulary question pool should combine two sources:

- Past-exam frequency: high-frequency words and phrases from 111-115 GSAT English extracted text.
- Recent news: keywords from the past two months of English-language magazines or newspapers, prioritizing TIME, The Guardian, Reuters/CommonWealth English, The Economist, and similar sources.

The goal is to strengthen both baseline exam vocabulary and current-affairs vocabulary.

Current target mix:

- 60% past-exam high-frequency vocabulary and phrases
- 30% recent English news keywords
- 10% diagnostic wrong-answer recovery

See `data/source_strategy.md` for source tiers, update cadence, and quality rules.

## Question-Type Reference

Past five-year English question-type statistics are used as a guide for question-bank expansion:

- 詞彙與語意：71.1%
- 閱讀理解：20.2%
- 寫作表達：5.2%
- 篇章與文意：3.5%

This ratio is a training reference, not an official exam blueprint.

## Question Modules

The next question-bank expansion is organized into modules:

- 閱讀測驗
- 篇章結構
- 文意選填
- 填字 / 綜合測驗
- 翻譯與寫作

Each module has its own source basis, focus skills, and seed examples so it can be expanded without mixing unrelated item types.

Formal question bank files live in `data/question_bank/`:

- `reading.json`
- `discourse.json`
- `cloze.json`
- `fill_blank.json`
- `translation.json`

Run this after adding questions:

```powershell
py scripts\validate_question_bank.py
```
