"""Run every terminal exercise with its catalog input and record the real output.

Usage: python tools/run_examples.py [--offline]

--offline skips exercises that need the network and keeps their recorded output.
The recorded output feeds the documentation, so examples are never written by hand.
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from catalog import EXERCISES

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_PATH = Path(__file__).with_name("examples.json")
TIMEOUT_SECONDS = 60


def build_command(exercise, temporary_directory: str) -> list[str]:
    interpreter = sys.executable if exercise.language == "python" else "node"
    hidden = [argument.format(tmp=temporary_directory) for argument in exercise.hidden_args]
    return [interpreter, exercise.repo_path, *hidden, *exercise.args]


def run_exercise(exercise) -> subprocess.CompletedProcess:
    with tempfile.TemporaryDirectory() as temporary_directory:
        return subprocess.run(
            build_command(exercise, temporary_directory),
            cwd=ROOT,
            input=exercise.stdin,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONUTF8": "1"},
            timeout=TIMEOUT_SECONDS,
        )


def main() -> int:
    offline = "--offline" in sys.argv
    examples = json.loads(EXAMPLES_PATH.read_text(encoding="utf-8")) if EXAMPLES_PATH.exists() else {}
    failures = []
    executed = skipped = 0
    for exercise in EXERCISES:
        if exercise.browser or (offline and exercise.network):
            skipped += 1
            continue
        result = run_exercise(exercise)
        executed += 1
        if result.returncode != 0 or "Traceback" in result.stderr:
            failures.append(f"{exercise.repo_path}: exit {result.returncode}\n{result.stderr}{result.stdout}")
        else:
            examples[exercise.repo_path] = result.stdout.rstrip()
    EXAMPLES_PATH.write_text(json.dumps(examples, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{executed} executed, {skipped} skipped, {len(failures)} failed")
    print("\n".join(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
