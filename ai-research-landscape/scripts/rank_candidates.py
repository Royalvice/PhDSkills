#!/usr/bin/env python3
"""
Rank AI research candidates by recency, influence, and source quality.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TOP_VENUES = {
    "cvpr",
    "iccv",
    "eccv",
    "neurips",
    "nips",
    "iclr",
    "icml",
    "siggraph",
    "siggraph asia",
    "tpami",
    "ijcv",
    "rss",
    "corl",
    "icra",
    "acl",
    "emnlp",
    "naacl",
}

GOOD_VENUE_HINTS = {
    "arxiv": 1.1,
    "openreview": 1.2,
    "cvf": 1.3,
    "pmlr": 1.3,
    "acm": 1.2,
    "ieee": 1.2,
    "springer": 1.1,
    "nature": 1.4,
    "science": 1.4,
}


@dataclass
class CandidateScore:
    priority_bucket: int
    score: float
    age_years: int
    citation_band: str
    venue_band: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rank research candidates from a JSON array.")
    parser.add_argument("input_json", help="Path to the candidate JSON file")
    parser.add_argument("-o", "--output", help="Output JSON path")
    parser.add_argument("--top-n", type=int, default=30, help="Number of items to keep in the primary output")
    parser.add_argument(
        "--include-unverified",
        action="store_true",
        help="Keep unverified candidates instead of filtering them out",
    )
    return parser.parse_args()


def load_candidates(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Input JSON must be an array of candidate objects.")
    return [item for item in data if isinstance(item, dict)]


def now_year() -> int:
    return datetime.now(timezone.utc).year


def age_of(year: Any) -> int:
    try:
        year_int = int(year)
    except (TypeError, ValueError):
        return 99
    return max(0, now_year() - year_int)


def citation_value(candidate: dict[str, Any]) -> int:
    citations = candidate.get("citations")
    if citations is None:
        return 0
    try:
        return max(0, int(citations))
    except (TypeError, ValueError):
        return 0


def citation_band(citations: int) -> str:
    if citations >= 1000:
        return "very-high"
    if citations >= 200:
        return "high"
    if citations >= 50:
        return "medium"
    if citations >= 10:
        return "low"
    return "unknown"


def venue_score(candidate: dict[str, Any]) -> tuple[float, str]:
    venue = str(candidate.get("venue") or "").strip().lower()
    url = str(candidate.get("canonical_url") or "").strip().lower()
    source_type = str(candidate.get("source_type") or "").strip().lower()

    if candidate.get("is_blog") or source_type == "blog":
        return 1.0, "official-blog"
    if venue in TOP_VENUES:
        return 1.5, "top"
    for hint, value in GOOD_VENUE_HINTS.items():
        if hint in venue or hint in url:
            return value, "trusted"
    if venue:
        return 0.9, "other"
    return 0.8, "unknown"


def priority_bucket(age_years: int, citations: int, is_foundational: bool, is_survey: bool) -> int:
    if age_years <= 2 and citations >= 200:
        return 0
    if age_years <= 2 and citations >= 50:
        return 1
    if age_years <= 5 and citations >= 200:
        return 2
    if age_years > 5 and (citations >= 500 or is_foundational or is_survey):
        return 3
    if age_years <= 5:
        return 4
    return 5


def compute_score(candidate: dict[str, Any]) -> CandidateScore:
    age_years = age_of(candidate.get("year"))
    citations = citation_value(candidate)
    is_foundational = bool(candidate.get("is_foundational"))
    is_survey = bool(candidate.get("is_survey"))
    venue_multiplier, venue_band = venue_score(candidate)

    bucket = priority_bucket(age_years, citations, is_foundational, is_survey)
    recency_score = max(0.0, 6.0 - min(age_years, 10) * 0.9)
    citation_score = math.log1p(citations) * 2.4
    survey_bonus = 1.6 if is_survey else 0.0
    foundation_bonus = 1.2 if is_foundational else 0.0
    verified_bonus = 1.0 if candidate.get("verified") else -2.5
    source_bonus = 0.6 if candidate.get("is_arxiv") else 0.0
    bucket_bonus = (6 - bucket) * 2.5

    score = (recency_score + citation_score + survey_bonus + foundation_bonus + verified_bonus + source_bonus + bucket_bonus) * venue_multiplier
    return CandidateScore(
        priority_bucket=bucket,
        score=round(score, 4),
        age_years=age_years,
        citation_band=citation_band(citations),
        venue_band=venue_band,
    )


def rank_candidates(candidates: list[dict[str, Any]], include_unverified: bool) -> list[dict[str, Any]]:
    ranked = []
    for candidate in candidates:
        if not include_unverified and not candidate.get("verified"):
            continue
        candidate_copy = dict(candidate)
        score = compute_score(candidate_copy)
        candidate_copy["age_years"] = score.age_years
        candidate_copy["citation_band"] = score.citation_band
        candidate_copy["venue_band"] = score.venue_band
        candidate_copy["priority_bucket"] = score.priority_bucket
        candidate_copy["score"] = score.score
        ranked.append(candidate_copy)

    ranked.sort(
        key=lambda item: (
            item["priority_bucket"],
            -item["score"],
            -citation_value(item),
            item.get("year") or 0,
            str(item.get("title") or "").lower(),
        )
    )
    for index, item in enumerate(ranked, start=1):
        item["rank"] = index
    return ranked


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_json)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".ranked.json")

    ranked = rank_candidates(load_candidates(input_path), args.include_unverified)
    primary = ranked[: max(0, args.top_n)]
    output_path.write_text(json.dumps(primary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote {len(primary)} ranked candidates to {output_path}")
    if len(ranked) > len(primary):
        print(f"Filtered {len(ranked) - len(primary)} additional verified candidates beyond top {args.top_n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
