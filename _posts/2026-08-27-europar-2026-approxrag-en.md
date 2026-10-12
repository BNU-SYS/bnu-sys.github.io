---
title: "Danying Ge Presented at Euro-Par 2026"
date: 2026-08-27
categories: [news, conference-report]
tags: [academic conference, Euro-Par, RAG, large-model inference, BNU-SYS]
cover: /images/conference/europar-2026-cover.jpg
excerpt: "At the 32nd International European Conference on Parallel and Distributed Computing (Euro-Par 2026), Danying Ge presented ApproxRAG, an inference acceleration work for retrieval-augmented generation (RAG) that jointly optimizes data movement among disk, host memory, and device memory to achieve up to a 3.66× inference speedup."
lang: en
related: false
permalink: /en/europar-2026-approxrag/
alt_zh: /news/conference-report/europar-2026-approxrag/
---

From August 24–28, 2026, the 32nd International European Conference on Parallel and Distributed Computing (Euro-Par 2026) was held in Pisa, Italy. Danying Ge, a doctoral student in the group, attended the conference and gave a presentation titled **ApproxRAG**.

## About the Conference

Euro-Par is Europe's flagship academic conference in the field of parallel and distributed computing. Held over a full week, it covers the field's complete research spectrum — from fundamental algorithms to end-to-end applications, from low-power edge devices to supercomputing and cloud-edge collaboration, and from architectural breakthroughs and compilation innovations to emerging programming models, performance engineering, reproducibility, and sustainability — providing scholars worldwide with an ample platform for academic exchange.

## Presentation Content

Danying Ge presented the research work ApproxRAG, an inference acceleration technique for retrieval-augmented generation (RAG). To address the high inference latency and heavy disk I/O overhead that existing RAG techniques face when processing large volumes of external documents, this work proposes a method that jointly optimizes data movement among **disk, host memory, and device memory**. The presentation elaborated on three core techniques of the framework:

1. **Hybrid compression strategy**: reducing the disk storage overhead of the key-value cache (KV Cache).

2. **Semantic-similarity-based KV Cache reuse mechanism**: reducing unnecessary disk accesses.

3. **Cache eviction strategy**: building an eviction policy that combines access frequency, temporal locality, and retrieval score to improve memory resource utilization.

## Experimental Results

The experiments were based on the LLaMA 2-7B and LLaMA 2-13B models and validated using a Wikipedia knowledge base along with several question-answering benchmarks. The results show that ApproxRAG achieves up to **3.66×** inference speedup while maintaining text generation quality, demonstrating its potential for efficient large-model inference and storage optimization.

## Highlights

![Danying Ge at the Euro-Par 2026 venue](/images/conference/europar-2026-01.jpg)

![Danying Ge presenting at Euro-Par 2026](/images/conference/europar-2026-02.jpg)
