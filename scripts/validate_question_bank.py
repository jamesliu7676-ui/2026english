import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BANK_DIR = ROOT / "data" / "question_bank"
SCHEMA = json.loads((BANK_DIR / "schema.json").read_text(encoding="utf-8"))
QUESTION_FILES = [
    "reading.json",
    "discourse.json",
    "cloze.json",
    "fill_blank.json",
    "translation.json",
]


def validate_item(file_name: str, index: int, item: dict) -> list[str]:
    errors = []
    label = f"{file_name}[{index}]"

    for field in SCHEMA["required"]:
        if field not in item:
            errors.append(f"{label}: missing {field}")

    if item.get("level") not in SCHEMA["levels"]:
        errors.append(f"{label}: invalid level {item.get('level')!r}")

    if item.get("sourceType") not in SCHEMA["sourceTypes"]:
        errors.append(f"{label}: invalid sourceType {item.get('sourceType')!r}")

    if item.get("moduleId") not in SCHEMA["moduleIds"]:
        errors.append(f"{label}: invalid moduleId {item.get('moduleId')!r}")

    if not isinstance(item.get("options"), list):
        errors.append(f"{label}: options must be a list")

    if not isinstance(item.get("tags"), list):
        errors.append(f"{label}: tags must be a list")

    if item.get("options") and item.get("answer") not in item.get("options", []):
        errors.append(f"{label}: answer must match one option")

    return errors


def main() -> int:
    errors = []
    total = 0
    seen_ids = set()

    for file_name in QUESTION_FILES:
        path = BANK_DIR / file_name
        items = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(items, list):
            errors.append(f"{file_name}: root must be a list")
            continue
        total += len(items)
        for index, item in enumerate(items):
            item_id = item.get("id")
            if item_id in seen_ids:
                errors.append(f"{file_name}[{index}]: duplicate id {item_id}")
            seen_ids.add(item_id)
            errors.extend(validate_item(file_name, index, item))

    if errors:
        print("Question bank validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Question bank validation passed: {total} items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
