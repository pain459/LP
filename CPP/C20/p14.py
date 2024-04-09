# Difference between 2 days along with time.

from datetime import *

# create datetime objects that store date and time
d1 = datetime(2000, 1, 1, 12, 12, 12, 12)
d2 = datetime(2024, 4, 9, 7, 41, 12, 12)

# Difference in days
diff = d2 - d1
# print(diff.days)

# Difference in weeks
weeks, days = divmod(diff.days, 7)
# print(weeks)

# Difference in hours
hours, secs = divmod(diff.seconds, 3600)
# print(hours)

# Difference in minutes
mins = secs//60

# Difference in seconds
secs = secs % 60

print(f'Diff is {weeks} weeks, {days} days, {hours} hours, {mins} minutes, {secs} seconds')