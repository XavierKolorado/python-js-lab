<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# JavaScript, nível 1: Fundamentos

*JavaScript, level 1: Fundamentals*

[Voltar ao README principal / Back to the main README](../../README.md)

- [01. Mensagem no console](01-mensagem-console.js)
- [02. Variáveis](02-variaveis.js)
- [03. Calculadora](03-calculadora.js)
- [04. Média de notas](04-media-notas.js)
- [05. Conversor de temperatura](05-conversor-temperatura.js)
- [06. Par ou ímpar](06-par-ou-impar.js)
- [07. Maior número](07-maior-numero.js)
- [08. Maioridade](08-maioridade.js)
- [09. Classificação de notas](09-classificacao-notas.js)
- [10. Calculadora de desconto](10-calculadora-desconto.js)

## 01. Mensagem no console / Console message

**Problema:** Exibir uma mensagem utilizando `console.log()`.  
**Problem:** Show a message with `console.log()`.

**Objetivo:** Executar JavaScript com Node.js.  
**Goal:** Run JavaScript with Node.js.

**Conceitos / Concepts:** `console.log`, template strings, `process.argv`

**Arquivo / File:** [`01-mensagem-console.js`](./01-mensagem-console.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/01-mensagem-console.js Ana
```

**Exemplo de execução / Example run**

```text
Olá, Ana! Boas-vindas ao Python & JavaScript Lab.
```

**Resultado esperado:** Saudação no terminal.  
**Expected result:** A greeting in the terminal.

<details><summary>Código completo / Full code: <code>01-mensagem-console.js</code></summary>

```javascript
// 01. Mensagem no console: exibe uma mensagem usando console.log().
"use strict";

function buildMessage(name = "visitante") {
  const cleanName = name.trim() || "visitante";
  return `Olá, ${cleanName}! Boas-vindas ao Python & JavaScript Lab.`;
}

function main() {
  console.log(buildMessage(process.argv[2]));
}

if (require.main === module) {
  main();
}

module.exports = { buildMessage };
```

</details>

## 02. Variáveis / Variables

**Problema:** Demonstrar o uso de `let` e `const`.  
**Problem:** Show how `let` and `const` work.

**Objetivo:** Entender reatribuição, mutação e escopo de bloco.  
**Goal:** Understand reassignment, mutation and block scope.

**Conceitos / Concepts:** `let`, `const`, escopo, `TypeError`

**Arquivo / File:** [`02-variaveis.js`](./02-variaveis.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/02-variaveis.js
```

**Exemplo de execução / Example run**

```text
let pode ser reatribuída: 15
const não pode: JavaScript: TypeError ao reatribuir uma const
const com objeto aceita mutação: { name: 'Lab', level: 1 }
escopo de bloco preserva o valor externo: fora
```

**Resultado esperado:** Quatro linhas, uma para cada comportamento.  
**Expected result:** Four lines, one per behavior.

<details><summary>Código completo / Full code: <code>02-variaveis.js</code></summary>

```javascript
// 02. Variáveis: demonstra a diferença entre let e const.
"use strict";

function demonstrateLet() {
  let score = 10;
  score += 5;
  return score;
}

function demonstrateConstReassignment() {
  const language = "JavaScript";
  try {
    const fixedValue = 1;
    fixedValue = 2;
  } catch (error) {
    return `${language}: ${error.name} ao reatribuir uma const`;
  }
  return language;
}

function demonstrateConstObject() {
  const profile = { name: "Lab" };
  profile.level = 1;
  return profile;
}

function demonstrateBlockScope() {
  const insideValue = "fora";
  {
    const insideValue = "dentro";
    if (insideValue !== "dentro") {
      throw new Error("Escopo de bloco inesperado.");
    }
  }
  return insideValue;
}

function main() {
  console.log("let pode ser reatribuída:", demonstrateLet());
  console.log("const não pode:", demonstrateConstReassignment());
  console.log("const com objeto aceita mutação:", demonstrateConstObject());
  console.log("escopo de bloco preserva o valor externo:", demonstrateBlockScope());
}

if (require.main === module) {
  main();
}

module.exports = {
  demonstrateLet,
  demonstrateConstReassignment,
  demonstrateConstObject,
  demonstrateBlockScope,
};
```

</details>

## 03. Calculadora / Calculator

**Problema:** Implementar uma calculadora simples.  
**Problem:** Build a simple calculator.

**Objetivo:** Mapear operadores para funções.  
**Goal:** Map operators to functions.

**Conceitos / Concepts:** objetos, arrow functions, `process.exitCode`

**Arquivo / File:** [`03-calculadora.js`](./03-calculadora.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/03-calculadora.js 10 + 5
```

**Exemplo de execução / Example run**

```text
10 + 5 = 15
```

**Resultado esperado:** O resultado da conta. Divisão por zero gera erro. No Git Bash, prefira `*` e `/` entre aspas e `MSYS_NO_PATHCONV=1`.  
**Expected result:** The result. Division by zero is an error. On Git Bash, quote `*` and `/` and set `MSYS_NO_PATHCONV=1`.

<details><summary>Código completo / Full code: <code>03-calculadora.js</code></summary>

```javascript
// 03. Calculadora: uso `node 03-calculadora.js 10 + 5`. No shell, escreva "*" entre aspas.
"use strict";

const OPERATIONS = {
  "+": (first, second) => first + second,
  "-": (first, second) => first - second,
  "*": (first, second) => first * second,
  "/": (first, second) => {
    if (second === 0) {
      throw new Error("Não é possível dividir por zero.");
    }
    return first / second;
  },
};

function parseNumber(rawValue) {
  const number = Number(String(rawValue).replace(",", "."));
  if (rawValue === undefined || String(rawValue).trim() === "" || !Number.isFinite(number)) {
    throw new Error(`Número inválido: ${rawValue}`);
  }
  return number;
}

function calculate(first, symbol, second) {
  const operation = OPERATIONS[symbol];
  if (!operation) {
    throw new Error(`Operação inválida: ${symbol}`);
  }
  return operation(first, second);
}

function main() {
  const [rawFirst, symbol, rawSecond] = process.argv.slice(2);
  try {
    const first = parseNumber(rawFirst);
    const second = parseNumber(rawSecond);
    console.log(`${first} ${symbol} ${second} = ${calculate(first, symbol, second)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { calculate, parseNumber };
```

</details>

## 04. Média de notas / Grade average

**Problema:** Receber três notas e calcular a média.  
**Problem:** Read three grades and compute the average.

**Objetivo:** Usar `map` e `reduce` com validação.  
**Goal:** Use `map` and `reduce` with validation.

**Conceitos / Concepts:** `reduce`, `Number.isFinite`, `toFixed`

**Arquivo / File:** [`04-media-notas.js`](./04-media-notas.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/04-media-notas.js 7 8.5 9
```

**Exemplo de execução / Example run**

```text
Média: 8.17
```

**Resultado esperado:** A média com duas casas decimais.  
**Expected result:** The average with two decimal places.

<details><summary>Código completo / Full code: <code>04-media-notas.js</code></summary>

```javascript
// 04. Média de notas: uso `node 04-media-notas.js 7 8.5 9`.
"use strict";

const GRADE_COUNT = 3;
const MAX_GRADE = 10;

function parseGrade(rawGrade) {
  const grade = Number(String(rawGrade).replace(",", "."));
  if (String(rawGrade).trim() === "" || !Number.isFinite(grade) || grade < 0 || grade > MAX_GRADE) {
    throw new Error(`Nota inválida: ${rawGrade}. Use valores de 0 a ${MAX_GRADE}.`);
  }
  return grade;
}

function calculateAverage(grades) {
  if (grades.length === 0) {
    throw new Error("Informe ao menos uma nota.");
  }
  return grades.reduce((total, grade) => total + grade, 0) / grades.length;
}

function main() {
  const rawGrades = process.argv.slice(2);
  try {
    if (rawGrades.length !== GRADE_COUNT) {
      throw new Error(`Informe exatamente ${GRADE_COUNT} notas.`);
    }
    console.log(`Média: ${calculateAverage(rawGrades.map(parseGrade)).toFixed(2)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { parseGrade, calculateAverage };
```

</details>

## 05. Conversor de temperatura / Temperature converter

**Problema:** Converter Celsius para Fahrenheit.  
**Problem:** Convert Celsius to Fahrenheit.

**Objetivo:** Escrever funções puras.  
**Goal:** Write pure functions.

**Conceitos / Concepts:** funções, `toFixed`, `??`

**Arquivo / File:** [`05-conversor-temperatura.js`](./05-conversor-temperatura.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/05-conversor-temperatura.js 25
```

**Exemplo de execução / Example run**

```text
25 °C = 77.0 °F
```

**Resultado esperado:** A temperatura em °F.  
**Expected result:** The temperature in °F.

<details><summary>Código completo / Full code: <code>05-conversor-temperatura.js</code></summary>

```javascript
// 05. Conversor de temperatura: uso `node 05-conversor-temperatura.js 25`.
"use strict";

const ABSOLUTE_ZERO_CELSIUS = -273.15;

function celsiusToFahrenheit(celsius) {
  if (!Number.isFinite(celsius)) {
    throw new Error("Informe uma temperatura numérica.");
  }
  if (celsius < ABSOLUTE_ZERO_CELSIUS) {
    throw new Error("A temperatura está abaixo do zero absoluto.");
  }
  return (celsius * 9) / 5 + 32;
}

function main() {
  const celsius = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`${celsius} °C = ${celsiusToFahrenheit(celsius).toFixed(1)} °F`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { celsiusToFahrenheit };
```

</details>

## 06. Par ou ímpar / Even or odd

**Problema:** Verificar se um número é par ou ímpar.  
**Problem:** Check whether a number is even or odd.

**Objetivo:** Usar o operador ternário.  
**Goal:** Use the ternary operator.

**Conceitos / Concepts:** `%`, ternário, `Number.isInteger`

**Arquivo / File:** [`06-par-ou-impar.js`](./06-par-ou-impar.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/06-par-ou-impar.js 7
```

**Exemplo de execução / Example run**

```text
7 é ímpar.
```

**Resultado esperado:** Uma frase com a paridade.  
**Expected result:** A sentence with the parity.

<details><summary>Código completo / Full code: <code>06-par-ou-impar.js</code></summary>

```javascript
// 06. Par ou ímpar: uso `node 06-par-ou-impar.js 7`.
"use strict";

function getParity(number) {
  if (!Number.isInteger(number)) {
    throw new Error("Informe um número inteiro.");
  }
  return number % 2 === 0 ? "par" : "ímpar";
}

function main() {
  const number = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`${number} é ${getParity(number)}.`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { getParity };
```

</details>

## 07. Maior número / Largest number

**Problema:** Encontrar o maior entre três números.  
**Problem:** Find the largest of three numbers.

**Objetivo:** Comparar valores com `if`.  
**Goal:** Compare values with `if`.

**Conceitos / Concepts:** `if`, desestruturação, `every`

**Arquivo / File:** [`07-maior-numero.js`](./07-maior-numero.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/07-maior-numero.js 4 19 7
```

**Exemplo de execução / Example run**

```text
Maior número: 19
```

**Resultado esperado:** O maior número.  
**Expected result:** The largest number.

<details><summary>Código completo / Full code: <code>07-maior-numero.js</code></summary>

```javascript
// 07. Maior número: uso `node 07-maior-numero.js 4 19 7`.
"use strict";

function largestOfThree(first, second, third) {
  const numbers = [first, second, third];
  if (!numbers.every(Number.isFinite)) {
    throw new Error("Informe três números válidos.");
  }
  let largest = first;
  if (second > largest) {
    largest = second;
  }
  if (third > largest) {
    largest = third;
  }
  return largest;
}

function main() {
  const [first, second, third] = process.argv.slice(2).map(Number);
  try {
    console.log(`Maior número: ${largestOfThree(first, second, third)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { largestOfThree };
```

</details>

## 08. Maioridade / Legal age

**Problema:** Verificar se uma pessoa é maior de idade.  
**Problem:** Check whether a person is an adult.

**Objetivo:** Validar antes de decidir.  
**Goal:** Validate before deciding.

**Conceitos / Concepts:** constantes, booleanos, exceções

**Arquivo / File:** [`08-maioridade.js`](./08-maioridade.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/08-maioridade.js 20
```

**Exemplo de execução / Example run**

```text
Maior de idade.
```

**Resultado esperado:** Maior ou menor de idade.  
**Expected result:** Adult or minor.

<details><summary>Código completo / Full code: <code>08-maioridade.js</code></summary>

```javascript
// 08. Maioridade: uso `node 08-maioridade.js 20`.
"use strict";

const LEGAL_AGE = 18;
const MAX_AGE = 130;

function isAdult(age) {
  if (!Number.isInteger(age) || age < 0 || age > MAX_AGE) {
    throw new Error(`Idade inválida. Use um inteiro de 0 a ${MAX_AGE}.`);
  }
  return age >= LEGAL_AGE;
}

function main() {
  const age = Number(process.argv[2] ?? "NaN");
  try {
    console.log(isAdult(age) ? "Maior de idade." : "Menor de idade.");
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { isAdult };
```

</details>

## 09. Classificação de notas / Grade classification

**Problema:** Classificar notas em categorias de desempenho.  
**Problem:** Sort grades into performance categories.

**Objetivo:** Trocar `if` em cadeia por uma tabela de dados.  
**Goal:** Replace an `if` chain with a data table.

**Conceitos / Concepts:** `find`, desestruturação, arrays de objetos

**Arquivo / File:** [`09-classificacao-notas.js`](./09-classificacao-notas.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/09-classificacao-notas.js 8.5
```

**Exemplo de execução / Example run**

```text
Nota 8.5: Bom
```

**Resultado esperado:** A categoria da nota.  
**Expected result:** The grade's category.

<details><summary>Código completo / Full code: <code>09-classificacao-notas.js</code></summary>

```javascript
// 09. Classificação de notas: uso `node 09-classificacao-notas.js 8.5`.
"use strict";

const CATEGORIES = [
  { minimum: 9, label: "Excelente" },
  { minimum: 7, label: "Bom" },
  { minimum: 5, label: "Regular" },
  { minimum: 0, label: "Insuficiente" },
];

function classifyGrade(grade) {
  if (!Number.isFinite(grade) || grade < 0 || grade > 10) {
    throw new Error("A nota deve estar entre 0 e 10.");
  }
  return CATEGORIES.find(({ minimum }) => grade >= minimum).label;
}

function main() {
  const grade = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`Nota ${grade}: ${classifyGrade(grade)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { classifyGrade };
```

</details>

## 10. Calculadora de desconto / Discount calculator

**Problema:** Calcular o preço final de um produto após aplicar desconto.  
**Problem:** Compute a product's final price after a discount.

**Objetivo:** Formatar moeda com `Intl`.  
**Goal:** Format currency with `Intl`.

**Conceitos / Concepts:** `Intl.NumberFormat`, objetos

**Arquivo / File:** [`10-calculadora-desconto.js`](./10-calculadora-desconto.js)

**Como executar / How to run**

```bash
node javascript/fundamentos/10-calculadora-desconto.js 200 15
```

**Exemplo de execução / Example run**

```text
Desconto: R$ 30,00
Preço final: R$ 170,00
```

**Resultado esperado:** O desconto e o preço final em reais.  
**Expected result:** The discount and the final price in reais.

<details><summary>Código completo / Full code: <code>10-calculadora-desconto.js</code></summary>

```javascript
// 10. Calculadora de desconto: uso `node 10-calculadora-desconto.js 200 15`.
"use strict";

function calculateDiscount(price, percentage) {
  if (!Number.isFinite(price) || price < 0) {
    throw new Error("O preço precisa ser um número positivo.");
  }
  if (!Number.isFinite(percentage) || percentage < 0 || percentage > 100) {
    throw new Error("O desconto deve estar entre 0 e 100.");
  }
  const discount = (price * percentage) / 100;
  return { discount, finalPrice: price - discount };
}

function formatCurrency(value) {
  return new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(value);
}

function main() {
  const [price, percentage] = process.argv.slice(2).map(Number);
  try {
    const { discount, finalPrice } = calculateDiscount(price, percentage);
    console.log(`Desconto: ${formatCurrency(discount)}`);
    console.log(`Preço final: ${formatCurrency(finalPrice)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { calculateDiscount, formatCurrency };
```

</details>
