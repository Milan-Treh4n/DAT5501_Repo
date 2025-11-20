# Fitting and forecasting activity 

This folder analyses global life expectancy using polynomial regression models (orders 1–9). The project performs two main tasks: forecasting and model testing. All analysis uses the dataset `life_expectancy.csv`.

Core tasks
- Forecasting life expectancy
  - Fits polynomial models (orders 1–9) to historical data (training = all years except last 10)
  - Forecasts the final 10 years with each model
  - Produces comparison plots showing orders 1–9 on a single figure
- Model testing using χ² per degree of freedom
  - Fits polynomials (orders 1–9) to the training data only
  - Computes χ² = Σ((observed − predicted)² / σ²) with σ = 0.01 × observed
  - Computes reduced chi-squared (χ²/ν) and ranks model orders

Included scripts and purpose
- `Model testing/chi_squared.py` — computes χ²/ν for polynomial fits and saves a χ² vs order plot (`plots_chi2/`).
- `Creating fitting comparisons/fitting_for_continents.py` — fits models per continent (or global average) and saves forecast comparison plots in `Creating fitting comparisons/plots/`.
- `Parameter Values/life_expectancy_model_selection.py` — computes best-fit parameter values and compares polynomial vs exponential models on the training set:
  - Loads `life_expectancy.csv`, computes the global average (excludes continent rows) and uses all years except the last 10 as training data.
  - Fits a chosen polynomial order (prints coefficients, covariance, uncertainties).
  - Attempts an exponential fit using scipy's curve_fit (prints parameters/covariance when successful).
  - Computes Bayesian Information Criterion (BIC) for each model from training residuals using σ = 0.01 × observed and prints which model BIC prefers.
  - Useful to extract numeric parameter values for reports and to compare model forms.

How scripts locate the data
- Scripts search for `life_expectancy.csv` in the script directory and up to three parent directories. Place `life_expectancy.csv` next to these scripts (or in a parent folder) to avoid path errors.

Dependencies
- pandas, numpy, matplotlib (most scripts)
- scipy (for `life_expectancy_model_selection.py`)
- Install with pip if needed:
  ```
  pip install pandas numpy matplotlib scipy
  ```

Run examples (macOS)
1. Open Terminal at the repository root.
2. (Optional) Create/activate virtual env:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Run χ² analysis:
   ```
   python "Fitting and forecasting activity/Model testing/chi_squared.py"
   ```
4. Run continent forecast comparisons:
   ```
   python "Fitting and forecasting activity/Creating fitting comparisons/fitting_for_continents.py"
   ```
5. Inspect parameter values / model comparison:
   ```
   python "Fitting and forecasting activity/Parameter Values/life_expectancy_model_selection.py"
   ```

Outputs
- Forecast comparison plots → `Creating fitting comparisons/plots/`
- χ² plot → `Model testing/plots_chi2/chi2_vs_order.png`
- Parameter prints and BIC summary → terminal output from `life_expectancy_model_selection.py`

Beginner tips
- If a script reports "file not found", ensure `life_expectancy.csv` is in the script folder or a parent folder and run from the repo root.
- If a required package is missing, install with pip as shown above.
- To inspect what each script does, open it in your editor and read the top comments and print statements.

Suggested learning path
1. Run `chi_squared.py` to see how model order affects χ²/ν.  
2. Run `fitting_for_continents.py` and view the saved plots to compare fits visually.  
3. Run `life_expectancy_model_selection.py` to obtain fitted parameters and a BIC-based model comparison.

Notes
- These scripts are educational examples for model selection and forecasting, not production workflows. Adjust σ, model choices or data filters to explore different assumptions.
```// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/Fitting and forecasting activity/README.md


