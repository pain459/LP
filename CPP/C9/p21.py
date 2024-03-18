# program to demonstrate global keyword
a = 1  # Global variable.


def myfunc():
    a = 2
    print(f'a is {a}')


myfunc()
print(f'a now is {a}')