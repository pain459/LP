from gavel_art import logo
from os import system

participants = {}  # Empty dictionary for the user inputs.
clear = lambda: system('clear')

def bidding_start():
    username = input('Enter your name: ')
    bid = float(input('Enter your bid: '))
    participants[username] = bid
    # print(participants)  # Test code to see the dict in real time.

def bidding_results():
    max_bid = 0
    max_bidder = None
    for i,j in participants.items():
        if j > max_bid:
            max_bid = j
            max_bidder = i
        else:
            pass
    print(f"Max bidder is {max_bidder} with value of {max_bid}")


other_entry = True

while other_entry:
    clear
    print(logo)
    print('Welcome to secret bidding!')
    bidding_start()
    choice = str(input('Do you want to continue? ')).lower()
    if choice == 'y':
        other_entry = True
        print("Let's try again!")
    elif choice == 'n':
        other_entry = False
        bidding_results()
        print('Program completed and terminated.')
    else:
        other_entry = True
        print('Invalid entry. Only y/n are allowed. Lets try again.')