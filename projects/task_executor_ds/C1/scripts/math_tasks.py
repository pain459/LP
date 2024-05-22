import numpy as np

def recursive_matrix_multiplication(size=50, depth=3):
    """Performs recursive matrix multiplication for increased complexity."""
    if depth == 0:
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)
        return np.dot(A, B)
    else:
        A = recursive_matrix_multiplication(size, depth - 1)
        B = recursive_matrix_multiplication(size, depth - 1)
        if A.shape != B.shape or A.shape[0] != A.shape[1]:
            raise ValueError("Matrices are not square or mismatched sizes.")
        return np.dot(A, B)

def recursive_matrix_inversion(size=30, depth=3):
    """Recursively inverts matrices to increase the computation demand."""
    if depth == 0:
        A = np.random.rand(size, size)
        return np.linalg.inv(A)
    else:
        A = recursive_matrix_inversion(size, depth - 1)
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix is not square")
        return np.linalg.inv(A)

import numpy as np

def recursive_solve_linear_system(size=30, depth=3):
    """Solves linear systems recursively to simulate heavy computational tasks."""
    if depth == 0:
        A = np.random.rand(size, size)
        b = np.random.rand(size)
        return np.linalg.solve(A, b)
    else:
        A, b = recursive_prepare_solve_linear_system(size, depth - 1)
        if A.shape[0] != A.shape[1] or A.shape[0] != size:
            raise ValueError("Matrix A is not square or does not match expected size")
        return np.linalg.solve(A, b)

def recursive_prepare_solve_linear_system(size=30, depth=3):
    """Prepares matrices for solving linear systems, ensuring they are square and match expected dimensions."""
    if depth == 0:
        A = np.random.rand(size, size)
        b = np.random.rand(size)
        return A, b
    else:
        A, b = recursive_prepare_solve_linear_system(size, depth - 1)
        if A.shape[0] != A.shape[1] or A.shape[0] != size:
            raise ValueError("Matrix A is not square or does not match expected size during preparation")
        return A, b


def describe_task(result, size, depth):
    """Generate a description of the task completed, including its size and depth of recursion."""
    return f"Task with size {size} and depth {depth} completed."
