import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { createContext, runInContext, Script } from "node:vm";

const page = readFileSync(new URL("../_pages/publications.html", import.meta.url), "utf8");
const script = page.match(/<script>\s*([\s\S]*?)<\/script>/)[1];
new Script(script);
const filter = script.slice(script.indexOf("function applyFilter()"), script.indexOf("function debounce("));
const topicClick = script.match(/button\.addEventListener\("click", function \(\) \{([\s\S]*?)\n\s*\}\);\n\s*tabsContainer/)[1];
const clearClick = script.match(/clearBtn\.addEventListener\("click", function \(\) \{([\s\S]*?)\n\s*\}\);/)[1];

function fixture() {
  const records = [
    ["forest traits alpha", ["traits"]],
    ["forest carbon beta", ["carbon"]],
    ["alpine traits gamma", ["traits"]],
  ];
  const items = records.map(() => ({ style: {} }));
  const yearSections = items.map((item) => ({ items: [item], header: { style: {} }, lists: [{ style: {} }] }));
  const tabButtons = ["all", "traits", "carbon"].map((id) => ({
    dataset: { topic: id },
    attributes: {},
    classList: {
      toggle(name, enabled) {
        this[name] = enabled;
      },
    },
    setAttribute(name, value) {
      this.attributes[name] = value;
    },
  }));
  const context = createContext({
    activeTopic: "all",
    input: {
      value: "",
      focus() {
        this.focused = true;
      },
    },
    clearBtn: { hidden: true },
    resultCount: {},
    emptyState: {},
    yearSections,
    itemCache: new Map(items.map((item, index) => [item, { text: records[index][0], topicSet: new Set(records[index][1]) }])),
    navItems: items.map((item, index) => ({ dataset: { navYear: String(2026 - index) } })),
    sectionByYear: new Map(yearSections.map((section, index) => [`year-${2026 - index}`, section])),
    topicDefinitions: ["all", "traits", "carbon"].map((id) => ({ id, label: id })),
    tabButtons,
  });
  runInContext(filter, context);
  return { context, items, apply: () => runInContext("applyFilter()", context) };
}

test("query AND selected topic; all query words are required, case-insensitively", () => {
  const { context, items, apply } = fixture();
  context.activeTopic = "traits";
  context.input.value = "  FOREST  alpha ";
  apply();
  assert.deepEqual(
    items.map((item) => item.style.display),
    ["", "none", "none"]
  );
  assert.match(context.resultCount.textContent, /^1 paper in traits/);
  assert.equal(context.emptyState.hidden, true);
  assert.equal(context.clearBtn.hidden, false);
});

test("changing topic preserves query and updates a single pressed selection", () => {
  const { context, items } = fixture();
  context.input.value = "forest";
  context.topic = { id: "carbon" };
  runInContext(topicClick, context);
  assert.equal(context.input.value, "forest");
  assert.deepEqual(
    items.map((item) => item.style.display),
    ["none", "", "none"]
  );
  assert.deepEqual(
    context.tabButtons.map((button) => button.attributes["aria-pressed"]),
    ["false", "false", "true"]
  );
  assert.equal(context.tabButtons.filter((button) => button.classList["is-active"]).length, 1);
});

test("empty results hide year headings, lists and year links", () => {
  const { context, items, apply } = fixture();
  context.input.value = "unmatched";
  apply();
  assert.ok(items.every((item) => item.style.display === "none"));
  assert.ok(context.yearSections.every((section) => section.header.style.display === "none" && section.lists[0].style.display === "none"));
  assert.ok(context.navItems.every((item) => item.hidden));
  assert.equal(context.emptyState.hidden, false);
  assert.match(context.resultCount.textContent, /^0 papers/);
});

test("clear resets only query, restores topic results and returns input focus", () => {
  const { context, items, apply } = fixture();
  context.activeTopic = "traits";
  context.input.value = "unmatched";
  apply();
  runInContext(clearClick, context);
  assert.equal(context.input.value, "");
  assert.equal(context.activeTopic, "traits");
  assert.deepEqual(
    items.map((item) => item.style.display),
    ["", "none", ""]
  );
  assert.equal(context.clearBtn.hidden, true);
  assert.equal(context.input.focused, true);
  assert.equal(context.emptyState.hidden, true);
  assert.match(context.resultCount.textContent, /^2 papers in traits/);
});

test("all topic restores the complete list without a query", () => {
  const { context, items, apply } = fixture();
  apply();
  assert.ok(items.every((item) => item.style.display === ""));
  assert.equal(context.resultCount.textContent, "3 papers in all.");
});

test("filters use native button semantics and an accessible live result status", () => {
  assert.match(page, /role="group" aria-label="Filter by research theme"/);
  assert.match(script, /button\.type = "button"/);
  assert.doesNotMatch(script, /aria-selected|setAttribute\("role", "tab"\)/);
  assert.match(page, /id="pub-search-count" role="status" aria-live="polite"/);
  assert.match(page, /aria-label="Clear publication search"/);
});
