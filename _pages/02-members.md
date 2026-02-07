---
title: "成员介绍"
permalink: /members/
layout: single
author_profile: false
classes:
  - members-page
description: "Star-Lab 课题组成员"
---

<style>
/* ===== Members page only: 强制统一 ===== */
.members-page .members-fw{
  max-width: 1160px;
  margin: 0 auto;
}

/* 标题 */
.members-page .members-title{
  font-size: 2.0rem;
  font-weight: 700;
  margin: 1rem 0 0.8rem;
  border-left: 4px solid #1f4e79;
  padding-left: 10px;
  line-height: 1.25;
}
.members-page .members-subtitle{
  font-size: 1.55rem;
  font-weight: 700;
  margin: 1rem 0 0.7rem;
  line-height: 1.25;
}
.members-page .members-divider{
  border: 0;
  border-top: 1px solid #e5e7eb;
  margin: 22px 0;
}

/* 网格 */
.members-page .faculty-grid{
  display: grid !important;
  grid-template-columns: repeat(3, 220px) !important;
  gap: 20px !important;
  justify-content: start !important;
}
.members-page .member-grid{
  display: grid !important;
  grid-template-columns: repeat(4, 220px) !important;
  gap: 20px !important;
  justify-content: start !important;
}

/* 卡片 */
.members-page .faculty-card,
.members-page .member-card{
  width: 220px !important;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  display: flex;
  flex-direction: column;
}

/* 关键：照片壳固定高度，图片绝对定位填满 */
.members-page .faculty-photo-shell,
.members-page .member-photo-shell{
  position: relative !important;
  width: 100% !important;
  height: 300px !important;   /* 所有照片统一高度 */
  padding: 0 !important;
  overflow: hidden !important;
  background: #efefef !important;
  border-bottom: 1px solid #e5e7eb !important;
}

.members-page .faculty-photo,
.members-page .member-photo{
  position: absolute !important;
  inset: 0 !important;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center top !important;
  display: block !important;
  background: #e5e7eb;
}

/* 文字区 */
.members-page .faculty-name,
.members-page .member-name{
  text-align: center;
  font-size: 1.08rem;
  font-weight: 700;
  color: #374151;
  line-height: 1.25;
  padding: 10px 8px;
  border-top: 1px solid #e5e7eb;
  background: #f3f4f6;
}
.members-page .faculty-info,
.members-page .member-meta{
  text-align: center;
  padding: 10px 12px 12px;
  background: #fff;
  color: #4b5563;
  line-height: 1.6;
  font-size: 0.94rem;
}
.members-page .faculty-info p,
.members-page .member-meta p{
  margin: 4px 0;
}
.members-page .faculty-info a{
  color: #1f4e79;
  text-decoration: none;
}
.members-page .faculty-info a:hover{
  text-decoration: underline;
}

/* 响应式 */
@media (max-width: 1200px){
  .members-page .faculty-grid{ grid-template-columns: repeat(2, 220px) !important; }
  .members-page .member-grid{ grid-template-columns: repeat(3, 220px) !important; }
}
@media (max-width: 900px){
  .members-page .faculty-grid{ grid-template-columns: repeat(1, 220px) !important; }
  .members-page .member-grid{ grid-template-columns: repeat(2, 220px) !important; }
}
@media (max-width: 560px){
  .members-page .member-grid{ grid-template-columns: repeat(1, 220px) !important; }
}
</style>

<div class="members-fw">

<h2 class="members-title">教师</h2>

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
    <div class="faculty-info">
      <p>&nbsp;</p>
    </div>
  </article>
</div>

<hr class="members-divider"/>

<h3 class="members-subtitle">博士生</h3>

<div class="member-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-bingxin.jpg' | relative_url }}" alt="刘秉鑫"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘秉鑫</div>
    <div class="member-meta">
      <p>2024级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ge-danying.jpg' | relative_url }}" alt="葛丹颖"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">葛丹颖</div>
    <div class="member-meta">
      <p>2025级</p>
      <p>研究方向：大模型推理加速</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-pan.jpg' | relative_url }}" alt="刘攀"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘攀</div>
    <div class="member-meta">
      <p>2025级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/liu-jingmin.jpg' | relative_url }}" alt="刘敬民"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">刘敬民</div>
    <div class="member-meta">
      <p>2025级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>
</div>

<hr class="members-divider"/>

<h3 class="members-subtitle">硕士生</h3>

<div class="member-grid">
  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/zhang-yuxiang.jpg' | relative_url }}" alt="张寓祥"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">张寓祥</div>
    <div class="member-meta">
      <p>2023级</p>
      <p>研究方向：并行计算</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/huang-yinghui.jpg' | relative_url }}" alt="黄颖晖"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">黄颖晖</div>
    <div class="member-meta">
      <p>2024级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/wang-zeyin.jpg' | relative_url }}" alt="王泽胤"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">王泽胤</div>
    <div class="member-meta">
      <p>2024级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/xiao-meihao.jpg' | relative_url }}" alt="肖美浩"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">肖美浩</div>
    <div class="member-meta">
      <p>2024级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/jiang-qizhi.jpg' | relative_url }}" alt="蒋祺至"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">蒋祺至</div>
    <div class="member-meta">
      <p>2024级</p>
      <p>研究方向：大模型推理加速</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/yang-yixue.jpg' | relative_url }}" alt="杨怡雪"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">杨怡雪</div>
    <div class="member-meta">
      <p>2025级</p>
      <p>研究方向：并行计算</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/hu-lu.jpg' | relative_url }}" alt="胡璐"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">胡璐</div>
    <div class="member-meta">
      <p>2025级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ma-wenbo.jpg' | relative_url }}" alt="马文博"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">马文博</div>
    <div class="member-meta">
      <p>2025级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>

  <div class="member-card">
    <div class="member-photo-shell">
      <img class="member-photo" src="{{ '/images/members/ou-xueqian.jpg' | relative_url }}" alt="欧学谦"
           onerror="this.onerror=null;this.src='{{ '/images/members/default.jpg' | relative_url }}';">
    </div>
    <div class="member-name">欧学谦</div>
    <div class="member-meta">
      <p>2025级</p>
      <p>研究方向：代码分析</p>
    </div>
  </div>
</div>

</div>
