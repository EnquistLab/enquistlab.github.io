---
layout: page
title: research
permalink: /research/
description: Current research themes and projects in the Enquist Macroecology Lab
nav: true
nav_order: 3
---

## Research Program

<figure class="field-photo">
  <img src="{{ "/assets/img/field/brian_field.jpg" | relative_url }}" alt="Brian Enquist conducting field measurements" loading="lazy">
  <figcaption>Field measurements — connecting individual-level physiology to ecosystem-scale patterns.</figcaption>
</figure>

Our lab develops theory and data-driven tools to explain how biodiversity is organized across scales, and how it is changing under climate and land-use pressure.

We organize our work as a connected process: observations and traits -> scaling and trait-based theory -> predictive models -> uncertainty-aware ecological forecasting.

Current themes include:

- Scaling in biology and allometry
- Forecasting the fate of biodiversity and the biosphere
- Trait-based ecology as a foundation for predictive ecology and biodiversity science
- Biodiversity informatics
- Macroecology of biodiversity gradients
- Ecology and evolution of plant functional and physiological integration
- Long-term monitoring of populations, communities, and ecosystems in tropical, temperate, and alpine environments

Our research flows from observation to prediction: we measure organisms and ecosystems, build theories about why patterns emerge across levels of biological organization, and test whether those theories can forecast how biodiversity responds to global change.

---

### Metabolic Scaling & Functional Biology

We develop and extend metabolic scaling theory (West, Brown, and Enquist 1997; 1999) to predict how growth, mortality, and resource use scale with body size and temperature. Current work applies these principles to forest structure, carbon dynamics, and demography.

**Key questions:**
- How do allometric constraints shape plant architecture and forest structure?
- Can metabolic scaling theory predict ecosystem carbon fluxes and turnover?
- What are the evolutionary origins of scaling relationships?

---

### Trait Driver Theory & Functional Ecology

[Trait Driver Theory (TDT)](https://www.nature.com/articles/s41477-019-0506-6) is a general theoretical framework that predicts how the distribution of functional traits in a community responds to environmental drivers. TDT bridges individual-level physiology, community assembly, and ecosystem function.

Applications include:
- Predicting community trait shifts under climate change
- Understanding trait-environment relationships across biomes
- Linking remote sensing spectral data to functional diversity

---

### BIEN: Botanical Information & Ecology Network

The [BIEN project](https://biendata.org/) compiles and standardizes occurrence records, trait measurements, and plot data for vascular plants in the Western Hemisphere. It is one of the largest plant biodiversity synthesis efforts globally.

**Tools:** [BIEN R package](https://cran.r-project.org/package=BIEN) | [GeoSpatial portal](https://biendata.org/)

<details class="bien-quickstart">
<summary>Quick start: access BIEN data in R</summary>

```r
install.packages("BIEN")
library(BIEN)

# Occurrence records for a species
occ <- BIEN_occurrence_species("Pinus ponderosa")

# Plant traits
traits <- BIEN_trait_species("Quercus agrifolia")

# Species range map
range <- BIEN_ranges_load_species("Populus tremuloides")
```

Full docs: [BIEN vignette](https://cran.r-project.org/web/packages/BIEN/vignettes/BIEN.html) · [All lab tools]({{ '/resources/' | relative_url }})
</details>

---

### Global Change Biology

We forecast how plant communities may respond to climate change using trait-based models, species distribution models, and process-based frameworks. Work includes:

- Trait-based range shift forecasting
- Detecting signals of climate-driven community turnover in BIEN data
- Assessing vulnerability of tropical and montane floras

**Uncertainty and transferability:** We report assumptions, data coverage limits, and scenario sensitivity when projecting biodiversity responses across regions and time.

---

### Collaborative Initiatives

We actively collaborate with local and international initiatives that support field work, synthesis, and training for students, postdocs, and collaborators. These collaborations include biodiversity forecasting and conservation planning efforts, including SPARC and related protected-area prioritization projects.

See [collaborators]({{ '/collaborators/' | relative_url }}) for examples.

---

### Long-Term Ecology

Our long-term work integrates repeated forest censuses, elevational transects, and distributed plot networks to quantify demographic and compositional change through time and to improve ecological prediction.

See [field sites]({{ '/field-sites/' | relative_url }}) for site details.

<figure class="field-photo" style="max-height:320px;">
  <img src="{{ '/assets/img/wordpress/sparc_overview_map.jpg' | relative_url }}" alt="SPARC biodiversity planning map — protected area prioritization across the Americas" loading="lazy" style="height:320px;object-fit:contain;background:#f7f6f2;">
  <figcaption>SPARC protected-area prioritization analysis — integrating BIEN occurrence and trait data to identify conservation priority regions across the Americas.</figcaption>
</figure>

---

### OpenTraits & Biodiversity Informatics

We are co-founders of the [OpenTraits Network](https://opentraits.org/), which promotes open, standardized, and interoperable trait data across all organisms. Related informatics work includes data standards (Darwin Core extensions for traits), quality control pipelines, and synthesis databases.

---

### Theory & Equation Figures

<div class="theory-figure-pair">
  <figure>
    <img src="{{ '/assets/img/wordpress/yoda_self_thinning_fig1.png' | relative_url }}" alt="Self-thinning conceptual figure: plant density declines as a power function of mean plant mass during stand development" loading="lazy">
    <figcaption>Self-thinning law — plant density declines as a power function of mean plant mass as a stand develops, a foundational prediction of metabolic scaling theory.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/wordpress/yoda_self_thinning_fig2.png' | relative_url }}" alt="Self-thinning scaling derivation: allometric exponents derived from metabolic scaling first principles" loading="lazy">
    <figcaption>Derivation of self-thinning exponents from allometric first principles — underpinning current lab work on forest structure, carbon dynamics, and demography.</figcaption>
  </figure>
</div>

