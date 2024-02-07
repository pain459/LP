# Find sum and product of 2 numbers

try:
    x = int(input("Enter int num1: "))
    y = int(input("Enter int num2: "))

    print(f"Sum of {x} & {y} is {x+y}")
    print(f"Product of {x} & {y} is {x*y}")

except ValueError:
    print("Invalid entries detected.")
