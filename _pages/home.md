---
layout: page
title: home
permalink: /
nav: false
nav_order: 1
---

<div class="hero-photo hero-home">
  {% include home-image.liquid name='field_opening' widths='640,960,1440,1920,2560' sizes='100vw' width=3031 height=1644 alt='Snow-covered mountain peaks above vegetated slopes under cloudy skies' loading='eager' %}
  <div class="hero-home__overlay">
    <h1 class="hero-home__title">Macroecology Lab</h1>
    <p class="hero-home__sub">University of Arizona &amp; Santa Fe Institute</p>
  </div>
</div>

<div class="home-mission">
  <p>We study how biodiversity, traits, and ecosystem function scale from individual organisms to whole ecosystems — and how those patterns shift under climate change and land-use pressure.</p>
</div>

<div class="home-recruitment-status">
  <a class="status-chip status-chip--info" href="{{ '/join/' | relative_url }}">Graduate inquiries welcome &rarr; Learn about joining the lab</a>
  <a href="{{ '/resources/' | relative_url }}">Tools &amp; Data</a>
</div>

<div class="home-cards">

  <a class="home-card" href="{{ '/about/' | relative_url }}">
    <div class="home-card__img">{% include home-image.liquid name='brian_field' widths='320,640,800' width=800 height=531 alt='Brian Enquist conducting field measurements in a forest' %}</div>
    <div class="home-card__body">
      <h3>About</h3>
      <p>Lab mission, research pillars, and approach.</p>
    </div>
  </a>

  <a class="home-card" href="{{ '/research/' | relative_url }}">
    <div class="home-card__img">{% include home-image.liquid name='aberg_andes' width=3696 height=2448 alt='Andes mountain landscape during ecological field sampling' %}</div>
    <div class="home-card__body">
      <h3>Research</h3>
      <p>Scaling, trait-based ecology, global change.</p>
    </div>
  </a>

  <a class="home-card" href="{{ '/people/' | relative_url }}">
    <div class="home-card__img">{% include home-image.liquid name='pftc_peru_students' width=3696 height=2448 alt='PFTC students and researchers during field training in Peru' %}</div>
    <div class="home-card__body">
      <h3>People</h3>
      <p>Graduate students, postdocs, and collaborators.</p>
    </div>
  </a>

  <a class="home-card" href="{{ '/field-sites/' | relative_url }}">
    <div class="home-card__img">{% include home-image.liquid name='rmbl_alpine' width=1356 height=2048 alt='Alpine meadow at Rocky Mountain Biological Laboratory field site' %}</div>
    <div class="home-card__body">
      <h3>Field Sites</h3>
      <p>Long-term plots in Costa Rica, Colorado, Peru, and beyond.</p>
    </div>
  </a>

  <a class="home-card" href="{{ '/publications/' | relative_url }}">
    <div class="home-card__img">{% include home-image.liquid name='sefdp_lidar' width=1953 height=1725 alt='LiDAR survey of San Emilio Forest Dynamics Plot canopy structure' %}</div>
    <div class="home-card__body">
      <h3>Publications</h3>
      <p>Papers, books, and open datasets.</p>
    </div>
  </a>

  <a class="home-card" href="{{ '/join/' | relative_url }}">
    <div class="home-card__img">{% include home-image.liquid name='dsc_3414' width=3696 height=2448 alt='Researchers measuring trees along an Andean elevational transect' %}</div>
    <div class="home-card__body">
      <h3>Join or Collaborate</h3>
      <p>Graduate students, postdocs, visitors, and partners.</p>
    </div>
  </a>

</div>
