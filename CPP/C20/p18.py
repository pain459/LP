# Sorting the group of dates in ascending order
from datetime import *

group = []

# add today's date to list.
group.append(date.today())

# add some more dates to the list
group.append(date(1947, 12, 12))
group.append(date(1857, 3, 1))
group.append(date(1912, 3, 5))

print(group)

group.sort()
for i in group:
    print(i)