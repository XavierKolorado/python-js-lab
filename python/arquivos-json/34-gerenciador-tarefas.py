"""34. Gerenciador de tarefas: CRUD com persistência em JSON.

Uso: python 34-gerenciador-tarefas.py [arquivo.json]
"""

import json
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "tarefas.json"
MENU = """
1. Criar tarefa
2. Listar tarefas
3. Editar tarefa
4. Concluir tarefa
5. Excluir tarefa
0. Sair"""


class TaskStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.tasks: list[dict] = self._load()

    def _load(self) -> list[dict]:
        if not self.path.exists():
            return []
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ValueError(f"{self.path.name} contém JSON inválido.") from error

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        content = json.dumps(self.tasks, ensure_ascii=False, indent=2)
        self.path.write_text(content, encoding="utf-8")

    def _find(self, task_id: int) -> dict:
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        raise KeyError(f"Tarefa {task_id} não encontrada.")

    @staticmethod
    def _clean_title(title: str) -> str:
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("O título é obrigatório.")
        return clean_title

    def create(self, title: str) -> dict:
        next_id = max((task["id"] for task in self.tasks), default=0) + 1
        task = {"id": next_id, "title": self._clean_title(title), "done": False}
        self.tasks.append(task)
        self._save()
        return task

    def update(self, task_id: int, title: str) -> dict:
        task = self._find(task_id)
        task["title"] = self._clean_title(title)
        self._save()
        return task

    def complete(self, task_id: int) -> dict:
        task = self._find(task_id)
        task["done"] = True
        self._save()
        return task

    def delete(self, task_id: int) -> None:
        self.tasks.remove(self._find(task_id))
        self._save()


def print_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {task['id']}. {task['title']}")


def read_task_id() -> int:
    raw_id = input("Número da tarefa: ").strip()
    if not raw_id.isdigit():
        raise ValueError("Digite um número válido.")
    return int(raw_id)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        store = TaskStore(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                print(f"Tarefa {store.create(input('Título: '))['id']} criada.")
            elif option == "2":
                print_tasks(store.tasks)
            elif option == "3":
                store.update(read_task_id(), input("Novo título: "))
                print("Tarefa atualizada.")
            elif option == "4":
                store.complete(read_task_id())
                print("Tarefa concluída.")
            elif option == "5":
                store.delete(read_task_id())
                print("Tarefa excluída.")
            elif option == "0":
                print("Até logo!")
                return 0
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as error:
            print(f"Erro: {error.args[0]}")


if __name__ == "__main__":
    sys.exit(main())
