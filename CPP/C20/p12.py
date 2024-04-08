# finding day of the week

from datetime import *

# accept date, month and year from the keyboard
d, m, y = [int(i) for i in input("Enter a date: ").split("/")]

# Store them in date class object
dt = date(y, m, d)

# %w - day number and %A full name of the week day.
print(dt.strftime('Day %w of the week. This is %A'))
