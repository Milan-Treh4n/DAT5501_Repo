# large_normal_data.py
import random
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

m, b = 2, 5
data = []

# Generate 100 data points
for i in range(100):
    x = i * 0.3  # 0, 0.3, 0.6, ...
    y = m * x + b + random.uniform(-0.8, 0.8)
    data.append((x, y))

with open("large_normal_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    writer.writerows(data)

print("Large normal data saved to large_normal_data.csv")

df = pd.read_csv("large_normal_data.csv")
x = df["x"].values
y = df["y"].values
m_fit, b_fit = np.polyfit(x, y, 1)

plt.scatter(x, y, color="blue", label="Data")
plt.plot(x, m_fit*x + b_fit, color="red", label="Best Fit Line")
plt.plot(x, 2*x + 5, "--", color="green", label="True Line")
plt.legend()
plt.title("Large Sized Plot (100 Points)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("large_normal_plot.png")
plt.show()

print("Large normal plot saved as large_normal_plot.png")
