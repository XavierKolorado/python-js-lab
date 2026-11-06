"""Repository-level checks: all 100 exercises exist and nothing is a placeholder."""

import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from catalog import EXERCISES  # noqa: E402

PLACEHOLDER_PATTERN = re.compile(r"\b(TODO|FIXME|pseudoc[óo]digo)\b|NotImplementedError|^\s*pass\s*$", re.MULTILINE)


def solution_files(exercise) -> list[Path]:
    path = ROOT / exercise.repo_path
    if exercise.browser:
        return [path / "index.html", path / "style.css", path / "script.js"]
    return [path]


def test_catalog_has_fifty_exercises_per_language():
    for language in ("python", "javascript"):
        numbers = [exercise.number for exercise in EXERCISES if exercise.language == language]
        assert numbers == list(range(1, 51))


@pytest.mark.parametrize("exercise", EXERCISES, ids=lambda exercise: exercise.repo_path)
def test_exercise_files_are_real_solutions(exercise):
    for path in solution_files(exercise):
        assert path.is_file(), path
        content = path.read_text(encoding="utf-8")
        assert len(content.strip()) > 100, path
        assert not PLACEHOLDER_PATTERN.search(content), path
