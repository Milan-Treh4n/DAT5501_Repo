import os
import pandas as pd
import matplotlib.pyplot as plt

# --- Ensure Python reads files from the same folder as this script ---
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)  # Change working directory to script location

# --- File paths (relative to this folder) ---
file_path = 'employment_services_uk.csv'
file_path2 = 'UK_emmigrants_data.csv'

# --- Load datasets ---
employment = pd.read_csv(file_path)
emigration = pd.read_csv(file_path2)

# --- Clean and preprocess the data ---
for col in employment.columns[1:]:
    employment[col] = employment[col].apply(
        lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x
    )

for col in emigration.columns[1:]:
    emigration[col] = emigration[col].apply(
        lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x
    )

# --- Drop rows with missing data ---
employment.dropna(inplace=True)
emigration.dropna(inplace=True)

# --- Ensure Year column is integer type ---
employment['Year'] = employment['Year'].astype(int)
emigration['Year'] = emigration['Year'].astype(int)

# --- Merge datasets on Year ---
merged_data = pd.merge(
    employment, emigration, on='Year', suffixes=('_employment', '_emigration')
)
merged_data.set_index('Year', inplace=True)

# --- Plotting the data ---
plt.figure(figsize=(14, 7))

plt.plot(
    merged_data.index,
    merged_data['Total_employment'],
    label='Total Employment',
    color='blue',
    marker='o'
)

plt.plot(
    merged_data.index,
    merged_data['Total_emigration'],
    label='Total Emigration',
    color='red',
    marker='o'
)

# --- Graph styling ---
plt.title('UK Employment vs Emigration Over Years', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# --- Show the plot ---
plt.show()

