def decor_2(func):
    def multiply_by_two(n):
        result = func(n)
        return result * 2

    return multiply_by_two


@decor_2
def num(n):
    return n * 10


print(num(10))
