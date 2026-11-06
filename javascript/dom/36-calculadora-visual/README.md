<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 36. Calculadora visual / Visual calculator

**Problema:** Criar uma calculadora funcional com interface gráfica.  
**Problem:** Build a working calculator with a graphical interface.

**Objetivo:** Modelar uma máquina de estados, sem `eval`.  
**Goal:** Model a state machine, without `eval`.

**Conceitos / Concepts:** CSS Grid, delegação de eventos, teclado

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/36-calculadora-visual/`

**Resultado esperado:** Contas encadeadas, mouse e teclado. Divisão por zero mostra Erro.  
**Expected result:** Chained math, mouse and keyboard. Division by zero shows Erro.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>36. Calculadora visual</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card calculator">
      <h1>Calculadora</h1>
      <output id="display" class="display" aria-live="polite">0</output>
      <div id="keypad" class="keypad">
        <button class="btn btn--ghost" data-action="clear" type="button">C</button>
        <button class="btn btn--ghost" data-action="backspace" type="button">⌫</button>
        <button class="btn btn--ghost" data-action="sign" type="button">±</button>
        <button class="btn" data-operator="/" type="button">÷</button>
        <button class="btn btn--ghost" data-digit="7" type="button">7</button>
        <button class="btn btn--ghost" data-digit="8" type="button">8</button>
        <button class="btn btn--ghost" data-digit="9" type="button">9</button>
        <button class="btn" data-operator="*" type="button">×</button>
        <button class="btn btn--ghost" data-digit="4" type="button">4</button>
        <button class="btn btn--ghost" data-digit="5" type="button">5</button>
        <button class="btn btn--ghost" data-digit="6" type="button">6</button>
        <button class="btn" data-operator="-" type="button">−</button>
        <button class="btn btn--ghost" data-digit="1" type="button">1</button>
        <button class="btn btn--ghost" data-digit="2" type="button">2</button>
        <button class="btn btn--ghost" data-digit="3" type="button">3</button>
        <button class="btn" data-operator="+" type="button">+</button>
        <button class="btn btn--ghost keypad-zero" data-digit="0" type="button">0</button>
        <button class="btn btn--ghost" data-action="decimal" type="button">,</button>
        <button class="btn" data-action="equals" type="button">=</button>
      </div>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const MAX_DIGITS = 12;
const ERROR_TEXT = "Erro";
const operations = {
  "+": (first, second) => first + second,
  "-": (first, second) => first - second,
  "*": (first, second) => first * second,
  "/": (first, second) => (second === 0 ? null : first / second),
};

const display = document.querySelector("#display");
const keypad = document.querySelector("#keypad");

const state = { current: "0", stored: null, operator: null, startNewNumber: false };

function render() {
  display.textContent = state.current.replace(".", ",");
}

function resetState() {
  Object.assign(state, { current: "0", stored: null, operator: null, startNewNumber: false });
}

function formatResult(value) {
  // toPrecision remove o ruído de ponto flutuante, como em 0.1 + 0.2.
  return String(Number(value.toPrecision(MAX_DIGITS)));
}

function inputDigit(digit) {
  if (state.startNewNumber || state.current === ERROR_TEXT) {
    state.current = digit;
    state.startNewNumber = false;
  } else if (state.current.replace(/[-.]/g, "").length < MAX_DIGITS) {
    state.current = state.current === "0" ? digit : state.current + digit;
  }
}

function inputDecimal() {
  if (state.startNewNumber || state.current === ERROR_TEXT) {
    state.current = "0.";
    state.startNewNumber = false;
  } else if (!state.current.includes(".")) {
    state.current += ".";
  }
}

function applyPendingOperation() {
  if (state.operator === null || state.stored === null) {
    return true;
  }
  const result = operations[state.operator](state.stored, Number(state.current));
  if (result === null) {
    resetState();
    state.current = ERROR_TEXT;
    state.startNewNumber = true;
    return false;
  }
  state.current = formatResult(result);
  return true;
}

function chooseOperator(operator) {
  if (state.current === ERROR_TEXT) {
    return;
  }
  // Trocar de operador sem digitar um novo número não deve calcular nada.
  if (!state.startNewNumber && !applyPendingOperation()) {
    return;
  }
  state.stored = Number(state.current);
  state.operator = operator;
  state.startNewNumber = true;
}

function calculateResult() {
  if (state.operator === null || !applyPendingOperation()) {
    return;
  }
  state.stored = null;
  state.operator = null;
  state.startNewNumber = true;
}

function backspace() {
  if (state.startNewNumber || state.current === ERROR_TEXT) {
    return;
  }
  const shortened = state.current.slice(0, -1);
  state.current = shortened === "" || shortened === "-" ? "0" : shortened;
}

function toggleSign() {
  if (state.current !== "0" && state.current !== ERROR_TEXT) {
    state.current = state.current.startsWith("-") ? state.current.slice(1) : `-${state.current}`;
  }
}

const actions = {
  clear: resetState,
  backspace,
  sign: toggleSign,
  decimal: inputDecimal,
  equals: calculateResult,
};

keypad.addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button) {
    return;
  }
  const { digit, operator, action } = button.dataset;
  if (digit !== undefined) {
    inputDigit(digit);
  } else if (operator) {
    chooseOperator(operator);
  } else {
    actions[action]();
  }
  render();
});

document.addEventListener("keydown", (event) => {
  const { key } = event;
  if (/^\d$/.test(key)) {
    inputDigit(key);
  } else if (key in operations) {
    chooseOperator(key);
  } else if (key === "Enter" || key === "=") {
    event.preventDefault();
    calculateResult();
  } else if (key === "," || key === ".") {
    inputDecimal();
  } else if (key === "Backspace") {
    backspace();
  } else if (key === "Escape") {
    resetState();
  } else {
    return;
  }
  render();
});

render();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
