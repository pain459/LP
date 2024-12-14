import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# -------------------------
# Step 1: Simulate Datadog Metric Extraction
# -------------------------

# Let's say we have metrics for an application that checks status every hour.
# We'll simulate a week's worth of hourly data.
num_hours = 24 * 7  # one week of hourly data
base_time = datetime.now()

timestamps = [base_time + timedelta(hours=i) for i in range(num_hours)]

# Simulate "up" (1) or "down" (0) metrics.
# We'll introduce some random downs to emulate noisy checks.
# For simplicity, let's say there's a 10% chance it's down.
status = np.random.choice([1, 0], size=num_hours, p=[0.9, 0.1])

# Create a DataFrame to represent these raw metrics.
df_raw = pd.DataFrame({
    'timestamp': timestamps,
    'status': status
})

# -------------------------
# Step 2: Store Data in "Data Lake"
# -------------------------
# In reality, you'd write to a cloud storage or data lake solution.
# For this example, let's just write to a local CSV file to simulate staging.
df_raw.to_csv('metrics_lake.csv', index=False)

print("Simulated metrics stored in 'metrics_lake.csv'")

# -------------------------
# Step 3: Load and Aggregate Data, Then Refine Alerts
# -------------------------
# Load from the "data lake"
df = pd.read_csv('metrics_lake.csv', parse_dates=['timestamp'])

# Sort by timestamp just to be sure
df = df.sort_values('timestamp')

# We want to reduce noise and only alert if the application is down for multiple consecutive checks.
# Example logic: Trigger an alert if application is down for 3 or more consecutive checks.

# Identify consecutive downs:
# We'll create a helper column to mark consecutive down counts.
df['down_streak'] = 0
consecutive = 0
for i in range(len(df)):
    if df.loc[i, 'status'] == 0:
        consecutive += 1
    else:
        consecutive = 0
    df.loc[i, 'down_streak'] = consecutive

# Now, determine at which points to generate alerts.
# Let's say we only alert if down_streak >= 3.
alerts = df[df['down_streak'] >= 3]

# Print the alert times
if not alerts.empty:
    print("ALERTS GENERATED:")
    for _, row in alerts.iterrows():
        print(f"ALERT: Application down for {row['down_streak']} consecutive checks as of {row['timestamp']}")
else:
    print("No alerts generated. The application did not meet the down threshold.")
