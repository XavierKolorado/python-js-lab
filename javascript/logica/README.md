<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# JavaScript, nível 2: Condições, loops e funções

*JavaScript, level 2: Conditions, loops and functions*

[Voltar ao README principal / Back to the main README](../../README.md)

- [11. Tabuada](11-tabuada.js)
- [12. Soma até N](12-soma-ate-n.js)
- [13. Fatorial](13-fatorial.js)
- [14. Jogo de adivinhação](14-jogo-adivinhacao.js)
- [15. Palíndromo](15-palindromo.js)
- [16. Contador de vogais](16-contador-vogais.js)
- [17. Números primos](17-numeros-primos.js)
- [18. Maior valor de array](18-maior-valor-array.js)
- [19. Inversor de strings](19-inversor-strings.js)
- [20. Contador regressivo](20-contador-regressivo.js)

## 11. Tabuada / Multiplication table

**Problema:** Exibir a tabuada de um número.  
**Problem:** Show a number's multiplication table.

**Objetivo:** Usar o laço `for`.  
**Goal:** Use the `for` loop.

**Conceitos / Concepts:** `for`, `padStart`, `join`

**Arquivo / File:** [`11-tabuada.js`](./11-tabuada.js)

**Como executar / How to run**

```bash
node javascript/logica/11-tabuada.js 7
```

**Exemplo de execução / Example run**

```text
7 x  1 = 7
7 x  2 = 14
7 x  3 = 21
7 x  4 = 28
7 x  5 = 35
7 x  6 = 42
7 x  7 = 49
7 x  8 = 56
7 x  9 = 63
7 x 10 = 70
```

**Resultado esperado:** Dez linhas de multiplicação.  
**Expected result:** Ten multiplication lines.

<details><summary>Código completo / Full code: <code>11-tabuada.js</code></summary>

```javascript
// 11. Tabuada: uso `node 11-tabuada.js 7`.
"use strict";

function buildMultiplicationTable(number, lastFactor = 10) {
  if (!Number.isInteger(number)) {
    throw new Error("Informe um número inteiro.");
  }
  const lines = [];
  for (let factor = 1; factor <= lastFactor; factor += 1) {
    lines.push(`${number} x ${String(factor).padStart(2)} = ${number * factor}`);
  }
  return lines;
}

function main() {
  try {
    console.log(buildMultiplicationTable(Number(process.argv[2] ?? "NaN")).join("\n"));
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { buildMultiplicationTable };
```

</details>

## 12. Soma até N / Sum up to N

**Problema:** Somar números de 1 até um limite.  
**Problem:** Add numbers from 1 to a limit.

**Objetivo:** Usar um acumulador.  
**Goal:** Use an accumulator.

**Conceitos / Concepts:** `for`, validação

**Arquivo / File:** [`12-soma-ate-n.js`](./12-soma-ate-n.js)

**Como executar / How to run**

```bash
node javascript/logica/12-soma-ate-n.js 100
```

**Exemplo de execução / Example run**

```text
A soma de 1 até 100 é 5050.
```

**Resultado esperado:** A soma de 1 até o limite.  
**Expected result:** The sum from 1 to the limit.

<details><summary>Código completo / Full code: <code>12-soma-ate-n.js</code></summary>

```javascript
// 12. Soma até N: uso `node 12-soma-ate-n.js 100`.
"use strict";

function sumUpTo(limit) {
  if (!Number.isInteger(limit) || limit < 1) {
    throw new Error("O limite precisa ser um inteiro maior ou igual a 1.");
  }
  let total = 0;
  for (let number = 1; number <= limit; number += 1) {
    total += number;
  }
  return total;
}

function main() {
  const limit = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`A soma de 1 até ${limit} é ${sumUpTo(limit)}.`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { sumUpTo };
```

</details>

## 13. Fatorial / Factorial

**Problema:** Calcular o fatorial de um número.  
**Problem:** Compute a number's factorial.

**Objetivo:** Usar `BigInt` para não perder precisão.  
**Goal:** Use `BigInt` to keep precision.

**Conceitos / Concepts:** `BigInt`, `for`

**Arquivo / File:** [`13-fatorial.js`](./13-fatorial.js)

**Como executar / How to run**

```bash
node javascript/logica/13-fatorial.js 25
```

**Exemplo de execução / Example run**

```text
25! = 15511210043330985984000000
```

**Resultado esperado:** O valor exato de n!.  
**Expected result:** The exact value of n!.

<details><summary>Código completo / Full code: <code>13-fatorial.js</code></summary>

```javascript
// 13. Fatorial: uso `node 13-fatorial.js 25`. BigInt mantém a precisão em valores grandes.
"use strict";

function factorial(number) {
  if (!Number.isInteger(number) || number < 0) {
    throw new Error("Informe um inteiro maior ou igual a zero.");
  }
  let result = 1n;
  for (let factor = 2n; factor <= BigInt(number); factor += 1n) {
    result *= factor;
  }
  return result;
}

function main() {
  const number = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`${number}! = ${factorial(number)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { factorial };
```

</details>

## 14. Jogo de adivinhação / Guessing game

**Problema:** Criar um jogo utilizando números aleatórios.  
**Problem:** Build a game with random numbers.

**Objetivo:** Ler linhas de forma assíncrona.  
**Goal:** Read lines asynchronously.

**Conceitos / Concepts:** `Math.random`, `readline`, `for await`

**Arquivo / File:** [`14-jogo-adivinhacao.js`](./14-jogo-adivinhacao.js)

**Como executar / How to run**

```bash
node javascript/logica/14-jogo-adivinhacao.js 3
```

**Entradas do exemplo / Example input:** `1` · `2` · `3`

**Exemplo de execução / Example run**

```text
Adivinhe o número de 1 a 3:
O número secreto é maior.
O número secreto é maior.
Parabéns! Você acertou em 3 tentativa(s).
```

**Resultado esperado:** Dicas até o acerto. O número sorteado muda a cada execução.  
**Expected result:** Hints until the hit. The drawn number changes on every run.

<details><summary>Código completo / Full code: <code>14-jogo-adivinhacao.js</code></summary>

```javascript
// 14. Jogo de adivinhação: uso `node 14-jogo-adivinhacao.js [maior-numero]`.
"use strict";

const readline = require("node:readline");

const DEFAULT_HIGHEST = 100;

function drawSecret(highest, random = Math.random) {
  return Math.floor(random() * highest) + 1;
}

function evaluateGuess(guess, secret) {
  if (guess < secret) {
    return "O número secreto é maior.";
  }
  if (guess > secret) {
    return "O número secreto é menor.";
  }
  return null;
}

async function play(highest) {
  const secret = drawSecret(highest);
  const lines = readline.createInterface({ input: process.stdin });
  let attempts = 0;
  console.log(`Adivinhe o número de 1 a ${highest}:`);
  for await (const line of lines) {
    const guess = Number(line.trim());
    if (line.trim() === "" || !Number.isInteger(guess) || guess < 1 || guess > highest) {
      console.log(`Digite um inteiro de 1 a ${highest}.`);
      continue;
    }
    attempts += 1;
    const hint = evaluateGuess(guess, secret);
    if (hint === null) {
      console.log(`Parabéns! Você acertou em ${attempts} tentativa(s).`);
      lines.close();
      return;
    }
    console.log(hint);
  }
  console.log(`Jogo encerrado. O número era ${secret}.`);
}

function main() {
  const highest = Number(process.argv[2] ?? DEFAULT_HIGHEST);
  if (!Number.isInteger(highest) || highest < 2) {
    console.error("Erro: o maior número precisa ser um inteiro maior que 1.");
    process.exitCode = 1;
    return;
  }
  play(highest);
}

if (require.main === module) {
  main();
}

module.exports = { drawSecret, evaluateGuess };
```

</details>

## 15. Palíndromo / Palindrome

**Problema:** Verificar se uma palavra é um palíndromo.  
**Problem:** Check whether a word is a palindrome.

**Objetivo:** Normalizar Unicode com regex.  
**Goal:** Normalize Unicode with regex.

**Conceitos / Concepts:** `normalize`, regex Unicode, espalhamento

**Arquivo / File:** [`15-palindromo.js`](./15-palindromo.js)

**Como executar / How to run**

```bash
node javascript/logica/15-palindromo.js 'Ame a ema'
```

**Exemplo de execução / Example run**

```text
"Ame a ema" é um palíndromo.
```

**Resultado esperado:** Informa se o texto é um palíndromo.  
**Expected result:** Says whether the text is a palindrome.

<details><summary>Código completo / Full code: <code>15-palindromo.js</code></summary>

```javascript
// 15. Palíndromo: uso `node 15-palindromo.js "Ame a ema"`.
"use strict";

function normalizeText(text) {
  return text
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]/gu, "");
}

function isPalindrome(text) {
  const normalized = normalizeText(text);
  if (normalized === "") {
    throw new Error("Informe ao menos uma letra ou número.");
  }
  return normalized === [...normalized].reverse().join("");
}

function main() {
  const text = process.argv[2] ?? "";
  try {
    console.log(`"${text}" ${isPalindrome(text) ? "é" : "não é"} um palíndromo.`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { isPalindrome };
```

</details>

## 16. Contador de vogais / Vowel counter

**Problema:** Contar vogais em uma frase.  
**Problem:** Count vowels in a sentence.

**Objetivo:** Percorrer strings com `for...of`.  
**Goal:** Walk strings with `for...of`.

**Conceitos / Concepts:** `for...of`, `Object.fromEntries`, `normalize`

**Arquivo / File:** [`16-contador-vogais.js`](./16-contador-vogais.js)

**Como executar / How to run**

```bash
node javascript/logica/16-contador-vogais.js 'Programação é prática'
```

**Exemplo de execução / Example run**

```text
Total de vogais: 9
{ a: 5, e: 1, i: 1, o: 2, u: 0 }
```

**Resultado esperado:** O total e a contagem por vogal.  
**Expected result:** The total and a count per vowel.

<details><summary>Código completo / Full code: <code>16-contador-vogais.js</code></summary>

```javascript
// 16. Contador de vogais: uso `node 16-contador-vogais.js "Programação é prática"`.
"use strict";

const VOWELS = "aeiou";

function countVowels(text) {
  const decomposed = text.normalize("NFD").toLowerCase();
  const counts = Object.fromEntries([...VOWELS].map((vowel) => [vowel, 0]));
  for (const character of decomposed) {
    if (character in counts) {
      counts[character] += 1;
    }
  }
  return counts;
}

function main() {
  const counts = countVowels(process.argv[2] ?? "");
  const total = Object.values(counts).reduce((sum, amount) => sum + amount, 0);
  console.log(`Total de vogais: ${total}`);
  console.log(counts);
}

if (require.main === module) {
  main();
}

module.exports = { countVowels };
```

</details>

## 17. Números primos / Prime numbers

**Problema:** Criar uma função que verifica se um número é primo.  
**Problem:** Write a function that checks for primes.

**Objetivo:** Limitar a busca por divisores.  
**Goal:** Limit the divisor search.

**Conceitos / Concepts:** `for`, `%`, casos de borda

**Arquivo / File:** [`17-numeros-primos.js`](./17-numeros-primos.js)

**Como executar / How to run**

```bash
node javascript/logica/17-numeros-primos.js 97
```

**Exemplo de execução / Example run**

```text
97 é primo.
```

**Resultado esperado:** Informa se o número é primo.  
**Expected result:** Says whether the number is prime.

<details><summary>Código completo / Full code: <code>17-numeros-primos.js</code></summary>

```javascript
// 17. Números primos: uso `node 17-numeros-primos.js 97`.
"use strict";

function isPrime(number) {
  if (!Number.isInteger(number)) {
    throw new Error("Informe um número inteiro.");
  }
  if (number < 2) {
    return false;
  }
  if (number % 2 === 0) {
    return number === 2;
  }
  for (let divisor = 3; divisor * divisor <= number; divisor += 2) {
    if (number % divisor === 0) {
      return false;
    }
  }
  return true;
}

function main() {
  const number = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`${number} ${isPrime(number) ? "é" : "não é"} primo.`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { isPrime };
```

</details>

## 18. Maior valor de array / Largest array value

**Problema:** Encontrar o maior número de um array.  
**Problem:** Find an array's largest number.

**Objetivo:** Percorrer arrays e tratar o caso vazio.  
**Goal:** Walk arrays and handle the empty case.

**Conceitos / Concepts:** `for...of`, `every`, exceções

**Arquivo / File:** [`18-maior-valor-array.js`](./18-maior-valor-array.js)

**Como executar / How to run**

```bash
node javascript/logica/18-maior-valor-array.js 3 9 2
```

**Exemplo de execução / Example run**

```text
Maior valor: 9
```

**Resultado esperado:** O maior valor. Array vazio gera erro.  
**Expected result:** The largest value. An empty array is an error.

<details><summary>Código completo / Full code: <code>18-maior-valor-array.js</code></summary>

```javascript
// 18. Maior valor de array: uso `node 18-maior-valor-array.js 3 9 2`.
"use strict";

function findLargest(numbers) {
  if (numbers.length === 0) {
    throw new Error("O array está vazio.");
  }
  if (!numbers.every(Number.isFinite)) {
    throw new Error("O array contém valores que não são números.");
  }
  let largest = numbers[0];
  for (const number of numbers) {
    if (number > largest) {
      largest = number;
    }
  }
  return largest;
}

function main() {
  try {
    console.log(`Maior valor: ${findLargest(process.argv.slice(2).map(Number))}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { findLargest };
```

</details>

## 19. Inversor de strings / String reverser

**Problema:** Criar uma função que inverte uma string.  
**Problem:** Write a function that reverses a string.

**Objetivo:** Percorrer caracteres completos, inclusive emojis.  
**Goal:** Walk whole characters, including emojis.

**Conceitos / Concepts:** espalhamento, `reverse`, `join`

**Arquivo / File:** [`19-inversor-strings.js`](./19-inversor-strings.js)

**Como executar / How to run**

```bash
node javascript/logica/19-inversor-strings.js 'Olá, mundo'
```

**Exemplo de execução / Example run**

```text
odnum ,álO
```

**Resultado esperado:** O texto de trás para frente.  
**Expected result:** The text backwards.

<details><summary>Código completo / Full code: <code>19-inversor-strings.js</code></summary>

```javascript
// 19. Inversor de strings: uso `node 19-inversor-strings.js "Olá, mundo"`.
"use strict";

function reverseString(text) {
  // O espalhamento percorre caracteres completos, preservando emojis.
  return [...text].reverse().join("");
}

function main() {
  console.log(reverseString(process.argv[2] ?? ""));
}

if (require.main === module) {
  main();
}

module.exports = { reverseString };
```

</details>

## 20. Contador regressivo / Countdown

**Problema:** Criar um contador regressivo.  
**Problem:** Build a countdown.

**Objetivo:** Usar temporizadores e callbacks.  
**Goal:** Use timers and callbacks.

**Conceitos / Concepts:** `setInterval`, `clearInterval`, callbacks

**Arquivo / File:** [`20-contador-regressivo.js`](./20-contador-regressivo.js)

**Como executar / How to run**

```bash
node javascript/logica/20-contador-regressivo.js 3
```

**Exemplo de execução / Example run**

```text
3
2
1
0
Tempo esgotado!
```

**Resultado esperado:** Um número por segundo até zero e o aviso final.  
**Expected result:** One number per second down to zero and a final notice.

<details><summary>Código completo / Full code: <code>20-contador-regressivo.js</code></summary>

```javascript
// 20. Contador regressivo: uso `node 20-contador-regressivo.js 5`.
"use strict";

const TICK_MILLISECONDS = 1000;

function buildCountdown(start) {
  if (!Number.isInteger(start) || start < 0) {
    throw new Error("Informe um inteiro maior ou igual a zero.");
  }
  return Array.from({ length: start + 1 }, (_, index) => start - index);
}

function runCountdown(start, onTick, onFinish, delay = TICK_MILLISECONDS) {
  const remaining = buildCountdown(start);
  const timer = setInterval(() => {
    onTick(remaining.shift());
    if (remaining.length === 0) {
      clearInterval(timer);
      onFinish();
    }
  }, delay);
}

function main() {
  try {
    runCountdown(
      Number(process.argv[2] ?? "NaN"),
      (seconds) => console.log(seconds),
      () => console.log("Tempo esgotado!"),
    );
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { buildCountdown, runCountdown };
```

</details>
