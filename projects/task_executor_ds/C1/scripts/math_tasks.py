import numpy as np

def matrix_multiplication(size=100):
    """Performs matrix multiplication on two randomly generated matrices of specified size."""
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    result = np.dot(A, B)
    return f"Matrix multiplication of size {size}x{size} completed."

def matrix_inversion(size=50):
    """Inverts a randomly generated square matrix of specified size."""
    A = np.random.rand(size, size)
    result = np.linalg.inv(A)
    return f"Matrix inversion of size {size}x{size} completed."

def solve_linear_system(size=50):
    """Solves a linear system Ax = b where A is a square matrix and b is a vector."""
    A = np.random.rand(size, size)
    b = np.random.rand(size)
    result = np.linalg.solve(A, b)
    return f"Solution of linear system of size {size} found."
