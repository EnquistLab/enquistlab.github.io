---
layout: page
title: gallery
permalink: /gallery/
description: Field landscapes, research sites, and lab life
nav: false
nav_order: 7
images:
  lightbox2: true
---

<style>
/* ── Gallery grid ───────────────────────────────────────────── */
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 10px;
  margin-bottom: 2.5rem;
}

.photo-gallery a {
  display: block;
  overflow: hidden;
  border-radius: 6px;
  line-height: 0;
  transition: opacity 0.2s ease;
}

.photo-gallery a:hover {
  opacity: 0.88;
}

.photo-gallery img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 6px;
  display: block;
}

.photo-gallery a.wide {
  grid-column: span 2;
}
.photo-gallery a.wide img {
  height: 220px;
}

/* ── Theme header ──────────────────────────────────────────── */
.gallery-theme-header {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  margin: 2.5rem 0 0.6rem;
}
.gallery-theme-header h2 {
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--global-text-color);
  margin: 0;
  white-space: nowrap;
}
.gallery-theme-header::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--global-divider-color, #d8d0c4);
}

/* ── Shuffle button ──────────────────────────────────────────── */
#gallery-shuffle-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  margin: 0.5rem 0 1.5rem;
  padding: 0.35rem 0.9rem;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #3a6b40;
  background: transparent;
  border: 1.5px solid #3a6b40;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease;
}
#gallery-shuffle-btn:hover {
  background: #3a6b40;
  color: #fff;
}
</style>

Photos from field campaigns, long-term research sites, and lab gatherings across the Americas and beyond.
Click any image to open the full view.

<button id="gallery-shuffle-btn">&#x21CC; Shuffle</button>

<div id="gallery-themes-container">

<!-- ── Tropical Forests ──────────────────────────────────────────── -->
<div class="gallery-theme-block">
<div class="gallery-theme-header"><h2>Tropical Forests</h2></div>

<div class="photo-gallery" data-theme="tropical-forests">

  <a href="{{ '/assets/img/field/field_opening.jpeg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Dry tropical forest, San Emilio FDP, Area de Conservación Guanacaste, Costa Rica"
     class="wide">
    <img src="{{ '/assets/img/field/field_opening.jpeg' | relative_url }}"
         alt="Dry tropical forest opening at San Emilio Forest Dynamics Plot, Costa Rica" loading="eager">
  </a>

  <a href="{{ '/assets/img/field/sefdp_lidar.jpg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="LiDAR survey, San Emilio Forest Dynamics Plot, Costa Rica">
    <img src="{{ '/assets/img/field/sefdp_lidar.jpg' | relative_url }}"
         alt="LiDAR survey at SEFDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3236.jpeg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Tree canopy, tropical dry forest, Costa Rica">
    <img src="{{ '/assets/img/wordpress/dsc_3236.jpeg' | relative_url }}"
         alt="Tree canopy, tropical dry forest, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/ceibo.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Ceibo tree (Ceiba pentandra), dry tropical forest, Costa Rica">
    <img src="{{ '/assets/img/wordpress/ceibo.png' | relative_url }}"
         alt="Ceibo tree, dry tropical forest, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cr-1-2.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="San Emilio Forest Dynamics Plot, Costa Rica">
    <img src="{{ '/assets/img/wordpress/cr-1-2.png' | relative_url }}"
         alt="San Emilio FDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cr-2-1.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="San Emilio Forest Dynamics Plot, Costa Rica">
    <img src="{{ '/assets/img/wordpress/cr-2-1.png' | relative_url }}"
         alt="San Emilio FDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cr-3-2.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="San Emilio Forest Dynamics Plot, Costa Rica">
    <img src="{{ '/assets/img/wordpress/cr-3-2.png' | relative_url }}"
         alt="San Emilio FDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cr-4-1.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="San Emilio Forest Dynamics Plot, Costa Rica">
    <img src="{{ '/assets/img/wordpress/cr-4-1.png' | relative_url }}"
         alt="San Emilio FDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/pfeiler_forest_1__72d0b3ba.jpg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Tall forest with emergent canopy trees, tropical field site">
    <img src="{{ '/assets/img/wordpress-legacy/originals/pfeiler_forest_1__72d0b3ba.jpg' | relative_url }}"
         alt="Tall tropical forest with emergent canopy trees" loading="lazy">
  </a>

</div>
</div><!-- /.gallery-theme-block -->

<!-- ── Andean & Montane ──────────────────────────────────────────── -->
<div class="gallery-theme-block">
<div class="gallery-theme-header"><h2>Andean &amp; Montane</h2></div>

<div class="photo-gallery" data-theme="andean-elevations">

  <a href="{{ '/assets/img/wordpress-legacy/originals/dsc_4115-2__8cde5bc1.jpg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="High-elevation Andes landscape along the elevation transect, Peru"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/dsc_4115-2__8cde5bc1.jpg' | relative_url }}"
         alt="High-elevation Andes landscape, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/aberg_andes.jpeg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Andes elevation transect, PFTC research site, Peru">
    <img src="{{ '/assets/img/field/aberg_andes.jpeg' | relative_url }}"
         alt="Andes elevation transect, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3414.jpeg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="High-Andes landscape along the PFTC transect, Peru">
    <img src="{{ '/assets/img/wordpress/dsc_3414.jpeg' | relative_url }}"
         alt="High-Andes landscape, PFTC transect, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/polylepis__c3788d1a.jpg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Polylepis high-Andean woodland, Peru">
    <img src="{{ '/assets/img/wordpress-legacy/originals/polylepis__c3788d1a.jpg' | relative_url }}"
         alt="Polylepis high-Andean woodland, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/dsc_3876__461b0b78.jpg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Mountain valley and cloud forest, Andes, Peru">
    <img src="{{ '/assets/img/wordpress-legacy/originals/dsc_3876__461b0b78.jpg' | relative_url }}"
         alt="Mountain valley and cloud forest, Andes, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/dsc_9737-2__a3db9ce9.jpeg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Andean alpine zone and sky, PFTC transect, Peru">
    <img src="{{ '/assets/img/wordpress-legacy/originals/dsc_9737-2__a3db9ce9.jpeg' | relative_url }}"
         alt="Andean alpine zone and sky, Peru" loading="lazy">
  </a>

</div>
</div><!-- /.gallery-theme-block -->

<!-- ── Rocky Mountains & Alpine ──────────────────────────────────────────── -->
<div class="gallery-theme-block">
<div class="gallery-theme-header"><h2>Rocky Mountains &amp; Alpine</h2></div>

<div class="photo-gallery" data-theme="rocky-mountains">

  <a href="{{ '/assets/img/field/rmbl_alpine.jpg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Alpine meadow above the Rocky Mountain Biological Laboratory, Gothic, Colorado"
     class="wide">
    <img src="{{ '/assets/img/field/rmbl_alpine.jpg' | relative_url }}"
         alt="Alpine meadow above RMBL, Gothic, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/avery-ridge.jpg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Avery Ridge, East River watershed, Colorado">
    <img src="{{ '/assets/img/wordpress/avery-ridge.jpg' | relative_url }}"
         alt="Avery Ridge, East River watershed, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/rmbl_fieldwork.jpg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Field sampling at the Rocky Mountain Biological Laboratory, Gothic, Colorado">
    <img src="{{ '/assets/img/field/rmbl_fieldwork.jpg' | relative_url }}"
         alt="Field sampling at RMBL, Gothic, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_5119.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Transplant plots in Washington Gulch, Crested Butte — RMBL Climate Change Experiment"
     class="wide">
    <img src="{{ '/assets/img/transplant/img_5119.jpeg' | relative_url }}"
         alt="Transplant plots in Washington Gulch, Crested Butte, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_4628.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Field crew deploying transplanted turf blocks — RMBL Climate Change Experiment, Colorado">
    <img src="{{ '/assets/img/transplant/img_4628.jpeg' | relative_url }}"
         alt="Field crew deploying transplanted turf blocks, RMBL, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_4699.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Alpine meadow transplant site, East River watershed, Colorado">
    <img src="{{ '/assets/img/transplant/img_4699.jpeg' | relative_url }}"
         alt="Alpine meadow transplant site, East River watershed, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_4991.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Monitoring transplanted meadow communities — RMBL Climate Change Experiment, Colorado">
    <img src="{{ '/assets/img/transplant/img_4991.jpeg' | relative_url }}"
         alt="Monitoring transplanted meadow communities, RMBL, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_5105.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Field measurements in transplant plots, Washington Gulch, Colorado">
    <img src="{{ '/assets/img/transplant/img_5105.jpeg' | relative_url }}"
         alt="Field measurements in transplant plots, Washington Gulch, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_5130.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Transplanted turf block in alpine meadow — RMBL Climate Change Experiment, Colorado">
    <img src="{{ '/assets/img/transplant/img_5130.jpeg' | relative_url }}"
         alt="Transplanted turf block in alpine meadow, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/6b088f65-b6cd-4af7-b24b-a67796c4a2b7_1_105_c.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Transplant plot measurement — RMBL Climate Change Experiment, Washington Gulch, Colorado">
    <img src="{{ '/assets/img/transplant/6b088f65-b6cd-4af7-b24b-a67796c4a2b7_1_105_c.jpeg' | relative_url }}"
         alt="Transplant plot measurement, Washington Gulch, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/951d70f5-aaf8-474c-b1bf-a7bc9e55bd85_1_105_c.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Plant community monitoring, Washington Gulch — RMBL Climate Change Experiment, Colorado">
    <img src="{{ '/assets/img/transplant/951d70f5-aaf8-474c-b1bf-a7bc9e55bd85_1_105_c.jpeg' | relative_url }}"
         alt="Plant community monitoring, Washington Gulch, Colorado" loading="lazy">
  </a>

</div>
</div><!-- /.gallery-theme-block -->

<!-- ── Global Experiment Network ──────────────────────────────────────────── -->
<div class="gallery-theme-block">
<div class="gallery-theme-header"><h2>Global Experiment Network</h2></div>

<div class="photo-gallery" data-theme="climate-experiments">

  <a href="{{ '/assets/img/wordpress-legacy/originals/otc-pb_svalbard__4870bb69.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Open-top chamber warming experiment, Svalbard, Norway"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/otc-pb_svalbard__4870bb69.jpg' | relative_url }}"
         alt="Open-top chamber warming experiment, Svalbard, Norway" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/otc_china__c886e5c8.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Open-top chamber warming experiment, China">
    <img src="{{ '/assets/img/wordpress-legacy/originals/otc_china__c886e5c8.jpg' | relative_url }}"
         alt="Open-top chamber warming experiment, China" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/harvard-1.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Harvard Forest, Petersham, Massachusetts — long-term forest dynamics site">
    <img src="{{ '/assets/img/wordpress/harvard-1.png' | relative_url }}"
         alt="Harvard Forest, Massachusetts" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/harvard-2.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Harvard Forest, Petersham, Massachusetts — long-term forest dynamics site">
    <img src="{{ '/assets/img/wordpress/harvard-2.png' | relative_url }}"
         alt="Harvard Forest, Massachusetts" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/tower-2.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field measurement tower, long-term monitoring site">
    <img src="{{ '/assets/img/wordpress/tower-2.png' | relative_url }}"
         alt="Field measurement tower" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/poles-2.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Vegetation monitoring poles, global experiment network site">
    <img src="{{ '/assets/img/wordpress/poles-2.png' | relative_url }}"
         alt="Vegetation monitoring poles, global experiment network" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/poles-6.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Vegetation monitoring poles, global experiment network site">
    <img src="{{ '/assets/img/wordpress/poles-6.png' | relative_url }}"
         alt="Vegetation monitoring poles, global experiment network" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/poles-7.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Vegetation monitoring poles, global experiment network site">
    <img src="{{ '/assets/img/wordpress/poles-7.png' | relative_url }}"
         alt="Vegetation monitoring poles, global experiment network" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/thu-1.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Experimental field plots, global trait and climate network site">
    <img src="{{ '/assets/img/wordpress/thu-1.png' | relative_url }}"
         alt="Experimental field plots, global network site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/thu-5.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Experimental field plots, global trait and climate network site">
    <img src="{{ '/assets/img/wordpress/thu-5.png' | relative_url }}"
         alt="Experimental field plots, global network site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/outdoor-3-1.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field vegetation measurements, global experiment network">
    <img src="{{ '/assets/img/wordpress/outdoor-3-1.png' | relative_url }}"
         alt="Field vegetation measurements, global experiment network" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/big-21.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field experiment site, global monitoring network">
    <img src="{{ '/assets/img/wordpress/big-21.png' | relative_url }}"
         alt="Field experiment site, global monitoring network" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0648.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field data collection, plant trait measurement campaign">
    <img src="{{ '/assets/img/wordpress/img_0648.jpg' | relative_url }}"
         alt="Field data collection, plant trait measurement" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0631.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field data collection, plant trait measurement campaign">
    <img src="{{ '/assets/img/wordpress/img_0631.jpg' | relative_url }}"
         alt="Field data collection, plant trait measurement" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0630.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field data collection, plant trait measurement campaign">
    <img src="{{ '/assets/img/wordpress/img_0630.jpg' | relative_url }}"
         alt="Field data collection, plant trait measurement" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0550.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field data collection, plant trait measurement campaign">
    <img src="{{ '/assets/img/wordpress/img_0550.jpg' | relative_url }}"
         alt="Field data collection, plant trait measurement" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0514.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field data collection, plant trait measurement campaign">
    <img src="{{ '/assets/img/wordpress/img_0514.jpg' | relative_url }}"
         alt="Field data collection, plant trait measurement" loading="lazy">
  </a>

</div>
</div><!-- /.gallery-theme-block -->

<!-- ── Arid & Dryland Ecosystems ──────────────────────────────────────────── -->
<div class="gallery-theme-block">
<div class="gallery-theme-header"><h2>Arid &amp; Dryland Ecosystems</h2></div>

<div class="photo-gallery" data-theme="arid-desert">

  <a href="{{ '/assets/img/wordpress-legacy/originals/organ-pipe-ben-31__bbd2f67c.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Organ Pipe Cactus National Monument, Sonoran Desert, Arizona"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/organ-pipe-ben-31__bbd2f67c.jpg' | relative_url }}"
         alt="Organ Pipe Cactus National Monument, Sonoran Desert, Arizona" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3371__62850edd.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Field research in dryland ecosystem">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3371__62850edd.jpg' | relative_url }}"
         alt="Field research in dryland ecosystem" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3446__33eff04b.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Field research in dryland ecosystem">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3446__33eff04b.jpg' | relative_url }}"
         alt="Field research in dryland ecosystem" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3441__764eb526.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Field research in dryland ecosystem">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3441__764eb526.jpg' | relative_url }}"
         alt="Field research in dryland ecosystem" loading="lazy">
  </a>

</div>
</div><!-- /.gallery-theme-block -->

<!-- ── Islands & Special Floras ──────────────────────────────────────────── -->
<div class="gallery-theme-block">
<div class="gallery-theme-header"><h2>Islands &amp; Special Floras</h2></div>

<div class="photo-gallery" data-theme="islands">

  <a href="{{ '/assets/img/wordpress/c-clahe060611-67_dubautia-latifolia.jpg' | relative_url }}"
     data-lightbox="islands"
     data-title="Dubautia latifolia (silversword alliance), high-elevation volcanic slopes, Haleakalā, Maui, Hawaiʻi"
     class="wide">
    <img src="{{ '/assets/img/wordpress/c-clahe060611-67_dubautia-latifolia.jpg' | relative_url }}"
         alt="Dubautia latifolia on high-elevation volcanic slopes, Haleakalā, Maui, Hawaiʻi" loading="lazy">
  </a>

</div>
</div><!-- /.gallery-theme-block -->

</div><!-- /#gallery-themes-container -->

---

<!-- ── Science in Action ────────────────────────────────────── -->

<div class="gallery-theme-header"><h2>Science in Action</h2></div>

<div class="photo-gallery" data-theme="people">

  <a href="{{ '/assets/img/team/lab_group_costa_rica.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Lab team at the San Emilio Forest Dynamics Plot, Área de Conservación Guanacaste, Costa Rica"
     class="wide">
    <img src="{{ '/assets/img/team/lab_group_costa_rica.jpeg' | relative_url }}"
         alt="Enquist Lab group at San Emilio FDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/planttraitcourse_2015__4c1c62f8.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Plant Functional Trait Course 2015, Andes, Peru"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/planttraitcourse_2015__4c1c62f8.jpg' | relative_url }}"
         alt="Plant Functional Trait Course 2015, Andes, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/team/pftc_group.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Plant Functional Trait Course (PFTC) group photo, Andes, Peru">
    <img src="{{ '/assets/img/team/pftc_group.jpeg' | relative_url }}"
         alt="PFTC group photo, Andes, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/pftc5_peru.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="PFTC5 participants in the field, Andes, Peru">
    <img src="{{ '/assets/img/field/pftc5_peru.jpeg' | relative_url }}"
         alt="PFTC5 fieldwork, Andes, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/pftc_peru_students.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Plant Functional Trait Course students collecting leaf trait data, Andes, Peru"
     class="wide">
    <img src="{{ '/assets/img/field/pftc_peru_students.jpeg' | relative_url }}"
         alt="PFTC students collecting leaf trait data, Andes, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/sefdp_resurvey_team.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="SEFDP 2019–2021 resurvey team, San Emilio FDP, Costa Rica">
    <img src="{{ '/assets/img/field/sefdp_resurvey_team.jpeg' | relative_url }}"
         alt="SEFDP resurvey team, San Emilio FDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/sefdp_diameter_measure.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Measuring tree diameter during the SEFDP census, San Emilio FDP, Costa Rica">
    <img src="{{ '/assets/img/field/sefdp_diameter_measure.jpg' | relative_url }}"
         alt="Tree diameter measurement, SEFDP census, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-020.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Brian J. Enquist, February 2020">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-020.jpg' | relative_url }}"
         alt="Brian J. Enquist, February 2020" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-088.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Brian J. Enquist, February 2020">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-088.jpg' | relative_url }}"
         alt="Brian J. Enquist, February 2020" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-047-1.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Brian J. Enquist, February 2020">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-047-1.jpg' | relative_url }}"
         alt="Brian J. Enquist, February 2020" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-031.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Brian J. Enquist, February 2020">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-031.jpg' | relative_url }}"
         alt="Brian J. Enquist, February 2020" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-003.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Brian J. Enquist, February 2020">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-003.jpg' | relative_url }}"
         alt="Brian J. Enquist, February 2020" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_5090.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Field data collection, Enquist Lab">
    <img src="{{ '/assets/img/wordpress/img_5090.jpeg' | relative_url }}"
         alt="Field data collection, Enquist Lab" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_5586.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Field data collection, Enquist Lab">
    <img src="{{ '/assets/img/wordpress/img_5586.jpeg' | relative_url }}"
         alt="Field data collection, Enquist Lab" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3219.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Field work, Enquist Lab">
    <img src="{{ '/assets/img/wordpress/dsc_3219.jpeg' | relative_url }}"
         alt="Field work, Enquist Lab" loading="lazy">
  </a>

</div>

<script>
(function () {
  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
    return arr;
  }
  function shuffleAll() {
    // Shuffle photos within each grid only — section order is preserved intentionally
    document.querySelectorAll('.photo-gallery').forEach(function (grid) {
      var items = Array.from(grid.children);
      shuffle(items);
      // Keep first child (wide hero) in place; shuffle the rest
      var hero = items.shift();
      shuffle(items);
      items.unshift(hero);
      items.forEach(function (el) { grid.appendChild(el); });
    });
  }
  shuffleAll();
  document.getElementById('gallery-shuffle-btn').addEventListener('click', shuffleAll);
})();
</script>
