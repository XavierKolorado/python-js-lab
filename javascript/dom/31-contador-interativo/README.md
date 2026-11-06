<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 31. Contador interativo / Interactive counter

**Problema:** Criar botões para incrementar, decrementar e zerar um contador.  
**Problem:** Create buttons to increment, decrement and reset a counter.

**Objetivo:** Selecionar elementos e reagir a cliques.  
**Goal:** Select elements and react to clicks.

**Conceitos / Concepts:** `querySelector`, `addEventListener`, `textContent`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/31-contador-interativo/`

**Resultado esperado:** O número muda a cada clique.  
**Expected result:** The number changes on each click.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>31. Contador interativo</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card">
      <h1>Contador interativo</h1>
      <p class="muted">Incremente, decremente ou zere o valor.</p>
      <output id="counter-value" class="counter" aria-live="polite">0</output>
      <div class="row counter-actions">
        <button id="decrement" class="btn btn--ghost" type="button">− 1</button>
        <button id="reset" class="btn btn--danger" type="button">Zerar</button>
        <button id="increment" class="btn" type="button">+ 1</button>
      </div>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
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
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
