# Asset price (Apple Stock)

This folder contains data and simple Python scripts that demonstrate basic data cleaning and exploratory analysis of Apple stock prices. It is written for beginners: open a script, run it, and inspect the saved plot/CSV to see what each step does.

What’s included
- apple_historical_data.csv — raw input (downloaded historical prices).
- Data_wrangling.py — cleans and prepares the raw CSV into cleaned_apple_data.csv.
- cleaned_apple_data.csv — cleaned dataset used by analysis scripts.
- yearly_price_change.py — computes and plots yearly price changes (saves a PNG).
- Daily price change/daily_price_change.py — computes daily returns and saves example plots.
- apple_stock_price.png, daily_sorting_t_vs_n.png — example output plots.

What each script does (short)
- Data_wrangling.py: reads the raw CSV, fixes column names/dates, drops or fills missing values, and writes cleaned_apple_data.csv.
- yearly_price_change.py: reads the cleaned CSV, computes yearly percent changes, and saves a plot and summary.
- Daily price change/daily_price_change.py: computes daily returns, sorts/analyses them and saves plots to illustrate behaviour.

How to run (macOS, minimal)
1. Open Terminal at the repository root.
2. (Optional but recommended) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install required packages if needed:
   ```
   pip install pandas numpy matplotlib
   ```
4. Run cleaning script:
   ```
   python "Asset price/Data_wrangling.py"
   ```
5. Run analyses:
   ```
   python "Asset price/yearly_price_change.py"
   python "Asset price/Daily price change/daily_price_change.py"
   ```

Where outputs go
- cleaned_apple_data.csv — created/overwritten by Data_wrangling.py in this folder.
- Plots (PNG) — saved in the same folder or the script’s configured path (check the top of each script).

Beginner tips and troubleshooting
- If a script errors with "file not found", confirm apple_historical_data.csv is in this folder or that cleaned_apple_data.csv exists after running the wrangling script.
- If plots do not appear on screen, check for saved PNG files in the folder.
- If Python modules are missing, install them with pip (see step 3).
- Open the scripts in your editor to read the comments — they explain each processing step.

Suggested learning path
1. Open Data_wrangling.py, run it, inspect cleaned_apple_data.csv.
2. Open yearly_price_change.py, run it, open the saved plot (apple_stock_price.png).
3. Run the daily script and compare daily vs yearly behaviour.

Contributing
- Add new plots to a dedicated `plots/` subfolder.
- If you add dependencies, list them in a project-level requirements file.
- Keep scripts small and well-commented so other beginners can follow them.

This README is intended to help you run the code, find outputs, and learn by example.// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/Asset price/README.md
# Asset price — Beginner guide (Apple stock)

This folder contains data and simple Python scripts that demonstrate basic data cleaning and exploratory analysis of Apple stock prices. It is written for beginners: open a script, run it, and inspect the saved plot/CSV to see what each step does.

What’s included
- apple_historical_data.csv — raw input (downloaded historical prices).
- Data_wrangling.py — cleans and prepares the raw CSV into cleaned_apple_data.csv.
- cleaned_apple_data.csv — cleaned dataset used by analysis scripts.
- yearly_price_change.py — computes and plots yearly price changes (saves a PNG).
- Daily price change/daily_price_change.py — computes daily returns and saves example plots.
- apple_stock_price.png, daily_sorting_t_vs_n.png — example output plots.

What each script does (short)
- Data_wrangling.py: reads the raw CSV, fixes column names/dates, drops or fills missing values, and writes cleaned_apple_data.csv.
- yearly_price_change.py: reads the cleaned CSV, computes yearly percent changes, and saves a plot and summary.
- Daily price change/daily_price_change.py: computes daily returns, sorts/analyses them and saves plots to illustrate behaviour.

How to run (macOS, minimal)
1. Open Terminal at the repository root.
2. (Optional but recommended) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install required packages if needed:
   ```
   pip install pandas numpy matplotlib
   ```
4. Run cleaning script:
   ```
   python "Asset price/Data_wrangling.py"
   ```
5. Run analyses:
   ```
   python "Asset price/yearly_price_change.py"
   python "Asset price/Daily price change/daily_price_change.py"
   ```

Where outputs go
- cleaned_apple_data.csv — created/overwritten by Data_wrangling.py in this folder.
- Plots (PNG) — saved in the same folder or the script’s configured path (check the top of each script).

Beginner tips and troubleshooting
- If a script errors with "file not found", confirm apple_historical_data.csv is in this folder or that cleaned_apple_data.csv exists after running the wrangling script.
- If plots do not appear on screen, check for saved PNG files in the folder.
- If Python modules are missing, install them with pip (see step 3).
- Open the scripts in your editor to read the comments — they explain each processing step.

Suggested learning path
1. Open Data_wrangling.py, run it, inspect cleaned_apple_data.csv.
2. Open yearly_price_change.py, run it, open the saved plot (apple_stock_price.png).
3. Run the daily script and compare daily vs yearly behaviour.

Contributing
- Add new plots to a dedicated `plots/` subfolder.
- If you add dependencies, list them in a project-level requirements file.
- Keep scripts small and well-commented so other beginners can follow them.

This README is intended to help you run the code, find outputs, and learn by example.