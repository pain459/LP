import random

player1 = input("Select rock, paper or scissor: ").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print(player1)
print(player2)