import random
from blackjack_logo import logo
from random import choice

cards_in_deck = [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def initialization():
    """Print logo"""
    print(logo)


def next_card(cards_in_deck):
    """This simulate drawing the next card and return the value."""
    return random.choice(cards_in_deck)


def start_cards():
    """Display starting cards of the game."""
    user_first_cards = [random.choice(
        cards_in_deck), random.choice(cards_in_deck)]
    computer_first_cards = [random.choice(
        cards_in_deck), random.choice(cards_in_deck)]
    print(f'Your cards [{user_first_cards[0]}, {user_first_cards[1]}]')
    # ------ #
    # user_first_cards = [13, 13]  # test case.
    # computer_first_cards = [13, 13]  # test case.
    # ------ #
    # Not displaying the computer second card. Instead we will display it as X.
    print(f"Computer's first cards [{computer_first_cards[0]}, X]")
    return [user_first_cards, computer_first_cards]


def user_draw_card(user_cards, cards_in_deck):
    user_lost_game = False
    while not user_lost_game:
        user_choice = str(
            input("Enter 'y' if you want a card. Enter 'n' to skip/declare: "))
        if user_choice == 'y':
            user_cards.append(next_card(cards_in_deck=cards_in_deck))
            if sum(user_cards) > 21:
                print(f'User lost. Total count is {sum(user_cards)}')
                user_lost_game = True
        elif user_choice == 'n':
            user_total = sum(user_cards)
            return user_total
        return


def computer_draw_card(computer_cards, cards_in_deck):
    computer_lost_game = False
    chance = [1, 0]
    while not computer_lost_game:
        draw_card = random.choice(chance)
        if draw_card == 1:
            # computer_next_cards = int(random.choice(cards_in_deck))
            computer_cards.append(random.choice(cards_in_deck))
            print(computer_cards)
            if sum(computer_cards) > 21:
                print(f'Computer lost. Total count is {sum(computer_cards)}')
                computer_lost_game = True
        elif draw_card == 0:
            computer_total = sum(computer_cards)
            return computer_cards
        return


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


def main():
    """Program starts here."""
    initialization()
    user_cards, computer_cards = start_cards()
    print(user_cards, computer_cards)
    user_total = user_draw_card(
        user_cards=user_cards, cards_in_deck=cards_in_deck)
    computer_total = computer_draw_card(
        computer_cards=computer_cards, cards_in_deck=cards_in_deck)
    print('Printing this later.')
    print(user_total)
    print(computer_total)


if __name__ == "__main__":
    main()
