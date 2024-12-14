import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# -------------------------
# Step 1: Simulate Metric Data at 1-Minute Intervals Over One Hour
# -------------------------
base_time = datetime.now()
period = 60  # total minutes in an hour
timestamps = [base_time + timedelta(minutes=i) for i in range(period)]

# Simulate a status metric: 1 = Up, 0 = Down
# We’ll have a certain probability of being down to mimic noise.
status = np.random.choice([1, 0], size=period, p=[0.9, 0.1])

df = pd.DataFrame({
    'timestamp': timestamps,
    'status': status
})

# Sort by timestamp just to ensure proper ordering
df = df.sort_values('timestamp')

# -------------------------
# Step 2: Analyze Data in 7-Minute Intervals
# -------------------------
# We want to check metrics continuously every 7 minutes. One approach:
# - Consider a rolling window of 7 minutes and analyze the sub-period.
# - A “rolling” or “sliding” window can help detect short-term trends like consecutive downs.

# First, set the timestamp as an index to resample and manage time-based operations easily.
df = df.set_index('timestamp')

# The frequency of the data is every 1 minute. We can now create a rolling window of 7 minutes.
# One subtlety: When using rolling windows on time-indexed data, ensure the data is properly
# sorted and has a proper frequency set. Pandas can use time-based offsets like '7min'.

df = df.sort_index()  # Just to ensure correct order by time.

# For each minute, consider the last 7 minutes of data and check conditions.
# Example condition: If the system has been down for more than half of the last 7 minutes,
# we trigger an alert.

window = '7min'

# Compute a rolling sum of downs over a 7-minute window.
df['down_count_7min'] = df['status'].rolling(window=window).apply(lambda x: (x == 0).sum(), raw=False)

# Let's define a condition:
# Alert if, within any 7-minute window, the system was down >= 3 times (for instance).
alert_condition = df['down_count_7min'] >= 3

alerts = df[alert_condition]

# -------------------------
# Step 3: Report Alerts
# -------------------------
if not alerts.empty:
    print("ALERTS TRIGGERED:")
    # Each row indicates a point in time where the last 7 minutes had 3 or more downs.
    # You may want to deduplicate or refine logic to trigger only once per event.
    for ts, row in alerts.iterrows():
        print(f"ALERT: At {ts}, {int(row['down_count_7min'])} downs in the last 7 minutes.")
else:
    print("No alerts triggered in this time period.")
