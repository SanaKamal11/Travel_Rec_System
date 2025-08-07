# 01_eda.ipynb

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure plots render in the notebook

# Load the dataset
df = pd.read_csv('data/merged_travel_data.csv')

# Basic overview
df.info()
df.describe()
print("\nMissing values:")
print(df.isnull().sum())

# Histogram: AvgTemp_C
plt.figure(figsize=(8, 5))
sns.histplot(df['AvgTemp_C'].dropna(), kde=True)
plt.title("Distribution of Average Temperature (°C)")
plt.xlabel("AvgTemp_C")
plt.ylabel("Frequency")
plt.show()

# Histogram: Monthly Cost
plt.figure(figsize=(8, 5))
sns.histplot(df['MonthlyCost'].dropna(), kde=True)
plt.title("Monthly Cost of Living")
plt.xlabel("Monthly Cost (USD)")
plt.ylabel("Frequency")
plt.show()

# Histogram: Safety Index
plt.figure(figsize=(8, 5))
sns.histplot(df['Safety Index'].dropna(), kde=True)
plt.title("Distribution of Safety Index")
plt.xlabel("Safety Index")
plt.ylabel("Frequency")
plt.show()

# Bar chart: Top 10 countries by number of cities
plt.figure(figsize=(10, 6))
df['Country'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries by Number of Cities")
plt.xlabel("Country")
plt.ylabel("Number of Cities")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[['AvgTemp_C', 'MonthlyCost', 'Safety Index']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Features")
plt.show()