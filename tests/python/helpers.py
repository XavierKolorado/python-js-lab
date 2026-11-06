"""Shared helpers: exercise file names start with digits, so `import` cannot load them."""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[2]
PYTHON_ROOT = ROOT / "python"


def exercise_path(number: int) -> Path:
    matches = list(PYTHON_ROOT.glob(f"*/{number:02d}-*.py"))
    assert len(matches) == 1, f"expected one file for exercise {number}, got {matches}"
    return matches[0]


def load(number: int) -> ModuleType:
    path = exercise_path(number)
    module_name = f"exercise_{number:02d}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    # dataclasses and typing resolve names through sys.modules during import.
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def run_script(number: int, stdin: str = "", *args: str) -> subprocess.CompletedProcess:
    environment = {**os.environ, "PYTHONUTF8": "1"}
    return subprocess.run(
        [sys.executable, str(exercise_path(number)), *args],
        input=stdin,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=environment,
        timeout=30,
    )
