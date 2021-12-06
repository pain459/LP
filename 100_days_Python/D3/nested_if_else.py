print('Welcome to the rollercoaster!')
height = int(input('Enter your height in cm: '))
if height >= 120:
    print('You are welcome to ride the roller coaster.')
    age = int(input('Please enter you age: '))
    if age < 12:
        print('You have to pay $5 for ticket.')
    elif age >= 12 and age <= 18:
        print('You have to pay $7 for ticket')
    else:
        print('You have to pay 12$ for ticket.')

else:
    print('Sorry, you have to grow taller before you can ride.')
