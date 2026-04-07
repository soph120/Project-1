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
summary = df.groupby('year')['petrol_usd_liter'].mean()
trend_start = summary.iloc[0]
trend_end = summary.iloc[-1]
total_change = round(trend_end - trend_start, 2)
pct_change = round(((trend_end - trend_start) / trend_start) * 100, 1)

yearly_change = summary.diff()
largest_increase_year = yearly_change.idxmax()
largest_increase_value = round(yearly_change.max(), 2)

largest_drop_year = yearly_change.idxmin()
largest_drop_value = round(yearly_change.min(), 2)

highest_region = df.groupby('region')['petrol_usd_liter'].mean().idxmax()
highest_region_value = round(df.groupby('region')['petrol_usd_liter'].mean().max(), 2)

corr = round(df['petrol_usd_liter'].corr(df['brent_crude_usd']), 2)

ai_output = f"""
AI Insight Report

From 2020 to 2026, average global petrol prices increased from {trend_start:.2f} to {trend_end:.2f} USD/L, a net change of {total_change:.2f} USD/L ({pct_change}%).

The sharpest annual increase occurred in {largest_increase_year}, when average petrol prices rose by {largest_increase_value:.2f} USD/L. The largest decline occurred in {largest_drop_year}, with a drop of {abs(largest_drop_value):.2f} USD/L.

On a regional basis, {highest_region} recorded the highest average petrol price at {highest_region_value:.2f} USD/L.

The correlation between Brent crude prices and petrol prices is {corr}, suggesting {"a strong" if abs(corr) >= 0.7 else "a moderate" if abs(corr) >= 0.4 else "a weak"} relationship between crude oil markets and retail fuel prices.

Overall, the data suggests that fuel price movements were shaped by a combination of energy market conditions, possible geopolitical disruptions, and domestic pricing structures such as taxes and subsidies.

If current trends persist, fuel prices may continue to experience upward pressure, particularly in regions with high taxation or limited subsidies.
"""

print(ai_output)
