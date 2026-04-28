---
layout: page
title: tools & data
permalink: /resources/
description: Open-source tools and databases from the Enquist Lab
nav: true
nav_order: 6
---

## Software & Open Data

Code and public tools associated with current and ongoing lab projects.

- [Enquist Lab on GitHub](https://github.com/EnquistLab)
- [Oxford Ecosystems Lab on GitHub](https://github.com/OxfordEcosystemsLab)
- [BIEN Data Portal](https://biendata.org/)

<div class="cta-row">
  <a class="btn btn-sm btn-cta-primary" href="https://biendata.org/" target="_blank" rel="noopener">Go to BIEN Portal</a>
  <a class="btn btn-sm btn-cta-outline" href="https://github.com/EnquistLab" target="_blank" rel="noopener">View on GitHub</a>
  <a class="btn btn-sm btn-cta-outline" href="https://plantfunctionaltraitscourses.w.uib.no/" target="_blank" rel="noopener">Read Training Materials</a>
</div>

<div class="resources-hero-grid">
	<figure class="resources-hero-grid__lead">
		<img src="{{ '/assets/img/wordpress/dsc_3236.jpeg' | relative_url }}" alt="Cloud-forest mountain slope along an Andean elevational transect" loading="lazy">
		<figcaption>Elevational campaigns tie field sampling to climate gradients and synthesis-ready datasets.</figcaption>
	</figure>
	<figure>
		<img src="{{ '/assets/img/wordpress/dsc_3443.jpeg' | relative_url }}" alt="Snow-covered Andean peaks above alpine field terrain" loading="lazy">
		<figcaption>Lab resources are built across linked mountain, forest, and climate-gradient systems.</figcaption>
	</figure>
	<figure>
		<img src="{{ '/assets/img/wordpress/img_0597.jpg' | relative_url }}" alt="Old-growth conifer forest with very small field crew at the base of towering trees" loading="lazy">
		<figcaption>Long-term plot measurements connect forest structure, demography, and open data workflows.</figcaption>
	</figure>
</div>
<p class="resources-hero-note">Lab software and open data products are built from the same pipeline: field observations, curated synthesis databases, and decision-oriented ecological analyses.</p>

<style>
  .resources-hero-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.35fr) minmax(0, 1fr);
    gap: 0.85rem;
    margin: 1.5rem 0 0.8rem;
    align-items: stretch;
  }
  .resources-hero-grid figure {
    margin: 0;
  }
  .resources-hero-grid__lead {
    grid-row: span 2;
  }
  .resources-hero-grid img {
    width: 100%;
    height: 100%;
    min-height: 220px;
    object-fit: cover;
    display: block;
    border-radius: 0.5rem;
  }
  .resources-hero-grid figcaption,
  .resources-hero-note {
    font-size: 0.84rem;
    color: var(--global-text-color-light);
    letter-spacing: 0.01em;
  }
  .resources-hero-grid figcaption {
    margin-top: 0.45rem;
  }
  .resources-hero-note {
    margin: 0 0 2rem;
    max-width: 48rem;
  }
  @media (max-width: 768px) {
    .resources-hero-grid {
      grid-template-columns: 1fr;
    }
    .resources-hero-grid__lead {
      grid-row: auto;
    }
    .resources-hero-grid img {
      min-height: 200px;
    }
  }
</style>

### Lab Resources

- [Teaching and training]({{ '/teaching/' | relative_url }})
- [News archive]({{ '/news/' | relative_url }})
- [Blog]({{ '/blog/' | relative_url }})
- [Press and media]({{ '/press-media/' | relative_url }})

---

### PFTC Resources

The [Plant Functional Trait Courses](https://plantfunctionaltraitscourses.w.uib.no/) are a major training pipeline for the lab's field-based trait ecology work. They combine hands-on sampling, data curation, community ecology, and quantitative analysis across diverse field settings.

<div class="photo-pair">
  <figure>
		<img src="{{ '/assets/img/wordpress/dsc_3414.jpeg' | relative_url }}" alt="Field team working across a high-Andean ridge with a broad mountain valley below" loading="lazy">
		<figcaption>PFTC training connects field logistics, trait sampling, and gradient-scale ecological inference.</figcaption>
  </figure>
  <figure>
		<img src="{{ '/assets/img/wordpress/img_5090.jpeg' | relative_url }}" alt="Researchers measuring a tree in tropical forest during field training" loading="lazy">
    <figcaption>Trait-course field campaigns link sampling design, climate gradients, and open data workflows.</figcaption>
  </figure>
</div>

<div class="resource-link-grid">
	<a class="resource-link-card" href="https://plantfunctionaltraitscourses.w.uib.no/">
		<h4>PFTC Website</h4>
		<p>Course overview, field locations, and program context.</p>
	</a>
	<a class="resource-link-card" href="https://plant-functional-trait-course.github.io/PFTC_teaching_material/">
		<h4>Teaching Material</h4>
		<p>Central course documentation and open teaching modules.</p>
	</a>
	<a class="resource-link-card" href="https://plant-functional-trait-course.github.io/PFTC_teaching_material/6_pftc_data.html">
		<h4>Working With PFTC Data</h4>
		<p>Data structure, workflow, and analysis orientation for course datasets.</p>
	</a>
	<a class="resource-link-card" href="https://plant-functional-trait-course.github.io/PFTC_teaching_material/9_data_curation.html">
		<h4>Data Curation</h4>
		<p>Cleaning, documentation, and QA practices for trait datasets.</p>
	</a>
	<a class="resource-link-card" href="https://plant-functional-trait-course.github.io/PFTC_teaching_material/10_community.html">
		<h4>Community And Sampling Data</h4>
		<p>Plot structure, community measurements, and sampling design guidance.</p>
	</a>
	<a class="resource-link-card" href="https://plant-functional-trait-course.github.io/PFTC_teaching_material/12_traits.html">
		<h4>Plant Functional Trait Data</h4>
		<p>Trait definitions, measurement protocols, and interpretation notes.</p>
	</a>
	<a class="resource-link-card" href="https://plantfunctionaltraitscourses.w.uib.no/course-lectures/">
		<h4>PFTC Lectures</h4>
		<p>Lecture archive covering methods, theory, and field applications.</p>
	</a>
</div>

---

---

### BIEN: Botanical Information & Ecology Network

<img src="{{ '/assets/img/wordpress/bien_logo_notext-1.png' | relative_url }}" alt="BIEN — Botanical Information and Ecology Network" style="max-width:220px;width:100%;display:block;margin:0.5rem 0 1.2rem;">

The [BIEN project](https://biendata.org/) compiles and standardizes occurrence records, trait measurements, and plot data for vascular plants of the Western Hemisphere — one of the largest plant biodiversity synthesis efforts globally. The database integrates herbarium specimens, citizen-science observations, and plot inventories spanning roughly 1800s–present, with taxonomic reconciliation against a versioned plant name backbone and coordinate-level QA filtering.

---

#### BIEN R Package

The `BIEN` R package provides programmatic access to ~85 million botanical observations, ~100,000 species range maps, and plant trait data for the New World.

<div style="display:flex;flex-wrap:wrap;gap:0.5rem 1.2rem;margin:0.4rem 0 0.8rem;font-size:0.93rem;">
  <span><strong>CRAN:</strong> <a href="https://cran.r-project.org/package=BIEN">BIEN on CRAN</a></span>
  <span><strong>GitHub:</strong> <a href="https://github.com/EnquistLab/BIEN">EnquistLab/BIEN</a></span>
  <span><strong>Citation:</strong> Maitner et al. (2018) <em>Methods in Ecology and Evolution</em></span>
</div>

```r
install.packages("BIEN")
library(BIEN)
sp <- BIEN_occurrence_species("Pinus ponderosa")
```

---

#### BIEN Data Portal & Interactive Apps

The [BIEN GeoSpatial portal](https://biendata.org/) provides web-based access to New World plant occurrence, range, and trait data with QA/QC, taxonomic harmonization, and geographic filtering. Three focused Shiny apps extend portal access for specific workflows:

<div class="bien-apps-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0.85rem;margin:0.9rem 0 1.2rem;">

<div style="border:1px solid var(--global-divider-color,#ddd);border-radius:6px;padding:0.9rem;">
  <strong><a href="https://benquist.shinyapps.io/bien-species-shinyapp/" target="_blank" rel="noopener">▶ BIEN Species Explorer</a></strong><br>
  <span style="font-size:0.87rem;">Browse occurrence records and range maps for ~120,000 Western Hemisphere plant species. Filter by native status, political unit, and elevation; download georeferenced records and range polygons.</span><br>
  <small><a href="https://github.com/benquist/BIEN-SpeciesShinyApp#readme" target="_blank" rel="noopener">GitHub README</a></small>
</div>

<div style="border:1px solid var(--global-divider-color,#ddd);border-radius:6px;padding:0.9rem;">
  <strong><a href="https://benquist.shinyapps.io/bien-traits-shinyapp/" target="_blank" rel="noopener">▶ BIEN Traits Explorer</a></strong><br>
  <span style="font-size:0.87rem;">Query, map, and export plant functional trait observations. Supports multi-species input, coverage preview, mapped observations, and reproducible R export code with full provenance metadata.</span><br>
  <small><a href="https://github.com/benquist/BIEN_Trait_Shiny_App#readme" target="_blank" rel="noopener">GitHub README</a></small>
</div>

<div style="border:1px solid var(--global-divider-color,#ddd);border-radius:6px;padding:0.9rem;">
  <strong><a href="https://benquist.shinyapps.io/bien-data-loader/" target="_blank" rel="noopener">▶ BIEN Data Loader</a></strong><br>
  <span style="font-size:0.87rem;">Upload a species list to retrieve, review, and bulk-export BIEN occurrence and trait data. Designed for batch queries and downstream biodiversity analysis workflows.</span><br>
  <small><a href="https://github.com/benquist/BIEN_Data_Loader#readme" target="_blank" rel="noopener">GitHub README</a></small>
</div>

</div>

---

#### BIEN Web Services

These services form a complete biodiversity data QA pipeline from taxonomic names to geographic context:

![BIEN workflow diagram: occurrence data flows through TNRS, GNRS, NSR, and GVS]({{ '/assets/img/wordpress/screen-shot-2020-12-29-at-6.27.29-pm.png' | relative_url }}){: .bien-workflow-image }

<div class="bien-services-grid">
  <a class="bien-service-card" href="https://tnrs.biendata.org/">
    <h4>TNRS</h4>
    <p>Taxonomic Name Resolution Service</p>
  </a>
  <a class="bien-service-card" href="https://gnrs.biendata.org/">
    <h4>GNRS</h4>
    <p>Geographic Name Resolution Service</p>
  </a>
  <a class="bien-service-card" href="https://nsr.biendata.org/">
    <h4>NSR</h4>
    <p>Native Species Resolver</p>
  </a>
  <a class="bien-service-card" href="https://gvs.biendata.org/">
    <h4>GVS</h4>
    <p>Geocoordinate Validation Service</p>
  </a>
</div>

<dl class="bien-service-detail" style="margin:0.6rem 0 0;font-size:0.92rem;">
  <dt><strong><a href="https://tnrs.biendata.org/">TNRS</a></strong> — Taxonomic Name Resolution Service</dt>
  <dd>Computer-assisted standardization of plant scientific names: corrects spelling errors, resolves synonyms, and maps names to accepted taxonomy. <a href="https://github.com/iPlantCollaborativeOpenSource/TNRS">GitHub source</a> · <a href="https://www.nature.com/articles/474263a">Featured in <em>Nature</em> (2011)</a> · <a href="https://link.springer.com/article/10.1186/1471-2105-14-16">Boyle et al. (2013), <em>BMC Bioinformatics</em></a></dd>
  <dt><strong><a href="https://gnrs.biendata.org/">GNRS</a></strong> — Geographic Name Resolution Service</dt>
  <dd>Standardizes political division names (country, state/province, county) against authoritative gazetteers, enabling consistent geographic filtering and data integration across sources. <a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0268162">Boyle et al. (2022), <em>PLOS ONE</em></a></dd>
  <dt><strong><a href="https://nsr.biendata.org/">NSR</a></strong> — Native Species Resolver</dt>
  <dd>Uses regional taxonomic checklists to determine whether observations of a species within a political division are native, introduced, or cultivated. <a href="http://bien.nceas.ucsb.edu/bien/tools/nsr/">Legacy tool page</a></dd>
  <dt><strong><a href="https://gvs.biendata.org/">GVS</a></strong> — Geocoordinate Validation Service</dt>
  <dd>Validates and corrects geocoordinates, flags implausible locations, and returns standardized political context for each point.</dd>
</dl>

#### R Vignettes

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0.5rem 1rem;margin:0.5rem 0 1.2rem;font-size:0.92rem;">
  <a href="https://cran.r-project.org/web/packages/BIEN/vignettes/BIEN.html">BIEN R package</a>
  <a href="https://cran.r-project.org/web/packages/TNRS/vignettes/TNRS_vignette.html">TNRS vignette</a>
  <a href="https://cran.r-project.org/web/packages/GNRS/vignettes/GNRS.html">GNRS vignette</a>
  <a href="https://cran.r-project.org/web/packages/NSR/vignettes/NSR.html">NSR vignette</a>
  <a href="https://cran.r-project.org/web/packages/GVS/vignettes/GVS.html">GVS vignette</a>
</div>

<style>
  .resource-link-grid,
  .bien-services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
    gap: 0.8rem;
    margin: 0.8rem 0 0.5rem;
  }
  .bien-workflow-image {
    display: block;
    width: 100%;
    max-width: 760px;
    height: auto;
    margin: 0.65rem auto 1rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 0.5rem;
  }
  .resource-link-card,
  .bien-service-card {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.7rem;
    padding: 0.85rem 0.9rem;
    background: color-mix(in srgb, var(--global-card-bg-color) 90%, var(--global-theme-color) 10%);
    text-decoration: none;
    color: var(--global-text-color);
    transition: border-color 0.2s ease, transform 0.2s ease;
  }
  .resource-link-card:hover,
  .resource-link-card:focus-visible,
  .bien-service-card:hover,
  .bien-service-card:focus-visible {
    border-color: var(--global-theme-color);
    transform: translateY(-1px);
    text-decoration: none;
  }
  .resource-link-card h4,
  .bien-service-card h4 {
    margin: 0 0 0.25rem;
    color: var(--global-theme-color);
  }
  .resource-link-card p,
  .bien-service-card p {
    margin: 0;
    font-size: 0.91rem;
  }
  .bien-service-detail dt {
    margin-top: 0.7rem;
    font-weight: 600;
  }
  .bien-service-detail dd {
    margin: 0.15rem 0 0 1rem;
    color: var(--global-text-color);
  }
</style>

---

### Hypervolumes

Estimates the shape and volume of high-dimensional ecological objects (niches, trait distributions) and performs set operations including intersection, union, and overlap. Used for n-dimensional niche measurement and species distribution modeling.

- **CRAN:** [hypervolume](https://cran.r-project.org/package=hypervolume)
- **Citation:** Blonder et al. (2014) *Global Ecology and Biogeography*

---

### fluxible

Processes ecosystem gas flux time series and applies quality assurance workflows for eddy covariance and closed-chamber measurements. Handles CO₂, CH₄, and N₂O flux data from a variety of sensor systems. Core functions include flux calculation from raw concentration–time curves, automatic detection of non-linear or problematic measurements, outlier flagging, and export of QA-annotated summaries.

Designed to integrate with the outputs of standard flux loggers and field datalogger formats, and pairs naturally with the lab's long-term ecosystem monitoring work at sites including RMBL and tropical elevational transects.

- **CRAN:** [fluxible](https://cran.r-project.org/web/packages/fluxible/index.html)
- **GitHub:** [jogaudard/fluxible](https://github.com/jogaudard/fluxible)
- **Vignette:** [Getting started with fluxible](https://cran.r-project.org/web/packages/fluxible/vignettes/)

```r
install.packages("fluxible")
library(fluxible)
```

---

### traitstrap

Bootstraps trait distributions to propagate uncertainty from individual-level measurements to community-weighted means and higher-order community trait statistics. Addresses a key challenge in trait-based ecology: raw community-weighted mean (CWM) calculations ignore intraspecific trait variation and sampling uncertainty. `traitstrap` implements parametric bootstrapping that draws from species-level trait distributions, weighted by abundance, producing CWMs with full uncertainty quantification suitable for downstream modeling.

Works directly with trait data from BIEN, TRY, and comparable databases, and is designed to integrate with the lab's Trait Driver Theory framework.

- **CRAN:** [traitstrap](https://cran.r-project.org/web/packages/traitstrap/index.html)
- **GitHub:** [Plant-Functional-Trait-Course/traitstrap](https://github.com/Plant-Functional-Trait-Course/traitstrap)
- **Citation:** Maitner et al. — see CRAN page for current reference
- **Vignette:** [traitstrap vignette](https://cran.r-project.org/web/packages/traitstrap/vignettes/)

```r
install.packages("traitstrap")
library(traitstrap)
```

---

### netassoc

Infers species associations from community co-occurrence matrices using partial correlations and Gaussian graphical models with null modeling.

- **CRAN:** [netassoc](https://cran.r-project.org/package=netassoc)
- **Citation:** Morueta-Holme, Blonder et al. *Ecography*

---

### comclim

Computes community climate statistics for volume and mismatch using species' climate niches, scaled relative to a regional species pool. Used to infer community assembly processes.

- **CRAN:** [comclim](https://cran.r-project.org/package=comclim)
- **Citation:** Blonder et al. (2015) *Ecology*

---

### Plant-O-Matic

Open software integrating biodiversity layers with mobile APIs to deliver plant identification and occurrence information.

- **Citation:** Enquist et al. (2016) *Methods in Ecology and Evolution*
- [GitHub](https://github.com/efitz/plantomatic)

### OpenTraits Network

We co-lead the [OpenTraits Network](https://opentraits.org/), which promotes open, standardized, and FAIR (Findable, Accessible, Interoperable, Reusable) trait data across all organisms.

- **Website:** [opentraits.org](https://opentraits.org/)
- **Publication:** Gallagher et al. (2020) *Nature Ecology & Evolution*

---

### Trait Driver Theory Tools

Code and tutorials for applying Trait Driver Theory to community data:

- **GitHub:** [EnquistLab/TraitDriverTheory](https://github.com/EnquistLab/)

---

---

### Tools & Datasets

| Resource | Description | Link |
|---|---|---|
| SALVIAS | Plant inventory plots database | [salvias.net](https://www.salvias.net/) |
| BIEN Traits | Validated plant trait measurements | [biendata.org](https://biendata.org/) |
| GBIF / TNRS | Taxonomic resolution tools | [tnrs.biendata.org](https://tnrs.biendata.org/) |

