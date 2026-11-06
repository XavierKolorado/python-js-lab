<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 38. Galeria de imagens / Image gallery

**Problema:** Criar uma galeria com filtros e visualização de imagens.  
**Problem:** Build a gallery with filters and an image viewer.

**Objetivo:** Derivar a interface de dados e estado.  
**Goal:** Derive the interface from data and state.

**Conceitos / Concepts:** CSS Grid, `dialog`, SVG, aritmética modular

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/38-galeria-imagens/`

**Resultado esperado:** Filtros por categoria e visualizador com anterior e próxima.  
**Expected result:** Category filters and a viewer with previous and next.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>38. Galeria de imagens</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card card--wide stack">
      <h1>Galeria de imagens</h1>
      <div id="filters" class="row" role="group" aria-label="Filtrar por categoria"></div>
      <div id="gallery" class="gallery"></div>
    </main>
    <dialog id="viewer" class="viewer" aria-label="Visualização da imagem">
      <img id="viewer-image" alt="" />
      <p id="viewer-caption"></p>
      <div class="row viewer-actions">
        <button id="previous-image" class="btn btn--ghost" type="button">Anterior</button>
        <button id="next-image" class="btn btn--ghost" type="button">Próxima</button>
        <button id="close-viewer" class="btn" type="button">Fechar</button>
      </div>
    </dialog>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const IMAGES = [
  { file: "montanha.svg", title: "Montanha", category: "natureza" },
  { file: "floresta.svg", title: "Floresta", category: "natureza" },
  { file: "mar.svg", title: "Mar", category: "natureza" },
  { file: "predios.svg", title: "Prédios", category: "cidade" },
  { file: "ponte.svg", title: "Ponte", category: "cidade" },
  { file: "circulos.svg", title: "Círculos", category: "abstrato" },
];
const ALL_CATEGORIES = "todas";

const filters = document.querySelector("#filters");
const gallery = document.querySelector("#gallery");
const viewer = document.querySelector("#viewer");
const viewerImage = document.querySelector("#viewer-image");
const viewerCaption = document.querySelector("#viewer-caption");

let activeCategory = ALL_CATEGORIES;
let viewerIndex = 0;

function visibleImages() {
  return activeCategory === ALL_CATEGORIES
    ? IMAGES
    : IMAGES.filter((image) => image.category === activeCategory);
}

function renderFilters() {
  const categories = [ALL_CATEGORIES, ...new Set(IMAGES.map((image) => image.category))];
  filters.replaceChildren(
    ...categories.map((category) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "btn";
      button.textContent = category;
      button.setAttribute("aria-pressed", String(category === activeCategory));
      button.addEventListener("click", () => {
        activeCategory = category;
        render();
      });
      return button;
    }),
  );
}

function renderGallery() {
  gallery.replaceChildren(
    ...visibleImages().map((image, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "gallery-item";
      button.setAttribute("aria-label", `Ampliar ${image.title}`);
      const thumbnail = document.createElement("img");
      thumbnail.src = `imagens/${image.file}`;
      thumbnail.alt = image.title;
      button.append(thumbnail);
      button.addEventListener("click", () => openViewer(index));
      return button;
    }),
  );
}

function render() {
  renderFilters();
  renderGallery();
}

function showImage(index) {
  const images = visibleImages();
  viewerIndex = (index + images.length) % images.length;
  const image = images[viewerIndex];
  viewerImage.src = `imagens/${image.file}`;
  viewerImage.alt = image.title;
  viewerCaption.textContent = `${image.title} (${viewerIndex + 1} de ${images.length})`;
}

function openViewer(index) {
  showImage(index);
  viewer.showModal();
}

document.querySelector("#previous-image").addEventListener("click", () => showImage(viewerIndex - 1));
document.querySelector("#next-image").addEventListener("click", () => showImage(viewerIndex + 1));
document.querySelector("#close-viewer").addEventListener("click", () => viewer.close());

render();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
