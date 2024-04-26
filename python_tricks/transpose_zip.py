# Transposing a list of lists using zip

x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

transposed = list(zip(*x))

for i in transposed:
    print(i)