# assert statement with message
try:
    x = int(input('Enter a number between 5 and 10: '))
    assert 5 <= x <= 10, 'Your input is not correct'
    print(f'The number is {x}')
except AssertionError as e:
    print(e)