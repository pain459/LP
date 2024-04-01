# Example for syntax error.
try:
    entry = eval(input('Enter date: '))
except SyntaxError:
    print('Invalid date entered.')
else:
    print(f'You entered {entry}')