import datetime
import numpy as np

def calculate_days_difference(date_str: str) -> int:
    """Calculate how many days between a given date and today."""
    try:
        input_date = np.datetime64(date_str)
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    today = np.datetime64(datetime.datetime.now().date())
    return int((today - input_date).astype(int))

# Run when script executes
user_date = input("Enter a date (YYYY-MM-DD): ")
try:
    days = calculate_days_difference(user_date)
    print(f"The difference between {user_date} and today is {days} days.")
except ValueError as error:
    print(error)


