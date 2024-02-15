# To find power value of a number

import argparse

# Call the argument parser.
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument('nums', nargs=2)

# retrieve the arguments into args object
args = parser.parse_args()
# Find the power of a value.
# args.nums represents a list
print("Number =", args.nums[0])
print("Power =", args.nums[1])

# Convert the arguments into float and then find the power
result = float(args.nums[0]) ** float(args.nums[1])
print("Result =", result)