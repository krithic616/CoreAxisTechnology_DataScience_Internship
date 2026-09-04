"""
CoreAxis Technology Data Science Internship
Task 2: Unemployment Analysis with Python

Expected input:
    data/Unemployment in India.csv

The script cleans the CoreAxis-specified dataset, performs EDA,
analyzes the early COVID-19 period, and saves summary visualizations.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
DATA_PATH = BASE / "data" / "Unemployment in India.csv"
OUTPUT_DIR = BASE / "visualizations"
OUTPUT_DIR.mkdir(exist_ok=True)

def load_and_clean(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df = df.dropna(how="all").drop_duplicates().copy()
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
    numeric_cols = [
        "Estimated Unemployment Rate (%)",
        "Estimated Employed",
        "Estimated Labour Participation Rate (%)",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.sort_values(["Date", "Region", "Area"])

def main():
    df = load_and_clean(DATA_PATH)
    monthly = (df.groupby("Date").agg(
        unemployment_rate=("Estimated Unemployment Rate (%)", "mean"),
        employed=("Estimated Employed", "mean"),
        labour_participation=("Estimated Labour Participation Rate (%)", "mean"),
    ).reset_index())
    area = (df.groupby("Area").agg(
        unemployment_rate=("Estimated Unemployment Rate (%)", "mean"),
        employed=("Estimated Employed", "mean"),
        labour_participation=("Estimated Labour Participation Rate (%)", "mean"),
    ).reset_index())
    region = (df.groupby("Region").agg(
        unemployment_rate=("Estimated Unemployment Rate (%)", "mean"),
        labour_participation=("Estimated Labour Participation Rate (%)", "mean"),
    ).sort_values("unemployment_rate", ascending=False))

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["Date"], monthly["unemployment_rate"], marker="o")
    plt.axvline(pd.Timestamp("2020-03-31"), linestyle="--")
    plt.title("Monthly Average Unemployment Rate")
    plt.xlabel("Date"); plt.ylabel("Average unemployment rate (%)")
    plt.xticks(rotation=45); plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_unemployment_trend.png", dpi=160); plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(area["Area"], area["unemployment_rate"])
    plt.title("Average Unemployment Rate: Rural vs Urban")
    plt.xlabel("Area"); plt.ylabel("Average unemployment rate (%)")
    plt.tight_layout(); plt.savefig(OUTPUT_DIR / "rural_vs_urban.png", dpi=160); plt.close()

    region_plot = region.sort_values("unemployment_rate")
    plt.figure(figsize=(10, 8))
    plt.barh(region_plot.index, region_plot["unemployment_rate"])
    plt.title("Average Unemployment Rate by Region")
    plt.xlabel("Average unemployment rate (%)")
    plt.tight_layout(); plt.savefig(OUTPUT_DIR / "region_unemployment.png", dpi=160); plt.close()

    covid = monthly[monthly["Date"] >= pd.Timestamp("2020-01-31")]
    plt.figure(figsize=(9, 5))
    plt.plot(covid["Date"], covid["unemployment_rate"], marker="o")
    plt.axvline(pd.Timestamp("2020-03-31"), linestyle="--")
    plt.title("Unemployment Rate During Early COVID-19 Period")
    plt.xlabel("Date"); plt.ylabel("Average unemployment rate (%)")
    plt.xticks(rotation=45); plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "covid_period.png", dpi=160); plt.close()

    print("Rows after cleaning:", len(df))
    print("Regions:", df["Region"].nunique())
    print("Date range:", df["Date"].min().date(), "to", df["Date"].max().date())
    print("\nOverall unemployment rate:", round(df["Estimated Unemployment Rate (%)"].mean(), 2), "%")
    print("\nAverage unemployment rate by area:")
    print(area[["Area", "unemployment_rate"]].round(2).to_string(index=False))
    print("\nTop five regions by average unemployment rate:")
    print(region.head(5).round(2).to_string())
    print("\nCorrelation matrix:")
    print(df[["Estimated Unemployment Rate (%)", "Estimated Employed", "Estimated Labour Participation Rate (%)"]].corr().round(3))

if __name__ == "__main__":
    main()
