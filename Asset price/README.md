# Asset price — Apple stock analysis

This folder contains scripts and data for basic analysis of Apple historical stock prices. The code computes and visualises daily and yearly price changes and includes a small data-wrangling step.

Main tasks
- Data cleaning and preparation
  - Data_wrangling.py: cleans raw CSV into cleaned_apple_data.csv
- Daily price analysis
  - Daily price change/daily_price_change.py: computes daily returns and generates daily plots
- Yearly price analysis & plotting
  - yearly_price_change.py: computes yearly changes and saves summary plot(s)

Files
- apple_historical_data.csv — raw input data
- cleaned_apple_data.csv — cleaned output used by analysis scripts
- Data_wrangling.py — cleaning & preprocessing script
- yearly_price_change.py — yearly analysis + plotting
- apple_stock_price.png — example output plot (stock price overview)
- Daily price change/
  - daily_price_change.py — daily-return calculations and plots
  - daily_sorting_t_vs_n.png — example daily-plot

Quick start (macOS)
1. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install minimal dependencies:
   ```
   pip install pandas numpy matplotlib
   ```
3. Run the cleaning script:
   ```
   python "Asset price/Data_wrangling.py"
   ```
4. Run analyses:
   ```
   python "Asset price/yearly_price_change.py"
   python "Asset price/Daily price change/daily_price_change.py"
   ```

Outputs
- cleaned_apple_data.csv — cleaned dataset used by other scripts
- apple_stock_price.png and plots in the Daily price change folder — saved figures for report/include

Notes
- Scripts expect the raw CSV to be present in this folder. Adjust paths if you move files.
- If you add new plotting or analysis scripts, save figures in this folder or a dedicated `plots/` subfolder for reproducibility.

Contributing
- Keep scripts small and deterministic.
- Add any new Python dependencies to the repo README or a requirements file.
```// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/Asset price/README.md
# Asset price — Apple stock analysis

This folder contains scripts and data for basic analysis of Apple historical stock prices. The code computes and visualises daily and yearly price changes and includes a small data-wrangling step.

Main tasks
- Data cleaning and preparation
  - Data_wrangling.py: cleans raw CSV into cleaned_apple_data.csv
- Daily price analysis
  - Daily price change/daily_price_change.py: computes daily returns and generates daily plots
- Yearly price analysis & plotting
  - yearly_price_change.py: computes yearly changes and saves summary plot(s)

Files
- apple_historical_data.csv — raw input data
- cleaned_apple_data.csv — cleaned output used by analysis scripts
- Data_wrangling.py — cleaning & preprocessing script
- yearly_price_change.py — yearly analysis + plotting
- apple_stock_price.png — example output plot (stock price overview)
- Daily price change/
  - daily_price_change.py — daily-return calculations and plots
  - daily_sorting_t_vs_n.png — example daily-plot

   ```

Outputs
- cleaned_apple_data.csv — cleaned dataset used by other scripts
- apple_stock_price.png and plots in the Daily price change folder — saved figures for report/include

Notes
- Scripts expect the raw CSV to be present in this folder. Adjust paths if you move files.
- If you add new plotting or analysis scripts, save figures in this folder or a dedicated `plots/` subfolder for reproducibility.

Contributing
- Keep scripts small and deterministic.
- Add any new Python dependencies to the repo README or a requirements file.