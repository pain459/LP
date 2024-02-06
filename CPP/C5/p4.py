# Accepting integer from the keyboard

try:
    str1 = input("Enter an integer: ")
    x = int(str1)
    print("Entered integer is:", x)

except ValueError:
    print("Invalid input.")
