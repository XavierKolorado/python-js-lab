<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 40. Cronômetro / Stopwatch

**Problema:** Implementar iniciar, pausar e zerar.  
**Problem:** Implement start, pause and reset.

**Objetivo:** Medir tempo sem acumular erro dos temporizadores.  
**Goal:** Measure time without accumulating timer drift.

**Conceitos / Concepts:** `performance.now`, `setInterval`, estado

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/40-cronometro/`

**Resultado esperado:** O tempo corre, pausa, retoma e zera.  
**Expected result:** Time runs, pauses, resumes and resets.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>40. Cronômetro</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card">
      <h1>Cronômetro</h1>
      <output id="time-display" class="time-display">00:00.00</output>
      <div class="row time-actions">
        <button id="start" class="btn" type="button">Iniciar</button>
        <button id="pause" class="btn btn--ghost" type="button" disabled>Pausar</button>
        <button id="reset" class="btn btn--danger" type="button">Zerar</button>
      </div>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
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
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
