# US Election Task 

This small folder contains a CSV of 2016 primary results and a simple Python script that creates a histogram/bar chart of vote fractions. It is written for beginners: open the script, run it, and inspect the saved image to see how data is loaded and plotted.

What’s included
- `US-2016-primary.csv` — input data (2016 primary results).
- `barchart_plot.py` — script that reads the CSV and produces a histogram/bar chart.
- `Donald_Trump_vote_fraction_bar_chart.png` — example output image created by the script.

What the script does (short)
- Loads the CSV file using pandas.
- Selects the column(s) for candidate vote fractions.
- Draws a histogram or bar chart using matplotlib and saves the figure as a PNG.

Requirements (basic)
- Python 3.x
- pandas and matplotlib

How to run (macOS)
1. Open Terminal at the repository root (or this folder).
2. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install required packages if not already installed:
   ```
   pip install pandas matplotlib
   ```
4. Run the script:
   ```
   python "US Election Task/Histogram_Plot.py"
   ```
5. Open the saved image (e.g. `Donald_Trump_vote_fraction_bar_chart.png`) in an image viewer.

Where output goes
- The plot PNG is saved in this folder (file name shown above). Check that file after the script finishes.

Beginner tips and troubleshooting
- File not found: make sure `US-2016-primary.csv` is in this folder and that you run the script from the repository root or this folder.
- Column errors: open `US-2016-primary.csv` in a text editor or spreadsheet to confirm the column names used by `barchart_plot.py` (update the script if the column name differs).
- Missing packages: install them with pip as shown above.
- If the plot looks odd, try printing the data inside the script (add print statements) to inspect values before plotting.

Suggested learning steps
1. Open `barchart_plot.py` and read the comments to see how the CSV is loaded and plotted.  
2. Run the script and open the generated PNG.  
3. Modify the script (change bins, labels, or the column used) and re-run to see how the plot changes.

This README is intended to help you run the script, find the output, and learn plotting basics by example.
```// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/US Election Task/README.md


