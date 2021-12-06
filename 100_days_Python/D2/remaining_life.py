age = input("What is your current age? ")

max_age = 90
rem_age = max_age - int(age)
rem_months = rem_age * 12
rem_weeks = rem_age * 52
rem_days = rem_age * 365

print(
    f'You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left.')
