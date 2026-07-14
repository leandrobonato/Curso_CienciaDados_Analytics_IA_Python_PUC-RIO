# MVP — Data Engineering: Global CO₂ Emissions & Absorption

Capstone project for the Data Engineering module of the PUC-Rio "Ciência de Dados e Analytics" postgraduate program. An end-to-end data pipeline that collects, cleans, and integrates public climate datasets from multiple international organizations to answer questions about global CO₂ emissions and absorption trends.

## Questions answered

1. What is the planet's carbon emission per year?
2. What is the carbon emission per country / per continent, per year?
3. What is the CO₂ absorption rate per year, per continent, per country?

## Data sources

Public datasets from Carbon Monitor, Climate Watch, the International Energy Agency (IEA), NASA, the United Nations, Our World in Data, and the World Bank Group. Source links and field-level documentation for every dataset used are in the notebook.

> Raw datasets are not included in this repository due to size — see the notebook for direct download links to each source.

## Contents

- [`MVP_Emissoes_CO2_Global.ipynb`](MVP_Emissoes_CO2_Global.ipynb) — main notebook: data collection, cleaning/ETL, integration, analysis and charts, self-assessment.
- [`scripts/`](scripts) — standalone Python helpers used during ETL (NetCDF→CSV conversion, splitting large CSVs for GitHub, country lookup by lat/long, GDP reference data).
- [`sql/`](sql) — SQL notes used while querying the integrated dataset.
- [`images/`](images) — exported charts (global/regional/country emission and absorption trends, 2000–2024).
- `aws-mvp-pipeline-simple-report.pdf`, `aws-mvp-pipeline-vpc.drawio.png` — draft design for a cloud (AWS) version of this pipeline (future work).

## Tech stack

Python, Pandas, NumPy, Matplotlib/Seaborn, SQL.
