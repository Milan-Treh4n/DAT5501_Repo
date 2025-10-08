import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("random_data.csv")
x = df["x"].values
y = df["y"].values

# Fit a line (least-squares)
m_fit, b_fit = np.polyfit(x, y, 1)

# Print fitted values
print(f"Fitted slope (m): {m_fit:.2f}")
print(f"Fitted intercept (b): {b_fit:.2f}")

# Plot data and fitted line
plt.scatter(x, y, label="Data", color="blue")
plt.plot(x, m_fit*x + b_fit, color="red", label="Line of best fit")
plt.plot(x, 2*x + 5, "--", color="green", label="True Line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Line Fit to Random Data")
plt.savefig("fit_plot.png")
plt.show()

print("Plot.png")
