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
