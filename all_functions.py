import numpy as np
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

# ===== NUMPY ARRAY CREATION =====
print("\n--- ARRAY CREATION ---")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 1:", arr1)
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print("Array 2:", arr2)
print("Zeros:", np.zeros((2,3)))
print("Ones:", np.ones((2,3)))
print("Identity:", np.eye(3))
print("Random:", np.random.rand(2,3))
print("Range:", np.arange(10))
print("Linspace:", np.linspace(0, 10, 5))

# ===== ARRAY PROPERTIES =====
print("\n--- ARRAY PROPERTIES ---")
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)
print("Item size:", arr1.itemsize)
print("Total bytes:", arr1.nbytes)

# ===== ARRAY OPERATIONS =====
print("\n--- ARRAY OPERATIONS ---")
print("Transpose:", arr1.T)
print("Flatten:", arr1.flatten())
print("Reshape:", arr1.reshape(3,2))

# ===== MATHEMATICAL FUNCTIONS =====
print("\n--- MATH FUNCTIONS ---")
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))
print("Std:", np.std(arr1))
print("Variance:", np.var(arr1))
print("Sort:", np.sort(arr1))
print("Unique:", np.unique(arr1))

# ===== ARRAY ARITHMETIC =====
print("\n--- ARRAY ARITHMETIC ---")
print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)
print("Matrix multiply:", np.dot(arr1, arr2.T))
print("Concatenate:", np.concatenate([arr1, arr2]))

# ===== PANDAS CONVERSION =====
print("\n--- PANDAS CONVERSION ---")
dd = pd.DataFrame(arr1)
print("DataFrame from array:")
print(dd)
ds = pd.Series(data['Price'])
print("\nSeries from CSV:")
print(ds.head())