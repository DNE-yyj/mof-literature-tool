from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TRIAGE_PATTERNS = {
    "fresh": re.compile(r"^- Fresh MOF transfer candidates: `(\d+)`$"),
    "prior_art": re.compile(r"^- Older MOF prior art exists: `(\d+)`$"),
    "recent_active": re.compile(r"^- Already active in recent MOF literature: `(\d+)`$"),
}

OPPORTUNITY_PATTERN = re.compile(r"^### \d+\. \[(.+?)\] (.+)$")
SOURCE_PATTERN = re.compile(r"^- Candidate source: (.+)$")
TRANSFER_DISTANCE_PATTERN = re.compile(r"^- Transfer distance: (.+)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize the latest combined method-transfer novelty report.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Path to a combined report.md. If omitted, the newest report under reports/method_transfer_novelty is used.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root used when auto-discovering the latest report.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of ranked opportunities to include.",
    )
    return parser.parse_args()


def discover_latest_report(repo_root: Path) -> Path:
    report_root = repo_root / "reports" / "method_transfer_novelty"
    reports = sorted(report_root.glob("*/report.md"))
    if not reports:
        raise FileNotFoundError(f"No combined report found under {report_root}")
    return reports[-1]


def parse_report(report_path: Path, top_n: int) -> dict[str, object]:
    text = report_path.read_text(encoding="utf-8")
    triage = {"fresh": None, "prior_art": None, "recent_active": None}
    ideas: list[dict[str, str]] = []

    for line in text.splitlines():
        for key, pattern in TRIAGE_PATTERNS.items():
            match = pattern.match(line)
            if match:
                triage[key] = int(match.group(1))

        match = OPPORTUNITY_PATTERN.match(line)
        if match and len(ideas) < max(top_n, 1):
            ideas.append(
                {
                    "status": match.group(1),
                    "title": match.group(2),
                    "candidate_source": "unknown",
                    "transfer_distance": "unclassified",
                }
            )
            continue

        match = SOURCE_PATTERN.match(line)
        if match and ideas:
            ideas[-1]["candidate_source"] = match.group(1)
            continue

        match = TRANSFER_DISTANCE_PATTERN.match(line)
        if match and ideas:
            ideas[-1]["transfer_distance"] = match.group(1)

    missing = [key for key, value in triage.items() if value is None]
    if missing:
        raise ValueError(f"Could not parse triage counts from {report_path}: missing {missing}")

    return {
        "report_path": str(report_path),
        "counts": triage,
        "top_ideas": ideas,
    }


def to_markdown(summary: dict[str, object]) -> str:
    counts = summary["counts"]
    ideas = summary["top_ideas"]

    lines = [
        "## Latest combined report",
        f"- Report: `{summary['report_path']}`",
        f"- Fresh MOF transfer candidates: `{counts['fresh']}`",
        f"- Older MOF prior art exists: `{counts['prior_art']}`",
        f"- Already active in recent MOF literature: `{counts['recent_active']}`",
        "",
        "## Top opportunities",
    ]
    for idx, idea in enumerate(ideas, start=1):
        lines.append(
            f"{idx}. `{idea['status']}` `{idea['transfer_distance']}` `{idea['candidate_source']}` - {idea['title']}"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    report_path = args.report or discover_latest_report(args.repo_root)
    summary = parse_report(report_path, top_n=args.top)
    output_root = report_path.parent

    summary_path = output_root / "summary.json"
    markdown_path = output_root / "summary.md"
    latest_path_file = args.repo_root / "latest_report_path.txt"
    latest_summary_file = args.repo_root / "latest_report_summary.md"

    markdown = to_markdown(summary)
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown_path.write_text(markdown, encoding="utf-8")
    latest_path_file.write_text(str(report_path) + "\n", encoding="utf-8")
    latest_summary_file.write_text(markdown, encoding="utf-8")

    print(markdown, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
