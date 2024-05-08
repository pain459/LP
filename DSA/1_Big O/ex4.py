# demo of dropping non-dominant in Big-O notation.

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)    # O(n^2)
    for k in range(n):
        print(k)           # O(n)


print_items(10)