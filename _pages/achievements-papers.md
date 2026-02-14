---
title: "学术论文"
permalink: /achievements/papers/
layout: single
author_profile: false
classes: wide
description: "Star-Lab 学术论文成果。"
---

{% for y in site.data.achievements.years %}
<h2 class="ach-year">{{ y.year }}</h2>

{% for p in y.papers %}
<div class="ach-item">
  <div class="ach-thumb-wrap">
    <img
      class="ach-thumb"
      src="{{ p.thumb | default: '/images/papers/default.png' | relative_url }}"
      alt="{{ p.title | escape }}"
      loading="lazy"
    >
  </div>

  <div class="ach-main">
    <div class="ach-line"><strong>作者:</strong> {{ p.authors }}</div>
    <div class="ach-line"><strong>论文:</strong> {{ p.title }}</div>
    <div class="ach-line"><strong>期刊或会议:</strong> {{ p.venue }}</div>
    {% if p.ccf %}<div class="ach-line"><strong>CCF等级:</strong> {{ p.ccf }}</div>{% endif %}

    <div class="ach-links">
      {% if p.pdf %}<a href="{{ p.pdf }}" target="_blank" rel="noopener">[PDF]</a>{% endif %}
      {% if p.slides %}<a href="{{ p.slides }}" target="_blank" rel="noopener">[Slides]</a>{% endif %}
      {% if p.doi %}<a href="{{ p.doi }}" target="_blank" rel="noopener">[DOI]</a>{% endif %}
      {% if p.bib %}<a href="{{ p.bib }}" target="_blank" rel="noopener">[BibTeX]</a>{% endif %}
      {% if p.code %}<a href="{{ p.code }}" target="_blank" rel="noopener">[Code]</a>{% endif %}
    </div>
  </div>
</div>
{% endfor %}
{% endfor %}
