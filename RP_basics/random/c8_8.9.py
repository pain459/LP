# Region 1: 87% chance of winning
# Region 2: 65% chance of winning
# Region 3: 17% chance of winning

import random

def counter(x):
    if random.random() < x:
        return "A"
    else:
        return "B"

can_A = 0
can_B = 0
can_A_R = 0
can_B_R = 0
regions = 0
w_p = [0.87, 0.65, 0.17]
for i in range(0, 3):
    for v in range(10000):
        if counter(w_p[i]) == 'A':
            can_A += 1
        else:
            can_B += 1
    if can_A > can_B:
        can_A_R += 1
    else:
        can_B_R += 1
if can_A_R > can_B_R:
    print("Candidate A won")
else:
    print("Candidate B won")

print(f"Total votes: \n"
      f"Candidate A = {can_A}\n"
      f"Candidate B = {can_B}")


