import datetime
import numpy as np

# Get user input for a date
user_input_date = input("Enter a date (YYYY-MM-DD): ")

# Convert the input string to a numpy datetime64 object
user_input_date = np.datetime64(user_input_date)

# Get the current date as a numpy datetime64 object
current_date = np.datetime64(datetime.datetime.now().date())

# Calculate the difference in days
date_difference = current_date - user_input_date
print(f"The difference in days is: {date_difference.astype(int)} days")