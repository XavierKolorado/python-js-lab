"""47. Gerenciador de tarefas com API: cliente REST para a JSONPlaceholder.

Uso:
  python 47-tarefas-api.py listar --usuario 1
  python 47-tarefas-api.py criar "Estudar HTTP"
  python 47-tarefas-api.py concluir 5
  python 47-tarefas-api.py excluir 5

A JSONPlaceholder responde como uma API real, mas não grava alterações.
"""

import argparse
import sys

import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"
TIMEOUT_SECONDS = 10
LIST_LIMIT = 5


class TaskApiClient:
    def __init__(self, base_url: str = BASE_URL) -> None:
        self.base_url = base_url
        self.session = requests.Session()

    def _request(self, method: str, url: str, **options) -> requests.Response:
        response = self.session.request(method, url, timeout=TIMEOUT_SECONDS, **options)
        response.raise_for_status()
        return response

    def list_tasks(self, user_id: int) -> list[dict]:
        return self._request("GET", self.base_url, params={"userId": user_id}).json()

    def create_task(self, title: str, user_id: int = 1) -> dict:
        if not title.strip():
            raise ValueError("O título é obrigatório.")
        payload = {"title": title.strip(), "completed": False, "userId": user_id}
        return self._request("POST", self.base_url, json=payload).json()

    def complete_task(self, task_id: int) -> dict:
        url = f"{self.base_url}/{task_id}"
        return self._request("PATCH", url, json={"completed": True}).json()

    def delete_task(self, task_id: int) -> None:
        self._request("DELETE", f"{self.base_url}/{task_id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Cliente REST de tarefas.")
    commands = parser.add_subparsers(dest="command", required=True)
    list_command = commands.add_parser("listar")
    list_command.add_argument("--usuario", type=int, default=1)
    commands.add_parser("criar").add_argument("titulo")
    commands.add_parser("concluir").add_argument("id", type=int)
    commands.add_parser("excluir").add_argument("id", type=int)
    return parser


def run_command(client: TaskApiClient, options: argparse.Namespace) -> None:
    if options.command == "listar":
        tasks = client.list_tasks(options.usuario)
        print(f"{len(tasks)} tarefa(s). Primeiras {LIST_LIMIT}:")
        for task in tasks[:LIST_LIMIT]:
            mark = "x" if task["completed"] else " "
            print(f"[{mark}] {task['id']}. {task['title']}")
    elif options.command == "criar":
        task = client.create_task(options.titulo)
        print(f"Tarefa simulada com id {task['id']}: {task['title']}")
    elif options.command == "concluir":
        task = client.complete_task(options.id)
        print(f"Tarefa {task['id']} concluída (simulação).")
    else:
        client.delete_task(options.id)
        print(f"Tarefa {options.id} excluída (simulação).")


def main() -> int:
    options = build_parser().parse_args()
    try:
        run_command(TaskApiClient(), options)
    except ValueError as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro ao chamar a API: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
