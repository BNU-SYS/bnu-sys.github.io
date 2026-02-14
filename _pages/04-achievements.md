---
# title: "成果展示"
permalink: /achievements/
layout: single
author_profile: false
classes: wide
description: "Star-Lab 团队成果：学术论文、开源项目、专利。"
---

<!-- =========================
     模块1：教师 -> 学术论文
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
      {% if p.pdf %}<a href="{{ p.pdf }}" target="_blank" rel="noopener">[PDF]</a>{% endif %}

    </div>
  </div>
</div>
{% endfor %}
{% endfor %}

<!-- =========================
     模块2：博士生 -> 开源项目
     ========================= -->
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
<div class="ach-block">
  <p>暂无开源项目。</p>
</div>
{% endif %}

<!-- =========================
     模块3：硕士生 -> 专利
     ========================= -->
<h2 class="ach-module-title">专利</h2>

{% if site.data.achievements.patents and site.data.achievements.patents.size > 0 %}
<div class="ach-block">
  <ul>
    {% for t in site.data.achievements.patents %}
    <li>
      <strong>{{ t.name }}</strong>
      {% if t.type %}（{{ t.type }}{% endif %}
      {% if t.year %}，{{ t.year }}{% endif %}
      {% if t.number %}，{{ t.number }}{% endif %}
      {% if t.type %}）{% endif %}
      {% if t.link %}<a href="{{ t.link }}" target="_blank" rel="noopener">[链接]</a>{% endif %}
    </li>
    {% endfor %}
  </ul>
</div>
{% else %}
<div class="ach-block">
  <p>暂无专利。</p>
</div>
{% endif %}
