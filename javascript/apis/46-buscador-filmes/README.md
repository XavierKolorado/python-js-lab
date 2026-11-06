<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 46. Buscador de filmes / Movie finder

**Problema:** Consumir uma API de filmes e apresentar resultados.  
**Problem:** Consume a movie API and show results.

**Objetivo:** Carregar uma vez e filtrar no cliente.  
**Goal:** Load once and filter on the client.

**Conceitos / Concepts:** `fetch`, `filter`, CSS Grid, Studio Ghibli API

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/46-buscador-filmes/`

**Resultado esperado:** Cartões de filmes filtrados por título, direção ou ano.  
**Expected result:** Movie cards filtered by title, director or year.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>46. Buscador de filmes</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card card--wide stack">
      <h1>Buscador de filmes</h1>
      <p class="muted">Filmes do Studio Ghibli, servidos pela Studio Ghibli API.</p>
      <input id="movie-search" type="search" aria-label="Buscar filme" placeholder="Busque por título, direção ou ano" />
      <p id="status" class="status" role="status"></p>
      <div id="movie-grid" class="movie-grid"></div>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const MOVIES_URL = "https://ghibliapi.vercel.app/films";
const TIMEOUT_MS = 10000;

const searchInput = document.querySelector("#movie-search");
const statusMessage = document.querySelector("#status");
const movieGrid = document.querySelector("#movie-grid");

let movies = [];

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function matchesSearch(movie, term) {
  return [movie.title, movie.director, movie.release_date]
    .join(" ")
    .toLowerCase()
    .includes(term);
}

function createMovieCard({ title, director, release_date: year, image, rt_score: score }) {
  const card = document.createElement("article");
  card.className = "movie";
  const poster = document.createElement("img");
  poster.src = image;
  poster.alt = `Pôster de ${title}`;
  poster.loading = "lazy";
  const body = document.createElement("div");
  body.className = "movie-body";
  const heading = document.createElement("h2");
  heading.textContent = title;
  const details = document.createElement("p");
  details.className = "muted";
  details.textContent = `${year} · ${director} · nota ${score}`;
  body.append(heading, details);
  card.append(poster, body);
  return card;
}

function render() {
  const term = searchInput.value.trim().toLowerCase();
  const results = movies.filter((movie) => matchesSearch(movie, term));
  movieGrid.replaceChildren(...results.map(createMovieCard));
  setStatus(results.length ? `${results.length} filme(s)` : "Nenhum filme encontrado.");
}

async function loadMovies() {
  setStatus("Carregando filmes...");
  searchInput.disabled = true;
  try {
    const response = await fetch(MOVIES_URL, { signal: AbortSignal.timeout(TIMEOUT_MS) });
    if (!response.ok) {
      throw new Error(`A API respondeu com status ${response.status}.`);
    }
    movies = await response.json();
    searchInput.disabled = false;
    render();
  } catch (error) {
    setStatus(`Falha ao carregar: ${error.message}`, true);
  }
}

searchInput.addEventListener("input", render);
loadMovies();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
