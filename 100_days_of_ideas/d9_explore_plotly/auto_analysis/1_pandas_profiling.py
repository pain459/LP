from pandas_profiling import ProfileReport
import pandas as pd

# Load the dataset
csv_file = "metrics.csv"  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Generate the profile report
profile = ProfileReport(
    df,
    title="Auto Analysis Report",
    explorative=True
)

# Save the report as an HTML file
output_file = "auto_analysis_report.html"
profile.to_file(output_file)

print(f"Analysis report saved to {output_file}")
