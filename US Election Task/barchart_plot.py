import pandas as pd
import os
import matplotlib.pyplot as plt

# Get the absolute path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the correct name of data file
file_name = 'US-2016-primary.csv'

# Join the script's directory path with the file name to get the full, correct path
file_path = os.path.join(script_dir, file_name)

try:
    df_primary = pd.read_csv(file_path, sep=';')

    # Display the first 5 rows
    print("--- First 5 Rows ---")
    print(df_primary.head())

    # Display the data types
    print("\n--- Column Data Types ---")
    print(df_primary.dtypes)

    # Plotting section
    candidate_name = "Donald Trump"

    # Group by state and candidate, sum votes
    state_totals = df_primary.groupby("state")["votes"].sum()
    candidate_votes = df_primary[df_primary["candidate"] == candidate_name].groupby("state")["votes"].sum()

    # Compute fraction of votes for the candidate per state
    vote_fraction = (candidate_votes / state_totals).dropna()

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(vote_fraction.index, vote_fraction.values, color='skyblue', edgecolor='black')
    plt.title(f"Bar Chart of Fraction of Votes for {candidate_name} by State")
    plt.xlabel("State")
    plt.ylabel("Fraction of Votes")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3)

    # Save the plot image to the repo
    plot_filename = f"{candidate_name.replace(' ', '_')}_vote_fraction_bar_chart.png"
    plot_path = os.path.join(script_dir, plot_filename)
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')

    print(f"\nPlot saved as: {plot_path}")

    # plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file at the path: {file_path}")
    print("Please make sure the file 'US-2016-primary.csv' is in the same folder as your Python script.")
except Exception as e:
    print(f"An error occurred: {e}")
