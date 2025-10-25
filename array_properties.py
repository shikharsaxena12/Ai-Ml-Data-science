import numpy as np

# ===== ARRAY PROPERTIES =====
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print("--- ARRAY PROPERTIES ---")
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)
print("Item size:", arr1.itemsize)
print("Total bytes:", arr1.nbytes)