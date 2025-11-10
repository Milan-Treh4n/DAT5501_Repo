import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import perf_counter

# read cleaned data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'cleaned_apple_data.csv')
df = pd.read_csv(csv_path)

# Ensure numeric and compute daily changes
df['Close/Last'] = pd.to_numeric(df['Close/Last'], errors='coerce')
delta = df['Close/Last'].diff().dropna().to_numpy()  # length L

# n values to test sorting time
max_n = min(365, len(delta))
ns = np.arange(7, max_n + 1)

times = []
# use a small repeat to average timing noise
for n in ns:
    arr = delta[:n].astype(float)  # view of first n deltas
    # warm up
    np.sort(arr)
    repeats = 20
    t0 = perf_counter()
    for _ in range(repeats):
        _ = np.sort(arr)
    t = (perf_counter() - t0) / repeats
    times.append(t)

ns = np.array(ns)
times = np.array(times)

# Fit times to n log n
nlog = ns * np.log2(ns)
c = (times @ nlog) / (nlog @ nlog)
pred = c * nlog

# Plot results
plt.figure(figsize=(8,5))
plt.plot(ns, times, label='Measured sort time (s)', marker='o', markersize=4)
plt.plot(ns, pred, label=f'scaled n·log2(n) (c={c:.3e})', linestyle='--')
plt.xlabel('n (number of ΔP elements sorted)')
plt.ylabel('Time (seconds)')
plt.title('Sorting time T vs n (ΔP) — compare with n·log n')
plt.legend()
plt.grid(True)
out = os.path.join(script_dir, 'daily_sorting_t_vs_n.png')
plt.tight_layout()
plt.savefig(out)
print(f'Plot saved to: {out}')
print(f'n range: {ns[0]}..{ns[-1]}, fitted scale c={c:.3e}')
print(f'Average T/(n·log2 n): {np.mean(times / nlog):.3e}')