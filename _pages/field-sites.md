---
layout: page
title: field sites
permalink: /field-sites/
description: Long-term research sites and field programs
nav: true
nav_order: 3.8
---

<style>
/* Remove the global paragraph max-width cap — let text fill the page container on this page */
.post p, .post li { max-width: none !important; }
</style>

## Field Sites & Long-Term Research

The lab works in many places around the globe, but much of our field work has focused on three primary systems: (i) long-term dynamics within a tropical forest in the Area de Conservacion Guanacaste, Costa Rica; (ii) an elevation transect at the Rocky Mountain Biological Lab in Colorado; and (iii) a global network of Gentry forest plots across latitudinal and elevational gradients. We also co-organize an international Plant Functional Trait Course program.

---

### (1) San Emilio Forest Dynamics Plot (SEFDP)

We organize a long-term forest dynamics plot in Santa Rosa National Park, Area de Conservacion Guanacaste — the largest and longest-running forest dynamics plot in the New World, now part of the [ForestGEO global forest network](https://forestgeo.si.edu/sites/san-emilio).

The SEFDP was originally censused in 1976 by George Stevens and Stephen Hubbell. All woody stems ≥ 3 cm diameter within a ~15 ha plot were measured and mapped. The plot was recensused in 1995–96, again in 2006–07, and most recently in a full resurvey in 2019–2021 (ForestGEO protocols, stems ≥ 1 cm). The plot contains approximately 50,000 individual trees of ~200 woody species. Research focuses on tree population dynamics, trait-based and ecophysiological approaches, and the influence of local soil and climate on forest change over nearly 50 years.

<div class="photo-pair">
  <figure>
    <img src="{{ "/assets/img/field/sefdp_diameter_measure.jpg" | relative_url }}" alt="Researcher measuring Guanacaste tree diameter at San Emilio FDP, Costa Rica" loading="lazy">
    <figcaption>Measuring a Guanacaste tree (<em>Enterolobium cyclocarpum</em>) during the 2019–2021 SEFDP census. Photo: ForestGEO / Flickr.</figcaption>
  </figure>
  <figure>
    <img src="{{ "/assets/img/field/sefdp_forest_canopy.jpg" | relative_url }}" alt="San Emilio Forest Dynamics Plot canopy view, Costa Rica" loading="lazy">
    <figcaption>Forest canopy at the San Emilio FDP — a seasonally dry tropical forest in the Área de Conservación Guanacaste. Photo: ForestGEO / Flickr.</figcaption>
  </figure>
</div>

---

### (2) Rocky Mountain Biological Laboratory (RMBL)

Since 2003 we have been monitoring ecosystem carbon fluxes, species composition and turnover, and phylogenetic and functional trait composition of montane to alpine plant communities across an elevational gradient in Gothic, Colorado. This long-term study forges links between physical environment variation (temperature and precipitation with elevation), functional trait composition, and whole-ecosystem carbon and water fluxes. The mountainous landscape at RMBL spans warm wet meadows to cold dry ridge tops, providing a wide range of physical and biological conditions ideal for testing scaling and trait-based theory.

[RMBL website](https://www.rmbl.org/)

<div class="photo-pair">
  <figure>
    <img src="{{ "/assets/img/field/rmbl_fieldwork.jpg" | relative_url }}" alt="RMBL Colorado field site" loading="lazy">
    <figcaption>Field work at the elevational gradient transect, Gothic, Colorado.</figcaption>
  </figure>
  <figure>
    <img src="{{ "/assets/img/field/rmbl_alpine.jpg" | relative_url }}" alt="Alpine meadow at Rocky Mountain Biological Laboratory" loading="lazy">
    <figcaption>Alpine meadow — upper end of the RMBL elevational gradient.</figcaption>
  </figure>
</div>

---

<a id="rmbl-transplant-project"></a>
### (3) RMBL Transplant Project (Climate Change Experiment)

The [RMBL Climate Change Experiment](https://rmblclimatechangeexperiment.wordpress.com/) is a whole-community transplant experiment in the East River watershed near Crested Butte, Colorado. Beginning in 2017, intact 0.5 m2 meadow turf blocks (plants plus soils) were moved up and down a ~400 m elevational gradient in Washington Gulch to simulate rapid climate shifts under controlled field conditions.

This design allows us to test both direct climate effects and indirect biotic effects on plant communities by immediately exposing the same community structure to warmer or cooler environments. Research integrates functional trait measurements, carbon and water fluxes, and species cover/height tracking to quantify community and ecosystem responses.

Project details:
- [Project Home](https://rmblclimatechangeexperiment.wordpress.com/)
- [History](https://rmblclimatechangeexperiment.wordpress.com/history/)
- [Research Methods](https://rmblclimatechangeexperiment.wordpress.com/research/)

<div class="photo-pair" id="transplant-photo-pair">
  <figure>
    <img id="transplant-img-0" src="{{ '/assets/img/transplant/img_5119.jpeg' | relative_url }}"
         alt="RMBL transplant experiment field plot, Washington Gulch" loading="lazy">
    <figcaption id="transplant-cap-0">Whole-community transplant plots in Washington Gulch, Crested Butte. Source: <a href="https://rmblclimatechangeexperiment.wordpress.com/" target="_blank" rel="noopener">RMBL Climate Change Experiment</a>.</figcaption>
  </figure>
  <figure>
    <img id="transplant-img-1" src="{{ '/assets/img/transplant/img_4628.jpeg' | relative_url }}"
         alt="Field crew working in alpine meadow, RMBL transplant project" loading="lazy">
    <figcaption id="transplant-cap-1">Field deployment and monitoring of transplanted meadow communities. Source: <a href="https://rmblclimatechangeexperiment.wordpress.com/" target="_blank" rel="noopener">RMBL Climate Change Experiment</a>.</figcaption>
  </figure>
</div>
<p style="text-align:center;margin-top:0.3rem;">
  <button id="transplant-shuffle-btn"
          onclick="transplantShuffle()"
          style="font-size:0.8rem;padding:0.25rem 0.9rem;border:1px solid var(--global-divider-color,#ccc);border-radius:4px;background:transparent;cursor:pointer;color:var(--global-text-color);opacity:0.7;"
          title="Show different photos from the RMBL Climate Change Experiment">
    ↺ shuffle photos
  </button>
</p>

<script>
(function () {
  var base = '{{ "/assets/img/transplant/" | relative_url }}';
  var photos = [
    { src: 'img_4597.jpeg', alt: 'Transplant meadow turf blocks, Washington Gulch' },
    { src: 'img_4628.jpeg', alt: 'Field crew during transplant setup, RMBL' },
    { src: 'img_4699.jpeg', alt: 'Alpine meadow transplant plots, East River watershed' },
    { src: 'img_4955.jpeg', alt: 'Transplant experiment plots, Washington Gulch' },
    { src: 'img_4991.jpeg', alt: 'Monitoring transplanted meadow communities, RMBL' },
    { src: 'img_5105.jpeg', alt: 'Field measurements in transplant plots' },
    { src: 'img_5106.jpeg', alt: 'Plant community sampling, RMBL transplant project' },
    { src: 'img_5119.jpeg', alt: 'Transplant plots and alpine landscape, Washington Gulch' },
    { src: 'img_5130.jpeg', alt: 'Transplanted turf block in alpine meadow' },
    { src: '67c37ce8-1000-4dd8-87e8-78ca46e5793f.jpg', alt: 'Overview of transplant experimental design' },
    { src: '11e467e7-68c8-493a-9275-d324db8e05c6_1_105_c.jpeg', alt: 'Field crew at RMBL transplant site' },
    { src: '25a758ae-621d-4ce9-a8c7-951b5c330c96_1_105_c.jpeg', alt: 'Meadow plant community, transplant experiment' },
    { src: '6b088f65-b6cd-4af7-b24b-a67796c4a2b7_1_105_c.jpeg', alt: 'Transplant plot measurement, RMBL' },
    { src: 'bdcfc73d-1c15-4a94-bf06-ca3b36dd5d51_1_105_c.jpeg', alt: 'Alpine vegetation at transplant site' },
    { src: 'd130cc2b-2843-45fa-846d-eb67af11ac99_1_105_c.jpeg', alt: 'Field data collection, RMBL transplant project' },
    { src: '951d70f5-aaf8-474c-b1bf-a7bc9e55bd85_1_105_c.jpeg', alt: 'Plant community monitoring, Washington Gulch' },
    { src: 'f61119ba-6a77-4d4b-9ca9-957a4fc4f087_1_105_c.jpeg', alt: 'RMBL transplant experiment field site' }
  ];

  var current = [8, 1]; // initial indices matching the default src above (img_5119, img_4628)

  function pick2() {
    var pool = photos.map(function(_, i) { return i; })
                     .filter(function(i) { return i !== current[0] && i !== current[1]; });
    var a = pool[Math.floor(Math.random() * pool.length)];
    pool = pool.filter(function(i) { return i !== a; });
    var b = pool[Math.floor(Math.random() * pool.length)];
    return [a, b];
  }

  window.transplantShuffle = function () {
    var next = pick2();
    var imgs = [document.getElementById('transplant-img-0'), document.getElementById('transplant-img-1')];
    imgs.forEach(function(img, j) {
      img.style.transition = 'opacity 0.3s';
      img.style.opacity = '0';
      setTimeout(function() {
        var p = photos[next[j]];
        img.src = base + p.src;
        img.alt = p.alt;
        img.style.opacity = '1';
      }, 300);
    });
    current = next;
    // prefetch remaining photos
    photos.forEach(function(p) {
      var pre = new Image();
      pre.src = base + p.src;
    });
  };

  // prefetch all on first load
  photos.forEach(function(p) { var pre = new Image(); pre.src = base + p.src; });
})();
</script>

---

### (4) Plant Functional Trait Courses (PFTC)

Our international [Plant Functional Trait Courses](https://plantfunctionaltraitscourses.w.uib.no/) offer hands-on training in trait measurement, data synthesis, and trait-based ecology within real-world field settings. Students plan and execute field research projects, collect and document plant functional trait data, and analyze results using trait-based approaches within climate change and ecosystem ecology. We work along elevational and climate gradients in **Norway, Colorado (USA), Peru, China**, and additional countries including Chile and South Africa.

<div class="photo-pair">
  <figure>
    <img src="{{ "/assets/img/field/pftc_peru_students.jpeg" | relative_url }}" alt="PFTC student researchers in Peru" loading="lazy">
    <figcaption>PFTC students collecting functional trait data, Peru.</figcaption>
  </figure>
  <figure>
    <img src="{{ "/assets/img/field/pftc5_peru.jpeg" | relative_url }}" alt="PFTC 5 fieldwork, Peru" loading="lazy">
    <figcaption>PFTC 5 field course, Andes, Peru.</figcaption>
  </figure>
</div>

---

### (5) ABERG / CHAMBASA

The **Andes Biodiversity and Ecosystems Research Group (ABERG)** is an international consortium co-led by [Yadvinder Malhi](https://www.eci.ox.ac.uk/people/ymalhi) (Oxford University) and Brian Enquist (University of Arizona) that uses the eastern Andean slope of southern Peru as a living laboratory for biodiversity and ecosystem science. The core study area — the Kosñipata Valley in Madre de Dios / Cusco, within and adjacent to **Manu National Park and Biosphere Reserve** — spans nearly 3,500 m of elevation from lowland Amazonian forest (~400 m) through lower and upper montane cloud forest to puna grasslands (~3,800 m), traversing one of the steepest gradients in temperature, precipitation, and biodiversity on Earth.

Within ABERG, the **CHAnging Montane Biodiversity And Structure Along the Andes (CHAMBASA)** program maintains a network of permanent forest census and functional trait measurement plots along this elevation transect. CHAMBASA plots are part of the Global Ecosystems Monitoring (GEM) network based at Oxford and are stationed at key field sites managed by the [Amazon Conservation Association](https://www.andesconservation.org/), including **Wayqecha** (~3,000 m, upper montane cloud forest) and **Villa Carmen** (~580 m, premontane forest), with additional plots at San Pedro (~1,500 m), Trocha Union (~1,855 m), and Pantiacolla (~450 m) near the lowland Amazon. At each site, we conduct standardized forest census (stems, diameter, height), leaf and wood functional trait measurement, and — in collaboration with Carnegie Institution scientists Gregory Asner and Roberta Martin — airborne hyperspectral imaging that scales plot-level traits to landscape and regional extents.

Research at ABERG/CHAMBASA addresses how carbon stocks, net primary productivity, forest structure, and plant functional traits respond to systematic variation in temperature, cloud immersion, and solar radiation across the gradient. Key findings include: the dominant role of declining solar radiation (not temperature alone) in driving reduced forest productivity at higher elevations ([Fyllas et al. 2017, *Ecology Letters*](https://doi.org/10.1111/ele.12770)); the large-scale consistency of trait-based allometric scaling theory across a 20°C temperature span ([Enquist et al. 2017, *Global Ecology and Biogeography*](https://doi.org/10.1111/geb.12645)); remote sensing of canopy functional trait distributions from airborne hyperspectral imagery ([Asner et al. 2017, *New Phytologist*](https://doi.org/10.1111/nph.14303); [Durán et al. 2019, *Science Advances*](https://doi.org/10.1126/sciadv.aaw8114)); the predicted darkening of tropical forest leaves under climate change ([Doughty et al. 2018, *Nature Climate Change*](https://doi.org/10.1038/s41558-018-0319-7)); and the structural and defensive roles of leaf venation networks along the gradient ([Blonder et al. 2017, *Ecology*](https://doi.org/10.1002/ecy.1731)). Since 2018, the monitoring network has extended into the puna ecosystem above tree line in collaboration with the [Plant Functional Trait Courses (PFTC)](/field-sites/#4-plant-functional-trait-courses-pftc) program.

Key collaborators include Norma Salinas and Walter Huaraca Huasco (UNSAAC, Cusco), Miles Silman (Wake Forest), Sandra Díaz (CONICET), Lisa Bentley (Sonoma State), Alexander Shenkin (Oxford), Benjamin Blonder (UC Berkeley), Gregory Goldsmith (Chapman), and Christopher Doughty (Northern Arizona University).

<div class="photo-pair">
  <figure>
    <img src="{{ '/assets/img/field/aberg_andes.jpeg' | relative_url }}" alt="ABERG elevational transect fieldwork, Andes cloud forest" loading="lazy">
    <figcaption>Elevational transect fieldwork — cloud forest to Puna grassland, Andes.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/wordpress/dsc_3443.jpeg' | relative_url }}" alt="Andean snowcap peaks above the ABERG study gradient, Peru" loading="lazy">
    <figcaption>The high Andes snowcap above the ABERG gradient — spanning nearly 3.5 km of elevation.</figcaption>
  </figure>
</div>

---

### (6) Forest MacroSystems Network

The [Forest MacroSystems Network](https://www.forestmacrosystems.org/) consists of nine forest monitoring sites arrayed across a broad latitudinal climate gradient. Since 2011 we have been monitoring annual tree growth and mortality using standardized Gentry-style plots. Sites span: **BCI Panama · Luquillo Puerto Rico · Guanacaste Costa Rica · Coweeta North Carolina · Harvard Forest Massachusetts · Niwot Ridge Colorado · Mt. Lemmon Arizona · HJ Andrews Oregon · British Columbia Canada**.

<div class="photo-pair">
  <figure>
    <img src="{{ "/assets/img/field/fms_network_overview.jpg" | relative_url }}" alt="Forest MacroSystems network overview" loading="lazy">
    <figcaption>Forest MacroSystems Network — nine long-term monitoring sites across a latitudinal gradient.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/wordpress/img_5586.jpeg' | relative_url }}" alt="Researchers at a Forest MacroSystems Network temperate forest monitoring site" loading="lazy">
    <figcaption>Ground-level forest monitoring — one of nine sites across the latitudinal network.</figcaption>
  </figure>
</div>

---

*For access to data from these sites, contact the lab or visit [biendata.org](https://biendata.org/).*

