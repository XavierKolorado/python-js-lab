<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 50. Aplicação de favoritos / Favorites app

**Problema:** Consumir uma API, filtrar resultados e permitir salvar favoritos.  
**Problem:** Consume an API, filter results and save favorites.

**Objetivo:** Unir dados remotos e estado local.  
**Goal:** Combine remote data and local state.

**Conceitos / Concepts:** `fetch`, `localStorage`, Rick and Morty API

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/50-aplicacao-favoritos/`

**Resultado esperado:** Busca por nome e status, e favoritos mantidos ao recarregar.  
**Expected result:** Search by name and status, with favorites kept after reload.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>50. Aplicação de favoritos</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card card--wide stack">
      <h1>Personagens favoritos</h1>
      <p class="muted">Dados da Rick and Morty API. Os favoritos ficam neste navegador.</p>
      <form id="filter-form" class="filters" novalidate>
        <input id="name-filter" type="search" aria-label="Filtrar por nome" placeholder="Nome do personagem" />
        <select id="status-filter" aria-label="Filtrar por status">
          <option value="">Todos os status</option>
          <option value="alive">Vivo</option>
          <option value="dead">Morto</option>
          <option value="unknown">Desconhecido</option>
        </select>
        <button class="btn" type="submit">Buscar</button>
        <label class="only-favorites"><input id="only-favorites" type="checkbox" /> Só favoritos</label>
      </form>
      <p id="status" class="status" role="status"></p>
      <div id="character-grid" class="character-grid"></div>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const CHARACTERS_URL = "https://rickandmortyapi.com/api/character/";
const STORAGE_KEY = "lab-favorite-characters";
const TIMEOUT_MS = 10000;

const filterForm = document.querySelector("#filter-form");
const nameFilter = document.querySelector("#name-filter");
const statusFilter = document.querySelector("#status-filter");
const onlyFavorites = document.querySelector("#only-favorites");
const statusMessage = document.querySelector("#status");
const characterGrid = document.querySelector("#character-grid");

let characters = [];
let favorites = loadFavorites();

function loadFavorites() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return Array.isArray(saved) ? saved : [];
  } catch {
    return [];
  }
}

function persistFavorites() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(favorites));
}

function isFavorite(id) {
  return favorites.some((favorite) => favorite.id === id);
}

function toggleFavorite(character) {
  favorites = isFavorite(character.id)
    ? favorites.filter(({ id }) => id !== character.id)
    : [...favorites, character];
  persistFavorites();
  render();
}

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

async function fetchCharacters(name, status) {
  const parameters = new URLSearchParams();
  if (name) {
    parameters.set("name", name);
  }
  if (status) {
    parameters.set("status", status);
  }
  const response = await fetch(`${CHARACTERS_URL}?${parameters}`, {
    signal: AbortSignal.timeout(TIMEOUT_MS),
  });
  // Esta API usa 404 para buscas sem resultado.
  if (response.status === 404) {
    return [];
  }
  if (!response.ok) {
    throw new Error(`A API respondeu com status ${response.status}.`);
  }
  return (await response.json()).results;
}

function createCharacterCard(character) {
  const card = document.createElement("article");
  card.className = "character";
  const picture = document.createElement("img");
  picture.src = character.image;
  picture.alt = character.name;
  picture.loading = "lazy";
  const body = document.createElement("div");
  body.className = "character-body";
  const heading = document.createElement("h2");
  heading.textContent = character.name;
  const details = document.createElement("span");
  details.className = "muted";
  details.textContent = `${character.species} · ${character.status}`;
  const favoriteButton = document.createElement("button");
  const favorite = isFavorite(character.id);
  favoriteButton.type = "button";
  favoriteButton.className = "btn btn--ghost";
  favoriteButton.textContent = favorite ? "★ Favorito" : "☆ Favoritar";
  favoriteButton.setAttribute("aria-pressed", String(favorite));
  favoriteButton.addEventListener("click", () => toggleFavorite(character));
  body.append(heading, details, favoriteButton);
  card.append(picture, body);
  return card;
}

function render() {
  const visible = onlyFavorites.checked ? favorites : characters;
  characterGrid.replaceChildren(...visible.map(createCharacterCard));
  const emptyMessage = onlyFavorites.checked
    ? "Nenhum favorito salvo."
    : "Nenhum personagem encontrado.";
  setStatus(visible.length ? `${visible.length} personagem(ns)` : emptyMessage);
}

async function search() {
  setStatus("Buscando...");
  try {
    characters = await fetchCharacters(nameFilter.value.trim(), statusFilter.value);
    render();
  } catch (error) {
    setStatus(`Falha ao buscar: ${error.message}`, true);
  }
}

filterForm.addEventListener("submit", (event) => {
  event.preventDefault();
  onlyFavorites.checked = false;
  search();
});

onlyFavorites.addEventListener("change", render);

search();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
