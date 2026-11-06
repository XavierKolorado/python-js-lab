<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 34. Menu responsivo / Responsive menu

**Problema:** Criar um menu de navegação que funcione em dispositivos móveis.  
**Problem:** Build a navigation menu that works on mobile.

**Objetivo:** Combinar media queries e estado acessível.  
**Goal:** Combine media queries and accessible state.

**Conceitos / Concepts:** `@media`, `aria-expanded`, teclado

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/34-menu-responsivo/`

**Resultado esperado:** Barra no desktop e painel no celular. Esc fecha.  
**Expected result:** A bar on desktop and a panel on mobile. Esc closes it.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>34. Menu responsivo</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <header class="site-header">
      <strong>Lab</strong>
      <button id="menu-toggle" class="btn btn--ghost menu-toggle" type="button" aria-expanded="false" aria-controls="site-menu">Menu</button>
      <nav id="site-menu" class="site-menu" aria-label="Principal">
        <a href="#inicio">Início</a>
        <a href="#projetos">Projetos</a>
        <a href="#contato">Contato</a>
      </nav>
    </header>
    <main class="card stack">
      <h1>Menu responsivo</h1>
      <p class="muted">Abaixo de 720 px, o menu vira um painel aberto pelo botão. A tecla Esc fecha o painel.</p>
      <section id="inicio"><h2>Início</h2><p>Conteúdo de exemplo.</p></section>
      <section id="projetos"><h2>Projetos</h2><p>Conteúdo de exemplo.</p></section>
      <section id="contato"><h2>Contato</h2><p>Conteúdo de exemplo.</p></section>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const menuToggle = document.querySelector("#menu-toggle");
const siteMenu = document.querySelector("#site-menu");

function setMenuOpen(isOpen) {
  siteMenu.classList.toggle("site-menu--open", isOpen);
  menuToggle.setAttribute("aria-expanded", String(isOpen));
  menuToggle.textContent = isOpen ? "Fechar" : "Menu";
}

menuToggle.addEventListener("click", () => {
  setMenuOpen(menuToggle.getAttribute("aria-expanded") !== "true");
});

siteMenu.addEventListener("click", (event) => {
  if (event.target.matches("a")) {
    setMenuOpen(false);
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    setMenuOpen(false);
  }
});
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
