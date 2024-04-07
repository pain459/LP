# Converting epoch time into datetime
import time

# localtime() converts the epoch time into time_struct object t

t = time.localtime(1712510568.4711637)

# Retrieving the date from the structure t
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print(f'Current date is {d}-{m}-{y}')

# Retrieve the time from the structure t
h = t.tm_hour
m = t.tm_hour
s = t.tm_sec
print(f'Time is {h}:{m}:{s}')