# 💰 Financial Data Cleaning

## 📌 Overview
This project showcases **data cleaning techniques** applied to financial data.  
It processes raw stock price, revenue, and expense data by handling missing values, removing outliers, and ensuring standard formats.

## 🚀 Features
✅ Handle **missing values** (fill stock prices with mean, revenue forward-fill, expenses with median).  
✅ Detect and **remove outliers** (unrealistic stock price fluctuations).  
✅ Standardize **date formats** (convert all dates to `YYYY-MM-DD`).  
✅ Convert **currency values** (USD, EUR, GBP) into a uniform format (USD).  
✅ Export **cleaned data** for analysis.  

## 📂 Files in This Project
| File Name                     | Description                                      |
|--------------------------------|--------------------------------------------------|
| `financial_data_cleaning.py`   | Python script that processes raw financial data. |
| `financial_data.csv`           | Sample raw dataset before cleaning.              |
| `cleaned_financial_data.csv`   | Output file with cleaned, structured data.       |

## ⚙️ How to Run
1. **Download the script and dataset** (`financial_data_cleaning.py` & `financial_data.csv`).
2. Open a **Terminal or Command Prompt** in the project folder.
3. Run the script:
   ```bash
   python financial_data_cleaning.py

