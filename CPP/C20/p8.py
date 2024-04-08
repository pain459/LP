# Create a date time object and change its contents

from datetime import *

# Create datetime object
dt1 = datetime(year=2024, month=4, day=8, hour=9, minute=26, second=0, microsecond=0)

print(dt1)

dt2 = dt1.replace(year=2026)

print(dt2)