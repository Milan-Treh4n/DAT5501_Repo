import os
import datetime
import numpy as np
import csv

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'random_dates.csv')

def dates_in_past(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        dates = [row[0] for row in reader]

    today = np.datetime64(datetime.datetime.now().date())

    for date_str in dates:
        try:
            # Parse the DD/MM/YYYY format
            date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            date_np = np.datetime64(date_obj)  # convert to numpy datetime64
        except ValueError:
            print(f"Invalid date format: {date_str}")
            continue

        days_diff = int((today - date_np).astype(int))
        if days_diff > 0:
            print(f"{date_str} is in the past ({days_diff} days ago).")
        elif days_diff < 0:
            print(f"{date_str} is in the future ({-days_diff} days from now).")
        else:
            print(f"{date_str} is today.")

# Run the function
dates_in_past(file_path)


