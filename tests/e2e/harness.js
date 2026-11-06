"use strict";

const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const { chromium } = require("playwright-core");

const JS_ROOT = path.resolve(__dirname, "../../javascript");
const LIVE_API = process.env.LIVE_API === "1";
const CONTENT_TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".svg": "image/svg+xml",
};

function startServer() {
  const server = http.createServer((request, response) => {
    const urlPath = decodeURIComponent(new URL(request.url, "http://localhost").pathname);
    const filePath = path.join(JS_ROOT, urlPath.endsWith("/") ? `${urlPath}index.html` : urlPath);
    if (!filePath.startsWith(JS_ROOT) || !fs.existsSync(filePath)) {
      response.writeHead(urlPath === "/favicon.ico" ? 204 : 404).end();
      return;
    }
    const contentType = CONTENT_TYPES[path.extname(filePath)] ?? "application/octet-stream";
    response.writeHead(200, { "Content-Type": contentType });
    fs.createReadStream(filePath).pipe(response);
  });
  return new Promise((resolve) => {
    server.listen(0, "127.0.0.1", () => resolve(server));
  });
}

function fulfillJson(route, json, status = 200) {
  return route.fulfill({
    status,
    contentType: "application/json",
    headers: { "Access-Control-Allow-Origin": "*" },
    body: JSON.stringify(json),
  });
}

class Lab {
  async start() {
    this.server = await startServer();
    this.baseUrl = `http://127.0.0.1:${this.server.address().port}`;
    this.browser = await chromium.launch({ channel: process.env.PW_CHANNEL ?? "chrome" });
  }

  async stop() {
    await this.browser?.close();
    this.server?.close();
  }

  // Opens one exercise in a clean context and fails on any uncaught page error.
  async open(folder, run, { contextOptions = {}, prepare } = {}) {
    const context = await this.browser.newContext(contextOptions);
    const page = await context.newPage();
    const pageErrors = [];
    page.on("pageerror", (error) => pageErrors.push(error.message));
    try {
      await prepare?.(page);
      await page.goto(`${this.baseUrl}/${folder}/`);
      await run(page);
      if (pageErrors.length > 0) {
        throw new Error(`Page errors: ${pageErrors.join(" | ")}`);
      }
    } finally {
      await context.close();
    }
  }
}

// Replaces a happy-path response with a fixture, unless LIVE_API=1 asks for the real API.
function stubSuccess(page, pattern, json) {
  return LIVE_API ? Promise.resolve() : page.route(pattern, (route) => fulfillJson(route, json));
}

module.exports = { Lab, LIVE_API, fulfillJson, stubSuccess };
