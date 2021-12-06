print('Welcome to Python Pizza Deliveries!')
size_p = str(input('What size of pizza do you want? S, M, or L '))
pepperoni = str(input('Do you want pepperoni? Y or N '))
extra_cheese = str(input('Do you want extra cheese? Y or N '))
total_bill = 0
if size_p == 'S':
    total_bill += 15
    if pepperoni == 'Y':
        total_bill += 2
    if extra_cheese == 'Y':
        total_bill += 1
elif size_p == 'M':
    total_bill += 20
    if extra_cheese == 'Y':
        total_bill += 1
elif size_p == 'L':
    total_bill += 25
    if extra_cheese == 'Y':
        total_bill += 1
if pepperoni == 'Y' and (size_p == 'M' or size_p == 'L'):
    total_bill += 3

print(f'Your final bill is ${total_bill}.')
