# Data Pipeline 
This folder contains example datasets, plotting scripts and unit tests that demonstrate simple data-processing and fitting workflows. It is organised by dataset size (small, medium, large) and includes examples with and without errors/outliers so you can see how fitting behaves in different situations.

## What this folder is for
- Learn how to load simple CSV data, run a fitting/plotting routine and inspect results.
- See how different dataset sizes and outliers affect model fits and visual output.
- Run and read basic unit tests that check behaviour and flag common problems.

## Concepts
- Dataset: a CSV file with numerical values. Scripts read these and produce plots or summary files.
- Fitting: a simple model (e.g. polynomial) is matched to the data points. The plot shows how well the model follows the data.
- Outliers / errors: some datasets include deliberate mistakes or large deviations. These help you learn how fits can be sensitive to bad data.
- Unit tests: small scripts that run checks and will pass/fail to tell you if the code behaves as expected.

## Folder structure and main files
- README.txt — short notes about the folder (this file expands on those notes).
- unit_tests.py, unit_test_for_erros.py — basic tests that exercise scripts and error handling.
- Advanced fitting tests/  
  - test_advanced_fittings.py — example tests for more complex fitting cases.
- Large sized data set/  
  - large_normal_data.csv, large_error_data.csv — example large datasets.  
  - large_normal_data.py, large_error_data.py — scripts that load and fit the large datasets.  
  - PNGs — saved plots demonstrating results.
- Medium sized data set/  
  - medium_normal_data.csv and a subfolder for medium sized datasets with outliers.  
  - Scripts and PNGs show how medium datasets behave.
- Small Data set/  
  - random_data.csv and plotting scripts.  
  - Small Data set with error bars/ contains example with error bars and outliers.
- Plots (.png) — visual output from the scripts. Inspect these to understand fit quality.

## How to use these files
- Open a script (e.g. `Small Data set/plotted fit.py`) in your editor to see how it reads a CSV, performs a fit and saves a plot.
- Run a script and then open the generated PNG to visually inspect the fit vs the data points.
- Compare the normal datasets to the corresponding “error” datasets to see the effect of outliers.
- Open the test files to see what behaviours are expected (for example: functions return arrays of the right shape, errors are handled).

## Interpreting outputs
- A good fit means the model curve follows the main trend of the points; large discrepancies indicate underfitting or outliers.
- Error/outlier plots show where a few points drive a poor model—consider robust methods or outlier removal in real projects.
- Unit test failures point to specific functions or assumptions that need fixing.

## Troubleshooting tips 
- If a script cannot find a CSV, check the file path and that the CSV is in the same folder or the script’s expected location.
- Large datasets may take longer to run; check memory and wait for scripts to finish.
- If plots are blank, verify the script actually saves data arrays and calls the plotting routine before closing.

## Contributing / extending
- Add new datasets in a new subfolder named for size or purpose.
- Add tests in `unit_tests.py` or new test files to cover new behaviour.
- Keep plots and generated CSVs alongside the scripts that produce them so others can inspect results.

This folder is structured to help you learn by example: open a small script, run it, look at the outputs, then explore larger and more complex cases.// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/Data Pipeline/README.md
