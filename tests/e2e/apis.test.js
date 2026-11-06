"use strict";

const assert = require("node:assert/strict");
const { after, before, test } = require("node:test");
const { Lab, fulfillJson, stubSuccess } = require("./harness");

const lab = new Lab();
before(() => lab.start());
after(() => lab.stop());

const text = (page, selector) => page.locator(selector).innerText();
const IMAGE = "data:image/gif;base64,R0lGODlhAQABAAAAACw=";

test("41 preferências persistem, limpam e toleram dado corrompido", async () => {
  await lab.open("apis/41-preferencias-localstorage", async (page) => {
    await page.fill('[name="name"]', "Ana");
    await page.selectOption('[name="fontSize"]', "20");
    await page.check('[name="highlight"]');
    await page.click('button[type="submit"]');
    await page.reload();
    assert.equal(await text(page, "#greeting"), "Olá, Ana!");
    assert.equal(await page.inputValue('[name="fontSize"]'), "20");
    assert.equal(await page.locator(".card--highlight").count(), 1);
    await page.click("#clear-preferences");
    await page.reload();
    assert.equal(await text(page, "#greeting"), "Nenhum nome salvo.");
    await page.evaluate(() => localStorage.setItem("lab-preferences", "{quebrado"));
    await page.reload();
    assert.equal(await text(page, "#greeting"), "Nenhum nome salvo.");
  });
});

test("42 login valida, avisa que é demo e não guarda senha", () =>
  lab.open("apis/42-login-demonstrativo", async (page) => {
    assert.match(await text(page, ".warning"), /não é segurança real/);
    await page.click('button[type="submit"]');
    assert.match(await text(page, "#login-error"), /Preencha/);
    await page.fill('[name="username"]', "aluno");
    await page.fill('[name="password"]', "errada");
    await page.click('button[type="submit"]');
    assert.match(await text(page, "#login-error"), /incorretos/);
    await page.fill('[name="password"]', "lab-demo");
    await page.click('button[type="submit"]');
    assert.match(await text(page, "#welcome-message"), /aluno/);
    const stored = await page.evaluate(() => JSON.stringify({ ...sessionStorage, ...localStorage }));
    assert.equal(stored.includes("lab-demo\""), false);
    await page.reload();
    assert.equal(await page.locator("#welcome-view").isVisible(), true);
    await page.click("#logout");
    assert.equal(await page.locator("#login-form").isVisible(), true);
  }));

test("43 API carrega usuários", () =>
  lab.open(
    "apis/43-consumo-api",
    async (page) => {
      await page.click("#load-users");
      await page.waitForSelector("#user-list li");
      assert.match(await text(page, "#status"), /usuário\(s\) carregado/);
    },
    {
      prepare: (page) =>
        stubSuccess(page, "**/jsonplaceholder.typicode.com/users", [
          { name: "Ana", email: "a@e.co", address: { city: "Recife" } },
        ]),
    },
  ));

test("43 API mostra erro de status e de rede", async () => {
  await lab.open(
    "apis/43-consumo-api",
    async (page) => {
      await page.click("#load-users");
      await page.waitForSelector(".status--error");
      assert.match(await text(page, "#status"), /500/);
      assert.equal(await page.locator("#load-users").isEnabled(), true);
    },
    { prepare: (page) => page.route("**/users", (route) => fulfillJson(route, {}, 500)) },
  );
  await lab.open(
    "apis/43-consumo-api",
    async (page) => {
      await page.click("#load-users");
      await page.waitForSelector(".status--error");
    },
    { prepare: (page) => page.route("**/users", (route) => route.abort()) },
  );
});

test("44 CEP exibe endereço", () =>
  lab.open(
    "apis/44-consulta-cep",
    async (page) => {
      await page.fill("#cep-input", "01001-000");
      await page.press("#cep-input", "Enter");
      await page.waitForSelector("#address dd");
      assert.match(await text(page, "#address"), /São Paulo/);
    },
    {
      prepare: (page) =>
        stubSuccess(page, "**/viacep.com.br/**", {
          cep: "01001-000", logradouro: "Praça da Sé", bairro: "Sé", localidade: "São Paulo", uf: "SP", ddd: "11",
        }),
    },
  ));

test("44 CEP recusa formato inválido e CEP inexistente", () =>
  lab.open(
    "apis/44-consulta-cep",
    async (page) => {
      await page.fill("#cep-input", "123");
      await page.press("#cep-input", "Enter");
      assert.match(await text(page, "#status"), /8 dígitos/);
      await page.fill("#cep-input", "99999-999");
      await page.press("#cep-input", "Enter");
      await page.waitForFunction(() => document.querySelector("#status").textContent.includes("não encontrado"));
    },
    { prepare: (page) => page.route("**/viacep.com.br/**", (route) => fulfillJson(route, { erro: "true" })) },
  ));

test("45 clima mostra a cidade", () =>
  lab.open(
    "apis/45-aplicacao-clima",
    async (page) => {
      await page.fill("#city-input", "Curitiba");
      await page.press("#city-input", "Enter");
      await page.waitForSelector("#weather:not([hidden])");
      assert.match(await text(page, "#weather-city"), /Curitiba/);
      assert.match(await text(page, "#weather-temperature"), /°C/);
    },
    {
      prepare: async (page) => {
        await stubSuccess(page, "**/geocoding-api.open-meteo.com/**", {
          results: [{ name: "Curitiba", country: "Brasil", latitude: -25.4, longitude: -49.2 }],
        });
        await stubSuccess(page, "**/api.open-meteo.com/**", {
          current: { temperature_2m: 20, relative_humidity_2m: 70, wind_speed_10m: 9, weather_code: 3 },
        });
      },
    },
  ));

test("45 clima valida vazio e cidade desconhecida", () =>
  lab.open(
    "apis/45-aplicacao-clima",
    async (page) => {
      await page.press("#city-input", "Enter");
      assert.match(await text(page, "#status"), /Digite/);
      await page.fill("#city-input", "Xyzzy");
      await page.press("#city-input", "Enter");
      await page.waitForFunction(() => document.querySelector("#status").textContent.includes("não encontrada"));
    },
    { prepare: (page) => page.route("**/geocoding-api.open-meteo.com/**", (route) => fulfillJson(route, {})) },
  ));

test("46 filmes carregam e filtram", () =>
  lab.open(
    "apis/46-buscador-filmes",
    async (page) => {
      await page.waitForSelector(".movie");
      const total = await page.locator(".movie").count();
      await page.fill("#movie-search", "totoro");
      assert.equal(await page.locator(".movie").count(), 1);
      assert.ok(total > 1);
      await page.fill("#movie-search", "zzz");
      assert.match(await text(page, "#status"), /Nenhum filme/);
    },
    {
      prepare: (page) =>
        stubSuccess(page, "**/ghibliapi.vercel.app/films", [
          { title: "My Neighbor Totoro", director: "Hayao Miyazaki", release_date: "1988", image: IMAGE, rt_score: "93" },
          { title: "Pom Poko", director: "Isao Takahata", release_date: "1994", image: IMAGE, rt_score: "78" },
        ]),
    },
  ));

test("46 filmes mostram falha da API", () =>
  lab.open(
    "apis/46-buscador-filmes",
    async (page) => {
      await page.waitForSelector(".status--error");
      assert.match(await text(page, "#status"), /503/);
    },
    { prepare: (page) => page.route("**/films", (route) => fulfillJson(route, {}, 503)) },
  ));

test("47 painel calcula indicadores", () =>
  lab.open(
    "apis/47-painel-dados",
    async (page) => {
      await page.waitForSelector(".metric");
      assert.equal(await page.locator(".metric").count(), 4);
      assert.ok((await page.locator(".bar").count()) >= 1);
      assert.ok((await page.locator("#top-products tr").count()) >= 1);
    },
    {
      prepare: (page) =>
        stubSuccess(page, "**/dummyjson.com/**", {
          products: [
            { title: "A", price: 10, rating: 4, stock: 2, category: "x" },
            { title: "B", price: 30, rating: 5, stock: 3, category: "y" },
          ],
        }),
    },
  ));

test("47 painel mostra falha e lista vazia", async () => {
  await lab.open(
    "apis/47-painel-dados",
    async (page) => {
      await page.waitForSelector(".status--error");
    },
    { prepare: (page) => page.route("**/dummyjson.com/**", (route) => route.abort()) },
  );
  await lab.open(
    "apis/47-painel-dados",
    async (page) => {
      await page.waitForFunction(() => document.querySelector("#status").textContent.includes("não retornou"));
    },
    { prepare: (page) => page.route("**/dummyjson.com/**", (route) => fulfillJson(route, { products: [] })) },
  );
});

test("48 CRUD cria, valida, edita, exclui e persiste", () =>
  lab.open("apis/48-crud-produtos", async (page) => {
    const fillProduct = async (name, price, quantity) => {
      await page.fill('[name="name"]', name);
      await page.fill('[name="price"]', price);
      await page.fill('[name="quantity"]', quantity);
      await page.click("#save-product");
    };
    assert.match(await text(page, "#product-rows"), /Nenhum produto/);
    await fillProduct("", "10", "1");
    assert.match(await text(page, "#status"), /nome/);
    await fillProduct("Mouse", "abc", "1");
    assert.match(await text(page, "#status"), /preço/);
    await fillProduct("Mouse", "80,50", "1.5");
    assert.match(await text(page, "#status"), /quantidade/);
    await fillProduct("Mouse", "80,50", "3");
    await page.reload();
    assert.match(await text(page, "#product-rows"), /Mouse/);
    await page.getByRole("button", { name: "Editar" }).click();
    assert.equal(await page.inputValue('[name="name"]'), "Mouse");
    await fillProduct("Mouse Pro", "99", "4");
    assert.match(await text(page, "#product-rows"), /Mouse Pro/);
    assert.equal(await page.locator("#product-rows tr").count(), 1);
    page.once("dialog", (dialog) => dialog.dismiss());
    await page.getByRole("button", { name: "Excluir" }).click();
    assert.match(await text(page, "#product-rows"), /Mouse Pro/);
    page.once("dialog", (dialog) => dialog.accept());
    await page.getByRole("button", { name: "Excluir" }).click();
    assert.match(await text(page, "#product-rows"), /Nenhum produto/);
  }));

test("49 paginação navega e respeita os limites", () =>
  lab.open("apis/49-paginacao", async (page) => {
    assert.equal(await page.locator("#item-list li").count(), 10);
    assert.equal(await page.locator("#previous-page").isDisabled(), true);
    await page.click("#next-page");
    assert.equal(await text(page, "#item-list li >> nth=0"), "Registro 11");
    await page.getByRole("button", { name: "6", exact: true }).click();
    assert.equal(await page.locator("#item-list li").count(), 3);
    assert.equal(await page.locator("#next-page").isDisabled(), true);
    assert.equal(await text(page, "#page-info"), "Exibindo 51 a 53 de 53");
    await page.selectOption("#page-size", "20");
    assert.equal(await page.locator("#page-buttons button").count(), 3);
    assert.equal(await text(page, "#item-list li >> nth=0"), "Registro 1");
  }));

const STUB_CHARACTERS = {
  results: [
    { id: 1, name: "Rick Sanchez", species: "Human", status: "Alive", image: IMAGE },
    { id: 2, name: "Morty Smith", species: "Human", status: "Alive", image: IMAGE },
  ],
};

test("50 favoritos filtram, salvam e persistem", () =>
  lab.open(
    "apis/50-aplicacao-favoritos",
    async (page) => {
      await page.waitForSelector(".character");
      await page.fill("#name-filter", "rick");
      await page.click('#filter-form button[type="submit"]');
      await page.waitForSelector(".character");
      await page.locator(".character button").first().click();
      const favoriteName = await text(page, ".character h2 >> nth=0");
      await page.reload();
      await page.waitForSelector(".character");
      await page.check("#only-favorites");
      assert.equal(await page.locator(".character").count(), 1);
      assert.equal(await text(page, ".character h2"), favoriteName);
      await page.locator(".character button").click();
      assert.match(await text(page, "#status"), /Nenhum favorito/);
    },
    { prepare: (page) => stubSuccess(page, "**/rickandmortyapi.com/**", STUB_CHARACTERS) },
  ));

test("50 favoritos tratam busca vazia e erro da API", async () => {
  await lab.open(
    "apis/50-aplicacao-favoritos",
    async (page) => {
      await page.waitForFunction(() => document.querySelector("#status").textContent.includes("Nenhum personagem"));
    },
    { prepare: (page) => page.route("**/rickandmortyapi.com/**", (route) => fulfillJson(route, { error: "x" }, 404)) },
  );
  await lab.open(
    "apis/50-aplicacao-favoritos",
    async (page) => {
      await page.waitForSelector(".status--error");
    },
    { prepare: (page) => page.route("**/rickandmortyapi.com/**", (route) => fulfillJson(route, {}, 500)) },
  );
});
