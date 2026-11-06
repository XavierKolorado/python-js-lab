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
