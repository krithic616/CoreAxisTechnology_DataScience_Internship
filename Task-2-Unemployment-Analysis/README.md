# Task 2 — Unemployment Analysis with Python

## Objective
Analyze unemployment trends in India using the exact dataset specified by the CoreAxis Technology Data Science Internship.

## Dataset
- Kaggle dataset: `gokulrajkmv/unemployment-in-india`
- Expected local filename: `data/Unemployment in India.csv`
- The raw dataset is not committed to this public repository. Place the downloaded dataset in the `data/` folder before running the analysis.

## Analysis performed
1. Data cleaning and validation
2. Descriptive statistics
3. Monthly unemployment-rate trend analysis
4. Rural vs. urban comparison
5. Regional comparison
6. Early COVID-19 period analysis
7. Relationship checks between unemployment, employment and labour participation
8. Visualization and interpretation

## Dataset cleaning
The supplied CSV contained 768 rows, including 28 completely blank rows. After removing blank rows and duplicate records, 740 observations remained. The cleaned dataset covers 28 regions from May 2019 through June 2020.

## Key findings from the supplied dataset
- Overall mean unemployment rate: **11.79%**
- Mean unemployment rate before March 2020: **9.51%**
- Mean unemployment rate from March 2020 onward: **17.78%**
- Monthly average unemployment rate: **10.70% in March 2020**, **23.64% in April 2020**, **24.88% in May 2020**, and **11.90% in June 2020**.
- Average unemployment was **10.32% in rural observations** and **13.17% in urban observations**.
- The five regions with the highest average unemployment rates were **Tripura (28.35%)**, **Haryana (26.28%)**, **Jharkhand (20.59%)**, **Bihar (18.92%)**, and **Himachal Pradesh (18.54%)**.
- The correlation between unemployment rate and estimated employed was **-0.223**. The correlation between unemployment rate and labour participation rate was approximately **0.003**. These are descriptive relationships and do not establish causation.

## Important Findings File
Detailed findings, interpretation, policy-relevant considerations, and limitations are documented in:

`IMPORTANT_FINDINGS.md`

A compact numerical summary is available in:

`important_findings_summary.csv`

## Visualizations
The analysis script generates:
- `visualizations/monthly_unemployment_trend.png`
- `visualizations/rural_vs_urban.png`
- `visualizations/region_unemployment.png`
- `visualizations/covid_period.png`

## Run
From the `Task-2-Unemployment-Analysis` directory:

```bash
python src/unemployment_analysis.py
```

Or open `notebooks/Unemployment_Analysis.ipynb` in Jupyter.

## Tools
Python, Pandas, NumPy, Matplotlib, Jupyter.

## Note
The COVID-19 interpretation is limited to the time period present in this dataset (through June 2020). The analysis describes patterns in the supplied data and does not claim that observed changes were caused by any single factor.
