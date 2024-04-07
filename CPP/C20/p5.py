# Find the current date and time using datetime class
from datetime import *

now = datetime.now()
print(now)

print(f'Date now: {now.day}/{now.month}/{now.year}')
print(f'Time now: {now.hour}:{now.minute}:{now.second}')