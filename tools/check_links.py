"""Fail when a relative Markdown link points to a file that does not exist.

Usage: python tools/check_links.py
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")
IGNORED_FOLDERS = {".venv", "node_modules", ".git"}


def markdown_files() -> list[Path]:
    return [
        path for path in ROOT.rglob("*.md")
        if not IGNORED_FOLDERS.intersection(path.relative_to(ROOT).parts) and ".template" not in path.name
    ]


def main() -> int:
    broken = []
    total = 0
    for markdown in markdown_files():
        content = re.sub(r"```.*?```", "", markdown.read_text(encoding="utf-8"), flags=re.DOTALL)
        for target in LINK_PATTERN.findall(content):
            total += 1
            clean_target = unquote(target.split("#")[0])
            if clean_target and not (markdown.parent / clean_target).exists():
                broken.append(f"{markdown.relative_to(ROOT)}: {target}")
    print(f"{total} relative links checked, {len(broken)} broken")
    print("\n".join(broken))
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
