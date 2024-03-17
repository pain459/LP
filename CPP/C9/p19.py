# Variable length argument demo
def add(farg, *args):
    """to add given numbers"""
    print("Formal argument=", farg)

    sum = 0
    for i in args:
        sum += i

    print("Sum of all numbers:", farg + sum)


add(5, 10)
add(5, 10, 20, 30, 40)
