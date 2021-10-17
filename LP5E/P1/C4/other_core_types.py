X = set('spam')
Y = {'h', 'a', 'm'}
X,Y  # ({'m', 's', 'a', 'p'}, {'m', 'h', 'a'}) tuple of 2 sets.
X & Y  # {'m', 'a'}  Intersection
X | Y  # {'m', 'h', 'p', 's', 'a'}  Union
X - Y  # {'s', 'p'}  Difference
X > Y  # False. Superset.
# set comprehensions
{i ** 2 for i in [1, 2, 3, 4]}  # {16, 1, 4, 9}

list(set([1, 2, 3, 4, 2, 3, 5]))  # [1, 2, 3, 4, 5]
set('spam') - set('ham')  # {'s', 'p'}
set('spam') == set('asmp')  # True
# 'in' membership tests.
'p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham']
# (True, True, True)

# Exploring decimal library
1 / 3  # 0.3333333333333333
(2/3) + (1/2)  # 1.1666666666666665

import decimal  # fixed precision
d = decimal.Decimal('3.141')
d + 1  # Decimal('4.141')
decimal.getcontext().prec = 2
decimal.Decimal('1.00') / decimal.Decimal('3.00')  # Decimal('0.33')

# Exploring fractions
from fractions import Fraction  # Fractions: numerator+denominator
f = Fraction(2, 3)
f + 1  # Fraction(5, 3)
f + Fraction(1, 2)  # Fraction(7, 6)