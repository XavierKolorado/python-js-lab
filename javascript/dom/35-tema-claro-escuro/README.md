<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 35. Tema claro e escuro / Light and dark theme

**Problema:** Criar um alternador de temas.  
**Problem:** Build a theme switcher.

**Objetivo:** Usar variáveis CSS e a preferência do sistema.  
**Goal:** Use CSS variables and the system preference.

**Conceitos / Concepts:** variáveis CSS, `matchMedia`, `localStorage`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/35-tema-claro-escuro/`

**Resultado esperado:** O tema alterna e continua salvo ao recarregar.  
**Expected result:** The theme switches and stays saved after reload.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>35. Tema claro e escuro</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Tema claro e escuro</h1>
      <p class="muted">A escolha fica salva. Sem escolha salva, o tema segue o sistema operacional.</p>
      <button id="theme-toggle" class="btn" type="button" aria-pressed="false">Ativar tema escuro</button>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const STORAGE_KEY = "lab-theme";
const themeToggle = document.querySelector("#theme-toggle");

function readSavedTheme() {
  const savedTheme = localStorage.getItem(STORAGE_KEY);
  return savedTheme === "dark" || savedTheme === "light" ? savedTheme : null;
}

function getSystemTheme() {
  return matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme) {
  const isDark = theme === "dark";
  document.documentElement.dataset.theme = theme;
  themeToggle.setAttribute("aria-pressed", String(isDark));
  themeToggle.textContent = isDark ? "Ativar tema claro" : "Ativar tema escuro";
}

themeToggle.addEventListener("click", () => {
  const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  localStorage.setItem(STORAGE_KEY, nextTheme);
  applyTheme(nextTheme);
});

applyTheme(readSavedTheme() ?? getSystemTheme());
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
