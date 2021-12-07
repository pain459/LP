import random
from art import logo

random_number_chosen = random.randint(1, 100)
print(f'Random number choosen is {random_number_chosen}')

easy_level = 10
hard_level = 5


def play_game(random_number_chosen, chances):
    print(logo)
    game_over = False
    while not game_over:
        print(f"You have {chances} to solve the problem.")
        chances -= 1
        user_guess = eval(input("Enter the number you guess: "))
        if user_guess > random_number_chosen and chances != 0:
            print('Too high')
            #chances -= 1
        elif user_guess < random_number_chosen and chances != 0:
            print('Too low')
            #chances -= 1
        elif chances == 0:
            print('All chances exhausted! Game will exit now.')
            game_over = True
            return
        else:
            print(
                f'Correct! You won! Guessed number is {random_number_chosen}')
            game_over = True


choose_level = str(input('Choose level hard/easy: ')).lower()
if choose_level == 'hard':
    chances = hard_level
    play_game(random_number_chosen=random_number_chosen, chances=chances)

elif choose_level == 'easy':
    chances = easy_level
    play_game(random_number_chosen=random_number_chosen, chances=chances)
else:
    print('Invalid entry!')
