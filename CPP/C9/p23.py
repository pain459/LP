# same name for global and local variable
a = 1


def myfunction():
    a = 2
    x = globals()['a']  # Get global var into x
    print(f'global var a = {x}')
    print(f'local var a = {a}')


myfunction()
print(f'global var of a = {a}')
