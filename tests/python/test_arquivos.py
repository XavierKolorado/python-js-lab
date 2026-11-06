import json
from decimal import Decimal

import pytest

from helpers import load, run_script


def test_31_saves_appends_and_reads(tmp_path):
    module = load(31)
    module.save_note(tmp_path, "ideias", "primeira")
    module.save_note(tmp_path, "ideias", "segunda")
    assert module.read_note(tmp_path, "ideias") == "primeira\nsegunda\n"
    assert module.list_notes(tmp_path) == ["ideias"]


def test_31_blocks_path_traversal(tmp_path):
    with pytest.raises(ValueError):
        load(31).note_path(tmp_path, "../segredo")


def test_31_missing_note_is_reported(tmp_path):
    assert "não existe" in run_script(31, "2\nnada\n0\n", str(tmp_path)).stdout


def test_32_statistics_and_missing_file(tmp_path):
    module = load(32)
    assert module.analyze_text("um dois\ntrês\n") == {"linhas": 2, "palavras": 3, "caracteres": 13}
    assert module.analyze_text("") == {"linhas": 0, "palavras": 0, "caracteres": 0}
    result = run_script(32, "", str(tmp_path / "nao-existe.txt"))
    assert result.returncode == 1
    assert "não encontrado" in result.stdout


def test_33_persists_and_rejects_duplicates(tmp_path):
    module = load(33)
    path = tmp_path / "sub" / "usuarios.json"
    users = module.load_users(path)
    module.add_user(users, "Ana", "ANA@example.com")
    module.save_users(path, users)
    reloaded = module.load_users(path)
    assert reloaded == [{"name": "Ana", "email": "ana@example.com"}]
    with pytest.raises(ValueError):
        module.add_user(reloaded, "Outra", "ana@example.com")
    with pytest.raises(ValueError):
        module.add_user(reloaded, "Bia", "sem-arroba")


def test_33_invalid_json_stops_without_overwriting(tmp_path):
    path = tmp_path / "usuarios.json"
    path.write_text("{quebrado", encoding="utf-8")
    result = run_script(33, "", str(path))
    assert result.returncode == 1
    assert path.read_text(encoding="utf-8") == "{quebrado"


def test_34_full_crud_survives_reload(tmp_path):
    module = load(34)
    path = tmp_path / "tarefas.json"
    store = module.TaskStore(path)
    first = store.create("Estudar")
    second = store.create("Praticar")
    store.update(first["id"], "Estudar Python")
    store.complete(first["id"])
    store.delete(second["id"])
    reloaded = module.TaskStore(path)
    assert reloaded.tasks == [{"id": 1, "title": "Estudar Python", "done": True}]
    assert reloaded.create("Nova")["id"] == 2
    with pytest.raises(KeyError):
        reloaded.complete(99)
    with pytest.raises(ValueError):
        reloaded.create("  ")


def test_35_balance_is_exact(tmp_path):
    module = load(35)
    transactions = []
    module.add_transaction(transactions, module.INCOME, "Salário", module.parse_amount("0,10"))
    module.add_transaction(transactions, module.INCOME, "Bônus", module.parse_amount("0.20"))
    module.add_transaction(transactions, module.EXPENSE, "Café", module.parse_amount("0.05"))
    assert module.calculate_balance(transactions) == Decimal("0.25")
    path = tmp_path / "financas.json"
    module.save_transactions(path, transactions)
    assert module.load_transactions(path) == transactions


@pytest.mark.parametrize("raw_amount", ["abc", "0", "-5", "NaN", "Infinity"])
def test_35_rejects_invalid_amounts(raw_amount):
    with pytest.raises(ValueError):
        load(35).parse_amount(raw_amount)


def test_36_history_is_written_and_errors_are_not(tmp_path):
    path = tmp_path / "historico.txt"
    output = run_script(36, "2 + 3\n1 / 0\nabc\nx + 1\nhistorico\nsair\n", str(path)).stdout
    assert "dividir por zero" in output
    assert path.read_text(encoding="utf-8") == "2 + 3 = 5\n"


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("ana@example.com", True),
        ("ana.souza+lab@sub.example.com.br", True),
        ("sem-arroba.com", False),
        ("ana@", False),
        ("@example.com", False),
        ("ana@example", False),
        ("a..b@example.com", False),
        (".ana@example.com", False),
        ("ana@-example.com", False),
        ("ana silva@example.com", False),
    ],
)
def test_37_email_format(email, expected):
    assert load(37).is_valid_email(email) is expected


def test_38_password_contains_every_selected_group():
    module = load(38)
    groups = module.build_character_groups(digits=True, uppercase=True, symbols=True)
    for _ in range(50):
        password = module.generate_password(8, groups)
        assert len(password) == 8
        assert all(any(char in group for char in password) for group in groups)


def test_38_respects_options_and_minimum():
    module = load(38)
    groups = module.build_character_groups(digits=False, uppercase=False, symbols=False)
    assert module.generate_password(20, groups).islower()
    with pytest.raises(ValueError):
        module.generate_password(7, groups)
    assert run_script(38, "", "--tamanho", "4").returncode != 0


def test_39_lend_and_return_survive_reload(tmp_path):
    module = load(39)
    path = tmp_path / "biblioteca.json"
    library = module.Library(path)
    library.add_book("Dom Casmurro", "Machado de Assis")
    library.lend("dom casmurro", "Ana")
    with pytest.raises(ValueError):
        library.lend("Dom Casmurro", "Bia")
    reloaded = module.Library(path)
    assert reloaded.books[0]["borrower"] == "Ana"
    reloaded.give_back("Dom Casmurro")
    with pytest.raises(ValueError):
        reloaded.give_back("Dom Casmurro")
    with pytest.raises(KeyError):
        reloaded.lend("Inexistente", "Ana")


def test_40_errors_are_translated_to_value_error(tmp_path):
    module = load(40)
    assert module.parse_age("30") == 30
    assert module.parse_json('{"a": 1}') == {"a": 1}
    with pytest.raises(ValueError):
        module.parse_age("trinta")
    with pytest.raises(ValueError):
        module.read_text_file(tmp_path / "nada.txt")
    with pytest.raises(ValueError):
        module.parse_json("{")


def test_40_demo_shows_success_and_failure():
    output = run_script(40).stdout
    assert output.count("[ok]") == 2
    assert output.count("[erro]") == 4


def test_json_files_stay_readable_with_accents(tmp_path):
    module = load(33)
    path = tmp_path / "usuarios.json"
    module.save_users(path, [{"name": "João", "email": "j@e.co"}])
    assert "João" in path.read_text(encoding="utf-8")
    assert json.loads(path.read_text(encoding="utf-8"))[0]["name"] == "João"
