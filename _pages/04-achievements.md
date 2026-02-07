---
title: "团队成果"
permalink: /achievements/
layout: single
author_profile: false
classes: wide
description: "Star-Lab 团队成果：论文、专利与软件系统。"
---

<section class="results-hero">
  <h1>团队成果</h1>
  <p>围绕计算机体系结构、并行与高性能计算、代码分析与优化、大模型推理优化等方向，持续产出高质量成果。</p>
</section>

{% assign paper_count = site.data.achievements.papers | size %}
{% assign patent_count = site.data.achievements.patents | size %}
{% assign software_count = site.data.achievements.software | size %}

<div class="results-metrics">
  <div class="metric-card">
    <div class="metric-value">{{ paper_count }}</div>
    <div class="metric-label">论文</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">{{ patent_count }}</div>
    <div class="metric-label">专利</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">{{ software_count }}</div>
    <div class="metric-label">软件</div>
  </div>
</div>

---

## 论文（Papers）

{% assign papers_sorted = site.data.achievements.papers | sort: "year" | reverse %}
{% for p in papers_sorted %}
<div class="result-item">
  <div class="result-year">{{ p.year }}</div>
  <div class="result-body">
    <h3>{{ p.title }}</h3>
    <p class="meta">
      <strong>{{ p.venue }}</strong> · {{ p.type }}<br/>
      {{ p.authors }}
    </p>
    <p class="links">
      {% if p.links.paper %}<a href="{{ p.links.paper }}" target="_blank" rel="noopener">Paper</a>{% endif %}
      {% if p.links.code %} · <a href="{{ p.links.code }}" target="_blank" rel="noopener">Code</a>{% endif %}
    </p>
  </div>
</div>
{% endfor %}

---

## 专利（Patents）

{% assign patents_sorted = site.data.achievements.patents | sort: "year" | reverse %}
{% for t in patents_sorted %}
<div class="result-item">
  <div class="result-year">{{ t.year }}</div>
  <div class="result-body">
    <h3>{{ t.title }}</h3>
    <p class="meta">
      专利号：{{ t.number }}<br/>
      状态：{{ t.status }}<br/>
      发明人：{{ t.inventors }}
    </p>
    {% if t.links.doc %}
    <p class="links"><a href="{{ t.links.doc }}" target="_blank" rel="noopener">专利文档</a></p>
    {% endif %}
  </div>
</div>
{% endfor %}

---

## 软件（Software）

{% assign software_sorted = site.data.achievements.software | sort: "year" | reverse %}
{% for s in software_sorted %}
<div class="result-item">
  <div class="result-year">{{ s.year }}</div>
  <div class="result-body">
    <h3>{{ s.name }}</h3>
    <p class="meta">
      类型：{{ s.category }}<br/>
      版本：{{ s.version }}<br/>
      {{ s.description }}
    </p>
    <p class="links">
      {% if s.links.repo %}<a href="{{ s.links.repo }}" target="_blank" rel="noopener">Repository</a>{% endif %}
      {% if s.links.demo %} · <a href="{{ s.links.demo }}" target="_blank" rel="noopener">Demo</a>{% endif %}
    </p>
  </div>
</div>
{% endfor %}
