"use strict";

const assert = require("node:assert/strict");
const { test } = require("node:test");
const { load } = require("./helpers");

const collections = (number) => load("arrays-objetos", number);

test("21 encontra extremos", () => {
  const { findMinMax } = collections(21);
  assert.deepEqual(findMinMax([8, 3, 15]), { smallest: 3, largest: 15 });
  assert.deepEqual(findMinMax([4]), { smallest: 4, largest: 4 });
  assert.throws(() => findMinMax([]));
});

test("22 remove repetidos mantendo a ordem", () => {
  const { removeDuplicates } = collections(22);
  assert.deepEqual(removeDuplicates(["a", "b", "a"]), ["a", "b"]);
  assert.deepEqual(removeDuplicates([]), []);
});

test("23 filtra pares", () => {
  const { filterEven } = collections(23);
  assert.deepEqual(filterEven([1, 2, 3, 4, 0, -2]), [2, 4, 0, -2]);
  assert.deepEqual(filterEven([]), []);
});

test("24 transforma sem alterar o original", () => {
  const { doubleValues, applyIncrease, toLabels } = collections(24);
  const products = [{ name: "A", price: 100 }];
  assert.deepEqual(doubleValues([1, 2]), [2, 4]);
  assert.ok(Math.abs(applyIncrease(products, 10)[0].price - 110) < 1e-9);
  assert.equal(products[0].price, 100);
  assert.deepEqual(toLabels(products), ["A: R$ 100.00"]);
});

test("25 soma com reduce e aceita array vazio", () => {
  const { sumValues } = collections(25);
  assert.equal(sumValues([10, 20, 30]), 60);
  assert.equal(sumValues([]), 0);
});

test("26 ordena sem alterar o original", () => {
  const { sortByPrice } = collections(26);
  const products = [{ price: 3 }, { price: 1 }, { price: 2 }];
  assert.deepEqual(sortByPrice(products).map(({ price }) => price), [1, 2, 3]);
  assert.deepEqual(sortByPrice(products, "desc").map(({ price }) => price), [3, 2, 1]);
  assert.equal(products[0].price, 3);
  assert.throws(() => sortByPrice(products, "lado"));
});

test("27 consulta o catálogo", () => {
  const { CATALOG, listCategories, filterByCategory, findProduct, formatProduct } = collections(27);
  assert.deepEqual(listCategories(CATALOG), ["informática", "móveis"]);
  assert.equal(filterByCategory(CATALOG, "móveis").length, 2);
  assert.deepEqual(filterByCategory(CATALOG, "nada"), []);
  assert.equal(findProduct(CATALOG, 99), null);
  assert.match(formatProduct(findProduct(CATALOG, 3)), /esgotado/);
});

test("28 busca ignorando acentos e maiúsculas", () => {
  const { USERS, searchUsers } = collections(28);
  assert.deepEqual(searchUsers(USERS, "ANA").map(({ id }) => id), [1, 3]);
  assert.deepEqual(searchUsers(USERS, "joao").map(({ id }) => id), [4]);
  assert.deepEqual(searchUsers(USERS, "zzz"), []);
});

test("29 agrupa nas fronteiras", () => {
  const { getAgeGroup, groupByAge } = collections(29);
  assert.equal(getAgeGroup(11), "crianças");
  assert.equal(getAgeGroup(12), "adolescentes");
  assert.equal(getAgeGroup(18), "adultos");
  assert.equal(getAgeGroup(60), "idosos");
  assert.throws(() => getAgeGroup(-1));
  assert.deepEqual(groupByAge([{ name: "A", age: 5 }, { name: "B", age: 6 }]), { crianças: ["A", "B"] });
  assert.deepEqual(groupByAge([]), {});
});

test("30 opera o carrinho", () => {
  const { ShoppingCart } = collections(30);
  const cart = new ShoppingCart();
  cart.add("Caderno", 10, 2);
  cart.add("Caderno", 10);
  cart.add("Caneta", 5);
  assert.equal(cart.total, 35);
  cart.remove("Caneta");
  assert.equal(cart.items.length, 1);
  assert.throws(() => cart.remove("Caneta"));
  assert.throws(() => cart.add("X", -1));
  assert.throws(() => cart.add("X", 1, 0));
});
