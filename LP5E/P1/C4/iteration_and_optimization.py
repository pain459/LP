# Using comprehensions
print([i ** 2 for i in range(1, 11)])

# traditional for loop
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)