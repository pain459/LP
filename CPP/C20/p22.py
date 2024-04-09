# To display calendar of a given month
from calendar import *

# ask the year and month
yy = int(input('Enter the year: '))
mm = int(input('Enter the month: '))

# display the calendar
str = month(theyear=yy, themonth=mm)
print(str)