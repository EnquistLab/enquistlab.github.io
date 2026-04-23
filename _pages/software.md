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

### Additional Lab Resources

- [Teaching and training]({{ '/teaching/' | relative_url }})
- [News archive]({{ '/news/' | relative_url }})
- [Blog]({{ '/blog/' | relative_url }})
- [Press and media]({{ '/press-media/' | relative_url }})

---

### Plant Functional Trait Course (PFTC) Resources <span class="tool-tags"><span class="tool-tag">training</span><span class="tool-tag">trait ecology</span><span class="tool-tag">field methods</span></span>

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

### BIEN R Package <span class="tool-tags"><span class="tool-tag">occurrence</span><span class="tool-tag">trait</span><span class="tool-tag">range</span></span>

The `BIEN` R package provides programmatic access to the Botanical Information and Ecology Network database — ~85 million botanical observations, ~100,000 species range maps, and plant trait data for the New World.

- **CRAN:** [BIEN on CRAN](https://cran.r-project.org/package=BIEN)
- **GitHub:** [EnquistLab/BIEN](https://github.com/EnquistLab/BIEN)
- **Citation:** Maitner et al. (2018) *Methods in Ecology and Evolution*

```r
install.packages("BIEN")
library(BIEN)
sp <- BIEN_occurrence_species("Pinus ponderosa")
```

---

### BIEN Data Portal <span class="tool-tags"><span class="tool-tag">occurrence</span><span class="tool-tag">spatial</span></span>

The BIEN GeoSpatial portal provides web-based access to New World plant occurrence, range, and trait data with QA/QC, taxonomic harmonization, and geographic filtering.

- **Portal:** [biendata.org](https://biendata.org/)

---

### Taxonomic Name Resolution Service (TNRS) <span class="tool-tags"><span class="tool-tag">taxonomy</span></span>

Computer-assisted standardization of plant scientific names: corrects spelling errors, resolves synonyms, and maps names to accepted taxonomy.

An online tool for the standardization of plant taxonomic names.

- [tnrs.biendata.org](https://tnrs.biendata.org/)
- [GitHub source](https://github.com/iPlantCollaborativeOpenSource/TNRS)
- [Featured in *Nature* (2011)](https://www.nature.com/articles/474263a)
- [TNRS publication: Boyle et al. (2013), *BMC Bioinformatics*](https://link.springer.com/article/10.1186/1471-2105-14-16)

---

### BIEN Web Services

These services support a complete biodiversity data QA workflow from names to geography:

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

<style>
	.resource-link-grid,
	.bien-services-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
		gap: 0.8rem;
		margin: 0.8rem 0 1.1rem;
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
		font-size: 0.94rem;
	}
</style>

- **GVS (Geocoordinate Validation Service):** validates and corrects geocoordinates and returns political context.

#### R Vignettes

- [Taxonomic Names Resolution Service (TNRS vignette)](https://cran.r-project.org/web/packages/TNRS/vignettes/TNRS_vignette.html)
- [Geographic Name Resolution Service (GNRS vignette)](https://cran.r-project.org/web/packages/GNRS/vignettes/GNRS.html)
- [Native Species Resolver (NSR vignette)](https://cran.r-project.org/web/packages/NSR/vignettes/NSR.html)
- [Geocoordinate Validation Service (GVS vignette)](https://cran.r-project.org/web/packages/GVS/vignettes/GVS.html)
- [BIEN R package vignette](https://cran.r-project.org/web/packages/BIEN/vignettes/BIEN.html)

---

### Native Species Resolver (NSR) <span class="tool-tags"><span class="tool-tag">taxonomy</span><span class="tool-tag">native status</span></span>

Uses regional taxonomic checklists to determine whether observations of a species within political divisions (country, state/province, county) are native or introduced.

- [bien.nceas.ucsb.edu/bien/tools/nsr/](http://bien.nceas.ucsb.edu/bien/tools/nsr/)

---

### Hypervolumes R Package <span class="tool-tags"><span class="tool-tag">trait</span><span class="tool-tag">niche</span></span>

Estimates the shape and volume of high-dimensional ecological objects (niches, trait distributions) and performs set operations including intersection, union, and overlap. Used for n-dimensional niche measurement and species distribution modeling.

- **CRAN:** [hypervolume](https://cran.r-project.org/package=hypervolume)
- **Citation:** Blonder et al. (2014) *Global Ecology and Biogeography*

---

### fluxible <span class="tool-tags"><span class="tool-tag">flux</span><span class="tool-tag">time series</span><span class="tool-tag">QA</span></span>

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

### traitstrap <span class="tool-tags"><span class="tool-tag">trait</span><span class="tool-tag">uncertainty</span><span class="tool-tag">bootstrap</span></span>

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

### netassoc R Package <span class="tool-tags"><span class="tool-tag">occurrence</span><span class="tool-tag">co-occurrence</span></span>

Infers species associations from community co-occurrence matrices using partial correlations and Gaussian graphical models with null modeling.

- **CRAN:** [netassoc](https://cran.r-project.org/package=netassoc)
- **Citation:** Morueta-Holme, Blonder et al. *Ecography*

---

### comclim R Package <span class="tool-tags"><span class="tool-tag">trait</span><span class="tool-tag">climate</span></span>

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

### Additional Tools & Datasets

| Resource | Description | Link |
|---|---|---|
| SALVIAS | Plant inventory plots database | [salvias.net](https://www.salvias.net/) |
| BIEN Traits | Validated plant trait measurements | [biendata.org](https://biendata.org/) |
| GBIF / TNRS | Taxonomic resolution tools | [tnrs.biendata.org](https://tnrs.biendata.org/) |

