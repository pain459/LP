a = 'string1'
b = 'string2'
c = 'string3'

# Default order
print("{} {} {}".format(a, b, c))

# Positional formatting
print("{1} {0} {2}".format(a, b, c))

# Key formatting
print("{b} {a} {c}".format(a=0, b=1, c=2))