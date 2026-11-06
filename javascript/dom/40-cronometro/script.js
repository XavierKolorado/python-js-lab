"use strict";

const UPDATE_INTERVAL_MS = 30;

const timeDisplay = document.querySelector("#time-display");
const startButton = document.querySelector("#start");
const pauseButton = document.querySelector("#pause");
const resetButton = document.querySelector("#reset");

let elapsedBeforeStart = 0;
let startedAt = null;
let timerId = null;

function currentElapsed() {
  return elapsedBeforeStart + (startedAt === null ? 0 : performance.now() - startedAt);
}

function formatTime(milliseconds) {
  const totalCentiseconds = Math.floor(milliseconds / 10);
  const minutes = Math.floor(totalCentiseconds / 6000);
  const seconds = Math.floor(totalCentiseconds / 100) % 60;
  const centiseconds = totalCentiseconds % 100;
  const pad = (value) => String(value).padStart(2, "0");
  return `${pad(minutes)}:${pad(seconds)}.${pad(centiseconds)}`;
}

function render() {
  timeDisplay.textContent = formatTime(currentElapsed());
}

function setRunning(isRunning) {
  startButton.disabled = isRunning;
  pauseButton.disabled = !isRunning;
}

function start() {
  startedAt = performance.now();
  timerId = setInterval(render, UPDATE_INTERVAL_MS);
  setRunning(true);
}

function pause() {
  elapsedBeforeStart = currentElapsed();
  startedAt = null;
  clearInterval(timerId);
  setRunning(false);
  render();
}

function reset() {
  clearInterval(timerId);
  elapsedBeforeStart = 0;
  startedAt = null;
  setRunning(false);
  render();
}

startButton.addEventListener("click", start);
pauseButton.addEventListener("click", pause);
resetButton.addEventListener("click", reset);
