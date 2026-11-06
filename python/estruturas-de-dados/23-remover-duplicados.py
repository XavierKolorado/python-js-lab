"""23. Remover duplicados: mantém a primeira ocorrência e a ordem original."""


def remove_duplicates(items: list) -> list:
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items


def main() -> None:
    items = input("Itens separados por espaço: ").split()
    unique_items = remove_duplicates(items)
    print(f"Sem duplicados: {' '.join(unique_items) or '(lista vazia)'}")
    print(f"Removidos: {len(items) - len(unique_items)}")


if __name__ == "__main__":
    main()
