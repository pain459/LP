import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]
user_choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

# rule set
if user_choice in [0, 1, 2]:
    print('You choose:')
    print(rps[user_choice])
    comp_choice = random.randint(1, 3) - 1
    print('Computer choose:')
    while True:  # Mandatory someone win condition.
        if user_choice == comp_choice:
            comp_choice = random.randint(1, 3) - 1
        else:
            break
    print(rps[comp_choice])
    if user_choice == 0 and comp_choice == 2:
        print('Rock Smashes Scissors!')
        print('You won!')
    elif user_choice == 2 and comp_choice == 1:
        print('Scissors Cut Paper!')
        print('You won!')
    elif user_choice == 1 and comp_choice == 0:
        print('Paper Covers Rock!')
        print('You won!')
    elif user_choice == comp_choice:
        print('Draw!')
    else:
        print('Computer won!')
else:
    print('Invalid input!')
