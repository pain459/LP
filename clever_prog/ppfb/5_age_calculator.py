# This program will calculate the age of the perform after taking input of year, month, date.

import datetime

print("Welcome to the age calculator")


def _prompt_age():
    _year = int(input("Enter the year of birth: "))
    _month = int(input("Enter the month of birth: "))
    _day = int(input("Enter the day of birth: "))
    _dob = datetime.date(_year, _month, _day)
    # print("Entered DOB is", _dob)
    return _dob


def _today():
    _current_day = datetime.date.today()
    return _current_day


def _calculate_age(_dob, _today):
    _age = int((_today - _dob).days / 365.25)  # Logic to calculate age in days.
    return _age


if __name__ == "__main__":
    # _prompt_age()
    print("Calculated age is", _calculate_age(_prompt_age(), _today()))
