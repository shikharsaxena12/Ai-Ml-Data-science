import numpy as np

# ===== ARRAY OPERATIONS =====
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print("--- ARRAY OPERATIONS ---")
print("Original:", arr1)
print("Transpose:", arr1.T)
print("Flatten:", arr1.flatten())
print("Reshape:", arr1.reshape(3,2))