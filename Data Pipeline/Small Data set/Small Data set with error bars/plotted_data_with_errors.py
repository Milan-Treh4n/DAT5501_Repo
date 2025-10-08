import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the new data
df = pd.read_csv("random_data_with_outliers.csv")
x = df["x"].values
y = df["y"].values
err = df["error"].values

# Weighted least squares fit (accounts for error bars)
weights = 1 / (err**2)
m_fit, b_fit = np.polyfit(x, y, 1, w=weights)

print(f"Fitted slope (m): {m_fit:.2f}")
print(f"Fitted intercept (b): {b_fit:.2f}")

# Plot data with error bars
plt.errorbar(x, y, yerr=err, fmt="o", label="Data with error bars", capsize=5)
plt.plot(x, m_fit*x + b_fit, color="orange", label="Line of best fit")
plt.plot(x, 2*x + 5, "--", color="green", label="True line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Line Fit with Outliers and Error Bars")
plt.savefig("fit_with_outliers_and_errors.png")
plt.show()

print("Plot saved as fit_with_outliers_and_errors.png")
