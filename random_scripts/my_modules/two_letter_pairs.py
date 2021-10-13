# This program will print the 2 letter pair with all alphabets
import string

l1 = string.ascii_lowercase
l2 = string.ascii_lowercase


def pair_strings():
    for i in l1:
        for j in l2:
            print(str(i + j))


if __name__ == "__main__":
    pair_strings()