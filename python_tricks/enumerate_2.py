# using enumerate to change negative numbers to 0

numbers  = [1, 2, -3, -4, 5, 6, -7, -8, 9, 0]

for index, number in enumerate(numbers):
    if number < 0 :
        numbers[index] = 0

print(numbers)