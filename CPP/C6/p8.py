# display a numeric digit in words

try:
    x = int(input("Enter a digit between or equal to zero and nine: "))
    if 0 <= x <= 9:
        if x == 0:
            print("ZERO")
        elif x == 1:
            print("ONE")
        elif x == 2:
            print("TWO")
        elif x == 3:
            print("THREE")
        elif x == 4:
            print("FOUR")
        elif x == 5:
            print("FIVE")
        elif x == 6:
            print("SIX")
        elif x == 7:
            print("SEVEN")
        elif x == 8:
            print("EIGHT")
        elif x == 9:
            print("NINE")
    else:
        print("Value not in range.")
except ValueError:
    print("Invalid entry!")