# Find the square of a given number using argparser

import argparse

parser = argparse.ArgumentParser(description="This program displays the square of a given int number. Only 1 number "
                                             "accepted.")
parser.add_argument("num", type=int, help="Please input integer type number.")
args = parser.parse_args()
result = args.num ** 2
print("Squared value is:", result)