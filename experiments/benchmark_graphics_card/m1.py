# PyCUDA for GPU Computation Benchmarking


import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np
import pycuda.gpuarray as gpuarray
from pycuda.elementwise import ElementwiseKernel
import time

# Create a large random array
size = 10**7
a = np.random.randn(size).astype(np.float32)
b = np.random.randn(size).astype(np.float32)

# Transfer data to the GPU
a_gpu = gpuarray.to_gpu(a)
b_gpu = gpuarray.to_gpu(b)
result_gpu = gpuarray.empty_like(a_gpu)

# Define a simple kernel to add two arrays
add_kernel = ElementwiseKernel(
    "float *a, float *b, float *result",
    "result[i] = a[i] + b[i]",
    "add"
)

# Run the kernel and measure time
start = time.time()
add_kernel(a_gpu, b_gpu, result_gpu)
cuda.Context.synchronize()  # Ensure all tasks are completed
end = time.time()

print(f"Time taken for GPU computation: {end - start:.4f} seconds")
