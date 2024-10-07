# Using cupy for Array Computations

import cupy as cp
import time

# Define large matrices
size = 5000
a = cp.random.randn(size, size).astype(cp.float32)
b = cp.random.randn(size, size).astype(cp.float32)

# Measure matrix multiplication time
start = time.time()
c = cp.dot(a, b)
cp.cuda.Stream.null.synchronize()  # Ensure all tasks are completed
end = time.time()

print(f"Time taken for matrix multiplication: {end - start:.4f} seconds")
