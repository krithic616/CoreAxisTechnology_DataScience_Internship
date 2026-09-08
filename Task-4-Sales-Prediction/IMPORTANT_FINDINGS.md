# Important Findings

- Dataset size: 200 observations.
- Missing values: 0.
- Duplicate rows: 0.
- Features: TV, Radio, Newspaper.
- Target: Sales.
- Train/test split: 80/20 with `random_state=42`.

## Model Performance
- Linear Regression: MAE 1.4608, RMSE 1.7816, R² 0.8994.
- Random Forest: MAE 0.6131, RMSE 0.7403, R² 0.9826.

## Correlation with Sales
- TV: 0.7822
- Radio: 0.5762
- Newspaper: 0.2283

## Random Forest Feature Importance
- TV: 0.6254
- Radio: 0.3617
- Newspaper: 0.0128

## Conclusion
Random Forest is the stronger predictive model on the selected test split. TV is the strongest individual advertising predictor, followed by Radio, while Newspaper has a weaker relationship with Sales.
