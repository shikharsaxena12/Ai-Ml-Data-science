import pandas as pd

# ===== PANDAS DATA EXPLORATION =====
data = pd.read_csv("house_price.csv")
n = 5

print("--- DATA PREVIEW ---")
print(data.head(n))  # first n records
print(data.tail(n))  # last n records

print("\n--- DATA STATISTICS ---")
print(data.describe())  # statistical summary
print(data.shape)  # (rows, columns)
print(data.columns)  # column names
print(data.dtypes)  # data types
print(data.info())  # comprehensive info
print(data.isnull().sum())  # null count per column