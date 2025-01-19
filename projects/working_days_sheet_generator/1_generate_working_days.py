import pandas as pd
from datetime import datetime, timedelta

def generate_working_days(start_date, end_date, output_file="working_days.csv"):
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
    df.to_csv(output_file, index=False)
    print(f"Working days CSV generated: {output_file}")

# Usage
generate_working_days("2025-01-01", "2025-12-31")
