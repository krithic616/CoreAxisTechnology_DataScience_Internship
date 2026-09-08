# Task 4 – Sales Prediction Using Python

## Objective
Predict sales from advertising expenditure and identify which channels provide the strongest predictive signal.

## Dataset
200 observations with TV, Radio, Newspaper and Sales. The original `Unnamed: 0` index was removed.

## Workflow
Data inspection → cleaning → EDA → correlation analysis → 80/20 train-test split → Linear Regression and Random Forest → MAE/RMSE/R² evaluation → feature importance → business interpretation.

## Results
| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 1.4608 | 1.7816 | 0.8994 |
| Random Forest | 0.6131 | 0.7403 | 0.9826 |

Random Forest is the best model with R² = 0.9826.

## Key Findings
- TV has the strongest correlation with Sales: 0.7822.
- Radio correlation: 0.5762.
- Newspaper correlation: 0.2283.
- Random Forest feature importance is provided in `feature_importance.csv`.

## Business Insights
TV is the strongest individual predictor in this dataset. Radio provides meaningful additional predictive signal, while Newspaper contributes much less. Budget allocation should nevertheless be validated with ROI/profit data before making real-world decisions.

## Limitation
The dataset has no dates, customer segments, geography, campaign quality or profitability fields. Therefore, this is channel-spend-based sales prediction, not time-series or segment-level forecasting.
