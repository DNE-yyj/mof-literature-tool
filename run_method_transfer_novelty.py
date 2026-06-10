from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any

from core import TRANSFER_NOVELTY_TAGS, build_parser, run_cli


REPO_ROOT = Path(__file__).resolve().parent

RUNS = (
    ("Recent MOF literature", "configs/weekly_mof_latest.json"),
    ("Cross-material ML transfer", "configs/materials_ml_transfer.json"),
    ("Long-horizon MOF method prior art", "configs/mof_ml_method_prior_art.json"),
)

METHOD_LABELS = {
    "active_learning": "active learning / Bayesian optimization",
    "equivariant_ml": "equivariant ML",
    "foundation_model": "foundation or pretrained model",
    "generative_model": "generative / diffusion / inverse design",
    "gnn": "graph neural network",
    "interatomic_potential": "ML interatomic potential",
    "multimodal": "multimodal or literature-mining model",
    "physics_informed": "physics-informed ML",
    "self_supervised": "self-supervised learning",
    "surrogate_model": "surrogate or multi-fidelity model",
    "symbolic_regression": "symbolic regression / descriptor discovery",
    "transfer_learning": "transfer learning / domain adaptation",
    "uncertainty": "uncertainty / OOD",
}

STATUS_FRESH = "Fresh MOF transfer candidate"
STATUS_PRIOR = "Older MOF prior art exists"
STATUS_RECENT = "Already active in recent MOF"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run MOF, cross-material ML, and long-horizon MOF prior-art scans, then build one novelty report.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=REPO_ROOT / "reports" / "method_transfer_novelty",
        help="Directory that will receive a timestamped combined report folder.",
    )
    parser.add_argument(
        "--limit-opportunities",
        type=int,
        default=20,
        help="Maximum cross-material papers to list in the combined opportunity section.",
    )
    return parser.parse_args()


def run_config(config_path: Path) -> dict[str, Path]:
    parser = build_parser()
    args = parser.parse_args(["--config", str(config_path)])
    return run_cli(args)


def load_papers(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Expected a list of papers in {path}")
    return [paper for paper in payload if isinstance(paper, dict)]


def load_manifest(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected a manifest object in {path}")
    return payload


def paper_tags(paper: dict[str, Any]) -> set[str]:
    raw_tags = paper.get("tags", [])
    if not isinstance(raw_tags, list):
        return set()
    return {str(tag) for tag in raw_tags}


def method_tags(paper: dict[str, Any]) -> list[str]:
    return sorted(paper_tags(paper).intersection(TRANSFER_NOVELTY_TAGS))


def index_by_method(papers: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = {}
    for paper in papers:
        for tag in method_tags(paper):
            index.setdefault(tag, []).append(paper)
    for tag, tagged_papers in index.items():
        index[tag] = sorted(
            tagged_papers,
            key=lambda item: (str(item.get("publication_date", "")), float(item.get("score", 0.0))),
            reverse=True,
        )
    return index


def classify_methods(
    methods: list[str],
    *,
    recent_mof_index: dict[str, list[dict[str, Any]]],
    prior_art_index: dict[str, list[dict[str, Any]]],
) -> tuple[str, list[str], list[str]]:
    recent_hits = [tag for tag in methods if tag in recent_mof_index]
    prior_hits = [tag for tag in methods if tag in prior_art_index]
    if recent_hits:
        return STATUS_RECENT, recent_hits, prior_hits
    if prior_hits:
        return STATUS_PRIOR, recent_hits, prior_hits
    return STATUS_FRESH, recent_hits, prior_hits


def title_of(paper: dict[str, Any]) -> str:
    return str(paper.get("title") or "Untitled")


def short_paper_line(paper: dict[str, Any]) -> str:
    date = str(paper.get("publication_date") or "unknown date")
    journal = str(paper.get("journal") or "unknown journal")
    return f"{title_of(paper)} ({journal}, {date})"


def evidence_lines(methods: list[str], index: dict[str, list[dict[str, Any]]], *, limit: int = 3) -> list[str]:
    seen: set[str] = set()
    lines: list[str] = []
    for tag in methods:
        for paper in index.get(tag, []):
            title = title_of(paper)
            if title in seen:
                continue
            seen.add(title)
            lines.append(f"{METHOD_LABELS.get(tag, tag)}: {short_paper_line(paper)}")
            if len(lines) >= limit:
                return lines
    return lines


def priority_rank(status: str) -> int:
    if status == STATUS_FRESH:
        return 0
    if status == STATUS_PRIOR:
        return 1
    return 2


def method_count_table(
    *,
    cross_papers: list[dict[str, Any]],
    recent_mof_papers: list[dict[str, Any]],
    prior_art_papers: list[dict[str, Any]],
) -> list[tuple[str, int, int, int]]:
    rows: list[tuple[str, int, int, int]] = []
    all_tags = sorted(TRANSFER_NOVELTY_TAGS)
    for tag in all_tags:
        cross_count = sum(1 for paper in cross_papers if tag in paper_tags(paper))
        recent_count = sum(1 for paper in recent_mof_papers if tag in paper_tags(paper))
        prior_count = sum(1 for paper in prior_art_papers if tag in paper_tags(paper))
        if cross_count or recent_count or prior_count:
            rows.append((tag, cross_count, recent_count, prior_count))
    return rows


def build_report(
    *,
    generated_at: str,
    run_outputs: dict[str, dict[str, Path]],
    manifests: dict[str, dict[str, Any]],
    cross_papers: list[dict[str, Any]],
    recent_mof_papers: list[dict[str, Any]],
    prior_art_papers: list[dict[str, Any]],
    limit_opportunities: int,
) -> str:
    recent_index = index_by_method(recent_mof_papers)
    prior_index = index_by_method(prior_art_papers)

    opportunity_rows = []
    for paper in cross_papers:
        methods = method_tags(paper)
        if not methods:
            continue
        status, recent_hits, prior_hits = classify_methods(
            methods,
            recent_mof_index=recent_index,
            prior_art_index=prior_index,
        )
        opportunity_rows.append(
            {
                "paper": paper,
                "methods": methods,
                "status": status,
                "recent_hits": recent_hits,
                "prior_hits": prior_hits,
            }
        )
    opportunity_rows.sort(
        key=lambda item: (
            priority_rank(str(item["status"])),
            -float(item["paper"].get("score", 0.0)),
            title_of(item["paper"]),
        )
    )

    lines = [
        "# Method Transfer Novelty Report",
        "",
        f"- Generated: `{generated_at}`",
        "- Logic: cross-material ML methods are candidate ideas; recent MOF literature checks current adoption; long-horizon MOF prior art checks older adoption.",
        "",
        "## Source Runs",
        "",
    ]
    for label, outputs in run_outputs.items():
        manifest = manifests[label]
        lines.extend(
            [
                f"- {label}: profile `{manifest.get('profile', 'unknown')}`, since `{manifest.get('from_date', 'unknown')}`, papers `{manifest.get('paper_count', 'unknown')}`",
                f"  - Report: `{outputs['report']}`",
            ]
        )

    fresh_count = sum(1 for row in opportunity_rows if row["status"] == STATUS_FRESH)
    prior_count = sum(1 for row in opportunity_rows if row["status"] == STATUS_PRIOR)
    recent_count = sum(1 for row in opportunity_rows if row["status"] == STATUS_RECENT)
    lines.extend(
        [
            "",
            "## Triage Summary",
            "",
            f"- Fresh MOF transfer candidates: `{fresh_count}`",
            f"- Older MOF prior art exists: `{prior_count}`",
            f"- Already active in recent MOF literature: `{recent_count}`",
            "",
            "## Method-Class Baseline",
            "",
            "| Method class | Cross-material ML | Recent MOF | Long-horizon MOF prior art |",
            "|---|---:|---:|---:|",
        ]
    )
    for tag, cross_count, recent_count_for_tag, prior_count_for_tag in method_count_table(
        cross_papers=cross_papers,
        recent_mof_papers=recent_mof_papers,
        prior_art_papers=prior_art_papers,
    ):
        lines.append(
            f"| {METHOD_LABELS.get(tag, tag)} | {cross_count} | {recent_count_for_tag} | {prior_count_for_tag} |"
        )

    lines.extend(["", "## Transfer Opportunities", ""])
    for index, row in enumerate(opportunity_rows[: max(limit_opportunities, 1)], start=1):
        paper = row["paper"]
        methods = [METHOD_LABELS.get(tag, tag) for tag in row["methods"]]
        status = str(row["status"])
        url = str(paper.get("url") or "")
        lines.extend(
            [
                f"### {index}. [{status}] {title_of(paper)}",
                "",
                f"- Journal/date: {paper.get('journal') or 'unknown'}; `{paper.get('publication_date') or 'unknown'}`",
                f"- Link: {url or 'N/A'}",
                f"- Method tags: {', '.join(methods)}",
                f"- MOF transfer note: {paper.get('mof_relevance') or 'Needs manual assessment.'}",
                f"- Suggested next step: {paper.get('next_steps') or 'Check full paper and MOF benchmark fit.'}",
            ]
        )
        recent_evidence = evidence_lines(row["recent_hits"], recent_index)
        prior_evidence = evidence_lines(row["prior_hits"], prior_index)
        if recent_evidence:
            lines.append("- Recent MOF evidence:")
            lines.extend(f"  - {line}" for line in recent_evidence)
        if prior_evidence:
            lines.append("- Long-horizon MOF prior art:")
            lines.extend(f"  - {line}" for line in prior_evidence)
        if not recent_evidence and not prior_evidence:
            lines.append("- MOF baseline evidence: no same method-class match found in the two MOF scans.")
        lines.append("")

    lines.extend(
        [
            "## Reading Rules",
            "",
            "- Fresh means no same method-class tag was found in the recent or long-horizon MOF baselines. It still needs full-paper confirmation.",
            "- Older prior art means the idea is not new to MOFs, but it may still be worth pursuing if the cross-material paper adds a new representation, label space, uncertainty loop, active-learning strategy, or validation regime.",
            "- Recent MOF activity means lower novelty unless the new method opens a clearly different MOF task or implementation path.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    generated_at = dt.datetime.now().replace(microsecond=0).isoformat()
    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")

    run_outputs: dict[str, dict[str, Path]] = {}
    manifests: dict[str, dict[str, Any]] = {}
    paper_sets: dict[str, list[dict[str, Any]]] = {}
    for label, config in RUNS:
        outputs = run_config(REPO_ROOT / config)
        run_outputs[label] = outputs
        manifests[label] = load_manifest(outputs["manifest"])
        paper_sets[label] = load_papers(outputs["json"])

    output_dir = args.output_root / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.md"
    manifest_path = output_dir / "manifest.json"

    report_text = build_report(
        generated_at=generated_at,
        run_outputs=run_outputs,
        manifests=manifests,
        cross_papers=paper_sets["Cross-material ML transfer"],
        recent_mof_papers=paper_sets["Recent MOF literature"],
        prior_art_papers=paper_sets["Long-horizon MOF method prior art"],
        limit_opportunities=args.limit_opportunities,
    )
    report_path.write_text(report_text, encoding="utf-8")
    manifest_path.write_text(
        json.dumps(
            {
                "generated_at": generated_at,
                "runs": {
                    label: {name: str(path) for name, path in outputs.items()}
                    for label, outputs in run_outputs.items()
                },
                "combined_report": str(report_path),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(f"Combined novelty report written to: {report_path}")
    print(f"Combined manifest written to: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
