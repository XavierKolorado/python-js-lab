# Guia de JavaScript / JavaScript guide

[Voltar ao README / Back to the README](../README.md)

## Preparar o ambiente / Set up

Requer Node.js 22 ou mais recente. Os exercícios não têm dependências. A única dependência de desenvolvimento é `playwright-core`, usada nos testes de navegador.
*Requires Node.js 22 or newer. Exercises have no dependencies. The only development dependency is `playwright-core`, used by the browser tests.*

```bash
npm install
```

## Exercícios de terminal (01 a 30) / Terminal exercises (01 to 30)

```bash
node javascript/fundamentos/04-media-notas.js 7 8.5 9
```

A entrada vem de argumentos, o que deixa os exemplos curtos e fáceis de testar. Cada arquivo exporta suas funções e só executa `main()` quando é chamado diretamente.
*Input comes from arguments, which keeps examples short and testable. Each file exports its functions and runs `main()` only when called directly.*

No Git Bash para Windows, um `/` isolado vira um caminho. Use `MSYS_NO_PATHCONV=1` no exercício 03 ou rode pelo PowerShell.
*On Git Bash for Windows, a lone `/` turns into a path. Use `MSYS_NO_PATHCONV=1` for exercise 03 or run it from PowerShell.*

## Projetos de navegador (31 a 50) / Browser projects (31 to 50)

Cada pasta tem `index.html`, `style.css`, `script.js` e `README.md`. Sirva a raiz do repositório:
*Each folder has `index.html`, `style.css`, `script.js` and `README.md`. Serve the repository root:*

```bash
python -m http.server 8000
```

Depois abra, por exemplo, `http://localhost:8000/javascript/dom/36-calculadora-visual/`.
*Then open, for example, `http://localhost:8000/javascript/dom/36-calculadora-visual/`.*

## Padrão dos projetos / Project pattern

- Dados vindos de APIs entram na página por `textContent`, nunca por `innerHTML`, o que evita injeção de HTML. / *API data reaches the page through `textContent`, never `innerHTML`, which prevents HTML injection.*
- Cada `style.css` traz a mesma base visual, para que a pasta funcione sozinha. / *Each `style.css` carries the same visual base, so the folder works alone.*
- Todo `fetch` tem tempo limite e confere `response.ok`. / *Every `fetch` has a timeout and checks `response.ok`.*

## Login demonstrativo / Demo login

O exercício 42 não é segurança real. Código de navegador pode ser lido e alterado por qualquer pessoa, então a senha de exemplo é pública e a verificação pode ser contornada. Autenticação de verdade acontece no servidor.
*Exercise 42 is not real security. Anyone can read and change browser code, so the sample password is public and the check can be bypassed. Real authentication happens on the server.*

## Testes / Tests

```bash
npm test
```

```bash
npm run test:e2e
```

Os testes de navegador usam o Google Chrome instalado. Para usar o Edge, defina `PW_CHANNEL=msedge`. Por padrão, as respostas das APIs são simuladas; `npm run test:e2e:live` usa as APIs reais.
*Browser tests use the installed Google Chrome. To use Edge, set `PW_CHANNEL=msedge`. API responses are simulated by default; `npm run test:e2e:live` uses the real APIs.*
