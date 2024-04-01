# An exception handling example.
try:
    f = open('myfile.txt', 'w')
    a, b = [int(i) for i in input("Enter two numbers: ").split()]
    c = a / b
    f.write(f'Writing {c} into myfile.txt')

except ZeroDivisionError:
    print('Division by zero happened.')
    print('Please do not enter 0 in input.')

finally:
    f.close()
    print('File closed')