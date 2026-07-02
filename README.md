
# Efficient Maize Preservation: Storage Silo Analytics
**Author:Tunu Chesco Pilla 
**Registration Number: BPE/D/2024/0014 
**Course Code: AGE219  

---

## Problem Statement
Post-harvest loss during grain storage is a critical challenge in agricultural engineering. Maize is highly sensitive to inner silo temperature shifts and localized moisture accumulation. Improper climate control prompts rapid structural grain decay and mold development. This analytical framework maps automated logging streams to understand the precise interaction thresholds between moisture indicators and overall silo preservation state.

## Data Source & Mined Repositories
This platform analyzes structured agricultural records modeled on actual environmental safety indicators. The experimental boundaries match baseline values referenced from these primary repositories:
1. **FAOSTAT (fao.org/faostat):** Used to baseline regional average crop post-harvest loss margins and storage metrics.
2. **World Bank Open Data (data.worldbank.org):** Sourced macro environmental tracking indexes for ambient tropical storage heat cycles.
3. **Google Dataset Search:** Configured to design the structural columns for 10 separate, independent time-series tracking datasets (`silo_week1.csv` to `silo_week10.csv`) reflecting multi-zone log readouts.

## Methodology
* **Pandas:** Handled tabular cleaning steps by programmatically joining all 10 independent tracking documents via `pd.concat()`, parsing date attributes, removing invalid data values, and calculating daily sector averages using aggregate group-by structures.
* **NumPy:** Conducted optimized vector array calculations to transform storage temperature dimensions across all files from Fahrenheit ($^\circ\text{F}$) scale down to standard metric units ($^\circ\text{C}$).
* **SciPy:** Executed a fast scientific bivariate linear regression algorithm (`stats.linregress`) to determine the correlation coefficient showing exactly how moisture percentage variations accelerate grain spoilage indicators.

---

## Results & Conclusion
The data displays an unmistakable linear increase in degradation flags when grain moisture drifts past $14.0\%$. Keeping the internal silo temperature constrained below $24^\circ\text{C}$ alongside automated air ventilation when moisture rises is the most efficient configuration for long-term maize preservation.

### Project Engineering Visualizations

#### 1. Trend Analysis Plot
![Trend Analysis](trend_analysis.png)

#### 2. Categorical Comparison Plot
![Categorical Comparison](categorical_comparison.png)

#### 3. Correlation Plot
![Correlation Plot](correlation_plot.png)




