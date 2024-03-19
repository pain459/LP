# Generator the returns sequence from x to y
def mygen(x, y):
    while x <= y:
        yield x
        x += 1


x = mygen(10, 20)


mapped_result = list(map(lambda x:x*2, list(x)))

print(mapped_result)