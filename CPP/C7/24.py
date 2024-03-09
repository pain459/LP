# Mathematical operations on arrays
import numpy as np

# Create an array
arr = np.array([10, 20, 30.5, -40])
print("Original array:", arr)

# Math operations
print("After adding 5:", arr+5)
print("After subtracting 5:", arr-5)
print("After multiplying 5:", arr*5)
print("After dividing 5:", arr/5)
print("After modulus with 5:", arr%5)

# Using arrays in expressions
print("Expression value:", (arr+5)**2-10)

# Performing math functions
print("Sin values:", np.sin(arr))
print("Cos values:", np.cos(arr))
print("Tan values:", np.tan(arr))
print("Biggest element:", np.max(arr))
print("Smallest element:", np.min(arr))
print("Sum of all elements:", np.sum(arr))
print("Average of all elements:", np.average(arr))