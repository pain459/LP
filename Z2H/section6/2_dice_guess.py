# This game will have 2 dices with 2 different value set. 
# Same game played by pandavas in kurukshetra

# library imports
from random import choice
from time import sleep
# function1 to get user input


def input_selection1():
    a = ''
    while a not in ['1', '3', '5', '7']:
        a = input('Enter a number from (1, 3, 5, 7):')
    return int(a)


def input_selection2():
    b = ''
    while b not in ['2', '4', '6', '8']:
        b = input('Enter a number from (2, 4, 6, 8):')
    return int(b)


# function2 to get the input for dice 1
# we will use random.choice here
dice1 = ['1', '3', '5', '7']
def dice_roll_1():
    x = choice(dice1)
    print('PITUHUUU')
    sleep(2)
    print(f'{x}')
    return int(x)

# function3 to get the input for dice 2


dice2 = ['2', '4', '6', '8']
def dice_roll_2():
    y = choice(dice2)
    print('PITUHUUU')
    sleep(2)
    print(f'{y}')
    return int(y)
# function4 for checking the results and giving fate.
# Panchali in this case.


def fate_decider(input_selection1, input_selection2, dice_roll_1, dice_roll_2):
    if input_selection1 == dice_roll_1 or input_selection2 == dice_roll_2:
        print('You won!')
    else:
        print('Panchali gone')

# instantiations
input1 = input_selection1()
input2 = input_selection2()
dice1_roll = dice_roll_1()
dice2_roll = dice_roll_2()
fate_decider = fate_decider(input1, input2, dice1_roll, dice2_roll)
