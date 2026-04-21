---
layout: page
title: resources
permalink: /software/
description: Open-source tools and databases from the Enquist Lab
nav: true
nav_order: 6
---

## Software & Open Data

Code and public tools associated with current and ongoing lab projects.

- [Enquist Lab on GitHub](https://github.com/EnquistLab)
- [Oxford Ecosystems Lab on GitHub](https://github.com/OxfordEcosystemsLab)
- [BIEN Data Portal](https://biendata.org/)

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

- [tnrs.biendata.org](https://tnrs.biendata.org/)
- [GitHub source](https://github.com/iPlantCollaborativeOpenSource/TNRS)
- Featured in *Nature* (2011)

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

### Additional Tools & Datasets

| Resource | Description | Link |
|---|---|---|
| SALVIAS | Plant inventory plots database | [salvias.net](https://www.salvias.net/) |
| BIEN Traits | Validated plant trait measurements | [biendata.org](https://biendata.org/) |
| GBIF / TNRS | Taxonomic resolution tools | [tnrs.biendata.org](https://tnrs.biendata.org/) |

