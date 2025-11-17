# Immigration project 

This folder compares employment statistics with emigration numbers for the UK. The scripts load simple CSV files, make plots, and save PNG images so you can visually compare trends.

What’s included
- `Employemnt_vs_emmigrants.py` — main plotting script (note the filename spelling).
- `employment_vs_emmigration_REAL.py` — alternate/cleaned analysis script.
- `employment_services_uk.csv` — employment data (input).
- `UK_emmigrants_data.csv` — emigration data (input).
- `employment_vs_emmigration.png` and `employment_vs_emigration_same_scale.png` — example output plots.

What the scripts do (short)
- Read the two CSV files (employment and emigration).
- Align the data by year, compute any simple summaries if needed.
- Plot employment vs emigration trends and save PNG files in this folder.

How to run (macOS)
1. Open Terminal in the repository root or this folder.
2. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install necessary packages if you do not have them:
   ```
   pip install pandas matplotlib
   ```
4. Run a script:
   ```
   python "Immigration project/Employemnt_vs_emmigrants.py"
   ```
   or
   ```
   python "Immigration project/employment_vs_emmigration_REAL.py"
   ```

Where outputs go
- PNG plots are saved in this folder (files listed above). Open them with your image viewer to inspect the results.

Beginner tips and troubleshooting
- File not found: make sure `employment_services_uk.csv` and `UK_emmigrants_data.csv` are in this folder.
- If plots look empty: check that the CSVs contain matching years and non-empty numeric columns.
- Spelling: there is a misspelt filename (`Employemnt_vs_emmigrants.py`) — run the exact name or rename it for convenience.
- Missing packages: install with pip as shown above.

Suggested learning path
1. Open the CSV files in a text editor or spreadsheet to see their columns (look for a Year column).
2. Open the plotting script(s) to see how the files are read and how the plot is constructed.
3. Run the script, then open the saved PNG(s) to compare employment and emigration visually.
4. Try changing plot labels, colours or the years included to explore effects.

Extending the analysis
- Add simple statistics (correlation, percent change) in the script to quantify relationships.
- Save cleaned, merged CSV if you plan to reuse the aligned data.

This README is written to help you run the code, find outputs, and learn by example.// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/Immigration project/README.md
