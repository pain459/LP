# Using partial to create partial functions with predefined arguments
from functools import partial

# original functions
def power(base, exponent):
    return base ** exponent

# Using partial to define square from power
square = partial(power, exponent = 2)

result = square(5)

print(result)