# MVP — Data Analysis & Best Practices: Blood Donor Registry

Capstone project for the Data Analysis module of the PUC-Rio "Ciência de Dados e Analytics" postgraduate program. A full exploratory data analysis of a blood donor registry, framed around testable hypotheses about donor demographics, blood type distribution, and donation behavior, following the CRISP-DM-style structure taught in the course (business understanding → data collection → preparation → exploration → modeling-ready dataset → conclusions).

## Dataset

[Blood Donor Registry Dataset](https://www.kaggle.com/datasets/tarekmasryo/blood-donor-registry-dataset) (Kaggle) — donor demographics, blood type, chronic conditions, smoking status, lifetime donations, and eligibility.

## Hypotheses explored

1. Which blood types face the most compatibility restrictions?
2. How does donor gender distribution vary?
3. Does smoking status correlate with donation behavior or chronic conditions?

## Key findings

- Very low participation from donors aged 20–30 relative to older cohorts — a risk signal for future donor-pool sustainability.
- O+ is the blood type with the strongest compatibility restrictions (62% of the affected sample).
- Smokers donate slightly more often than non-smokers, and — counter to the initial hypothesis — show marginally *fewer* chronic conditions in this dataset.
- Rare types (B-, AB-, AB+) warrant targeted retention campaigns given the shrinking donor base.

Full statistical breakdown (means, standard deviations, histograms per hypothesis) and the final conclusion are in the notebook.

## Contents

- [`MVP_Doacao_de_Sangue.ipynb`](MVP_Doacao_de_Sangue.ipynb) — main notebook: data cleaning, descriptive statistics, hypothesis testing, visualizations, conclusion.
- [`data/`](data) — donor registry (ML-ready), blood compatibility lookup, and population distribution reference data.

## Tech stack

Python, Pandas, NumPy, Matplotlib/Seaborn, SciPy.
