---
title: "论文成果"
permalink: /achievements/
layout: single
author_profile: false
classes: wide
description: "BNU-SYS 团队成果：学术论文、专利。"
---

<!-- =========================
     模块1：学术论文
     ========================= -->
<h2 class="ach-module-title">学术论文</h2>

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
      {% if p.pdf and p.pdf != '' %}<a href="{{ p.pdf }}" target="_blank" rel="noopener">[PDF]</a>{% else %}<span class="ach-link-off">[PDF]</span>{% endif %}
      {% if p.slides and p.slides != '' %}<a href="{{ p.slides }}" target="_blank" rel="noopener">[Slides]</a>{% else %}<span class="ach-link-off">[Slides]</span>{% endif %}
      {% if p.doi and p.doi != '' %}<a href="{{ p.doi }}" target="_blank" rel="noopener">[DOI]</a>{% else %}<span class="ach-link-off">[DOI]</span>{% endif %}
      {% if p.bibtex and p.bibtex != '' %}<a href="{{ p.bibtex }}" target="_blank" rel="noopener">[Bibtex]</a>{% else %}<span class="ach-link-off">[Bibtex]</span>{% endif %}
      {% if p.code and p.code != '' %}<a href="{{ p.code }}" target="_blank" rel="noopener">[Code]</a>{% else %}<span class="ach-link-off">[Code]</span>{% endif %}
    </div>
  </div>
</div>
{% endfor %}
{% endfor %}

<!-- =========================
     模块2：专利
     ========================= -->
<h2 class="ach-module-title">专利</h2>

{% if site.data.achievements.patents and site.data.achievements.patents.size > 0 %}
<div class="ach-block">
  {% for t in site.data.achievements.patents %}
  <div class="ach-patent">
    <div class="ach-line"><strong>发明人:</strong> {{ t.inventors }}</div>
    <div class="ach-line"><strong>专利:</strong> {{ t.title }}</div>
    <div class="ach-line"><strong>专利号:</strong> {{ t.number }}{% if t.pub_no %}（公开号：{{ t.pub_no }}）{% endif %}</div>
    {% if t.status %}<div class="ach-line"><strong>状态:</strong> {{ t.status }}{% if t.grant_date %}，{{ t.grant_date }}{% endif %}</div>{% endif %}

    <div class="ach-links">
      {% if t.html and t.html != '' %}<a href="{{ t.html }}" target="_blank" rel="noopener">[HTML]</a>{% else %}<span class="ach-link-off">[HTML]</span>{% endif %}
    </div>
  </div>
  {% endfor %}
</div>
{% else %}
<div class="ach-block">
  <p>暂无专利。</p>
</div>
{% endif %}
