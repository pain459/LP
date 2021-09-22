# how many flips it takes to get at least 1 heads and 1 tails of a single coin.
import random
def coin():
    if random.randint(0, 1) == 0:
        return "heads"
    elif random.randint(0, 1) == 1:
        return "tails"
    else:
        return "null"

heads = 0
tails = 0

for i in range(1, 1000):
    if coin() == "heads":
        heads += 1
        if heads >= 1 and tails >= 1:
            print(heads, tails)
            break
    else:
        tails += 1
        if heads >= 1 and tails >= 1:
            print(heads, tails)
            break

# print(f"It took {heads} heads flips and {tails} tails flips to achieve at least 1 each.")
print(f"It tool {int(heads) + int(tails)} flips to land on both heads and tails.")


#####

# how many flips it takes to get at least 1 heads and 1 tails of a single coin.
import random
def coin():
    if random.randint(0, 1) == 0:
        return "heads"
    elif random.randint(0, 1) == 1:
        return "tails"
    else:
        return "null"

heads = 0
tails = 0
trails = 1000000
for i in range(0, trails):
    if coin() == "heads":
        heads += 1
    else:
        tails += 1

print(f"heads are {round((int(heads)/int(trails)) * 100, 2)}% and tails are {round((int(tails)/int(trails)) * 100, 2)}%")

