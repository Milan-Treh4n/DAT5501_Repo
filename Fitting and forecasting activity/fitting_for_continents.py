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
    'Period life expectancy at birth': 'LifeExpectancy'
}, inplace=True)

# Define the list of continents to analyse
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']

# Filter the DataFrame to only include continent data
df_continents = df[df['Entity'].isin(continents)].copy()

if df_continents.empty:
    print("Error: Could not find any continent data in the 'Entity' column.")
    print("Looked for:", continents)
    sys.exit()

print(f"Found continent data. Analyzing {len(continents)} continents...")


#  Main Analysis Loop (per continent) 
for continent in continents:
    print(f"\n=======================================================")
    print(f"--- Analyzing Continent: {continent.upper()} ---")
    print(f"=======================================================")

   #  Data Extraction (for this continent)
    try:
        continent_data_series = df_continents[
            df_continents['Entity'] == continent
        ].set_index('Year')['LifeExpectancy'].sort_index()
        
        if continent_data_series.empty:
            print(f"No data found for {continent}.")
            continue # Skip to the next continent
    except Exception as e:
        print(f"Error processing data for {continent}: {e}")
        continue
# Data Splitting (Training and Forecasting Sets)
    all_years = np.array(continent_data_series.index)

    # Check if there is enough data to split
    if len(all_years) < 11:
        print(f"Skipping {continent}: Not enough data (need > 10 years).")
        continue
# The 'past' (training data) is all years except the last 10
    training_years = all_years[:-10]
    training_data = np.array(continent_data_series.loc[training_years])

    # The 'future' (forecast data) is the last 10 years we held out
    future_years = all_years[-10:]
    actual_data = np.array(continent_data_series.loc[future_years])

    print(f"Training on {len(training_years)} years (from {training_years[0]} to {training_years[-1]}).")
    print(f"Forecasting 10 years (from {future_years[0]} to {future_years[-1]}).")

#  Polynomial Fitting and Forecasting (for degrees 1 to 9)
    for degree in range(1, 10):
        # Fit a polynomial model of the specified degree to the training data
        model_coeffs = np.polyfit(training_years, training_data, degree)
        
        # Create a polynomial function from the model's coefficients
        p = np.poly1d(model_coeffs)
        
        # Use the function to forecast the 10 'future' years
        forecast_values = p(future_years)
        
        # --- Print the Results ---

        print(f"\n--- Forecast (Order {degree}): {continent} ---")
        print(" Year | Forecast |  Actual")
        print("---------------------------------")
        
        # Loop through the 10 future years and print the forecast vs. actual
        for i in range(len(future_years)):
            year = future_years[i]
            forecast = forecast_values[i]
            actual = actual_data[i]
            print(f" {year} | {forecast:8.2f} | {actual:7.2f}")

print("\nAnalysis complete.")