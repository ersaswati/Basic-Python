import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Mean:", np.mean(a))

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Shape:", arr.shape)
print("Column mean:", arr.mean(axis=0))
print("Row mean:", arr.mean(axis=1))

print("Broadcasting:", arr + 10)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Dot product:\n", np.dot(A, B))