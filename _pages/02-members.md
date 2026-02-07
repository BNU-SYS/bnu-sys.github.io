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
/* ==========================================================================
   强制覆盖样式 (Force Override)
   使用 html body 前缀是为了确立最高优先级，战胜 _page.scss
   ========================================================================== */

/* 1. 强制重置容器宽度 */
html body .members-page .members-fw {
  max-width: 1160px;
  margin: 0 auto;
}

/* 2. 强制锁定网格列宽 */
html body .members-page .faculty-grid {
  display: grid !important;
  grid-template-columns: repeat(3, 220px) !important; /* 教师3列，每列220px */
  gap: 20px !important;
  justify-content: start !important;
}

html body .members-page .member-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 220px) !important; /* 学生4列，每列220px */
  gap: 20px !important;
  justify-content: start !important;
}

/* 3. 强制卡片宽度 */
html body .members-page .faculty-card,
html body .members-page .member-card {
  width: 220px !important;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  display: flex;
  flex-direction: column;
}

/* 
   4. 核心修复：照片外壳 (Shell) 
   这里强制高度为 300px
*/
html body .members-page .faculty-photo-shell,
html body .members-page .member-photo-shell {
  position: relative !important;
  width: 100% !important;
  height: 300px !important;     /* <--- 强制高度，改这里调整长宽比 */
  padding: 0 !important;
  overflow: hidden !important;  /* 超出部分切掉 */
  background: #e5e7eb !important;
  border-bottom: 1px solid #e5e7eb !important;
  aspect-ratio: auto !important; /* 杀死 SCSS 中的 aspect-ratio */
}

/* 
   5. 核心修复：照片本体 (Img) 
   强制填满外壳，且杀死 aspect-ratio 和 height: auto
*/
html body .members-page .faculty-photo,
html body .members-page .member-photo {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;        /* 强制拉伸到 300px 高 */
  
  object-fit: cover !important;   /* 关键：保持比例填满，不拉伸变形 */
  object-position: top center !important; /* 优先显示头部 */
  
  max-width: none !important;
  max-height: none !important;
  min-height: 100% !important;
  aspect-ratio: auto !important;  /* 再次确保杀死 SCSS 中的比例限制 */
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
}

/* ===== 以下是普通文字样式，无需最高权重 ===== */
.members-page .members-title {
  font-size: 2.0rem;
  font-weight: 700;
  margin: 1rem 0 0.8rem;
  border-left: 4px solid #1f4e79;
  padding-left: 10px;
}
.members-page .members-subtitle {
  font-size: 1.55rem;
  font-weight: 700;
  margin: 1rem 0 0.7rem;
}
.members-page .members-divider {
  border: 0;
  border-top: 1px solid #e5e7eb;
  margin: 22px 0;
}
.members-page .faculty-name,
.members-page .member-name {
  text-align: center;
  font-size: 1.08rem;
  font-weight: 700;
  color: #374151;
  padding: 10px 8px;
  border-top: 1px solid #e5e7eb;
  background: #f3f4f6;
  line-height: 1.3;
}
.members-page .faculty-info,
.members-page .member-meta {
  text-align: center;
  padding: 10px 12px;
  background: #fff;
  color: #4b5563;
  font-size: 0.94rem;
  flex-grow: 1; /* 确保卡片底部对齐 */
}
.members-page .faculty-info a {
  color: #1f4e79;
  text-decoration: none;
}

/* ===== 响应式适配 ===== */
@media (max-width: 1200px) {
  html body .members-page .faculty-grid { grid-template-columns: repeat(2, 220px) !important; }
  html body .members-page .member-grid { grid-template-columns: repeat(3, 220px) !important; }
}
@media (max-width: 960px) {
  html body .members-page .faculty-grid { grid-template-columns: repeat(1, 220px) !important; }
  html body .members-page .member-grid { grid-template-columns: repeat(2, 220px) !important; }
}
@media (max-width: 560px) {
  html body .members-page .member-grid { grid-template-columns: repeat(1, 220px) !important; }
  /* 手机端居中 */
  html body .members-page .faculty-grid,
  html body .members-page .member-grid { justify-content: center !important; }
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
    <div class="member-name">欧学谦（2025级）</div>
    <div class="member-meta">
     
      <p>研究方向：代码分析</p>
    </div>
  </div>
</div>

</div>
