import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Changed 'apple_data_cleaned.csv' to 'cleaned_apple_data.csv'
file_path = os.path.join(os.path.dirname(__file__), 'cleaned_apple_data.csv')
data = pd.read_csv(file_path)

# Ensure 'Date' is in datetime format for better plotting
data['Date'] = pd.to_datetime(data['Date'])

plt.figure(figsize=(10, 6))

# Changed data['Close'] to data['Close/Last']
plt.plot(data['Date'], data['Close/Last'], label='Apple Stock Price', color='lightgreen')

plt.title('Apple Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot in the same directory as the script
plot_save_path = os.path.join(os.path.dirname(__file__), 'apple_stock_price.png')
plt.savefig(plot_save_path)

# plt.show() # plt.show() can sometimes cause issues in scripts, saving is safer.
print(f"Plot saved successfully to {plot_save_path}")
