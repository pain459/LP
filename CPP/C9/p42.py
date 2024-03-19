# generator that returns the characters from A to C
def mygen():
    yield "A"
    yield "B"
    yield "C"


g = mygen()

print(next(g))
print(next(g))
print(next(g))