# This program will give random ticket numbers between 1 to 100 for 10 winners.
from random import randint
_ = list
x = _(range(1, 101))
for i in enumerate(range(1, 11)):
    print(i[1], randint(1, 100))
