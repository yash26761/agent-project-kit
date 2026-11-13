#!/usr/bin/env python3
"""Install missing AI coding-agent instruction files into a project."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


KIT_ROOT = Path(__file__).resolve().parent.parent
AGENTS = "AGENTS.md"
TOOLS = {
    "codex": [],
    "cursor": [],
    "cline": [],
    "windsurf": [],
    "claude": ["CLAUDE.md"],
    "gemini": ["GEMINI.md"],
    "copilot": [".github/copilot-instructions.md"],
    "aider": [".aider.conf.yml"],
    "continue": [".continue/rules/00-project.md"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Add the shared AGENTS.md and selected AI-tool adapters to an existing "
            "project. Existing files are never overwritten."
        )
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.cwd(),
        help="Project directory to update (default: current directory)",
    )
    parser.add_argument(
        "--tools",
        nargs="+",
        choices=[*TOOLS, "all"],
        default=["all"],
        help="Tools to connect (default: all supported tools)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which files would be added without writing them",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    if not target.is_dir():
        print(f"Target directory does not exist: {target}", file=sys.stderr)
        return 2

    requested = list(TOOLS) if "all" in args.tools else args.tools
    files = [AGENTS]
    for tool in requested:
        files.extend(TOOLS[tool])

    created: list[str] = []
    skipped: list[str] = []
    for relative in dict.fromkeys(files):
        source = KIT_ROOT / relative
        destination = target / relative
        if not source.is_file():
            print(f"Kit source file is missing: {relative}", file=sys.stderr)
            return 2
        if destination.exists():
            skipped.append(relative)
            continue
        if args.dry_run:
            created.append(relative)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        created.append(relative)

    action = "Would add" if args.dry_run else "Added"
    print(f"{action} {len(created)} file(s) to {target}:")
    for relative in created:
        print(f"  + {relative}")
    if skipped:
        print("Kept existing files (nothing was overwritten):")
        for relative in skipped:
            print(f"  = {relative}")
        if AGENTS in skipped:
            print("Merge the kit guidance into your existing AGENTS.md if useful.")
        if ".aider.conf.yml" in skipped:
            print("Add `read: AGENTS.md` to your existing Aider config if desired.")
    print("Review the added files, then fill in project-specific commands and rules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
