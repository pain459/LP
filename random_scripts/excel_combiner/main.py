import pandas as pd
import glob

# Get a list of all Excel files in the current directory
xlsx_files = glob.glob('*.xlsx')

# Read the first Excel file to get the headers
first_file = pd.read_excel(xlsx_files[0])

# Initialize an empty list to store the data frames
data_frames = []

# Loop through each Excel file (starting from the second one)
for file in xlsx_files:
    # Read the data from each file skipping the header row
    data = pd.read_excel(file, header=None, skiprows=1)
    data_frames.append(data)

# Concatenate all data frames in the list
combined_data = pd.concat(data_frames)

# Write the combined data to a new Excel file
combined_data.to_excel('combined_file.xlsx', index=False, header=first_file.columns)
