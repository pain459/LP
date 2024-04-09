# Difference days, weeks and months between 2 dates
from datetime import *

# enter the two dates from the keyboard
d1, m1, y1 = [int(i) for i in input('Enter birth date :').split('/')]
d2, m2, y2 = [int(j) for j in input('Enter to compare date :').split('/')]

# Create date class objects with this data
dt1 = date(y1, m1, d1)
dt2 = date(y2, m2, d2)

# Find the days difference between 2 dates
dt = dt2 - dt1
print(f'Days in difference {dt}')

# difference in weeks
weeks, days = divmod(dt.days, 7)
print(f'Weeks difference = {weeks}')

# difference in months
months, days = divmod(dt.days, 30)
print(f'Months difference = {months}')