# Efficient Maize Preservation: Storage Silo Analytics
**Author:** [Tunu Chesco Pilla]  
**Registration Number:** [BPE/D/2024/0014]  
*course name:**Basics of computer programming 
**Course Code:** AGE219  

---

## Problem Statement
Post-harvest losses in agricultural engineering present severe food security issues. Maize is highly subjected to high internal grain temperatures and humidity fluctuations during silo storage, leading to fungal development and facilitating spoilage. This project establishes data-driven correlations between critical physical variables to automate silo ventilation adjustments.

## Data Source
The analytical engine programmatically mines data from **10 separate tabular `.csv` data loggers** (`silo_week1.csv` to `silo_week10.csv`), tracking timestamps, temperatures, moisture counts, and corresponding deterioration rates across distinct spatial blocks.

## Methodology
* **Pandas:** Structured data processing by dynamically joining files, parsing time structures, cleaning records with missing inputs, and filtering systemic anomalous outliers.
* **NumPy:** Conducted high-efficiency array mathematics converting temperature attributes into scientific international units (°C).
* **SciPy:** Executed a standard computational scientific bivariate linear regression modeling step to find the exact mathematical trend between environment moisture profiles and grain preservation health index.

---

## Results & Conclusion
The statistical test returned a strong positive correlation between moisture contents and degradation indicators. To achieve highly efficient maize preservation, ambient moisture must be strictly maintained below a specific safety margin (< 14.5%).

### Project Engineering Visualizations

#### 1. Trend Analysis Plot
![Trend Analysis](trend_analysis.png)

#### 2. Categorical Comparison Plot
![Categorical Comparison](categorical_comparison.png)

#### 3. Correlation Plot
![Correlation Plot](correlation_plot.png)
