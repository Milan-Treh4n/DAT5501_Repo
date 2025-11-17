# Fitting and forecasting activity

This folder contains scripts that analyse global life expectancy data using polynomial regression models (orders 1–9). The project performs two major analytical tasks: forecasting and model testing. All analysis is based on the dataset `life_expectancy.csv`.

Overview
- Forecasting life expectancy (per-continent or global average)
- Model testing using χ² per degree of freedom to assess fit quality

1) Forecasting Life Expectancy
The forecasting script uses historical life expectancy data for continents or for the global average. Main steps:
- Data preparation
  - Loads `life_expectancy.csv`
  - Filters data to include only continental values (or excludes continents when calculating a global average)
  - Extracts life expectancy series depending on availability in the dataset
- Training / forecast split
  - Uses all years except the last 10 as training data
  - Uses the final 10 years as the forecasting period
- Polynomial model fitting
  - Fits polynomial regression models of orders 1 through 9
  - Forecasts the final 10 years using each model
  - Creates comparison plots showing all polynomial orders on a single figure
  - Saves plots automatically into a `plots/` directory so they appear in your GitHub repository

This part demonstrates how different model complexities behave and highlights overfitting at higher polynomial orders.

2) Model Testing Using Chi-Squared per Degree of Freedom
The second script evaluates model quality statistically using only the training portion of the dataset.
- Model fitting
  - Fits polynomial regressions (orders 1–9) to the same training data used in the forecasting script
- Goodness-of-fit calculation
  - Computes the chi-squared statistic:
    χ² = Σ ((observed − predicted)² / σ²)
  - Uses 1% of the observed life expectancy as σ (σ = 0.01 × observed)
  - Computes reduced chi-squared χ²/ν (ν = degrees of freedom)
- Model ranking
  - Prints χ²/ν values for each model order
  - Automatically identifies the best-fitting orders (prints top results)

This section focuses on statistical fit quality and supports choosing an appropriate model order for forecasting.

All analysis uses the file `life_expectancy.csv`.

What’s in this folder
- `chi_squared.py` — computes χ² per degree of freedom for polynomial fits (orders 1–9) and saves a plot (`plots_chi2/chi2_vs_order.png`).
- `Creating fitting comparisons/` — scripts to fit and compare polynomial forecasts per continent (saves plots in `plots/`).
- Other helper scripts and example plots used in the report.

How the scripts find the data
- Scripts look for `life_expectancy.csv` in the same folder as the script and in up to three parent folders. If the file is not found, the script will print an error and stop.
- Place `life_expectancy.csv` next to the scripts (or one of the parent folders) to avoid path errors.

Run the scripts (macOS)
1. Open Terminal in the repository root.
2. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install packages if you need them:
   ```
   pip install pandas numpy matplotlib
   ```
4. Run the χ² analysis:
   ```
   python "Fitting and forecasting activity/Model testing/chi_squared.py"
   ```
5. Run the continent forecast comparisons:
   ```
   python "Fitting and forecasting activity/Creating fitting comparisons/fitting_for_continents.py"
   ```

Where outputs are saved
- Forecast comparison plots → `Creating fitting comparisons/plots/` (one plot per continent).  
- χ² plot → `Model testing/plots_chi2/chi2_vs_order.png`.

Beginner tips and troubleshooting
- File not found: ensure `life_expectancy.csv` is in the script folder or a parent folder, or run the script from the repository root.
- Missing packages: install with pip as shown above.
- Plots not opening: check the `plots/` or `plots_chi2/` folders for saved PNG files.
- If a script fails, copy the exact error message and open the script in your editor to see which line caused it.

Suggested learning path
1. Open `chi_squared.py` and read the comments to see how training vs testing data are split.  
2. Run `chi_squared.py` and open the saved χ² plot to understand model fit quality.  
3. Open `fitting_for_continents.py`, run it, and inspect the continent forecast plots to compare polynomial orders.

Notes
- The analyses are examples for learning model selection and forecasting. They are not production pipelines.
- Keep `life_expectancy.csv` near these scripts for an easy start.
```// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/Fitting and forecasting activity/README.md


