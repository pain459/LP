# Getting time only from datetime object
from datetime import *

# Create datetime object with current date and time
dt = datetime.now()

print(dt)

# get current time

ct = dt.strftime("%H:%M:%S")
print(ct)