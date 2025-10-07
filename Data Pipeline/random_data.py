import random
import csv

m, b = 2, 5  # true slope and intercept
data = []

for x in range(10):
    y = m * x + b + random.uniform(-1, 1)  # add random noise
    data.append((x, y))

# Save to CSV
with open("random_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    writer.writerows(data)

print("random_data.csv saved")
