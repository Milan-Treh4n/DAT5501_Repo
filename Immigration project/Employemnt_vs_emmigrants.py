import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# --- Set working directory to the script folder ---
script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# --- Load data ---
employment_file = 'employment_services_uk.csv'
emigration_file = 'UK_emmigrants_data.csv'

employment = pd.read_csv(employment_file)
emigration = pd.read_csv(emigration_file)

# --- Clean column names ---
employment.columns = employment.columns.str.strip()
emigration.columns = emigration.columns.str.strip()

# --- Convert numeric strings with commas to float ---
def clean_numbers(column):
    return column.apply(lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x)

for col in employment.columns[1:]:
    employment[col] = clean_numbers(employment[col])
for col in emigration.columns[1:]:
    emigration[col] = clean_numbers(emigration[col])

# --- Drop missing values and ensure Year is integer ---
employment.dropna(inplace=True)
emigration.dropna(inplace=True)
employment['Year'] = employment['Year'].astype(int)
emigration['Year'] = emigration['Year'].astype(int)

# --- Merge datasets by Year ---
merged = pd.merge(employment, emigration, on='Year')
merged.set_index('Year', inplace=True)

# --- Format Y-axis as millions ---
def millions(x, pos):
    return f'{x/1e6:.1f}M'

# --- Plot: Employment (left axis) vs Emigration (right axis) ---
fig, ax1 = plt.subplots(figsize=(12, 6))

# Employment (bars)
ax1.bar(
    merged.index,
    merged['Approx total number of employees'],
    color='silver',
    alpha=0.7,
    label='Total Employment'
)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Total Employment (in millions)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.set_major_formatter(FuncFormatter(millions))

# Emigration (line)
ax2 = ax1.twinx()
ax2.plot(
    merged.index,
    merged['Total number of emmigrants'],
    color='purple',
    marker='o',
    linewidth=2,
    label='Total Emigration'
)
ax2.set_ylabel('Total Emigration (in millions)', color='purple', fontsize=12)
ax2.tick_params(axis='y', labelcolor='purple')
ax2.yaxis.set_major_formatter(FuncFormatter(millions))

# --- Title and styling ---
plt.title(
    'UK Employment vs Emigration Over Time',
    fontsize=16,
    fontweight='bold'
)
plt.xticks(rotation=45)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Combine legends
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left')

plt.tight_layout()
plt.show()










