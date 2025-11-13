import pandas as pd
import numpy as np
import sys
import warnings

# Data Loading and Preparation

warnings.filterwarnings("ignore", category=np.RankWarning)

# Try to load the dataset
try:
    df = pd.read_csv("life_expectancy.csv")
except FileNotFoundError:
    print("Error: 'life_expectancy.csv' not found.")
    print("Please make sure the file is in the same directory as the script.")
    sys.exit() # Exit the script if the file isn't found
except Exception as e:
    print(f"An error occurred while loading the file: {e}")
    sys.exit()

# Rename the long column for easier use
df.rename(columns={
    'Period life expectancy at birth': 'Life_Expectancy'
}, inplace=True)

print("Data loaded. Calculating global average life expectancy per year...")

# Group by 'Year' and get the mean 'Life_Expectancy'
avg_le_by_year = df.groupby('Year')['Life_Expectancy'].mean()

# Get all unique years from new data and sort them
all_years = np.array(avg_le_by_year.index.sort_values())
# Prepare the 'M' values (independent variable)
training_M = all_years[:-10]  # All years except the last 10
training_years = all_years[:-10]
training_data = np.array(avg_le_by_year.loc[training_years])
# Prepare the 'future' years (last 10 years)
future_years = all_years[-10:]
actual_data = np.array(avg_le_by_year.loc[future_years])

print(f"Training on {len(training_years)} years (from {training_years[0]} to {training_years[-1]}).")
print(f"Forecasting 10 years (from {future_years[0]} to {future_years[-1]}).")

# Polynomial Regression and Forecasting
for degree in range(1, 10):
    # Fit a polynomial model of the specified degree
    model_coeffs = np.polyfit(training_M, training_data, degree)
    
    # Create a polynomial function from the model's coefficients
    p = np.poly1d(model_coeffs)
    
    # Use the function to forecast the 10 'future' years
    forecast_values = p(future_years)
    
    # --- Print the Results ---
    
    print(f"\n--- Forecast: Polynomial Order {degree} ---")
    print(" Year | Forecast |  Actual")
    print("---------------------------------")
    
    # Loop through the 10 future years and print the forecast vs. actual
    for i in range(len(future_years)):
        year = future_years[i]
        forecast = forecast_values[i]
        actual = actual_data[i]
        print(f" {year} | {forecast:8.2f} | {actual:7.2f}")

print("\nAnalysis complete.")
