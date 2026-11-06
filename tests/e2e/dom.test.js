"use strict";

const assert = require("node:assert/strict");
const { after, before, test } = require("node:test");
const { Lab } = require("./harness");

const lab = new Lab();
before(() => lab.start());
after(() => lab.stop());

const text = (page, selector) => page.locator(selector).innerText();

test("31 contador incrementa, decrementa e zera", () =>
  lab.open("dom/31-contador-interativo", async (page) => {
    await page.click("#increment");
    await page.click("#increment");
    await page.click("#decrement");
    assert.equal(await text(page, "#counter-value"), "1");
    await page.click("#reset");
    assert.equal(await text(page, "#counter-value"), "0");
    await page.click("#decrement");
    assert.equal(await text(page, "#counter-value"), "-1");
  }));

test("32 lista adiciona, conclui, remove e recusa vazio", () =>
  lab.open("dom/32-lista-tarefas", async (page) => {
    await page.click("#task-form button");
    assert.match(await text(page, "#form-error"), /Digite/);
    for (const title of ["Estudar", "Praticar"]) {
      await page.fill("#task-input", title);
      await page.press("#task-input", "Enter");
    }
    assert.equal(await page.locator(".task-item").count(), 2);
    await page.locator(".task-item input").first().check();
    assert.equal(await text(page, "#task-summary"), "1 pendente(s) de 2");
    await page.locator(".task-item .btn--danger").first().click();
    assert.equal(await text(page, ".task-item span"), "Praticar");
  }));

test("33 formulário mostra erros e aceita dados válidos", () =>
  lab.open("dom/33-formulario-validado", async (page) => {
    await page.click("#signup-form button");
    assert.match(await text(page, "#form-status"), /Corrija/);
    assert.equal(await page.locator('[aria-invalid="true"]').count(), 5);
    await page.fill('[name="name"]', "Ana");
    await page.fill('[name="email"]', "ana@example.com");
    await page.fill('[name="age"]', "30");
    await page.fill('[name="password"]', "abc12345");
    await page.fill('[name="confirmation"]', "diferente1");
    await page.click("#signup-form button");
    assert.match(await text(page, '[data-error-for="confirmation"]'), /não coincidem/);
    await page.fill('[name="confirmation"]', "abc12345");
    await page.click("#signup-form button");
    assert.match(await text(page, "#form-status"), /sucesso/);
  }));

test("34 menu abre no celular e fica fixo no desktop", async () => {
  await lab.open(
    "dom/34-menu-responsivo",
    async (page) => {
      const firstLink = page.locator("#site-menu a").first();
      assert.equal(await firstLink.isVisible(), false);
      await page.click("#menu-toggle");
      assert.equal(await firstLink.isVisible(), true);
      assert.equal(await page.getAttribute("#menu-toggle", "aria-expanded"), "true");
      await page.keyboard.press("Escape");
      assert.equal(await firstLink.isVisible(), false);
      await page.click("#menu-toggle");
      await firstLink.click();
      assert.equal(await firstLink.isVisible(), false);
    },
    { contextOptions: { viewport: { width: 375, height: 700 } } },
  );
  await lab.open(
    "dom/34-menu-responsivo",
    async (page) => {
      assert.equal(await page.locator("#menu-toggle").isVisible(), false);
      assert.equal(await page.locator("#site-menu a").first().isVisible(), true);
    },
    { contextOptions: { viewport: { width: 1200, height: 700 } } },
  );
});

test("35 tema segue o sistema e guarda a escolha", () =>
  lab.open(
    "dom/35-tema-claro-escuro",
    async (page) => {
      const theme = () => page.evaluate(() => document.documentElement.dataset.theme);
      assert.equal(await theme(), "dark");
      await page.click("#theme-toggle");
      assert.equal(await theme(), "light");
      await page.reload();
      assert.equal(await theme(), "light");
    },
    { contextOptions: { colorScheme: "dark" } },
  ));

test("36 calculadora faz contas, encadeia e trata divisão por zero", () =>
  lab.open("dom/36-calculadora-visual", async (page) => {
    const press = async (keys) => {
      for (const key of keys) {
        await page.keyboard.press(key);
      }
    };
    const display = () => text(page, "#display");
    await page.click('[data-digit="7"]');
    await page.click('[data-operator="*"]');
    await page.click('[data-digit="8"]');
    await page.click('[data-action="equals"]');
    assert.equal(await display(), "56");
    await press(["Escape", "0", ",", "1", "+", "0", ",", "2", "Enter"]);
    assert.equal(await display(), "0,3");
    await press(["Escape", "2", "+", "3", "+", "4", "Enter"]);
    assert.equal(await display(), "9");
    await press(["Escape", "5", "+", "*", "2", "Enter"]);
    assert.equal(await display(), "10");
    await press(["Escape", "5", "/", "0", "Enter"]);
    assert.equal(await display(), "Erro");
    await press(["4"]);
    assert.equal(await display(), "4");
    await press(["Backspace"]);
    assert.equal(await display(), "0");
    await page.click('[data-digit="9"]');
    await page.click('[data-action="sign"]');
    assert.equal(await display(), "-9");
  }));

test("37 modal abre e fecha por botão, Esc e fundo", () =>
  lab.open("dom/37-modal", async (page) => {
    const modal = page.locator("#modal");
    await page.click("#open-modal");
    assert.equal(await modal.isVisible(), true);
    // O evento close do dialog é assíncrono, então o teste espera o texto aparecer.
    const resultIs = (expected) =>
      page.waitForFunction((value) => document.querySelector("#modal-result").textContent === value, expected);
    await page.click('button[value="confirmado"]');
    await resultIs("Resultado: confirmado");
    await page.click("#open-modal");
    await page.keyboard.press("Escape");
    await resultIs("Resultado: fechado");
    assert.equal(await modal.isVisible(), false);
    await page.click("#open-modal");
    await page.mouse.click(5, 5);
    assert.equal(await modal.isVisible(), false);
    await page.click("#open-modal");
    await page.locator("#modal-title").click();
    assert.equal(await modal.isVisible(), true);
  }));

test("38 galeria filtra, carrega imagens e navega", () =>
  lab.open("dom/38-galeria-imagens", async (page) => {
    assert.equal(await page.locator(".gallery-item").count(), 6);
    await page.waitForFunction(() =>
      [...document.images].filter((image) => image.closest(".gallery")).every((image) => image.naturalWidth > 0),
    );
    await page.getByRole("button", { name: "natureza" }).click();
    assert.equal(await page.locator(".gallery-item").count(), 3);
    await page.locator(".gallery-item").first().click();
    assert.equal(await text(page, "#viewer-caption"), "Montanha (1 de 3)");
    await page.click("#previous-image");
    assert.equal(await text(page, "#viewer-caption"), "Mar (3 de 3)");
    await page.click("#next-image");
    assert.equal(await text(page, "#viewer-caption"), "Montanha (1 de 3)");
    await page.click("#close-viewer");
    assert.equal(await page.locator("#viewer").isVisible(), false);
  }));

test("39 pesquisa ignora acentos e destaca o termo", () =>
  lab.open("dom/39-pesquisa-tempo-real", async (page) => {
    assert.equal(await page.locator("#result-list li").count(), 19);
    await page.fill("#search-input", "sao");
    assert.equal(await page.locator("#result-list li").count(), 2);
    assert.equal(await text(page, "#result-list mark >> nth=0"), "São");
    await page.fill("#search-input", "zzz");
    assert.match(await text(page, "#result-count"), /Nenhum/);
  }));

test("40 cronômetro inicia, pausa, retoma e zera", () =>
  lab.open("dom/40-cronometro", async (page) => {
    const display = () => text(page, "#time-display");
    await page.click("#start");
    await page.waitForTimeout(200);
    await page.click("#pause");
    const paused = await display();
    assert.notEqual(paused, "00:00.00");
    await page.waitForTimeout(100);
    assert.equal(await display(), paused);
    await page.click("#start");
    await page.waitForTimeout(100);
    await page.click("#pause");
    assert.ok((await display()) > paused);
    await page.click("#reset");
    assert.equal(await display(), "00:00.00");
    await page.click("#start");
    await page.click("#reset");
    await page.waitForTimeout(80);
    assert.equal(await display(), "00:00.00");
  }));
