# program to apply decorators with @
def decor(fun):
    def inner():
        value = fun()
        return value + 2
    return inner


def decor1(fun):
    def inner():
        value = fun()
        return value * 20
    return inner


@decor   # This decorator will be applied second.
@decor1  # This decorator will be applied first.
def num():
    return 10


print(num())
