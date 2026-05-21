import csv
import json
import re
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path(r"G:\我的雲端硬碟\歷屆試題\分析輸出\文字抽取")
YEARS = ["111", "112", "113", "114", "115"]
TEXT_FILES = [SOURCE_DIR / f"{year}-英文.txt" for year in YEARS]

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "than", "that", "this", "these", "those",
    "is", "are", "was", "were", "be", "been", "being", "am", "do", "does", "did", "done",
    "have", "has", "had", "having", "can", "could", "will", "would", "may", "might", "must",
    "shall", "should", "to", "of", "in", "on", "at", "by", "for", "from", "with", "without",
    "as", "into", "over", "under", "between", "among", "about", "after", "before", "during",
    "through", "within", "it", "its", "they", "them", "their", "he", "she", "his", "her",
    "we", "us", "our", "you", "your", "i", "me", "my", "one", "two", "three", "all", "some",
    "many", "much", "more", "most", "other", "another", "each", "every", "only", "also",
    "not", "no", "so", "very", "just", "there", "here", "when", "where", "who", "which",
    "what", "why", "how", "choose", "best", "answer", "question", "questions", "page", "pages",
    "following", "paragraph", "passage", "part", "section", "test", "english", "year", "years",
    "first", "second", "third", "used", "use", "using", "such", "often", "around", "new", "old",
    "word", "words", "out", "made", "while", "even", "like", "same", "thing", "things", "way",
    "day", "days", "place", "make", "take", "get", "go", "come", "see", "know", "say", "said",
    "find",
    "tell", "told", "called", "became", "become", "well", "back", "long", "good", "great",
}

WORD_MEANINGS = {
    "people": "人們",
    "students": "學生",
    "study": "研究;學習",
    "life": "生活;生命",
    "time": "時間",
    "water": "水",
    "food": "食物",
    "children": "孩子",
    "school": "學校",
    "world": "世界",
    "animals": "動物",
    "research": "研究",
    "information": "資訊",
    "health": "健康",
    "century": "世紀",
    "culture": "文化",
    "language": "語言",
    "experience": "經驗",
    "important": "重要的",
    "different": "不同的",
    "social": "社會的",
    "change": "改變",
    "energy": "能源;精力",
    "environment": "環境",
    "example": "例子",
    "problem": "問題",
    "process": "過程",
    "support": "支持;支撐",
    "animal": "動物",
    "human": "人類的;人類",
    "body": "身體",
    "island": "島嶼",
    "community": "社群;社區",
    "system": "系統",
    "activity": "活動",
    "skill": "技能",
    "design": "設計",
    "local": "當地的",
    "public": "公共的",
    "possible": "可能的",
    "natural": "自然的",
    "special": "特別的",
    "traditional": "傳統的",
    "modern": "現代的",
    "show": "顯示;展示",
    "thus": "因此",
    "country": "國家",
    "since": "自從;因為",
    "small": "小的",
    "help": "幫助",
    "until": "直到",
    "true": "真實的",
    "today": "今日;現今",
    "popular": "受歡迎的",
    "early": "早期的;早的",
    "because": "因為",
    "almost": "幾乎",
    "need": "需要",
    "develop": "發展",
    "provide": "提供",
    "create": "創造",
    "increase": "增加",
    "include": "包含",
    "produce": "生產;產生",
    "believe": "相信",
    "consider": "考慮",
    "suggest": "建議;顯示",
    "however": "然而",
    "although": "雖然",
    "therefore": "因此",
}

PHRASE_MEANINGS = {
    "such as": "例如",
    "in order to": "為了",
    "as well as": "以及",
    "rather than": "而不是",
    "according to": "根據",
    "at least": "至少",
    "because of": "因為",
    "instead of": "而不是",
    "in addition": "此外",
    "in contrast": "相較之下",
    "as a result": "因此",
    "be likely to": "有可能",
    "pay attention to": "注意",
    "take part in": "參與",
    "look forward to": "期待",
    "come up with": "想出",
    "make sure": "確保",
    "find out": "找出",
    "deal with": "處理",
    "lead to": "導致",
    "depend on": "取決於",
    "focus on": "專注於",
}

PHRASE_PATTERNS = [
    "such as", "in order to", "as well as", "rather than", "according to", "at least",
    "because of", "instead of", "in addition", "in contrast", "as a result", "be likely to",
    "pay attention to", "take part in", "look forward to", "come up with", "make sure",
    "find out", "deal with", "lead to", "depend on", "focus on",
]

GRAMMAR_RULES = [
    ("transition words", "轉折、因果、補充連接詞", re.compile(r"\b(however|therefore|although|though|moreover|instead|otherwise|besides|nevertheless|meanwhile|because|since)\b", re.I)),
    ("relative clauses", "關係子句", re.compile(r"\b(who|whom|whose|which|that|where|when)\b\s+\w+", re.I)),
    ("passive voice", "被動語態", re.compile(r"\b(is|are|was|were|be|been|being)\s+\w+(ed|en)\b", re.I)),
    ("conditional sentences", "條件句", re.compile(r"\bif\b[^.?!,;:]{0,80}\b(will|would|can|could|may|might|should)\b", re.I)),
    ("participial phrases", "分詞構句", re.compile(r"(^|[.!?]\s+)(\w+ing|\w+ed),\s+\w+", re.I)),
    ("infinitive purpose", "不定詞表目的", re.compile(r"\b(in order to|so as to|to)\s+\w+", re.I)),
    ("comparatives", "比較級", re.compile(r"\b(more|less|better|worse|larger|smaller|higher|lower|faster|slower)\b\s+\w+\s+\bthan\b", re.I)),
    ("modal auxiliaries", "情態助動詞", re.compile(r"\b(can|could|may|might|must|should|would)\s+\w+", re.I)),
]


def normalize_word(word: str) -> str:
    word = word.lower().strip("'")
    if len(word) > 5 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 5 and word.endswith("es"):
        return word[:-2]
    if len(word) > 4 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def level_for_rank(index: int, total: int) -> str:
    if index < max(1, total * 0.3):
        return "high"
    if index < max(2, total * 0.7):
        return "medium"
    return "low"


def generated_example(item_type: str, text: str) -> str:
    if item_type == "grammar":
        return f"Practice this grammar point in a GSAT-style sentence: {text}."
    if item_type == "phrase":
        return f"Students should understand how to use '{text}' in a reading passage."
    return f"Students should recognize '{text}' quickly in GSAT reading passages."


def read_source_texts() -> tuple[str, dict[str, str]]:
    chunks = []
    year_texts = {}
    missing = []
    for year, file_path in zip(YEARS, TEXT_FILES):
        if file_path.exists():
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            chunks.append(content)
            year_texts[year] = content
        else:
            missing.append(str(file_path))
    if missing:
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))
    return "\n".join(chunks), year_texts


def word_items(year_texts: dict[str, str]) -> list[dict]:
    counts = Counter()
    year_counts = Counter()
    for text in year_texts.values():
        words = [normalize_word(match.group()) for match in re.finditer(r"[A-Za-z][A-Za-z'-]{2,}", text)]
        filtered = [word for word in words if word not in STOPWORDS and not word.isdigit()]
        counts.update(filtered)
        year_counts.update(set(filtered))

    scored = [
        (word, count, year_counts[word])
        for word, count in counts.items()
        if year_counts[word] >= 2 and len(word) >= 4
    ]
    scored.sort(key=lambda row: (row[2], row[1], row[0]), reverse=True)
    common = scored[:24]
    return [
        {
            "type": "word",
            "text": word,
            "frequency": count,
            "level": level_for_rank(index, len(common)),
            "meaning": WORD_MEANINGS.get(word, "待補"),
            "example": generated_example("word", word),
        }
        for index, (word, count, _years_seen) in enumerate(common)
    ]


def phrase_items(text: str) -> list[dict]:
    lowered = re.sub(r"\s+", " ", text.lower())
    counts = Counter()
    for phrase in PHRASE_PATTERNS:
        counts[phrase] = len(re.findall(rf"\b{re.escape(phrase)}\b", lowered))
    common = [(phrase, count) for phrase, count in counts.most_common() if count > 0][:18]
    return [
        {
            "type": "phrase",
            "text": phrase,
            "frequency": count,
            "level": level_for_rank(index, len(common)),
            "meaning": PHRASE_MEANINGS.get(phrase, "待補"),
            "example": generated_example("phrase", phrase),
        }
        for index, (phrase, count) in enumerate(common)
    ]


def grammar_items(text: str) -> list[dict]:
    counts = []
    for name, meaning, pattern in GRAMMAR_RULES:
        counts.append((name, meaning, len(pattern.findall(text))))
    common = [(name, meaning, count) for name, meaning, count in sorted(counts, key=lambda row: row[2], reverse=True) if count > 0]
    return [
        {
            "type": "grammar",
            "text": name,
            "frequency": count,
            "level": level_for_rank(index, len(common)),
            "meaning": meaning,
            "example": generated_example("grammar", name),
        }
        for index, (name, meaning, count) in enumerate(common)
    ]


def write_csv(items: list[dict]) -> None:
    output_path = PROJECT_ROOT / "data" / "exam_frequency_seed.csv"
    with output_path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["type", "text", "frequency", "level", "meaning", "example"])
        writer.writeheader()
        writer.writerows(items)


def write_js(items: list[dict]) -> None:
    output_path = PROJECT_ROOT / "web" / "frequency-data.js"
    meta = {
        "target": "高中學測英文",
        "sourceRange": "111-115學年度英文試題文字抽取",
        "note": "由 G:\\我的雲端硬碟\\歷屆試題\\分析輸出\\文字抽取 的五份英文試題文字統計產生。單字與片語為字面出現次數；文法為規則線索估算。",
    }
    content = (
        "window.examFrequencyMeta = "
        + json.dumps(meta, ensure_ascii=False, indent=2)
        + ";\n\nwindow.examFrequencyItems = "
        + json.dumps(items, ensure_ascii=False, indent=2)
        + ";\n"
    )
    output_path.write_text(content, encoding="utf-8")


def main() -> None:
    source_text, year_texts = read_source_texts()
    items = word_items(year_texts) + phrase_items(source_text) + grammar_items(source_text)
    write_csv(items)
    write_js(items)
    print(f"wrote {len(items)} frequency items from {len(TEXT_FILES)} source files")


if __name__ == "__main__":
    main()
