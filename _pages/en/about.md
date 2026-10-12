---
title: "About"
permalink: /en/about/
layout: single
author_profile: false
classes: wide
lang: en
description: "BNU-SYS: computer architecture, parallel and high-performance computing, code analysis and optimization, and large-model inference optimization."
---

<section class="star-hero">
  <p class="star-summary">
    BNU-SYS is part of the School of Artificial Intelligence at Beijing Normal University and is led by
    Professor Weixing Ji. Rooted in the core problems of computer systems, the group conducts systematic research
    along the chain of computer architecture—compiler optimization—parallel computing—large-model inference,
    covering the optimization of sparse-matrix computation and iterative solvers, compression and inference
    acceleration for large models, compiler optimization for domestic processors, and large-scale code defect detection.
  </p>
</section>

---

## Research Directions

<div class="star-grid">
  <div class="star-card">
    <h3>Sparse-matrix computation and iterative solver optimization</h3>
    <p>The nonzeros of sparse matrices are irregularly distributed, which limits parallel efficiency. Based on the characteristics of nonzero distributions, the group accelerates sparse computational kernels. Targeting the three problems of key-kernel computational cost, distributed data-communication cost, and load imbalance, it studies new floating-point format designs, low-precision transmission optimization, and reinforcement-learning-based load balancing.</p>
  </div>
  <div class="star-card">
    <h3>Large-model compression and inference acceleration</h3>
    <p>Research on key techniques such as KV cache, FlashAttention, and speculative decoding. The group develops MuduoXinyu, a lightweight in-house inference engine supporting GPU, NPU, and DCU backends. For the challenges that RAG and speculative decoding face in vertical-domain applications, it studies multi-task speculative decoding optimization.</p>
  </div>
  <div class="star-card">
    <h3>Feedback-directed compiler optimization and superoptimization for domestic processors</h3>
    <p>To address the lack of efficient numerical libraries for domestic architectures, the group extracts and optimizes common operators in typical applications and studies feedback-driven optimization and superoptimization for numerical computation. To date it has optimized 200 numerical programs for the ARM family, with results deployed in 3 organizations.</p>
  </div>
  <div class="star-card">
    <h3>Large-scale code defect detection and open-source defect corpus construction</h3>
    <p>To tackle concurrency errors, resource leaks, and other defects that are hard to locate and detect in large codebases, the group builds real-world defect corpora and efficient detection tools, covering three areas: building a Java resource-leak test suite, defect detection for kernel-driver code, and building a concurrency-error test suite for the Linux kernel.</p>
  </div>
</div>

---

## Research Philosophy

- **Academic rigor**: clear problem definitions, well-designed experiments, and verifiable conclusions.
- **Systems perspective**: jointly considering algorithms, compilers, and hardware for end-to-end optimization.
- **Reproducibility**: emphasized via public implementations, reproducible experiments, and transferable engineering.

---

## Group Photo

<figure class="star-figure">
  <img src="{{ '/images/group-photo.jpg' | relative_url }}" alt="BNU-SYS group photo" class="img-fluid" />
  <figcaption>BNU-SYS teamwork and research exchange</figcaption>
</figure>
