# to find some of 2 given numbers

import argparse

parser = argparse.ArgumentParser(description="This program calculates the sum of 2 given numbers.")

parser.add_argument("n1", type=float, help="Input first number.")
parser.add_argument("n2", type=float, help="Input second number.")

args = parser.parse_args()

result = float(args.n1) + float(args.n2)
print("Sum of two=", result)