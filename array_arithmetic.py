import numpy as np

# ===== ARRAY ARITHMETIC =====
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

print("--- ARRAY ARITHMETIC ---")
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)
print("Matrix multiply:", np.dot(arr1, arr2.T))
print("Concatenate:", np.concatenate([arr1, arr2]))