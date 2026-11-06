import pytest

from helpers import load, run_script


def test_01_uses_default_name_for_blank_input():
    module = load(1)
    assert "Ana" in module.build_welcome_message(" Ana ")
    assert "visitante" in module.build_welcome_message("   ")


def test_02_rejects_age_out_of_range():
    module = load(2)
    assert module.parse_age(" 30 ") == 30
    with pytest.raises(ValueError):
        module.parse_age("131")
    assert "1 ano" in module.format_profile("Ana", 1)
    assert "1 anos" not in module.format_profile("Ana", 1)


def test_03_accepts_decimal_comma_and_rejects_infinity():
    module = load(3)
    assert module.parse_number("2,5") == 2.5
    assert module.add(2, 3) == 5
    with pytest.raises(ValueError):
        module.parse_number("inf")


def test_04_average_and_grade_limits():
    module = load(4)
    assert module.calculate_average([7, 8, 9]) == 8
    with pytest.raises(ValueError):
        module.parse_grade("10.5")
    with pytest.raises(ValueError):
        module.calculate_average([])


@pytest.mark.parametrize(("celsius", "fahrenheit"), [(0, 32), (100, 212), (-40, -40)])
def test_05_known_temperatures(celsius, fahrenheit):
    assert load(5).celsius_to_fahrenheit(celsius) == fahrenheit


def test_05_rejects_below_absolute_zero():
    with pytest.raises(ValueError):
        load(5).celsius_to_fahrenheit(-300)


def test_06_conversion_and_invalid_rate():
    module = load(6)
    assert module.convert_brl_to_usd(100, 5) == 20
    with pytest.raises(ValueError):
        module.convert_brl_to_usd(100, 0)


def test_07_rectangle_measures():
    module = load(7)
    assert module.rectangle_measures(3, 4) == (12, 14)
    with pytest.raises(ValueError):
        module.rectangle_measures(0, 4)


@pytest.mark.parametrize(("number", "label"), [(0, "par"), (7, "ímpar"), (-4, "par"), (-3, "ímpar")])
def test_08_parity(number, label):
    assert load(8).parity(number) == label


def test_09_legal_age_boundary():
    module = load(9)
    assert module.is_adult(18) is True
    assert module.is_adult(17) is False
    with pytest.raises(ValueError):
        module.is_adult(-1)


@pytest.mark.parametrize("numbers", [(1, 2, 3), (3, 2, 1), (2, 3, 1), (3, 3, 3)])
def test_10_largest_in_any_position(numbers):
    assert load(10).largest_of_three(*numbers) == 3


@pytest.mark.parametrize(
    ("number", "stdin", "expected"),
    [
        (2, "\nAna\nabc\n200\n30\n", "Idade inválida"),
        (3, "abc\n1\n2\n", "1 + 2 = 3"),
        (4, "11\n7\n8\n9\n", "Média: 8.00"),
        (5, "x\n-300\n100\n", "212.0 °F"),
        (6, "-1\n100\n0\n5\n", "US$ 20.00"),
        (7, "0\n2\n3\n", "Área: 6"),
        (8, "1.5\n4\n", "4 é par"),
        (9, "-1\n17\n", "Faltam 1 ano(s)"),
        (10, "nan\n1\n2\n3\n", "Maior número: 3"),
    ],
)
def test_invalid_input_is_asked_again(number, stdin, expected):
    result = run_script(number, stdin)
    assert result.returncode == 0, result.stderr
    assert expected in result.stdout
