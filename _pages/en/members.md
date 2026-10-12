---
title: "People"
permalink: /en/members/
layout: single
author_profile: false
classes:
  - wide
  - members-page
lang: en
description: "BNU-SYS Lab members"
---

<style>
/* ===== Members page: single source of truth ===== */
.members-fw{
  --card-w: 132px;   /* was 150 -> further reduced */
  --photo-h: 176px;  /* was 200 -> further reduced */
  --gap-x: 40px;     /* increased horizontal spacing */
  --gap-y: 20px;     /* vertical spacing (adjust as needed) */

  max-width: 1240px;
  margin: 0 auto;
  padding: 0 8px;
}

/* headings (font size unchanged) */
.members-fw h2{
  margin: 10px 0 12px;
  padding-left: 10px;
  border-left: 4px solid #1f4e79;
  line-height: 1.25;
}

/* separator */
.members-fw .members-sep{
  border: 0;
  border-top: 1px solid #e5e7eb;
  margin: 20px 0;
}

/* shared grid rules */
.members-fw .faculty-grid,
.members-fw .member-grid,
.members-fw .master-grid{
  display: grid !important;
  column-gap: var(--gap-x) !important;
  row-gap: var(--gap-y) !important;
  justify-content: center !important;
  align-items: start !important;
  margin: 10px 0 18px;
}

/* faculty: 3 columns */
.members-fw .faculty-grid{
  grid-template-columns: repeat(3, var(--card-w)) !important;
}

/* PhD students: 4 columns */
.members-fw .member-grid{
  grid-template-columns: repeat(4, var(--card-w)) !important;
}

/* master's students: 4 columns */
.members-fw .master-grid{
  grid-template-columns: repeat(4, var(--card-w)) !important;
}

/* card */
.members-fw .faculty-card,
.members-fw .member-card{
  width: var(--card-w) !important;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  box-sizing: border-box;
}

/* photo container */
.members-fw .faculty-photo-shell,
.members-fw .member-photo-shell{
  position: relative !important;
  width: var(--card-w) !important;
  height: var(--photo-h) !important;
  padding: 0 !important;
  overflow: hidden !important;
  background: #efefef;
  border-bottom: 1px solid #e5e7eb;
  box-sizing: border-box;
}

/* fill container with image */
.members-fw .faculty-photo,
.members-fw .member-photo{
  position: absolute !important;
  inset: 0 !important;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center top !important;
  display: block !important;
  background: #e5e7eb;
}

/* name (font size unchanged) */
.members-fw .faculty-name,
.members-fw .member-name{
  text-align: center;
  font-size: 0.96rem;
  font-weight: 700;
  color: #374151;
  line-height: 1.35;
  padding: 8px 6px 10px;
  background: #f3f4f6;
  border-top: 1px solid #e5e7eb;
}

/* faculty extra info (font size unchanged) */
.members-fw .faculty-info{
  text-align: center;
  padding: 8px 8px 10px;
  background: #fff;
  min-height: 56px;
}
.members-fw .faculty-info p{ margin: 4px 0; }
.members-fw .faculty-info a{
  color: #1f4e79;
  text-decoration: none;
}
.members-fw .faculty-info a:hover{ text-decoration: underline; }

/* responsive */
@media (max-width: 1200px){
  .members-fw .faculty-grid{ grid-template-columns: repeat(2, var(--card-w)) !important; }
  .members-fw .member-grid{  grid-template-columns: repeat(3, var(--card-w)) !important; }
  .members-fw .master-grid{  grid-template-columns: repeat(4, var(--card-w)) !important; } /* keep 4 columns */
}
@media (max-width: 900px){
  .members-fw .faculty-grid{ grid-template-columns: repeat(2, var(--card-w)) !important; }
  .members-fw .member-grid{  grid-template-columns: repeat(2, var(--card-w)) !important; }
  .members-fw .master-grid{  grid-template-columns: repeat(2, var(--card-w)) !important; }
}
@media (max-width: 560px){
  .members-fw .faculty-grid,
  .members-fw .member-grid,
  .members-fw .master-grid{ grid-template-columns: 1fr !important; }

  .members-fw .faculty-card,
  .members-fw .member-card{
    width: var(--card-w) !important;
    margin: 0 auto;
  }
}
</style>




<div class="members-fw">

<h2 class="members-subtitle">Faculty</h2>

<div class="faculty-grid">
  <article class="faculty-card">
    <div class="faculty-photo-shell">
      <img class="faculty-photo"
           src="{{ '/images/members/ji-weixing.png' | relative_url }}"
           alt="Weixing Ji"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="faculty-name">Weixing Ji<br>(Professor)</div>
    <div class="faculty-info">
      <p><a href="https://ai.bnu.edu.cn/xygk/szdw/zgj/71b78ada5c214438ba5026d0ff6d61a3.htm" target="_blank" rel="noopener">Homepage</a></p>
    </div>
  </article>

  <article class="faculty-card">
    <div class="faculty-photo-shell">
      <img class="faculty-photo"
           src="{{ '/images/members/gao-jianhua.jpg' | relative_url }}"
           alt="Jianhua Gao"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="faculty-name">Jianhua Gao<br>(Lecturer)</div>
    <div class="faculty-info">
      <p><a href="https://ai.bnu.edu.cn/xygk/szdw/zj/8730b86554214b389bbedf5a5d137092.htm" target="_blank" rel="noopener">Homepage</a></p>
    </div>
  </article>

  <article class="faculty-card">
    <div class="faculty-photo-shell">
      <img class="faculty-photo"
           src="{{ '/images/members/shi-jianjun.jpg' | relative_url }}"
           alt="Jianjun Shi"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="faculty-name">Jianjun Shi<br>(Postdoc)</div>
    <div class="faculty-info"></div>
  </article>
</div>

<hr class="members-sep" />

<h2 class="members-subtitle">Ph.D. Students</h2>

<div class="member-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liubingxin.jpg' | relative_url }}" alt="Bingxin Liu"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Bingxin Liu<br>(2024)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ge-danying.jpg' | relative_url }}" alt="Danying Ge"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Danying Ge<br>(2025)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-pan.jpg' | relative_url }}" alt="Pan Liu"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Pan Liu<br>(2025)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-jingmin.jpg' | relative_url }}" alt="Jingmin Liu"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Jingmin Liu<br>(2025)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo member-photo-full" src="{{ '/images/members/bai-lu.jpg' | relative_url }}" alt="Lu Bai"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Lu Bai<br>(2026)</div>
  </div>
</div>

<hr class="members-sep" />

<h2 class="members-subtitle">Master's Students</h2>

<div class="master-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/huang-yinghui.jpg' | relative_url }}" alt="Yinghui Huang"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Yinghui Huang<br>(2024)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/wang-zeyin.jpg' | relative_url }}" alt="Zeyin Wang"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Zeyin Wang<br>(2024)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/xiao-meihao.jpg' | relative_url }}" alt="Meihao Xiao"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Meihao Xiao<br>(2024)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/jiang-qizhi.jpg' | relative_url }}" alt="Qizhi Jiang"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Qizhi Jiang<br>(2024)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/yang-yixue.jpg' | relative_url }}" alt="Yixue Yang"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Yixue Yang<br>(2025)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/hu-lu.jpg' | relative_url }}" alt="Lu Hu"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Lu Hu<br>(2025)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ma-wenbo.jpg' | relative_url }}" alt="Wenbo Ma"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Wenbo Ma<br>(2025)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ou-xueqian.jpg' | relative_url }}" alt="Xueqian Ou"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Xueqian Ou<br>(2025)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/guo-jianfeng.jpg' | relative_url }}" alt="Jianfeng Guo"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Jianfeng Guo<br>(2026)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/wang-xinyue.jpg' | relative_url }}" alt="Xinyue Wang"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Xinyue Wang<br>(2026)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/jia-renwu.jpg' | relative_url }}" alt="Renwu Jia"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Renwu Jia<br>(2026)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/fu-junlin.jpg' | relative_url }}" alt="Junlin Fu"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Junlin Fu<br>(2026)</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ma-yinglin.jpg' | relative_url }}" alt="Yinglin Ma"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Yinglin Ma<br>(2026)</div>
  </div>
</div>

<hr class="members-sep" />

<h2 class="members-subtitle">Graduates</h2>

<div class="master-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/zhang-yuxiang.jpg' | relative_url }}" alt="Yuxiang Zhang"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">Yuxiang Zhang<br>(2023)</div>
    <div class="faculty-info">
      <p>Employer: Ctrip · Software Engineer</p>
    </div>
  </div>
</div>

</div>
