# displaying the range of continuous dates
from datetime import *

# Start with today.
d = date.today()
print(d)

# get future dates
for i in range(100):
    print(d + timedelta(days=i))
