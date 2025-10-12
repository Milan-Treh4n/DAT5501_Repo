import os
import pandas as pd
import matplotlib.pyplot as plt

# --- Ensure Python reads files from the same folder as this script ---
# This helps make the script portable.
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)  # Change working directory to script location

# --- File paths (relative to this folder) ---
file_path = 'employment_services_uk.csv'
file_path2 = 'UK_emmigrants_data.csv'

# --- Load datasets ---
employment = pd.read_csv(file_path)
emigration = pd.read_csv(file_path2)

# --- Best practice: Clean column names to remove leading/trailing spaces ---
employment.columns = employment.columns.str.strip()
emigration.columns = emigration.columns.str.strip()

# --- Clean and preprocess the data ---
# Convert columns with numbers (stored as strings with commas) to float type
for col in employment.columns[1:]:
    if employment[col].dtype == 'object': # Apply only to object type columns
        employment[col] = employment[col].apply(
            lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x
        )

for col in emigration.columns[1:]:
    if emigration[col].dtype == 'object': # Apply only to object type columns
        emigration[col] = emigration[col].apply(
            lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x
        )

# --- Drop rows with missing data ---
employment.dropna(inplace=True)
emigration.dropna(inplace=True)

# --- Ensure Year column is integer type for accurate merging ---
employment['Year'] = employment['Year'].astype(int)
emigration['Year'] = emigration['Year'].astype(int)

# --- Merge datasets on the 'Year' column ---
merged_data = pd.merge(
    employment, emigration, on='Year'
)
merged_data.set_index('Year', inplace=True)

# --- Plotting the data with a Combination Bar and Line Chart ---
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot Total Employment as a Bar Chart on the primary Y-axis (ax1)
color = 'tab:blue'
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Total Employment (in tens of millions)', color=color, fontsize=12)
bar1 = ax1.bar(merged_data.index, merged_data['Approx total number of employees'], color=color, alpha=0.7, label='Total Employment')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle='--', alpha=0.6)

# Create a second Y-axis (ax2) that shares the same X-axis
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Total Emigration (in millions)', color=color, fontsize=12)
line2 = ax2.plot(merged_data.index, merged_data['Total number of emmigrants'], color=color, marker='o', label='Total Emigration')
ax2.tick_params(axis='y', labelcolor=color)

# --- Graph styling ---
plt.title('UK Employment (Bars) vs Emigration (Line) Over Years', fontsize=16, fontweight='bold')
plt.xticks(merged_data.index, rotation=45) # Rotate year labels for better readability

# Create a single legend for both the bar and line plots
# We get the handles from the line plot and create a handle for the bar plot
handles, labels = ax2.get_legend_handles_labels()
ax1.legend(handles=[bar1] + handles, labels=['Total Employment'] + labels, loc='upper left')

fig.tight_layout()  # Adjusts plot to prevent labels from overlapping
plt.show()





