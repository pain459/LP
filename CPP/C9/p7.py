# a function returns two results
def sum_sub(a, b):
    """This function returns the results of
    addition and subtraction of a, b"""
    c = a + b
    d = a - b
    return c, d


# Get the results from the sum_sub() function
x, y = sum_sub(10, 30)
# display the results
print("Result of addition:", x)
print("Result of subtraction:", y)
