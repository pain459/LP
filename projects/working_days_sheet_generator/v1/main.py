import pandas as pd
from datetime import datetime, timedelta

def generate_working_days(start_date, end_date):
    """Generate the initial working_days.csv with weekends marked as non-working."""
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    dates = []
    current_date = start_date
    
    while current_date <= end_date:
        day_name = current_date.strftime("%A")
        working_day = 0 if day_name in ["Saturday", "Sunday"] else 1
        dates.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "day": day_name,
            "working_day": working_day
        })
        current_date += timedelta(days=1)
    
    df = pd.DataFrame(dates)
    df.to_csv("working_days.csv", index=False)
    print("Step 1: working_days.csv generated.")

def update_with_holidays(holiday_sheet_file):
    """Update working_days.csv with holidays from holiday_sheet.csv."""
    # Load the working days CSV
    working_days = pd.read_csv("working_days.csv")
    
    # Load the holiday sheet
    holidays = pd.read_csv(holiday_sheet_file)
    holidays["date"] = pd.to_datetime(holidays["date"]).dt.strftime("%Y-%m-%d")
    
    # Update working_days.csv with holidays
    working_days["date"] = pd.to_datetime(working_days["date"]).dt.strftime("%Y-%m-%d")
    working_days.loc[working_days["date"].isin(holidays["date"]), "working_day"] = 0
    
    # Save updated CSV
    working_days.to_csv("updated_working_days.csv", index=False)
    print("Step 2: updated_working_days.csv generated with holidays marked.")

def main():
    # User inputs
    start_date = "2025-01-01"  # Change as needed
    end_date = "2025-12-31"    # Change as needed
    holiday_sheet_file = "holiday_sheet.csv"
    
    # Generate initial working_days.csv
    generate_working_days(start_date, end_date)
    
    # Update with holidays
    update_with_holidays(holiday_sheet_file)
    
    print("All steps completed successfully. Final file: updated_working_days.csv")

if __name__ == "__main__":
    main()
