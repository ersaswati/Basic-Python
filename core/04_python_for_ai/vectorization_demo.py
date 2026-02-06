import numpy as np
import time

arr = np.random.rand(1_000_000)

start = time.time()
result = arr * 2
print("Vectorized time:", time.time() - start)