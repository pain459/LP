import pandas as pd


def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def query_details(df, start_date, end_date, headers):
    try:
        mask = (df.iloc[:, 0] >= start_date) & (df.iloc[:, 0] <= end_date)
        filtered_df = df.loc[mask]
        result_dict = {}
        for index, row in filtered_df.iterrows():
            result_dict[row.iloc[0]] = dict(row[headers])
        return result_dict
    except KeyError:
        print("Invalid headers provided.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    file_path = input("Enter the path of the Excel file: ")
    df = read_excel_file(file_path)
    if df is not None:
        print("Excel file loaded successfully.")
        print("Columns:", df.columns)
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        headers = input("Enter headers (comma-separated): ").split(',')
        filtered_data = query_details(df, start_date, end_date, headers)
        if filtered_data is not None:
            print("Filtered Data:")
            for date, data in filtered_data.items():
                print(f"Date: {date}")
                print("Data:", data)
