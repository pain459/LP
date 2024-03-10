# Script to calculate factorial.
def factorial_test(n):
    if n == 0:
        return 1
    else:
        return n * factorial_test(n - 1)

# result = factorial(100)
# print(result)