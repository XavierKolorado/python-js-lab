"use strict";

const fs = require("node:fs");
const path = require("node:path");

const JS_ROOT = path.resolve(__dirname, "../../javascript");

function load(category, number) {
  const prefix = `${String(number).padStart(2, "0")}-`;
  const directory = path.join(JS_ROOT, category);
  const file = fs.readdirSync(directory).find((name) => name.startsWith(prefix));
  return require(path.join(directory, file));
}

module.exports = { load, JS_ROOT };
