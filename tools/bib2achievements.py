#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from collections import defaultdict
from pathlib import Path

import bibtexparser
import yaml

def norm_authors(a: str) -> str:
    return ", ".join([x.strip() for x in a.replace("\n", " ").split(" and ") if x.strip()])

def venue_of(e: dict) -> str:
    return e.get("booktitle") or e.get("journal") or e.get("publisher") or ""

def doi_link(doi: str) -> str:
    doi = (doi or "").strip()
    if not doi:
        return ""
    if doi.startswith("http://") or doi.startswith("https://"):
        return doi
    return f"https://doi.org/{doi}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bib", required=True, help="输入 bib 文件路径")
    parser.add_argument("--out", default="_data/achievements.yml", help="输出 yml 路径")
    args = parser.parse_args()

    bib_path = Path(args.bib)
    out_path = Path(args.out)

    with bib_path.open("r", encoding="utf-8") as f:
        bib_db = bibtexparser.load(f)

    by_year = defaultdict(list)

    for e in bib_db.entries:
        year_raw = e.get("year", "").strip()
        try:
            year = int(year_raw)
        except Exception:
            year = 0

        item = {
            "authors": norm_authors(e.get("author", "")),
            "title": e.get("title", "").replace("{", "").replace("}", "").strip(),
            "venue": venue_of(e).replace("{", "").replace("}", "").strip(),
            "year": year if year else year_raw,
            "thumb": "/images/papers/default.png",
            "pdf": e.get("url", "").strip(),      # 有些 bib 的 url 就是论文页/PDF
            "slides": "",
            "doi": doi_link(e.get("doi", "")),
            "bibtex": "",
            "code": "",
        }
        by_year[year].append(item)

    years_sorted = sorted([y for y in by_year.keys() if isinstance(y, int)], reverse=True)

    result = {
        "years": [{"year": y, "papers": by_year[y]} for y in years_sorted],
        "patents": [],
        "software": []
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(result, f, allow_unicode=True, sort_keys=False)

    print(f"[OK] 写入 {out_path}")

if __name__ == "__main__":
    main()
