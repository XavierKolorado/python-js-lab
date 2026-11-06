// 30. Carrinho de compras: adiciona, remove e totaliza produtos.
"use strict";

class ShoppingCart {
  #items = new Map();

  add(name, price, quantity = 1) {
    if (!name || !Number.isFinite(price) || price < 0) {
      throw new Error("Produto inválido.");
    }
    if (!Number.isInteger(quantity) || quantity < 1) {
      throw new Error("A quantidade precisa ser um inteiro positivo.");
    }
    const current = this.#items.get(name);
    this.#items.set(name, { name, price, quantity: (current?.quantity ?? 0) + quantity });
  }

  remove(name) {
    if (!this.#items.delete(name)) {
      throw new Error(`Produto fora do carrinho: ${name}`);
    }
  }

  get items() {
    return [...this.#items.values()];
  }

  get total() {
    return this.items.reduce((sum, { price, quantity }) => sum + price * quantity, 0);
  }
}

function main() {
  const cart = new ShoppingCart();
  cart.add("Caderno", 25.9, 2);
  cart.add("Caneta", 4.5, 3);
  cart.add("Mochila", 129.9);
  cart.remove("Caneta");
  cart.items.forEach(({ name, price, quantity }) => {
    console.log(`${quantity}x ${name} - R$ ${(price * quantity).toFixed(2)}`);
  });
  console.log(`Total: R$ ${cart.total.toFixed(2)}`);
}

if (require.main === module) {
  main();
}

module.exports = { ShoppingCart };
