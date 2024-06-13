import pandas as pd
import pytz
from datetime import datetime
import argparse

def to_epoch(date_obj, hour, minute, timezone_str='Asia/Kolkata'):
    timezone = pytz.timezone(timezone_str)
    dt = date_obj.replace(hour=hour, minute=minute, second=0, microsecond=0)
    dt = timezone.localize(dt)
    return int(dt.timestamp())

def to_epoch_next_day(date_obj, hour, minute, timezone_str='Asia/Kolkata'):
    timezone = pytz.timezone(timezone_str)
    dt = date_obj + pd.Timedelta(days=1)
    dt = dt.replace(hour=hour, minute=minute, second=0, microsecond=0)
    dt = timezone.localize(dt)
    return int(dt.timestamp())

def generate_date_range_dict(file_path, start_date, end_date):
    # Load the uploaded Excel file
    df = pd.read_excel(file_path)

    # Ensure the DATE column is in datetime format
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Check if both dates are in the sheet
    if start_date not in df['DATE'].values or end_date not in df['DATE'].values:
        raise ValueError("Both start_date and end_date must be present in the sheet.")

    # Check if start_date is less than end_date
    if start_date >= end_date:
        raise ValueError("start_date must be less than end_date.")

    # Add new columns
    df['M_S'] = df['DATE'].apply(lambda x: to_epoch(x, 7, 0))
    df['M_E'] = df['DATE'].apply(lambda x: to_epoch(x, 14, 0))
    df['A_S'] = df['DATE'].apply(lambda x: to_epoch(x, 14, 0))
    df['A_E'] = df['DATE'].apply(lambda x: to_epoch(x, 22, 0))
    df['N_S'] = df['DATE'].apply(lambda x: to_epoch(x, 22, 0))
    df['N_E'] = df['DATE'].apply(lambda x: to_epoch_next_day(x, 7, 0))
    df['D1_S'] = df['DATE'].apply(lambda x: to_epoch(x, 9, 0))
    df['D1_E'] = df['DATE'].apply(lambda x: to_epoch(x, 21, 0))
    df['D2_S'] = df['DATE'].apply(lambda x: to_epoch(x, 21, 0))
    df['D2_E'] = df['DATE'].apply(lambda x: to_epoch_next_day(x, 9, 0))

    # Filter dataframe by date range using loc to avoid the SettingWithCopyWarning
    df_filtered = df.loc[(df['DATE'] >= start_date) & (df['DATE'] <= end_date)].copy()

    # Set index to the formatted date
    df_filtered.set_index(df_filtered['DATE'].dt.strftime('%Y-%m-%d'), inplace=True)

    # Drop the original DATE column
    df_filtered.drop(columns=['DATE'], inplace=True)

    # Convert dataframe to dictionary
    data_dict_formatted = df_filtered.to_dict(orient='index')

    return data_dict_formatted

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description='Generate dictionary from Excel file based on date range.')
    parser.add_argument('-f', '--file_path', type=str, required=True, help='Path to the Excel file')
    parser.add_argument('-s', '--start_date', type=str, required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('-e', '--end_date', type=str, required=True, help='End date in YYYY-MM-DD format')
    args = parser.parse_args()

    # Convert start_date and end_date to datetime
    start_date = pd.to_datetime(args.start_date)
    end_date = pd.to_datetime(args.end_date)

    try:
        result_dict = generate_date_range_dict(args.file_path, start_date, end_date)
        print(result_dict)
    except ValueError as e:
        print(e)
