# large_error_data.py
import random
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

m, b = 2, 5
data = []

for i in range(100):
    x = i * 0.3
    error = random.uniform(0.3, 1.0)
    y = m * x + b + random.uniform(-1, 1)
    data.append((x, y, error))

with open("large_error_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y", "error"])
    writer.writerows(data)

print("Large error data saved to large_error_data.csv")

df = pd.read_csv("large_error_data.csv")
x = df["x"].values
y = df["y"].values
err = df["error"].values

weights = 1 / (err ** 2)
m_fit, b_fit = np.polyfit(x, y, 1, w=weights)

plt.errorbar(x, y, yerr=err, fmt="o", color="blue", capsize=5, label="Data with Error Bars")
plt.plot(x, m_fit*x + b_fit, color="red", label="Weighted Best Fit Line")
plt.plot(x, 2*x + 5, "--", color="green", label="True Line")
plt.legend()
plt.title("Large Sized Plot (100 Points, Error Bars)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("large_error_plot.png")
plt.show()

print("Large error plot saved as large_error_plot.png")
