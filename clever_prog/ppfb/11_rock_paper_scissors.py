import random

standard_choices = ["rock", "paper", "scissors"]
player1 = input("Select rock, paper or scissor: ").lower()
if player1 not in standard_choices:
    print("Not a valid choice. Exiting.")
    exit(1)

player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print(player1)
print("Player2 selected:", player2)
