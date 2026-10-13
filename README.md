# Smart Factory Energy Optimisation Using Machine Learning

**Data Science | Unsupervised Learning | Energy Analytics | Industry 4.0**

A public, reproducible **synthetic-data demonstration** inspired by my 2024 MSc Artificial Intelligence and Data Science final-year project at the University of Hull: *Unsupervised Machine Learning Approaches for Determining Influential Factors of Energy Consumption in an Industry 4.0 Smart Factory*.

> **Data protection:** This repository does **not** contain the original industrial datasets, original notebook outputs, internal equipment identifiers, or the complete dissertation. All included sample data and generated charts are synthetic. Synthetic-demo metrics are **not** the academic report's results.

## Business problem

Energy-intensive manufacturers need to understand which operational and environmental factors coincide with high electricity demand, distinguish production-driven demand from potential inefficiencies, and identify operating patterns worth investigating.

**Questions:**
1. How do production, ambient conditions and equipment loads relate to energy consumption?
2. Can unsupervised learning identify distinct factory operating modes?
3. Which systems warrant further investigation for energy-efficiency improvements?

## What I did in the original MSc research

- Structured the work using **CRISP-DM**.
- Combined production, energy and environmental information; assessed missing values and prepared analytical variables.
- Investigated **Pearson and partial correlations** to distinguish simple associations from associations controlling for other variables.
- Examined time-series patterns and reported **SARIMA/SARIMAX** analysis.
- Compared **Autoencoder + K-Means**, **PCA + K-Means**, and **hierarchical clustering**.
- Evaluated cluster quality with silhouette, Davies–Bouldin and Calinski–Harabasz metrics.

**Original final-year-project-reported clustering comparison** (historical academic results; not reproduced by the synthetic demo):

| Method | Silhouette | Davies–Bouldin | Calinski–Harabasz |
|---|---:|---:|---:|
| Autoencoder + K-Means | **0.6135** | 0.5805 | **32.4517** |
| PCA + K-Means | 0.2176 | 0.6979 | 6.8215 |
| Hierarchical clustering | 0.4562 | **0.4884** | 22.7242 |

The academic report selected Autoencoder + K-Means for its strongest silhouette and Calinski–Harabasz scores, while hierarchical clustering had the lowest Davies–Bouldin score. The academic report also reports correlations between energy use and cooling equipment, production volumes and ambient temperature. **These are associations, not proof of causation or realised energy savings.**

## Public reproducible demo

This repository provides a **simplified baseline**, not a full recreation of the original research. It uses synthetic daily observations and demonstrates:

- Data checks and numeric correlations
- Median imputation and standardisation
- K-Means clustering, comparing k=2–5 using silhouette score
- PCA for **2D visualisation only**
- Synthetic energy trend and cluster visualisations

**Not yet implemented in the public demo:** autoencoder, hierarchical clustering, partial correlation, or SARIMA forecasting. These methods are described as part of the original academic project, not falsely represented as reproduced by the included code.

## Run locally

```bash
python -m pip install -r requirements.txt
python src/analysis.py
```

The script prints summary statistics and saves `synthetic_energy_trend.png` and `synthetic_clusters.png` in the repository root.

## Project structure

```text
smart-factory-energy-portfolio/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── synthetic_factory_energy.csv
├── src/
│   └── analysis.py
└── notebooks/
    └── synthetic_energy_demo.ipynb
```

## Findings and business interpretation

The **original academic project** identified cooling systems, selected production equipment and production volume as areas associated with total energy demand. Seasonal temperature variation also appeared relevant. The practical recommendation is to **prioritise monitoring and validation** of these systems before proposing changes, and to track energy intensity (e.g., kWh per unit produced) rather than electricity consumption alone.

**Important limitations:** The research report contains a few inconsistent descriptions of cluster count (three in the results table and profiles, four in some figure captions). The forecasting summary also contains unusual coefficient/statistic formatting. These require validation against original analysis before making strong claims. No actual savings, causal impacts, or forecast accuracy improvements are claimed.

## Skills demonstrated

`Python` · `Pandas` · `Scikit-learn` · `EDA` · `Data Cleaning` · `Feature Scaling` · `Clustering` · `PCA` · `Model Evaluation` · `Data Visualisation` · `Business Communication`

**Author:** Oluwatobiloba Olufowobi | MSc Artificial Intelligence and Data Science, University of Hull
