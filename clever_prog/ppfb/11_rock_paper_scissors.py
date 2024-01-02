import random

standard_choices = ["rock", "paper", "scissors"]
player1 = input("Select rock, paper or scissor: ").lower()
if player1 not in standard_choices:
    print("Not a valid choice. Exiting.")
    exit(1)

# player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
player2 = random.choice(standard_choices).lower()
print(player1)
print("Player2 selected:", player2)

# Game winning and loosing conditions.
if player1 == "rock" and player2 == "paper":
    print("Player 2 wins!")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 Wins!")
elif player1 == player2:
    print("Tie!")
else:
    print("Player 1 Wins!")
