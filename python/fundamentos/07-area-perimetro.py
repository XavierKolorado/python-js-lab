"""07. Área e perímetro: calcula as medidas de um retângulo."""

import math


def rectangle_measures(width: float, height: float) -> tuple[float, float]:
    if width <= 0 or height <= 0:
        raise ValueError("Largura e altura precisam ser maiores que zero.")
    return width * height, 2 * (width + height)


def read_side(prompt: str) -> float:
    while True:
        try:
            side = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if math.isfinite(side) and side > 0:
            return side
        print("A medida precisa ser maior que zero.")


def main() -> None:
    width = read_side("Largura: ")
    height = read_side("Altura: ")
    area, perimeter = rectangle_measures(width, height)
    print(f"Área: {area:g}")
    print(f"Perímetro: {perimeter:g}")


if __name__ == "__main__":
    main()
