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
    BNU-SYS 立足计算机系统核心问题，围绕“体系结构—编译优化—并行计算—大模型推理”开展系统化研究，
    强调理论严谨、工程可复现与真实场景可落地。
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
    <p>面向高效智能计算的架构设计与优化，关注存储层次、执行效率与系统吞吐。</p>
  </div>
  <div class="star-card">
    <h3>并行与高性能计算</h3>
    <p>研究并行算法与系统协同优化，提升多核、多GPU及异构平台上的计算性能。</p>
  </div>
  <div class="star-card">
    <h3>代码分析与优化</h3>
    <p>围绕编译分析、程序表示与优化策略，提升程序执行效率与可维护性。</p>
  </div>
  <div class="star-card">
    <h3>大模型推理优化</h3>
    <p>聚焦推理链路中的延迟、吞吐与资源效率，探索系统层可部署优化方法。</p>
  </div>
</div>

---

## 课题组合照

<div class="star-gallery" id="starGallery">
  <button class="sg-btn sg-prev" type="button" aria-label="上一张">‹</button>

  <div class="sg-viewport">
    <img class="sg-image is-active"
         src="{{ '/images/group/group-01.jpg' | relative_url }}"
         alt="Star-Lab 合照 1：团队合影">
    <img class="sg-image"
         src="{{ '/images/group/group-02.jpg' | relative_url }}"
         alt="Star-Lab 合照 2：学术交流">
    <img class="sg-image"
         src="{{ '/images/group/group-03.jpg' | relative_url }}"
         alt="Star-Lab 合照 3：团建活动">
     <img class="sg-image is-active"
         src="{{ '/images/group/group-04.jpg' | relative_url }}"
         alt="Star-Lab 合照 1：团队合影">
  </div>

  <button class="sg-btn sg-next" type="button" aria-label="下一张">›</button>
</div>

<div class="sg-caption" id="sgCaption">Star-Lab 团队合影（2026年）</div>

<div class="sg-dots" id="sgDots" aria-label="图片索引"></div>

<script>
(function () {
  var gallery = document.getElementById('starGallery');
  if (!gallery) return;

  var imgs = Array.prototype.slice.call(gallery.querySelectorAll('.sg-image'));
  var prev = gallery.querySelector('.sg-prev');
  var next = gallery.querySelector('.sg-next');
  var caption = document.getElementById('sgCaption');
  var dotsWrap = document.getElementById('sgDots');
  var idx = 0;

  function renderDots() {
    dotsWrap.innerHTML = '';
    imgs.forEach(function (_, i) {
      var b = document.createElement('button');
      b.className = 'sg-dot' + (i === idx ? ' is-active' : '');
      b.type = 'button';
      b.setAttribute('aria-label', '第' + (i + 1) + '张');
      b.addEventListener('click', function () {
        idx = i;
        render();
      });
      dotsWrap.appendChild(b);
    });
  }

  function render() {
    imgs.forEach(function (im, i) {
      im.classList.toggle('is-active', i === idx);
    });
    var cap = imgs[idx].getAttribute('data-caption') || '';
    caption.textContent = cap;
    renderDots();
  }

  function showNext() {
    idx = (idx + 1) % imgs.length;
    render();
  }

  function showPrev() {
    idx = (idx - 1 + imgs.length) % imgs.length;
    render();
  }

  next.addEventListener('click', showNext);
  prev.addEventListener('click', showPrev);

  // 键盘支持
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight') showNext();
    if (e.key === 'ArrowLeft') showPrev();
  });

  render();
})();
</script>