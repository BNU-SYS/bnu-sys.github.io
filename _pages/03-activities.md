---
title: "BNU-SYS"
permalink: /
layout: single
author_profile: false
classes: wide news-page
lang: zh
description: "BNU-SYS 团队新闻：学术会议/报告、最新论文、竞赛获奖、团建活动、课题组合影"
---

<div class="home-hero">
  <p class="home-hero__lead">
    BNU-SYS 隶属北京师范大学人工智能学院，课题负责人为计卫星教授。课题组立足计算机系统核心问题，
    围绕“体系结构—编译优化—并行计算—大模型推理”开展系统化研究，研究内容涵盖稀疏矩阵计算与迭代求解算法优化、
    大模型压缩与推理加速、面向国产处理器的编译优化，以及大规模代码缺陷检测。
  </p>
</div>

## 学术会议 / 报告 {#conference-report}

{% assign conference_posts = site.posts | where: "lang", "zh" | where_exp: "p", "p.categories contains 'conference-report'" %}
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
<p>暂无学术会议/报告新闻。</p>
{% endif %}

---

## 最新论文 {#latest-papers}

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
<p>暂无论文。</p>
{% endif %}

---

## 竞赛获奖 {#competition-award}

{% assign award_posts = site.posts | where: "lang", "zh" | where_exp: "p", "p.categories contains 'competition-award'" %}
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
<p>暂无竞赛获奖新闻。</p>
{% endif %}

---

## 团建活动 {#team-building}

{% assign team_building_posts = site.posts | where: "lang", "zh" | where_exp: "p", "p.categories contains 'team-building'" %}
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
<p>暂无团建活动新闻。</p>
{% endif %}

---

## 课题组合影 {#gallery}

{% assign group_photos = site.static_files | where_exp: "f", "f.path contains '/images/group/'" | sort: "path" %}
{% if group_photos.size > 0 %}
<div class="group-marquee">
  <div class="group-marquee__track">
    {% for f in group_photos %}<img class="group-marquee__img" src="{{ f.path | relative_url }}" alt="BNU-SYS 课题组合影">{% endfor %}
    {% for f in group_photos %}<img class="group-marquee__img" src="{{ f.path | relative_url }}" alt="" aria-hidden="true">{% endfor %}
  </div>
</div>
{% else %}
<p>暂无合影。</p>
{% endif %}
