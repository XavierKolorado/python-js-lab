import pytest

from helpers import load, run_script


def test_21_min_max_and_empty_list():
    module = load(21)
    assert module.find_min_max([3, -1, 9]) == (-1, 9)
    assert module.find_min_max([5]) == (5, 5)
    with pytest.raises(ValueError):
        module.find_min_max([])


def test_22_average_and_empty_list():
    module = load(22)
    assert module.average([2, 4, 6]) == 4
    with pytest.raises(ValueError):
        module.average([])


def test_23_keeps_first_occurrence_order():
    assert load(23).remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert load(23).remove_duplicates([]) == []


def test_24_sort_does_not_change_the_original():
    numbers = [5, 2, 9, 2, -1]
    assert load(24).insertion_sort(numbers) == [-1, 2, 2, 5, 9]
    assert numbers == [5, 2, 9, 2, -1]


def test_24_does_not_call_builtin_sorting():
    source = (load(24).__file__)
    code = open(source, encoding="utf-8").read().split('"""', 2)[2]
    assert "sorted(" not in code and ".sort(" not in code


def test_25_split():
    assert load(25).split_even_odd([1, 2, 3, 4, 0]) == ([2, 4, 0], [1, 3])


@pytest.mark.parametrize(
    ("number", "expected"),
    [(-7, False), (0, False), (1, False), (2, True), (9, False), (97, True), (7919, True)],
)
def test_26_primes(number, expected):
    assert load(26).is_prime(number) is expected


def test_27_reverse():
    assert load(27).reverse_text("Python") == "nohtyP"
    assert load(27).reverse_text("") == ""


def test_28_frequency_ignores_case_and_punctuation():
    frequencies = load(28).word_frequency("Olá, olá! Mundo guarda-chuva 123")
    assert frequencies == {"olá": 2, "mundo": 1, "guarda-chuva": 1}


def test_29_contact_book_flow():
    book = load(29).ContactBook()
    book.add("Ana", "1111")
    book.add("Bruno", "2222")
    assert [contact["name"] for contact in book.search("an")] == ["Ana"]
    with pytest.raises(ValueError):
        book.add("ana", "3333")
    book.delete("ANA")
    assert len(book.list_all()) == 1
    with pytest.raises(KeyError):
        book.delete("Ana")


def test_30_inventory_flow():
    inventory = load(30).Inventory()
    inventory.add_product("Caneta", 5)
    assert inventory.adjust_quantity("caneta", -2) == 3
    with pytest.raises(ValueError):
        inventory.adjust_quantity("caneta", -4)
    with pytest.raises(KeyError):
        inventory.quantity_of("Lápis")


@pytest.mark.parametrize(
    ("number", "stdin", "expected"),
    [
        (21, "\n", "lista está vazia"),
        (21, "1 a 3\n", "apenas números"),
        (22, "\n", "lista está vazia"),
        (24, "\n", "nada a ordenar"),
        (24, "x\n", "apenas números"),
        (25, "1 2.5\n", "apenas números inteiros"),
        (26, "abc\n", "Entrada inválida"),
        (29, "4\nNinguém\n9\n0\n", "não está na agenda"),
        (30, "3\nNada\n0\n", "Produto não encontrado"),
    ],
)
def test_invalid_input_is_reported_in_portuguese(number, stdin, expected):
    result = run_script(number, stdin)
    assert result.returncode == 0, result.stderr
    assert expected in result.stdout
