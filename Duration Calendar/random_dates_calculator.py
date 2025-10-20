import datetime
import numpy as np

file_path = 'random_dates.csv'
file_path = np.numpy64

def dates_in_past(file_path):
    for dates in file_path:
        if dates < np.datetime64(datetime.datetime.now().date()):
            print(f"{dates} is in the past.")
        else:
            print(f"{dates} is not in the past.")