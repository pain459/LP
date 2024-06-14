import pandas as pd
import openpyxl
import pytz
from datetime import datetime
import argparse
import requests
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
logger = logging.getLogger('ScheduleLogger')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('schedule.log', maxBytes=5*1024*1024, backupCount=2)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

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

def validate_data(df):
    required_columns = {'DATE', 'M', 'A', 'N', 'D1', 'D2', 'E'}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Input file is missing required columns: {required_columns - set(df.columns)}")

    if not pd.api.types.is_datetime64_any_dtype(df['DATE']):
        raise ValueError("DATE column must be of datetime type")

    for col in required_columns - {'DATE'}:
        if not pd.api.types.is_string_dtype(df[col]):
            raise ValueError(f"{col} column must be of string type")

def generate_date_range_dict(file_path, start_date, end_date):
    try:
        # Load the uploaded Excel file
        df = pd.read_excel(file_path)

        # Ensure the DATE column is in datetime format
        df['DATE'] = pd.to_datetime(df['DATE'])

        # Validate the data
        validate_data(df)

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
        df['E_S'] = df['DATE'].apply(lambda x: to_epoch(x, 7, 0))
        df['E_E'] = df['DATE'].apply(lambda x: to_epoch_next_day(x, 7, 0))

        # Filter dataframe by date range using loc to avoid the SettingWithCopyWarning
        df_filtered = df.loc[(df['DATE'] >= start_date) & (df['DATE'] <= end_date)].copy()

        # Set index to the formatted date
        df_filtered.set_index(df_filtered['DATE'].dt.strftime('%Y-%m-%d'), inplace=True)

        # Drop the original DATE column
        df_filtered.drop(columns=['DATE'], inplace=True)

        # Convert dataframe to dictionary
        data_dict_formatted = df_filtered.to_dict(orient='index')

        return data_dict_formatted
    except Exception as e:
        logger.error(f"Error processing the input file: {e}")
        raise

# Mapping of columns
column_map = {
    'M': 'primary',
    'A': 'primary',
    'N': 'primary',
    'D1': 'secondary',
    'D2': 'secondary',
    'E': 'extended'
}

def translate_column(column_name):
    return column_map.get(column_name, column_name)

def update_detail(t1, t2, user, team, role):
    # Sample API endpoint
    api_url = "https://jsonplaceholder.typicode.com/posts"  # Replace with your actual API endpoint

    # Payload to send to the API
    payload = {
        "start_time": t1,
        "end_time": t2,
        "user": user,
        "team": team,
        "role": role
    }

    try:
        # Simulate API call (replace with actual API call using requests.post in a real scenario)
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Log and print the response (for demonstration purposes)
        response_data = response.json()
        log_message = f"API Response for user {user} and team {team}: {response_data}"
        logger.info(log_message)
        print(log_message)
    except requests.RequestException as e:
        error_message = f"API request failed for user {user} and team {team}: {e}"
        logger.error(error_message)
        print(error_message)
        raise

def flusher(start_date, end_date, team):
    # Convert start_date and end_date to epoch
    start_date_epoch = to_epoch(start_date, 0, 0)
    end_date_epoch = to_epoch(end_date, 23, 59)
    
    # Sample API endpoint
    api_url = "https://jsonplaceholder.typicode.com/posts"  # Replace with your actual API endpoint

    # Payload to send to the API for flushing
    payload = {
        "start_time": start_date_epoch,
        "end_time": end_date_epoch,
        "team": team
    }

    try:
        # Simulate API call for flushing (replace with actual API call using requests.post in a real scenario)
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Log and print the response (for demonstration purposes)
        response_data = response.json()
        log_message = f"Flusher API Response for team {team}: {response_data}"
        logger.info(log_message)
        print(log_message)
        return True
    except requests.RequestException as e:
        error_message = f"Flusher API request failed for team {team}: {e}"
        logger.error(error_message)
        print(error_message)
        return False

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description='Generate dictionary from Excel file based on date range and update details using API.')
    parser.add_argument('-f', '--file_path', type=str, required=False, help='Path to the Excel file')
    parser.add_argument('-s', '--start_date', type=str, required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('-e', '--end_date', type=str, required=True, help='End date in YYYY-MM-DD format')
    parser.add_argument('-t', '--team', type=str, required=True, help='Team name for API')
    parser.add_argument('--flush_only', action='store_true', help='Execute only the flush function')

    args = parser.parse_args()

    # Convert start_date and end_date to datetime
    start_date = pd.to_datetime(args.start_date)
    end_date = pd.to_datetime(args.end_date)

    if args.flush_only:
        try:
            logger.info("Starting flush task...")
            print("Starting flush task...")
            if flusher(start_date, end_date, args.team):
                logger.info("Flusher task completed successfully.")
                print("Flusher task completed successfully.")
            else:
                logger.error("Flusher task failed.")
                print("Flusher task failed.")
        except Exception as e:
            logger.error(f"Unexpected error during flush: {e}")
            print(f"Unexpected error during flush: {e}")
    else:
        try:
            logger.info("Starting dry run...")
            print("Starting dry run...")
            result_dict = generate_date_range_dict(args.file_path, start_date, end_date)
            
            logger.info("Dry run successful. Starting flusher task...")
            print("Dry run successful. Starting flusher task...")
            
            # Run the flusher function
            if flusher(start_date, end_date, args.team):
                logger.info("Flusher task successful. Starting actual update task...")
                print("Flusher task successful. Starting actual update task...")
                
                # Iterating through each date_key and details in result_dict
                for date_key, details in result_dict.items():
                    for col in ['M', 'A', 'N', 'D1', 'D2', 'E']:
                        user = details[col]
                        role = translate_column(col)
                        t1 = details[f"{col}_S"]
                        t2 = details[f"{col}_E"] if col != 'D1' else details['D2_E']
                        update_detail(t1, t2, user, args.team, role)
                
                logger.info("Task completed successfully.")
                print("Task completed successfully.")
                print(result_dict)
            else:
                logger.error("Flusher task failed. Aborting operation.")
                print("Flusher task failed. Aborting operation.")
        except ValueError as e:
            logger.error(e)
            print(e)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"Unexpected error: {e}")
