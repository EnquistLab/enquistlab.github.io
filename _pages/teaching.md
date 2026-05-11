---
layout: page
title: teaching
permalink: /teaching/
description: Courses, workshops, video lectures, and open training materials in plant ecology, macroecology, and biodiversity science
nav: true
nav_order: 5
---

<div style="float:right;width:38%;max-width:360px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0;">
    <img src="{{ '/assets/img/wordpress/img_5586.jpeg' | relative_url }}" alt="Field-based training in plant functional ecology" style="width:100%;border-radius:4px;" loading="lazy">
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Field-based training in plant functional ecology — PFTC participants measure plant traits in alpine terrain.</figcaption>
  </figure>
</div>

Teaching in the Enquist Lab spans formal university courses, international field training programs, workshops, and open video lectures and slides. The unifying theme is using biodiversity science, macroecology, and quantitative methods to understand plant form, function, and diversity across scales.

<div class="cta-row">
  <a class="btn btn-sm btn-cta-primary" href="https://plantfunctionaltraitscourses.w.uib.no/" target="_blank" rel="noopener">PFTC Field Courses</a>
  <a class="btn btn-sm btn-cta-outline" href="https://ecol586.wordpress.com/" target="_blank" rel="noopener">ECOL 586 Blog</a>
  <a class="btn btn-sm btn-cta-outline" href="https://smduranm.github.io/EEB_R_workshops/" target="_blank" rel="noopener">EEB R Workshops</a>
</div>

---

### Current & Recent Courses {#courses}

| Course | Title |
|--------|-------|
| [ECOL 340](https://ecol340.wordpress.com/) | Evolution of Plant Form, Function, and Diversity |
| [ECOL 596x](https://smduranm.github.io/EEB_R_workshops/) | R Workshops for EEB PhD Students and Postdocs |
| [ECOL 586](https://ecol586.wordpress.com/) | Biological Scaling and Macroscopic Processes |
| ECOL 596W | New Methods in Trait-based Ecology and Evolution |
| ECOL 600 | Ecology and Evolution Core Class |

---

### Plant Functional Trait Courses (PFTC) {#pftc}

The [Plant Functional Trait Courses](https://plantfunctionaltraitscourses.w.uib.no/) provide hands-on training in plant functional traits ecology within a real-life field research project setting. Students plan and execute a trait-based research project, collect and document plant functional trait data in the field, and explore these data using trait-based approaches within climate change research and ecosystem ecology. Field campaigns have taken place in **Norway, Colorado (USA), Peru, China**, and additional countries.

---

### Workshops & Short Courses {#workshops}

- **Integrating and Cleaning Biodiversity Data** — workflows to model ranges and merge ecological, phylogenetic, and trait information. Taught at the 2017 International Biogeography Society meeting, Tucson, AZ. [Course overview](https://tucson2017ibs.wordpress.com/workshops/integrating-and-cleaning-biodiversity-data-workflows-to-model-ranges-and-merge-associated-ecological-phylogenetic-and-trait-information/)

<h2 class="teaching-section-heading" id="videos">Video Lectures</h2>

<div class="video-shuffle-bar">
  <button class="btn btn-shuffle" id="shuffleBtn" onclick="shuffleLecture()">&#x1F500; Shuffle Lecture</button>
</div>

<div class="featured-video-player" id="featuredPlayer" style="display:none;" aria-live="polite">
  <div class="video-embed-wrapper">
    <figure style="position:absolute;top:0;left:0;width:100%;height:100%;margin:0;">
      <iframe id="featuredIframe" src="" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="width:100%;height:100%;border-radius:6px;border:0;"></iframe>
    </figure>
  </div>
  <p class="video-caption" id="featuredCaption" style="text-align:center;font-size:0.95rem;margin-top:0.75rem;"></p>
</div>

<script>
(function () {
  var lectures = [
    { src: "https://www.youtube.com/embed/GEuvFfI3ZtY", title: "Our Rapidly Changing Biosphere", sub: "University of Arizona Public Science Lecture, 2020" },
    { src: "https://www.youtube.com/embed/u1NJTtWQSHQ", title: "The Concept of Time in Biology, and the Unity of Life", sub: "Oxford Martin School, 2017" },
    { src: "https://www.youtube.com/embed/q8EuFziyDwI", title: "NOVA: Hunting the Hidden Dimension", sub: "Fractal geometry and metabolic scaling — lab work starts ~43 min" },
    { src: "https://www.youtube.com/embed/HYdeYuk3Qa4", title: "National Geographic: X-Ray Earth", sub: "Metabolic scaling theory in action — lab work starts ~50 min" }
  ];
  var lastIdx = -1;

  window.shuffleLecture = function () {
    var idx;
    do { idx = Math.floor(Math.random() * lectures.length); } while (lectures.length > 1 && idx === lastIdx);
    lastIdx = idx;
    var lec = lectures[idx];
    var iframe = document.getElementById('featuredIframe');
    iframe.src = lec.src + '?autoplay=1';
    document.getElementById('featuredCaption').innerHTML = '<strong>' + lec.title + '</strong><br>' + lec.sub;
    var player = document.getElementById('featuredPlayer');
    player.style.display = 'block';
    setTimeout(function () { player.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 50);
  };
})();
</script>

<div class="video-lecture-grid">

  <div class="video-card">
    <div class="video-embed-wrapper">
      {% include video.liquid path="https://www.youtube.com/embed/GEuvFfI3ZtY" title="Our Rapidly Changing Biosphere — U of Arizona Public Science Lecture" %}
    </div>
    <p class="video-caption"><strong>Our Rapidly Changing Biosphere</strong><br>University of Arizona Public Science Lecture, 2020</p>
  </div>

  <div class="video-card">
    <div class="video-embed-wrapper">
      {% include video.liquid path="https://www.youtube.com/embed/u1NJTtWQSHQ" title="The Concept of Time in Biology, and the Unity of Life — Oxford Martin School 2017" %}
    </div>
    <p class="video-caption"><strong>The Concept of Time in Biology, and the Unity of Life</strong><br>Oxford Martin School, 2017</p>
  </div>

  <div class="video-card">
    <div class="video-embed-wrapper">
      {% include video.liquid path="https://www.youtube.com/embed/q8EuFziyDwI" title="NOVA: Hunting the Hidden Dimension — Fractal geometry and metabolic scaling" %}
    </div>
    <p class="video-caption"><strong>NOVA: Hunting the Hidden Dimension</strong><br>Fractal geometry and metabolic scaling — see the lab's work starting at ~43 min</p>
  </div>

  <div class="video-card">
    <div class="video-embed-wrapper">
      {% include video.liquid path="https://www.youtube.com/embed/HYdeYuk3Qa4" title="National Geographic X-Ray Earth — Metabolic scaling in action" %}
    </div>
    <p class="video-caption"><strong>National Geographic: X-Ray Earth</strong><br>Metabolic scaling theory in action — see the lab's work starting at ~50 min</p>
  </div>

</div>

<h2 class="teaching-section-heading" id="materials">Open Slides &amp; Materials</h2>

<ul class="materials-list">
  <li>
    <i class="fas fa-external-link-alt" aria-hidden="true"></i>
    <span><strong>#PlantBlindness: Why Plants Matter and Why We Study Traits</strong> — Enquist (2020). <a href="https://doi.org/10.6084/m9.figshare.12084966.v1" target="_blank" rel="noopener">Slides ↗</a></span>
  </li>
  <li>
    <i class="fas fa-external-link-alt" aria-hidden="true"></i>
    <span><strong>Introduction to Trait-Based Ecology</strong> (updated) — Enquist (2020). <a href="https://doi.org/10.6084/m9.figshare.11704383.v1" target="_blank" rel="noopener">Slides ↗</a></span>
  </li>
  <li>
    <i class="fas fa-external-link-alt" aria-hidden="true"></i>
    <span><strong>Muy BIEN: Next Steps in a Global Workflow for Integrating Plant Botanical Observations</strong> — Enquist et al. (2018). <a href="https://doi.org/10.6084/m9.figshare.6983024.v1" target="_blank" rel="noopener">Slides ↗</a></span>
  </li>
  <li>
    <i class="fas fa-external-link-alt" aria-hidden="true"></i>
    <span><strong>Trait Drivers Theory: Integrating and Scaling from Plant Form, Function &amp; Strategies to Ecosystems</strong> — Enquist &amp; Savage (2017). <a href="https://doi.org/10.6084/m9.figshare.5328004.v1" target="_blank" rel="noopener">Slides ↗</a></span>
  </li>
  <li>
    <i class="fas fa-external-link-alt" aria-hidden="true"></i>
    <span><strong>Introduction to Data Science &amp; Management: What They Don't (But Should) Teach You About the Scientific Method</strong> — Enquist (2016). <a href="https://figshare.com/articles/How_to_think_About_Your_Data_Introduction_to_Data_Science_Management_what_they_don_t_but_should_-_teach_you_about_the_scientific_method_/4251953" target="_blank" rel="noopener">Slides ↗</a></span>
  </li>
  <li>
    <i class="fas fa-external-link-alt" aria-hidden="true"></i>
    <span><strong>A Quick Introduction to Trait-Based Ecology</strong> — Enquist (2015). <a href="https://figshare.com/articles/A_quick_and_rough_introduction_to_trait_based_ecology/1396511" target="_blank" rel="noopener">Slides ↗</a></span>
  </li>
  <li>
    <i class="fas fa-external-link-alt" aria-hidden="true"></i>
    <span><strong>Overview Lecture on Macroecology</strong> — Enquist (2014). <a href="https://figshare.com/articles/Overview_lecture_on_Macroecology/1247653" target="_blank" rel="noopener">Slides ↗</a></span>
  </li>
  <li>
    <i class="fas fa-external-link-alt" aria-hidden="true"></i>
    <span><strong>Introduction to Metabolic Scaling Theory: From Cells to Ecosystems</strong> — Enquist (2014). <a href="https://figshare.com/articles/Introduction_to_Metabolic_Scaling_Theory_From_cells_to_ecosystems/1275197" target="_blank" rel="noopener">Slides ↗</a></span>
  </li>
</ul>

---

### Resources for Students {#resources}

- [BIEN R package](https://cran.r-project.org/package=BIEN)
- [OpenTraits data standards](https://opentraits.org/)
- [All FigShare lectures and presentations](https://figshare.com/authors/Brian_Enquist/663712)
- [ECOL 586 course blog](https://ecol586.wordpress.com/)

