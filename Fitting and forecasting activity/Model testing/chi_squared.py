import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Locate CSV file
script_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
csv_path = os.path.join(script_dir, "life_expectancy.csv")

# If not found, search up to 3 levels up
if not os.path.exists(csv_path):
    parent = script_dir
    for _ in range(3):
        parent = os.path.dirname(parent)
        candidate = os.path.join(parent, "life_expectancy.csv")
        if os.path.exists(candidate):
            csv_path = candidate
            break

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"life_expectancy.csv not found near {script_dir}")

# Load CSV 
data = pd.read_csv(csv_path)

# Rename for easier references
data = data.rename(columns={"Period life expectancy at birth": "Life_Expectancy"})

# Continents to exclude for global average
continents = ["Africa", "Asia", "Europe", "Oceania"]

# Keep only countries (exclude continents)
filtered = data[~data["Entity"].isin(continents)]

# Compute average life expectancy per year
avg_le = filtered.groupby("Year")["Life_Expectancy"].mean()

# Convert to arrays
all_years = avg_le.index.values
all_values = avg_le.values

# Training = all but last 10 years
training_years = all_years[:-10]
training_data = all_values[:-10]

# Number of data points in training set
N = len(training_years)

# Assume 1% relative uncertainties
sigma = 0.01 * training_data

orders = range(1, 10)
chi2_per_dof = []

print("Computing chi-squared per degree of freedom using training data only:\n")

for deg in orders:
    # Fit polynomial on training data only
    coeffs = np.polyfit(training_years, training_data, deg)
    poly = np.poly1d(coeffs)
    
    # Model evaluated on training data
    model_pred = poly(training_years)
    
    # Compute chi-squared
    chi2 = np.sum(((training_data - model_pred) / sigma) ** 2)
    dof = N - (deg + 1)
    chi2_nu = chi2 / dof
    chi2_per_dof.append(chi2_nu)
    
    print(f"Order {deg}: χ²/ν = {chi2_nu:.4f}")

# Save plot directory
os.makedirs("plots_chi2", exist_ok=True)

# Plot chi-squared per degree of freedom
plt.figure(figsize=(8, 5))
plt.plot(orders, chi2_per_dof, marker="o")
plt.title("Chi-squared per Degree of Freedom (Training Data)")
plt.xlabel("Polynomial Order")
plt.ylabel("χ² per Degree of Freedom")
plt.grid(True)
plt.savefig("plots_chi2/chi2_vs_order.png", dpi=300)
plt.close()

# Determine the best order
best_order = orders[np.argmin(chi2_per_dof)]
best_value = min(chi2_per_dof)

print(f"\nBest-fitting model: Polynomial order {best_order} with χ²/ν = {best_value:.4f}")
print("Plot saved to: plots_chi2/chi2_vs_order.png")




