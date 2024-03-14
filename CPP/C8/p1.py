# Indexing on Strings
str = 'Core Python'

# Access each character using while loop
n = len(str)
i = 0
while i < n:
    print(str[i], end=' ')
    i += 1
print()  # Put cursor into next line
# Access in reverse order.
i = -1
while i >= -n:
    print(str[i], end=' ')
    i -= 1
print()  # Put cursor into next line
# Access in reverse order using negative index
i = 1
while i <= n:
    print(str[-i], end=' ')
    i += 1

