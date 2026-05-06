---
layout: page
title: research
permalink: /research/
description: Current research themes and projects in the Enquist Macroecology Lab
nav: false
nav_order: 3
---

## Research Program

<nav class="section-jump-nav" aria-label="Research section navigation">
  <div class="section-jump-nav__header">
    <span class="section-jump-nav__label">Jump to theme</span>
  </div>
  <div class="section-jump-nav__links">
    <a class="section-jump-nav__link" href="#theory">Theory</a>
    <a class="section-jump-nav__link" href="#metabolic-scaling-functional-biology">Metabolic Scaling</a>
    <a class="section-jump-nav__link" href="#trait-based-ecology">Trait-Based Ecology</a>
    <a class="section-jump-nav__link" href="#trait-driver-theory-functional-ecology">Trait Driver Theory</a>
    <a class="section-jump-nav__link" href="#bien-botanical-information-ecology-network">BIEN</a>
    <a class="section-jump-nav__link" href="#global-change-biology">Global Change Biology</a>
    <a class="section-jump-nav__link" href="#long-term-ecology">Long-Term Ecology</a>
    <a class="section-jump-nav__link" href="#opentraits-biodiversity-informatics">OpenTraits</a>
  </div>
</nav>

<figure class="field-photo">
  <img src="{{ "/assets/img/field/brian_field.jpg" | relative_url }}" alt="Brian Enquist conducting field measurements" loading="lazy">
  <figcaption>Field measurements — connecting individual-level physiology to ecosystem-scale patterns.</figcaption>
</figure>

Our lab develops theory and data-driven tools to explain how biodiversity is organized across scales, and how it is changing under climate and land-use pressure.

We organize our work as a connected process: observations and traits → scaling and trait-based theory → predictive models → uncertainty-aware ecological forecasting.

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

### Theory {#theory}

The lab's empirical programs are grounded in two interconnected theoretical frameworks — **Metabolic Scaling Theory (MST)** and **Trait Driver Theory (TDT)** — that together aim to explain biological organization from cells to ecosystems and predict how communities respond to environmental change. Both frameworks are mathematically explicit: they generate quantitative, falsifiable predictions that can be confronted with data and refined.

#### Metabolic Scaling Theory (MST) {#metabolic-scaling-theory}

Metabolic Scaling Theory rests on a central insight: the geometry of biological distribution networks — the branching vascular systems of plants and animals — imposes universal constraints on how metabolic rate scales with body size. West, Brown, and Enquist showed that a space-filling, area-preserving fractal vascular network minimizes energy dissipation and thereby generates the ¾-power scaling of metabolic rate with body mass, $$B \propto M^{3/4}$$, observed across more than 27 orders of magnitude ([West, Brown & Enquist 1997](https://doi.org/10.1126/science.276.5309.122)). This is not merely an empirical regularity — it is a derived consequence of network geometry and fluid-transport physics.

From this foundation, the theory generates a unified set of predictions. Growth rates, lifespan, reproductive output, and the turnover of energy and biomass all scale predictably with body size and temperature ([West, Brown & Enquist 1999](https://doi.org/10.1126/science.284.5420.1677)). In plants, the fractal vascular network constrains stem diameter, height, and leaf-area allometries ([West, Enquist & Brown 1999](https://doi.org/10.1038/23040)), and metabolic constraints set population density and above-ground biomass across forests ([Enquist, Brown & West 1998](https://doi.org/10.1038/28048)). Temperature enters through a Boltzmann–Arrhenius activation-energy factor, grounding MST thermodynamically and connecting it directly to global-change projections.

Brown et al. extended MST into the **Metabolic Theory of Ecology (MTE)**, showing that the same mass and temperature scaling permeates population dynamics, species diversity gradients, ecosystem energy flux, and elemental stoichiometry ([Brown et al. 2004](https://doi.org/10.1890/03-9000)). Current Enquist Lab work extends and tests MST predictions at ecosystem scale — connecting allometric constraints to forest carbon stocks, demography, and the structure of plant communities across biomes.

**Scope:** subcellular metabolic pathways to biome-level carbon budgets.
**Goal:** derive macroecological patterns from first principles of physics and network geometry.
**Applications:** forest biomass and carbon modeling, demographic forecasting, climate-scaling of plant productivity, earth system model parameterization.

**Key papers:**
- [West, Brown & Enquist (1997)](https://doi.org/10.1126/science.276.5309.122) — fractal vascular networks and the ¾ scaling law
- [West, Brown & Enquist (1999)](https://doi.org/10.1126/science.284.5420.1677) — fractal geometry and allometric scaling across life
- [West, Enquist & Brown (1999)](https://doi.org/10.1038/23040) — general model for plant vascular structure and allometry (*Nature*)
- [Enquist, Brown & West (1998)](https://doi.org/10.1038/28048) — plant population density and biomass scaling
- [Brown et al. (2004)](https://doi.org/10.1890/03-9000) — Metabolic Theory of Ecology
- [West, Enquist & Brown (2009)](https://doi.org/10.1073/pnas.0812294106) — a general quantitative theory of forest structure and dynamics

#### Trait Driver Theory (TDT) {#trait-driver-theory}

While MST explains size- and temperature-dependent variation in metabolic flux, **Trait Driver Theory** addresses a complementary question: why do communities assemble the functional trait distributions they do, and how will those distributions shift as environments change? TDT is a quantitative, mechanistic framework that predicts the mean, variance, and shape of functional trait distributions in a local community as a function of environmental drivers — temperature, water availability, disturbance, and resource supply ([Enquist et al. 2015](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065250415000070)).

The core logic is probabilistic and multi-scale. At the regional scale, the pool of available species defines a prior distribution of trait values shaped by evolutionary history and dispersal. At the local scale, environmental filters and biotic interactions select from that pool, shifting the realized trait distribution in predictable directions. TDT formalizes this filtering mathematically: environmental drivers compress, shift, or broaden the trait distribution, with measurable consequences for community function. Because intraspecific trait variation (ITV) contributes substantially to total community-level trait variance, TDT explicitly partitions variation across levels — individual, population, species, and community — rather than collapsing it to species means ([Enquist et al. 2019](https://www.nature.com/articles/s41477-019-0506-6)).

TDT bridges scales that are often treated separately in ecology: individual physiology sets the trait values that are possible; evolutionary history determines what is available in a regional pool; environment determines what is favored locally; and the aggregate of these processes produces the community-level functional fingerprint that shapes carbon exchange, water flux, and competitive dynamics at ecosystem scale. This positions TDT as a theoretical spine connecting leaf-level measurements to global biodiversity forecasting.

**Scope:** individual leaf traits to continental-scale functional diversity gradients.
**Goal:** build a predictive, mathematically grounded theory of community assembly and ecosystem function based on trait distributions.
**Applications:** forecasting community trait shifts under climate change, explaining elevational and latitudinal diversity gradients, linking remote-sensing spectral signatures to functional state, improving land-surface model trait parameterizations.

**Key papers:**
- [Enquist et al. (2015)](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065250415000070) — original TDT framework and predictions
- [Enquist et al. (2019)](https://www.nature.com/articles/s41477-019-0506-6) — extending TDT with intraspecific variation (*Nature Plants*)

---

### Metabolic Scaling & Functional Biology

We develop and extend metabolic scaling theory (West, Brown, and Enquist 1997; 1999) to predict how growth, mortality, and resource use scale with body size and temperature. Current work applies these principles to forest structure, carbon dynamics, and demography.

**Key questions:**
- How do allometric constraints shape plant architecture and forest structure?
- Can metabolic scaling theory predict ecosystem carbon fluxes and turnover?
- What are the evolutionary origins of scaling relationships?

---

### Trait-Based Ecology

<figure class="field-photo">
  <img src="{{ '/assets/img/wordpress/dsc_3443.jpeg' | relative_url }}" alt="Snow-covered Andean peaks above alpine field terrain" loading="lazy">
  <figcaption>Trait ecology links leaf- and plant-level strategies to mountain-scale environmental gradients.</figcaption>
</figure>

Plant functional traits — measurable attributes such as leaf size, wood density, plant height, and water-use efficiency — encode how organisms interact with their environment, competitors, and resources. The lab's trait-based ecology program spans from individual leaves to global biomes, with the unifying goal of building a predictive science of plant form, function, and response to change.

**From traits to prediction.** Our approach treats traits not merely as descriptors but as mechanistic currencies that link physiology, community assembly, and ecosystem function. By measuring how traits vary across individuals, species, and environments — and by integrating those measurements with metabolic theory — we develop frameworks that forecast how plant communities will respond to climate change, land-use pressure, and other global drivers.

**Core contributions and ongoing work:**
- Developing and testing [Trait Driver Theory (TDT)](https://www.nature.com/articles/s41477-019-0506-6), a general framework predicting how trait distributions in a community shift as environmental conditions change ([Enquist et al. 2015](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065250415000070))
- Quantifying intraspecific trait variation (ITV) and its role in community stability, climate buffering, and ecological forecasting — including new bootstrap uncertainty methods ([traitstrap](https://cran.r-project.org/package=traitstrap))
- Integrating remotely sensed spectral data with ground-based trait measurements to scale functional diversity from plots to continents (Durán et al. 2019 *Science Advances*; Wieczynski et al. 2022 *Ecography*)
- Contributing to global trait databases including TRY, OpenTraits, and BIEN, and establishing open-science standards for trait data ([Gallagher et al. 2020](https://doi.org/10.1038/s41559-020-1109-6) *Nature Ecology & Evolution*; Keller et al. 2023 *Methods in Ecology & Evolution*)
- Connecting trait variation to forest carbon and productivity at landscape and regional scales

**Forward look.** The next frontier is trait-based ecological forecasting: using measured trait distributions — including their uncertainty — to predict community-level responses to novel climates, assess biodiversity vulnerability, and improve land-surface models. This requires integrating trait data with demographic models, remote sensing, and process-based earth system frameworks. We are actively building these pipelines through BIEN, OpenTraits, and collaborative field programs including [PFTC]({{ '/resources/' | relative_url }}).

---

### Trait Driver Theory & Functional Ecology

[Trait Driver Theory (TDT)](https://www.nature.com/articles/s41477-019-0506-6) is a quantitative, mechanistic framework that predicts how the statistical distribution of functional traits in a community responds to environmental drivers — temperature, water availability, disturbance, and land use. TDT bridges individual-level physiology, community assembly, and ecosystem function, providing a theoretical spine for the lab's broader trait-based program ([Enquist et al. 2015](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065250415000070)).

Applications include:
- Predicting community trait shifts under climate change
- Understanding trait-environment relationships across elevational and latitudinal gradients
- Linking remote sensing spectral signatures to functional diversity
- Informing carbon-cycle and land-surface models with trait-based predictions

---

### BIEN: Botanical Information & Ecology Network

<figure class="field-photo">
  <img src="{{ '/assets/img/wordpress/dsc_3236.jpeg' | relative_url }}" alt="Cloud-forest mountain slope along an Andean elevational transect" loading="lazy">
  <figcaption>BIEN synthesis products integrate occurrence, trait, and climate data across regional and continental gradients.</figcaption>
</figure>

<img src="{{ '/assets/img/wordpress/bien_logo_notext-1.png' | relative_url }}" alt="BIEN — Botanical Information and Ecology Network" style="max-width:220px;width:100%;display:block;margin:0.6rem 0 1rem;">

The [BIEN project](https://biendata.org/) compiles and standardizes occurrence records, trait measurements, and plot data for vascular plants in the Western Hemisphere. It is one of the largest plant biodiversity synthesis efforts globally. The database integrates herbarium specimens, citizen-science observations, and plot inventories spanning roughly 1800s–present, with taxonomic reconciliation against a versioned plant name backbone and coordinate-level QA filtering.

**Citation:** [Enquist et al. (2026)](https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/2041-210x.70274) *Methods in Ecology and Evolution*

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
  <small><a href="https://github.com/benquist/BIEN_Trait_Shiny_App#readme" target="_blank" rel="noopener">GitHub README</a></small>
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

The Enquist Lab is a co-founding member and active contributor to the [Open Traits Network (OTN)](https://opentraits.org/) — a global, decentralized community of researchers and institutions working to standardize and integrate trait data across all organisms. OTN is guided by Open Science principles: open methods, open source, and open data.

**What the OTN does.**
The network maintains a [global registry of trait-based initiatives](https://opentraits.org/datasets.html), shares reproducible workflows and tools for aggregating trait data, advocates for free data flow and appropriate attribution of effort, and works toward a shared *trait core* — a minimal interoperable vocabulary that facilitates synthesis across databases. The registry currently spans hundreds of datasets, covering plants, animals, fungi, and microbes across all biomes.

**Our contributions and roles.**
Lab members have contributed to OTN in multiple capacities:
- **Co-authoring the network's foundational paper**: [Gallagher et al. (2020)](https://doi.org/10.1038/s41559-020-1109-6) *Nature Ecology & Evolution* — introducing OTN and its open-science vision for trait data across all life.
- **Best-practice guidance**: Enquist is a contributing author on [Keller et al. (2023)](https://doi.org/10.1111/2041-210X.14033) *Methods in Ecology and Evolution* — "Ten (mostly) simple rules to future-proof trait data in ecological and evolutionary sciences" — an open, community-driven resource now hosted at [opentraits.org/best-practices.html](https://opentraits.org/best-practices.html).
- **Tool development**: Contributing to [`traitdataform`](https://ecologicaltraitdata.github.io/traitdataform/) and [`traitstrap`](https://cran.r-project.org/package=traitstrap) for standardized trait formatting and bootstrap-based trait gap-filling.
- **Data pipelines**: Building interoperable ingestion workflows that connect BIEN, TRY, FRED, and other databases into OTN-compatible formats with full provenance tracking.

**Five OTN principles the lab practices:**
1. Openly sharing data, methods, protocols, code, and workflows
2. Appropriately citing original data collectors and providing scholarly credit
3. Providing full metadata alongside trait observations
4. Collecting trait data following reproducible, standardized methods
5. Providing training resources in trait collection and database construction

**Key connected databases.**
The lab's biodiversity informatics work connects across a growing ecosystem of open trait and occurrence resources:

| Resource | Scope |
|----------|-------|
| [TRY Plant Trait Database](https://www.try-db.org/) | Global plant traits, >15M records |
| [BIEN](https://bien.nceas.ucsb.edu/bien/) | Neotropical plant occurrence and traits |
| [FRED](https://roots.ornl.gov/) | Fine-root traits across ecosystems |
| [GBIF](https://www.gbif.org/) | Global biodiversity occurrence records |
| [GIFT](https://gift.uni-goettingen.de/) | Plant species richness and functional traits |
| [OTN Dataset Registry](https://opentraits.org/datasets.html) | Cross-taxon trait database catalog |

**Biodiversity informatics more broadly.**
Beyond trait databases, the lab contributes to informatics infrastructure for ecological synthesis: Darwin Core extensions for trait data, quality-control pipelines for taxonomic reconciliation, and open workflows connecting field observations to continental-scale synthesis products. This infrastructure underpins our forecasting work through BIEN and enables reproducible, uncertainty-aware macroecology at global scale.

