import pandas as pd
import os # Import the os module

# Get the absolute path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Join that path with the CSV file name
csv_path = os.path.join(script_dir, 'apple_historical_data.csv')

# Read the CSV using this full, correct path
df = pd.read_csv(csv_path)

# Data Cleaning Steps

# 1. Clean 'Close/Last' column
df['Close/Last'] = df['Close/Last'].astype(str).str.replace('$', '')
df['Close/Last'] = pd.to_numeric(df['Close/Last'])

# 2. Convert 'Date' column
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# 3. Sort by Date
df = df.sort_values(by='Date', ascending=True)

# 4. Save the cleaned data (this will also save to the 'Asset price' folder)
cleaned_csv_path = os.path.join(script_dir, 'cleaned_apple_data.csv')
df.to_csv(cleaned_csv_path, index=False)

print(f"Cleaned data saved to {cleaned_csv_path}")
print("\nCleaned Data Head:")
print(df.head())

  