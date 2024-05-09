# Pointers demo with integers

x = 1
y = 2

print(f'x = {x} and value of x is {id(x)}')
print(f'y = {y} and value of x is {id(y)}')

# equalling y to x

y = x
print(f'After equalling y to x')
print(f'x = {x} and value of x is {id(x)}')
print(f'y = {y} and value of x is {id(y)}')

# now setting x to 2

x = 2
print(f'After setting x back to {x}')
print(f'x = {x} and value of x is {id(x)}')
print(f'y = {y} and value of x is {id(y)}')


'''
see the memory locations shifting but not changing.
x = 1 and value of x is 138752914473200
y = 2 and value of x is 138752914473232
After equalling y to x
x = 1 and value of x is 138752914473200
y = 1 and value of x is 138752914473200
After setting x back to 2
x = 2 and value of x is 138752914473232
y = 1 and value of x is 138752914473200
'''