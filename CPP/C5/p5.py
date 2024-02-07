# accepting integer from the keyboard

try:
    x = int(input("Enter an integer: "))
    print("You entered:", x)

except ValueError:
    print("Invalid input.")