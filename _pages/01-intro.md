---
title: "团队简介"
permalink: /about/
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
    BNU-SYS 隶属北京师范大学人工智能学院，课题负责人为计卫星教授。课题组立足计算机系统核心问题，
    围绕“体系结构—编译优化—并行计算—大模型推理”开展系统化研究，研究内容涵盖稀疏矩阵计算与迭代求解算法优化、
    大模型压缩与推理加速、面向国产处理器的编译优化，以及大规模代码缺陷检测。
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
    <h3>稀疏矩阵计算与迭代求解算法优化</h3>
    <p>稀疏矩阵非零元分布不规则、并行效率较低。课题组基于非零元分布特征开展稀疏计算内核加速优化；针对关键内核计算开销、分布式数据通信开销与负载不均衡三类问题，研究新型浮点格式设计、低精度传输优化与基于强化学习的负载均衡方法。</p>
  </div>
  <div class="star-card">
    <h3>大模型压缩与推理加速</h3>
    <p>围绕 KV Cache、FlashAttention、投机解码等关键技术开展研究；自研轻量级推理引擎 MuduoXinyu（木铎芯语），支持 GPU、NPU、DCU 等后端；针对 RAG 与投机解码在垂域应用中面临的挑战，开展垂域多任务的投机解码优化研究。</p>
  </div>
  <div class="star-card">
    <h3>面向国产处理器的反馈式编译优化与超优化技术</h3>
    <p>针对国产体系架构缺少高效适配数值计算库的问题，对典型应用中的常见算子进行提取与优化，研究基于反馈驱动优化与超优化技术的数值计算编译优化方法。目前已针对 ARM 系列完成 200 个数值计算程序的优化，成果在 3 个单位落地应用。</p>
  </div>
  <div class="star-card">
    <h3>大规模代码缺陷检测与开源缺陷库构建</h3>
    <p>针对大规模代码中并发错误、资源泄露等难以定位与检测的问题，构建面向大规模代码的真实缺陷库与高效检测工具，形成 Java 资源泄露测试集构建、内核驱动代码缺陷检测、Linux 内核并发错误缺陷测试集构建三方面工作。</p>
  </div>
</div>

---

## 研究理念

- **学术严谨**：问题定义清晰，实验设计规范，结论可验证。  
- **系统视角**：联合考虑算法、编译与硬件，追求端到端优化。  
- **可复现性**：强调公开实现、实验可复现与工程可迁移。  

---

## 课题组合照

<figure class="star-figure">
  <img src="../images/group-photo.jpg" alt="BNU-SYS 课题组合照" class="img-fluid" />
  <figcaption>BNU-SYS 团队协作与研究交流</figcaption>
</figure>
