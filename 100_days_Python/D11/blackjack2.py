import random
from blackjack_logo import logo
from random import choice

cards_in_deck = [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
game_end_master = False


def initialization():
    """Print logo"""
    print(logo)


def start_cards():
    """Display starting cards of the game."""
    user_first_cards = [random.choice(
        cards_in_deck), random.choice(cards_in_deck)]
    computer_first_cards = [random.choice(
        cards_in_deck), random.choice(cards_in_deck)]
    # print(user_first_cards)
    # print(computer_first_cards)
    print(f'Your cards [{user_first_cards[0]}, {user_first_cards[1]}]')
    # ------ #
    # user_first_cards = [13, 13]  # test case.
    # computer_first_cards = [13, 13]  # test case.
    # ------ #
    # Not displaying the computer second card. Instead we will display it as X.
    print(f"Computer's first cards [{computer_first_cards[0]}, X]")

    # if check_immediate_winner(user_first_cards=user_first_cards, computer_first_cards=computer_first_cards):
    #     return game_end()
    # else:
    #     pass
    # print(user_first_cards)
    return [user_first_cards, computer_first_cards]


def check_immediate_winner(user_first_cards, computer_first_cards):
    if user_first_cards == [13, 13] and computer_first_cards == [13, 13]:
        print('Miracle!')
        return True
    elif computer_first_cards == [13, 13]:
        print('Computer won blackjack with first cards only')
        return True
    elif user_first_cards == [13, 13]:
        print('User won backjack with first cards only')
        return True
    elif user_first_cards == ([10, 13] or [13, 10]):
        print('User won blackjack with perfect combo')
        return True
    elif computer_first_cards == ([10, 13] or [13, 10]):
        print('Computer won blackjack with perfect combo')
        return True
    else:
        pass


def next_card(cards_in_deck):
    """This simulate drawing the next card and return the value."""
    return random.choice(cards_in_deck)


def count_exceeded(cards):
    """This function will return True if the the total is greater than 21, else it will return False."""
    if sum(cards) > 21:
        return True
    else:
        return False


def minimum_count(cards):
    """This function will check for minimum count 18 for current cards."""
    if sum(cards) < 18:
        return True
    else:
        return False


def winner_on_next_card(cards):
    """This functionw will check the next card and decide if the current player is winner"""
    if sum(cards) == 21:
        print('BlackJack 21 acheived!')
        return game_end()
    else:
        return False


def draw_cards_user(user_cards, cards_in_deck):
    """This function will draw cards for user."""
    draw_card = str(input("type 'y to draw another card. Type 'n' to hold: "))
    stop_taking_cards = False
    while not stop_taking_cards:
        if draw_card == 'y':
            user_cards.append(next_card(cards_in_deck=cards_in_deck))
            print(user_cards)
            if winner_on_next_card(cards=user_cards):
                print('User won with last card.')
                stop_taking_cards = True
                return game_end()
            else:
                # pass
                stop_taking_cards = False
        elif draw_card == 'n':
            if minimum_count(cards=user_cards):
                print('Minimum count not acheived to hold. Computer won!')
                stop_taking_cards = True
                return game_end()
            else:
                stop_taking_cards = False
                pass
    return


def draw_cards_computer(user_cards, computer_cards, cards_in_deck,):
    """This function will draw cards for the computer"""
    pass


def game_end():
    """Simulate game ending."""
    stop_game = False
    while not stop_game:
        user_choice = str(input('Do you want to play again? y/n: '))
        if user_choice == 'y':
            print('Starting new game!')
            stop_game = False
            # main()
            return main()
        elif user_choice == 'n':
            print('Program will terminate now!')
            stop_game = True
            # terminated()
            return terminated()
        else:
            print('Invalid option. Try again!')
            stop_game = False


def terminated():
    print('PROGRAM END!')
    # exit()


def main():
    """Program starts here."""
    initialization()
    user_cards, computer_cards = start_cards()
    #print(user_cards, computer_cards)
    if check_immediate_winner(user_first_cards=user_cards, computer_first_cards=computer_cards):
        return game_end()
    else:
        pass
    # draw_cards_user(user_cards=user, computer_cards=computer,
    #                 cards_in_deck=cards_in_deck)
    #print(user_cards, computer_cards)
    draw_cards_user(user_cards=user_cards, cards_in_deck=user_cards)

    print('Printing this later.')


if __name__ == "__main__":
    main()
