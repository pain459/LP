# using permutations method to generate all possible outcomes
from itertools import combinations

x = ['a', 'b', 'c', 'd']

combination_s = combinations(x, 2)
for i in combination_s:
    print(i, end=' ')
print('\n')