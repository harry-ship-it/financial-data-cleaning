import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('financial_data.csv')

print("Original Data:")
print(data.head())

# Step 1: Handle Missing Values
data['stock_price'] = data['stock_price'].fillna(data['stock_price'].mean())
data['revenue'] = data['revenue'].fillna(method='ffill')
data['expenses'] = data['expenses'].fillna(data['expenses'].median())

# Step 2: Detect & Remove Outliers in Stock Prices
Q1 = data['stock_price'].quantile(0.25)
Q3 = data['stock_price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['stock_price'] >= lower_bound) & (data['stock_price'] <= upper_bound)]

# Step 3: Standardize Date Formats
data['date'] = pd.to_datetime(data['date'], errors='coerce')
data = data.dropna(subset=['date'])
data['date'] = data['date'].dt.strftime('%Y-%m-%d')

# Step 4: Convert Currency to USD
exchange_rates = {'USD': 1, 'EUR': 1.1, 'GBP': 1.3}
data['currency'] = data['currency'].fillna('USD')
data['stock_price'] = data.apply(lambda row: row['stock_price'] * exchange_rates[row['currency']], axis=1)
data['currency'] = 'USD'

# Step 5: Save Cleaned Data
cleaned_file_path = 'cleaned_financial_data.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
