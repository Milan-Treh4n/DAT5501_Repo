import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data_with_error.csv")
x, y, err = df["x"], df["y"], df["error"]

# Weighted least squares fit: weights = 1 / error²
weights = 1 / err**2
m_fit, b_fit = np.polyfit(x, y, 1, w=weights)

plt.errorbar(x, y, yerr=err, fmt="o", label="Data with error bars")
plt.plot(x, m_fit*x + b_fit, color="red", label="Weighted best fit")
plt.legend()
plt.savefig("fit_with_error.png")
