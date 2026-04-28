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

### Trait-Based Ecology

Plant functional traits — measurable attributes such as leaf size, wood density, plant height, and water-use efficiency — encode how organisms interact with their environment, competitors, and resources. The lab's trait-based ecology program spans from individual leaves to global biomes, with the unifying goal of building a predictive science of plant form, function, and response to change.

**From traits to prediction.** Our approach treats traits not merely as descriptors but as mechanistic currencies that link physiology, community assembly, and ecosystem function. By measuring how traits vary across individuals, species, and environments — and by integrating those measurements with metabolic theory — we develop frameworks that forecast how plant communities will respond to climate change, land-use pressure, and other global drivers.

**Core contributions and ongoing work:**
- Developing and testing [Trait Driver Theory (TDT)](https://www.nature.com/articles/s41477-019-0506-6), a general framework predicting how trait distributions in a community shift as environmental conditions change
- Quantifying intraspecific trait variation (ITV) and its role in community stability, climate buffering, and ecological forecasting — including new bootstrap uncertainty methods ([traitstrap](https://cran.r-project.org/package=traitstrap))
- Integrating remotely sensed spectral data with ground-based trait measurements to scale functional diversity from plots to continents (Durán et al. 2019 *Science Advances*; Wieczynski et al. 2022 *Ecography*)
- Contributing to global trait databases including TRY, OpenTraits, and BIEN, and establishing open-science standards for trait data ([Gallagher et al. 2020](https://doi.org/10.1038/s41559-020-1109-6) *Nature Ecology & Evolution*; Keller et al. 2023 *Methods in Ecology & Evolution*)
- Connecting trait variation to forest carbon and productivity at landscape and regional scales

**Forward look.** The next frontier is trait-based ecological forecasting: using measured trait distributions — including their uncertainty — to predict community-level responses to novel climates, assess biodiversity vulnerability, and improve land-surface models. This requires integrating trait data with demographic models, remote sensing, and process-based earth system frameworks. We are actively building these pipelines through BIEN, OpenTraits, and collaborative field programs including [PFTC]({{ '/resources/' | relative_url }}).

---

### Trait Driver Theory & Functional Ecology

[Trait Driver Theory (TDT)](https://www.nature.com/articles/s41477-019-0506-6) is a quantitative, mechanistic framework that predicts how the statistical distribution of functional traits in a community responds to environmental drivers — temperature, water availability, disturbance, and land use. TDT bridges individual-level physiology, community assembly, and ecosystem function, providing a theoretical spine for the lab's broader trait-based program.

Applications include:
- Predicting community trait shifts under climate change
- Understanding trait-environment relationships across elevational and latitudinal gradients
- Linking remote sensing spectral signatures to functional diversity
- Informing carbon-cycle and land-surface models with trait-based predictions

---

### BIEN: Botanical Information & Ecology Network

<img src="{{ '/assets/img/wordpress/bien_logo_notext-1.png' | relative_url }}" alt="BIEN — Botanical Information and Ecology Network" style="max-width:220px;width:100%;display:block;margin:0.6rem 0 1rem;">

The [BIEN project](https://biendata.org/) compiles and standardizes occurrence records, trait measurements, and plot data for vascular plants in the Western Hemisphere. It is one of the largest plant biodiversity synthesis efforts globally. The database integrates herbarium specimens, citizen-science observations, and plot inventories spanning roughly 1800s–present, with taxonomic reconciliation against a versioned plant name backbone and coordinate-level QA filtering.

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

#### BIEN Interactive Apps

<div class="bien-apps-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem;margin:1rem 0;">

<div style="border:1px solid var(--global-divider-color,#ddd);border-radius:6px;padding:1rem;">
  <strong><a href="https://benquist.shinyapps.io/bien-species-shinyapp/" target="_blank" rel="noopener">▶ BIEN Species Explorer</a></strong><br>
  <span style="font-size:0.88rem;">Browse occurrence records and range maps for ~120,000 Western Hemisphere plant species. Filter by native status, political unit, and elevation; download georeferenced records and range polygons.</span><br>
  <small><a href="https://github.com/benquist/BIEN-SpeciesShinyApp#readme" target="_blank" rel="noopener">GitHub README</a></small>
</div>

<div style="border:1px solid var(--global-divider-color,#ddd);border-radius:6px;padding:1rem;">
  <strong><a href="https://benquist.shinyapps.io/bien-traits-shinyapp/" target="_blank" rel="noopener">▶ BIEN Traits Explorer</a></strong><br>
  <span style="font-size:0.88rem;">Query, map, and export plant functional trait observations from the BIEN trait database. Supports multi-species input, trait-level coverage preview, mapped observations, and reproducible R export code with full provenance and citation metadata.</span><br>
  <small><a href="https://github.com/benquist/biodiversity-agents-lab/tree/main/BIEN-TraitsShinyApp#readme" target="_blank" rel="noopener">GitHub README</a></small>
</div>

<div style="border:1px solid var(--global-divider-color,#ddd);border-radius:6px;padding:1rem;">
  <strong><a href="https://benquist.shinyapps.io/bien-data-loader/" target="_blank" rel="noopener">▶ BIEN Data Loader</a></strong><br>
  <span style="font-size:0.88rem;">Upload a species list to retrieve, review, and bulk-export BIEN occurrence and trait data. Designed for batch queries and downstream biodiversity analysis workflows.</span><br>
  <small><a href="https://github.com/benquist/BIEN_Data_Loader#readme" target="_blank" rel="noopener">GitHub README</a></small>
</div>

</div>

---

### Global Change Biology

We use trait-based models, species distribution models, and process-based frameworks to project how plant communities may respond to climate change. Work includes:

- Trait-based range shift projections
- Detecting signals of climate-driven community turnover in BIEN data
- Assessing vulnerability of tropical and montane floras

**Uncertainty and transferability:** We report assumptions, data coverage limits, and scenario sensitivity when projecting biodiversity responses across regions and time. All projections are contingent on emission and land-use scenarios; results are validated where possible using spatial cross-validation, temporal holdouts, and MESS surfaces to flag extrapolation risk.

**Sampling bias:** BIEN occurrence records reflect the history of botanical collecting and citizen-science participation — roads, research stations, and well-surveyed regions are over-represented. We apply spatial thinning, bias layers, and target-group background sampling in SDM workflows to mitigate this.

---

### Collaborative Initiatives

We actively collaborate with local and international initiatives that support field work, synthesis, and training for students, postdocs, and collaborators. These collaborations include biodiversity forecasting and conservation planning efforts, including SPARC and related protected-area prioritization projects.

See [collaborators]({{ '/collaborators/' | relative_url }}) for examples.

---

### Long-Term Ecology

Our long-term work integrates repeated forest censuses, elevational transects, and distributed plot networks to quantify demographic and compositional change through time and to improve ecological prediction.

See [field sites]({{ '/field-sites/' | relative_url }}) for site details.

<figure class="field-photo" style="max-height:420px;">
  <img src="{{ '/assets/img/wordpress/rmbl-transplant-img_4955.jpeg' | relative_url }}" alt="RMBL transplant project meadow block experiment in Washington Gulch, Colorado" loading="lazy" style="height:420px;object-fit:cover;object-position:center 42%;">
  <figcaption>RMBL Transplant Project: whole-community meadow blocks moved along an elevational temperature gradient to experimentally simulate climate change. See the <a href="{{ '/field-sites/#rmbl-transplant-project' | relative_url }}">Field Sites project page</a> for design and methods.</figcaption>
</figure>

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

