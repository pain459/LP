# example for IO Error
try:
    name = input('Enter file name: ')
    f = open(name, 'r')
except IOError:
    print(f'File not found! {name}')
else:
    n = len(f.readlines())
    print(f'{name} has {n} lines.')
    f.close()
