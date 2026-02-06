import numpy as np

# ============================================================
'''
TOPIC 1: ARRAY CREATION
SUBTOPICS: zeros, ones, range, random
INPUT: Shape / range values
OUTPUT: Different initialized arrays

📌 Rule to remember:
np.function((rows, columns))
So 3×3 = (3,3)

EXPECTED OUTPUT (random will vary):
Zeros:
 [[0. 0. 0.]
  [0. 0. 0.]]
Ones:
 [[1. 1.]
  [1. 1.]]
Range: [0 2 4 6 8]
Random: 2x2 matrix with values between 0 and 1
'''
print("TOPIC 1: ARRAY CREATION")

print("Zeros:\n", np.zeros((2,3)))
print("Ones:\n", np.ones((2,2)))
print("Range:", np.arange(0,10,2))
print("Random:\n", np.random.rand(2,2))
print("="*60)


# ============================================================
'''
TOPIC 2: SHAPE & RESHAPING
SUBTOPICS: shape, reshape, transpose
INPUT: 1D array
OUTPUT: Matrix forms

EXPECTED OUTPUT:
Shape: (6,)
Reshaped:
 [[1 2 3]
  [4 5 6]]
Transpose:
 [[1 4]
  [2 5]
  [3 6]]
'''
print("TOPIC 2: RESHAPING")

a = np.array([1,2,3,4,5,6])
b = a.reshape(2,3)
print("Shape:", a.shape)
print("Reshaped:\n", b)
print("Transpose:\n", b.T)
print("="*60)


# ============================================================
'''
TOPIC 3: ELEMENT-WISE MATH
SUBTOPICS: add, multiply, exp, sqrt
INPUT: Two vectors
OUTPUT: Vectorized operations

EXPECTED OUTPUT:
Add: [5 7 9]
Multiply: [ 4 10 18]
Exp: [ 2.718..., 7.389..., 20.085... ]
Sqrt: [1. 1.414... 1.732...]
'''
print("TOPIC 3: MATH OPS")

x = np.array([1,2,3])
y = np.array([4,5,6])
print("Add:", x+y)
print("Multiply:", x*y)
print("Exp:", np.exp(x))
print("Sqrt:", np.sqrt(x))
print("="*60)


# ============================================================
'''
TOPIC 4: MATRIX / LINEAR ALGEBRA
SUBTOPICS: dot product, inverse, norm
INPUT: Matrices
OUTPUT: ML core math

EXPECTED OUTPUT:
Dot Product:
 [[19 22]
  [43 50]]
Inverse of A:
 [[-2.   1. ]
  [ 1.5 -0.5]]
Norm of A: 5.477...
'''
print("TOPIC 4: LINEAR ALGEBRA")

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("Dot Product:\n", A @ B)
print("Inverse of A:\n", np.linalg.inv(A))
print("Norm of A:", np.linalg.norm(A))
print("="*60)


# ============================================================
'''
TOPIC 5: STATISTICS
SUBTOPICS: mean, std, sum, argmax
INPUT: Dataset array
OUTPUT: Data insights

EXPECTED OUTPUT:
Mean: 30.0
Std: 14.142...
Sum: 150
Index of Max: 4
'''
print("TOPIC 5: STATISTICS")

data = np.array([10,20,30,40,50])
print("Mean:", np.mean(data))
print("Std:", np.std(data))
print("Sum:", np.sum(data))
print("Index of Max:", np.argmax(data))
print("="*60)


# ============================================================
'''
TOPIC 6: INDEXING & FILTERING
SUBTOPICS: slicing, boolean mask, where
INPUT: Array
OUTPUT: Filtered results

EXPECTED OUTPUT:
Slice: [ 5 10 15]
Greater than 10: [15 20]
Where >10: (array([3, 4]),)
'''
print("TOPIC 6: INDEXING")

arr = np.array([1,5,10,15,20])
print("Slice:", arr[1:4])
print("Greater than 10:", arr[arr>10])
print("Where >10:", np.where(arr>10))
print("="*60)


# ============================================================
'''
TOPIC 7: BROADCASTING
SUBTOPICS: vector + matrix
INPUT: Column and row vectors
OUTPUT: Broadcasted matrix

EXPECTED OUTPUT:
[[11 21 31]
 [12 22 32]
 [13 23 33]]
'''
print("TOPIC 7: BROADCASTING")

col = np.array([[1],[2],[3]])
row = np.array([10,20,30])
print("Broadcast Result:\n", col + row)
print("="*60)
