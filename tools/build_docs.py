"""Generate the README files from tools/catalog.py and tools/examples.json.

Usage: python tools/build_docs.py
"""

import json
from pathlib import Path

from catalog import EXERCISES, LEVELS

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = json.loads(Path(__file__).with_name("examples.json").read_text(encoding="utf-8"))
TEMPLATE = Path(__file__).with_name("README.template.md").read_text(encoding="utf-8")
MAX_EXAMPLE_LINES = 30
GENERATED_NOTICE = "<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->\n"
LANGUAGE_LABELS = {"python": "Python", "javascript": "JavaScript"}
CODE_FENCES = {".py": "python", ".js": "javascript", ".html": "html", ".css": "css"}


def exists_and_has_content(exercise) -> bool:
    path = ROOT / exercise.repo_path
    if exercise.browser:
        parts = [path / name for name in ("index.html", "style.css", "script.js")]
        return all(part.is_file() and part.stat().st_size > 0 for part in parts)
    return path.is_file() and path.stat().st_size > 0


def run_command(exercise) -> str:
    interpreter = "python" if exercise.language == "python" else "node"
    arguments = [
        f"'{argument}'" if any(char in argument for char in ' {"') else argument
        for argument in exercise.args
    ]
    return " ".join([interpreter, exercise.repo_path, *arguments])


def trimmed_output(exercise) -> str:
    lines = EXAMPLES[exercise.repo_path].splitlines()
    if len(lines) <= MAX_EXAMPLE_LINES:
        return "\n".join(lines)
    return "\n".join([*lines[:MAX_EXAMPLE_LINES], f"... ({len(lines) - MAX_EXAMPLE_LINES} linhas omitidas)"])


def execution_section(exercise) -> list[str]:
    if exercise.browser:
        folder = exercise.repo_path
        return [
            "**Como executar / How to run**",
            "",
            "```bash",
            "python -m http.server 8000",
            "```",
            "",
            f"Abra / Open: `http://localhost:8000/{folder}/`",
            "",
        ]
    section = ["**Como executar / How to run**", "", "```bash", run_command(exercise), "```", ""]
    if exercise.stdin:
        typed = " · ".join(f"`{line}`" for line in exercise.stdin.splitlines())
        section += [f"**Entradas do exemplo / Example input:** {typed}", ""]
    section += ["**Exemplo de execução / Example run**", "", "```text", trimmed_output(exercise), "```", ""]
    return section


def code_block(path: Path) -> list[str]:
    fence = CODE_FENCES[path.suffix]
    return [
        f"<details><summary>Código completo / Full code: <code>{path.name}</code></summary>",
        "",
        f"```{fence}",
        path.read_text(encoding="utf-8").rstrip(),
        "```",
        "",
        "</details>",
        "",
    ]


def exercise_doc(exercise, heading: str, link_prefix: str) -> list[str]:
    lines = [
        f"{heading} {exercise.number:02d}. {exercise.title_pt} / {exercise.title_en}",
        "",
        f"**Problema:** {exercise.description_pt}  ",
        f"**Problem:** {exercise.description_en}",
        "",
        f"**Objetivo:** {exercise.goal_pt}  ",
        f"**Goal:** {exercise.goal_en}",
        "",
        f"**Conceitos / Concepts:** {exercise.concepts}",
        "",
    ]
    if link_prefix is not None:
        lines += [f"**Arquivo / File:** [`{exercise.path}`]({link_prefix}{exercise.path})", ""]
    lines += execution_section(exercise)
    lines += [
        f"**Resultado esperado:** {exercise.expected_pt}  ",
        f"**Expected result:** {exercise.expected_en}",
        "",
    ]
    return lines


def write_browser_readme(exercise) -> None:
    folder = ROOT / exercise.repo_path
    lines = [GENERATED_NOTICE]
    lines += exercise_doc(exercise, "#", None)
    for name in ("index.html", "style.css", "script.js"):
        if name != "style.css":
            lines += code_block(folder / name)
    lines.append("O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.\n")
    (folder / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_level_readme(level) -> None:
    exercises = [
        exercise for exercise in EXERCISES
        if exercise.language == level.language and exercise.folder == level.folder
    ]
    label = LANGUAGE_LABELS[level.language]
    lines = [
        GENERATED_NOTICE,
        f"# {label}, nível {level.number}: {level.title_pt}",
        "",
        f"*{label}, level {level.number}: {level.title_en}*",
        "",
        "[Voltar ao README principal / Back to the main README](../../README.md)",
        "",
    ]
    for exercise in exercises:
        anchor_target = f"{exercise.path}/" if exercise.browser else exercise.path
        lines.append(f"- [{exercise.number:02d}. {exercise.title_pt}]({anchor_target})")
    lines.append("")
    for exercise in exercises:
        lines += exercise_doc(exercise, "##", "./")
        if exercise.browser:
            write_browser_readme(exercise)
        else:
            lines += code_block(ROOT / exercise.repo_path)
    path = ROOT / level.language / level.folder / "README.md"
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def exercise_table(language: str) -> str:
    sections = []
    for level in (item for item in LEVELS if item.language == language):
        rows = [
            f"### Nível {level.number}: {level.title_pt} · *{level.title_en}*",
            "",
            f"[Documentação do nível / Level docs]({language}/{level.folder}/README.md)",
            "",
            "| # | Exercício | Exercise | Conceitos / Concepts |",
            "|---:|---|---|---|",
        ]
        for exercise in EXERCISES:
            if exercise.language == language and exercise.folder == level.folder:
                rows.append(
                    f"| {exercise.number:02d} | [{exercise.title_pt}]({exercise.repo_path}) "
                    f"| {exercise.title_en} | {exercise.concepts} |"
                )
        sections.append("\n".join(rows))
    return "\n\n".join(sections)


def progress_checklist(language: str) -> str:
    lines = []
    for exercise in EXERCISES:
        if exercise.language == language:
            mark = "x" if exists_and_has_content(exercise) else " "
            lines.append(f"- [{mark}] {exercise.number:02d}. {exercise.title_pt}")
    return "\n".join(lines)


def count_solved(language: str) -> int:
    return sum(
        exists_and_has_content(exercise)
        for exercise in EXERCISES
        if exercise.language == language
    )


def write_root_readme() -> None:
    python_total = sum(exercise.language == "python" for exercise in EXERCISES)
    javascript_total = sum(exercise.language == "javascript" for exercise in EXERCISES)
    python_solved = count_solved("python")
    javascript_solved = count_solved("javascript")
    replacements = {
        "{{PY_TOTAL}}": python_total,
        "{{JS_TOTAL}}": javascript_total,
        "{{TOTAL}}": python_total + javascript_total,
        "{{PY_SOLVED}}": python_solved,
        "{{JS_SOLVED}}": javascript_solved,
        "{{SOLVED}}": python_solved + javascript_solved,
        "{{PY_TABLE}}": exercise_table("python"),
        "{{JS_TABLE}}": exercise_table("javascript"),
        "{{PY_CHECKLIST}}": progress_checklist("python"),
        "{{JS_CHECKLIST}}": progress_checklist("javascript"),
    }
    content = TEMPLATE
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, str(value))
    (ROOT / "README.md").write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    for level in LEVELS:
        write_level_readme(level)
    write_root_readme()
    print(f"Docs generated for {len(EXERCISES)} exercises.")


if __name__ == "__main__":
    main()
