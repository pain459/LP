# Formatting the date

from datetime import *

# Get current date and time

td = date.today()
print(td)

# Format the td to convert into string str
str = td.strftime("%d, %B, %y")

print(str)