# Handling assertion error
try:
    to_validate = int(input("Enter a number greater than 0: "))
    assert to_validate > 0, "Entered number is less than 0"
    print("U entered", to_validate)
except AssertionError as e:
    print("Wrong input entered.", e) # This e is going to bring the message from the top assert statement.
except ValueError:
    print("Input not an integer.")
