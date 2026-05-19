#!/usr/bin/env python3
"""Build docs/questions.json from FInal/1 and FInal/*.xlsx."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from translations_ar import TOPICS_AR, lookup_translation

ROOT = Path(__file__).resolve().parents[1]
FINAL_DIR = ROOT / "FInal"
OUT = ROOT / "docs" / "questions.json"

HEADER = ["difficulty", "case_scenario", "lead_in", "a", "b", "c", "d", "e", "answer"]

TOPIC_NAMES = {
    "Arrays": "Arrays (1D & 2D)",
    "BSTImpl": "Binary Search Tree",
    "BinaryTree": "Binary Trees",
    "BubbleSort": "Bubble Sort",
    "GraphRep": "Graph Representation",
    "Intro DSA": "Intro to DSA",
    "LinkedList": "Linked Lists",
    "LinkedListImpl": "Linked List Implementation",
    "MergeSort": "Merge Sort",
    "QueueConcepts": "Queue Concepts",
    "QueueOps": "Queue Operations",
    "Stack": "Stack",
    "StackImpl": "Stack Implementation",
    "StackOps": "Stack Operations",
}


def topic_from_case(case: str) -> str:
    m = re.match(r"^(.+?)_case\d+", case, re.I)
    if m:
        key = m.group(1).replace("_", " ")
        return TOPIC_NAMES.get(key, key)
    return case


def row_to_question(parts: list, source: str) -> dict | None:
    if len(parts) < 9:
        return None
    d = dict(zip(HEADER, [str(x or "").strip() for x in parts[:9]]))
    if d["difficulty"].lower() not in ("easy", "medium", "hard"):
        return None
    ans = d["answer"].lower()
    if ans not in "abcde":
        return None
    return {
        "difficulty": d["difficulty"].lower(),
        "case": d["case_scenario"],
        "topic": topic_from_case(d["case_scenario"]),
        "question": d["lead_in"],
        "options": {"a": d["a"], "b": d["b"], "c": d["c"], "d": d["d"], "e": d["e"]},
        "answer": ans,
        "_key": (d["case_scenario"], d["lead_in"]),
        "source": source,
    }


def load_xlsx(path: Path) -> list[dict]:
    import openpyxl

    wb = openpyxl.load_workbook(path, read_only=True)
    rows = list(wb.active.iter_rows(values_only=True))
    out = []
    for row in rows[1:]:
        q = row_to_question(list(row), path.name)
        if q:
            out.append(q)
    return out


def load_tsv(path: Path) -> list[dict]:
    out = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        if not line.strip() or line.startswith("difficulty"):
            continue
        q = row_to_question(line.split("\t"), path.name)
        if q:
            out.append(q)
    return out


def main() -> int:
    seen: dict[tuple, dict] = {}

    for path in sorted(FINAL_DIR.glob("*.xlsx")):
        for q in load_xlsx(path):
            seen[q["_key"]] = q

    tsv = FINAL_DIR / "1"
    if tsv.is_file():
        for q in load_tsv(tsv):
            seen[q["_key"]] = q

    questions = []
    for i, q in enumerate(sorted(seen.values(), key=lambda x: (x["topic"], x["case"])), 1):
        del q["_key"]
        q["id"] = i
        tr = lookup_translation(q["case"], q["question"])
        if tr:
            q["question_ar"] = tr["question_ar"]
            q["options_ar"] = tr["options_ar"]
        q["topic_ar"] = TOPICS_AR.get(q["topic"], q["topic"])
        questions.append(q)

    topics = sorted({q["topic"] for q in questions})
    topics_ar = {t: TOPICS_AR.get(t, t) for t in topics}
    payload = {
        "title": "DSA Final Exam MCQs",
        "title_ar": "أسئلة اختيار من متعدد — هياكل البيانات",
        "updated": __import__("datetime").date.today().isoformat(),
        "count": len(questions),
        "topics": topics,
        "topics_ar": topics_ar,
        "questions": questions,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(questions)} questions to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
