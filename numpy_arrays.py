import numpy as np

# ===== NUMPY ARRAY CREATION =====
print("--- ARRAY CREATION ---")
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