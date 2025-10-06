import numpy as np
import pandas as pd

# Parameters
m, b = 2, 5
x = np.linspace(0, 10, 100)

# Random errors for each point (like standard deviation of measurement)
errors = np.random.uniform(0.5, 1.5, size=len(x))

# Generate noisy data based on those errors
noise = np.random.normal(0, errors)
y = m * x + b + noise

# Save to CSV
df = pd.DataFrame({"x": x, "y": y, "error": errors})
df.to_csv("data_with_error.csv", index=False)
