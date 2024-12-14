import pandas as pd

# Read the original data generated from the previous script
df = pd.read_csv('original_metrics_1.csv', parse_dates=['timestamp'])
df = df.sort_values('timestamp')

# Set the timestamp as index for time-based rolling operations
df = df.set_index('timestamp')

# We will use a 7-minute rolling window to count how many times the system was down
window = '7min'
df['down_count_7min'] = df['status'].rolling(window=window).apply(lambda x: (x == 0).sum(), raw=False)

# Define an alert condition: if down_count_7min >= 3 at any given minute
df['alert_triggered'] = df['down_count_7min'] >= 3

# Reset index for saving to CSV
df_aggregated = df.reset_index()

# Write the aggregated results to a new CSV file
df_aggregated.to_csv('aggregated_alerts.csv', index=False)
print("Aggregated alert results stored in 'aggregated_alerts_1.csv'.")

# Print a summary of alerts
alerts = df_aggregated[df_aggregated['alert_triggered'] == True]
if not alerts.empty:
    print("ALERTS TRIGGERED:")
    for _, row in alerts.iterrows():
        print(f"ALERT: At {row['timestamp']}, there were {int(row['down_count_7min'])} downs in the last 7 minutes.")
else:
    print("No alerts triggered during this period.")
