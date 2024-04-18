import pandas as pd
import glob

# Get a list of all Excel files in the current directory
xlsx_files = glob.glob('*.xlsx')

# Read the first Excel file to get the headers
first_file = pd.read_excel(xlsx_files[0])
print("Headers from the first file:", first_file.columns)

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each Excel file (starting from the second one)
for file in xlsx_files[1:]:
    print("Reading data from file:", file)
    # Read the data from each file skipping the header row
    data = pd.read_excel(file, header=None, skiprows=1)
    print("Read", len(data), "rows of data")
    # Concatenate the data with the combined DataFrame
    combined_data = pd.concat([combined_data, data])

# Write the combined data to a new Excel file
combined_data.to_excel('combined_file.xlsx', index=False, header=first_file.columns)
print("Combined data written to combined_file.xlsx")
