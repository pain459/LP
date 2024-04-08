# Combining date and time

from datetime import *

d = date(2016, 2, 27)
t = time(15, 30)
dt = datetime.combine(d, t)

print(dt)