---
title: "BNU-SYS"
permalink: /en/
layout: single
author_profile: false
classes: wide news-page
lang: en
description: "BNU-SYS news: conferences/talks, latest papers, awards, team activities, group photos"
---

<div class="home-hero">
  <p class="home-hero__lead">
    BNU-SYS is part of the School of Artificial Intelligence at Beijing Normal University and is led by
    Professor Weixing Ji. Rooted in the core problems of computer systems, the group conducts systematic
    research along the chain of computer architecture—compiler optimization—parallel computing—large-model
    inference, covering the optimization of sparse-matrix computation and iterative solvers, compression and
    inference acceleration for large models, compiler optimization for domestic processors, and large-scale
    code defect detection.
  </p>
</div>

## Conferences / Talks {#conference-report}

{% assign conference_posts = site.posts | where: "lang", "en" | where_exp: "p", "p.categories contains 'conference-report'" %}
{% if conference_posts.size > 0 %}
<div class="news-grid">
  {% for post in conference_posts limit: 8 %}
  <article class="news-card{% if post.cover %} has-cover{% endif %}">
    {% if post.cover %}
    <a class="news-thumb" href="{{ post.url | relative_url }}">
      <img src="{{ post.cover | relative_url }}" alt="{{ post.title }}">
    </a>
    {% endif %}
    <div class="news-body">
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p class="news-meta">{{ post.date | date: "%Y-%m-%d" }}</p>
      {% if post.excerpt %}
      <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
      {% endif %}
    </div>
  </article>
  {% endfor %}
</div>
{% else %}
<p>No conference/talk news yet.</p>
{% endif %}

---

## Latest Papers {#latest-papers}

{% assign years_desc = site.data.achievements.years | sort: "year" | reverse %}
{% assign latest_papers = years_desc.first.papers %}
{% if latest_papers and latest_papers.size > 0 %}
<div class="latest-papers">
  {% for p in latest_papers limit: 5 %}
  <div class="latest-paper">
    <div class="latest-paper__title">{{ p.title }}</div>
    <div class="latest-paper__meta">{{ p.authors }} · {{ p.venue }}{% if p.ccf and p.ccf != 'None' %} · CCF {{ p.ccf }}{% endif %}</div>
    <div class="latest-paper__links">
      {% if p.pdf and p.pdf != '' %}<a href="{{ p.pdf }}" target="_blank" rel="noopener">[PDF]</a>{% endif %}
      {% if p.doi and p.doi != '' %}<a href="{{ p.doi }}" target="_blank" rel="noopener">[DOI]</a>{% endif %}
      {% if p.code and p.code != '' %}<a href="{{ p.code }}" target="_blank" rel="noopener">[Code]</a>{% endif %}
    </div>
  </div>
  {% endfor %}
</div>
{% else %}
<p>No papers yet.</p>
{% endif %}

---

## Awards {#competition-award}

{% assign award_posts = site.posts | where: "lang", "en" | where_exp: "p", "p.categories contains 'competition-award'" %}
{% if award_posts.size > 0 %}
<div class="news-grid">
  {% for post in award_posts limit: 8 %}
  <article class="news-card">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p class="news-meta">{{ post.date | date: "%Y-%m-%d" }}</p>
    {% if post.excerpt %}
    <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
    {% endif %}
  </article>
  {% endfor %}
</div>
{% else %}
<p>No award news yet.</p>
{% endif %}

---

## Team Activities {#team-building}

{% assign team_building_posts = site.posts | where: "lang", "en" | where_exp: "p", "p.categories contains 'team-building'" %}
{% if team_building_posts.size > 0 %}
<div class="news-grid">
  {% for post in team_building_posts limit: 8 %}
  <article class="news-card">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p class="news-meta">{{ post.date | date: "%Y-%m-%d" }}</p>
    {% if post.excerpt %}
    <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
    {% endif %}
  </article>
  {% endfor %}
</div>
{% else %}
<p>No team activity news yet.</p>
{% endif %}

---

## Group Photos {#gallery}

{% assign group_photos = site.static_files | where_exp: "f", "f.path contains '/images/group/'" | sort: "path" %}
{% if group_photos.size > 0 %}
<div class="group-marquee">
  <div class="group-marquee__track">
    {% for f in group_photos %}<img class="group-marquee__img" src="{{ f.path | relative_url }}" alt="BNU-SYS group photo">{% endfor %}
    {% for f in group_photos %}<img class="group-marquee__img" src="{{ f.path | relative_url }}" alt="" aria-hidden="true">{% endfor %}
  </div>
</div>
{% else %}
<p>No group photos yet.</p>
{% endif %}
