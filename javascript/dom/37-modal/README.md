<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 37. Modal / Modal

**Problema:** Criar uma janela modal que abre e fecha.  
**Problem:** Build a modal window that opens and closes.

**Objetivo:** Usar o elemento nativo `dialog`.  
**Goal:** Use the native `dialog` element.

**Conceitos / Concepts:** `dialog`, `showModal`, `::backdrop`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/37-modal/`

**Resultado esperado:** Fecha pelo botão, por Esc ou clicando fora.  
**Expected result:** Closes by button, Esc or a click outside.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>37. Modal</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Modal</h1>
      <p class="muted">Feche pelo botão, pela tecla Esc ou clicando fora da janela.</p>
      <button id="open-modal" class="btn" type="button">Abrir modal</button>
      <p id="modal-result" class="status" role="status"></p>
    </main>
    <dialog id="modal" class="modal" aria-labelledby="modal-title">
      <h2 id="modal-title">Confirmar inscrição?</h2>
      <p>Esta janela usa o elemento nativo dialog, que já prende o foco.</p>
      <form method="dialog" class="row modal-actions">
        <button class="btn btn--ghost" value="cancelado">Cancelar</button>
        <button class="btn" value="confirmado">Confirmar</button>
      </form>
    </dialog>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const modal = document.querySelector("#modal");
const modalResult = document.querySelector("#modal-result");

document.querySelector("#open-modal").addEventListener("click", () => {
  modal.returnValue = "";
  modal.showModal();
});

modal.addEventListener("click", (event) => {
  // Um clique no fundo tem o próprio dialog como alvo; no conteúdo, não.
  const box = modal.getBoundingClientRect();
  const isInside =
    event.clientX >= box.left && event.clientX <= box.right &&
    event.clientY >= box.top && event.clientY <= box.bottom;
  if (event.target === modal && !isInside) {
    modal.close("fechado");
  }
});

modal.addEventListener("close", () => {
  modalResult.textContent = `Resultado: ${modal.returnValue || "fechado"}`;
});
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
