---
layout: page
title: resources
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

<figure class="resources-hero-banner">
  <img src="{{ '/assets/img/wordpress/dsc_3225.jpg' | relative_url }}" alt="Researcher conducting leaf gas-exchange measurements at an Andean high-altitude field station, cloud-forest slopes visible through the window" loading="lazy">
  <figcaption>High-Andes field station: leaf-level gas-exchange measurements linking plant physiology to ecosystem function.</figcaption>
</figure>

<style>
  .resources-hero-banner {
    margin: 1.5rem 0 2rem;
    overflow: hidden;
    border-radius: 4px;
  }
  .resources-hero-banner img {
    width: 100%;
    height: 260px;
    object-fit: cover;
    object-position: center 30%;
    display: block;
  }
  .resources-hero-banner figcaption {
    font-size: 0.82rem;
    color: var(--global-text-color-light);
    margin-top: 0.4rem;
    letter-spacing: 0.01em;
  }
</style>

### Additional Lab Resources

- [Teaching and training]({{ '/teaching/' | relative_url }})
- [News archive]({{ '/news/' | relative_url }})
- [Blog]({{ '/blog/' | relative_url }})
- [Press and media]({{ '/press-media/' | relative_url }})

---

### BIEN R Package

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

### BIEN Data Portal

The BIEN GeoSpatial portal provides web-based access to New World plant occurrence, range, and trait data with QA/QC, taxonomic harmonization, and geographic filtering.

- **Portal:** [biendata.org](https://biendata.org/)

---

### Taxonomic Name Resolution Service (TNRS)

Computer-assisted standardization of plant scientific names: corrects spelling errors, resolves synonyms, and maps names to accepted taxonomy.

An online tool for the standardization of plant taxonomic names.

- [tnrs.biendata.org](https://tnrs.biendata.org/)
- [GitHub source](https://github.com/iPlantCollaborativeOpenSource/TNRS)
- Featured in *Nature* (2011)

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
	.bien-services-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
		gap: 0.8rem;
		margin: 0.8rem 0 1.1rem;
	}

	.bien-service-card {
		border: 1px solid var(--global-divider-color);
		border-radius: 0.7rem;
		padding: 0.85rem 0.9rem;
		background: color-mix(in srgb, var(--global-card-bg-color) 90%, var(--global-theme-color) 10%);
		text-decoration: none;
		color: var(--global-text-color);
		transition: border-color 0.2s ease, transform 0.2s ease;
	}

	.bien-service-card:hover,
	.bien-service-card:focus-visible {
		border-color: var(--global-theme-color);
		transform: translateY(-1px);
		text-decoration: none;
	}

	.bien-service-card h4 {
		margin: 0 0 0.25rem;
		color: var(--global-theme-color);
	}

	.bien-service-card p {
		margin: 0;
		font-size: 0.94rem;
	}
</style>

- **TNRS (Taxonomic Name Resolution Service):** an online tool for the standardization of plant taxonomic names.
- **GNRS (Geographic Name Resolution Service):** standardizes political division names globally.
- **NSR (Native Species Resolver):** flags potentially introduced occurrences by political division.
- **GVS (Geocoordinate Validation Service):** validates and corrects geocoordinates and returns political context.

#### Our Other Services

- [Geographic Name Resolution Service](https://gnrs.biendata.org/)
- [Native Species Resolver](https://nsr.biendata.org/)
- [Geocoordinate Validation Service](https://gvs.biendata.org/)

#### R Vignettes

- [Taxonomic Names Resolution Service (TNRS vignette)](https://cran.r-project.org/web/packages/TNRS/vignettes/TNRS_vignette.html)
- [Geographic Name Resolution Service (GNRS vignette)](https://cran.r-project.org/web/packages/GNRS/vignettes/GNRS.html)
- [Native Species Resolver (NSR vignette)](https://cran.r-project.org/web/packages/NSR/vignettes/NSR.html)
- [Geocoordinate Validation Service (GVS vignette)](https://cran.r-project.org/web/packages/GVS/vignettes/GVS.html)
- [BIEN R package vignette](https://cran.r-project.org/web/packages/BIEN/vignettes/BIEN.html)

---

### Native Species Resolver (NSR)

Uses regional taxonomic checklists to determine whether observations of a species within political divisions (country, state/province, county) are native or introduced.

- [bien.nceas.ucsb.edu/bien/tools/nsr/](http://bien.nceas.ucsb.edu/bien/tools/nsr/)

---

### Hypervolumes R Package

Estimates the shape and volume of high-dimensional ecological objects (niches, trait distributions) and performs set operations including intersection, union, and overlap. Used for n-dimensional niche measurement and species distribution modeling.

- **CRAN:** [hypervolume](https://cran.r-project.org/package=hypervolume)
- **Citation:** Blonder et al. (2014) *Global Ecology and Biogeography*

---

### netassoc R Package

Infers species associations from community co-occurrence matrices using partial correlations and Gaussian graphical models with null modeling.

- **CRAN:** [netassoc](https://cran.r-project.org/package=netassoc)
- **Citation:** Morueta-Holme, Blonder et al. *Ecography*

---

### comclim R Package

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

### Additional R Packages

#### fluxible

Tools for processing ecosystem gas flux time series and QA workflows.

- **CRAN:** [fluxible](https://cran.r-project.org/web/packages/fluxible/index.html)

#### traitstrap

Bootstrap and uncertainty tools for trait-based ecological analyses.

- **CRAN:** [traitstrap](https://cran.r-project.org/web/packages/traitstrap/index.html)

---

### Additional Tools & Datasets

| Resource | Description | Link |
|---|---|---|
| SALVIAS | Plant inventory plots database | [salvias.net](https://www.salvias.net/) |
| BIEN Traits | Validated plant trait measurements | [biendata.org](https://biendata.org/) |
| GBIF / TNRS | Taxonomic resolution tools | [tnrs.biendata.org](https://tnrs.biendata.org/) |

