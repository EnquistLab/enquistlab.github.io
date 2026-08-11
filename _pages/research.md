---
layout: page
title: research
permalink: /research/
description: Current research themes and projects in the Enquist Macroecology Lab
nav: false
nav_order: 3
---

## Research Program

<figure class="field-photo">
  <img src="{{ "/assets/img/field/brian_field.jpg" | relative_url }}" alt="Brian Enquist conducting field measurements" loading="lazy">
  <figcaption>Field measurements — connecting individual-level physiology to ecosystem-scale patterns.</figcaption>
</figure>

<div class="research-intro-grid">
<div class="research-intro-grid__text">
<p>Our lab studies how biodiversity is organized across scales — from leaves and individuals to communities, ecosystems, and the biosphere — and how those patterns shift under climate change and land-use pressure.</p>
<p>We connect observation, theory, and prediction in a single workflow: <strong>measure ecological patterns</strong> → <strong>develop mechanistic explanations</strong> → <strong>forecast future change</strong>.</p>
</div>
<aside class="research-program-card">
  <div class="research-program-card__photo">
    <img src="{{ '/assets/img/field/sefdp_forest_canopy.jpg' | relative_url }}" alt="Tropical forest canopy at a Smithsonian ForestGEO long-term monitoring plot — a site where MST allometric scaling predictions are tested at ecosystem scale" loading="lazy">
  </div>
  <div class="research-program-card__body">
    <div class="research-program-card__label">Explore Research</div>
    <ul class="research-program-card__links">
      <li><a href="#theory">Theory: MST &amp; TDT</a></li>
      <li><a href="#trait-based-ecology">Trait-Based Ecology</a></li>
      <li><a href="#ecophysiology">Ecophysiology</a></li>
      <li><a href="#bien-botanical-information-ecology-network">BIEN &amp; Informatics</a></li>
      <li><a href="#global-change-biology">Biodiversity Forecasting</a></li>
      <li><a href="#long-term-ecology">Long-Term Ecology</a></li>
      <li><a href="{{ '/field-sites/' | relative_url }}">Field Sites →</a></li>
    </ul>
  </div>
</aside>
</div>

<div class="research-theme-grid">
  <div class="research-theme-card">
    <h3>Scaling</h3>
    <p>How do body size, vascular architecture, and temperature shape growth, metabolism, and ecosystem function?</p>
  </div>
  <div class="research-theme-card">
    <h3>Traits</h3>
    <p>How do functional trait distributions predict community assembly, ecological filtering, and climate response?</p>
  </div>
  <div class="research-theme-card">
    <h3>Informatics</h3>
    <p>How do we synthesize millions of plant records, traits, and environmental layers into reproducible ecological tools?</p>
  </div>
  <div class="research-theme-card">
    <h3>Forecasting</h3>
    <p>How do biodiversity and ecosystem function change under alternative climates, land-use pressures, and disturbance?</p>
  </div>
</div>

---

### Theory {#theory}

The lab's empirical programs are grounded in two interconnected theoretical frameworks — **Metabolic Scaling Theory (MST)** and **Trait Driver Theory (TDT)** — that together aim to explain biological organization from cells to ecosystems and predict how communities respond to environmental change. Both frameworks are mathematically explicit: they generate quantitative, falsifiable predictions that can be confronted with data and refined.

#### Metabolic Scaling Theory (MST) {#metabolic-scaling-theory}

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <img src="{{ '/assets/img/wordpress/yoda_self_thinning_fig1.png' | relative_url }}" alt="Self-thinning law: plant density declines as a power function of mean plant mass" style="width:100%;border-radius:4px;" loading="lazy">
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Self-thinning law — plant density declines as a power function of mean plant mass as a stand develops, a direct prediction of MST from first principles of network geometry.</figcaption>
  </figure>
  <figure style="margin:0 0 0.75rem;">
    <img src="{{ '/assets/img/wordpress/yoda_self_thinning_fig2.png' | relative_url }}" alt="Derivation of self-thinning exponents from allometric first principles" style="width:100%;border-radius:4px;" loading="lazy">
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Derivation of self-thinning exponents from allometric first principles — connecting vascular network geometry to stand-level biomass dynamics.</figcaption>
  </figure>
  <div style="border-left:3px solid #4a90d9;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Recent lab papers</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://www.annualreviews.org/content/journals/10.1146/annurev-ecolsys-102723-054525">Vasseur, Mahaut, Enquist &amp; Violle (2025)</a> — From organism traits to ecosystem processes: why size is so important. <em>Ann. Rev. Ecol. Evol. Syst.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://royalsocietypublishing.org/doi/full/10.1098/rstb.2023.0010">Enquist, Erwin, Savage &amp; Marquet (2024)</a> — Scaling approaches and macroecology for ecological resilience in the Anthropocene. <em>Phil. Trans. B</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.pnas.org/doi/10.1073/pnas.2209196121">Enquist, Kempes &amp; West (2024)</a> — Developing a predictive science of the biosphere. <em>PNAS</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.nature.com/articles/s41467-020-14369-y">Enquist et al. (2020)</a> — The megabiota are disproportionately important for biosphere functioning. <em>Nature Communications</em></li>
    </ul>
  </div>
</div>

Metabolic Scaling Theory rests on a central insight: the branching tubes that deliver water and nutrients through a plant or animal are not arranged arbitrarily — they follow a geometry dictated by physics. That geometry imposes a universal constraint on how metabolic rate — the pace at which an organism burns energy — scales with body size. West, Brown, and Enquist showed that a space-filling, area-preserving fractal vascular network minimizes energy dissipation and thereby generates the ¾-power scaling of metabolic rate with body mass, $$B \propto M^{3/4}$$ ([West, Brown & Enquist 1997](https://doi.org/10.1126/science.276.5309.122)). Subsequent empirical tests have confirmed this relationship across more than 27 orders of magnitude in body mass ([Gillooly et al. 2001](https://doi.org/10.1126/science.1061967); [Savage et al. 2004](https://doi.org/10.1111/j.0269-8463.2004.00856.x)). This is not merely an empirical regularity — it is a derived consequence of network geometry and fluid-transport physics.

From this foundation, the theory generates a unified set of predictions. Growth rates, lifespan, reproductive output, and the turnover of energy and biomass all scale predictably with body size and temperature ([West, Brown & Enquist 1999](https://doi.org/10.1126/science.284.5420.1677)). In plants, the fractal vascular network constrains stem diameter, height, and leaf-area allometries ([West, Enquist & Brown 1999](https://doi.org/10.1038/23040)), and metabolic constraints set population density and above-ground biomass across forests ([Enquist, Brown & West 1998](https://doi.org/10.1038/28048)). Temperature scales metabolic rate through a well-characterized thermodynamic relationship: warmer organisms run faster metabolically. This grounds MST in physics rather than empiricism and creates a direct bridge to global-change projections — warmer climates predictably accelerate biological processes across levels of organization.

Brown et al. extended MST into the **Metabolic Theory of Ecology (MTE)** ([Brown et al. 2004](https://doi.org/10.1890/03-9000)), showing that the same mass and temperature scaling permeates population dynamics, species diversity gradients, ecosystem energy flux, and elemental stoichiometry. Current Enquist Lab work extends and tests MST predictions at ecosystem scale — connecting allometric constraints to forest carbon stocks, demography, and the structure of plant communities across biomes. Recent work examines how MST principles scale from organism traits and stoichiometry to ecosystem function ([Enquist, Michaletz & Kerkhoff 2016](https://www.cambridge.org/core/books/abs/biogeoscience-approach-to-ecosystems/toward-a-general-scaling-theory-for-linking-traits-stoichiometry-and-body-size-to-ecosystem-function/71B3511BF7753E8F636C921952DA76FA) / [PDF](https://www.researchgate.net/profile/Sean-Michaletz/publication/313987048_Toward_a_general_scaling_theory_for_linking_traits_stoichiometry_and_body_size_to_ecosystem_function/links/59e660734585151e545cdc1a/Toward-a-General-Scaling-Theory-for-Linking-Traits-Stoichiometry-and-Body-Size-to-Ecosystem-Function.pdf)), how the megabiota disproportionately drive biosphere functioning ([Enquist et al. 2020](https://www.nature.com/articles/s41467-020-14369-y)), and how scaling frameworks underpin assessments of ecological resilience in the Anthropocene ([Enquist, Erwin, Savage & Marquet 2024](https://royalsocietypublishing.org/doi/full/10.1098/rstb.2023.0010)).

**Scope:** subcellular metabolic pathways to biome-level carbon budgets.
**Goal:** derive macroecological patterns from first principles of physics and network geometry.
**Applications:** forest biomass and carbon modeling, demographic forecasting, climate-scaling of plant productivity, earth system model parameterization.

**Key papers:**

- [West, Brown & Enquist (1997)](https://doi.org/10.1126/science.276.5309.122) — fractal vascular networks and the ¾ scaling law
- [West, Brown & Enquist (1999)](https://doi.org/10.1126/science.284.5420.1677) — fractal geometry and allometric scaling across life
- [West, Enquist & Brown (1999)](https://doi.org/10.1038/23040) — general model for plant vascular structure and allometry (_Nature_)
- [Enquist, Brown & West (1998)](https://doi.org/10.1038/28048) — plant population density and biomass scaling
- [West, Enquist & Brown (2009)](https://doi.org/10.1073/pnas.0812294106) — a general quantitative theory of forest structure and dynamics
- [Enquist, Michaletz & Kerkhoff (2016)](https://www.cambridge.org/core/books/abs/biogeoscience-approach-to-ecosystems/toward-a-general-scaling-theory-for-linking-traits-stoichiometry-and-body-size-to-ecosystem-function/71B3511BF7753E8F636C921952DA76FA) ([PDF](https://www.researchgate.net/profile/Sean-Michaletz/publication/313987048_Toward_a_general_scaling_theory_for_linking_traits_stoichiometry_and_body_size_to_ecosystem_function/links/59e660734585151e545cdc1a/Toward-a-General-Scaling-Theory-for-Linking-Traits-Stoichiometry-and-Body-Size-to-Ecosystem-Function.pdf)) — Toward a general scaling theory linking traits, stoichiometry, and body size to ecosystem function. In: _Ecosystems: A Biogeoscience Approach_ (Johnson & Martin, eds.), Cambridge University Press
- [Enquist et al. (2020)](https://www.nature.com/articles/s41467-020-14369-y) — The megabiota are disproportionately important for biosphere functioning (_Nature Communications_)
- [Enquist, Erwin, Savage & Marquet (2024)](https://royalsocietypublishing.org/doi/full/10.1098/rstb.2023.0010) — Scaling approaches and macroecology provide a foundation for assessing ecological resilience in the Anthropocene (_Phil. Trans. B_)
- [Vasseur, Mahaut, Enquist & Violle (2025)](https://www.annualreviews.org/content/journals/10.1146/annurev-ecolsys-102723-054525) — From organism traits to ecosystem processes: why size is so important (_Ann. Rev. Ecol. Evol. Syst._)

<div style="clear:both;"></div>

#### Trait Driver Theory (TDT) {#trait-driver-theory}

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <div style="border-left:3px solid #4a90d9;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Recent lab papers</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://www.sciencedirect.com/science/article/pii/S0169534722002749">Chacón-Labella et al. (2022)</a> — How to improve scaling from traits to ecosystem processes. <em>Trends Ecol. Evol.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.14160">Maitner et al. (2023)</a> — Bootstrapping outperforms community-weighted approaches for estimating trait distributions. <em>Methods Ecol. Evol.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://onlinelibrary.wiley.com/doi/full/10.1111/ecog.06078">Wieczynski et al. (2022)</a> — Integrating trait-based models and remotely-sensed foliar trait data. <em>Ecography</em></li>
    </ul>
  </div>
</div>

While MST explains size- and temperature-dependent variation in metabolic flux, **Trait Driver Theory** addresses a complementary question: why do communities assemble the functional trait distributions they do, and how will those distributions shift as environments change? TDT is a quantitative, mechanistic framework that predicts the mean, variance, and shape of functional trait distributions in a local community as a function of environmental drivers — temperature, water availability, disturbance, and resource supply ([Enquist et al. 2015](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065250415000070)).

The core logic is probabilistic and multi-scale. At the regional scale, the pool of available species defines a prior distribution of trait values shaped by evolutionary history and dispersal. At the local scale, environmental filters and biotic interactions select from that pool, shifting the realized trait distribution in predictable directions. TDT formalizes this filtering mathematically: environmental drivers compress, shift, or broaden the trait distribution, with measurable consequences for community function. Because intraspecific trait variation (ITV) contributes substantially to total community-level trait variance, TDT explicitly partitions variation across levels — individual, population, species, and community — rather than collapsing it to species means. Empirical tests across tropical forests spanning broad temperature gradients confirm that environmental drivers shift functional trait distributions in the directions TDT predicts ([Enquist et al. 2017](https://onlinelibrary.wiley.com/doi/10.1111/geb.12645)).

TDT bridges scales that are often treated separately in ecology: individual physiology sets the trait values that are possible; evolutionary history determines what is available in a regional pool; environment determines what is favored locally; and the aggregate of these processes produces the community-level functional fingerprint that shapes carbon exchange, water flux, and competitive dynamics at ecosystem scale. This positions TDT as a theoretical spine connecting leaf-level measurements to global biodiversity forecasting.

**Scope:** individual leaf traits to continental-scale functional diversity gradients.
**Goal:** build a predictive, mathematically grounded theory of community assembly and ecosystem function based on trait distributions.
**Applications:** forecasting community trait shifts under climate change, explaining elevational and latitudinal diversity gradients, linking remote-sensing spectral signatures to functional state, improving land-surface model trait parameterizations.

**Key papers:**

- [Enquist et al. (2015)](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065250415000070) — original TDT framework and predictions
- [Enquist et al. (2017)](https://onlinelibrary.wiley.com/doi/10.1111/geb.12645) — assessing trait-based scaling theory across tropical forests spanning a broad temperature gradient (_Global Ecol. Biogeogr._)

<div style="clear:both;"></div>

---

### Trait-Based Ecology {#trait-based-ecology}

<figure class="field-photo">
  <img src="{{ '/assets/img/wordpress/dsc_3443.jpeg' | relative_url }}" alt="Snow-covered Andean peaks above alpine field terrain" loading="lazy">
  <figcaption>Trait ecology links leaf- and plant-level strategies to mountain-scale environmental gradients.</figcaption>
</figure>

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <img src="{{ '/assets/img/field/pftc5_peru.jpeg' | relative_url }}" alt="Researchers measuring plant functional traits on an Andean slope during a PFTC field course in Peru" style="width:100%;border-radius:4px;" loading="lazy">
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">PFTC field campaign, Wayqecha, Peru — standardized trait measurement along an elevation gradient from cloud forest to páramo.</figcaption>
  </figure>
  <div style="border-left:3px solid #2b6cb0;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Key papers</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.14160" rel="external nofollow noopener" target="_blank">Maitner et al. (2023)</a> — Bootstrap trait distributions outperform community-weighted means. <em>Methods Ecol. Evol.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://onlinelibrary.wiley.com/doi/10.1111/geb.12645" rel="external nofollow noopener" target="_blank">Enquist et al. (2017)</a> — Trait-based scaling across tropical forests. <em>Global Ecol. Biogeogr.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.nature.com/articles/s41559-021-01396-1" rel="external nofollow noopener" target="_blank">Kemppinen et al. (2021)</a> — Consistent trait–environment relationships in tundra. <em>Nat. Ecol. Evol.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://doi.org/10.1038/s41559-020-1109-6" rel="external nofollow noopener" target="_blank">Gallagher et al. (2020)</a> — Open Traits Network. <em>Nat. Ecol. Evol.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://onlinelibrary.wiley.com/doi/full/10.1111/ecog.06078" rel="external nofollow noopener" target="_blank">Wieczynski et al. (2022)</a> — Remote-sensing + trait models. <em>Ecography</em></li>
    </ul>
  </div>
</div>

Plant functional traits — leaf size, wood density, height, specific leaf area, water-use efficiency — are not merely descriptions of what plants look like. They are the currencies through which organisms manage their acquisition of carbon, water, and nutrients, and the entries through which evolution, environment, and ecological filtering jointly shape community composition. The lab's trait-based ecology program is organized around a single driving question: can we use the statistical distributions of functional traits within communities to predict how those communities will change as climates shift?

**The theoretical backbone** is [Trait Driver Theory (TDT)](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065250415000070), developed and tested in this lab ([Enquist et al. 2015](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065250415000070); [Enquist et al. 2017](https://onlinelibrary.wiley.com/doi/10.1111/geb.12645)), which predicts how trait distributions — not just mean values — shift as a direct function of environmental drivers. A key insight is that the _shape_ of a trait distribution encodes information about ecological filtering and community assembly that the mean discards. [Maitner et al. (2023)](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.14160) (_Methods Ecol. Evol._) demonstrated that standard community-weighted approaches systematically underestimate distributional tails — the parts of the trait distribution most sensitive to environmental extremes. The [`traitstrap`](https://cran.r-project.org/package=traitstrap) R package formalizes a bootstrap-based remedy, propagating intraspecific uncertainty through community-level calculations. [Kemppinen et al. (2021)](https://www.nature.com/articles/s41559-021-01396-1) (_Nat. Ecol. Evol._) confirmed that consistent trait–environment relationships hold within and across tundra communities, supporting TDT's core assumption that environment is a strong filter on which traits are expressed locally. Integrating remotely sensed spectral data with ground-based trait measurements further enables scaling functional diversity from plots to continents ([Wieczynski et al. 2022](https://onlinelibrary.wiley.com/doi/full/10.1111/ecog.06078), _Ecography_).

**Measurement and scale.** The lab co-organizes the international [Plant Functional Traits Courses (PFTC)]({{ '/resources/' | relative_url }}) — a program in which field courses produce open, publishable datasets as a direct pedagogical output. Published campaigns span Norway climate gradients ([Vandvik et al. 2025](https://www.nature.com/articles/s41597-025-05509-4), _Scientific Data_), Andean Puna grasslands in Peru ([Halbritter et al. 2024](https://www.nature.com/articles/s41597-024-02980-3), _Scientific Data_), and Afromontane grasslands of South Africa ([Halbritter et al. 2025](https://www.nature.com/articles/s41597-025-06045-x), _Scientific Data_). These campaigns link individual trait measurements to ecosystem gas fluxes along environmental gradients, testing whether trait-based models built on plots can scale to landscapes. At broader scales, lab contributions to TRY, OpenTraits, and BIEN include establishing data-quality standards for trait synthesis ([Gallagher et al. 2020](https://doi.org/10.1038/s41559-020-1109-6), _Nat. Ecol. Evol._; [Keller et al. 2023](https://doi.org/10.1111/2041-210X.14033), _Methods Ecol. Evol._).

**Forward look.** The next challenge is closing the loop from trait measurement to ecological forecast. Using measured trait distributions — including their bootstrapped uncertainty — to predict community responses to novel climates requires integrating traitstrap-style tools with demographic models, spectral remote sensing, and process-based land-surface frameworks. A key open question is whether trait–environment relationships calibrated in contemporary gradient studies transfer reliably to novel climatic states — the same extrapolation problem that challenges SDMs. Addressing it requires out-of-range validation, mechanistic model constraints, and explicit uncertainty quantification.

<div style="clear:both;"></div>

---

### Ecophysiology {#ecophysiology}

Ecophysiology — the study of how physical and physiological processes interact to govern plant function — is an area of sustained innovation in this lab. Building on the mechanistic foundations of Metabolic Scaling Theory, lab members extended physics, geometry, and physiology to explain why leaves are built the way they are, how they regulate temperature, how plant communities exchange carbon and water with the atmosphere, and how xylem network architecture constrains water transport from roots to leaves. These contributions span from vein-level biophysics to ecosystem-scale flux measurements, uniting individual organ function with broader macroecological patterns.

#### Leaf Venation & Leaf Functioning {#leaf-venation}

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <a href="{{ '/assets/img/ecophysiology/matos2025_fig2.png' | relative_url }}" target="_blank" rel="noopener" title="Click to enlarge">
      <img src="{{ '/assets/img/ecophysiology/matos2025_fig2.png' | relative_url }}" alt="Grid of cleared and stained leaves showing hierarchical venation at low and high vein density, colour-coded by vein order: primary (blue), secondary (green), tertiary (gold)" style="width:100%;border-radius:4px;cursor:zoom-in;" loading="lazy">
    </a>
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Hierarchical venation at low and high density: primary (blue), secondary (green), and tertiary (gold) veins. Vein density sets hydraulic conductance and photosynthetic capacity. © Matos et al. 2025, <em>Nature Plants</em>, CC-BY 4.0. <span style="font-style:italic;">Click to enlarge.</span></figcaption>
  </figure>
  <div style="border-left:3px solid #4a90d9;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Key papers</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://www.nature.com/articles/s41477-025-02011-y">Matos et al. (2025)</a> — Leaf venation network evolution across clades and scales. <em>Nature Plants.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/323107018">Blonder, Salinas, Bentley, Shenkin et al. &amp; Enquist (2018)</a> — Structural and defensive roles of angiosperm leaf venation network reticulation across an Andes–Amazon elevation gradient.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/47789081">Blonder, Violle, Bentley &amp; Enquist (2011)</a> — Leaf venation networks and the origin of the leaf economics spectrum. <em>Ecology Letters</em> 14:91–100.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/261603497">Blonder &amp; Enquist (2014)</a> — Inferring climate from angiosperm leaf venation network geometry. <em>New Phytologist</em> 204:116–126.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://doi.org/10.1093/jxb/eru143">Blonder, Violle, Bentley &amp; Enquist (2014)</a> — Inclusion of vein traits improves predictive power for the leaf economic spectrum. <em>J. Exp. Bot.</em> 65:5109–5114.</li>
    </ul>
  </div>
</div>

Leaf venation networks are biological distribution networks whose branching geometry, vein density, and topological reticulation set physical constraints on water delivery to mesophyll cells, CO₂ diffusion paths, and the energy budget of the leaf. The lab contributed a biophysical framework treating vein networks as optimized hydraulic circuits: vein density determines flow resistance from xylem conduit to cell, which in turn governs maximum stomatal conductance and photosynthetic capacity. This is network and graph theory applied to organ biology — the same first-principles logic that underlies metabolic scaling, now resolved at millimeter scales within a leaf lamina.

Empirically, Blonder et al. (2011) showed that vein geometry is a mechanistic origin of the leaf economic spectrum — the multivariate axis of leaf form and function encapsulating the slow–fast resource-acquisition continuum — and Blonder et al. (2014, _J. Exp. Bot._) demonstrated that including vein traits substantially improves its predictive power. Vein reticulation also varies systematically along the steep Andes–Amazon elevational gradient, reflecting structural reinforcement against herbivory and hydraulic adaptations to the combined stresses of freeze-thaw cycles and declining atmospheric pressure at altitude ([Blonder et al. 2018](https://www.researchgate.net/publication/323107018)). Matos et al. (2025, _Nature Plants_) extended this perspective phylogenetically, revealing how vein network architecture has evolved across angiosperm clades and spatial scales, shaped jointly by developmental constraints, hydraulic selection, and evolutionary history.

<div class="section-fill-card">
  <div class="section-fill-card__label">Related resources</div>
  <ul class="section-fill-card__links">
    <li><a href="{{ '/assets/img/ecophysiology/leaf_venation_network.svg' | relative_url }}" target="_blank" rel="noopener">Leaf vein network topology diagram →</a></li>
    <li><a href="#trait-based-ecology">Trait-based ecology: how vein density anchors the leaf economics spectrum</a></li>
    <li><a href="#plant-hydraulics">Plant Hydraulics &amp; Path Length: vascular constraints at tree scale</a></li>
  </ul>
</div>

<div style="clear:both;"></div>

#### Leaf Thermoregulation {#leaf-thermoregulation}

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <a href="{{ '/assets/img/ecophysiology/michaletz2016_fig2.jpg' | relative_url }}" target="_blank" rel="noopener" title="Click to enlarge">
      <img src="{{ '/assets/img/ecophysiology/michaletz2016_fig2.jpg' | relative_url }}" alt="Scatter plots of leaf temperature excess (T_leaf minus T_air) versus air temperature across field sites, showing active thermoregulation" style="width:100%;border-radius:4px;cursor:zoom-in;" loading="lazy">
    </a>
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Leaf temperature excess (T<sub>leaf</sub> − T<sub>air</sub>) across air temperatures: leaves thermoregulate rather than passively tracking air temperature. © Michaletz, Enquist et al. 2016, <em>Nature Plants</em>, CC-BY 4.0. <span style="font-style:italic;">Click to enlarge.</span></figcaption>
  </figure>
  <div style="border-left:3px solid #4a90d9;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Key papers</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/282939777">Michaletz, Weiser, Zhou, Kaspari, Helliker &amp; Enquist (2015)</a> — Plant thermoregulation: energetics, trait–environment interactions, and carbon economics. <em>Trends Ecol. Evol.</em> 30:714–724.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/306394173">Michaletz, Weiser, McDowell, Zhou, Kaspari, Helliker &amp; Enquist (2016)</a> — The energetic and carbon economic origins of leaf thermoregulation. <em>Nature Plants</em> 2:16129.</li>
    </ul>
  </div>
</div>

Leaves are not passive temperature recorders. They actively modulate their temperature through transpirational cooling, boundary layer conductance, and leaf geometry — size, shape, and orientation all govern how heat is exchanged with the surrounding atmosphere. Michaletz, Enquist, and colleagues developed an energy-balance biophysical framework that predicts the offset between leaf temperature and air temperature as a function of absorbed radiation, wind speed, stomatal conductance, and leaf size. This offset is not a minor correction: it can exceed several degrees Celsius under high-radiation, low-wind conditions, with meaningful consequences for enzymatic rates, stomatal behavior, and water-use efficiency.

The macroecological implication is significant. Standard correlative analyses that link plant traits to climate using ambient air temperature may systematically misrepresent the thermal environment that leaf biochemistry actually experiences. Incorporating energy-balance physics into trait–climate frameworks yields mechanistically grounded predictions of how functional trait distributions will shift as both air temperature and vapor pressure deficit increase under climate change — and identifies where correlative approaches are most likely to fail.

<div class="section-fill-card">
  <div class="section-fill-card__label">Related resources</div>
  <ul class="section-fill-card__links">
    <li><a href="{{ '/assets/img/ecophysiology/leaf_energy_balance.svg' | relative_url }}" target="_blank" rel="noopener">Leaf energy balance diagram →</a></li>
    <li><a href="#community-carbon-water">Plant Community Carbon &amp; Water Exchange: scaling leaf function to ecosystem flux</a></li>
  </ul>
</div>

<div style="clear:both;"></div>

#### Plant Community Carbon & Water Exchange {#community-carbon-water}

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <a href="{{ '/assets/img/ecophysiology/fluxible_tent_peru.jpg' | relative_url }}" target="_blank" rel="noopener" title="Click to enlarge">
      <img src="{{ '/assets/img/ecophysiology/fluxible_tent_peru.jpg' | relative_url }}" alt="Researchers deploying a large closed-loop transparent flux chamber in Andean páramo grassland to measure ecosystem CO2 and H2O exchange" style="width:100%;border-radius:4px;cursor:zoom-in;" loading="lazy">
    </a>
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Closed-loop chamber deployment in Andean páramo. Photo: Gaudard, Enquist et al. 2025 (<a href="https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/2041-210X.70161">fluxible</a> project). <span style="font-style:italic;">Click to enlarge.</span></figcaption>
  </figure>
  <figure style="margin:0 0 0.75rem;">
    <a href="{{ '/assets/img/ecophysiology/halbritter2025_fig1.png' | relative_url }}" target="_blank" rel="noopener" title="Click to enlarge">
      <img src="{{ '/assets/img/ecophysiology/halbritter2025_fig1.png' | relative_url }}" alt="Multi-site elevational field study design in Afromontane Drakensberg grasslands showing paired east-west measurement plots across five elevations" style="width:100%;border-radius:4px;cursor:zoom-in;" loading="lazy">
    </a>
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Afromontane field campaign: paired plots across five elevations (2000–2800 m) in Maloti-Drakensberg grasslands measuring plant traits and ecosystem CO₂/H₂O fluxes. © Halbritter et al. 2025, <em>Scientific Data</em>, CC-BY 4.0. <span style="font-style:italic;">Click to enlarge.</span></figcaption>
  </figure>
  <div style="border-left:3px solid #4a90d9;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Key papers</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/272494697" rel="external nofollow noopener" target="_blank">Sloat, Henderson, Lamanna &amp; Enquist (2015)</a> — The effect of the foresummer drought on carbon uptake across western U.S. grasslands. <em>Ecosystems</em> 18:533–545.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/317752755">Sørensen, Strimbeck, Nystuen, Kapas, Enquist &amp; Graae (2017)</a> — Draining the pool? Carbon storage and fluxes in three alpine plant communities. <em>Ecosystems</em> 21:316–330.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/2041-210X.70161">Gaudard, Telford, Chacon-Labella, Dawson, Enquist, Töpper et al. &amp; Halbritter (2025)</a> — fluxible: An R package to process ecosystem gas fluxes from closed-loop chambers in an automated and reproducible way. <em>Methods Ecol. Evol.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.nature.com/articles/s41597-025-06045-x">Halbritter, Vandvik, Bison, Clark, Cross, Greve et al. &amp; Enquist (2025)</a> — Plant traits and associated ecological data from Afromontane grasslands of Maloti-Drakensberg, South Africa. <em>Scientific Data</em> 12(1):1778.</li>
    </ul>
  </div>
</div>

Connecting individual leaf function to ecosystem-scale carbon and water balance requires measurements at multiple spatial scales. The lab has contributed to closed-loop and open-path chamber-based approaches that capture net ecosystem exchange of CO₂ and H₂O at fine spatial resolutions, complementing eddy covariance flux towers and enabling reproducible measurements in remote or structurally complex ecosystems where tower deployment is impractical. A key finding from this work is that community composition — not just climate — is a primary mediator of ecosystem carbon uptake: [Sloat, Henderson, Lamanna & Enquist (2015)](https://www.researchgate.net/publication/272494697) (_Ecosystems_ 18:533–545) showed that the **foresummer drought** — the window of low soil moisture between snowmelt and summer monsoon rains at Rocky Mountain sites — significantly suppresses net ecosystem carbon uptake, and that whether a meadow is forb-dominated or grass-dominated determines the magnitude of that suppression. This sensitivity to vegetation functional composition means that trait-based characterizations of communities are necessary inputs to carbon flux models, not just descriptors. Sørensen et al. (2017) extended this comparative approach across three alpine plant community types, demonstrating community-level variation in carbon storage and flux balance under analogous climate pressures.

The [fluxible](https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/2041-210X.70161) R package, co-authored by Enquist and collaborators, provides an automated and reproducible workflow for processing raw chamber flux time series — from gas concentration change curves to net ecosystem exchange estimates — with explicit uncertainty propagation and standardized output formats for multi-site comparisons. The lab has also released [co2fluxtent](https://github.com/PaulESantos/co2fluxtent), an internally developed R package designed for open-path flux tent deployments, extending the lab's chamber-based toolchain to additional measurement configurations. This tooling underpins field campaigns including work in the Maloti-Drakensberg Afromontane grasslands of South Africa, an ecosystem poorly represented in global carbon budgets. The associated trait and ecological dataset ([Halbritter et al. 2025](https://www.nature.com/articles/s41597-025-06045-x)) links functional trait variation to ecosystem functioning in high-altitude grasslands under increasing climate pressure, providing a reproducible foundation for future synthesis across Afromontane biomes.

<div style="clear:both;"></div>

#### Plant Hydraulics & Path Length {#plant-hydraulics}

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <a href="{{ '/assets/img/ecophysiology/brummer2021_fig1_full.png' | relative_url }}" target="_blank" rel="noopener" title="Click to enlarge">
      <div class="fig-crop"><img src="{{ '/assets/img/ecophysiology/brummer2021_fig1_full.png' | relative_url }}" alt="Comparison of plant (angiosperm tree) and mammalian (mouse lung) vascular branching silhouettes plus scatter plots of branching geometry, illustrating shared geometric principles across biological transport networks" style="cursor:zoom-in;" loading="lazy"></div>
    </a>
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Plant and animal branching networks share geometric principles: radial and length scale factors distinguish angiosperm, gymnosperm, and mammalian vascular systems. © Brummer, Enquist et al. 2021, <em>J. R. Soc. Interface</em>, CC-BY 4.0. <span style="font-style:italic;">Click to enlarge.</span></figcaption>
  </figure>
  <div style="border-left:3px solid #4a90d9;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Key papers</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/216811042">Enquist (2003)</a> — Cope's Rule and the evolution of long-distance transport in vascular plants: allometric scaling, biomass partitioning, and optimization. <em>Plant, Cell &amp; Environment</em> 26:151–161.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/49675520">Savage, Bentley, Enquist, Sperry, Smith, Reich &amp; von Allmen (2010)</a> — Hydraulic tradeoffs and space-filling enable predictions of vascular structure and function in plants. <em>PNAS</em> 107:22722–22727.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/257531792">Smith, Sperry, Enquist, Savage, McCulloh &amp; Bentley (2014)</a> — Deviation from symmetrically self-similar branching in trees predicts altered hydraulics, mechanics, light interception and metabolic scaling. <em>New Phytologist</em> 201:217–229.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://doi.org/10.1098/rsif.2020.0624">Brummer et al. &amp; Enquist (2021)</a> — Branching principles of animal and plant networks identified by combining extensive data, machine learning and modelling. <em>J. R. Soc. Interface.</em></li>
    </ul>
  </div>
</div>

Water flows upward through plant tissue under tension — leaves lose water to the air through transpiration, and that loss pulls a continuous column of water from soil to canopy. The path length from root tip to leaf sets total hydraulic resistance, and the tapering of conduit diameter from trunk to twig determines how resistance is distributed along the flow path. The West-Brown-Enquist vascular network model predicts that optimal tapering — minimizing total transport resistance while maintaining space-filling — generates the ¾-power metabolic scaling and the allometric relationships among stem diameter, height, and leaf area observed across plant life. Hydraulics is therefore not a module separate from metabolic scaling theory but a mechanistic foundation of it.

Enquist (2003) extended this reasoning to macroevolution, connecting Cope's Rule — the recurrent evolutionary tendency toward larger body size across lineages — to directional selection favoring longer-distance water transport and the biomass partitioning trade-offs that accompany increasing plant size. Savage et al. (2010) demonstrated that introducing hydraulic trade-offs and space-filling constraints into the vascular network model substantially improves predictions of conduit structure and function across plant size classes. Smith et al. (2014) showed empirically that deviations from idealized symmetric self-similar branching carry simultaneous, predictable consequences for hydraulic efficiency, mechanical support, light interception, and metabolic scaling — revealing the multi-functional constraints under which real plant architectures evolve. Brummer et al. (2021) used machine learning and extensive branching data from both animal and plant networks to identify the shared geometric principles underlying biological transport networks, grounding plant hydraulic theory within a broader comparative framework.

<div class="section-fill-card">
  <div class="section-fill-card__label">Related resources</div>
  <ul class="section-fill-card__links">
    <li><a href="{{ '/assets/img/ecophysiology/plant_hydraulic_network.svg' | relative_url }}" target="_blank" rel="noopener">Plant vascular network diagram →</a></li>
    <li><a href="#metabolic-scaling-theory">Metabolic Scaling Theory: how hydraulic geometry underlies the ¾ scaling law</a></li>
  </ul>
</div>

<div style="clear:both;"></div>

---

### BIEN: Botanical Information & Ecology Network {#bien-botanical-information-ecology-network}

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <img src="{{ '/assets/img/wordpress/bci-trail-map.jpg' | relative_url }}" alt="Map of Barro Colorado Island ForestGEO plot network in Panama — one of the intensive study sites whose data flow into the BIEN database" style="width:100%;border-radius:4px;" loading="lazy">
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">Barro Colorado Island, Panama — one of many intensive plot networks whose occurrence and trait data are integrated in BIEN.</figcaption>
  </figure>
  <div style="border-left:3px solid #2b6cb0;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Key resources</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/2041-210x.70274" rel="external nofollow noopener" target="_blank">Enquist et al. (2026)</a> — BIEN: a global synthesis resource for Western Hemisphere plants. <em>Methods Ecol. Evol.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://cran.r-project.org/package=BIEN" rel="external nofollow noopener" target="_blank">BIEN R package</a> — programmatic access to occurrences, traits, ranges, and plot data.</li>
      <li style="margin-bottom:0.35rem;"><a href="https://biendata.org/" rel="external nofollow noopener" target="_blank">biendata.org</a> — GeoSpatial portal and documentation.</li>
    </ul>
  </div>
</div>

<img src="{{ '/assets/img/wordpress/bien_logo_notext-1.png' | relative_url }}" alt="BIEN — Botanical Information and Ecology Network" style="max-width:180px;width:100%;display:block;margin:0.4rem 0 0.9rem;">

Reliable biodiversity science requires reliable data — and that requires knowing where species have actually been recorded, how completely those records reflect reality, and whether the names attached to records refer to the same entity across time and region. The [BIEN project](https://biendata.org/) addresses this at continental scale: it compiles and standardizes occurrence records, plant trait measurements, and vegetation plot data for vascular plants across the Western Hemisphere, making it one of the largest plant biodiversity synthesis efforts globally. The database integrates herbarium specimens, citizen-science observations, and plot inventories spanning roughly 1800s–present, with taxonomic reconciliation against a versioned plant name backbone and coordinate-level QA filtering that removes records with known georeferencing errors, cultivated provenance, or coordinate–country mismatches. The result is a synthesis resource that underpins macroecological analyses, SDM workflows, and trait-based forecasting at scales from regional to hemispheric ([Enquist et al. 2026](https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/2041-210x.70274), _Methods Ecol. Evol._).

<div style="clear:both;"></div>

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

#### Explore BIEN Species Data Interactively

Browse occurrence records and range maps for ~120,000 Western Hemisphere plant species — filter by native status, political unit, and elevation, then download georeferenced records and range polygons directly from the app.

<div style="margin: 1.5rem 0 0.5rem;">
  <iframe
    src="https://benquist.shinyapps.io/bien-species-shinyapp/"
    title="BIEN Species Explorer"
    width="100%"
    height="650"
    style="border: none; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.13);"
    loading="lazy"
    allowfullscreen>
  </iframe>
</div>

<p style="text-align:center; margin-bottom: 2rem;">
  <a class="status-chip status-chip--info" href="https://benquist.shinyapps.io/bien-species-shinyapp/" target="_blank" rel="noopener">Open BIEN Species Explorer in a new tab &rarr;</a>
</p>

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

### Forecasting Biodiversity Under Global Change {#global-change-biology}

<figure class="field-photo">
  <img src="{{ '/assets/img/field/aberg_andes.jpeg' | relative_url }}" alt="Andean mountain landscape along an elevational gradient where vegetation composition shifts driven by climate are being documented" loading="lazy">
  <figcaption>Andean elevational gradient — documenting vegetation shifts as a testbed for biodiversity forecasting models.</figcaption>
</figure>

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <img src="{{ '/assets/img/wordpress/sparc_overview_map.jpg' | relative_url }}" alt="SPARC protected-area prioritization map showing biodiversity conservation priority regions across the Americas, derived from BIEN occurrence data" style="width:100%;border-radius:4px;" loading="lazy">
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">SPARC conservation priority regions across the Americas — integrating BIEN species occurrence and climate data.</figcaption>
  </figure>
  <div style="border-left:3px solid #2b6cb0;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Key papers</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://www.nature.com/articles/s41467-023-44321-9" rel="external nofollow noopener" target="_blank">Boonman et al. (2024)</a> — 17,000+ tree species at risk from rapid global change. <em>Nature Communications</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://doi.org/10.1038/s41477-022-01130-0" rel="external nofollow noopener" target="_blank">Pillet et al. (2022)</a> — Elevated extinction risk of cacti under climate change. <em>Nature Plants</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.pnas.org/doi/abs/10.1073/pnas.2517585122" rel="external nofollow noopener" target="_blank">Moulatlet et al. (2025)</a> — Climatic niche breadth predicts plant range size globally. <em>PNAS</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://onlinelibrary.wiley.com/doi/full/10.1111/geb.13847" rel="external nofollow noopener" target="_blank">Serra-Diaz et al. (2024)</a> — occTest: systematic QA of species occurrence data. <em>Global Ecol. Biogeogr.</em></li>
    </ul>
  </div>
</div>

Species and communities do not experience climate change only in the future — they are experiencing it now. Range edges are already contracting and shifting, functional compositions are already changing, and species in some regions are already encountering climates with no historical analogue in their evolutionary experience. Translating these ongoing changes into defensible projections requires integrating occurrence data, trait information, and climate forcing within models that are explicit about their assumptions and honest about the limits of their predictions.

**What we have found.** Applying species distribution models to the global tree flora, [Boonman et al. (2024)](https://www.nature.com/articles/s41467-023-44321-9) (_Nature Communications_) estimated that more than 17,000 tree species — roughly 30% of all tree species globally — face elevated risk under business-as-usual emissions, with tropical and island taxa disproportionately affected. A companion analysis ([Boonman et al. 2025](https://www.pnas.org/doi/abs/10.1073/pnas.2420059122), _PNAS_) found that even under the most optimistic mitigation scenario, a substantial fraction of tree diversity will be exposed to macroclimatic conditions unprecedented in their evolutionary history — meaning extrapolation beyond calibration space is unavoidable regardless of emission pathway. Taxon-specific analyses sharpen the picture: [Pillet et al. (2022)](https://doi.org/10.1038/s41477-022-01130-0) (_Nature Plants_) showed that more than 60% of cactus species face elevated extinction risk, with arid-land endemics experiencing the sharpest projected range contractions. [Moulatlet et al. (2025)](https://www.pnas.org/doi/abs/10.1073/pnas.2517585122) (_PNAS_) connected climatic niche breadth to range size and ecological dominance across the global plant flora, establishing a mechanistic basis for why narrow-niche specialists are disproportionately vulnerable.

**Uncertainty, transferability, and data quality.** All projections in this lab are conditional on the emission scenario assumed, the overlap between calibration and future climate space, and the quality of underlying occurrence data. We use similarity surfaces (MESS) to flag where projections extend beyond training-climate space; results in extrapolation zones are reported with explicit uncertainty ranges rather than treated as equivalent to interpolations. Occurrence data pass through `occTest` ([Serra-Diaz et al. 2024](https://onlinelibrary.wiley.com/doi/full/10.1111/geb.13847), _GEB_), a multi-test quality control pipeline that removes coordinate errors, duplicates, and records inconsistent with known ecological context. We apply spatial thinning, bias layers, and target-group background sampling to mitigate the spatial overrepresentation of well-surveyed regions endemic to herbarium and citizen-science datasets. Models are validated against temporal holdouts and independent regional data where available.

**Forward look.** The next generation of biodiversity forecasting moves from correlative SDMs toward mechanistically constrained projection — integrating trait-based models that predict _which functional types_ persist under novel climates with demographic models capturing lag effects and dispersal limitation. Current BIEN data synthesis ([Enquist et al. 2026](https://doi.org/10.1111/2041-210x.70274), _Methods Ecol. Evol._) provides the occurrence and trait data platform for this integration across the Western Hemisphere.

<div style="clear:both;"></div>

---

### Collaborative Initiatives

We actively collaborate with local and international initiatives that support field work, synthesis, and training for students, postdocs, and collaborators. These collaborations include biodiversity forecasting and conservation planning efforts, including SPARC and related protected-area prioritization projects.

See [collaborators]({{ '/collaborators/' | relative_url }}) for examples.

---

### Long-Term Ecology {#long-term-ecology}

<div style="float:right;width:40%;max-width:340px;margin-left:1.5rem;margin-bottom:1rem;">
  <figure style="margin:0 0 0.75rem;">
    <a href="{{ '/assets/img/transplant/bektas2024-transplant-network-fig2.jpg' | relative_url }}" target="_blank" rel="noopener" title="Click to enlarge">
      <img src="{{ '/assets/img/transplant/bektas2024-transplant-network-fig2.jpg' | relative_url }}" alt="TransPlant Network map showing 22 elevation gradient sites across 20 mountainous regions used to test community responses to experimental climate warming" style="width:100%;border-radius:4px;cursor:zoom-in;" loading="lazy">
    </a>
    <figcaption style="font-size:0.78rem;color:#555;margin-top:0.35rem;">The TransPlant Network — 22 elevation gradient sites across 20 mountain regions for coordinated whole-community transplant experiments. © Bektas et al. 2024, <em>Ecography</em>. <span style="font-style:italic;">Click to enlarge.</span></figcaption>
  </figure>
  <div style="border-left:3px solid #2b6cb0;padding-left:0.75rem;">
    <div style="font-size:0.82rem;font-weight:600;margin-bottom:0.4rem;">Key papers &amp; sites</div>
    <ul style="font-size:0.8rem;margin:0;padding-left:1.1rem;line-height:1.45;">
      <li style="margin-bottom:0.35rem;"><a href="https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/ecog.07378" rel="external nofollow noopener" target="_blank">Bektas et al. (2024)</a> — TransPlant Network design and protocols. <em>Ecography</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/339468161" rel="external nofollow noopener" target="_blank">Swenson, Hulshof, Katabuchi &amp; Enquist (2020)</a> — 30-year functional diversity shifts in tropical dry forest. <em>Ecol. Monogr.</em></li>
      <li style="margin-bottom:0.35rem;"><a href="https://www.researchgate.net/publication/272494697" rel="external nofollow noopener" target="_blank">Sloat et al. (2015)</a> — Foresummer drought and alpine carbon uptake. <em>Ecosystems</em></li>
      <li style="margin-bottom:0.35rem;"><a href="{{ '/field-sites/' | relative_url }}">Field Sites page →</a></li>
    </ul>
  </div>
</div>

Ecological understanding limited to snapshot comparisons across space cannot reliably separate the signal of climate change from the noise of local history, soil variation, and community assembly. Long-term repeated measurements at fixed sites provide the temporal leverage needed to detect genuine change, test process-based predictions, and validate models built on space-for-time substitutions. The lab has invested in this infrastructure across three complementary systems: a tropical dry forest dynamics plot running since the 1970s, a temperate montane monitoring transect operating since 2003, and a whole-community climate change experiment embedded in a global transplant network.

**San Emilio Forest Dynamics Plot (SEFDP).** The SEFDP in Santa Rosa National Park, Area de Conservación Guanacaste, Costa Rica, is among the oldest and largest tropical forest dynamics plots in the Western Hemisphere and a member of the [ForestGEO global network](https://forestgeo.si.edu/sites/san-emilio). First censused by Stevens and Hubbell in 1976 (~15 ha, ~50,000 stems, ~200 woody species), the plot has been fully resurveyed in 1995–96, 2006–07, and most recently 2019–2021, generating a nearly 50-year record through repeated El Niño droughts and disturbance cycles in a seasonally dry tropical system. Analysis of this record has revealed that community responses to drought and historical disturbance are strongly non-uniform across functional types: drought-tolerant and drought-sensitive assemblages diverge on different compositional trajectories, confounding predictions based on mean community shifts alone. [Swenson, Hulshof, Katabuchi, & Enquist (2020)](https://www.researchgate.net/publication/339468161) (_Ecol. Monogr._ 90:e01408) documented systematic shifts in functional composition and diversity across three decades, implicating long-term climate forcing on top of disturbance legacies — one of the most temporally resolved records of functional change in any tropical system. The [dedicated San Emilio Forest Dynamics Plot site](https://benquist.github.io/SanEmilioForestDynamicsPlot.github.io/) is the place to explore this long-term research program in more depth, including its full census history and data-access information.

**RMBL montane gradient.** Since 2003 the lab has monitored ecosystem carbon fluxes, species composition, and functional trait distributions across an elevational gradient at the [Rocky Mountain Biological Laboratory](https://www.rmbl.org/) in Gothic, Colorado. Work from this system revealed that the **foresummer drought** — the period of low soil moisture between snowmelt and summer monsoon rains — is a key driver of year-to-year variation in ecosystem carbon uptake, with community composition mediating sensitivity ([Sloat et al. 2015](https://www.researchgate.net/publication/272494697), _Ecosystems_ 18:533).

**RMBL Transplant Project and TransPlant Network.** Beginning in 2017, intact 0.5 m² meadow turf blocks — vegetation and soil together — were moved ±400 m along an elevational gradient in Washington Gulch, simulating rapid climate warming or cooling under field conditions. Because the community structure and soil biota move intact, confounding factors that plague observational gradient studies are minimized. The experiment is embedded within the [TransPlant Network](https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/ecog.07378) ([Bektas et al. 2024](https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/ecog.07378), _Ecography_) — 22 elevation gradients across 20 mountainous regions of the Northern Hemisphere — enabling cross-biome meta-analysis of how warming restructures plant functional diversity, productivity, and ecosystem carbon balance.

<div class="photo-strip photo-strip--three">
  <figure>
    <img src="{{ '/assets/img/transplant/img_4955.jpeg' | relative_url }}" alt="RMBL mountain meadow transplant blocks in Washington Gulch, Colorado — whole-community turf blocks moved along an elevational gradient" loading="lazy">
    <figcaption>Transplant blocks at RMBL — entire meadow communities moved upslope and downslope.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/field/sefdp_resurvey_team.jpeg' | relative_url }}" alt="Resurvey team measuring trees at the San Emilio Forest Dynamics Plot in Costa Rica" loading="lazy">
    <figcaption>SEFDP resurvey team — a nearly 50-year demographic record in seasonal tropical dry forest.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/field/sefdp_lidar.jpg' | relative_url }}" alt="LiDAR canopy scan at the San Emilio ForestGEO plot — 3D structure mapped to connect stem-level censuses to canopy-scale biomass" loading="lazy">
    <figcaption>LiDAR mapping at SEFDP — 3D canopy structure connecting stem censuses to forest biomass.</figcaption>
  </figure>
</div>

<div style="clear:both;"></div>

---

### OpenTraits & Biodiversity Informatics {#opentraits-biodiversity-informatics}

The Enquist Lab is a co-founding member and active contributor to the [Open Traits Network (OTN)](https://opentraits.org/) — a global, decentralized community of researchers and institutions working to standardize and integrate trait data across all organisms. OTN is guided by Open Science principles: open methods, open source, and open data.

**What the OTN does.**
The network maintains a [global registry of trait-based initiatives](https://opentraits.org/datasets.html), shares reproducible workflows and tools for aggregating trait data, advocates for free data flow and appropriate attribution of effort, and works toward a shared _trait core_ — a minimal interoperable vocabulary that facilitates synthesis across databases. The registry currently spans hundreds of datasets, covering plants, animals, fungi, and microbes across all biomes.

**Our contributions and roles.**
Lab members have contributed to OTN in multiple capacities:

- **Co-authoring the network's foundational paper**: [Gallagher et al. (2020)](https://doi.org/10.1038/s41559-020-1109-6) _Nature Ecology & Evolution_ — introducing OTN and its open-science vision for trait data across all life.
- **Best-practice guidance**: Enquist is a contributing author on [Keller et al. (2023)](https://doi.org/10.1111/2041-210X.14033) _Methods in Ecology and Evolution_ — "Ten (mostly) simple rules to future-proof trait data in ecological and evolutionary sciences" — an open, community-driven resource now hosted at [opentraits.org/best-practices.html](https://opentraits.org/best-practices.html).
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

| Resource                                                     | Scope                                        |
| ------------------------------------------------------------ | -------------------------------------------- |
| [TRY Plant Trait Database](https://www.try-db.org/)          | Global plant traits, >15M records            |
| [BIEN](https://bien.nceas.ucsb.edu/bien/)                    | Neotropical plant occurrence and traits      |
| [FRED](https://roots.ornl.gov/)                              | Fine-root traits across ecosystems           |
| [GBIF](https://www.gbif.org/)                                | Global biodiversity occurrence records       |
| [GIFT](https://gift.uni-goettingen.de/)                      | Plant species richness and functional traits |
| [OTN Dataset Registry](https://opentraits.org/datasets.html) | Cross-taxon trait database catalog           |

**Biodiversity informatics more broadly.**
Beyond trait databases, the lab contributes to informatics infrastructure for ecological synthesis: Darwin Core extensions for trait data, quality-control pipelines for taxonomic reconciliation, and open workflows connecting field observations to continental-scale synthesis products. This infrastructure underpins our forecasting work through BIEN and enables reproducible, uncertainty-aware macroecology at global scale.
