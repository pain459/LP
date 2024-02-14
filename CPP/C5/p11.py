# Python program to accept 3 numbers in a same line

a, b, c = [int(i) for i in input("Enter 3 numbers separated by space: ").split()]
print(f'Entered numbers are {a}, {b} & {c}.')