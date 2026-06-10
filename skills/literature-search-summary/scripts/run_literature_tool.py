#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO_MARKERS = ("run.py", "core.py", "profiles.py")


def looks_like_repo(path: Path) -> bool:
    return all((path / marker).exists() for marker in REPO_MARKERS) and (path / "configs").is_dir()


def search_upwards(start: Path) -> Path | None:
    candidates = [start, *start.parents]
    for candidate in candidates:
        if looks_like_repo(candidate):
            return candidate
    return None


def search_downwards(start: Path, *, limit: int = 200) -> Path | None:
    checked = 0
    for candidate in start.rglob("run.py"):
        checked += 1
        if checked > limit:
            break
        repo_root = candidate.parent
        if looks_like_repo(repo_root):
            return repo_root
    return None


def resolve_repo(path_value: str | None) -> Path:
    start = Path(path_value or ".").expanduser().resolve()
    if start.is_file():
        start = start.parent
    match = search_upwards(start)
    if match is not None:
        return match
    match = search_downwards(start)
    if match is not None:
        return match
    raise SystemExit(
        f"Could not locate a literature_tool repository from: {start}\n"
        "Expected run.py, core.py, profiles.py, and configs/."
    )


def resolve_path(value: str | None, *, repo_root: Path, must_exist: bool) -> Path | None:
    if value is None:
        return None
    candidate = Path(value).expanduser()
    if not candidate.is_absolute():
        candidate = (repo_root / candidate).resolve()
    if must_exist and not candidate.exists():
        raise SystemExit(f"Path does not exist: {candidate}")
    return candidate


def build_command(args: argparse.Namespace, repo_root: Path) -> list[str]:
    run_py = repo_root / "run.py"
    command = [args.python_exe, str(run_py)]

    config_path = resolve_path(args.config, repo_root=repo_root, must_exist=True)
    output_dir = resolve_path(args.output_dir, repo_root=repo_root, must_exist=False)

    if config_path is not None:
        command.extend(["--config", str(config_path)])
    if args.profile:
        command.extend(["--profile", args.profile])
    if args.days is not None:
        command.extend(["--days", str(args.days)])
    if args.limit is not None:
        command.extend(["--limit", str(args.limit)])
    if args.rows_per_query is not None:
        command.extend(["--rows-per-query", str(args.rows_per_query)])
    if output_dir is not None:
        command.extend(["--output-dir", str(output_dir)])
    if args.mailto:
        command.extend(["--mailto", args.mailto])
    for query in args.query:
        command.extend(["--query", query])

    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve a literature_tool repository and invoke run.py without the OpenAI path.",
    )
    parser.add_argument(
        "--repo",
        help="Repository root or a nearby directory. Defaults to the current directory.",
    )
    parser.add_argument(
        "--config",
        help="Config JSON path, resolved relative to the repository root when not absolute.",
    )
    parser.add_argument("--profile", help="Built-in profile name such as mof_latest.")
    parser.add_argument("--days", type=int, help="Lookback window in days.")
    parser.add_argument("--limit", type=int, help="Retained paper count after ranking.")
    parser.add_argument("--rows-per-query", type=int, help="Fetched rows per query before deduplication.")
    parser.add_argument(
        "--output-dir",
        help="Output directory, resolved relative to the repository root when not absolute.",
    )
    parser.add_argument("--mailto", help="Optional polite-pool email for public APIs.")
    parser.add_argument(
        "--query",
        action="append",
        default=[],
        help="Repeat to override the profile query list.",
    )
    parser.add_argument(
        "--python-exe",
        default=sys.executable,
        help="Python interpreter to use. Defaults to the current interpreter.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the resolved repository and command without executing.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = resolve_repo(args.repo)
    command = build_command(args, repo_root)

    print(f"Repository: {repo_root}")
    print(f"Command: {subprocess.list2cmdline(command)}")

    if args.dry_run:
        return 0

    completed = subprocess.run(command, cwd=repo_root)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
