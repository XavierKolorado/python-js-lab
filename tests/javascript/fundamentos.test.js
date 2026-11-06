"use strict";

const assert = require("node:assert/strict");
const { test } = require("node:test");
const { load } = require("./helpers");

const fundamentals = (number) => load("fundamentos", number);

test("01 usa nome padrão em texto vazio", () => {
  const { buildMessage } = fundamentals(1);
  assert.match(buildMessage("Ana"), /Ana/);
  assert.match(buildMessage("  "), /visitante/);
  assert.match(buildMessage(), /visitante/);
});

test("02 demonstra let e const", () => {
  const module = fundamentals(2);
  assert.equal(module.demonstrateLet(), 15);
  assert.match(module.demonstrateConstReassignment(), /TypeError/);
  assert.deepEqual(module.demonstrateConstObject(), { name: "Lab", level: 1 });
  assert.equal(module.demonstrateBlockScope(), "fora");
});

test("03 calcula e trata erros", () => {
  const { calculate, parseNumber } = fundamentals(3);
  assert.equal(calculate(10, "+", 5), 15);
  assert.equal(calculate(10, "-", 5), 5);
  assert.equal(calculate(10, "*", 5), 50);
  assert.equal(calculate(10, "/", 5), 2);
  assert.throws(() => calculate(1, "/", 0), /zero/);
  assert.throws(() => calculate(1, "%", 2), /inválida/);
  assert.equal(parseNumber("2,5"), 2.5);
  assert.throws(() => parseNumber("abc"));
  assert.throws(() => parseNumber(""));
  assert.throws(() => parseNumber(undefined));
});

test("04 calcula média e valida notas", () => {
  const { parseGrade, calculateAverage } = fundamentals(4);
  assert.equal(calculateAverage([7, 8, 9]), 8);
  assert.throws(() => calculateAverage([]));
  assert.equal(parseGrade("8,5"), 8.5);
  assert.throws(() => parseGrade("11"));
  assert.throws(() => parseGrade(""));
});

test("05 converte temperaturas", () => {
  const { celsiusToFahrenheit } = fundamentals(5);
  assert.equal(celsiusToFahrenheit(0), 32);
  assert.equal(celsiusToFahrenheit(100), 212);
  assert.throws(() => celsiusToFahrenheit(-300));
  assert.throws(() => celsiusToFahrenheit(NaN));
});

test("06 identifica paridade", () => {
  const { getParity } = fundamentals(6);
  assert.equal(getParity(4), "par");
  assert.equal(getParity(-3), "ímpar");
  assert.throws(() => getParity(1.5));
});

test("07 acha o maior em qualquer posição", () => {
  const { largestOfThree } = fundamentals(7);
  assert.equal(largestOfThree(3, 1, 2), 3);
  assert.equal(largestOfThree(1, 3, 2), 3);
  assert.equal(largestOfThree(1, 2, 3), 3);
  assert.throws(() => largestOfThree(1, NaN, 3));
});

test("08 respeita o limite de 18 anos", () => {
  const { isAdult } = fundamentals(8);
  assert.equal(isAdult(18), true);
  assert.equal(isAdult(17), false);
  assert.throws(() => isAdult(-1));
});

test("09 classifica nas fronteiras", () => {
  const { classifyGrade } = fundamentals(9);
  assert.equal(classifyGrade(9), "Excelente");
  assert.equal(classifyGrade(8.99), "Bom");
  assert.equal(classifyGrade(5), "Regular");
  assert.equal(classifyGrade(0), "Insuficiente");
  assert.throws(() => classifyGrade(10.1));
});

test("10 aplica desconto", () => {
  const { calculateDiscount } = fundamentals(10);
  assert.deepEqual(calculateDiscount(200, 15), { discount: 30, finalPrice: 170 });
  assert.throws(() => calculateDiscount(-1, 10));
  assert.throws(() => calculateDiscount(100, 101));
});
