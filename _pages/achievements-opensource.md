---
title: "开源项目"
permalink: /achievements/opensource/
layout: single
author_profile: false
classes: wide
description: "Star-Lab 开源项目成果。"
---

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
  <p>暂无开源项目条目。</p>
</div>
{% endif %}
