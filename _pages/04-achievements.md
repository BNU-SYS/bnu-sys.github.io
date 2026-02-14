---
title: "成果展示"
permalink: /achievements/
layout: single
author_profile: false
classes: wide
description: "Star-Lab 团队成果：学术论文与开源项目。"
---

<h2 class="ach-module-title">学术论文</h2>

{% if site.data.achievements.years and site.data.achievements.years.size > 0 %}
  {% for y in site.data.achievements.years %}
  <h2 class="ach-year">{{ y.year }}</h2>

  {% if y.papers and y.papers.size > 0 %}
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
        <div class="ach-line"><strong>期刊/会议:</strong> {{ p.venue }}</div>
        {% if p.ccf %}<div class="ach-line"><strong>CCF等级:</strong> {{ p.ccf }}</div>{% endif %}

        <div class="ach-links">
          {% if p.pdf %}<a href="{{ p.pdf }}" target="_blank" rel="noopener">[PDF]</a>{% endif %}
          {% if p.doi %}<a href="{{ p.doi }}" target="_blank" rel="noopener">[DOI]</a>{% endif %}
          {% if p.code %}<a href="{{ p.code }}" target="_blank" rel="noopener">[Code]</a>{% endif %}
          {% if p.bib %}<a href="{{ p.bib }}" target="_blank" rel="noopener">[BibTeX]</a>{% endif %}
        </div>
      </div>
    </div>
    {% endfor %}
  {% else %}
    <div class="ach-block"><p>该年份暂无论文条目。</p></div>
  {% endif %}
  {% endfor %}
{% else %}
  <div class="ach-block"><p>暂无论文数据。</p></div>
{% endif %}

<h2 class="ach-module-title">开源项目</h2>

{% if site.data.achievements.opensource and site.data.achievements.opensource.size > 0 %}
<div class="ach-block">
  <ul>
    {% for o in site.data.achievements.opensource %}
    <li>
      <strong>{{ o.name }}</strong>
      {% if o.desc %}：{{ o.desc }}{% endif %}
      {% if o.year %}（{{ o.year }}）{% endif %}
      {% if o.stars %}（⭐ {{ o.stars }}）{% endif %}
      {% if o.link %}<a href="{{ o.link }}" target="_blank" rel="noopener">[仓库]</a>{% endif %}
      {% if o.doc %}<a href="{{ o.doc }}" target="_blank" rel="noopener">[文档]</a>{% endif %}
      {% if o.demo %}<a href="{{ o.demo }}" target="_blank" rel="noopener">[Demo]</a>{% endif %}
    </li>
    {% endfor %}
  </ul>
</div>
{% else %}
<div class="ach-block"><p>暂无开源项目数据。</p></div>
{% endif %}
