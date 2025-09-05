let grid = document.querySelector(".grid")

// use a fragment for performance
let fragment = document.createDocumentFragment();

for (let i = 1; i <= 4681; i++) {
    let button = document.createElement("button");
    button.textContent = String(i); // numbers start at 1
    button.dataset.idx = String(i - 1); // zero-based index
    fragment.appendChild(button);
}

grid.appendChild(fragment);

// --- Hover highlighting logic ---
const NUM_COLS = 52;
let buttons = Array.from(grid.children);
let lastHoveredIndex = null;

function clearHighlights() {
    if (!buttons.length) return;
    for (let btn of buttons) {
        btn.classList.remove("is-hovered", "is-row-highlight", "is-col-highlight");
    }
}

function highlightFor(index) {
    if (index == null || index < 0 || index >= buttons.length) return;
    const hovered = buttons[index];
    const row = Math.floor(index / NUM_COLS);
    const col = index % NUM_COLS;

    // highlight row
    const rowStart = row * NUM_COLS;
    for (let c = 0; c < NUM_COLS; c++) {
        const idx = rowStart + c;
        if (idx >= buttons.length) break;
        if (idx === index) continue; // hovered gets darker style separately
        buttons[idx].classList.add("is-row-highlight");
    }

    // highlight column
    for (let r = 0; ; r++) {
        const idx = r * NUM_COLS + col;
        if (idx >= buttons.length) break;
        if (idx === index) continue;
        buttons[idx].classList.add("is-col-highlight");
    }

    // hovered button
    hovered.classList.add("is-hovered");
}

grid.addEventListener("mouseover", (e) => {
    const target = e.target;
    if (!(target instanceof HTMLButtonElement)) return;
    const idx = Number(target.dataset.idx);
    if (idx === lastHoveredIndex) return;
    clearHighlights();
    highlightFor(idx);
    lastHoveredIndex = idx;
});

grid.addEventListener("mouseleave", () => {
    clearHighlights();
    lastHoveredIndex = null;
});
