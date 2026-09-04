# Task 2 — Important Findings

## Dataset Summary

- **Source:** Kaggle `gokulrajkmv/unemployment-in-india`
- **Valid observations:** 740
- **Regions:** 28
- **Period:** May 2019 to June 2020
- **Frequency:** Monthly
- **Geographic breakdown:** Rural and Urban

## Important Findings

### 1. Overall Unemployment

The mean unemployment rate across the cleaned observations was **11.79%**.

### 2. COVID-19 Period

The monthly average unemployment rate was relatively stable around 9–10% through early 2020, then increased sharply:

| Month | Average unemployment rate |
|---|---:|
| March 2020 | 10.70% |
| April 2020 | 23.64% |
| May 2020 | 24.88% |
| June 2020 | 11.90% |

The highest monthly average in the dataset occurred in **May 2020 at 24.88%**. June 2020 showed a substantial decline to 11.90%.

### 3. Pre-COVID vs. COVID-Period Comparison

Using March 2020 as the start of the COVID-period analysis:

- **Before March 2020:** 9.51% average unemployment
- **March 2020 onward:** 17.78% average unemployment

This indicates a pronounced change in unemployment during the period covered by the dataset. The dataset alone does not establish causation.

### 4. Rural vs. Urban

- **Rural average:** 10.32%
- **Urban average:** 13.17%

Urban observations had the higher average unemployment rate in this dataset.

### 5. Regional Differences

The five regions with the highest average unemployment rates were:

1. **Tripura — 28.35%**
2. **Haryana — 26.28%**
3. **Jharkhand — 20.59%**
4. **Bihar — 18.92%**
5. **Himachal Pradesh — 18.54%**

This shows substantial variation across regions.

### 6. Relationship Between Variables

The correlation between unemployment rate and estimated employment was **-0.223**.

This is a weak negative correlation in the supplied observations. Correlation is descriptive and should not be interpreted as proof of a causal relationship.

The correlation between unemployment rate and labour participation rate was approximately **0.003**, indicating almost no linear relationship in this dataset.

## Interpretation

The strongest pattern in the dataset is the sharp rise in unemployment during **April–May 2020**, followed by a marked reduction in June 2020. Regional and rural/urban differences are also substantial.

## Policy-Relevant Considerations

Based strictly on the observed patterns, the analysis suggests that:

- Employment-support measures should consider regional differences rather than using a single uniform assumption.
- Urban areas in this dataset show higher average unemployment and may require focused employment-support analysis.
- The sharp April–May 2020 increase highlights the importance of monitoring labour-market disruption during major economic shocks.
- Regional unemployment indicators can be used to identify areas requiring closer labour-market assessment.

These are analytical considerations derived from the dataset, not causal policy conclusions.

## Limitation

The dataset ends in **June 2020**, so this project should not be interpreted as an analysis of India's unemployment situation after that period. The COVID-19 analysis is limited to the observations available in the supplied dataset.
