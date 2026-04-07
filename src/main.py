# 1. Load raw dataset
import pandas as pd
df = pd.read_csv("global_fuel_prices_2020_2026.csv")
df.head()

# 2. Exploratory Data Analysis (EDA) - Understand structure and data quality
print(df.info()) # View dataset structure and data types
print(df.describe()) # Summary statistics for numerical columns
print(df.isnull().sum()) # Check for missing values

# 3. Data Cleaning - Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# 4. Verify that date column was successfully converted to datetime format.
df.info()

# 5. Feature engineering and aggregation
df['year'] = df['date'].dt.year
df.groupby('year')['petrol_usd_liter'].mean()

# 6. Data Visualization (Trend Analysis)
import matplotlib.pyplot as plt

df.groupby('year')['petrol_usd_liter'].mean().plot()
plt.title("Average Petrol Price Over Time")
plt.ylabel("USD per Liter")
plt.show()

# 7. AI-Style Insight Generation
year_summary = df.groupby('year')['petrol_usd_liter'].mean()
region_summary = df.groupby('region')['petrol_usd_liter'].mean().sort_values(ascending=False)
subsidy_summary = df.groupby('subsidy_level')['petrol_usd_liter'].mean().sort_values(ascending=False)
income_summary = df.groupby('income_level')['petrol_usd_liter'].mean().sort_values(ascending=False)
tax_corr = df['petrol_usd_liter'].corr(df['tax_percentage'])
brent_corr = df['petrol_usd_liter'].corr(df['brent_crude_usd'])

top_region = region_summary.index[0]
top_region_value = region_summary.iloc[0]
bottom_region = region_summary.index[-1]
bottom_region_value = region_summary.iloc[-1]

high_subsidy = subsidy_summary.index[0]
high_subsidy_value = subsidy_summary.iloc[0]
low_subsidy = subsidy_summary.index[-1]
low_subsidy_value = subsidy_summary.iloc[-1]

top_income = income_summary.index[0]
top_income_value = income_summary.iloc[0]
bottom_income = income_summary.index[-1]
bottom_income_value = income_summary.iloc[-1]

ai_output = f"""
AI Insight Report

Global average petrol prices rose from {year_summary.iloc[0]:.2f} USD/L in {year_summary.index[0]} to {year_summary.iloc[-1]:.2f} USD/L in {year_summary.index[-1]}, indicating that higher fuel costs over this period were not a short-lived spike but part of a broader upward shift.

This increase was not evenly distributed. {top_region} recorded the highest average petrol price at {top_region_value:.2f} USD/L, while {bottom_region} recorded the lowest at {bottom_region_value:.2f} USD/L, suggesting that geography and regional policy frameworks materially shape consumer fuel costs.

Differences across subsidy regimes are also significant. {high_subsidy} countries averaged {high_subsidy_value:.2f} USD/L, compared with {low_subsidy} countries at {low_subsidy_value:.2f} USD/L, indicating that subsidy structures may either cushion or amplify the pass-through of energy market shocks to retail prices.

A similar divide appears across income groups. {top_income} income countries averaged {top_income_value:.2f} USD/L, versus {bottom_income} income countries at {bottom_income_value:.2f} USD/L, suggesting that pump prices reflect not only commodity markets but also fiscal capacity, pricing policy, and energy market design.

The correlation between Brent crude and petrol prices is {brent_corr:.2f}, while the correlation between petrol prices and tax percentage is {tax_corr:.2f}. This implies that retail fuel prices are shaped by both upstream oil market conditions and downstream policy choices such as taxation.

Overall, the dataset suggests that rising petrol prices should be understood not only as an oil story, but as the outcome of a wider system involving crude prices, state intervention, tax policy, and regional energy vulnerability.
"""
print(ai_output)

# 8. Output
Global average petrol prices rose from 1.48 USD/L in 2020 to 2.65 USD/L in 2026, indicating that higher fuel costs over this period were not a short-lived spike but part of a broader upward shift.
This increase was not evenly distributed. Europe recorded the highest average petrol price at 3.70 USD/L, while Middle East recorded the lowest at 1.23 USD/L, suggesting that geography and regional policy frameworks materially shape consumer fuel costs.
Differences across subsidy regimes are also significant. Low countries averaged 3.45 USD/L, compared with Very High countries at 0.15 USD/L, indicating that subsidy structures may either cushion or amplify the pass-through of energy market shocks to retail prices.
A similar divide appears across income groups. High income countries averaged 3.55 USD/L, versus Low income countries at 1.39 USD/L, suggesting that pump prices reflect not only commodity markets but also fiscal capacity, pricing policy, and energy market design.
The correlation between Brent crude and petrol prices is 0.26, while the correlation between petrol prices and tax percentage is 0.52. This implies that retail fuel prices are shaped by both upstream oil market conditions and downstream policy choices such as taxation.
Overall, the dataset suggests that rising petrol prices should be understood not only as an oil story, but as the outcome of a wider system involving crude prices, state intervention, tax policy, and regional energy vulnerability.
