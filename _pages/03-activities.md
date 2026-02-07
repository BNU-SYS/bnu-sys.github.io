---
title: "团队新闻"
permalink: /news/
layout: single
author_profile: false
classes: wide news-page
description: "Star-Lab 团队新闻：团建活动、学术会议/报告、竞赛获奖"
---

<div class="news-index-nav">
  <a href="#team-building">团建活动</a>
  <a href="#conference-report">学术会议 / 报告</a>
  <a href="#competition-award">竞赛获奖</a>
</div>

## 团建活动 {#team-building}

{% assign team_building_posts = site.posts | where_exp: "p", "p.categories contains 'team-building'" %}
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

## 学术会议 / 报告 {#conference-report}

{% assign conference_posts = site.posts | where_exp: "p", "p.categories contains 'conference-report'" %}
{% if conference_posts.size > 0 %}
<div class="news-grid">
  {% for post in conference_posts limit: 8 %}
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
<p>暂无学术会议/报告新闻。</p>
{% endif %}

---

## 竞赛获奖 {#competition-award}

{% assign award_posts = site.posts | where_exp: "p", "p.categories contains 'competition-award'" %}
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
