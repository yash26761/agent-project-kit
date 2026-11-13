#!/usr/bin/env python3
"""Read-only checks for the Agent Project Kit instruction adapters."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ADAPTERS = {
    "Claude Code": ("CLAUDE.md", "@AGENTS.md"),
    "Gemini CLI": ("GEMINI.md", "@./AGENTS.md"),
    "GitHub Copilot CLI": (".github/copilot-instructions.md", "@../AGENTS.md"),
    "Aider": (".aider.conf.yml", "read: AGENTS.md"),
    "Continue": (".continue/rules/00-project.md", "AGENTS.md"),
}
DIRECT_AGENTS_TOOLS = ("Codex", "Cursor", "Cline", "Windsurf")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check whether supported coding agents can find the shared AGENTS.md."
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.cwd(),
        help="Project directory to inspect (default: current directory)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable results",
    )
    return parser.parse_args()


def adapter_is_connected(root: Path, tool: str, path: str, marker: str) -> tuple[str, str]:
    adapter_path = root / path
    if not adapter_path.is_file():
        return "not-installed", f"{path} is not present"

    content = adapter_path.read_text(encoding="utf-8", errors="replace")
    if tool == "Aider":
        connected = any(
            line.strip().startswith("read:") and "AGENTS.md" in line
            for line in content.splitlines()
        )
    else:
        connected = marker in content

    if connected:
        return "connected", f"{path} points to AGENTS.md"
    return "review", f"{path} exists but does not use the kit's AGENTS.md bridge"


def inspect(root: Path) -> dict[str, object]:
    agents_file = root / "AGENTS.md"
    results: list[dict[str, str]] = []

    if agents_file.is_file():
        results.append({
            "tool": ", ".join(DIRECT_AGENTS_TOOLS),
            "status": "connected",
            "detail": "Root AGENTS.md is present",
        })
    else:
        results.append({
            "tool": ", ".join(DIRECT_AGENTS_TOOLS),
            "status": "missing",
            "detail": "Root AGENTS.md is missing",
        })

    for tool, (path, marker) in ADAPTERS.items():
        status, detail = adapter_is_connected(root, tool, path, marker)
        results.append({"tool": tool, "status": status, "detail": detail})

    return {
        "target": str(root),
        "canonical_file": "AGENTS.md",
        "results": results,
        "ok": agents_file.is_file() and all(
            item["status"] != "review" for item in results
        ),
    }


def main() -> int:
    args = parse_args()
    root = args.target.expanduser().resolve()
    if not root.is_dir():
        print(f"Target directory does not exist: {root}")
        return 2

    report = inspect(root)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Agent Project Kit check: {root}")
        for result in report["results"]:
            tool = result["tool"]
            status = result["status"].upper()
            print(f"[{status}] {tool}: {result['detail']}")
        if not report["ok"]:
            print("Add AGENTS.md or review adapter files marked REVIEW.")
        print("This checks repository files only; it does not launch or authenticate AI tools.")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
