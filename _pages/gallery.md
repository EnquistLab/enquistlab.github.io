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

<!-- ── Tropical Forests ──────────────────────────────────────────── -->

<div class="gallery-theme-header"><h2>Tropical Forests</h2></div>

<div class="photo-gallery" data-theme="tropical-forests">

  <a href="{{ '/assets/img/field/field_opening.jpeg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Dry tropical forest, San Emilio FDP, Area de Conservación Guanacaste, Costa Rica"
     class="wide">
    <img src="{{ '/assets/img/field/field_opening.jpeg' | relative_url }}"
         alt="Dry tropical forest opening, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/sefdp_lidar.jpg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="LiDAR survey, San Emilio Forest Dynamics Plot, Costa Rica">
    <img src="{{ '/assets/img/field/sefdp_lidar.jpg' | relative_url }}"
         alt="LiDAR survey at SEFDP, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/sefdp_forest_canopy.jpg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Tropical forest canopy, San Emilio Forest Dynamics Plot, Costa Rica"
     class="wide">
    <img src="{{ '/assets/img/field/sefdp_forest_canopy.jpg' | relative_url }}"
         alt="Tropical forest canopy, Costa Rica" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3236.jpeg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Tree canopy, tropical forest">
    <img src="{{ '/assets/img/wordpress/dsc_3236.jpeg' | relative_url }}"
         alt="Tree canopy, tropical forest" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/ceibo.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Ceibo tree, dry tropical forest">
    <img src="{{ '/assets/img/wordpress/ceibo.png' | relative_url }}"
         alt="Ceibo tree, dry tropical forest" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cr-1-2.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Costa Rica field site">
    <img src="{{ '/assets/img/wordpress/cr-1-2.png' | relative_url }}"
         alt="Costa Rica field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cr-2-1.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Costa Rica field site">
    <img src="{{ '/assets/img/wordpress/cr-2-1.png' | relative_url }}"
         alt="Costa Rica field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cr-3-2.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Costa Rica field site">
    <img src="{{ '/assets/img/wordpress/cr-3-2.png' | relative_url }}"
         alt="Costa Rica field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cr-4-1.png' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Costa Rica field site">
    <img src="{{ '/assets/img/wordpress/cr-4-1.png' | relative_url }}"
         alt="Costa Rica field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/pfeiler_forest_1__72d0b3ba.jpg' | relative_url }}"
     data-lightbox="tropical-forests"
     data-title="Tall forest with emergent canopy trees">
    <img src="{{ '/assets/img/wordpress-legacy/originals/pfeiler_forest_1__72d0b3ba.jpg' | relative_url }}"
         alt="Tall forest, emergent canopy trees" loading="lazy">
  </a>

</div>

<!-- ── Andean Elevations ──────────────────────────────────────────── -->

<div class="gallery-theme-header"><h2>Andean Elevations</h2></div>

<div class="photo-gallery" data-theme="andean-elevations">

  <a href="{{ '/assets/img/field/aberg_andes.jpeg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Andes elevation transect, Peru">
    <img src="{{ '/assets/img/field/aberg_andes.jpeg' | relative_url }}"
         alt="Andes elevation transect, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3414.jpeg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="High-Andes landscape along the PFTC transect, Peru">
    <img src="{{ '/assets/img/wordpress/dsc_3414.jpeg' | relative_url }}"
         alt="High-Andes landscape, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/polylepis__c3788d1a.jpg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Polylepis high-Andean woodland, Peru">
    <img src="{{ '/assets/img/wordpress-legacy/originals/polylepis__c3788d1a.jpg' | relative_url }}"
         alt="Polylepis woodland, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/dsc_3876__461b0b78.jpg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Mountain valley and cloud forest, Peru">
    <img src="{{ '/assets/img/wordpress-legacy/originals/dsc_3876__461b0b78.jpg' | relative_url }}"
         alt="Mountain valley, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/dsc_4115-2__8cde5bc1.jpg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="High-elevation Andes landscape, Peru"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/dsc_4115-2__8cde5bc1.jpg' | relative_url }}"
         alt="Andes landscape, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/dsc_9737-2__a3db9ce9.jpeg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Andean alpine zone and sky, Peru">
    <img src="{{ '/assets/img/wordpress-legacy/originals/dsc_9737-2__a3db9ce9.jpeg' | relative_url }}"
         alt="Andean alpine zone, Peru" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-dsc_9737-2.jpeg' | relative_url }}"
     data-lightbox="andean-elevations"
     data-title="Andean alpine zone, Peru">
    <img src="{{ '/assets/img/wordpress/cropped-dsc_9737-2.jpeg' | relative_url }}"
         alt="Andean alpine zone, Peru" loading="lazy">
  </a>

</div>

<!-- ── Rocky Mountains &amp; Alpine ──────────────────────────────────────────── -->

<div class="gallery-theme-header"><h2>Rocky Mountains &amp; Alpine</h2></div>

<div class="photo-gallery" data-theme="rocky-mountains">

  <a href="{{ '/assets/img/field/rmbl_alpine.jpg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Alpine meadow above the Rocky Mountain Biological Laboratory, Gothic, Colorado"
     class="wide">
    <img src="{{ '/assets/img/field/rmbl_alpine.jpg' | relative_url }}"
         alt="Alpine meadow, RMBL, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/avery-ridge.jpg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Avery Ridge landscape">
    <img src="{{ '/assets/img/wordpress/avery-ridge.jpg' | relative_url }}"
         alt="Avery Ridge landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/rockies_transect__uib_d1f52468.jpg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Rocky Mountains elevation transect, Colorado"
     class="wide">
    <img src="{{ '/assets/img/wordpress-legacy/originals/rockies_transect__uib_d1f52468.jpg' | relative_url }}"
         alt="Rocky Mountains transect, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3202__db000470.jpg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Forest landscape, Rocky Mountain Biological Laboratory, Colorado">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3202__db000470.jpg' | relative_url }}"
         alt="Forest landscape, RMBL, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_5119.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Transplant plots in Washington Gulch, Crested Butte — RMBL Climate Change Experiment"
     class="wide">
    <img src="{{ '/assets/img/transplant/img_5119.jpeg' | relative_url }}"
         alt="Transplant plots in Washington Gulch, Crested Butte" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_4628.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Field crew deploying transplanted turf blocks — RMBL Climate Change Experiment">
    <img src="{{ '/assets/img/transplant/img_4628.jpeg' | relative_url }}"
         alt="Field crew, RMBL transplant experiment" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_4699.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Alpine meadow transplant site, East River watershed, Colorado">
    <img src="{{ '/assets/img/transplant/img_4699.jpeg' | relative_url }}"
         alt="Alpine meadow transplant site, Colorado" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_4991.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Monitoring transplanted meadow communities — RMBL Climate Change Experiment">
    <img src="{{ '/assets/img/transplant/img_4991.jpeg' | relative_url }}"
         alt="Monitoring transplanted meadow communities, RMBL" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_5105.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Field measurements in transplant plots, Washington Gulch">
    <img src="{{ '/assets/img/transplant/img_5105.jpeg' | relative_url }}"
         alt="Field measurements in transplant plots, Washington Gulch" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/img_5130.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Transplanted turf block in alpine meadow — RMBL Climate Change Experiment">
    <img src="{{ '/assets/img/transplant/img_5130.jpeg' | relative_url }}"
         alt="Transplanted turf block in alpine meadow" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/6b088f65-b6cd-4af7-b24b-a67796c4a2b7_1_105_c.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Transplant plot measurement — RMBL Climate Change Experiment">
    <img src="{{ '/assets/img/transplant/6b088f65-b6cd-4af7-b24b-a67796c4a2b7_1_105_c.jpeg' | relative_url }}"
         alt="Transplant plot measurement, RMBL" loading="lazy">
  </a>

  <a href="{{ '/assets/img/transplant/951d70f5-aaf8-474c-b1bf-a7bc9e55bd85_1_105_c.jpeg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Plant community monitoring, Washington Gulch — RMBL Climate Change Experiment">
    <img src="{{ '/assets/img/transplant/951d70f5-aaf8-474c-b1bf-a7bc9e55bd85_1_105_c.jpeg' | relative_url }}"
         alt="Plant community monitoring, Washington Gulch" loading="lazy">
  </a>

  <a href="{{ '/assets/img/field/rmbl_fieldwork.jpg' | relative_url }}"
     data-lightbox="rocky-mountains"
     data-title="Field sampling at the Rocky Mountain Biological Laboratory, Colorado">
    <img src="{{ '/assets/img/field/rmbl_fieldwork.jpg' | relative_url }}"
         alt="RMBL fieldwork, Colorado" loading="lazy">
  </a>

</div>

<!-- ── Climate Experiments ──────────────────────────────────────────── -->

<div class="gallery-theme-header"><h2>Climate Experiments</h2></div>

<div class="photo-gallery" data-theme="climate-experiments">

  <a href="{{ '/assets/img/wordpress-legacy/originals/otc-pb_svalbard__4870bb69.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Open-top chamber warming experiment, Svalbard, Norway">
    <img src="{{ '/assets/img/wordpress-legacy/originals/otc-pb_svalbard__4870bb69.jpg' | relative_url }}"
         alt="OTC warming experiment, Svalbard" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/otc_china__c886e5c8.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Open-top chamber warming experiment, China">
    <img src="{{ '/assets/img/wordpress-legacy/originals/otc_china__c886e5c8.jpg' | relative_url }}"
         alt="OTC warming experiment, China" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/tower-2.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field measurement tower">
    <img src="{{ '/assets/img/wordpress/tower-2.png' | relative_url }}"
         alt="Field tower" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/poles-2.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field measurement poles">
    <img src="{{ '/assets/img/wordpress/poles-2.png' | relative_url }}"
         alt="Field measurement poles" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/poles-6.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field measurement poles">
    <img src="{{ '/assets/img/wordpress/poles-6.png' | relative_url }}"
         alt="Field measurement poles" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/poles-7.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field measurement poles">
    <img src="{{ '/assets/img/wordpress/poles-7.png' | relative_url }}"
         alt="Field measurement poles" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/thu-1.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field experiment site">
    <img src="{{ '/assets/img/wordpress/thu-1.png' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/thu-5.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field experiment site">
    <img src="{{ '/assets/img/wordpress/thu-5.png' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/harvard-1.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Harvard Forest field site">
    <img src="{{ '/assets/img/wordpress/harvard-1.png' | relative_url }}"
         alt="Harvard Forest field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/harvard-2.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Harvard Forest field site">
    <img src="{{ '/assets/img/wordpress/harvard-2.png' | relative_url }}"
         alt="Harvard Forest field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_5352.jpeg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_5352.jpeg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0648.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_0648.jpg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0631.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_0631.jpg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0630.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_0630.jpg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0550.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_0550.jpg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0514.jpg' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_0514.jpg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/outdoor-3-1.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Outdoor field work">
    <img src="{{ '/assets/img/wordpress/outdoor-3-1.png' | relative_url }}"
         alt="Outdoor field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/big-21.png' | relative_url }}"
     data-lightbox="climate-experiments"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/big-21.png' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

</div>

<!-- ── Arid &amp; Desert Landscapes ──────────────────────────────────────────── -->

<div class="gallery-theme-header"><h2>Arid &amp; Desert Landscapes</h2></div>

<div class="photo-gallery" data-theme="arid-desert">

  <a href="{{ '/assets/img/wordpress-legacy/originals/organ-pipe-ben-31__bbd2f67c.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Organ Pipe Cactus National Monument, Arizona">
    <img src="{{ '/assets/img/wordpress-legacy/originals/organ-pipe-ben-31__bbd2f67c.jpg' | relative_url }}"
         alt="Organ Pipe Cactus NM, Arizona" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/c-clahe060611-67_dubautia-latifolia.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Dubautia latifolia, Hawaii">
    <img src="{{ '/assets/img/wordpress/c-clahe060611-67_dubautia-latifolia.jpg' | relative_url }}"
         alt="Dubautia latifolia" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3186__3aface6a.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Field research, arid landscape">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3186__3aface6a.jpg' | relative_url }}"
         alt="Field research" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3371__62850edd.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Field research">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3371__62850edd.jpg' | relative_url }}"
         alt="Field research" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3446__33eff04b.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Field research">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3446__33eff04b.jpg' | relative_url }}"
         alt="Field research" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress-legacy/originals/img_3441__764eb526.jpg' | relative_url }}"
     data-lightbox="arid-desert"
     data-title="Field research">
    <img src="{{ '/assets/img/wordpress-legacy/originals/img_3441__764eb526.jpg' | relative_url }}"
         alt="Field research" loading="lazy">
  </a>

</div>

<!-- ── Field Landscapes ──────────────────────────────────────────── -->

<div class="gallery-theme-header"><h2>Field Landscapes</h2></div>

<div class="photo-gallery" data-theme="landscapes">

  <a href="{{ '/assets/img/wordpress/cropped-1973302_927546123924359_1777004156092313692_o-1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-1973302_927546123924359_1777004156092313692_o-1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-8741662722_d00d53a512_o-2.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-8741662722_d00d53a512_o-2.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-8741662722_d00d53a512_o-1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-8741662722_d00d53a512_o-1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-398967_402706289741681_100000069398128_1594096_736206182_n-1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-398967_402706289741681_100000069398128_1594096_736206182_n-1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-14297765828_509ede7066_o-1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-14297765828_509ede7066_o-1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-550106_3567860316612_913822306_n-1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-550106_3567860316612_913822306_n-1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-img_0546_2-1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-img_0546_2-1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-cropped-1973302_927546123924359_1777004156092313692_o2.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-cropped-1973302_927546123924359_1777004156092313692_o2.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-image1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-image1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-8735545283_443199c858_o1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-8735545283_443199c858_o1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-untitled51.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-untitled51.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-14297898047_2bb15514b1_o2.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-14297898047_2bb15514b1_o2.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-8742092306_30b07cac7e_o1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field landscape">
    <img src="{{ '/assets/img/wordpress/cropped-8742092306_30b07cac7e_o1.jpg' | relative_url }}"
         alt="Field landscape" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/trees.png' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Trees">
    <img src="{{ '/assets/img/wordpress/trees.png' | relative_url }}"
         alt="Trees" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_2963.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_2963.jpg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3225.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3225.jpg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_6512-1.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/img_6512-1.jpg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/img_0597.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field work">
    <img src="{{ '/assets/img/wordpress/img_0597.jpg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_5672.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_5672.jpg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_2928.jpeg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_2928.jpeg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3211-1.jpeg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3211-1.jpeg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3224.jpg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3224.jpg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3255.jpeg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3255.jpeg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3286.jpeg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3286.jpeg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3294.jpeg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3294.jpeg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3337.jpeg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3337.jpeg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3355.jpeg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3355.jpeg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3426.jpeg' | relative_url }}"
     data-lightbox="landscapes"
     data-title="Field site">
    <img src="{{ '/assets/img/wordpress/dsc_3426.jpeg' | relative_url }}"
         alt="Field site" loading="lazy">
  </a>

</div>

---

<!-- ── People & Field Work ────────────────────────────────────── -->

<div class="gallery-section-title">People &amp; Field Work</div>

<div class="photo-gallery" data-theme="people">

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

  <a href="{{ '/assets/img/wordpress/amanda.png' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/amanda.png' | relative_url }}"
         alt="Lab member" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/working-1.png' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/working-1.png' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-047-1.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-047-1.jpg' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-031.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-031.jpg' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-003.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-003.jpg' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/pulling3-1.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/pulling3-1.jpg' | relative_url }}"
         alt="Field work" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian2.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/brian2.jpg' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/interview-2-1.png' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/interview-2-1.png' | relative_url }}"
         alt="Interview" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-untitled91.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/cropped-untitled91.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-img_13681.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/cropped-img_13681.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/untitled23.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/untitled23.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/8735578355_2727abf16d_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/8735578355_2727abf16d_o.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-8736672508_ce0859930d_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/cropped-8736672508_ce0859930d_o.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-16820461938_9d89b29d51_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/cropped-16820461938_9d89b29d51_o.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/16982234246_dbf43a38d9_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/16982234246_dbf43a38d9_o.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/16385832784_db147c9558_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/16385832784_db147c9558_o.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/image.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/image.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dscn5015.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/dscn5015.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/christine_14.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/christine_14.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-bien_2012.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/cropped-bien_2012.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/10553859_850734928272146_2591283871298109790_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/10553859_850734928272146_2591283871298109790_o.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/550106_3567860316612_913822306_n.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/550106_3567860316612_913822306_n.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-bigelow-5.png' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/cropped-bigelow-5.png' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/cropped-growth-season-11.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/cropped-growth-season-11.jpg' | relative_url }}"
         alt="People" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/screen-shot-2020-12-15-at-2.29.22-pm.png' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/screen-shot-2020-12-15-at-2.29.22-pm.png' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/screen-shot-2020-12-15-at-2.33.21-pm.png' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/screen-shot-2020-12-15-at-2.33.21-pm.png' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/screen-shot-2020-12-15-at-2.34.29-pm.png' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/screen-shot-2020-12-15-at-2.34.29-pm.png' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/14356996100_37b42655b3_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/14356996100_37b42655b3_o.jpg' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/14520555176_ac6abbf459_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/14520555176_ac6abbf459_o.jpg' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/14543636665_e684ee739b_o.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/14543636665_e684ee739b_o.jpg' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/brian-enquist-feb2020-060.jpg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-060.jpg' | relative_url }}"
         alt="Brian Enquist" loading="lazy">
  </a>

  <a href="{{ '/assets/img/wordpress/dsc_3219.jpeg' | relative_url }}"
     data-lightbox="people"
     data-title="">
    <img src="{{ '/assets/img/wordpress/dsc_3219.jpeg' | relative_url }}"
         alt="Field work" loading="lazy">
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
  function shuffleAllGrids() {
    document.querySelectorAll('.photo-gallery').forEach(function (grid) {
      var items = Array.from(grid.children);
      shuffle(items);
      items.forEach(function (el) { grid.appendChild(el); });
    });
  }
  shuffleAllGrids();
  document.getElementById('gallery-shuffle-btn').addEventListener('click', shuffleAllGrids);
})();
</script>
