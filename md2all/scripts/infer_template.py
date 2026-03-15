#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from common import load_csl_catalog, infer_locale, read_text

ACADEMIC_HINTS = (
    "abstract", "references", "bibliography", "method", "experiment", "thesis",
    "论文", "参考文献", "摘要", "实验", "研究方法", "开题", "中期"
)
BUSINESS_HINTS = (
    "executive summary", "market", "roadmap", "meeting", "brief", "memo", "business",
    "汇报", "市场", "会议纪要", "方案", "项目"
)
NOTICE_HINTS = ("通知", "说明", "公告", "notice", "announcement")
RESUME_HINTS = ("resume", "curriculum vitae", "简历", "教育经历", "工作经历")


def choose_template(text: str) -> str:
    lowered = text.lower()
    if any(h in lowered for h in RESUME_HINTS):
        return "resume"
    if any(h in lowered for h in NOTICE_HINTS):
        return "notice-explanation"
    if any(h in lowered for h in ACADEMIC_HINTS):
        if "开题" in text or "中期" in text or "proposal" in lowered or "midterm" in lowered:
            return "proposal-midterm"
        if "thesis" in lowered or "毕业论文" in text or "学位论文" in text:
            return "degree-thesis"
        return "academic-report"
    if any(h in lowered for h in BUSINESS_HINTS):
        if "brief" in lowered or "简报" in text:
            return "business-brief"
        if "handout" in lowered or "讲义" in text or "发言提纲" in text:
            return "business-handout"
        return "business-report"
    heading_count = len(re.findall(r"^\s{0,3}#{1,3}\s", text, flags=re.MULTILINE))
    citation_count = len(re.findall(r"\[@[A-Za-z0-9:_-]+\]", text))
    if heading_count >= 5 or citation_count >= 3:
        return "academic-report"
    return "general-document"


def default_csl(locale: str) -> str:
    return "gb7714" if locale == "zh" else "apa"


def infer(path: Path) -> dict[str, str]:
    text = read_text(path)
    locale = infer_locale(text)
    return {"template": choose_template(text), "locale": locale, "csl": default_csl(locale)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Infer md2all template and locale.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = infer(args.input)
    if args.json:
        payload = {**result, "available_csl": [item["id"] for item in load_csl_catalog()["styles"]]}
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for key, value in result.items():
            print(f"{key}={value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
