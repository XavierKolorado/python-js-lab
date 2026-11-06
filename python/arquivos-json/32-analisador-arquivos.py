"""32. Analisador de arquivos: conta linhas, palavras e caracteres.

Uso: python 32-analisador-arquivos.py [arquivo]
Sem argumento, o programa analisa o próprio código-fonte.
"""

import sys
from pathlib import Path


def analyze_text(text: str) -> dict[str, int]:
    return {
        "linhas": len(text.splitlines()),
        "palavras": len(text.split()),
        "caracteres": len(text),
    }


def analyze_file(path: Path) -> dict[str, int]:
    return analyze_text(path.read_text(encoding="utf-8"))


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__)
    try:
        statistics = analyze_file(path)
    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado: {path}")
        return 1
    except (IsADirectoryError, PermissionError):
        print(f"Erro: não foi possível abrir {path}")
        return 1
    except UnicodeDecodeError:
        print(f"Erro: {path} não é um arquivo de texto UTF-8.")
        return 1
    print(f"Arquivo: {path.name}")
    for label, value in statistics.items():
        print(f"{label.capitalize()}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
