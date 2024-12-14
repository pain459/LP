import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate one full day (24 hours) of data at 1-minute intervals
base_time = datetime.now()
period = 60 * 24  # 1440 minutes in a day
timestamps = [base_time + timedelta(minutes=i) for i in range(period)]

# Simulate status: 1 = Up, 0 = Down
# Let's say there's a 10% chance of being down to mimic noise.
status = np.random.choice([1, 0], size=period, p=[0.9, 0.1])

df = pd.DataFrame({
    'timestamp': timestamps,
    'status': status
})

# Sort by timestamp (just a safety measure)
df = df.sort_values('timestamp')

# Write this to a CSV file
df.to_csv('original_metrics_1.csv', index=False)
print("Generated 24 hours of simulated data in 'original_metrics.csv'.")
