# Company Purchasing Analytics

A procurement analytics portfolio project built with **Excel, Power BI, and Python** using a synthetic purchasing dataset.

The project demonstrates how purchasing data can be transformed into **procurement KPIs, spend analysis, supplier and buyer insights, interactive dashboards, and management-oriented recommendations**.

## Project Highlights

- Procurement Spend Analysis
- Supplier Analysis
- Buyer Analysis
- Item Analysis
- Category Analysis
- Procurement KPI Development
- Spend Concentration Analysis
- DAX Measures
- Interactive Power BI Reporting
- Management Insights

## Tech Stack

- **Excel** – PivotTables, charts, KPI analysis
- **Power BI** – Power Query, Data Modeling, DAX, Interactive Dashboards
- **Python** – Pandas, Matplotlib

## Repository Structure

```text
data/        Dataset
excel/       Excel analysis
powerbi/     Power BI dashboard
python/      Python scripts
outputs/     Analysis results
images/      Dashboard screenshots
report/      Exported Power BI PDF

Excel Analysis
Spend by Category

Analyzes procurement spend across purchasing categories to identify major cost drivers.

Top Purchased Items

Ranks purchased items based on total procurement spend.

Quantity vs Cost Analysis

The scatter analysis shows a very weak relationship between purchase quantity and total procurement cost.

The calculated R² value is approximately 0.0025, meaning that quantity explains only about 0.25% of the variation in procurement cost.

This suggests that factors such as unit price and product type have a much stronger influence on procurement spend.

Power BI Dashboard

The Power BI report contains six analytical pages:

Executive Overview
Spend Analysis
Supplier Analysis
Item Analysis
Buyer Analysis
Procurement Management Insights
01 — Executive Overview

Key KPIs:

Total Spend
Total Orders
Average Order Value
Weighted Average Unit Price
Total Quantity
Number of Suppliers

Includes a monthly procurement spend trend.

02 — Spend Analysis

Analyzes:

Spend by Category
Top Purchased Items
Spend by Buyer
Spend Distribution
03 — Supplier Analysis

Analyzes:

Top Suppliers by Total Spend
Supplier Spend Share
Supplier Spend Summary

Example DAX:

Supplier Spend Share % =
DIVIDE(
    [Total Spend],
    CALCULATE(
        [Total Spend],
        REMOVEFILTERS(FactPurchases[Supplier])
    ),
    0
)
04 — Item Analysis

Analyzes:

Top Items by Spend
Quantity by Item
Quantity vs Spend
High-value items
05 — Buyer Analysis

Analyzes:

Spend by Buyer
Orders by Buyer
Buyer Spend vs Orders
Buyer Spend Share

Example DAX:

Buyer Spend Share % =
DIVIDE(
    [Total Spend],
    CALCULATE(
        [Total Spend],
        REMOVEFILTERS(FactPurchases[Buyer])
    ),
    0
)
06 — Procurement Management Insights

The final page converts analytical results into management-oriented insights.

It evaluates concentration across:

Categories
Suppliers
Items
Buyers

A simple rule-based framework was created for portfolio purposes:

Indicator	Low	Medium	High
Top Category Share	< 30%	30–50%	> 50%
Top Supplier Share	< 20%	20–35%	> 35%
Top Item Share	< 20%	20–35%	> 35%
Top Buyer Share	< 15%	15–25%	> 25%

The dashboard uses DAX to classify concentration dynamically as Low, Medium, or High.

Example:

Supplier Concentration Level =
SWITCH(
    TRUE(),
    [Top Supplier Share %] > 0.35, "High",
    [Top Supplier Share %] >= 0.20, "Medium",
    "Low"
)

The Management Matrix links findings with:

Business Impact
Recommended Action
Dynamic Priority
Key Business Insights

Current analysis indicates:

The leading category represents approximately 56.2% of total spend
The leading supplier represents approximately 26.5%
The highest-spend item is approximately $472K
The leading buyer represents approximately 7.8% of spend

These are treated as concentration indicators, not complete procurement risk assessments.

Power BI Skills Demonstrated
Power Query
Data Modeling
Date Table
DAX Measures
KPI Cards
Spend Share Analysis
Top-N Analysis
Scatter Analysis
Conditional Formatting
Interactive Filtering
Dynamic Priority Logic
Business Storytelling
Dataset
Dataset: Company Purchasing Dataset
Type: Synthetic Procurement Data
License: CC0 1.0
Source: Kaggle
Original Creator: Shahriar Kabir

Dataset source:

https://www.kaggle.com/datasets/shahriarkabir/company-purchasing-dataset

The original dataset was created by the original author. All analysis, dashboards, DAX measures, interpretations, and management insights in this repository are my own work.

Disclaimer

This project is intended for educational and portfolio purposes only.

The dataset is synthetic and does not represent a real company.

The concentration thresholds and management recommendations used in the Power BI dashboard are project-defined analytical assumptions, not universal procurement standards.

In a real business environment, such thresholds should be adapted to company strategy, category characteristics, supplier markets, operational criticality, and risk appetite.
