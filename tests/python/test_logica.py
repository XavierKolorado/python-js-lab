import pytest

from helpers import load, run_script


def test_11_all_operations():
    module = load(11)
    assert module.calculate(6, "+", 3) == 9
    assert module.calculate(6, "-", 3) == 3
    assert module.calculate(6, "*", 3) == 18
    assert module.calculate(6, "/", 3) == 2


def test_11_division_by_zero_and_unknown_operator():
    module = load(11)
    with pytest.raises(ZeroDivisionError):
        module.calculate(1, "/", 0)
    with pytest.raises(ValueError):
        module.calculate(1, "%", 2)
    assert "dividir por zero" in run_script(11, "1\n/\n0\n").stdout


@pytest.mark.parametrize(
    ("year", "expected"),
    [(2024, True), (2023, False), (1900, False), (2000, True)],
)
def test_12_leap_years(year, expected):
    assert load(12).is_leap_year(year) is expected


def test_13_counts_one_to_limit():
    numbers = load(13).count_up_to(100)
    assert numbers[0] == 1 and numbers[-1] == 100 and len(numbers) == 100


def test_14_table_lines():
    lines = load(14).multiplication_table(7)
    assert len(lines) == 10
    assert lines[-1] == "7 x 10 = 70"


def test_15_sum():
    module = load(15)
    assert module.sum_up_to(100) == 5050
    with pytest.raises(ValueError):
        module.sum_up_to(0)


def test_16_factorial():
    module = load(16)
    assert module.factorial(0) == 1
    assert module.factorial(5) == 120
    with pytest.raises(ValueError):
        module.factorial(-1)


def test_17_guess_feedback_and_seeded_game():
    module = load(17)
    assert module.evaluate_guess(1, 5) == "maior"
    assert module.evaluate_guess(9, 5) == "menor"
    assert module.evaluate_guess(5, 5) == "acertou"
    stdin = "".join(f"{guess}\n" for guess in range(1, 101))
    assert "Parabéns" in run_script(17, stdin, "42").stdout


def test_18_login_accepts_only_correct_credentials():
    module = load(18)
    account = module.create_account("aluno", "segredo-teste")
    assert b"segredo-teste" not in account["hash"]
    assert module.verify_login(account, "aluno", "segredo-teste") is True
    assert module.verify_login(account, "aluno", "errada") is False
    assert module.verify_login(account, "outro", "segredo-teste") is False


def test_18_blocks_after_three_attempts():
    output = run_script(18, "x\ny\n" * 3).stdout
    assert "limite de tentativas" in output


@pytest.mark.parametrize("text", ["arara", "Ame a ema", "A sacada da casa", "Socorram-me, subi no ônibus em Marrocos"])
def test_19_palindromes(text):
    assert load(19).is_palindrome(text) is True


def test_19_non_palindrome_and_empty():
    module = load(19)
    assert module.is_palindrome("python") is False
    with pytest.raises(ValueError):
        module.is_palindrome(" ... ")


def test_20_counts_accented_vowels():
    counts = load(20).count_vowels("Água É ótima")
    assert counts == {"a": 3, "e": 1, "i": 1, "o": 1, "u": 1}
