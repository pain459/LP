# A decorator that increments the value by 2
def decor_inc_2(func):
    def wrapper():
        result = func()
        return result + 2

    return wrapper


def original_input(func):
    def wrapper(n):
        result = func(n)
        return int(result / (10 ** (n-1)))

    return wrapper


@decor_inc_2
def num():
    return 10


@original_input
def pow_of_10(n):
    return 10 ** n


print(num())
print(pow_of_10(10))
