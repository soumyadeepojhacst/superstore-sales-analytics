import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '..', 'data', 'superstore_excel.csv')

df = pd.read_csv(file_path,encoding='latin1')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.month_name()
df['Order Quarter'] = df['Order Date'].dt.quarter

df['Shipping Days'] = (df['Ship Date']-df['Order Date']).dt.days

df['Profit Margin'] = (df['Profit']/df['Sales'])*100

df.to_csv('Superstore_Cleaned.csv',index=False)




