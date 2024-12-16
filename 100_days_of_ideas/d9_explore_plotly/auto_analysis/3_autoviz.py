from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd

# Load the dataset
csv_file = "metrics.csv"  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Initialize AutoViz
AV = AutoViz_Class()

# Generate and display visualizations
output_folder = "output_autoviz"  # Specify output folder for graphs
dft = AV.AutoViz(
    filename="", 
    dfte=df, 
    depVar="",  # Specify the dependent variable if applicable
    verbose=2, 
    chart_format="png", 
    save_plot_dir=output_folder
)

print(f"Graphs saved to {output_folder}")
