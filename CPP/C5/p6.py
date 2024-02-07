# program to accept floating numbers as input

try:
    x = float(input("Enter a float number: "))
    print("You entered:", x)

except ValueError:
    print("Invalid entry.")