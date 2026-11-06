<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 41. Preferências com localStorage / Preferences with localStorage

**Problema:** Salvar e recuperar preferências do usuário.  
**Problem:** Save and restore user preferences.

**Objetivo:** Persistir no navegador e tolerar dados corrompidos.  
**Goal:** Persist in the browser and tolerate corrupted data.

**Conceitos / Concepts:** `localStorage`, `JSON`, formulários

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/41-preferencias-localstorage/`

**Resultado esperado:** Nome, fonte e destaque voltam ao recarregar.  
**Expected result:** Name, font and highlight return after reload.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>41. Preferências com localStorage</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card">
      <h1>Preferências</h1>
      <p id="greeting" class="muted"></p>
      <form id="preferences-form" class="stack">
        <label>Seu nome <input name="name" maxlength="40" /></label>
        <label>Tamanho da fonte
          <select name="fontSize">
            <option value="14">Pequena</option>
            <option value="16">Média</option>
            <option value="20">Grande</option>
          </select>
        </label>
        <label class="inline-field"><input name="highlight" type="checkbox" /> Destacar a borda do cartão</label>
        <div class="row">
          <button class="btn" type="submit">Salvar</button>
          <button id="clear-preferences" class="btn btn--danger" type="button">Limpar</button>
        </div>
      </form>
      <p id="status" class="status" role="status"></p>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const STORAGE_KEY = "lab-preferences";
const DEFAULT_PREFERENCES = { name: "", fontSize: "16", highlight: false };

const form = document.querySelector("#preferences-form");
const greeting = document.querySelector("#greeting");
const statusMessage = document.querySelector("#status");

function loadPreferences() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return { ...DEFAULT_PREFERENCES, ...saved };
  } catch {
    // Dado corrompido não deve impedir a página de abrir.
    return { ...DEFAULT_PREFERENCES };
  }
}

function applyPreferences({ name, fontSize, highlight }) {
  document.documentElement.style.fontSize = `${fontSize}px`;
  document.querySelector(".card").classList.toggle("card--highlight", highlight);
  greeting.textContent = name ? `Olá, ${name}!` : "Nenhum nome salvo.";
}

function fillForm({ name, fontSize, highlight }) {
  form.elements.name.value = name;
  form.elements.fontSize.value = fontSize;
  form.elements.highlight.checked = highlight;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const preferences = {
    name: form.elements.name.value.trim(),
    fontSize: form.elements.fontSize.value,
    highlight: form.elements.highlight.checked,
  };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(preferences));
  applyPreferences(preferences);
  statusMessage.textContent = "Preferências salvas.";
});

document.querySelector("#clear-preferences").addEventListener("click", () => {
  localStorage.removeItem(STORAGE_KEY);
  fillForm(DEFAULT_PREFERENCES);
  applyPreferences(DEFAULT_PREFERENCES);
  statusMessage.textContent = "Preferências removidas.";
});

const initialPreferences = loadPreferences();
fillForm(initialPreferences);
applyPreferences(initialPreferences);
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
