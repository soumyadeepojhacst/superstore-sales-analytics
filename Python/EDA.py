import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, '..', 'data', 'Superstore_Cleaned.csv')

df = pd.read_csv(file_path,parse_dates=['Order Date','Ship Date'])

sns.set_style('whitegrid')

category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=category_profit.index,y=category_profit.values)
plt.title('Total profit by category')
plt.ylabel('Profit')
plt.savefig('chart_profile_by_category.png')
plt.close()

subcat_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values()
plt.figure(figsize=(10,8))
sns.barplot(x=subcat_profit.values, y=subcat_profit.index)
plt.title('Profit by Sub-Category (Lowest to Highest)')
plt.savefig('chart_profit_by_subcategory.png')
plt.close()

first_month = df['Order Date'].min().to_period('M')
last_month = df['Order Date'].max().to_period('M')
df_trend = df[
    (df['Order Date'].dt.to_period('M') != first_month) &
    (df['Order Date'].dt.to_period('M') != last_month)
]
monthly_sales = df_trend.groupby(df_trend['Order Date'].dt.to_period('M'))['Sales'].sum()
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend (May 2023 - Mar 2025)')
plt.ylabel('Sales')
plt.xlabel('Order Date')
plt.savefig('chart_monthly_sales_trend.png')
plt.close()


region_perf = df.groupby('Region')[['Sales','Profit']].sum().sort_values('Profit',ascending=False)
plt.figure(figsize=(10,8))
region_perf.plot(kind='bar')
plt.title('Sales & Profit by Region')
plt.savefig('chart_region_performance.png')
plt.close()

df_filtered = df[(df['Profit Margin'] >= -100) & (df['Profit Margin'] <= 100)]
print(f"Rows before: {len(df)}, Rows after filtering: {len(df_filtered)}")
correlation_margin = df_filtered['Discount'].corr(df_filtered['Profit Margin'])
print(f"Correlation (filtered): {correlation_margin:.3f}")
plt.figure(figsize=(8,5))
sns.regplot(data=df_filtered, x='Discount', y='Profit Margin', 
            scatter_kws={'alpha':0.15, 's':15}, line_kws={'color':'red'})
plt.title('Discount vs Profit Margin (outliers removed)')
plt.savefig('chart_discount_vs_margin.png')
plt.close()

segment_analysis = df.groupby('Segment').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Avg_Order_Value=('Sales', 'mean'),
    Order_Count=('Order ID', 'nunique')
).sort_values('Total_Profit', ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=segment_analysis.index, y=segment_analysis['Total_Profit'])
plt.title('Total Profit by Customer Segment')
plt.ylabel('Profit')
plt.savefig('chart_profit_by_segment.png')
plt.close()


top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_customers)

