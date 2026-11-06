"use strict";

const assert = require("node:assert/strict");
const { test, mock } = require("node:test");
const { load } = require("./helpers");

const logic = (number) => load("logica", number);

test("11 monta dez linhas", () => {
  const { buildMultiplicationTable } = logic(11);
  const lines = buildMultiplicationTable(7);
  assert.equal(lines.length, 10);
  assert.equal(lines[9], "7 x 10 = 70");
  assert.throws(() => buildMultiplicationTable(1.5));
});

test("12 soma de 1 até N", () => {
  const { sumUpTo } = logic(12);
  assert.equal(sumUpTo(100), 5050);
  assert.throws(() => sumUpTo(0));
});

test("13 calcula fatorial sem perder precisão", () => {
  const { factorial } = logic(13);
  assert.equal(factorial(0), 1n);
  assert.equal(factorial(25), 15511210043330985984000000n);
  assert.throws(() => factorial(-1));
});

test("14 sorteia dentro do intervalo e orienta palpites", () => {
  const { drawSecret, evaluateGuess } = logic(14);
  assert.equal(drawSecret(100, () => 0), 1);
  assert.equal(drawSecret(100, () => 0.999), 100);
  assert.match(evaluateGuess(1, 5), /maior/);
  assert.match(evaluateGuess(9, 5), /menor/);
  assert.equal(evaluateGuess(5, 5), null);
});

test("15 reconhece palíndromos", () => {
  const { isPalindrome } = logic(15);
  assert.equal(isPalindrome("Ame a ema"), true);
  assert.equal(isPalindrome("Socorram-me, subi no ônibus em Marrocos"), true);
  assert.equal(isPalindrome("javascript"), false);
  assert.throws(() => isPalindrome("..."));
});

test("16 conta vogais acentuadas", () => {
  const { countVowels } = logic(16);
  assert.deepEqual(countVowels("Água É ótima"), { a: 3, e: 1, i: 1, o: 1, u: 1 });
  assert.deepEqual(countVowels(""), { a: 0, e: 0, i: 0, o: 0, u: 0 });
});

test("17 verifica primos", () => {
  const { isPrime } = logic(17);
  for (const prime of [2, 3, 97, 7919]) {
    assert.equal(isPrime(prime), true);
  }
  for (const composite of [-7, 0, 1, 9, 49]) {
    assert.equal(isPrime(composite), false);
  }
  assert.throws(() => isPrime(1.5));
});

test("18 encontra o maior valor", () => {
  const { findLargest } = logic(18);
  assert.equal(findLargest([3, 9, 2]), 9);
  assert.equal(findLargest([-5, -2]), -2);
  assert.throws(() => findLargest([]));
  assert.throws(() => findLargest([1, NaN]));
});

test("19 inverte preservando emoji", () => {
  const { reverseString } = logic(19);
  assert.equal(reverseString("abc"), "cba");
  assert.equal(reverseString("a😀b"), "b😀a");
  assert.equal(reverseString(""), "");
});

test("20 conta até zero e encerra", () => {
  const { buildCountdown, runCountdown } = logic(20);
  assert.deepEqual(buildCountdown(3), [3, 2, 1, 0]);
  assert.throws(() => buildCountdown(-1));

  mock.timers.enable({ apis: ["setInterval"] });
  const ticks = [];
  let finished = 0;
  runCountdown(2, (seconds) => ticks.push(seconds), () => { finished += 1; });
  mock.timers.tick(5000);
  mock.timers.reset();
  assert.deepEqual(ticks, [2, 1, 0]);
  assert.equal(finished, 1);
});
