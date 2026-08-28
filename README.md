# Car Market Analysis

## Project Overview
This Python script analyzes historical used-car market data from Car Dekho to identify key factors influencing vehicle resale prices. It cleans the raw data, performs feature engineering, and generates high-resolution data visualizations to help buyers, sellers, and dealers evaluate fair market value[cite: 1].

---

## What the Code Does

* **Data Loading & Preprocessing:** Reads the dataset into a Pandas DataFrame and creates a new `Vehicle_Age` feature based on the manufacturing year[cite: 1].
* **Price Relationship Analysis:** Generates a scatter plot comparing original showroom prices (`Present_Price`) against resale prices (`Selling_Price`), categorized by fuel type and transmission[cite: 1].
* **Category Breakdown:** Creates box plots comparing selling price distributions across different fuel types (Petrol, Diesel, CNG) and transmission models (Manual vs. Automatic)[cite: 1].
* **Depreciation Tracking:** Plots a line chart showing how selling prices decay as vehicle age increases[cite: 1].
* **Correlation Mapping:** Builds a numerical heatmap highlighting relationships between vehicle age, mileage, original price, and selling price[cite: 1].
* **Automated Image Export:** Saves all generated charts as high-resolution PNG image files directly to your folder for immediate use in presentation slides[cite: 1].

---

## Prerequisites & Installation

Run the following command in your terminal or prompt to install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```
##How to Run

Ensure 1776311302-P3-Car Market Trends Analysis with Car Dekho Data.csv is in the same directory as your Python script

Execute the script using:

```bash
python car_market_analysis.py
```
