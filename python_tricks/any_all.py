# Check if any number in the list is even

num = [1, 2, 3, 4, 5, 6, 7]
print(any(i % 2 == 0 for i in num))

# check if all numbers in the list are even
print(all(i % 2 == 0 for i in num))