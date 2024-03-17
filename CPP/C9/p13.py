# passing an integer to a function
def modify(x):
    """Reassign a value to the variable"""
    x = 15
    print(x, id(x))


# call modify and pass x
x = 10
modify(x)
print(x, id(x))