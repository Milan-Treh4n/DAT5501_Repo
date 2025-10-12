import pandas as pd
import matplotlib.pyplot as plt

file_path = 'employment_services_uk.csv'
file_path2 = 'UK_emmigrants_data.csv'
employment = pd.read_csv(file_path)
emigration = pd.read_csv(file_path2)

# Clean and preprocess the data
for col in employment.columns[1:]:
    employment[col] = employment[col].apply(lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x)

for col in emigration.columns[1:]:
    emigration[col] = emigration[col].apply(lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x)

# Drop rows with any NaN values
employement.dropna(inplace=True)
emigration.dropna(inplace=True)

# Convert 'Year' column to integer
employement['Year'] = employement['Year'].astype(int)
emigration['Year'] = emigration['Year'].astype(int)

# Merge datasets on 'Year'
merged_data = pd.merge(employement, emigration, on='Year', suffixes=('_employment', '_emigration'))
merged_data.set_index('Year', inplace=True)

# Plotting the data
plt.figure(figsize=(14, 7))
plt.plot(merged_data.index, merged_data['Total_employment'], label='Total Employment', color='blue', marker='o')
plt.plot(merged_data.index, merged_data['Total_emigration'], label='Total Emigration', color='red', marker='o')
plt.title('UK Employment vs Emigration Over Years')
plt.xlabel('Year')
plt.ylabel('Number of People')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
