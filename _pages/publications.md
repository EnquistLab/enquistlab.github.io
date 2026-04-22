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

Use the search box to filter the complete publication list below.

<input
	type="text"
	id="fullpubsearch"
	spellcheck="false"
	autocomplete="off"
	class="search bibsearch-form-input"
	placeholder="Type to filter complete publication list"
>

<div id="full-publication-list">
{% capture full_publication_markdown %}{% include publications_full_from_doc.md %}{% endcapture %}
{{ full_publication_markdown | markdownify }}
</div>

<script>
	document.addEventListener('DOMContentLoaded', function () {
		const input = document.getElementById('fullpubsearch');
		const container = document.getElementById('full-publication-list');
		if (!input || !container) return;

		const yearHeaders = Array.from(container.querySelectorAll('h3'));

		function applyFilter() {
			const query = input.value.trim().toLowerCase();

			yearHeaders.forEach((header) => {
				let node = header.nextElementSibling;
				let visibleCount = 0;
				while (node && node.tagName !== 'H3') {
					if (node.tagName === 'UL') {
						const items = Array.from(node.querySelectorAll('li'));
						items.forEach((li) => {
							const text = li.textContent.toLowerCase();
							const match = query === '' || text.includes(query);
							li.style.display = match ? '' : 'none';
							if (match) visibleCount += 1;
						});
					}
					node = node.nextElementSibling;
				}

				const showYear = visibleCount > 0 || query === '';
				header.style.display = showYear ? '' : 'none';

				node = header.nextElementSibling;
				while (node && node.tagName !== 'H3') {
					if (node.tagName === 'UL') {
						node.style.display = showYear ? '' : 'none';
					}
					node = node.nextElementSibling;
				}
			});
		}

		input.addEventListener('input', applyFilter);
	});
</script>
