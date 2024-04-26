# Filter a list based on condition.

numbers = [1, 7, 3, 9, 5, 2, 8]

# Filter out numbers greater than 5 using filter and lambda

filtered_numbers = list(filter(lambda x: x > 5, numbers))

print(filtered_numbers)