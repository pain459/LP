# Python program to create 2 decorators
def decor(fun):
    def inner():
        value = fun()
        return value + 2
    return inner


def decor1(fun):
    def inner():
        value = fun()
        return value * 2
    return inner


# actual function
def num():
    return 10

# applying the decor once
result_fun = decor(num)
print(result_fun())

# applying the decor twice
result_fun1 = decor(decor1(num))
print(result_fun1())