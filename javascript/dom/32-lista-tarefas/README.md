<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 32. Lista de tarefas / To-do list

**Problema:** Adicionar, concluir e remover tarefas.  
**Problem:** Add, complete and remove tasks.

**Objetivo:** Renderizar uma lista a partir do estado.  
**Goal:** Render a list from state.

**Conceitos / Concepts:** `createElement`, `replaceChildren`, formulários

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/32-lista-tarefas/`

**Resultado esperado:** Tarefas aparecem, são riscadas e somem. Texto vazio é recusado.  
**Expected result:** Tasks appear, get crossed out and disappear. Blank text is refused.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>32. Lista de tarefas</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Lista de tarefas</h1>
      <form id="task-form" class="task-form">
        <input id="task-input" aria-label="Nova tarefa" placeholder="O que precisa ser feito?" maxlength="120" />
        <button class="btn" type="submit">Adicionar</button>
      </form>
      <p id="form-error" class="status status--error" role="alert"></p>
      <ul id="task-list" class="task-list"></ul>
      <p id="task-summary" class="muted"></p>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const taskForm = document.querySelector("#task-form");
const taskInput = document.querySelector("#task-input");
const taskList = document.querySelector("#task-list");
const formError = document.querySelector("#form-error");
const taskSummary = document.querySelector("#task-summary");

let tasks = [];
let nextTaskId = 1;

function createTaskElement(task) {
  const item = document.createElement("li");
  item.className = `task-item${task.done ? " task-item--done" : ""}`;

  const label = document.createElement("label");
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = task.done;
  checkbox.addEventListener("change", () => toggleTask(task.id));
  const title = document.createElement("span");
  title.textContent = task.title;
  label.append(checkbox, title);

  const removeButton = document.createElement("button");
  removeButton.type = "button";
  removeButton.className = "btn btn--danger";
  removeButton.textContent = "Remover";
  removeButton.addEventListener("click", () => removeTask(task.id));

  item.append(label, removeButton);
  return item;
}

function render() {
  taskList.replaceChildren(...tasks.map(createTaskElement));
  const pending = tasks.filter((task) => !task.done).length;
  taskSummary.textContent = tasks.length
    ? `${pending} pendente(s) de ${tasks.length}`
    : "Nenhuma tarefa por aqui.";
}

function toggleTask(id) {
  tasks = tasks.map((task) => (task.id === id ? { ...task, done: !task.done } : task));
  render();
}

function removeTask(id) {
  tasks = tasks.filter((task) => task.id !== id);
  render();
}

taskForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const title = taskInput.value.trim();
  if (!title) {
    formError.textContent = "Digite o nome da tarefa.";
    return;
  }
  formError.textContent = "";
  tasks.push({ id: nextTaskId, title, done: false });
  nextTaskId += 1;
  taskForm.reset();
  taskInput.focus();
  render();
});

render();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
