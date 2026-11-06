"use strict";

const counterValue = document.querySelector("#counter-value");
let count = 0;

function setCount(newCount) {
  count = newCount;
  counterValue.textContent = String(count);
}

document.querySelector("#increment").addEventListener("click", () => setCount(count + 1));
document.querySelector("#decrement").addEventListener("click", () => setCount(count - 1));
document.querySelector("#reset").addEventListener("click", () => setCount(0));
