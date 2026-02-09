---
title: "BNU-SYS"
permalink: /
layout: single
author_profile: false
classes: wide
description: "BNU-SYS，聚焦计算机体系结构、并行与高性能计算、代码分析与优化、大模型推理优化。"
---

<section class="star-hero">
  <!-- <p class="star-kicker">Beijing Normal University · School of Artificial Intelligence</p>
  <h1>BNU-SYS</h1> -->
  <!-- <p class="star-tagline">面向智能计算时代的系统底层研究</p> -->
  <p class="star-summary">
    BNU-SYS立足计算机系统核心问题，围绕计算机体系结构、并行计算与高性能计算、代码分析与编译优化、大模型推理加速等开展系统化研究，强调理论严谨、工程可复现与真实场景可落地。
  </p>

  <!-- <div class="star-quicklinks">
    <a class="star-btn" href="/members/">成员介绍</a>
    <a class="star-btn star-btn-secondary" href="/activities/">团建活动</a>
  </div> -->
</section>

---

## 研究方向

<div class="star-grid">
  <div class="star-card">
    <h3>计算机体系结构</h3>
    <p>面向高效智能计算的架构设计与优化，关注软硬结合、异构架构、领域加速等方向。</p>
  </div>
  <div class="star-card">
    <h3>并行与高性能计算</h3>
    <p>研究典型数值计算内核在国产CPU和XPU上的加速优化，典型科学计算与工程应用在大规模集群上的加速优化。</p>
  </div>
  <div class="star-card">
    <h3>代码分析与优化</h3>
    <p>面向大规模开源项目的高质量缺陷口构建，静态分析与机器学习相结合的缺陷检测和代码切片；面向国产计算平台的反馈编译优化（FDO/PGO)超优化技术（SuperOptimization）。</p>
  </div>
  <div class="star-card">
    <h3>大模型推理优化</h3>
    <p>面向LLM垂直领域应用，从领域知识高效利用、领域任务高效计算等方面开展研究，并重点关注教育领域的落地应用。</p>
  </div>
</div>

---

## 课题组合照

<div class="sg-carousel" id="groupCarousel">
  <div class="sg-viewport">
    <img class="sg-image is-active"
         src="{{ '/images/group/group-01.jpg' | relative_url }}">

    <img class="sg-image"
         src="{{ '/images/group/group-03.jpg' | relative_url }}">

    <img class="sg-image"
         src="{{ '/images/group/group-04.jpg' | relative_url }}">
  </div>

  <!-- 按钮一定要在 sg-carousel 内部 -->
  <button class="sg-btn sg-prev" type="button" aria-label="上一张">‹</button>
  <button class="sg-btn sg-next" type="button" aria-label="下一张">›</button>
</div>

<p class="sg-caption" id="groupCaption">Star-Lab 团队合影 </p>

<script>
(function () {
  const root = document.getElementById('groupCarousel');
  if (!root) return;

  const images = Array.from(root.querySelectorAll('.sg-image'));
  const prevBtn = root.querySelector('.sg-prev');
  const nextBtn = root.querySelector('.sg-next');
  const caption = document.getElementById('groupCaption');
  let idx = images.findIndex(img => img.classList.contains('is-active'));
  if (idx < 0) idx = 0;

  function render() {
    images.forEach((img, i) => img.classList.toggle('is-active', i === idx));
    caption.textContent = images[idx].dataset.caption || images[idx].alt || '';
  }

  prevBtn.addEventListener('click', () => {
    idx = (idx - 1 + images.length) % images.length;
    render();
  });

  nextBtn.addEventListener('click', () => {
    idx = (idx + 1) % images.length;
    render();
  });

  render();
})();
</script>

