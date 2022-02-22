# Inserting items into a list
# Also covering extending items in a list.

print("Demonstration on inserting items to a list.")

x = [1, 2, 3]
x.insert(2, 'item1')
print(x)

x.insert(0, 'item2')
print(x)

x.extend([4, 5, 6])
print(x)

# can I extend it with a tuple?
# Yes, but it is still adding as items in the list.
x.extend((7, 8, 9))
print(x)


# creating a list and reversing in one line.
y = [i for i in range(1, 11)][::-1]
print(y)