# decorator increases the value to a function by 2
def decor(fun):
    def inner():
        value = fun()
        return value + 2

    return inner


def num():
    return 10


# Call decorator function and pass num
result_fun = decor(num)
print(result_fun())