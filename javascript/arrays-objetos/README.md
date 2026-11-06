<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# JavaScript, nível 3: Arrays e objetos

*JavaScript, level 3: Arrays and objects*

[Voltar ao README principal / Back to the main README](../../README.md)

- [21. Maior e menor](21-maior-menor.js)
- [22. Remover duplicados](22-remover-duplicados.js)
- [23. Filtro de pares](23-filtro-pares.js)
- [24. Transformação de arrays](24-transformacao-arrays.js)
- [25. Soma com reduce](25-soma-reduce.js)
- [26. Ordenação de produtos](26-ordenacao-produtos.js)
- [27. Catálogo de produtos](27-catalogo-produtos.js)
- [28. Busca de usuários](28-busca-usuarios.js)
- [29. Agrupamento por idade](29-agrupamento-idade.js)
- [30. Carrinho de compras](30-carrinho-compras.js)

## 21. Maior e menor / Largest and smallest

**Problema:** Encontrar o maior e o menor valor de um array.  
**Problem:** Find an array's largest and smallest values.

**Objetivo:** Acumular dois valores com `reduce`.  
**Goal:** Accumulate two values with `reduce`.

**Conceitos / Concepts:** `reduce`, `Math.min`, `Math.max`

**Arquivo / File:** [`21-maior-menor.js`](./21-maior-menor.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/21-maior-menor.js 8 3 15
```

**Exemplo de execução / Example run**

```text
Menor: 3
Maior: 15
```

**Resultado esperado:** O menor e o maior valor.  
**Expected result:** The smallest and largest values.

<details><summary>Código completo / Full code: <code>21-maior-menor.js</code></summary>

```javascript
// 21. Maior e menor: uso `node 21-maior-menor.js 8 3 15`.
"use strict";

function findMinMax(numbers) {
  if (numbers.length === 0) {
    throw new Error("O array está vazio.");
  }
  if (!numbers.every(Number.isFinite)) {
    throw new Error("O array contém valores que não são números.");
  }
  return numbers.reduce(
    ({ smallest, largest }, number) => ({
      smallest: Math.min(smallest, number),
      largest: Math.max(largest, number),
    }),
    { smallest: numbers[0], largest: numbers[0] },
  );
}

function main() {
  try {
    const { smallest, largest } = findMinMax(process.argv.slice(2).map(Number));
    console.log(`Menor: ${smallest}`);
    console.log(`Maior: ${largest}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { findMinMax };
```

</details>

## 22. Remover duplicados / Remove duplicates

**Problema:** Remover valores repetidos de um array.  
**Problem:** Remove repeated values from an array.

**Objetivo:** Conhecer a estrutura `Set`.  
**Goal:** Learn the `Set` structure.

**Conceitos / Concepts:** `Set`, espalhamento

**Arquivo / File:** [`22-remover-duplicados.js`](./22-remover-duplicados.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/22-remover-duplicados.js a b a c b
```

**Exemplo de execução / Example run**

```text
[ 'a', 'b', 'c' ]
```

**Resultado esperado:** O array sem repetições.  
**Expected result:** The array without repeats.

<details><summary>Código completo / Full code: <code>22-remover-duplicados.js</code></summary>

```javascript
// 22. Remover duplicados: uso `node 22-remover-duplicados.js a b a c b`.
"use strict";

function removeDuplicates(items) {
  return [...new Set(items)];
}

function main() {
  const items = process.argv.slice(2);
  console.log(removeDuplicates(items));
}

if (require.main === module) {
  main();
}

module.exports = { removeDuplicates };
```

</details>

## 23. Filtro de pares / Even filter

**Problema:** Filtrar números pares utilizando `filter()`.  
**Problem:** Filter even numbers with `filter()`.

**Objetivo:** Criar arrays com um predicado.  
**Goal:** Build arrays with a predicate.

**Conceitos / Concepts:** `filter`, arrow functions

**Arquivo / File:** [`23-filtro-pares.js`](./23-filtro-pares.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/23-filtro-pares.js 1 2 3 4 5 6
```

**Exemplo de execução / Example run**

```text
Pares: [ 2, 4, 6 ]
```

**Resultado esperado:** Somente os números pares.  
**Expected result:** Only the even numbers.

<details><summary>Código completo / Full code: <code>23-filtro-pares.js</code></summary>

```javascript
// 23. Filtro de pares: uso `node 23-filtro-pares.js 1 2 3 4`.
"use strict";

const DEFAULT_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function filterEven(numbers) {
  return numbers.filter((number) => number % 2 === 0);
}

function main() {
  const args = process.argv.slice(2).map(Number);
  const numbers = args.length > 0 ? args : DEFAULT_NUMBERS;
  if (!numbers.every(Number.isInteger)) {
    console.error("Erro: informe apenas números inteiros.");
    process.exitCode = 1;
    return;
  }
  console.log("Pares:", filterEven(numbers));
}

if (require.main === module) {
  main();
}

module.exports = { filterEven };
```

</details>

## 24. Transformação de arrays / Array transformation

**Problema:** Transformar valores utilizando `map()`.  
**Problem:** Transform values with `map()`.

**Objetivo:** Gerar novos arrays sem alterar o original.  
**Goal:** Create new arrays without changing the original.

**Conceitos / Concepts:** `map`, espalhamento de objetos

**Arquivo / File:** [`24-transformacao-arrays.js`](./24-transformacao-arrays.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/24-transformacao-arrays.js
```

**Exemplo de execução / Example run**

```text
Dobro: [ 2, 4, 6 ]
Com 10% de aumento: [ 'Teclado: R$ 165.00', 'Mouse: R$ 88.00', 'Monitor: R$ 990.00' ]
```

**Resultado esperado:** Valores dobrados e preços com aumento.  
**Expected result:** Doubled values and increased prices.

<details><summary>Código completo / Full code: <code>24-transformacao-arrays.js</code></summary>

```javascript
// 24. Transformação de arrays: aplica map() para criar novos arrays.
"use strict";

const PRODUCTS = [
  { name: "Teclado", price: 150 },
  { name: "Mouse", price: 80 },
  { name: "Monitor", price: 900 },
];

function doubleValues(numbers) {
  return numbers.map((number) => number * 2);
}

function applyIncrease(products, percentage) {
  const factor = 1 + percentage / 100;
  return products.map((product) => ({ ...product, price: product.price * factor }));
}

function toLabels(products) {
  return products.map(({ name, price }) => `${name}: R$ ${price.toFixed(2)}`);
}

function main() {
  console.log("Dobro:", doubleValues([1, 2, 3]));
  console.log("Com 10% de aumento:", toLabels(applyIncrease(PRODUCTS, 10)));
}

if (require.main === module) {
  main();
}

module.exports = { doubleValues, applyIncrease, toLabels };
```

</details>

## 25. Soma com reduce / Sum with reduce

**Problema:** Somar valores utilizando `reduce()`.  
**Problem:** Add values with `reduce()`.

**Objetivo:** Entender acumulador e valor inicial.  
**Goal:** Understand the accumulator and initial value.

**Conceitos / Concepts:** `reduce`

**Arquivo / File:** [`25-soma-reduce.js`](./25-soma-reduce.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/25-soma-reduce.js 10 20 30
```

**Exemplo de execução / Example run**

```text
Soma: 60
```

**Resultado esperado:** A soma dos valores.  
**Expected result:** The sum of the values.

<details><summary>Código completo / Full code: <code>25-soma-reduce.js</code></summary>

```javascript
// 25. Soma com reduce: uso `node 25-soma-reduce.js 10 20 30`.
"use strict";

function sumValues(numbers) {
  return numbers.reduce((total, number) => total + number, 0);
}

function main() {
  const numbers = process.argv.slice(2).map(Number);
  if (!numbers.every(Number.isFinite)) {
    console.error("Erro: informe apenas números.");
    process.exitCode = 1;
    return;
  }
  console.log(`Soma: ${sumValues(numbers)}`);
}

if (require.main === module) {
  main();
}

module.exports = { sumValues };
```

</details>

## 26. Ordenação de produtos / Product sorting

**Problema:** Ordenar objetos por preço.  
**Problem:** Sort objects by price.

**Objetivo:** Escrever comparadores e evitar mutação.  
**Goal:** Write comparators and avoid mutation.

**Conceitos / Concepts:** `sort`, cópia de arrays

**Arquivo / File:** [`26-ordenacao-produtos.js`](./26-ordenacao-produtos.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/26-ordenacao-produtos.js desc
```

**Exemplo de execução / Example run**

```text
Monitor: R$ 900.00
Headset: R$ 220.00
Teclado: R$ 150.00
Mouse: R$ 80.00
```

**Resultado esperado:** Produtos em ordem de preço.  
**Expected result:** Products in price order.

<details><summary>Código completo / Full code: <code>26-ordenacao-produtos.js</code></summary>

```javascript
// 26. Ordenação de produtos: uso `node 26-ordenacao-produtos.js [asc|desc]`.
"use strict";

const PRODUCTS = [
  { name: "Monitor", price: 900 },
  { name: "Mouse", price: 80 },
  { name: "Teclado", price: 150 },
  { name: "Headset", price: 220 },
];

function sortByPrice(products, direction = "asc") {
  if (direction !== "asc" && direction !== "desc") {
    throw new Error('A direção deve ser "asc" ou "desc".');
  }
  const multiplier = direction === "asc" ? 1 : -1;
  // A cópia evita alterar o array recebido, pois sort() muda o original.
  return [...products].sort((first, second) => (first.price - second.price) * multiplier);
}

function main() {
  try {
    for (const { name, price } of sortByPrice(PRODUCTS, process.argv[2])) {
      console.log(`${name}: R$ ${price.toFixed(2)}`);
    }
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { sortByPrice };
```

</details>

## 27. Catálogo de produtos / Product catalog

**Problema:** Criar um catálogo utilizando arrays e objetos.  
**Problem:** Build a catalog with arrays and objects.

**Objetivo:** Combinar consultas sobre coleções.  
**Goal:** Combine queries over collections.

**Conceitos / Concepts:** `filter`, `find`, `Set`, `??`

**Arquivo / File:** [`27-catalogo-produtos.js`](./27-catalogo-produtos.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/27-catalogo-produtos.js móveis
```

**Exemplo de execução / Example run**

```text
Cadeira - R$ 750.00 (esgotado)
Mesa - R$ 1200.00 (6 em estoque)
```

**Resultado esperado:** Produtos da categoria, com disponibilidade.  
**Expected result:** The category's products with availability.

<details><summary>Código completo / Full code: <code>27-catalogo-produtos.js</code></summary>

```javascript
// 27. Catálogo de produtos: uso `node 27-catalogo-produtos.js [categoria]`.
"use strict";

const CATALOG = [
  { id: 1, name: "Notebook", category: "informática", price: 3500, stock: 4 },
  { id: 2, name: "Mouse", category: "informática", price: 80, stock: 30 },
  { id: 3, name: "Cadeira", category: "móveis", price: 750, stock: 0 },
  { id: 4, name: "Mesa", category: "móveis", price: 1200, stock: 6 },
];

function listCategories(catalog) {
  return [...new Set(catalog.map((product) => product.category))];
}

function filterByCategory(catalog, category) {
  return catalog.filter((product) => product.category === category);
}

function findProduct(catalog, id) {
  return catalog.find((product) => product.id === id) ?? null;
}

function formatProduct({ name, price, stock }) {
  const availability = stock > 0 ? `${stock} em estoque` : "esgotado";
  return `${name} - R$ ${price.toFixed(2)} (${availability})`;
}

function main() {
  const category = process.argv[2];
  const products = category ? filterByCategory(CATALOG, category) : CATALOG;
  if (products.length === 0) {
    console.log(`Categoria sem produtos. Opções: ${listCategories(CATALOG).join(", ")}`);
    return;
  }
  console.log(products.map(formatProduct).join("\n"));
}

if (require.main === module) {
  main();
}

module.exports = { CATALOG, listCategories, filterByCategory, findProduct, formatProduct };
```

</details>

## 28. Busca de usuários / User search

**Problema:** Criar uma lista de usuários com pesquisa por nome.  
**Problem:** Build a user list with name search.

**Objetivo:** Comparar textos sem acentos.  
**Goal:** Compare text without accents.

**Conceitos / Concepts:** `includes`, `normalize`, `filter`

**Arquivo / File:** [`28-busca-usuarios.js`](./28-busca-usuarios.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/28-busca-usuarios.js ana
```

**Exemplo de execução / Example run**

```text
Ana Souza (Recife)
Luana Melo (Manaus)
```

**Resultado esperado:** Usuários cujo nome contém o termo.  
**Expected result:** Users whose name contains the term.

<details><summary>Código completo / Full code: <code>28-busca-usuarios.js</code></summary>

```javascript
// 28. Busca de usuários: uso `node 28-busca-usuarios.js ana`.
"use strict";

const USERS = [
  { id: 1, name: "Ana Souza", city: "Recife" },
  { id: 2, name: "Bruno Lima", city: "Curitiba" },
  { id: 3, name: "Luana Melo", city: "Manaus" },
  { id: 4, name: "João Araújo", city: "Salvador" },
];

function normalize(text) {
  return text.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase().trim();
}

function searchUsers(users, term) {
  const needle = normalize(term);
  return users.filter((user) => normalize(user.name).includes(needle));
}

function main() {
  const term = process.argv[2] ?? "";
  if (term.trim() === "") {
    console.error("Erro: informe parte de um nome.");
    process.exitCode = 1;
    return;
  }
  const results = searchUsers(USERS, term);
  if (results.length === 0) {
    console.log("Nenhum usuário encontrado.");
  }
  results.forEach(({ name, city }) => console.log(`${name} (${city})`));
}

if (require.main === module) {
  main();
}

module.exports = { USERS, searchUsers };
```

</details>

## 29. Agrupamento por idade / Grouping by age

**Problema:** Agrupar pessoas por faixa etária.  
**Problem:** Group people by age range.

**Objetivo:** Construir um objeto com `reduce`.  
**Goal:** Build an object with `reduce`.

**Conceitos / Concepts:** `reduce`, `Object.entries`

**Arquivo / File:** [`29-agrupamento-idade.js`](./29-agrupamento-idade.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/29-agrupamento-idade.js
```

**Exemplo de execução / Example run**

```text
crianças: Lia
adolescentes: Davi
adultos: Marta, Caio
idosos: Rosa
```

**Resultado esperado:** Uma linha por faixa etária.  
**Expected result:** One line per age range.

<details><summary>Código completo / Full code: <code>29-agrupamento-idade.js</code></summary>

```javascript
// 29. Agrupamento por idade: separa pessoas em faixas etárias.
"use strict";

const PEOPLE = [
  { name: "Lia", age: 9 },
  { name: "Davi", age: 15 },
  { name: "Marta", age: 34 },
  { name: "Caio", age: 41 },
  { name: "Rosa", age: 72 },
];

function getAgeGroup(age) {
  if (!Number.isInteger(age) || age < 0) {
    throw new Error(`Idade inválida: ${age}`);
  }
  if (age < 12) {
    return "crianças";
  }
  if (age < 18) {
    return "adolescentes";
  }
  return age < 60 ? "adultos" : "idosos";
}

function groupByAge(people) {
  return people.reduce((groups, person) => {
    const group = getAgeGroup(person.age);
    groups[group] = [...(groups[group] ?? []), person.name];
    return groups;
  }, {});
}

function main() {
  for (const [group, names] of Object.entries(groupByAge(PEOPLE))) {
    console.log(`${group}: ${names.join(", ")}`);
  }
}

if (require.main === module) {
  main();
}

module.exports = { getAgeGroup, groupByAge };
```

</details>

## 30. Carrinho de compras / Shopping cart

**Problema:** Adicionar e remover produtos e calcular o total.  
**Problem:** Add and remove products and compute the total.

**Objetivo:** Encapsular estado em uma classe.  
**Goal:** Encapsulate state in a class.

**Conceitos / Concepts:** classes, campos privados, `Map`, getters

**Arquivo / File:** [`30-carrinho-compras.js`](./30-carrinho-compras.js)

**Como executar / How to run**

```bash
node javascript/arrays-objetos/30-carrinho-compras.js
```

**Exemplo de execução / Example run**

```text
2x Caderno - R$ 51.80
1x Mochila - R$ 129.90
Total: R$ 181.70
```

**Resultado esperado:** Itens do carrinho e o total.  
**Expected result:** The cart items and the total.

<details><summary>Código completo / Full code: <code>30-carrinho-compras.js</code></summary>

```javascript
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
```

</details>
