---
layout: page
title: team
permalink: /people/
description: Members and alumni of the Enquist Macroecology Lab
nav: false
nav_order: 2.1
---

<div class="people-page">

<!-- ============================================================
     PEOPLE PAGE
     Member data lives in _data/people.yml and is synced
     automatically from the lab's Google Sheet via the
     "Sync People Sheet" GitHub Actions workflow.

     To update your entry, use the Google Form linked in
     _data/people.yml (or the lab wiki).
     ============================================================ -->

<nav class="news-section-nav" aria-label="Page sections">
  <a href="#principal-investigator">Principal Investigator</a>
  <a href="#postdoctoral-researchers">Postdocs</a>
  <a href="#graduate-students">Graduate Students</a>
  <a href="#lab-team-technical-staff">Staff</a>
  <a href="#alumni">Alumni</a>
</nav>

<div class="photo-pair">
  <figure>
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-088.jpg' | relative_url }}" alt="Brian J. Enquist, February 2020" loading="lazy">
    <figcaption>Brian J. Enquist</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/wordpress/avery-ridge.jpg' | relative_url }}" alt="Avery Ridge landscape" loading="lazy">
    <figcaption>Avery Ridge</figcaption>
  </figure>
</div>

<a id="principal-investigator" tabindex="-1" aria-hidden="true"></a>

## Principal Investigator

<p><strong>Identity:</strong> Brian J. Enquist (ORCID: <a href="https://orcid.org/0000-0002-6124-7096" target="_blank" rel="noopener">0000-0002-6124-7096</a>) · Primary profile: <a href="{{ '/about/' | relative_url }}">About</a> · Google Scholar: <a href="https://scholar.google.com/citations?user=mAbA6EoAAAAJ&amp;hl=en" target="_blank" rel="noopener">mAbA6EoAAAAJ</a>.</p>

<div class="team-pi">
  <img src="{{ '/assets/img/team/brian_enquist.jpg' | relative_url }}" alt="Brian J. Enquist" class="team-pi__photo">
  <div class="team-pi__bio">
    <h3>Brian J. Enquist</h3>
    <p>Professor, Department of Ecology and Evolutionary Biology, University of Arizona; External Professor, Santa Fe Institute.</p>
    <p>
      <a href="https://scholar.google.com/citations?user=mAbA6EoAAAAJ&hl=en">Google Scholar</a> ·
      <a href="https://github.com/benquist">GitHub</a> ·
      <a href="https://github.com/EnquistLab">Lab GitHub</a> ·
      <a href="mailto:benquist@arizona.edu">benquist@arizona.edu</a>
    </p>
  </div>
</div>

{% if site.data.people.postdocs.size > 0 %}
<a id="postdoctoral-researchers" tabindex="-1" aria-hidden="true"></a>

## Postdoctoral Researchers

<div class="team-grid">
{% for person in site.data.people.postdocs %}
  <div class="team-card" role="group" aria-labelledby="postdoc-{{ forloop.index }}">
    {% if person.photo and person.photo != "" %}
      <img src="{{ '/assets/img/team/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="team-card__photo" loading="lazy">
    {% else %}
      <div class="team-card__photo team-card__photo--placeholder" aria-hidden="true">
        <span>{{ person.name | split: " " | map: "first" | join: "" | truncate: 2, "" | upcase }}</span>
      </div>
    {% endif %}
    <p class="team-card__name" id="postdoc-{{ forloop.index }}">{{ person.name }}</p>
    {% if person.affiliation and person.affiliation != "" %}
      <p class="team-card__role">{{ person.affiliation }}</p>
    {% endif %}
    {% if person.bio and person.bio != "" %}
      <p class="team-card__bio">{{ person.bio }}</p>
    {% endif %}
    <p class="team-card__links">
      {% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" title="Google Scholar" target="_blank" rel="noopener">Scholar</a>{% endif %}
      {% if person.researchgate and person.researchgate != "" %}<a href="{{ person.researchgate }}" title="ResearchGate" target="_blank" rel="noopener">ResearchGate</a>{% endif %}
      {% if person.github and person.github != "" %}<a href="{{ person.github }}" title="GitHub" target="_blank" rel="noopener">GitHub</a>{% endif %}
      {% if person.website and person.website != "" %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
      {% if person.email and person.email != "" %}<a href="mailto:{{ person.email }}" title="Email">Email</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
{% endif %}

---

{% if site.data.people.grad_students.size > 0 %}
<a id="graduate-students" tabindex="-1" aria-hidden="true"></a>

## Graduate Students

<div class="team-grid">
{% for person in site.data.people.grad_students %}
  <div class="team-card" role="group" aria-labelledby="grad-{{ forloop.index }}">
    {% if person.photo and person.photo != "" %}
      <img src="{{ '/assets/img/team/' | append: person.photo | relative_url }}" alt="{{ person.name }}" class="team-card__photo" loading="lazy">
    {% else %}
      <div class="team-card__photo team-card__photo--placeholder" aria-hidden="true">
        <span>{{ person.name | split: " " | map: "first" | join: "" | truncate: 2, "" | upcase }}</span>
      </div>
    {% endif %}
    <p class="team-card__name" id="grad-{{ forloop.index }}">{{ person.name }}</p>
    {% if person.degree and person.degree != "" %}
      <p class="team-card__role">{{ person.degree }} Student</p>
    {% endif %}
    {% if person.bio and person.bio != "" %}
      <p class="team-card__bio">{{ person.bio }}</p>
    {% endif %}
    <p class="team-card__links">
      {% if person.google_scholar and person.google_scholar != "" %}<a href="{{ person.google_scholar }}" title="Google Scholar" target="_blank" rel="noopener">Scholar</a>{% endif %}
      {% if person.researchgate and person.researchgate != "" %}<a href="{{ person.researchgate }}" title="ResearchGate" target="_blank" rel="noopener">ResearchGate</a>{% endif %}
      {% if person.github and person.github != "" %}<a href="{{ person.github }}" title="GitHub" target="_blank" rel="noopener">GitHub</a>{% endif %}
      {% if person.website and person.website != "" %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
      {% if person.email and person.email != "" %}<a href="mailto:{{ person.email }}" title="Email">Email</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
{% endif %}

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
      {% if person.researchgate and person.researchgate != "" %}<a href="{{ person.researchgate }}" title="ResearchGate" target="_blank" rel="noopener">ResearchGate</a>{% endif %}
      {% if person.github and person.github != "" %}<a href="{{ person.github }}" title="GitHub" target="_blank" rel="noopener">GitHub</a>{% endif %}
      {% if person.website and person.website != "" %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
      {% if person.email and person.email != "" %}<a href="mailto:{{ person.email }}" title="Email">Email</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
{% endif %}

<a id="lab-team-technical-staff" tabindex="-1" aria-hidden="true"></a>

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
      {% if person.website and person.website != "" %}<a href="{{ person.website }}" title="Website" target="_blank" rel="noopener">Web</a>{% endif %}
      {% if person.email and person.email != "" %}<a href="mailto:{{ person.email }}" title="Email">Email</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>

## Extended Lab Network

<aside class="network-aside">
  <div class="network-chips">
    <span class="network-chip">Alberto Burquez</span>
    <span class="network-chip">Bente Graae</span>
    <span class="network-chip">Deborah Goldberg</span>
    <span class="network-chip">Jens-Christian Svenning</span>
    <span class="network-chip">Yadvinder Malhi</span>
    <span class="network-chip">Cory Merow</span>
    <span class="network-chip">Henry Horn</span>
    <span class="network-chip">Angelina Martinez-Yrizar</span>
    <span class="network-chip">Ruben Milla</span>
    <span class="network-chip">Choy Huang</span>
    <span class="network-chip">Van Savage</span>
    <span class="network-chip">Richard Strimbeck</span>
    <span class="network-chip">Vigdis Vandvik</span>
  </div>
</aside>

<a id="alumni" tabindex="-1" aria-hidden="true"></a>

## Alumni

_Former Lab Graduate Students, Notable Undergraduates & Postdocs_

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

{% comment %}
Prefer Scholar links for alumni names, then fall back to ResearchGate,
LinkedIn, or website so non-Scholar profiles remain clickable.
{% endcomment %}

{% if postdoc_alumni.size > 0 %}

<section class="alumni-band">
  <div class="alumni-band__header">
    <h3>Former Postdoctoral Researchers <span class="alumni-count-badge">{{ postdoc_alumni.size }}</span></h3>
  </div>

{% if postdoc_2000s.size > 0 %}

  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2000s</p>
    <div class="alumni-directory">
      {% assign postdoc_2000s_sorted = postdoc_2000s | sort: "end_year" %}
      {% for person in postdoc_2000s_sorted %}
      {% assign alumni_photo = site.data.alumni_photos | where: "name", person.name | first %}
      <article class="alumni-card{% if alumni_photo %} alumni-card--has-photo{% endif %}">
        {% if alumni_photo %}<img src="{{ alumni_photo.url }}" alt="{{ person.name }}" class="alumni-card__avatar" loading="lazy" onerror="this.style.display='none';var c=this.closest('.alumni-card');if(c)c.classList.remove('alumni-card--has-photo')"><div class="alumni-card__body">{% endif %}
        {% assign alumni_profile_url = person.google_scholar | default: person.researchgate | default: person.linkedin | default: person.website %}
        <h4 class="alumni-card__name">{% if alumni_profile_url and alumni_profile_url != "" %}<a href="{{ alumni_profile_url }}" target="_blank" rel="noopener noreferrer">{{ person.name }}<span class="alumni-ext-link" aria-hidden="true"> ↗</span></a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
        {% if alumni_photo %}</div>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}

{% if postdoc_2010s.size > 0 %}

  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2010s</p>
    <div class="alumni-directory">
      {% assign postdoc_2010s_sorted = postdoc_2010s | sort: "end_year" %}
      {% for person in postdoc_2010s_sorted %}
      {% assign alumni_photo = site.data.alumni_photos | where: "name", person.name | first %}
      <article class="alumni-card{% if alumni_photo %} alumni-card--has-photo{% endif %}">
        {% if alumni_photo %}<img src="{{ alumni_photo.url }}" alt="{{ person.name }}" class="alumni-card__avatar" loading="lazy" onerror="this.style.display='none';var c=this.closest('.alumni-card');if(c)c.classList.remove('alumni-card--has-photo')"><div class="alumni-card__body">{% endif %}
        {% assign alumni_profile_url = person.google_scholar | default: person.researchgate | default: person.linkedin | default: person.website %}
        <h4 class="alumni-card__name">{% if alumni_profile_url and alumni_profile_url != "" %}<a href="{{ alumni_profile_url }}" target="_blank" rel="noopener noreferrer">{{ person.name }}<span class="alumni-ext-link" aria-hidden="true"> ↗</span></a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
        {% if alumni_photo %}</div>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}

{% if postdoc_2020s.size > 0 %}

  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2020s</p>
    <div class="alumni-directory">
      {% assign postdoc_2020s_sorted = postdoc_2020s | sort: "end_year" %}
      {% for person in postdoc_2020s_sorted %}
      {% assign alumni_photo = site.data.alumni_photos | where: "name", person.name | first %}
      <article class="alumni-card{% if alumni_photo %} alumni-card--has-photo{% endif %}">
        {% if alumni_photo %}<img src="{{ alumni_photo.url }}" alt="{{ person.name }}" class="alumni-card__avatar" loading="lazy" onerror="this.style.display='none';var c=this.closest('.alumni-card');if(c)c.classList.remove('alumni-card--has-photo')"><div class="alumni-card__body">{% endif %}
        {% assign alumni_profile_url = person.google_scholar | default: person.researchgate | default: person.linkedin | default: person.website %}
        <h4 class="alumni-card__name">{% if alumni_profile_url and alumni_profile_url != "" %}<a href="{{ alumni_profile_url }}" target="_blank" rel="noopener noreferrer">{{ person.name }}<span class="alumni-ext-link" aria-hidden="true"> ↗</span></a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
        {% if alumni_photo %}</div>{% endif %}
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
    <h3>Former Graduate Students <span class="alumni-count-badge">{{ grad_alumni.size }}</span></h3>
  </div>

{% if grad_2000s.size > 0 %}

  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2001–2009</p>
    <div class="alumni-directory">
      {% assign grad_2000s_sorted = grad_2000s | sort: "end_year" %}
      {% for person in grad_2000s_sorted %}
      {% assign alumni_photo = site.data.alumni_photos | where: "name", person.name | first %}
      <article class="alumni-card{% if alumni_photo %} alumni-card--has-photo{% endif %}">
        {% if alumni_photo %}<img src="{{ alumni_photo.url }}" alt="{{ person.name }}" class="alumni-card__avatar" loading="lazy" onerror="this.style.display='none';var c=this.closest('.alumni-card');if(c)c.classList.remove('alumni-card--has-photo')"><div class="alumni-card__body">{% endif %}
        {% assign alumni_profile_url = person.google_scholar | default: person.researchgate | default: person.linkedin | default: person.website %}
        <h4 class="alumni-card__name">{% if alumni_profile_url and alumni_profile_url != "" %}<a href="{{ alumni_profile_url }}" target="_blank" rel="noopener noreferrer">{{ person.name }}<span class="alumni-ext-link" aria-hidden="true"> ↗</span></a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
        {% if alumni_photo %}</div>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}

{% if grad_2010s.size > 0 %}

  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2010–2019</p>
    <div class="alumni-directory">
      {% assign grad_2010s_sorted = grad_2010s | sort: "end_year" %}
      {% for person in grad_2010s_sorted %}
      {% assign alumni_photo = site.data.alumni_photos | where: "name", person.name | first %}
      <article class="alumni-card{% if alumni_photo %} alumni-card--has-photo{% endif %}">
        {% if alumni_photo %}<img src="{{ alumni_photo.url }}" alt="{{ person.name }}" class="alumni-card__avatar" loading="lazy" onerror="this.style.display='none';var c=this.closest('.alumni-card');if(c)c.classList.remove('alumni-card--has-photo')"><div class="alumni-card__body">{% endif %}
        {% assign alumni_profile_url = person.google_scholar | default: person.researchgate | default: person.linkedin | default: person.website %}
        <h4 class="alumni-card__name">{% if alumni_profile_url and alumni_profile_url != "" %}<a href="{{ alumni_profile_url }}" target="_blank" rel="noopener noreferrer">{{ person.name }}<span class="alumni-ext-link" aria-hidden="true"> ↗</span></a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
        {% if alumni_photo %}</div>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endif %}

{% if grad_2020s.size > 0 %}

  <div class="alumni-cohort">
    <p class="alumni-cohort__label">2020s</p>
    <div class="alumni-directory">
      {% assign grad_2020s_sorted = grad_2020s | sort: "end_year" %}
      {% for person in grad_2020s_sorted %}
      {% assign alumni_photo = site.data.alumni_photos | where: "name", person.name | first %}
      <article class="alumni-card{% if alumni_photo %} alumni-card--has-photo{% endif %}">
        {% if alumni_photo %}<img src="{{ alumni_photo.url }}" alt="{{ person.name }}" class="alumni-card__avatar" loading="lazy" onerror="this.style.display='none';var c=this.closest('.alumni-card');if(c)c.classList.remove('alumni-card--has-photo')"><div class="alumni-card__body">{% endif %}
        {% assign alumni_profile_url = person.google_scholar | default: person.researchgate | default: person.linkedin | default: person.website %}
        <h4 class="alumni-card__name">{% if alumni_profile_url and alumni_profile_url != "" %}<a href="{{ alumni_profile_url }}" target="_blank" rel="noopener noreferrer">{{ person.name }}<span class="alumni-ext-link" aria-hidden="true"> ↗</span></a>{% else %}{{ person.name }}{% endif %}</h4>
        {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
        {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
        {% if alumni_photo %}</div>{% endif %}
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
    {% assign alumni_photo = site.data.alumni_photos | where: "name", person.name | first %}
    <article class="alumni-card{% if alumni_photo %} alumni-card--has-photo{% endif %}">
      {% if alumni_photo %}<img src="{{ alumni_photo.url }}" alt="{{ person.name }}" class="alumni-card__avatar" loading="lazy" onerror="this.style.display='none';var c=this.closest('.alumni-card');if(c)c.classList.remove('alumni-card--has-photo')"><div class="alumni-card__body">{% endif %}
      {% assign alumni_profile_url = person.google_scholar | default: person.researchgate | default: person.linkedin | default: person.website %}
      <h4 class="alumni-card__name">{% if alumni_profile_url and alumni_profile_url != "" %}<a href="{{ alumni_profile_url }}" target="_blank" rel="noopener noreferrer">{{ person.name }}<span class="alumni-ext-link" aria-hidden="true"> ↗</span></a>{% else %}{{ person.name }}{% endif %}</h4>
      {% if person.degree and person.degree != "" %}<p class="alumni-card__meta">{{ person.degree }}</p>{% endif %}
      {% if person.institution and person.institution != "" %}<p class="alumni-card__institution">{{ person.institution }}</p>{% endif %}
      {% if alumni_photo %}</div>{% endif %}
    </article>
    {% endfor %}
  </div>
</section>
{% endif %}

{% endif %}

<div class="lab-photo-gallery">
  <figure class="story-photo">
    <img src="{{ '/assets/img/wordpress/avery-ridge.jpg' | relative_url }}" alt="Avery Ridge landscape" loading="lazy">
    <figcaption>Avery Ridge</figcaption>
  </figure>
  <figure class="story-photo">
    <img src="{{ '/assets/img/wordpress/brian-enquist-feb2020-088.jpg' | relative_url }}" alt="Brian J. Enquist, February 2020" loading="lazy">
    <figcaption>Brian J. Enquist</figcaption>
  </figure>
  <figure class="story-photo">
    <img src="{{ '/assets/img/wordpress/picture-359196-1544529215.jpg' | relative_url }}" alt="Lab team portrait from collaborative field program" loading="lazy">
    <figcaption>Lab team portrait</figcaption>
  </figure>
  <figure class="story-photo">
    <img src="{{ '/assets/img/wordpress/dsc_5672.jpg' | relative_url }}" alt="Field team at Rocky Mountain Biological Laboratory transect site" loading="lazy">
    <figcaption>Field team at Rocky Mountain Biological Laboratory</figcaption>
  </figure>
</div>

</div>
