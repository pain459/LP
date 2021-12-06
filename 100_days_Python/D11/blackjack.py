import random
from blackjack_logo import logo
from random import choice

cards_in_deck = [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def initialization():
    print(logo)

def start_cards():
    user_first_cards = [random.choice(cards_in_deck), random.choice(cards_in_deck)]
    computer_first_cards = [random.choice(cards_in_deck), random.choice(cards_in_deck)]
    print(f'Your cards [{user_first_cards[0]}, {user_first_cards[1]}]')
    print(f"Computer's first cards [{computer_first_cards[0]}, X]")  # Not displaying the computer second card. Instead we will display it as X.
    return user_first_cards, computer_first_cards

def draw_cards_user(user_cards):
    print(user_cards)
    end_turn = False
    while not end_turn:
        draw_card = str(input("Type 'y' to get another card, type 'n' to pass: ")).lower()
        if draw_card == 'y':
            user_next_cards = int(random.choice(cards_in_deck))
            user_cards.append(user_next_cards)
            if sum(user_cards) > 21:
                print('User lost the game! Dealer won.')
            elif sum(user_cards) == 21:
                print('User found blackjack. User won.')
            print(user_cards)
            end_turn = False
        elif draw_card == 'n':
            print('Holding your position!')
            print(user_cards)
            end_turn = True
        else:
            print('Invalid option. Try again!')
            end_turn = False


def draw_cards_computer():
    pass

def display_result():
    pass


stop_game = False

while not stop_game:
    initialization()
    user_first_cards, computer_first_cards = start_cards()
    draw_cards_user(user_first_cards)
    user_choice = str(input('Do you want to play again? y/n: '))
    if user_choice == 'y':
        print('Starting new game!')
        stop_game = False
    elif user_choice == 'n':
        print('Program will terminate now!')
        stop_game = True
    else:
        print('Invalid option. Try again!')
        stop_game = False