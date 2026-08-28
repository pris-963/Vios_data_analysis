import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"

# 1. Load Dataset
df = pd.read_csv("1776311302-P3-Car Market Trends Analysis with Car Dekho Data.csv")

# Feature Engineering
current_year = 2026
df["Vehicle_Age"] = current_year - df["Year"]

print("--- DATA SUMMARY ---")
print(df.info())
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# ---------------------------------------------------------
# Visualization 1: Distribution of Selling Price vs Present Price
# ---------------------------------------------------------
plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=df,
    x="Present_Price",
    y="Selling_Price",
    hue="Fuel_Type",
    style="Transmission",
    s=70,
)
plt.title(
    "Selling Price vs. Present Price by Fuel Type & Transmission",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Present Price (in Lakhs)", fontsize=12)
plt.ylabel("Selling Price (in Lakhs)", fontsize=12)
plt.tight_layout()
plt.savefig("1_selling_vs_present_price.png", dpi=300)
plt.show()

# ---------------------------------------------------------
# Visualization 2: Selling Price by Fuel Type and Transmission
# ---------------------------------------------------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(data=df, x="Fuel_Type", y="Selling_Price", palette="Set2")
plt.title("Selling Price by Fuel Type", fontsize=12, fontweight="bold")
plt.xlabel("Fuel Type", fontsize=10)
plt.ylabel("Selling Price (in Lakhs)", fontsize=10)

plt.subplot(1, 2, 2)
sns.boxplot(data=df, x="Transmission", y="Selling_Price", palette="Set1")
plt.title("Selling Price by Transmission", fontsize=12, fontweight="bold")
plt.xlabel("Transmission", fontsize=10)
plt.ylabel("Selling Price (in Lakhs)", fontsize=10)

plt.tight_layout()
plt.savefig("2_price_by_fuel_and_transmission.png", dpi=300)
plt.show()

# ---------------------------------------------------------
# Visualization 3: Impact of Vehicle Age on Selling Price
# ---------------------------------------------------------
plt.figure(figsize=(10, 5))
sns.lineplot(
    data=df, x="Vehicle_Age", y="Selling_Price", marker="o", color="crimson"
)
plt.title(
    "Impact of Vehicle Age on Selling Price (Depreciation Trend)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Vehicle Age (Years)", fontsize=12)
plt.ylabel("Selling Price (in Lakhs)", fontsize=12)
plt.tight_layout()
plt.savefig("3_age_vs_selling_price.png", dpi=300)
plt.show()

# ---------------------------------------------------------
# Visualization 4: Correlation Heatmap
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("4_correlation_heatmap.png", dpi=300)
plt.show()
