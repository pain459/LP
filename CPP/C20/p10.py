# Find the day of the year
from datetime import *

# get today's date
td = date.today()
print(td)

# %j returns the day of the year as 001, 002,...366
s1 = td.strftime("%j")
print(f"Today is {s1}th day of the current year.")

# Find the week day name
s2 = td.strftime("%A")
print(f"It is {s2}")