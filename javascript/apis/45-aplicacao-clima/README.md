<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 45. Aplicação de clima / Weather app

**Problema:** Criar uma aplicação que apresenta informações meteorológicas de uma API pública.  
**Problem:** Build an app that shows weather data from a public API.

**Objetivo:** Encadear requisições dependentes.  
**Goal:** Chain dependent requests.

**Conceitos / Concepts:** `fetch`, `URLSearchParams`, Open-Meteo

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/45-aplicacao-clima/`

**Resultado esperado:** Temperatura, condição, umidade e vento da cidade.  
**Expected result:** The city's temperature, condition, humidity and wind.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>45. Aplicação de clima</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Clima agora</h1>
      <form id="city-form" class="search-form" novalidate>
        <input id="city-input" aria-label="Cidade" placeholder="Ex.: Curitiba" />
        <button class="btn" type="submit">Consultar</button>
      </form>
      <p id="status" class="status" role="status"></p>
      <article id="weather" class="weather" hidden>
        <h2 id="weather-city"></h2>
        <p id="weather-temperature" class="temperature"></p>
        <p id="weather-description"></p>
        <p id="weather-details" class="muted"></p>
      </article>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search";
const FORECAST_URL = "https://api.open-meteo.com/v1/forecast";
const TIMEOUT_MS = 10000;
const WEATHER_GROUPS = [
  { codes: [0], label: "Céu limpo" },
  { codes: [1, 2], label: "Parcialmente nublado" },
  { codes: [3], label: "Nublado" },
  { codes: [45, 48], label: "Neblina" },
  { codes: [51, 53, 55, 56, 57], label: "Garoa" },
  { codes: [61, 63, 65, 66, 67, 80, 81, 82], label: "Chuva" },
  { codes: [71, 73, 75, 77, 85, 86], label: "Neve" },
  { codes: [95, 96, 99], label: "Trovoada" },
];

const cityForm = document.querySelector("#city-form");
const cityInput = document.querySelector("#city-input");
const statusMessage = document.querySelector("#status");
const weatherCard = document.querySelector("#weather");

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function describeWeather(code) {
  return WEATHER_GROUPS.find(({ codes }) => codes.includes(code))?.label ?? "Condição desconhecida";
}

async function fetchJson(baseUrl, parameters) {
  const url = `${baseUrl}?${new URLSearchParams(parameters)}`;
  const response = await fetch(url, { signal: AbortSignal.timeout(TIMEOUT_MS) });
  if (!response.ok) {
    throw new Error(`A API respondeu com status ${response.status}.`);
  }
  return response.json();
}

async function findCity(name) {
  const { results } = await fetchJson(GEOCODING_URL, { name, count: 1, language: "pt" });
  if (!results?.length) {
    throw new Error("Cidade não encontrada.");
  }
  return results[0];
}

async function fetchWeather({ latitude, longitude }) {
  const { current } = await fetchJson(FORECAST_URL, {
    latitude,
    longitude,
    current: "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
    timezone: "auto",
  });
  return current;
}

function renderWeather(city, weather) {
  document.querySelector("#weather-city").textContent = `${city.name}, ${city.country ?? ""}`;
  document.querySelector("#weather-temperature").textContent = `${Math.round(weather.temperature_2m)} °C`;
  document.querySelector("#weather-description").textContent = describeWeather(weather.weather_code);
  document.querySelector("#weather-details").textContent =
    `Umidade ${weather.relative_humidity_2m}% · Vento ${weather.wind_speed_10m} km/h`;
  weatherCard.hidden = false;
}

cityForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const cityName = cityInput.value.trim();
  weatherCard.hidden = true;
  if (!cityName) {
    setStatus("Digite o nome de uma cidade.", true);
    return;
  }
  setStatus("Consultando...");
  try {
    const city = await findCity(cityName);
    renderWeather(city, await fetchWeather(city));
    setStatus("");
  } catch (error) {
    setStatus(error.message, true);
  }
});
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
