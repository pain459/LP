# Using assert to filter out the entered number

x = int(input("Enter a number greater than 0: "))
assert x > 0, "Wrong number entered"
print("U entered", x)