import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Set working directory
script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# Load the CSV files
employment = pd.read_csv('employment_services_uk.csv')
emigration = pd.read_csv('UK_emmigrants_data.csv')

# Clean column names and numbers
for df in [employment, emigration]:
    df.columns = df.columns.str.strip()
    for col in df.columns[1:]:
        df[col] = df[col].apply(lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x)
    df.dropna(inplace=True)
    df['Year'] = df['Year'].astype(int)

# Merge on Year
merged = pd.merge(employment, emigration, on='Year').set_index('Year')

# Format y-axis in millions
def millions(x, pos):
    return f'{x/1e6:.1f}M'

# Plot
plt.figure(figsize=(12, 6))

# Employment line (purple)
plt.plot(
    merged.index,
    merged['Approx total number of employees'],
    color='red',
    linewidth=2.5,
    marker='o',
    label='Total Employment'
)

# Emigration line (teal for contrast)
plt.plot(
    merged.index,
    merged['Total number of emmigrants'],
    color='teal',
    linewidth=2.5,
    marker='o',
    label='Total Emigration'
)

plt.title('UK Employment vs Emigration (Same Scale)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of People (in millions)', fontsize=12)
plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('employment_vs_emigration_same_scale.png')
plt.show()