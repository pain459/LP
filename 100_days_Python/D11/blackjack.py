import random
import blackjack_logo
from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def initialization():
    print(blackjack_logo.logo)


def give_2_random_cards_each(deck_of_cards):
    """We will generate 2 random cards from the deck."""
    user_first_cards = [random.choice(
        deck_of_cards), random.choice(deck_of_cards)]
    computer_first_cards = [random.choice(
        deck_of_cards), random.choice(deck_of_cards)]
    print(f'Your cards [{user_first_cards[0]}, {user_first_cards[1]}]')
    # ------ #
    # user_first_cards = [10, 11]  # test case.
    # computer_first_cards = [13, 13]  # test case.
    # ------ #
    # Not displaying the computer second card. Instead, we will display it as X.
    print(f"Computer's first cards [{computer_first_cards[0]}, X]")
    return user_first_cards, computer_first_cards


def validate_blackjack(user_cards, computer_cards):
    print('Checking if user or computer have blackjack')
    if sum(computer_cards) == 21:
        print('Computer has blackjack')
        return
    elif sum(user_cards) == 21:
        print('User has the blackjack')
        return
    else:
        print('No blackjack detected!')
        return user_draw_card(user_cards=user_cards, computer_cards=computer_cards)


def user_draw_card(user_cards, computer_cards, ):
    if sum(user_cards) > 21:
        # user_cards = [1 if i == 11 else i for i in user_cards]
        if 11 in user_cards:
            user_cards = [1 if i == 11 else i for i in user_cards]
            if sum(user_cards) > 21:
                print('User lost the game')
                return
            else:
                return draw_another_card(user_cards=user_cards, deck_of_cards=cards, computer_cards=computer_cards)
        else:
            print(f'count is {sum(user_cards)}')
            print('User lost.')
            return
    else:
        print('No Ace in the cards!')
        return draw_another_card(user_cards=user_cards, deck_of_cards=cards, computer_cards=computer_cards)


def draw_another_card(user_cards, computer_cards, deck_of_cards=cards):
    print('Another card needed!')
    user_choice = str(input("Enter 'y' if you want a card. Enter 'n' to skip: "))
    if user_choice == 'y':
        user_cards.append(random.choice(cards))
        print(user_cards)
        return validate_blackjack(user_cards=user_cards, computer_cards=computer_cards)
    elif user_choice == 'n':
        print(f"User stands at {sum(user_cards)}")
        return computer_draw_another_card(user_cards, computer_cards, deck_of_cards=cards)


def computer_draw_another_card(user_cards, computer_cards, deck_of_cards=cards):
    if sum(user_cards) < 17:
        print('Computer won as the user count is less than 17.')
    elif sum(user_cards) > 17:
        computer_cards.append(random.choice(cards))
        computer_turn_over = False
        while not computer_turn_over:
            if 21 > sum(user_cards) > 17 and sum(computer_cards) <= 21:
                if sum(computer_cards) > sum(user_cards):
                    return computer_won_game(computer_cards=computer_cards, user_cards=user_cards)
                # computer_turn_over = True
                elif sum(computer_cards) == sum(user_cards):
                    return draw_game(user_cards=user_cards, computer_cards=computer_cards)
                # computer_turn_over = True
                elif sum(computer_cards) < sum(user_cards):
                    return user_won_game(computer_cards=computer_cards, user_cards=user_cards)
            computer_turn_over = True


def computer_won_game(computer_cards, user_cards):
    print(f"Computer won! Score is {sum(computer_cards)} vs {sum(user_cards)}")


def user_won_game(user_cards, computer_cards):
    print(f"User won! Score is {sum(user_cards)} vs {sum(computer_cards)}")


def draw_game(user_cards, computer_cards):
    print(f"Its a Draw! Score is {sum(user_cards)} vs {sum(computer_cards)}")


def main():
    initialization()
    cards_user, cards_computer = give_2_random_cards_each(deck_of_cards=cards)
    # print(cards_user) # Spoilers
    # print(cards_computer) # spoilers
    validate_blackjack(user_cards=cards_user, computer_cards=cards_computer)


if __name__ == "__main__":
    main()
