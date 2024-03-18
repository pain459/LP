# lambda to find the biggest of 2 numbers.
x = lambda a, b: a if a > b else b
# i, j = 34, 56
i, j = [int(k) for k in input("Enter 2 numbers separated by comma: ").split(',')]
result = x(i, j)
print(f'Greater out of {i} and {j} is {result}')