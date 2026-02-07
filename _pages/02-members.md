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
/* ===== Members page (self-contained) ===== */
.members-fw{
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 8px;
}

/* 标题风格 */
.members-fw h2{
  margin: 8px 0 14px;
  padding-left: 10px;
  border-left: 4px solid #1f4e79;
}
.members-fw h3{
  margin: 10px 0 12px;
}

/* 分隔线 */
.members-sep{
  border: 0;
  border-top: 1px solid #e5e7eb;
  margin: 20px 0;
}

/* 网格：教师3列，学生4列 */
.faculty-grid{
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 220px));
  gap: 20px;
  justify-content: center;
  align-items: start;
  margin: 10px 0 18px;
}

.member-grid{
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 220px));
  gap: 20px;
  justify-content: center;
  align-items: start;
  margin: 10px 0 18px;
}

/* 卡片 */
.faculty-card,
.member-card{
  border: 1px solid #e5e7eb;
  background: #f9fafb;
}

.faculty-photo-shell,
.member-photo-shell{
  padding: 8px;
  background: #efefef;
  border-bottom: 1px solid #e5e7eb;
}

/* 关键：教师和学生照片统一尺寸（同一比例） */
.faculty-photo,
.member-photo{
  width: 100%;
  aspect-ratio: 3 / 4;
  height: auto;
  object-fit: cover;
  object-position: center top;
  display: block;
  background: #e5e7eb;
}

/* 名字样式统一 */
.faculty-name,
.member-name{
  text-align: center;
  font-size: 1.05rem;
  font-weight: 700;
  color: #374151;
  line-height: 1.35;
  padding: 10px 6px 12px;
  background: #f3f4f6;
  border-top: 1px solid #e5e7eb;
}

/* 教师附加信息 */
.faculty-info{
  text-align: center;
  padding: 10px 10px 12px;
  background: #fff;
  min-height: 68px;
}
.faculty-info p{
  margin: 4px 0;
}
.faculty-info a{
  color: #1f4e79;
  text-decoration: none;
}
.faculty-info a:hover{
  text-decoration: underline;
}

/* 响应式 */
@media (max-width: 1200px){
  .faculty-grid{ grid-template-columns: repeat(3, minmax(0, 210px)); }
  .member-grid{  grid-template-columns: repeat(3, minmax(0, 210px)); }
}
@media (max-width: 900px){
  .faculty-grid{ grid-template-columns: repeat(2, minmax(0, 210px)); }
  .member-grid{  grid-template-columns: repeat(2, minmax(0, 210px)); }
}
@media (max-width: 560px){
  .faculty-grid,
  .member-grid{ grid-template-columns: 1fr; }
  .faculty-card,
  .member-card{ max-width: 260px; margin: 0 auto; }
}
</style>

<div class="members-fw">

## 教师

<div class="faculty-grid">
  <article class="faculty-card">
    <div class="faculty-photo-shell">
      <img class="faculty-photo"
           src="{{ '/images/members/ji-weixing.png' | relative_url }}"
           alt="计卫星"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="faculty-name">计卫星（教授）</div>
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
    <div class="faculty-name">高建花（讲师）</div>
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
    <div class="faculty-name">石剑君（博士后）</div>
    <div class="faculty-info"></div>
  </article>
</div>

<hr class="members-sep" />

### 博士生

<div class="member-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-bingxin.jpg' | relative_url }}" alt="刘秉鑫"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘秉鑫</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ge-danying.jpg' | relative_url }}" alt="葛丹颖"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">葛丹颖</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-pan.jpg' | relative_url }}" alt="刘攀"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘攀</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-jingmin.jpg' | relative_url }}" alt="刘敬民"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘敬民</div>
  </div>
</div>

<hr class="members-sep" />

### 硕士生

<div class="member-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/zhang-yuxiang.jpg' | relative_url }}" alt="张寓祥"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">张寓祥</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/huang-yinghui.jpg' | relative_url }}" alt="黄颖晖"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">黄颖晖</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/wang-zeyin.jpg' | relative_url }}" alt="王泽胤"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">王泽胤</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/xiao-meihao.jpg' | relative_url }}" alt="肖美浩"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">肖美浩</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/jiang-qizhi.jpg' | relative_url }}" alt="蒋祺至"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">蒋祺至</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/yang-yixue.jpg' | relative_url }}" alt="杨怡雪"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">杨怡雪</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/hu-lu.jpg' | relative_url }}" alt="胡璐"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">胡璐</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ma-wenbo.jpg' | relative_url }}" alt="马文博"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">马文博</div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ou-xueqian.jpg' | relative_url }}" alt="欧学谦"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">欧学谦（2025级）</div>
  </div>
</div>

</div>
