(() => {
  const path = window.location.pathname.replace(/\/+$/, "") || "/";
  if (path === "/") return;

  const nav = document.querySelector(".section-jump-nav");
  if (!nav) return;

  const article = document.querySelector(".post article");
  if (!article) return;

  const source = article.querySelector(".clearfix") || article;
  const headings = [...source.querySelectorAll("h2, h3")].filter((el) => {
    if (!el.textContent || !el.textContent.trim()) return false;
    if (el.closest(".home-cards, .team-grid, .resource-link-grid")) return false;
    return true;
  });

  if (headings.length < 2) {
    nav.remove();
    return;
  }

  const usedIds = new Set(
    [...document.querySelectorAll("[id]")]
      .map((el) => el.id)
      .filter(Boolean)
  );

  const slugify = (text) =>
    text
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9\s-]/g, "")
      .replace(/\s+/g, "-")
      .replace(/-+/g, "-")
      .replace(/^-|-$/g, "");

  headings.forEach((h, i) => {
    if (!h.id) {
      const base = slugify(h.textContent) || `section-${i + 1}`;
      let id = base;
      let n = 2;
      while (usedIds.has(id)) {
        id = `${base}-${n}`;
        n += 1;
      }
      h.id = id;
      usedIds.add(id);
    }
  });

  const header = document.createElement("div");
  header.className = "section-jump-nav__header";
  const label = document.createElement("span");
  label.className = "section-jump-nav__label";
  label.textContent = "On this page";
  header.appendChild(label);
  nav.appendChild(header);

  const linksRow = document.createElement("div");
  linksRow.className = "section-jump-nav__links";
  headings.forEach((h) => {
    const a = document.createElement("a");
    a.className = "section-jump-nav__link";
    if (h.tagName && h.tagName.toLowerCase() === "h3") {
      a.classList.add("section-jump-nav__link--subsection");
    }
    a.href = `#${h.id}`;
    a.textContent = h.textContent.trim();
    linksRow.appendChild(a);
  });
  nav.appendChild(linksRow);
})();
