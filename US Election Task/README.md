# Unit test activity 

This small folder demonstrates a basic unit-test setup in Python. It is designed for beginners who want to see how a function is tested and how to run tests locally.

What’s included
- `Milan_function.py` — a small example module containing the function(s) under test.
- `test_unittest_example.py` — a minimal test file (compatible with pytest and unittest-style assertions).

What this teaches
- How to separate code and tests.
- How to run tests and read test output.
- How failing tests point to problems in your code.

How to run the tests (macOS, very simple)
1. Open Terminal at the repository root.
2. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install pytest (if not already installed):
   ```
   pip install pytest
   ```
4. Run the tests:
   ```
   pytest -q "Unit test activity/test_unittest_example.py"
   ```

If tests pass you will see a green success message. If a test fails, pytest will show which test failed and why.

Beginner tips
- Open `Milan_function.py` to see the function(s) being tested.
- Open `test_unittest_example.py` to see examples of assertions (expected vs actual).
- Run a single test file as shown above while you edit code to get fast feedback.
- If you prefer Python's built-in unittest, you can also run:
  ```
  python -m unittest "Unit test activity/test_unittest_example.py"
  ```

Troubleshooting
- "Module not found" — make sure you run pytest from the repository root so relative imports work.
- If pytest is not installed, install it with pip (step 3).
- Read the assertion message shown by pytest: it usually explains what went wrong.

Suggested learning path
1. Read the test file to understand the expected behaviour.
2. Run the tests to see the current status.
3. Make a small change in `Milan_function.py`, run tests again, observe results.
4. Try adding a new test case to practise writing assertions.

This README is meant to help you run and understand the simple unit-test example.// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/Unit test activity/README.md
