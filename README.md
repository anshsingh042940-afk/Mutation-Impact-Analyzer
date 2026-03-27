# Mutation Impact Analyzer

A Python project that analyzes DNA mutations to see how they affect protein synthesis.  
It identifies **silent, missense, and nonsense mutations** and visualizes the impact using a pie chart.

---

## Features
- Compare original and mutated DNA sequences
- Break DNA into codons (3 bases each)
- Translate codons to amino acids
- Detect mutation types:
  - **Silent mutation** – no protein change
  - **Missense mutation** – protein structure changes
  - **Nonsense mutation** – protein stops early
- Visualize results with a pie chart showing protein affected vs not affected

---

## Installation

1. Install Python (version 3.8+ recommended)
2. Install required libraries:
   ```bash
   pip install biopython pandas matplotlib
