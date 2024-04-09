# Who is older?
from datetime import *

# Get both birthdays
d1, m1, y1 = [int(i) for i in input("Enter birthday 1: ").split('/')]
b1 = datetime(y1, m1, d1)
d2, m2, y2 = [int(j) for j in input("Enter birthday 2: ").split('/')]
b2 = datetime(y2, m2, d2)

# compare birthdays
if b1 == b2:
    print('Both persons are of equal age.')
elif b1 < b2:
    print('The first person is older.')
else:
    print('The second person is older.')
