import sys

# Just a trivial script that sums integer arguments
args = sys.argv[1:]
nums = map(int, args)
print(sum(nums))
