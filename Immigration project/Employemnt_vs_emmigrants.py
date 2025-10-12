import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Set the working directory to where this script is located
script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# Load the two CSV files
employment_file = 'employment_services_uk.csv'
emigration_file = 'UK_emmigrants_data.csv'

employment = pd.read_csv(employment_file)
emigration = pd.read_csv(emigration_file)

# Clean column names to remove any extra spaces
employment.columns = employment.columns.str.strip()
emigration.columns = emigration.columns.str.strip()

# Convert numbers stored as strings with commas into floats
def clean_numbers(column):
    return column.apply(lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x)

for col in employment.columns[1:]:
    employment[col] = clean_numbers(employment[col])

for col in emigration.columns[1:]:
    emigration[col] = clean_numbers(emigration[col])

# Remove any rows that contain missing values
employment.dropna(inplace=True)
emigration.dropna(inplace=True)

# Make sure the 'Year' column is an integer for merging
employment['Year'] = employment['Year'].astype(int)
emigration['Year'] = emigration['Year'].astype(int)

# Merge the two datasets by 'Year'
merged = pd.merge(employment, emigration, on='Year')
merged.set_index('Year', inplace=True)

# Format large numbers on the Y-axis to show in millions
def millions(x, pos):
    return f'{x/1e6:.1f}M'

# Create the figure and first Y-axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot employment as bars
ax1.bar(
    merged.index,
    merged['Approx total number of employees'],
    color='silver',
    alpha=0.8,
    label='Total Employment'
)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Total Employment (in millions)', fontsize=12)
ax1.tick_params(axis='y')
ax1.yaxis.set_major_formatter(FuncFormatter(millions))

# Create a second Y-axis and plot emigration as a line
ax2 = ax1.twinx()
ax2.plot(
    merged.index,
    merged['Total number of emmigrants'],
    color='purple',
    marker='o',
    linewidth=2.5,
    label='Total Emigration'
)
ax2.set_ylabel('Total Emigration (in millions)', fontsize=12)
ax2.tick_params(axis='y')
ax2.yaxis.set_major_formatter(FuncFormatter(millions))

# Add a title and improve readability
plt.title('UK Employment vs Emigration Over Time', fontsize=16, fontweight='bold')
plt.xticks(rotation=45)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Combine legends from both axes
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left')

plt.tight_layout()
plt.savefig('employment_vs_emigration.png')
plt.show()












