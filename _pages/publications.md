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
{% capture full_publication_markdown %}{% include publications_full_from_doc.md %}{% endcapture %}
{{ full_publication_markdown | markdownify }}
</div>

<script>
	document.addEventListener('DOMContentLoaded', function () {
		const input = document.getElementById('bibsearch');
		const container = document.getElementById('full-publication-list');
		if (!input || !container) return;

		input.placeholder = 'Type to filter complete publication list';

		function escapeHtml(value) {
			return value
				.replace(/&/g, '&amp;')
				.replace(/</g, '&lt;')
				.replace(/>/g, '&gt;')
				.replace(/"/g, '&quot;')
				.replace(/'/g, '&#39;');
		}

		function detectPaperUrl(text) {
			const doiUrlMatch = text.match(/https?:\/\/doi\.org\/\S+/i);
			if (doiUrlMatch) return doiUrlMatch[0].replace(/[),.;]+$/, '');

			const doiMatch = text.match(/\b10\.\d{4,9}\/[\-._;()\/:A-Z0-9]+/i);
			if (doiMatch) return 'https://doi.org/' + doiMatch[0].replace(/[),.;]+$/, '');

			const urlMatch = text.match(/https?:\/\/\S+/i);
			if (urlMatch) return urlMatch[0].replace(/[),.;]+$/, '');

			return null;
		}

		function linkifyPublicationTitles() {
			const items = Array.from(container.querySelectorAll('li'));
			items.forEach((li) => {
				if (li.querySelector('a.paper-title-link')) return;

				const text = li.textContent.replace(/\s+/g, ' ').trim();
				const url = detectPaperUrl(text);
				if (!url) return;

				let start = -1;
				let end = -1;
				const yearMatch = text.match(/\(\d{4}\)\s*/);
				if (yearMatch && yearMatch.index !== undefined) {
					start = yearMatch.index + yearMatch[0].length;
					end = text.indexOf('. ', start);
					if (end === -1) end = text.indexOf('.', start);
				}

				if (start < 0 || end <= start) {
					const first = text.indexOf('. ');
					const second = first >= 0 ? text.indexOf('. ', first + 2) : -1;
					if (first >= 0 && second > first + 2) {
						start = first + 2;
						end = second;
					}
				}

				if (start < 0 || end <= start) return;

				const prefix = text.slice(0, start);
				const title = text.slice(start, end + 1).trim();
				const suffix = text.slice(end + 1);
				if (title.length < 10) return;

				li.innerHTML =
					escapeHtml(prefix) +
					'<a class="paper-title-link" href="' +
					escapeHtml(url) +
					'" target="_blank" rel="noopener noreferrer">' +
					escapeHtml(title) +
					'</a>' +
					escapeHtml(suffix);
			});
		}

		linkifyPublicationTitles();

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
