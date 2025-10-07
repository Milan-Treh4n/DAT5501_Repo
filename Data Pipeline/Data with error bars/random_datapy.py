import random
import csv

# True line parameters
m, b = 2, 5
data = []

# Generate data with random noise and error bars
for x in range(10):
    # normal noise and an "error bar" value
    error = random.uniform(0.3, 1.0)  # random uncertainty for each point
    y = m * x + b + random.uniform(-1, 1)

    # add an occasional outlier
    if x in [3, 7]:  # 2 outliers for demonstration
        y += random.uniform(10, 15)

    data.append((x, y, error))

# Save to CSV
with open("random_data_with_outliers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y", "error"])  # column headers
    writer.writerows(data)

print("Data with outliers and errors saved to random_data_with_outliers.csv")
