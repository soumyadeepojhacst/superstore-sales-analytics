
# Superstore Sales Analytics Project

An end-to-end data analysis project covering the full pipeline: **data cleaning
(Python) → database querying (SQL) → business reporting (Excel) →
interactive dashboarding (Power BI)**.

## Project Overview

This project analyzes a retail Superstore dataset (5,000 orders) to answer
six core business questions using four different tools, showing the same
findings validated consistently across the entire stack.

## Tech Stack

- **Python** (pandas, matplotlib, seaborn) — data cleaning, feature
  engineering, exploratory data analysis
- **MySQL** — relational database, analytical queries using GROUP BY,
  window functions (RANK), CTEs, and CASE-based binning
- **Excel** — pivot tables, calculated fields, and a one-page dashboard
  with KPI cards
- **Power BI** — two-page interactive dashboard with DAX measures and
  slicers

## Dataset

Superstore sales dataset — 5,000 rows, 15 original columns including
Order Date, Ship Date, Region, Category, Sub-Category, Customer, Sales,
Discount, and Profit.

## Business Questions & Key Insights

**1. Which product category/sub-category generates the most profit — and
are any actually losing money?**
All three categories generate similar total profit (Office Supplies and
Furniture ~755K, Technology ~730K). At the sub-category level, Tables and
Chairs are the most profitable (~195K each), while Computers and Storage
are the least profitable (~130-135K). No sub-category runs at a loss.

**2. How do sales trend over time — are there seasonal spikes?**
Monthly sales fluctuate between ~440K and ~595K over the two-year period
(May 2023–March 2025) with no strong or consistent seasonal pattern.
Incomplete boundary months were identified and excluded to avoid a
misleading trend line.

**3. Which region performs best/worst in sales and profit?**
South leads in both sales (~3.25M) and profit (~575K), followed closely
by West, Central, and East. All four regions convert sales to profit at
a similar rate (~17-18% margin) — no region is significantly
underperforming.

**4. Who are the top 10 customers by revenue, and what % of total sales
do they represent?**
The top 10 customers (led by Michael Williams at $13,947) collectively
represent approximately 0.8% of total company revenue — a healthy sign
that the business isn't overly dependent on a small group of customers.

**5. Does higher discount lead to lower profit?**
No. Testing both raw profit and profit margin, correlation with discount
rate was close to zero. Average profit margin stayed within a narrow
17-21% band across every discount range from 0% to 50%, indicating
discount level is not a meaningful driver of profitability in this
dataset.

**6. Which customer segment is most profitable?**
Home Office is the most profitable segment (~775K total profit, 34.6%
share), slightly ahead of Corporate and Consumer (both ~730K, nearly
identical).

## Project Structure

```
├── data/       Cleaned dataset used across all tools
├── python/     Data cleaning & EDA script
├── sql/        Database schema + analysis queries
├── excel/      Pivot table report & dashboard
├── powerbi/    Interactive .pbix dashboard
└── screenshots/  Visuals of dashboards and charts
```

## Dashboards

### Power BI — Executive Summary

![Executive Summary](screenshots/dashboard_page1.png)

### Power BI — Customer & Segment Analysis

![Customer Analysis](screenshots/dashboard_page2.png)

### Excel Report Dashboard

![Excel Dashboard](screenshots/excel_dashboard.png)

## How to Reproduce This Project

1. Clone this repository
2. Run `python/cleaning_data.py` on the raw dataset to generate the
   cleaned CSV
3. Load the cleaned CSV into MySQL using the schema and `LOAD DATA INFILE` commands in `sql/analysis_queries.sql`
4. Run the analysis queries in MySQL Workbench
5. Open `excel/Superstore_Report.xlsx` to view the pivot table report
6. Open `powerbi/Superstore_Dashboard.pbix` in Power BI Desktop
   (requires a local MySQL connection matching the `superstore_db`
   schema) to view the interactive dashboard

## Author

Built as a portfolio project to demonstrate an end-to-end analytics
workflow spanning Python, SQL, Excel, and Power BI.
