"""05. Conversor Celsius para Fahrenheit: aplica F = C * 9/5 + 32."""

import math

ABSOLUTE_ZERO_CELSIUS = -273.15


def celsius_to_fahrenheit(celsius: float) -> float:
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError("A temperatura está abaixo do zero absoluto.")
    return celsius * 9 / 5 + 32


def read_celsius() -> float:
    while True:
        try:
            celsius = float(input("Temperatura em °C: ").strip().replace(",", "."))
            if not math.isfinite(celsius):
                raise ValueError("A temperatura precisa ser finita.")
            celsius_to_fahrenheit(celsius)
            return celsius
        except ValueError:
            print(f"Valor inválido. Digite um número a partir de {ABSOLUTE_ZERO_CELSIUS}.")


def main() -> None:
    celsius = read_celsius()
    print(f"{celsius:.1f} °C = {celsius_to_fahrenheit(celsius):.1f} °F")


if __name__ == "__main__":
    main()
