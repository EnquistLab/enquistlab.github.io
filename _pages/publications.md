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

{% include bib_search.liquid %}

<div id="full-publication-list">
{% include publications_full_from_doc.md %}
</div>

<script>
	document.addEventListener('DOMContentLoaded', function () {
		const input = document.getElementById('bibsearch');
		const container = document.getElementById('full-publication-list');
		if (!input || !container) return;

		input.placeholder = 'Type to filter complete publication list';

		const yearHeaders = Array.from(container.querySelectorAll('p')).filter((p) => {
			const t = p.textContent.trim();
			return /^\d{4}$/.test(t) || /^\d{4}\s*-\s*\d{4}$/.test(t);
		});

		function applyFilter() {
			const query = input.value.trim().toLowerCase();

			yearHeaders.forEach((header) => {
				let node = header.nextElementSibling;
				let visibleCount = 0;
				while (
					node &&
					!(
						node.tagName === 'P' &&
						(/^[0-9]{4}$/.test(node.textContent.trim()) ||
							/^[0-9]{4}\s*-\s*[0-9]{4}$/.test(node.textContent.trim()))
					)
				) {
					if (node.tagName === 'OL' || node.tagName === 'UL') {
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
				while (
					node &&
					!(
						node.tagName === 'P' &&
						(/^[0-9]{4}$/.test(node.textContent.trim()) ||
							/^[0-9]{4}\s*-\s*[0-9]{4}$/.test(node.textContent.trim()))
					)
				) {
					if (node.tagName === 'OL' || node.tagName === 'UL') {
						node.style.display = showYear ? '' : 'none';
					}
					node = node.nextElementSibling;
				}
			});
		}

		input.addEventListener('input', applyFilter);
	});
</script>
