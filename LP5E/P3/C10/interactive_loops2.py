# Using try and except statements for previous example.

while True:
    reply = input('Enter text (stop will terminate): ')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye!')


# supporting float numbers

while True:
    reply = input('Enter a number: ')
    if reply == 'stop': break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye!')