# Kadane's Algorithm
from sys import maxsize

def max_sequence(a):

    # max_so_far = -maxsize - 1
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, len(a)):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Should be 6
print(max_sequence([-1, 2, -3, 2, -5, 2]))  # Should be 2
print(max_sequence([]))
