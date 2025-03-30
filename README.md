# Multi-Level Comparison Sorting Algorithms

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

A comparative analysis of sorting algorithms with multi-level attribute comparisons.

## 🔄 Fork Information

This project was forked from [file-sorting-starter](https://github.com/Algorithmology/file-sorting-starter) and significantly extended with:

- Multi-level sorting capabilities
- Expanded dataset support

## 📌 Overview

This project evaluates three sorting algorithms (**Bubble Sort**, **QuickSort**, and **Timsort**) when handling datasets with duplicate entries in primary attributes. Key features:

- **Hierarchical tie-breaking** (`country > name > phone_number > job > email`)
- **Performance benchmarking** across duplicate rates (25-100%)
- **Cross-platform analysis** (macOS vs Windows)

[🔗 Detailed Blog Post on Key Findings](https://algorithmology.org/allhands/spring2025/weekeleven/teamfour/)

## 🛠️ Installation

### Requirements
- Python 3.10+
- No external dependencies

```bash
git clone https://github.com/hemanialaparthi/wapbac-sorting.git
cd wapbac-sorting
poetry install
```

## 🚀 Usage

Example Command:

```bash
poetry run filesorter --attribute email --approach bubblesort_multilevel --input-file input/people.txt --output-file output/people.txt
```

