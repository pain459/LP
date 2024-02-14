# Convert numbers from other systems to decimal numbers

str1 = input("Enter hexadecimal number: ")
n = int(str1, 16)
print("Hexadecimal to Decimal =", n)

str2 = input("Enter a octal number: ")
n = int(str2, 8)
print("Octal to Decimal =", n)

str3 = input("Enter a binary number: ")
n = int(str3, 2)
print("Binary to Decimal =", n)

a, b = [int(i) for i in input("Enter 2 numbers: ").split()]
print(f'The entered numbers are {a} and {b}')