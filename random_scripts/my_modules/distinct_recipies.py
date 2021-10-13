# buggy script

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

# This program will print the 2 letter pair with all alphabets
import string

from collections import Counter


def distinct_strings():
    all = []
    for i in FLAVORS:
        for j in FLAVORS:
            all.append((i, j))

    # print(all)
    # final = list(set(all))

    res = [ele for ele, count in Counter(all).items() if count > 1]
    print(res)

    for i, j in all:
        if i == j or j == i:
            pass
        else:
            pass
            # print(f'{i}, {j}')


if __name__ == "__main__":
    distinct_strings()
