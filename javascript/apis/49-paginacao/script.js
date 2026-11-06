"use strict";

const TOTAL_ITEMS = 53;
const ITEMS = Array.from({ length: TOTAL_ITEMS }, (_, index) => `Registro ${index + 1}`);

const pageSizeSelect = document.querySelector("#page-size");
const itemList = document.querySelector("#item-list");
const pageButtons = document.querySelector("#page-buttons");
const previousButton = document.querySelector("#previous-page");
const nextButton = document.querySelector("#next-page");
const pageInfo = document.querySelector("#page-info");

let currentPage = 1;

function paginate(items, page, pageSize) {
  const totalPages = Math.max(1, Math.ceil(items.length / pageSize));
  const safePage = Math.min(Math.max(page, 1), totalPages);
  const start = (safePage - 1) * pageSize;
  return { page: safePage, totalPages, start, pageItems: items.slice(start, start + pageSize) };
}

function createPageButton(pageNumber, isCurrent) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "btn btn--ghost";
  button.textContent = pageNumber;
  if (isCurrent) {
    button.setAttribute("aria-current", "page");
  }
  button.addEventListener("click", () => goToPage(pageNumber));
  return button;
}

function goToPage(page) {
  currentPage = page;
  render();
}

function render() {
  const pageSize = Number(pageSizeSelect.value);
  const { page, totalPages, start, pageItems } = paginate(ITEMS, currentPage, pageSize);
  currentPage = page;
  itemList.replaceChildren(
    ...pageItems.map((text) => {
      const item = document.createElement("li");
      item.textContent = text;
      return item;
    }),
  );
  pageButtons.replaceChildren(
    ...Array.from({ length: totalPages }, (_, index) => createPageButton(index + 1, index + 1 === page)),
  );
  previousButton.disabled = page === 1;
  nextButton.disabled = page === totalPages;
  pageInfo.textContent = `Exibindo ${start + 1} a ${start + pageItems.length} de ${ITEMS.length}`;
}

previousButton.addEventListener("click", () => goToPage(currentPage - 1));
nextButton.addEventListener("click", () => goToPage(currentPage + 1));
pageSizeSelect.addEventListener("change", () => goToPage(1));

render();
