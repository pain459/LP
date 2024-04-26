# iterate over multiples lists using zip

# ['product', 'quantity', 'price_per_piece']
x = ['apples', 'oranges', 'plums']
y = [250, 300, 150]
z = [25, 12, 55]

# Calculating SKU values
for item, quantity, price in zip(x, y, z):
    print(f'{item}\'s are worth of {quantity * price}')


# In [5]: for i in zip(x, y):
#    ...:     print(i)
#    ...: 
# ('a', 1)
# ('b', 2)
# ('c', 3)
