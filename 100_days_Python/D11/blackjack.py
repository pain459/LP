import random
from blackjack_logo import logo
from random import choice

cards_in_deck = [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def initialization():
    print(logo)


def start_cards():
    user_first_cards = [random.choice(
        cards_in_deck), random.choice(cards_in_deck)]
    computer_first_cards = [random.choice(
        cards_in_deck), random.choice(cards_in_deck)]
    print(f'Your cards [{user_first_cards[0]}, {user_first_cards[1]}]')
    # Not displaying the computer second card. Instead we will display it as X.
    print(f"Computer's first cards [{computer_first_cards[0]}, X]")
    return user_first_cards, computer_first_cards


def check_win_loose(user_first_cards, computer_first_cards, user_cards, computer_cards):
    if user_first_cards == [13, 13]:
        print('User won!')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
        # return
    elif computer_first_cards == [13, 13]:
        print('Computer won!')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
        # return
    elif sum(user_first_cards) == sum(computer_first_cards):
        print('Game Draw. Dealer won!')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
        # return
    elif sum(user_first_cards) == 21:
        print('User won blackjack! Count 21')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
        # return
    elif sum(computer_first_cards) == 21:
        print('Computer won blackjack! Count 21')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
        # return
    elif sum(user_first_cards) > 21:
        print('Computer Won as user cards are above count 21.')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
        # return
    elif sum(computer_first_cards) > 21:
        print('User Won as computer cards are above count 21.')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
        # return
    elif sum(user_cards) == 21:
        print('User won! Found backjack with count 21.')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
    elif sum(computer_cards) == 21:
        print('Computer won! Found blackjack with count 21.')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)
    elif sum(user_cards) > 21:
        print('Computer won. Card count exceeded 21 for user.')
        game_end(user_first_cards, computer_first_cards,
                 user_cards, computer_cards)


def validate_cards():
    pass


def draw_cards_user(user_cards, computer_cards):
    print(user_cards)
    end_turn_user = False
    while not end_turn_user:
        check_win_loose(user_first_cards=user_first_cards,
                        computer_first_cards=computer_first_cards, user_cards=user_cards, computer_cards=computer_cards)
        draw_card = str(
            input("Type 'y' to get another card, type 'n' to pass: ")).lower()
        if draw_card == 'y':
            user_next_cards = int(random.choice(cards_in_deck))
            user_cards.append(user_next_cards)
            print(user_cards)
            end_turn_user = False
        elif draw_card == 'n':
            print('Holding your position!')
            print(user_cards)
            end_turn_user = True
        else:
            print('Invalid option. Try again!')
            end_turn_user = False


def draw_cards_computer(computer_cards):
    print(computer_cards)
    chance = [1, 0]
    end_turn_computer = False
    while not end_turn_computer:
        draw_card = random.choice(chance)
        if draw_card == 1:
            computer_next_cards = int(random.choice(cards_in_deck))
            computer_cards.append(computer_next_cards)
            print(computer_cards)
            end_turn_computer = False
        elif draw_card == 0:
            print('Holding your position!')
            print(computer_cards)
            end_turn_computer = True
        else:  # This is technically not required.
            print('Invalid option. Try again!')
            end_turn_computer = False


def display_result():
    pass


def game_end(user_first_cards, computer_first_cards, user_cards, computer_cards):
    user_first_cards = []
    computer_first_cards = []
    user_cards = []
    computer_cards = []
    stop_game = False
    while not stop_game:
        user_choice = str(input('Do you want to play again? y/n: '))
        if user_choice == 'y':
            print('Starting new game!')
            stop_game = False
            return
        elif user_choice == 'n':
            print('Program will terminate now!')
            stop_game = True
        else:
            print('Invalid option. Try again!')
            stop_game = False


initialization()
user_first_cards, computer_first_cards = start_cards()
draw_cards_user(user_cards=user_first_cards,
                computer_cards=computer_first_cards)
draw_cards_computer(computer_cards=computer_first_cards)
