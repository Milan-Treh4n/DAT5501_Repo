import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import math

# Load data
df = pd.read_csv("life_expectancy.csv")
df = df.rename(columns={"Period life expectancy at birth": "Life_Expectancy"})

# Filter out continents
continents = ["Africa", "Asia", "Europe", "Oceania"]
df_filtered = df[~df["Entity"].isin(continents)]

avg_le = df_filtered.groupby("Year")["Life_Expectancy"].mean()
years = avg_le.index.values
values = avg_le.values

# Split into training and testing
train_years = years[:-10]
train_vals = values[:-10]

N = len(train_years)
sigma = 0.01 * train_vals  

# Choosing the best polynomial order from model tests

best_order = 6

print(f"Using best polynomial order: {best_order}")

# Fit polynomial model
poly_coeffs, poly_cov = np.polyfit(train_years, train_vals, best_order, cov=True)

print("\n=== Polynomial Parameter Values ===")
print(poly_coeffs)

print("\n=== Polynomial Covariance Matrix ===")
print(poly_cov)

# Parameter uncertainties are sqrt of diagonal
poly_uncertainties = np.sqrt(np.diag(poly_cov))
print("\n=== Parameter Uncertainties ===")
print(poly_uncertainties)

# --------------------------------------------------------------
# Fit an exponential model
# --------------------------------------------------------------

def exp_model(x, a, b, c):
    return a * np.exp(b * (x - x.min())) + c
initial_guess = [1, 0.01, 50]

try:
    params_exp, cov_exp = curve_fit(exp_model, train_years, train_vals, p0=initial_guess, sigma=sigma, absolute_sigma=True)
    exp_uncertainties = np.sqrt(np.diag(cov_exp))

    print("\n=== Exponential Model Parameters ===")
    print(params_exp)

    print("\n=== Exponential Covariance Matrix ===")
    print(cov_exp)

    print("\n=== Exponential Parameter Uncertainties ===")
    print(exp_uncertainties)

except RuntimeError:
    print("Exponential model failed to converge.")
    params_exp = None

# --------------------------------------------------------------
# Compute BIC for comparison
# --------------------------------------------------------------

def compute_bic(y_obs, y_model, sigma, num_params):
    residuals = (y_obs - y_model) / sigma
    chi2 = np.sum(residuals**2)
    k = num_params
    n = len(y_obs)
    return n * np.log(chi2/n) + k * np.log(n)

# Polynomial prediction
poly = np.poly1d(poly_coeffs)
y_poly_pred = poly(train_years)

bic_poly = compute_bic(train_vals, y_poly_pred, sigma, best_order + 1)

print(f"\nBIC (Polynomial order {best_order}): {bic_poly:.3f}")

# Exponential prediction & BIC
if params_exp is not None:
    y_exp_pred = exp_model(train_years, *params_exp)
    bic_exp = compute_bic(train_vals, y_exp_pred, sigma, 3)
    print(f"BIC (Exponential model): {bic_exp:.3f}")
else:
    bic_exp = None

# Summary
print("\n=== Model Comparison ===")
if bic_exp is None:
    print("Polynomial model is best (exponential failed).")
elif bic_poly < bic_exp:
    print(f"Polynomial (order {best_order}) is best according to BIC.")
else:
    print("Exponential model is best according to BIC.")
