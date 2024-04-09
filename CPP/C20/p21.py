# to test whether leap year or not
from calendar import *

y = int(input('Enter year: '))
if isleap(y):
    print('Leap year!')
else:
    print('Not a leap year!')