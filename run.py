from __future__ import annotations

import sys
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
for candidate in (PARENT_ROOT, MODULE_ROOT):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

try:
    from literature_tool.core import build_parser, run_cli
except ImportError:
    from core import build_parser, run_cli


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    outputs = run_cli(args)
    print(f"Report written to: {outputs['report']}")
    print(f"Metadata JSON: {outputs['json']}")
    print(f"Metadata TSV: {outputs['tsv']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
