---
layout: page
title: team
permalink: /people/
description: Members and alumni of the Enquist Macroecology Lab
nav: true
nav_order: 4
---

<!-- ============================================================
     PEOPLE PAGE
     Member data lives in _data/people.yml and is synced
     automatically from the lab's Google Sheet via the
     "Sync People Sheet" GitHub Actions workflow.

     To update your entry, use the Google Form linked in
     _data/people.yml (or the lab wiki).
     ============================================================ -->

<div class="photo-pair" style="margin-bottom:2.5rem;">
  <figure>
    <img src="{{ '/assets/img/team/lab_group_costa_rica.jpeg' | relative_url }}" alt="Lab team at the San Emilio Forest Dynamics Plot, Costa Rica" loading="lazy">
    <figcaption>Field team at the San Emilio Forest Dynamics Plot, Costa Rica</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/team/pftc_group.jpeg' | relative_url }}" alt="PFTC team, Peru" loading="lazy">
    <figcaption>Plant Functional Trait Course students and researchers, Peru</figcaption>
  </figure>
</div>

## Principal Investigator

<div class="team-pi">
  <img src="{{ '/assets/img/team/brian_enquist.jpg' | relative_url }}" alt="Brian J. Enquist" class="team-pi__photo">
  <div class="team-pi__bio">
    <h3>Brian J. Enquist</h3>
    <p>Professor, Department of Ecology and Evolutionary Biology, University of Arizona; External Professor, Santa Fe Institute.</p>
    <p>
      <a href="https://scholar.google.com/citations?user=mAbA6EoAAAAJ&hl=en">Google Scholar</a> ·
      <a href="https://github.com/bjenquist">GitHub</a> ·
      <a href="mailto:benquist@arizona.edu">benquist@arizona.edu</a>
    </p>
    <blockquote>"If you want to build a ship, do not drum up people to collect wood and assign tasks, but rather teach them to long for the endless immensity of the sea." — Antoine de Saint-Exupery</blockquote>
  </div>
</div>

---

{% if site.data.people.postdocs.size > 0 %}
## Postdoctoral Researchers

<div class="team-grid">
{% for person in site.data.people.postdocs %}
  <div class="team-card">
    {% if person.photo and person.photo != "" %}
      <img src="{{ '/assets/img/team/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="team-card__photo" loading="lazy">
    {% else %}
      <div class="team-card__photo team-card__photo--placeholder" aria-hidden="true">
        <span>{{ person.name | split: " " | map: "first" | join: "" | truncate: 2, "" | upcase }}</span>
      </div>
    {% endif %}
    <p class="team-card__name">{{ person.name }}</p>
    {% if person.affiliation and person.affiliation != "" %}
      <p class="team-card__role">{{ person.affiliation }}</p>
    {% endif %}
    {% if person.bio and person.bio != "" %}
      <p class="team-card__bio">{{ person.bio }}</p>
    {% endif %}
    <p class="team-card__links">
      {% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" title="Google Scholar" target="_blank" rel="noopener">Scholar</a>{% endif %}
      {% if person.github and person.github != "" %}{% if person.google_scholar and person.google_scholar != "" %} · {% endif %}<a href="{{ person.github }}" title="GitHub" target="_blank" rel="noopener">GitHub</a>{% endif %}
      {% if person.website and person.website != "" %}{% if person.google_scholar and person.google_scholar != "" or person.github and person.github != "" %} · {% endif %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
      {% if person.email and person.email != "" %}{% if person.google_scholar and person.google_scholar != "" or person.github and person.github != "" or person.website and person.website != "" %} · {% endif %}<a href="mailto:{{ person.email }}" title="Email">Email</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
{% endif %}

---

{% if site.data.people.grad_students.size > 0 %}
## Graduate Students

<div class="team-grid">
{% for person in site.data.people.grad_students %}
  <div class="team-card">
    {% if person.photo and person.photo != "" %}
      <img src="{{ '/assets/img/team/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="team-card__photo" loading="lazy">
    {% else %}
      <div class="team-card__photo team-card__photo--placeholder" aria-hidden="true">
        <span>{{ person.name | split: " " | map: "first" | join: "" | truncate: 2, "" | upcase }}</span>
      </div>
    {% endif %}
    <p class="team-card__name">{{ person.name }}</p>
    {% if person.degree and person.degree != "" %}
      <p class="team-card__role">{{ person.degree }} Student</p>
    {% endif %}
    {% if person.bio and person.bio != "" %}
      <p class="team-card__bio">{{ person.bio }}</p>
    {% endif %}
    <p class="team-card__links">
      {% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" title="Google Scholar" target="_blank" rel="noopener">Scholar</a>{% endif %}
      {% if person.github and person.github != "" %}{% if person.google_scholar and person.google_scholar != "" %} · {% endif %}<a href="{{ person.github }}" title="GitHub" target="_blank" rel="noopener">GitHub</a>{% endif %}
      {% if person.website and person.website != "" %}{% if person.google_scholar and person.google_scholar != "" or person.github and person.github != "" %} · {% endif %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
      {% if person.email and person.email != "" %}{% if person.google_scholar and person.google_scholar != "" or person.github and person.github != "" or person.website and person.website != "" %} · {% endif %}<a href="mailto:{{ person.email }}" title="Email">Email</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
{% endif %}

---

{% if site.data.people.visiting_students.size > 0 %}
## Visiting Graduate Students

<div class="team-grid">
{% for person in site.data.people.visiting_students %}
  <div class="team-card">
    {% if person.photo and person.photo != "" %}
      <img src="{{ '/assets/img/team/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="team-card__photo" loading="lazy">
    {% else %}
      <div class="team-card__photo team-card__photo--placeholder" aria-hidden="true">
        <span>{{ person.name | split: " " | map: "first" | join: "" | truncate: 2, "" | upcase }}</span>
      </div>
    {% endif %}
    <p class="team-card__name">{{ person.name }}</p>
    {% if person.institution and person.institution != "" %}
      <p class="team-card__role">{{ person.institution }}</p>
    {% endif %}
    {% if person.bio and person.bio != "" %}
      <p class="team-card__bio">{{ person.bio }}</p>
    {% endif %}
    <p class="team-card__links">
      {% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" title="Google Scholar" target="_blank" rel="noopener">Scholar</a>{% endif %}
      {% if person.github and person.github != "" %}{% if person.google_scholar and person.google_scholar != "" %} · {% endif %}<a href="{{ person.github }}" title="GitHub" target="_blank" rel="noopener">GitHub</a>{% endif %}
      {% if person.website and person.website != "" %}{% if person.google_scholar and person.google_scholar != "" or person.github and person.github != "" %} · {% endif %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
      {% if person.email and person.email != "" %}{% if person.google_scholar and person.google_scholar != "" or person.github and person.github != "" or person.website and person.website != "" %} · {% endif %}<a href="mailto:{{ person.email }}" title="Email">Email</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
{% endif %}

---

## Lab Team & Technical Staff

<div class="team-grid">
{% for person in site.data.people.staff %}
  <div class="team-card">
    {% if person.photo and person.photo != "" %}
      <img src="{{ '/assets/img/team/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="team-card__photo" loading="lazy">
    {% else %}
      <div class="team-card__photo team-card__photo--placeholder" aria-hidden="true">
        <span>{{ person.name | split: " " | map: "first" | join: "" | truncate: 2, "" | upcase }}</span>
      </div>
    {% endif %}
    <p class="team-card__name">{{ person.name }}</p>
    {% if person.role and person.role != "" %}
      <p class="team-card__role">{{ person.role }}</p>
    {% endif %}
    {% if person.bio and person.bio != "" %}
      <p class="team-card__bio">{{ person.bio }}</p>
    {% endif %}
    <p class="team-card__links">
      {% if person.github and person.github != "" %}<a href="{{ person.github }}" title="GitHub" target="_blank" rel="noopener">GitHub</a>{% endif %}
      {% if person.website and person.website != "" %}{% if person.github and person.github != "" %} · {% endif %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
      {% if person.email and person.email != "" %}{% if person.github and person.github != "" or person.website and person.website != "" %} · {% endif %}<a href="mailto:{{ person.email }}" title="Email">Email</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
- Nathan Castler
- Amanda Henderson

---

## Undergraduate Researchers

- Connor Wilson
- Cecina Babich Morrow
- Elisabeth Bergman (University of Arizona, honors project)
- Kenji Hayashi (Brown University, honors project)

---

<figure class="story-photo">
  <img src="{{ '/assets/img/team/lab_group_peru.jpeg' | relative_url }}" alt="Lab group at PFTC Peru — elevational gradient fieldwork" loading="lazy">
  <figcaption>PFTC 5 researchers on the elevational gradient, Peru</figcaption>
</figure>

## Extended Lab Network

Visitors, sabbatarians, and collaborators have included Alberto Burquez, Bente Graae, Deborah Goldberg, Jens-Christian Svenning, Yadvinder Malhi, Cory Merow, Henry Horn, Angelina Martinez-Yrizar, Ruben Milla, Choy Huang, Van Savage, Richard Strimbeck, and Vigdis Vandvik.

> Individual team member photos can be added to `assets/img/team/` — just drop headshots there and let us know to update the grid.


## Alumni

{% if site.data.people.alumni.size > 0 %}
<div class="team-grid team-grid--alumni">
{% for person in site.data.people.alumni %}
  <div class="team-card team-card--alumni">
    {% if person.photo and person.photo != "" %}
      <img src="{{ '/assets/img/team/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="team-card__photo" loading="lazy">
    {% else %}
      <div class="team-card__photo team-card__photo--placeholder" aria-hidden="true">
        <span>{{ person.name | split: " " | map: "first" | join: "" | truncate: 2, "" | upcase }}</span>
      </div>
    {% endif %}
    <p class="team-card__name">{{ person.name }}</p>
    <p class="team-card__role">
      {{ person.role }}{% if person.degree and person.degree != "" %} ({{ person.degree }}){% endif %}{% if person.institution and person.institution != "" %} · {{ person.institution }}{% elsif person.affiliation and person.affiliation != "" %} · {{ person.affiliation }}{% endif %}
    </p>
    <p class="team-card__links">
      {% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" title="Google Scholar" target="_blank" rel="noopener">Scholar</a>{% endif %}
      {% if person.website and person.website != "" %}{% if person.google_scholar and person.google_scholar != "" %} · {% endif %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
{% endif %}

Former postdocs also include Noah Charney, Margaret Evans, and many additional alumni now in academia, government, and non-profit science.

![Lab team portrait from collaborative field program]({{ '/assets/img/wordpress/picture-359196-1544529215.jpg' | relative_url }})

![Field team at Rocky Mountain Biological Laboratory transect site]({{ '/assets/img/wordpress/dsc_5672.jpg' | relative_url }})


