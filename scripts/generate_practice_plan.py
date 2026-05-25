import argparse
import csv
import json
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
QUESTION_BANK_DIR = DATA_DIR / "question_bank"
DEFAULT_OUTPUT_DIR = ROOT / "docs" / "practice_plans"

QUESTION_FILES = [
    "reading.json",
    "discourse.json",
    "cloze.json",
    "fill_blank.json",
    "translation.json",
]

MODULE_LABELS = {
    "reading": "閱讀測驗",
    "discourse": "篇章結構",
    "cloze": "文意選填",
    "fill_blank": "填字 / 綜合測驗",
    "translation": "翻譯與寫作",
}

SKILL_TO_MODULES = {
    "vocabulary": ["cloze", "fill_blank"],
    "grammar": ["fill_blank", "discourse"],
    "reading": ["reading", "discourse"],
    "writing": ["translation"],
    "strategy": ["reading", "discourse"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a 7-day GSAT English practice plan from errors and question banks."
    )
    parser.add_argument("--student-id", default="SAMPLE", help="Anonymous student id.")
    parser.add_argument(
        "--start-date",
        default=date.today().isoformat(),
        help="First practice date in YYYY-MM-DD format.",
    )
    parser.add_argument("--days", type=int, default=7, help="Number of practice days.")
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory for the generated Markdown plan.",
    )
    return parser.parse_args()


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def load_question_bank() -> dict[str, list[dict]]:
    bank = {}
    for file_name in QUESTION_FILES:
        path = QUESTION_BANK_DIR / file_name
        module_id = path.stem
        bank[module_id] = json.loads(path.read_text(encoding="utf-8"))
    return bank


def load_open_errors(student_id: str) -> list[dict]:
    path = DATA_DIR / "error_log.csv"
    if not path.exists():
        return []

    errors = []
    for row in read_csv(path):
        if row.get("student_id") != student_id:
            continue
        if row.get("status", "").lower() == "closed":
            continue
        errors.append(row)
    return errors


def rank_focus_skills(errors: list[dict]) -> list[str]:
    if not errors:
        return ["vocabulary", "reading", "grammar", "writing", "strategy"]

    counts = Counter(row.get("skill") or row.get("type") for row in errors)
    ranked = [skill for skill, _ in counts.most_common() if skill]
    for fallback in ["vocabulary", "reading", "grammar", "writing", "strategy"]:
        if fallback not in ranked:
            ranked.append(fallback)
    return ranked


def build_module_priority(skills: list[str]) -> list[str]:
    priority = []
    for skill in skills:
        for module_id in SKILL_TO_MODULES.get(skill, []):
            if module_id not in priority:
                priority.append(module_id)
    for module_id in MODULE_LABELS:
        if module_id not in priority:
            priority.append(module_id)
    return priority


def pick_cycle(items: list[dict], index: int, count: int) -> list[dict]:
    if not items:
        return []
    return [items[(index + offset) % len(items)] for offset in range(count)]


def group_frequency_items() -> dict[str, list[dict]]:
    items = read_csv(DATA_DIR / "exam_frequency_seed.csv")
    grouped = defaultdict(list)
    level_rank = {"high": 0, "medium": 1, "low": 2}
    for item in items:
        grouped[item["type"]].append(item)
    for key in grouped:
        grouped[key].sort(key=lambda row: (level_rank.get(row.get("level"), 9), -int(row["frequency"])))
    return grouped


def build_daily_plan(
    day_index: int,
    practice_date: date,
    skills: list[str],
    module_priority: list[str],
    question_bank: dict[str, list[dict]],
    frequency_items: dict[str, list[dict]],
    news_keywords: list[dict],
    open_errors: list[dict],
) -> str:
    focus_skill = skills[day_index % len(skills)]
    primary_module = module_priority[day_index % len(module_priority)]
    secondary_module = module_priority[(day_index + 1) % len(module_priority)]

    words = pick_cycle(frequency_items.get("word", []), day_index * 3, 3)
    phrases = pick_cycle(frequency_items.get("phrase", []), day_index * 2, 2)
    news = pick_cycle(news_keywords, day_index * 2, 2)
    questions = pick_cycle(question_bank.get(primary_module, []), day_index * 2, 2)
    questions.extend(pick_cycle(question_bank.get(secondary_module, []), day_index, 1))
    error = open_errors[day_index % len(open_errors)] if open_errors else None

    lines = [
        f"## Day {day_index + 1}｜{practice_date.isoformat()}",
        "",
        f"- 今日優先補強：{focus_skill}",
        f"- 題型主軸：{MODULE_LABELS.get(primary_module, primary_module)}",
        "- 建議時間：30 分鐘",
        "",
        "### 1. 單字主動回想",
        "",
        "| 項目 | 中文提示 | 來源 | 例句 / 線索 |",
        "|---|---|---|---|",
    ]

    for item in words:
        lines.append(f"| {item['text']} | {item['meaning']} | 近五年考古題 | {item['example']} |")
    for item in phrases:
        lines.append(f"| {item['text']} | {item['meaning']} | 近五年考古題 | {item['example']} |")
    for item in news:
        lines.append(f"| {item['keyword']} | {item['meaning_zh']} | 近兩個月新聞 | {item['example']} |")

    lines.extend([
        "",
        "### 2. 題型練習",
        "",
    ])

    for number, question in enumerate(questions, start=1):
        options = " / ".join(question["options"])
        passage = question.get("passage", "").strip()
        if passage:
            lines.append(f"{number}. {question['question']}  ")
            lines.append(f"   - 題型：{MODULE_LABELS.get(question['moduleId'], question['moduleId'])}｜{question['focus']}")
            lines.append(f"   - 短文：{passage}")
        else:
            lines.append(f"{number}. {question['question']}")
            lines.append(f"   - 題型：{MODULE_LABELS.get(question['moduleId'], question['moduleId'])}｜{question['focus']}")
        lines.append(f"   - 選項：{options}")
        lines.append(f"   - 正解：{question['answer']}")
        lines.append(f"   - 線索：{question['explanation']}")

    lines.extend([
        "",
        "### 3. 錯題回收",
        "",
    ])

    if error:
        lines.extend([
            f"- 舊錯題：{error.get('question_id', '')}",
            f"- 錯因：{error.get('error_reason', '')}",
            f"- 正確線索：{error.get('correct_clue', '')}",
            "- 今日處理：先口頭說明錯因，再重寫一個同型句。",
        ])
    else:
        lines.append("- 目前沒有開放中的錯題；今天把題型練習中的錯題新增到 `data/error_log.csv`。")

    lines.extend([
        "",
        "### 4. 寫作輸出",
        "",
        "- 用今天 2 個單字或新聞關鍵字寫 3-5 句英文。",
        "- 至少使用 1 個轉折、因果或補充連接詞。",
        "",
    ])
    return "\n".join(lines)


def render_plan(student_id: str, start_date: date, days: int) -> str:
    open_errors = load_open_errors(student_id)
    skills = rank_focus_skills(open_errors)
    module_priority = build_module_priority(skills)
    question_bank = load_question_bank()
    frequency_items = group_frequency_items()
    news_keywords = read_csv(DATA_DIR / "news_keyword_seed.csv")

    lines = [
        f"# 7 天高中學測英文補強計畫｜{student_id}",
        "",
        f"- 起始日期：{start_date.isoformat()}",
        f"- 天數：{days}",
        f"- 主要弱點排序：{', '.join(skills)}",
        f"- 開放中錯題數：{len(open_errors)}",
        "",
        "## 使用方式",
        "",
        "每天做完後，把錯題、錯因、正確線索與下次複習日寫回 `data/error_log.csv`。",
        "若學生資料需要保留，請只使用匿名 ID、班級代碼或座號，不寫真實姓名。",
        "",
    ]

    for day_index in range(days):
        lines.append(
            build_daily_plan(
                day_index,
                start_date + timedelta(days=day_index),
                skills,
                module_priority,
                question_bank,
                frequency_items,
                news_keywords,
                open_errors,
            )
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    start_date = datetime.strptime(args.start_date, "%Y-%m-%d").date()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output = render_plan(args.student_id, start_date, args.days)
    output_path = output_dir / f"{start_date.isoformat()}_{args.student_id}_7_day_practice.md"
    output_path.write_text(output, encoding="utf-8")
    print(f"Generated {output_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
