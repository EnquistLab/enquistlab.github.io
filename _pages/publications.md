---
layout: page
permalink: /publications/
title: publications
description: Publications, CV, and external scholarly profiles.
nav: true
nav_order: 5
---

## Publications and CV

- [Google Scholar profile](https://scholar.google.com/citations?user=mAbA6EoAAAAJ&hl=en)
- [ResearchGate profile](https://www.researchgate.net/profile/Brian-Enquist)
- Full CV: [View the CV page]({{ '/cv/' | relative_url }})

---

## Complete Publication List

Use the tabs to group papers by subject area, or use the search box to filter within the active group.

<div class="publication-topic-toolbar">
	<div id="publication-topic-tabs" class="publication-topic-tabs" role="tablist" aria-label="Publication subject areas"></div>
	<p class="publication-topic-caption">Select a subject area to view matching papers chronologically, then search within that active view.</p>
</div>

{% include bib_search.liquid %}

<p id="publication-topic-empty" class="publication-topic-empty" hidden>No publications match the current subject tab and search query.</p>

<div id="full-publication-list">
{% include publications_full_from_doc.md %}
</div>

<style>
	.publication-topic-toolbar {
		margin: 1.5rem 0 1rem;
	}

	.publication-topic-tabs {
		display: flex;
		flex-wrap: wrap;
		gap: 0.65rem;
		margin-bottom: 0.75rem;
	}

	.publication-topic-tab {
		appearance: none;
		border: 1px solid var(--global-divider-color);
		background: linear-gradient(180deg, var(--global-card-bg-color) 0%, color-mix(in srgb, var(--global-card-bg-color) 88%, var(--global-theme-color) 12%) 100%);
		border-radius: 999px;
		color: var(--global-text-color);
		cursor: pointer;
		font: inherit;
		line-height: 1.2;
		padding: 0.6rem 0.95rem;
		transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.2s ease;
	}

	.publication-topic-tab:hover,
	.publication-topic-tab:focus-visible {
		border-color: var(--global-theme-color);
		color: var(--global-theme-color);
		outline: none;
		transform: translateY(-1px);
	}

	.publication-topic-tab.is-active {
		background: var(--global-theme-color);
		border-color: var(--global-theme-color);
		color: var(--global-card-bg-color);
	}

	.publication-topic-count {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		min-width: 1.65rem;
		height: 1.65rem;
		margin-left: 0.45rem;
		padding: 0 0.45rem;
		border-radius: 999px;
		background: color-mix(in srgb, var(--global-theme-color) 16%, transparent);
		font-size: 0.82rem;
		font-weight: 600;
	}

	.publication-topic-tab.is-active .publication-topic-count {
		background: color-mix(in srgb, var(--global-card-bg-color) 22%, transparent);
	}

	.publication-topic-caption {
		margin: 0;
		color: var(--global-text-color-light);
		font-size: 0.98rem;
	}

	.publication-topic-empty {
		display: inline-block;
		margin: 0 0 1rem;
		padding: 0.7rem 0.9rem;
		border-left: 3px solid var(--global-theme-color);
		background: color-mix(in srgb, var(--global-theme-color) 10%, transparent);
		color: var(--global-text-color);
	}
</style>

<script>
	document.addEventListener('DOMContentLoaded', function () {
		const input = document.getElementById('bibsearch');
		const container = document.getElementById('full-publication-list');
		const tabsContainer = document.getElementById('publication-topic-tabs');
		const emptyState = document.getElementById('publication-topic-empty');
		if (!input || !container || !tabsContainer || !emptyState) return;

		input.placeholder = 'Type to filter complete publication list';

		const topicDefinitions = [
			{ id: 'all', label: 'All', threshold: 0, matchers: [] },
			{
				id: 'macroecology',
				label: 'Macroecology',
				threshold: 2,
				matchers: [
					{ pattern: /macroecolog/i, weight: 3 },
					{ pattern: /biogeograph/i, weight: 2 },
					{ pattern: /latitudinal/i, weight: 2 },
					{ pattern: /range size/i, weight: 2 },
					{ pattern: /species richness/i, weight: 2 },
					{ pattern: /rarity/i, weight: 1 },
					{ pattern: /broad geographic/i, weight: 2 },
					{ pattern: /continental/i, weight: 1 },
				],
			},
			{
				id: 'metabolic-scaling-allometry',
				label: 'Metabolic Scaling and Allometry',
				threshold: 2,
				matchers: [
					{ pattern: /allometr/i, weight: 3 },
					{ pattern: /metabolic/i, weight: 2 },
					{ pattern: /scaling/i, weight: 1 },
					{ pattern: /body size/i, weight: 2 },
					{ pattern: /biomass allocation/i, weight: 2 },
					{ pattern: /quarter-power/i, weight: 3 },
					{ pattern: /stoichiometr/i, weight: 1 },
				],
			},
			{
				id: 'trait-based-ecology',
				label: 'Trait-based Ecology',
				threshold: 2,
				matchers: [
					{ pattern: /trait-based/i, weight: 3 },
					{ pattern: /functional trait/i, weight: 3 },
					{ pattern: /leaf economics/i, weight: 2 },
					{ pattern: /trait variation/i, weight: 2 },
					{ pattern: /trait diversity/i, weight: 2 },
					{ pattern: /phenotypic distribution/i, weight: 2 },
					{ pattern: /intraspecific variation/i, weight: 1 },
					{ pattern: /leaf mass per area/i, weight: 1 },
					{ pattern: /\btraits\b/i, weight: 1 },
				],
			},
			{
				id: 'ecophysiology',
				label: 'Ecophysiology',
				threshold: 2,
				matchers: [
					{ pattern: /\bflux\b|\bfluxes\b/i, weight: 2 },
					{ pattern: /hydraulic/i, weight: 2 },
					{ pattern: /photosynth/i, weight: 2 },
					{ pattern: /respiration/i, weight: 2 },
					{ pattern: /drought/i, weight: 1 },
					{ pattern: /thermoregulation/i, weight: 2 },
					{ pattern: /stoichiometr/i, weight: 2 },
					{ pattern: /carbon economics/i, weight: 2 },
					{ pattern: /carbon exchange/i, weight: 2 },
					{ pattern: /primary productivity/i, weight: 1 },
					{ pattern: /water relations/i, weight: 2 },
					{ pattern: /physiolog/i, weight: 1 },
				],
			},
			{
				id: 'functional-ecology',
				label: 'Functional Ecology',
				threshold: 2,
				matchers: [
					{ pattern: /functional diversity/i, weight: 3 },
					{ pattern: /functional composition/i, weight: 3 },
					{ pattern: /community assembly/i, weight: 2 },
					{ pattern: /ecosystem function/i, weight: 2 },
					{ pattern: /ecological function/i, weight: 2 },
					{ pattern: /distinctiveness/i, weight: 1 },
					{ pattern: /evenness/i, weight: 1 },
				],
			},
			{
				id: 'tropical-ecology',
				label: 'Tropical Ecology',
				threshold: 2,
				matchers: [
					{ pattern: /tropical/i, weight: 2 },
					{ pattern: /amazon/i, weight: 2 },
					{ pattern: /neotropical/i, weight: 2 },
					{ pattern: /andes-amazon/i, weight: 2 },
					{ pattern: /tropical forest/i, weight: 3 },
					{ pattern: /dry forest/i, weight: 2 },
					{ pattern: /montane cloud forest/i, weight: 2 },
				],
			},
			{
				id: 'arctic-alpine',
				label: 'Arctic and Alpine',
				threshold: 2,
				matchers: [
					{ pattern: /arctic/i, weight: 2 },
					{ pattern: /alpine/i, weight: 2 },
					{ pattern: /tundra/i, weight: 2 },
					{ pattern: /svalbard/i, weight: 2 },
					{ pattern: /subalpine/i, weight: 2 },
					{ pattern: /afromontane/i, weight: 1 },
				],
			},
			{
				id: 'biodiversity-informatics',
				label: 'Biodiversity Informatics',
				threshold: 2,
				matchers: [
					{ pattern: /biodiversity informatics/i, weight: 3 },
					{ pattern: /\bBIEN\b/i, weight: 3 },
					{ pattern: /database/i, weight: 2 },
					{ pattern: /databases/i, weight: 2 },
					{ pattern: /metadata/i, weight: 2 },
					{ pattern: /occurrence data/i, weight: 2 },
					{ pattern: /reproducible workflow/i, weight: 2 },
					{ pattern: /name resolution/i, weight: 3 },
					{ pattern: /cyberinfrastructure/i, weight: 2 },
					{ pattern: /informatics/i, weight: 2 },
				],
			},
		];

		let activeTopic = 'all';

		const yearHeaders = Array.from(container.querySelectorAll('p')).filter((p) => {
			const t = p.textContent.trim();
			return /^\d{4}$/.test(t) || /^\d{4}\s*-\s*\d{4}$/.test(t);
		});

		const yearSections = yearHeaders.map((header) => {
			const lists = [];
			let node = header.nextElementSibling;
			while (
				node &&
				!(
					node.tagName === 'P' &&
					(/^[0-9]{4}$/.test(node.textContent.trim()) ||
						/^[0-9]{4}\s*-\s*[0-9]{4}$/.test(node.textContent.trim()))
				)
			) {
				if (node.tagName === 'OL' || node.tagName === 'UL') {
					lists.push(node);
				}
				node = node.nextElementSibling;
			}

			const items = lists.flatMap((list) => Array.from(list.children).filter((child) => child.tagName === 'LI'));
			return { header, lists, items };
		});

		function scoreTopic(text, topic) {
			return topic.matchers.reduce((score, matcher) => {
				return matcher.pattern.test(text) ? score + matcher.weight : score;
			}, 0);
		}

		function classifyPublication(text) {
			return topicDefinitions
				.filter((topic) => topic.id !== 'all')
				.filter((topic) => scoreTopic(text, topic) >= topic.threshold)
				.map((topic) => topic.id);
		}

		const allItems = yearSections.flatMap((section) => section.items);
		const topicCounts = { all: allItems.length };
		topicDefinitions.forEach((topic) => {
			if (topic.id !== 'all') topicCounts[topic.id] = 0;
		});

		allItems.forEach((li) => {
			const normalizedText = li.textContent.toLowerCase().replace(/\s+/g, ' ').trim();
			const topics = classifyPublication(normalizedText);
			li.dataset.topics = topics.join('|');
			topics.forEach((topicId) => {
				topicCounts[topicId] += 1;
			});
		});

		const tabButtons = topicDefinitions.map((topic) => {
			const button = document.createElement('button');
			button.type = 'button';
			button.className = 'publication-topic-tab';
			button.id = `publication-topic-tab-${topic.id}`;
			button.setAttribute('role', 'tab');
			button.setAttribute('aria-selected', topic.id === activeTopic ? 'true' : 'false');
			button.dataset.topic = topic.id;
			button.innerHTML = `${topic.label}<span class="publication-topic-count">${topicCounts[topic.id] || 0}</span>`;
			button.addEventListener('click', function () {
				activeTopic = topic.id;
				tabButtons.forEach((tabButton) => {
					const isActive = tabButton.dataset.topic === activeTopic;
					tabButton.classList.toggle('is-active', isActive);
					tabButton.setAttribute('aria-selected', isActive ? 'true' : 'false');
				});
				applyFilter();
			});
			tabsContainer.appendChild(button);
			return button;
		});

		tabButtons.forEach((tabButton) => {
			const isActive = tabButton.dataset.topic === activeTopic;
			tabButton.classList.toggle('is-active', isActive);
		});

		function itemMatchesTopic(li) {
			if (activeTopic === 'all') return true;
			const topics = li.dataset.topics ? li.dataset.topics.split('|').filter(Boolean) : [];
			return topics.includes(activeTopic);
		}

		function applyFilter() {
			const query = input.value.trim().toLowerCase();
			let visibleTotal = 0;

			yearSections.forEach((section) => {
				let visibleCount = 0;

				section.items.forEach((li) => {
					const text = li.textContent.toLowerCase();
					const matchesQuery = query === '' || text.includes(query);
					const matchesTopic = itemMatchesTopic(li);
					const match = matchesQuery && matchesTopic;
					li.style.display = match ? '' : 'none';
					if (match) {
						visibleCount += 1;
						visibleTotal += 1;
					}
				});

				section.header.style.display = visibleCount > 0 ? '' : 'none';
				section.lists.forEach((list) => {
					list.style.display = visibleCount > 0 ? '' : 'none';
				});
			});

			emptyState.hidden = visibleTotal !== 0;
		}

		input.addEventListener('input', applyFilter);
		applyFilter();
	});
</script>
