<style>
/* ===== Members page: single source of truth ===== */
.members-fw{
  --card-w: 132px;   /* 原 150 -> 进一步缩小 */
  --photo-h: 176px;  /* 原 200 -> 进一步缩小 */
  --gap-x: 24px;     /* 横向间距增大 */
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
