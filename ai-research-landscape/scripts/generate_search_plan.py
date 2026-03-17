#!/usr/bin/env python3
"""
Generate a search plan, query list, and starter candidate file for a research topic.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a search plan workspace for an AI topic.")
    parser.add_argument("--topic", required=True, help="Research topic or task.")
    parser.add_argument("--count", type=int, default=30, help="Target number of representative works.")
    parser.add_argument("--seed-paper", action="append", default=[], help="Seed paper title. Repeatable.")
    parser.add_argument("--seed-lab", action="append", default=[], help="Seed lab, company, or author string. Repeatable.")
    parser.add_argument("--output-dir", default="topic-workspace", help="Directory to write the generated files into.")
    return parser.parse_args()


def build_queries(topic: str, seed_papers: list[str], seed_labs: list[str]) -> list[str]:
    topic_q = f'"{topic}"'
    queries = [
        f"{topic_q} survey",
        f"{topic_q} review",
        f"{topic_q} tutorial",
        f"{topic_q} arXiv",
        f"{topic_q} site:scholar.google.com",
        f"{topic_q} CVPR OR ICCV OR ECCV OR NeurIPS OR ICLR",
        f"{topic_q} official blog",
    ]
    for seed in seed_papers:
        queries.extend([f'"{seed}"', f'"{seed}" citations', f'"{seed}" related work'])
    for seed in seed_labs:
        queries.extend([f"{topic_q} \"{seed}\"", f"{topic_q} site:research.google blog \"{seed}\""])
    deduped = []
    seen = set()
    for query in queries:
        if query not in seen:
            seen.add(query)
            deduped.append(query)
    return deduped


def build_markdown(topic: str, count: int, queries: list[str], seed_papers: list[str], seed_labs: list[str]) -> str:
    lines = [f"# Search Plan: {topic}", "", f"Target shortlist size: {count}", "", "## Seed Papers", ""]
    lines.extend([f"- {item}" for item in seed_papers] or ["- None"])
    lines.extend(["", "## Seed Labs Or Authors", ""])
    lines.extend([f"- {item}" for item in seed_labs] or ["- None"])
    lines.extend(["", "## Suggested Queries", ""])
    lines.extend([f"- `{query}`" for query in queries])
    lines.extend(["", "## Workflow Notes", "", "- Search surveys first and add them to candidates.seed.json.", "- Export useful Google Scholar entries as BibTeX and ingest them with scripts/import_bibtex_candidates.py.", "- Verify every shortlisted item before setting verified=true.", ""])
    return "\n".join(lines)


def build_seed_candidates(topic: str, seed_papers: list[str], seed_labs: list[str]) -> list[dict]:
    items = []
    for title in seed_papers:
        items.append({"title": title, "authors": [], "organization": None, "year": None, "venue": None, "citations": None, "source_type": "paper", "canonical_url": None, "scholar_url": None, "discovery_channels": ["seed"], "is_survey": False, "is_foundational": False, "is_blog": False, "is_arxiv": False, "verified": False, "summary": f"Seed paper for topic: {topic}", "notes": None})
    for org in seed_labs:
        items.append({"title": f"{topic} - {org}", "authors": [], "organization": org, "year": None, "venue": None, "citations": None, "source_type": "system", "canonical_url": None, "scholar_url": None, "discovery_channels": ["seed"], "is_survey": False, "is_foundational": False, "is_blog": True, "is_arxiv": False, "verified": False, "summary": f"Seed organization or system hint for topic: {topic}", "notes": None})
    return items


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    queries = build_queries(args.topic, args.seed_paper, args.seed_lab)
    (out_dir / "queries.txt").write_text("\n".join(queries) + "\n", encoding="utf-8")
    (out_dir / "search-plan.md").write_text(build_markdown(args.topic, args.count, queries, args.seed_paper, args.seed_lab), encoding="utf-8")
    (out_dir / "candidates.seed.json").write_text(json.dumps(build_seed_candidates(args.topic, args.seed_paper, args.seed_lab), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote search plan workspace to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
