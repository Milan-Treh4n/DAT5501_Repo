import pandas as pd
import numpy as np
import sys
import warnings
import matplotlib.pyplot as plt
import os

#  Data Loading and Preparation
warnings.filterwarnings("ignore", category=np.RankWarning)
# Locate the CSV file
csv_name = "life_expectancy.csv"
script_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
csv_path = os.path.join(script_dir, csv_name)

# If not found, search up to 3 levels up
if not os.path.exists(csv_path):
    parent = script_dir
    for _ in range(3):
        parent = os.path.dirname(parent)
        candidate = os.path.join(parent, csv_name)
        if os.path.exists(candidate):
            csv_path = candidate
            break

if not os.path.exists(csv_path):
    print(f"Error: '{csv_name}' not found near {script_dir}")
    print("Place the CSV in the same folder as this script or in a parent folder.")
    sys.exit(1)

# Load the dataset
df = pd.read_csv(csv_path)

# Rename the long column for easier use
df.rename(columns={
    'Period life expectancy at birth': 'LifeExpectancy'
}, inplace=True)

# Define the list of continents to analyse
continents = ['Africa', 'Asia', 'Europe', 'Oceania']

# Filter the DataFrame to only include continent data
df_continents = df[df['Entity'].isin(continents)].copy()

if df_continents.empty:
    print("Error: No continent data found in the dataset.")
    sys.exit()

# Create output folder for plots
os.makedirs("plots", exist_ok=True)

#  Main analysis per continent
for continent in continents:
    try:
        continent_data_series = df_continents[
            df_continents['Entity'] == continent
        ].set_index('Year')['LifeExpectancy'].sort_index()
        
        if continent_data_series.empty:
            continue 
    except Exception:
        continue

# Extract years and data
    all_years = np.array(continent_data_series.index)

    if len(all_years) < 11:
        continue

    print(f"\n=======================================================")
    print(f"--- Analysing Continent: {continent.upper()} ---")
    print(f"=======================================================")

    training_years = all_years[:-10]
    training_data = np.array(continent_data_series.loc[training_years])

# Forecasting years and actual data
    future_years = all_years[-10:]
    actual_data = np.array(continent_data_series.loc[future_years])

    print(f"Training on {len(training_years)} years (from {training_years[0]} to {training_years[-1]}).")
    print(f"Forecasting 10 years (from {future_years[0]} to {future_years[-1]}).")

    # Create clean comparison plot
    plt.figure(figsize=(10, 6))

# Plot actual data points
    for degree in range(1, 10):
        try:
            model_coeffs = np.polyfit(training_years, training_data, degree)
            p = np.poly1d(model_coeffs)
            forecast_values = p(future_years)
        except np.RankWarning:
            continue

        # Print the forecast table for this order
        print(f"\n--- Forecast (Order {degree}): {continent} ---")
        print(" Year | Forecast | Actual")
        print("---------------------------------")
        for i in range(len(future_years)):
            year = future_years[i]
            forecast = forecast_values[i]
            actual = actual_data[i]
            print(f" {year} | {forecast:8.2f} | {actual:7.2f}")

        # Add the forecast line to the plot
        plt.plot(future_years, forecast_values, label=f"Order {degree}")

    # Finalise and save the plot
    plt.title(f"{continent} - Polynomial Forecast Comparison (Orders 1–9)")
    plt.xlabel("Year")
    plt.ylabel("Forecasted Life Expectancy at Birth")
    plt.legend(title="Polynomial Order", fontsize="small", ncol=3)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    plot_path = f"plots/{continent.replace(' ', '_')}_forecast_comparison.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f" Saved plot: {plot_path}")

    plt.show()
    plt.close()

print("\nAnalysis complete. All plots saved in the 'plots' folder.")





