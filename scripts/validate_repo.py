#!/usr/bin/env python3
"""Validate the public coach packs without exposing local learner records."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_SESSION_FILES = {"sessions/README.md", "sessions/example.md"}
REQUIRED_FILES = {
    ".gitignore",
    "AGENTS.md",
    "LOCAL_PROFILE.example.md",
    "README.en.md",
    "README.md",
    "README.zh-CN.md",
    "START_HERE.md",
    "docs/COACH_PACK_CONTRACT.md",
    "sessions/README.md",
    "sessions/example.md",
}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def tracked_files() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return {
        path.decode("utf-8")
        for path in result.stdout.split(b"\0")
        if path
    }


def local_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
    parsed = urlparse(target)
    if parsed.scheme or target.startswith(("#", "mailto:", "data:")):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    return (source.parent / path).resolve()


def main() -> int:
    tracked = tracked_files()
    errors: list[str] = []

    missing = sorted(REQUIRED_FILES - tracked)
    if missing:
        errors.append("missing required tracked files: " + ", ".join(missing))

    if "LOCAL_PROFILE.md" in tracked:
        errors.append("LOCAL_PROFILE.md is private and must not be tracked")

    private_sessions = sorted(
        path
        for path in tracked
        if path.startswith("sessions/") and path not in ALLOWED_SESSION_FILES
    )
    if private_sessions:
        errors.append("private session receipts are tracked: " + ", ".join(private_sessions))

    obsidian_files = sorted(path for path in tracked if path.startswith(".obsidian/"))
    if obsidian_files:
        errors.append("local Obsidian state is tracked: " + ", ".join(obsidian_files))

    coach_files = sorted(ROOT.glob("coaches/**/COACH.md"))
    if not coach_files:
        errors.append("no coach packs found")
    for coach_file in coach_files:
        receipt_file = coach_file.with_name("RECEIPT.md")
        if not receipt_file.is_file():
            errors.append(f"coach pack lacks RECEIPT.md: {coach_file.parent.relative_to(ROOT)}")

    for markdown_file in sorted(ROOT.glob("**/*.md")):
        if ".git" in markdown_file.parts:
            continue
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = local_link_target(markdown_file, raw_target)
            if target is None:
                continue
            if not target.is_relative_to(ROOT) or not target.exists():
                relative_source = markdown_file.relative_to(ROOT)
                errors.append(f"broken local link in {relative_source}: {raw_target}")

    if errors:
        print("2torGPT validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "2torGPT validation passed: "
        f"{len(coach_files)} coach packs, privacy boundary intact, local links resolved."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
