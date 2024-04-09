# Finding future date and time

from datetime import *

# Store the date and time in datetime object d1
d1 = datetime(2024, 4, 9, 7, 49, 0)

# Define the duration using timedelta object: period1
period1 = timedelta(days=90, seconds=10, minutes=12, hours=8)

# add the duration to d1 and display
print(f'the new date and time is {d1 + period1}')
