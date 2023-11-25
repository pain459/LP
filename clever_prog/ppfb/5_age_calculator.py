# This program will calculate the age of the perform after taking input of year, month, date.

import datetime

print("Welcome to the age calculator")
_year = int(input("Enter the year of birth: "))
_month = int(input("Enter the month of birth: "))
_day = int(input("Enter the day of birth: "))
_dob = datetime.date(_year, _month, _day)

print("Enter DOB is", _dob)

_today = datetime.date.today()

_age = int((_today - _dob).days / 365.25) # Logic to calculate age in days.

print("Calculated age is", _age)