import pandas as pd
import numpy as np
import sys
import warnings

#  Data Loading and Preparation
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

# Define the list of continents to exclude
continents_to_exclude = ['Africa', 'Asia', 'Europe', 'Oceania']

# Filter the DataFrame to exclude continent data
df_filtered = df[~df['Entity'].isin(continents_to_exclude)].copy()

if df_filtered.empty:
    print("Error: Filtering out continents left no data.")
    sys.exit()

print("Data loaded. Calculating average life expectancy (excluding continents)...")

# Calculate average life expectancy per year, excluding continents
avg_le_by_year = df_filtered.groupby('Year')['Life_Expectancy'].mean()

if avg_le_by_year.empty:
    print("Error: Could not calculate average life expectancy from filtered data.")
    sys.exit()

#  Data Splitting (Training and Forecasting Sets)
all_years = np.array(avg_le_by_year.index.sort_values())

# Check if there is enough data to split
if len(all_years) < 11:
    print(f"Error: Not enough data (need > 10 years). Found only {len(all_years)}.")
    sys.exit()

# Prepare the 'training' data
training_years = all_years[:-10]  # All years except the last 10
training_data = np.array(avg_le_by_year.loc[training_years])

# Prepare the 'future' years (last 10 years)
future_years = all_years[-10:]
actual_data = np.array(avg_le_by_year.loc[future_years])

print(f"Training on {len(training_years)} years (from {training_years[0]} to {training_years[-1]}).")
print(f"Forecasting 10 years (from {future_years[0]} to {future_years[-1]}).")

#  Polynomial Fitting and Forecasting
for degree in range(1, 10):
    # Fit a polynomial model of the specified degree to the training data
    model_coeffs = np.polyfit(training_years, training_data, degree)
    
    # Create a polynomial function from the model's coefficients
    p = np.poly1d(model_coeffs)
    
    # Use the function to forecast the 10 'future' years
    forecast_values = p(future_years)
    
    # --- Print the Results ---
    
    print(f"\n--- Forecast (Order {degree}): Avg. (Excl. Continents) ---")
    print(" Year | Forecast |  Actual")
    print("---------------------------------")
    
    # Loop through the 10 future years and print the forecast vs. actual
    for i in range(len(future_years)):
        year = future_years[i]
        forecast = forecast_values[i]
        actual = actual_data[i]
        print(f" {year} | {forecast:8.2f} | {actual:7.2f}")

print("\nAnalysis complete.")
