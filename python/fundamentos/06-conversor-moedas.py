"""06. Conversor de moedas: converte reais para dólares com a cotação informada."""

import math


def convert_brl_to_usd(amount_brl: float, usd_rate: float) -> float:
    if amount_brl < 0:
        raise ValueError("O valor em reais não pode ser negativo.")
    if usd_rate <= 0:
        raise ValueError("A cotação precisa ser maior que zero.")
    return amount_brl / usd_rate


def read_positive_number(prompt: str, allow_zero: bool) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if math.isfinite(value) and (value > 0 or (allow_zero and value == 0)):
            return value
        print("O número precisa ser positivo.")


def main() -> None:
    amount_brl = read_positive_number("Valor em reais (R$): ", allow_zero=True)
    usd_rate = read_positive_number("Cotação do dólar (R$ por US$ 1): ", allow_zero=False)
    amount_usd = convert_brl_to_usd(amount_brl, usd_rate)
    print(f"R$ {amount_brl:.2f} = US$ {amount_usd:.2f} (cotação {usd_rate:.4f})")


if __name__ == "__main__":
    main()
