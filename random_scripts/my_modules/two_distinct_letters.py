# This program will print the 2 letter pair with all alphabets
import string

l1 = string.ascii_lowercase
l2 = string.ascii_lowercase


def distinct_strings():
    for i in l1:
        for j in l2:
            if i != j:
                print(str(i + j))
            else:
                pass


if __name__ == "__main__":
    distinct_strings()