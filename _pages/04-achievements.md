---
title: "团队成果"
permalink: /achievements/
layout: single
author_profile: false
classes: wide
description: "Star-Lab 团队成果：论文、专利与软件。"
---

{% for y in site.data.achievements.years %}
<h3 class="members-subtitle ach-year">{{ y.year }}</h3>

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
    <!-- <div class="ach-line"><strong>Year:</strong> {{ p.year }}</div> -->

    <div class="ach-links">
      {% if p.pdf %}<a href="{{ p.pdf }}" target="_blank" rel="noopener">[PDF]</a>{% endif %}
    </div>
  </div>
</div>
{% endfor %}
{% endfor %}

{% if site.data.achievements.patents and site.data.achievements.patents.size > 0 %}
<h2 class="ach-module-title">专利</h2>
<div class="ach-block">
  <ul>
    {% for t in site.data.achievements.patents %}
    <li>
      <strong>{{ t.name }}</strong>（{{ t.type }}，{{ t.year }}，{{ t.number }}）
      {% if t.link %}<a href="{{ t.link }}" target="_blank" rel="noopener">[链接]</a>{% endif %}
    </li>
    {% endfor %}
  </ul>
</div>
{% endif %}

{% if site.data.achievements.software and site.data.achievements.software.size > 0 %}
<h2 class="ach-module-title">软件</h2>
<div class="ach-block">
  <ul>
    {% for s in site.data.achievements.software %}
    <li>
      <strong>{{ s.name }}</strong>（{{ s.year }}，登记号：{{ s.reg_no }}）
      {% if s.link %}<a href="{{ s.link }}" target="_blank" rel="noopener">[链接]</a>{% endif %}
    </li>
    {% endfor %}
  </ul>
</div>
{% endif %}
