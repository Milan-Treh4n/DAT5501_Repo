# Duration Calendar

This folder contains small Python scripts to create random dates, compute durations, and run simple tests. It is written for beginners: open a script, run it, and read the comments to learn what each step does.

What’s included
- duration_calendar.py — main script to compute durations / build a simple calendar from the dates file.
- random_dates_calculator.py — generates a CSV of random dates (example input).
- random_dates.csv — example CSV of dates (can be overwritten).
- unit_testpy.py — small unit-test script to check expected behaviour.

What each file does (short)
- random_dates_calculator.py: creates or updates random_dates.csv with sample dates. Useful to generate test data.
- duration_calendar.py: reads random_dates.csv, computes durations between dates (or other date-based summaries) and prints/saves results.
- unit_testpy.py: contains basic tests you can run to verify the scripts behave as expected.

How to run (macOS)
1. Open Terminal at the repository root.
2. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Generate example dates (optional):
   ```
   python "Duration Calendar/random_dates_calculator.py"
   ```
   This will create/update `Duration Calendar/random_dates.csv`.
4. Run the duration script:
   ```
   python "Duration Calendar/duration_calendar.py"
   ```
5. Run the tests:
   ```
   python "Duration Calendar/unit_testpy.py"
   ```
   or, if you have pytest installed:
   ```
   pytest "Duration Calendar/unit_testpy.py"
   ```

Tips
- Open the .py files in your editor and read the top comments — they explain what inputs are expected and what outputs are created.
- If a script says "file not found", make sure `random_dates.csv` exists in the same folder or run the generator first.
- These scripts use Python’s standard library (datetime, csv, random). No extra packages are required for basic use.

Troubleshooting
- Permission error when running: ensure the file is readable and you have the correct working directory.
- Unexpected date format errors: inspect `random_dates.csv` to confirm dates are in the expected format (see script comments).
- Test failures: open `unit_testpy.py` to see expected results and match your local files.

Suggested learning path
1. Run the date generator to produce sample data.
2. Inspect `random_dates.csv` to see the date format.
3. Run `duration_calendar.py` and review output.
4. Read and run `unit_testpy.py` to understand expected behaviours.

This README is intended to help you run the code, locate outputs, and learn by example. Keep scripts small and experiment by changing the generator parameters to see how outputs change.