import pandas as pd
from datetime import datetime
import argparse

def calculate_total_working_days(updated_working_days_file, start_date, end_date):
    """
    Calculate the total working days between two dates using the updated_working_days.csv file.

    Args:
    - updated_working_days_file: Path to the updated_working_days.csv file.
    - start_date: Start date in 'YYYY-MM-DD' format.
    - end_date: End date in 'YYYY-MM-DD' format.

    Returns:
    - Total working days as an integer.

    Sample invocation:
    python calculate_working_days.py updated_working_days.csv 2025-01-01 2025-12-31
    """
    # Load the updated working days CSV
    working_days = pd.read_csv(updated_working_days_file)
    
    # Ensure the date column is in datetime format
    working_days["date"] = pd.to_datetime(working_days["date"])
    
    # Convert input dates to datetime
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Filter rows within the date range
    filtered_days = working_days[(working_days["date"] >= start_date) & (working_days["date"] <= end_date)]
    
    # Calculate the sum of working days (working_day = 1)
    total_working_days = filtered_days["working_day"].sum()
    
    # Print the result
    print(f"Total working days between {start_date.date()} and {end_date.date()}: {total_working_days}")
    return total_working_days

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Calculate total working days between two dates.")
    parser.add_argument("updated_working_days_file", type=str, help="Path to the updated_working_days.csv file")
    parser.add_argument("start_date", type=str, help="Start date in 'YYYY-MM-DD' format")
    parser.add_argument("end_date", type=str, help="End date in 'YYYY-MM-DD' format")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function with parsed arguments
    calculate_total_working_days(args.updated_working_days_file, args.start_date, args.end_date)

if __name__ == "__main__":
    main()
