# Recursion in python
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result


# Find the factorial for first 10 numbers
for i in range(1, 11):
    print(f'Factorial of {i} is {factorial(i)}')