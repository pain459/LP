import os
import csv


def find_isin_in_files(symbol, csv_files):
    for csv_file in csv_files:
        isin = find_isin(symbol, csv_file)
        if isin:
            return isin
    return None


def find_isin(symbol, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            if row[0] == symbol:
                return row[1]  # Assuming ISIN is in the second column
    return None


if __name__ == "__main__":
    csv_directory = "your_csv_directory"  # Provide the directory path containing your CSV files
    symbol = input("Enter the stock symbol: ").upper()

    # Get a list of CSV files in the directory
    csv_files = [os.path.join(csv_directory, file) for file in os.listdir(csv_directory) if file.endswith('.csv')]

    isin = find_isin_in_files(symbol, csv_files)
    if isin:
        print(f"The ISIN number for {symbol} is: {isin}")
    else:
        print(f"Unable to find ISIN number for {symbol}. Please verify the symbol.")
