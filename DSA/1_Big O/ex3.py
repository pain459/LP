# Complexity of O(n^2) demo.

def print_numbers(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_numbers(10)