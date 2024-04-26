# applying function using map in the list of iterables
x = [1, 2, 3, 4, 5, 6]

# square each number using map() and a lambda function
squared_numbers = list(map(lambda i : i ** 2, x))

print(squared_numbers)