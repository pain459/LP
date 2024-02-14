# 3 numbers entered with seperator , and give the added result

a, b, c = [int(i) for i in input("Enter 3 numbers separated by ',': ").split(',')]
print(f'Entered numbers are {a}, {b} & {c}.')
print("Sum is =", a+b+c)