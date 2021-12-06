print('Welcome to the rollercoaster!')
height = int(input('Enter your height in cm: '))
total_bill = 0
if height >= 120:
    print('You are welcome to ride the roller coaster.')
    age = int(input('Please enter you age: '))
    if age < 12:
        print('$5 for ticket added to bill')
        total_bill += 5
    elif age >= 12 and age <= 18:
        print('$7 for ticket added to bill.')
        total_bill += 7
    elif age >= 45 and age <= 55:
        print('You can ride for free!')
        total_bill += 0
    else:
        print('12$ for ticket added to bill.')
        total_bill += 12
    photo_r = input('Do you want a photo?(Yes/No): ')
    if photo_r == 'Yes':
        print('$3 for photo added to bill.')
        total_bill += 3
        print(f'Your total bill is ${total_bill}')
    if photo_r == 'No':
        print(f'Your total bill is ${total_bill}')
else:
    print('Sorry, you have to grow taller before you can ride.')
