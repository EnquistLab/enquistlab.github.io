---
layout: page
title: gallery
permalink: /gallery/
description: Field landscapes, research sites, and lab life
nav: true
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

/* ── Section heading (People only) ─────────────────────────── */
.gallery-section-title {
  font-size: 1.2rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin: 2rem 0 0.75rem;
  color: var(--global-text-color);
  border-bottom: 2px solid var(--global-divider-color, #e0e0e0);
  padding-bottom: 0.4rem;
}
</style>

Photos from field campaigns, long-term research sites, and lab gatherings across the Americas and beyond.
Click any image to open the full view.

<div class="photo-gallery">

  <a href="{{ '/assets/img/field/field_opening.jpeg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Dry tropical forest, San Emilio FDP, Area de Conservación Guanacaste, Costa Rica"
     class="wide">
    <img src="{{ '/assets/img/field/field_opening.jpeg' | relative_url }}"
         alt="Dry tropical forest opening, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/aberg_andes.jpeg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Andes elevation transect, Peru">
    <img src="{{ '/assets/img/field/aberg_andes.jpeg' | relative_url }}"
         alt="Andes elevation transect, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/rmbl_alpine.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Alpine meadow above the Rocky Mountain Biological Laboratory, Gothic, Colorado"
     class="wide">
    <img src="{{ '/assets/img/field/rmbl_alpine.jpg' | relative_url }}"
         alt="Alpine meadow, RMBL, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/avery-ridge.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Avery Ridge landscape">
    <img src="{{ '/assets/img/wordpress/avery-ridge.jpg' | relative_url }}"
         alt="Avery Ridge landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/sefdp_lidar.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="LiDAR survey, San Emilio Forest Dynamics Plot, Costa Rica">
    <img src="{{ '/assets/img/field/sefdp_lidar.jpg' | relative_url }}"
         alt="LiDAR survey at SEFDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/polylepis__c3788d1a.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Polylepis high-Andean woodland, Peru">
    <img src="{{ '/assets/img/wordpress-legacy/originals/polylepis__c3788d1a.jpg' | relative_url }}"
         alt="Polylepis woodland, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/rockies_transect__uib_d1f52468.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Rocky Mountains elevation transect, Colorado"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/rockies_transect__uib_d1f52468.jpg' | relative_url }}"
         alt="Rocky Mountains transect, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/otc-pb_svalbard__4870bb69.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Open-top chamber warming experiment, Svalbard, Norway">
    <img src="{{ '/assets/img/wordpress-legacy/originals/otc-pb_svalbard__4870bb69.jpg' | relative_url }}"
         alt="OTC warming experiment, Svalbard" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/organ-pipe-ben-31__bbd2f67c.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Organ Pipe Cactus National Monument, Arizona">
    <img src="{{ '/assets/img/wordpress-legacy/originals/organ-pipe-ben-31__bbd2f67c.jpg' | relative_url }}"
         alt="Organ Pipe Cactus NM, Arizona" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/dsc_4115-2__0f2dcb5e.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="High-elevation Andes landscape, Peru"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/dsc_4115-2__0f2dcb5e.jpg' | relative_url }}"
         alt="Andes landscape, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/dsc_9737-2__36ae8a5c.jpeg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Andean alpine zone and sky, Peru">
    <img src="{{ '/assets/img/wordpress-legacy/originals/dsc_9737-2__36ae8a5c.jpeg' | relative_url }}"
         alt="Andean alpine zone, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_5672.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_5672.jpg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_2963.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_2963.jpg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3225.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3225.jpg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0597.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_0597.jpg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/otc_china__02ab175d.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Open-top chamber warming experiment, China">
    <img src="{{ '/assets/img/wordpress-legacy/originals/otc_china__02ab175d.jpg' | relative_url }}"
         alt="OTC warming experiment, China" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3186__1bb50ea6.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Field research">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3186__1bb50ea6.jpg' | relative_url }}"
         alt="Field research" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3371__3a002e6b.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Field research">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3371__3a002e6b.jpg' | relative_url }}"
         alt="Field research" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3441__3b5d6b5f.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Field research">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3441__3b5d6b5f.jpg' | relative_url }}"
         alt="Field research" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3446__04f3f8e6.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Field research">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3446__04f3f8e6.jpg' | relative_url }}"
         alt="Field research" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/pfeiler_forest_1__ee3592b1.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Tall forest with emergent canopy trees">
    <img src="{{ '/assets/img/wordpress-legacy/originals/pfeiler_forest_1__ee3592b1.jpg' | relative_url }}"
         alt="Tall forest, emergent canopy trees" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/pfeiler_forest3__1fdfdc64.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Forest understorey and canopy">
    <img src="{{ '/assets/img/wordpress-legacy/originals/pfeiler_forest3__1fdfdc64.jpg' | relative_url }}"
         alt="Forest understorey and canopy" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/sefdp_forest_canopy.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Tropical forest canopy, San Emilio Forest Dynamics Plot, Costa Rica"
     class="wide">
    <img src="{{ '/assets/img/field/sefdp_forest_canopy.jpg' | relative_url }}"
         alt="Tropical forest canopy, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3202__fa8fe550.jpg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Forest landscape, Rocky Mountain Biological Laboratory, Colorado">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3202__fa8fe550.jpg' | relative_url }}"
         alt="Forest landscape, RMBL, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3236.jpeg' | relative_url }}"
     data-lightbox="gallery"
     data-title="Tree canopy, tropical forest">
    <img src="{{ '/assets/img/wordpress/dsc_3236.jpeg' | relative_url }}"
         alt="Tree canopy, tropical forest" loading="lazy">
  </a>

</div>

---

<div class="gallery-section-title">People &amp; Field Work</div>

<div class="photo-gallery">

  <a href="{{ '/assets/img/team/lab_group_costa_rica.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Lab team at the San Emilio Forest Dynamics Plot, Area de Conservación Guanacaste, Costa Rica"
     class="wide">
    <img src="{{ '/assets/img/team/lab_group_costa_rica.jpeg' | relative_url }}"
         alt="Lab group, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/team/pftc_group.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Plant Functional Trait Course (PFTC) group, Peru">
    <img src="{{ '/assets/img/team/pftc_group.jpeg' | relative_url }}"
         alt="PFTC group photo, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/pftc5_peru.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="PFTC5 participants in the field, Peru">
    <img src="{{ '/assets/img/field/pftc5_peru.jpeg' | relative_url }}"
         alt="PFTC5 fieldwork, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/pftc_peru_students.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Plant Functional Trait Course students collecting data, Peru"
     class="wide">
    <img src="{{ '/assets/img/field/pftc_peru_students.jpeg' | relative_url }}"
         alt="PFTC students, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/sefdp_resurvey_team.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="SEFDP 2019–2021 resurvey team, San Emilio FDP, Costa Rica">
    <img src="{{ '/assets/img/field/sefdp_resurvey_team.jpeg' | relative_url }}"
         alt="SEFDP resurvey team, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/sefdp_diameter_measure.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Measuring tree diameter during the SEFDP census, Costa Rica">
    <img src="{{ '/assets/img/field/sefdp_diameter_measure.jpg' | relative_url }}"
         alt="Tree diameter measurement, SEFDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/rmbl_fieldwork.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Field sampling at the Rocky Mountain Biological Laboratory, Colorado">
    <img src="{{ '/assets/img/field/rmbl_fieldwork.jpg' | relative_url }}"
         alt="RMBL fieldwork, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-020.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Brian Enquist, February 2020">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-020.jpg' | relative_url }}"
         alt="Brian J. Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-088.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Brian Enquist, February 2020">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-088.jpg' | relative_url }}"
         alt="Brian J. Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_5090.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_5090.jpeg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_5586.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_5586.jpeg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/planttraitcourse_2015__4c1c62f8.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="Plant Functional Trait Course 2015, Peru"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/planttraitcourse_2015__4c1c62f8.jpg' | relative_url }}"
         alt="Plant Trait Course 2015" loading="lazy">
  </a>

</div>
