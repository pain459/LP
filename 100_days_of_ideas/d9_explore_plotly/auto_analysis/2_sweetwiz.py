import sweetviz as sv
import pandas as pd

# Load the dataset
csv_file = "metrics.csv"  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Generate the analysis report
report = sv.analyze(df)

# Save the report as an HTML file
output_file = "sweetviz_report.html"
report.show_html(output_file)

print(f"Analysis report saved to {output_file}")
