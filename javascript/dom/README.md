<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# JavaScript, nível 4: DOM e interação com páginas

*JavaScript, level 4: DOM and page interaction*

[Voltar ao README principal / Back to the main README](../../README.md)

- [31. Contador interativo](31-contador-interativo/)
- [32. Lista de tarefas](32-lista-tarefas/)
- [33. Formulário validado](33-formulario-validado/)
- [34. Menu responsivo](34-menu-responsivo/)
- [35. Tema claro e escuro](35-tema-claro-escuro/)
- [36. Calculadora visual](36-calculadora-visual/)
- [37. Modal](37-modal/)
- [38. Galeria de imagens](38-galeria-imagens/)
- [39. Pesquisa em tempo real](39-pesquisa-tempo-real/)
- [40. Cronômetro](40-cronometro/)

## 31. Contador interativo / Interactive counter

**Problema:** Criar botões para incrementar, decrementar e zerar um contador.  
**Problem:** Create buttons to increment, decrement and reset a counter.

**Objetivo:** Selecionar elementos e reagir a cliques.  
**Goal:** Select elements and react to clicks.

**Conceitos / Concepts:** `querySelector`, `addEventListener`, `textContent`

**Arquivo / File:** [`31-contador-interativo`](./31-contador-interativo)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/31-contador-interativo/`

**Resultado esperado:** O número muda a cada clique.  
**Expected result:** The number changes on each click.

## 32. Lista de tarefas / To-do list

**Problema:** Adicionar, concluir e remover tarefas.  
**Problem:** Add, complete and remove tasks.

**Objetivo:** Renderizar uma lista a partir do estado.  
**Goal:** Render a list from state.

**Conceitos / Concepts:** `createElement`, `replaceChildren`, formulários

**Arquivo / File:** [`32-lista-tarefas`](./32-lista-tarefas)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/32-lista-tarefas/`

**Resultado esperado:** Tarefas aparecem, são riscadas e somem. Texto vazio é recusado.  
**Expected result:** Tasks appear, get crossed out and disappear. Blank text is refused.

## 33. Formulário validado / Validated form

**Problema:** Criar um formulário com validação de campos.  
**Problem:** Build a form with field validation.

**Objetivo:** Validar por campo e informar erros com acessibilidade.  
**Goal:** Validate per field and report errors accessibly.

**Conceitos / Concepts:** `FormData`, regex, `aria-invalid`

**Arquivo / File:** [`33-formulario-validado`](./33-formulario-validado)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/33-formulario-validado/`

**Resultado esperado:** Mensagens por campo e sucesso quando tudo está válido.  
**Expected result:** Per-field messages and success when all is valid.

## 34. Menu responsivo / Responsive menu

**Problema:** Criar um menu de navegação que funcione em dispositivos móveis.  
**Problem:** Build a navigation menu that works on mobile.

**Objetivo:** Combinar media queries e estado acessível.  
**Goal:** Combine media queries and accessible state.

**Conceitos / Concepts:** `@media`, `aria-expanded`, teclado

**Arquivo / File:** [`34-menu-responsivo`](./34-menu-responsivo)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/34-menu-responsivo/`

**Resultado esperado:** Barra no desktop e painel no celular. Esc fecha.  
**Expected result:** A bar on desktop and a panel on mobile. Esc closes it.

## 35. Tema claro e escuro / Light and dark theme

**Problema:** Criar um alternador de temas.  
**Problem:** Build a theme switcher.

**Objetivo:** Usar variáveis CSS e a preferência do sistema.  
**Goal:** Use CSS variables and the system preference.

**Conceitos / Concepts:** variáveis CSS, `matchMedia`, `localStorage`

**Arquivo / File:** [`35-tema-claro-escuro`](./35-tema-claro-escuro)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/35-tema-claro-escuro/`

**Resultado esperado:** O tema alterna e continua salvo ao recarregar.  
**Expected result:** The theme switches and stays saved after reload.

## 36. Calculadora visual / Visual calculator

**Problema:** Criar uma calculadora funcional com interface gráfica.  
**Problem:** Build a working calculator with a graphical interface.

**Objetivo:** Modelar uma máquina de estados, sem `eval`.  
**Goal:** Model a state machine, without `eval`.

**Conceitos / Concepts:** CSS Grid, delegação de eventos, teclado

**Arquivo / File:** [`36-calculadora-visual`](./36-calculadora-visual)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/36-calculadora-visual/`

**Resultado esperado:** Contas encadeadas, mouse e teclado. Divisão por zero mostra Erro.  
**Expected result:** Chained math, mouse and keyboard. Division by zero shows Erro.

## 37. Modal / Modal

**Problema:** Criar uma janela modal que abre e fecha.  
**Problem:** Build a modal window that opens and closes.

**Objetivo:** Usar o elemento nativo `dialog`.  
**Goal:** Use the native `dialog` element.

**Conceitos / Concepts:** `dialog`, `showModal`, `::backdrop`

**Arquivo / File:** [`37-modal`](./37-modal)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/37-modal/`

**Resultado esperado:** Fecha pelo botão, por Esc ou clicando fora.  
**Expected result:** Closes by button, Esc or a click outside.

## 38. Galeria de imagens / Image gallery

**Problema:** Criar uma galeria com filtros e visualização de imagens.  
**Problem:** Build a gallery with filters and an image viewer.

**Objetivo:** Derivar a interface de dados e estado.  
**Goal:** Derive the interface from data and state.

**Conceitos / Concepts:** CSS Grid, `dialog`, SVG, aritmética modular

**Arquivo / File:** [`38-galeria-imagens`](./38-galeria-imagens)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/38-galeria-imagens/`

**Resultado esperado:** Filtros por categoria e visualizador com anterior e próxima.  
**Expected result:** Category filters and a viewer with previous and next.

## 39. Pesquisa em tempo real / Live search

**Problema:** Filtrar elementos conforme o usuário digita.  
**Problem:** Filter items as the user types.

**Objetivo:** Reagir ao evento `input` e destacar sem `innerHTML`.  
**Goal:** React to `input` and highlight without `innerHTML`.

**Conceitos / Concepts:** `input`, `normalize`, `DocumentFragment`

**Arquivo / File:** [`39-pesquisa-tempo-real`](./39-pesquisa-tempo-real)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/39-pesquisa-tempo-real/`

**Resultado esperado:** A lista diminui a cada tecla e o termo fica destacado.  
**Expected result:** The list narrows on each key and the term is highlighted.

## 40. Cronômetro / Stopwatch

**Problema:** Implementar iniciar, pausar e zerar.  
**Problem:** Implement start, pause and reset.

**Objetivo:** Medir tempo sem acumular erro dos temporizadores.  
**Goal:** Measure time without accumulating timer drift.

**Conceitos / Concepts:** `performance.now`, `setInterval`, estado

**Arquivo / File:** [`40-cronometro`](./40-cronometro)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/40-cronometro/`

**Resultado esperado:** O tempo corre, pausa, retoma e zera.  
**Expected result:** Time runs, pauses, resumes and resets.
