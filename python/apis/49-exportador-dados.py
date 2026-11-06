"""49. Exportador de dados: consulta uma API e salva o resultado em JSON.

Uso: python 49-exportador-dados.py [arquivo.json]
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

SOURCE_URL = "https://jsonplaceholder.typicode.com/users"
DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "usuarios-exportados.json"
TIMEOUT_SECONDS = 10


def fetch_records(url: str = SOURCE_URL) -> list[dict]:
    response = requests.get(url, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def simplify_record(record: dict) -> dict:
    return {
        "id": record["id"],
        "name": record["name"],
        "email": record["email"],
        "city": record["address"]["city"],
        "company": record["company"]["name"],
    }


def build_export(records: list[dict]) -> dict:
    return {
        "source": SOURCE_URL,
        "exported_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total": len(records),
        "records": [simplify_record(record) for record in records],
    }


def save_export(path: Path, export: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(export, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        export = build_export(fetch_records())
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a API: {error}")
        return 1
    except (KeyError, TypeError):
        print("Erro: a API respondeu em um formato inesperado.")
        return 1
    save_export(path, export)
    print(f"{export['total']} registro(s) exportado(s) para {path.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
