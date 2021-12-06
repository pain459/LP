print('Welcome to the tip calculator.')
total_bill = eval(input('What was your total bill? $'))
tip_percent = eval(input(
    'What percentage tip would you like to give? 10, 12, or 15? '))
total_people = eval(input('How many people to split the bill? '))

if tip_percent in [10, 12, 15]:
    tip_amount = (tip_percent / 100) * total_bill
bill_with_tip = total_bill + tip_amount
shared_bill = round(bill_with_tip / total_people, 2)

print(f'Each person should pay: ${shared_bill}')
