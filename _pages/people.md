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

---

<figure class="story-photo">
  <img src="{{ '/assets/img/team/lab_group_peru.jpeg' | relative_url }}" alt="Lab group at PFTC Peru — elevational gradient fieldwork" loading="lazy">
  <figcaption>PFTC 5 researchers on the elevational gradient, Peru</figcaption>
</figure>

## Extended Lab Network

Visitors, sabbatarians, and collaborators have included Alberto Burquez, Bente Graae, Deborah Goldberg, Jens-Christian Svenning, Yadvinder Malhi, Cory Merow, Henry Horn, Angelina Martinez-Yrizar, Ruben Milla, Choy Huang, Van Savage, Richard Strimbeck, and Vigdis Vandvik.

---

## Alumni

*Former Lab Graduate Students, Notable Undergraduates & Postdocs*

{% if site.data.people.alumni.size > 0 %}

{% assign alumni = site.data.people.alumni %}
{% assign postdoc_alumni = alumni | where_exp: "p", "p.degree contains 'Postdoc'" %}
{% assign grad_alumni = alumni | where_exp: "p", "p.degree contains 'PhD' or p.degree contains 'Masters'" %}
{% assign undergrad_alumni = alumni | where_exp: "p", "p.degree contains 'Notable Undergraduate'" %}

{% assign postdoc_2000s = postdoc_alumni | where_exp: "p", "p.start_year >= 2000 and p.start_year <= 2009" %}
{% assign postdoc_2010s = postdoc_alumni | where_exp: "p", "p.start_year >= 2010 and p.start_year <= 2019" %}
{% assign postdoc_2020s = postdoc_alumni | where_exp: "p", "p.start_year >= 2020" %}

{% assign grad_2000s = grad_alumni | where_exp: "p", "p.start_year >= 2001 and p.start_year <= 2009" %}
{% assign grad_2010s = grad_alumni | where_exp: "p", "p.start_year >= 2010 and p.start_year <= 2019" %}
{% assign grad_2020s = grad_alumni | where_exp: "p", "p.start_year >= 2020" %}

{% if postdoc_alumni.size > 0 %}
<section class="alumni-band">
  <div class="alumni-band__header">
    <h3>Former Postdoctoral Researchers</h3>
    <p>{{ postdoc_alumni.size }} researchers whose work shaped the lab's theory, synthesis, and field programs.</p>
  </div>

  {% if postdoc_2000s.size > 0 %}
  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2000s</p>
    <div class="alumni-directory">
      {% for person in postdoc_2000s %}
      <article class="alumni-card">
        <h4 class="alumni-card__name">{% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" target="_blank" rel="noopener noreferrer">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</h4>
        <p class="alumni-card__meta">{{ person.degree }}</p>
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if postdoc_2010s.size > 0 %}
  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2010s</p>
    <div class="alumni-directory">
      {% for person in postdoc_2010s %}
      <article class="alumni-card">
        <h4 class="alumni-card__name">{% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" target="_blank" rel="noopener noreferrer">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</h4>
        <p class="alumni-card__meta">{{ person.degree }}</p>
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if postdoc_2020s.size > 0 %}
  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2020s</p>
    <div class="alumni-directory">
      {% for person in postdoc_2020s %}
      <article class="alumni-card">
        <h4 class="alumni-card__name">{% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" target="_blank" rel="noopener noreferrer">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</h4>
        <p class="alumni-card__meta">{{ person.degree }}</p>
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}
</section>
{% endif %}

{% if grad_alumni.size > 0 %}
<section class="alumni-band">
  <div class="alumni-band__header">
    <h3>Graduate Alumni</h3>
    <p>{{ grad_alumni.size }} doctoral, master's, and thesis-track alumni organized by training era.</p>
  </div>

  {% if grad_2000s.size > 0 %}
  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2001–2009</p>
    <div class="alumni-directory">
      {% for person in grad_2000s %}
      <article class="alumni-card">
        <h4 class="alumni-card__name">{% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" target="_blank" rel="noopener noreferrer">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if grad_2010s.size > 0 %}
  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2010–2019</p>
    <div class="alumni-directory">
      {% for person in grad_2010s %}
      <article class="alumni-card">
        <h4 class="alumni-card__name">{% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" target="_blank" rel="noopener noreferrer">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if grad_2020s.size > 0 %}
  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2020s</p>
    <div class="alumni-directory">
      {% for person in grad_2020s %}
      <article class="alumni-card">
        <h4 class="alumni-card__name">{% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" target="_blank" rel="noopener noreferrer">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}
</section>
{% endif %}

{% if undergrad_alumni.size > 0 %}
<section class="alumni-band">
  <div class="alumni-band__header">
    <h3>Notable Undergraduate Researchers</h3>
    <p>Early-career researchers who contributed important work during undergraduate training.</p>
  </div>
  <div class="alumni-directory alumni-directory--compact">
    {% for person in undergrad_alumni %}
    <article class="alumni-card">
      <h4 class="alumni-card__name">{% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" target="_blank" rel="noopener noreferrer">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</h4>
      {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
      {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
    </article>
    {% endfor %}
  </div>
</section>
{% endif %}

{% endif %}

![Lab team portrait from collaborative field program]({{ '/assets/img/wordpress/picture-359196-1544529215.jpg' | relative_url }})

![Field team at Rocky Mountain Biological Laboratory transect site]({{ '/assets/img/wordpress/dsc_5672.jpg' | relative_url }})


