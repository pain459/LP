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
# Introduce a certain probability of being down
status = np.random.choice([1, 0], size=period, p=[0.9, 0.1])

df = pd.DataFrame({
    'timestamp': timestamps,
    'status': status
})

# Sort by timestamp to ensure proper ordering
df = df.sort_values('timestamp')

# Write the original data to a CSV file for comparison
df.to_csv('original_metrics.csv', index=False)
print("Original metrics stored in 'original_metrics.csv'")

# -------------------------
# Step 2: Analyze Data in 7-Minute Intervals
# -------------------------
# Set timestamp as index
df = df.set_index('timestamp')
df = df.sort_index()

# Compute a rolling sum of downs over a 7-minute window
window = '7min'
df['down_count_7min'] = df['status'].rolling(window=window).apply(lambda x: (x == 0).sum(), raw=False)

# Define alert condition: if down_count_7min >= 3 at any given minute
df['alert_triggered'] = df['down_count_7min'] >= 3

# -------------------------
# Step 3: Write Aggregated Data and Alerts to CSV
# -------------------------
# Reset index so timestamp is a column again
df_aggregated = df.reset_index()

df_aggregated.to_csv('aggregated_alerts.csv', index=False)
print("Aggregated results (with rolling 7-minute down counts) stored in 'aggregated_alerts.csv'")

# -------------------------
# Step 4: Print Summary / Comparison
# -------------------------
alerts = df_aggregated[df_aggregated['alert_triggered'] == True]

if not alerts.empty:
    print("ALERTS TRIGGERED:")
    for _, row in alerts.iterrows():
        print(f"ALERT: At {row['timestamp']}, {int(row['down_count_7min'])} downs in the last 7 minutes.")
else:
    print("No alerts triggered in this period.")

# Additional Comparison:
# Just printing how many times the system was down in total
total_downs = (df_aggregated['status'] == 0).sum()
print(f"Total downs in the hour: {total_downs}")
