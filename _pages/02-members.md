---
title: "成员介绍"
permalink: /members/
layout: single
author_profile: false
classes:
  - wide
  - members-page
description: "Star-Lab 课题组成员"
---

<style>
/* ===== Members page: single source of truth ===== */
.members-fw{
  --card-w: 132px;   /* 原 150 -> 进一步缩小 */
  --photo-h: 176px;  /* 原 200 -> 进一步缩小 */
  --gap-x: 30px;     /* 横向间距增大 */
  --gap-y: 20px;     /* 纵向间距（可按需调） */

  max-width: 1240px;
  margin: 0 auto;
  padding: 0 8px;
}

/* 标题（不改字体大小） */
.members-fw h2{
  margin: 10px 0 12px;
  padding-left: 10px;
  border-left: 4px solid #1f4e79;
  line-height: 1.25;
}

/* 分隔线 */
.members-fw .members-sep{
  border: 0;
  border-top: 1px solid #e5e7eb;
  margin: 20px 0;
}

/* 网格通用 */
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

/* 教师 3 列 */
.members-fw .faculty-grid{
  grid-template-columns: repeat(3, var(--card-w)) !important;
}

/* 博士生 4 列 */
.members-fw .member-grid{
  grid-template-columns: repeat(4, var(--card-w)) !important;
}

/* 硕士生 4 列（按你的新要求） */
.members-fw .master-grid{
  grid-template-columns: repeat(4, var(--card-w)) !important;
}

/* 卡片 */
.members-fw .faculty-card,
.members-fw .member-card{
  width: var(--card-w) !important;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  box-sizing: border-box;
}

/* 照片容器 */
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

/* 图片填满容器 */
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

/* 名字（不改字体大小） */
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

/* 教师附加信息（不改字体大小） */
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

/* 响应式 */
@media (max-width: 1200px){
  .members-fw .faculty-grid{ grid-template-columns: repeat(2, var(--card-w)) !important; }
  .members-fw .member-grid{  grid-template-columns: repeat(3, var(--card-w)) !important; }
  .members-fw .master-grid{  grid-template-columns: repeat(4, var(--card-w)) !important; } /* 保持4列 */
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

<h2 class="members-subtitle">教师</h2>

<div class="faculty-grid">
  <article class="faculty-card">
    <div class="faculty-photo-shell">
      <img class="faculty-photo"
           src="{{ '/images/members/ji-weixing.png' | relative_url }}"
           alt="计卫星"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="faculty-name">计卫星<br>（教授）</div>
    <div class="faculty-info">
      <p><a href="https://ai.bnu.edu.cn/xygk/szdw/zgj/71b78ada5c214438ba5026d0ff6d61a3.htm" target="_blank" rel="noopener">个人主页</a></p>
    </div>
  </article>

  <article class="faculty-card">
    <div class="faculty-photo-shell">
      <img class="faculty-photo"
           src="{{ '/images/members/gao-jianhua.jpg' | relative_url }}"
           alt="高建花"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="faculty-name">高建花<br>（讲师）</div>
    <div class="faculty-info">
      <p><a href="https://ai.bnu.edu.cn/xygk/szdw/zj/8730b86554214b389bbedf5a5d137092.htm" target="_blank" rel="noopener">个人主页</a></p>
    </div>
  </article>

  <article class="faculty-card">
    <div class="faculty-photo-shell">
      <img class="faculty-photo"
           src="{{ '/images/members/shi-jianjun.jpg' | relative_url }}"
           alt="石剑君"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="faculty-name">石剑君<br>（博士后）</div>
    <div class="faculty-info"></div>
  </article>
</div>

<hr class="members-sep" />

<h2 class="members-subtitle">博士生</h2>

<div class="member-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-bingxin.jpg' | relative_url }}" alt="刘秉鑫"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘秉鑫<br>（2024级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ge-danying.jpg' | relative_url }}" alt="葛丹颖"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">葛丹颖<br>（2025级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-pan.jpg' | relative_url }}" alt="刘攀"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘攀<br>（2025级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-jingmin.jpg' | relative_url }}" alt="刘敬民"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘敬民<br>（2025级）</div>
  </div>
</div>

<hr class="members-sep" />

<h2 class="members-subtitle">硕士生</h2>

<div class="master-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/zhang-yuxiang.jpg' | relative_url }}" alt="张寓祥"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">张寓祥<br>（2023级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/huang-yinghui.jpg' | relative_url }}" alt="黄颖晖"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">黄颖晖<br>（2024级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/wang-zeyin.jpg' | relative_url }}" alt="王泽胤"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">王泽胤<br>（2024级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/xiao-meihao.jpg' | relative_url }}" alt="肖美浩"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">肖美昊<br>（2024级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/jiang-qizhi.jpg' | relative_url }}" alt="蒋祺至"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">蒋祺至<br>（2024级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/yang-yixue.jpg' | relative_url }}" alt="杨怡雪"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">杨怡雪<br>（2025级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/hu-lu.jpg' | relative_url }}" alt="胡璐"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">胡璐<br>（2025级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ma-wenbo.jpg' | relative_url }}" alt="马文博"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">马文博<br>（2025级）</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ou-xueqian.jpg' | relative_url }}" alt="欧学谦"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">欧学谦<br>（2025级）</div>
  </div>
</div>

</div>
