# program to calculate factorial
def fact(n):
    """Calculate factorial and return the value"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        while n >= 1:
            return n * fact(n - 1)
        n -= 1


x = fact(999)
print(x)
