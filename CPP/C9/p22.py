# Accessing a global variable inside a function
a = 2


def myfunction():
    global a
    print(f'Global a is {a}')
    a = 5
    print('Modifying value of a now.')
    print(f'Local value of a is set to {a}')


myfunction()
print(f'Global a is {a}')