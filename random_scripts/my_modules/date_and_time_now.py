from datetime import datetime


def date_and_time_today():
    """Today is 2015-09-17 and it is 09:34:35."""
    now = datetime.now()
    print(f'Today is {now.strftime("%G-%m-%d")} and it is {now.strftime("%H:%M:%S")}.')


if __name__ == "__main__":
    date_and_time_today()
