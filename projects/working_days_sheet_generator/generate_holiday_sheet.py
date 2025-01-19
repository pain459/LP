import pandas as pd

# Standard Indian Holidays for 2025
indian_holidays = [
    {"date": "2025-01-01", "holiday_name": "New Year's Day"},
    {"date": "2025-01-14", "holiday_name": "Makar Sankranti / Pongal"},
    {"date": "2025-01-26", "holiday_name": "Republic Day"},
    {"date": "2025-03-17", "holiday_name": "Holi"},
    {"date": "2025-04-14", "holiday_name": "Ambedkar Jayanti"},
    {"date": "2025-04-18", "holiday_name": "Good Friday"},
    {"date": "2025-05-01", "holiday_name": "May Day / Maharashtra Day"},
    {"date": "2025-08-15", "holiday_name": "Independence Day"},
    {"date": "2025-10-02", "holiday_name": "Gandhi Jayanti"},
    {"date": "2025-10-21", "holiday_name": "Dussehra"},
    {"date": "2025-11-01", "holiday_name": "Diwali (Deepavali)"},
    {"date": "2025-11-15", "holiday_name": "Bhai Dooj"},
    {"date": "2025-12-25", "holiday_name": "Christmas Day"}
]

# Convert to DataFrame
holiday_df = pd.DataFrame(indian_holidays)

# Save to CSV
holiday_csv_path = "holiday_sheet.csv"
holiday_df.to_csv(holiday_csv_path, index=False)
holiday_csv_path
