---
title: "葛丹颖参加 Euro-Par 2026 并作论文报告"
date: 2026-08-27
lang: zh
categories: [news, conference-report]
tags: [学术会议, Euro-Par, RAG, 大模型推理, BNU-SYS]
cover: /images/conference/europar-2026-cover.jpg
alt_en: /en/europar-2026-approxrag/
excerpt: "葛丹颖在第 32 届欧洲并行与分布式计算会议（Euro-Par 2026）上汇报了面向检索增强生成（RAG）的推理加速工作 ApproxRAG，通过协同优化磁盘、主机内存与设备内存的数据流动，实现最高 3.66 倍推理加速。"
---

2026 年 8 月 24–28 日，第 32 届欧洲并行与分布式计算会议（32nd International European Conference on Parallel and Distributed Computing，Euro-Par 2026）在意大利比萨（Pisa）举行。课题组博士生葛丹颖参加本次会议，并作题为 **ApproxRAG** 的学术报告。

## 会议简介

Euro-Par 是欧洲并行与分布式计算领域的旗舰学术会议。会议历时一周，覆盖该领域从基础算法到端到端应用、从低功耗边缘设备到超算与云边协同、从体系结构突破与编译创新到新兴编程模型、性能工程、可复现性与可持续性的完整研究谱系，为全球学者提供了充分的学术交流平台。

## 报告内容

葛丹颖汇报的研究工作 ApproxRAG 是一项面向检索增强生成（Retrieval-Augmented Generation，RAG）的推理加速技术。针对现有 RAG 技术在处理大量外部文档时面临的推理延迟高、磁盘 I/O 开销大等问题，该研究提出了一种协同优化**磁盘、主机内存与设备内存**三者数据流动的方法。报告详细阐述了框架的三项核心技术：

1. **混合压缩策略**：降低键值缓存（KV Cache）的磁盘存储开销；
2. **基于语义相似性的键值缓存重用机制**：减少不必要的磁盘访问；
3. **缓存淘汰策略**：结合访问频率、时间局部性与检索得分构建淘汰策略，提高内存资源利用效率。

## 实验结果

实验基于 LLaMA 2-7B 与 LLaMA 2-13B 模型，使用维基百科知识库及多个问答评测任务进行验证。结果表明，ApproxRAG 在保证文本生成质量的同时，实现了最高 **3.66 倍**的推理加速，展现了其在大模型高效推理与存储优化方面的应用潜力。

## 参会掠影

![葛丹颖在 Euro-Par 2026 会议现场](/images/conference/europar-2026-01.jpg)

![葛丹颖在 Euro-Par 2026 作报告](/images/conference/europar-2026-02.jpg)
