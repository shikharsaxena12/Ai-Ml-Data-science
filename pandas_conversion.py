import numpy as np
import pandas as pd

# ===== PANDAS CONVERSION =====
data = pd.read_csv("house_price.csv")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print("--- PANDAS CONVERSION ---")
dd = pd.DataFrame(arr1)
print("DataFrame from array:")
print(dd)

ds = pd.Series(data['Price'])
print("\nSeries from CSV:")
print(ds.head())