# medium_error_data.py
import random
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

m, b = 2, 5
data = []

for i in range(50):
    x = i * 0.5
    error = random.uniform(0.3, 1.0)
    y = m * x + b + random.uniform(-1, 1)
    data.append((x, y, error))

with open("medium_error_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y", "error"])
    writer.writerows(data)

print("Medium error data saved to medium_error_data.csv")

df = pd.read_csv("medium_error_data.csv")
x = df["x"].values
y = df["y"].values
err = df["error"].values

# Weighted fit
weights = 1 / (err ** 2)
m_fit, b_fit = np.polyfit(x, y, 1, w=weights)

plt.errorbar(x, y, yerr=err, fmt="o", color="blue", capsize=5, label="Data with Error Bars")
plt.plot(x, m_fit*x + b_fit, color="red", label="Weighted Best Fit Line")
plt.plot(x, 2*x + 5, "--", color="green", label="True Line")
plt.legend()
plt.title("Medium Sized Plot (50 Points, Error Bars)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("medium_error_plot.png")
plt.show()

print("Medium error plot saved as medium_error_plot.png")
