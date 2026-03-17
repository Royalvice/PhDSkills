#!/usr/bin/env python3
"""
Build a markdown research-status draft from ranked candidate metadata.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a markdown research digest from candidate JSON.")
    parser.add_argument("input_json", help="Ranked or unranked candidate JSON")
    parser.add_argument("-o", "--output", help="Output markdown path")
    parser.add_argument("--topic", required=True, help="Topic name")
    parser.add_argument("--top-n", type=int, default=30, help="Number of works to include")
    parser.add_argument(
        "--bibliography",
        default="references.bib",
        help="Pandoc bibliography path to place in the markdown front matter",
    )
    return parser.parse_args()


def load_items(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Input JSON must be an array.")
    return [item for item in data if isinstance(item, dict)]


def author_label(item: dict[str, Any]) -> str:
    authors = item.get("authors")
    if isinstance(authors, list) and authors:
        if len(authors) == 1:
            return authors[0]
        if len(authors) == 2:
            return f"{authors[0]} and {authors[1]}"
        return f"{authors[0]} et al."
    organization = item.get("organization")
    if organization:
        return str(organization)
    return "Unknown authors"


def cite(item: dict[str, Any]) -> str:
    key = str(item.get("bib_key") or "").strip()
    return f" [@{key}]" if key else ""


def summarize_threads(items: list[dict[str, Any]]) -> list[str]:
    counter = Counter()
    for item in items:
        for channel in item.get("discovery_channels", []):
            counter[str(channel)] += 1
    if not counter:
        return ["- The candidate set needs manual thematic grouping before finalization."]
    lines = []
    for name, count in counter.most_common(4):
        lines.append(f"- `{name}` contributes {count} shortlisted works and should be mapped to one concrete technical thread.")
    return lines


def build_front_matter(topic: str, bibliography: str, items: list[dict[str, Any]]) -> list[str]:
    keys = [str(item.get("bib_key") or "").strip() for item in items]
    keys = [key for key in keys if key]
    lines = [
        "---",
        f'title: "{topic} Research Status"',
        f"bibliography: {bibliography}",
        "link-citations: true",
    ]
    if keys:
        lines.append("nocite: |")
        for key in keys:
            lines.append(f"  @{key}")
    lines.append("---")
    lines.append("")
    return lines


def build_markdown(topic: str, bibliography: str, items: list[dict[str, Any]]) -> str:
    years = [int(item["year"]) for item in items if str(item.get("year", "")).isdigit()]
    year_range = f"{min(years)}-{max(years)}" if years else "unknown"
    surveys = sum(1 for item in items if item.get("is_survey"))
    blogs = sum(1 for item in items if item.get("is_blog"))
    foundational = sum(1 for item in items if item.get("is_foundational"))

    lines = build_front_matter(topic, bibliography, items)
    lines.extend([
        f"# {topic} Research Status",
        "",
        "## Scope",
        "",
        f"This draft summarizes `{topic}` through {len(items)} verified works spanning {year_range}.",
        "",
        "## Executive Summary",
        "",
        f"The current shortlist contains {surveys} surveys, {foundational} explicitly foundational works, and {blogs} official blog or system references. Refine the narrative after checking that the final set covers both historical milestones and the latest frontier.",
        "",
        "## Field Evolution",
        "",
        "- Identify the earliest field-defining papers in the shortlist and explain what technical bottleneck they unlocked using direct Pandoc citations such as `[@key]`.",
        "- Group the middle period by the main paradigm shift rather than by publication year alone.",
        "- Explain why the newest 2-year window changes the frontier instead of merely improving metrics.",
        "",
        "## Major Research Threads",
        "",
    ])
    lines.extend(summarize_threads(items))
    lines.extend([
        "",
        "## Representative Works",
        "",
    ])
    for index, item in enumerate(items, start=1):
        venue = item.get("venue") or item.get("source_type") or "Unknown venue"
        url = item.get("canonical_url") or ""
        summary = item.get("summary") or "Add a one-sentence reason this work matters."
        lines.extend([
            f"### {index}. {item.get('title', 'Untitled')}{cite(item)}",
            "",
            f"- Source: {author_label(item)}; {item.get('year', 'n.d.')}; `{venue}`",
            f"- Why it matters: {summary}",
            f"- URL: {url}",
            "",
        ])
    lines.extend([
        "## Current Frontier",
        "",
        "- Highlight the most recent highly cited papers and explain what changed in model design, system design, or evaluation using `[@bib_key]` citations.",
        "- Note whether official product or lab pages reveal deployment constraints not captured by papers.",
        "",
        "## Open Problems",
        "",
        "- Add 3 to 5 open problems after reading the selected works in sequence.",
        "- Separate scientific unknowns from engineering bottlenecks.",
        "",
        "## Verification Notes",
        "",
        "- Confirm every URL, BibTeX key, and metadata field before treating this draft as final.",
        "- Record unresolved ambiguities such as missing citation counts or competing venue versions.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_json)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".md")

    items = load_items(input_path)[: max(0, args.top_n)]
    output_path.write_text(build_markdown(args.topic, args.bibliography, items), encoding="utf-8")
    print(f"Wrote markdown digest for {len(items)} works to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
