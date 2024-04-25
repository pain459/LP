# using permutations method to generate all possible outcomes
from itertools import permutations

x = ['a', 'b', 'c', 'd']

permuatation_s = permutations(x, 2)
for i in permuatation_s:
    print(i, end=' ')
print('\n')