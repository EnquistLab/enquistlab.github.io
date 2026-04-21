---
layout: page
title: resources
permalink: /software/
description: Open-source tools and databases from the Enquist Lab
nav: true
nav_order: 5
---

## Software & Open Data

Code and public tools associated with current and ongoing lab projects.

- [Enquist Lab on GitHub](https://github.com/EnquistLab)
- [BIEN](https://biendata.org/)

### Additional Lab Resources

- [Teaching and training]({{ '/teaching/' | relative_url }})
- [News archive]({{ '/news/' | relative_url }})
- [Blog]({{ '/blog/' | relative_url }})
- [Press and media]({{ '/press-media/' | relative_url }})

---

### BIEN R Package

The `BIEN` R package provides programmatic access to the Botanical Information and Ecology Network database, including occurrence records, trait data, species range maps, and plot data for New World plants.

- **CRAN:** [BIEN on CRAN](https://cran.r-project.org/package=BIEN)
- **GitHub:** [EnquistLab/BIEN](https://github.com/EnquistLab/BIEN)
- **Citation:** Maitner et al. (2018) *Methods in Ecology and Evolution*

```r
install.packages("BIEN")
library(BIEN)
# Get all records for a species
sp <- BIEN_occurrence_species("Pinus ponderosa")
```

---

### BIEN Data Portal

The BIEN GeoSpatial portal provides web-based access to New World plant occurrence, range, and trait data with QA/QC, taxonomic harmonization, and geographic filtering.

- **Portal:** [biendata.org](https://biendata.org/)

![BIEN network logo]({{ '/assets/img/wordpress/bien_logo_notext-1.png' | relative_url }})

---

### APIs and Services

- **Taxonomic Name Resolution Service (TNRS):** standardize plant scientific names, spelling variants, and synonyms
- **Native Species Resolver (NSR):** determine whether records are native or introduced by political geography
- **BIEN data access tools:** retrieval of occurrences, traits, and range products

---

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

