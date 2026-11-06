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
