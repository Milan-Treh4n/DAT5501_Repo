# .circleci

This folder contains simple CircleCI configuration and a tiny example test. It is used to show how continuous integration (CI) can run tests automatically for the repository.

Why this folder exists
- Demonstrates a basic CI pipeline that installs dependencies and runs tests.
- Provides a minimal example you can run locally to understand CI behaviour.
- Keeps CI-related files together so the rest of the project stays clean.

What is here
- `config.yml` — CircleCI pipeline configuration (what the CI server runs).
- `requirements.txt` — Python packages needed by the CI job and the tests.
- `milan_function.py` — Small example module used by the tests.
- `test_milan.py` — A minimal pytest test for the example module.

Simple explanation of CI (for beginners)
- Continuous Integration (CI) runs automated tasks (like tests) whenever code changes.
- CircleCI reads `config.yml` and runs the steps defined there (install, test, etc.).
- CI helps catch errors early and ensures code in the repository works consistently.

Run the example locally (very simple)
1. Open a terminal in the repository root.
2. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r .circleci/requirements.txt
   ```
4. Run the tests with pytest:
   ```
   pytest -q .circleci/test_milan.py
   ```

If you see tests pass, the CI pipeline would likely pass too (assuming similar environment).

Troubleshooting (common beginner issues)
- "Module not found" — make sure your virtual environment is activated and you installed requirements.
- Wrong Python version — check `config.yml` for the Python version used in CI and use the same locally.
- Path problems — run the commands from the repository root so paths like `.circleci/test_milan.py` resolve.

Notes for learning
- Open `config.yml` to see a step-by-step description of what CI does (install, run tests).
- Open `test_milan.py` and `milan_function.py` to see a minimal example of a function and its test.
- If you want to try CircleCI locally, the CircleCI CLI can emulate jobs, but it is optional.

Contributing tips
- Keep tests small and deterministic (no random behaviour).
- Add new test files under `.circleci/` or the repo test folder and update `requirements.txt` if you add dependencies.
- Update `config.yml` if CI needs additional steps (linting, formatting, coverage).

This file is intended as a gentle introduction so you can run and understand the simple CI example in this folder. ````// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/.circleci/README.md
# .circleci — Beginner-friendly guide

This folder contains simple CircleCI configuration and a tiny example test. It is used to show how continuous integration (CI) can run tests automatically for the repository.

Why this folder exists
- Demonstrates a basic CI pipeline that installs dependencies and runs tests.
- Provides a minimal example you can run locally to understand CI behaviour.
- Keeps CI-related files together so the rest of the project stays clean.

What is here
- `config.yml` — CircleCI pipeline configuration (what the CI server runs).
- `requirements.txt` — Python packages needed by the CI job and the tests.
- `milan_function.py` — Small example module used by the tests.
- `test_milan.py` — A minimal pytest test for the example module.

Simple explanation of CI (for beginners)
- Continuous Integration (CI) runs automated tasks (like tests) whenever code changes.
- CircleCI reads `config.yml` and runs the steps defined there (install, test, etc.).
- CI helps catch errors early and ensures code in the repository works consistently.

Run the example locally (very simple)
1. Open a terminal in the repository root.
2. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r .circleci/requirements.txt
   ```
4. Run the tests with pytest:
   ```
   pytest -q .circleci/test_milan.py
   ```

If you see tests pass, the CI pipeline would likely pass too (assuming similar environment).

Troubleshooting (common beginner issues)
- "Module not found" — make sure your virtual environment is activated and you installed requirements.
- Wrong Python version — check `config.yml` for the Python version used in CI and use the same locally.
- Path problems — run the commands from the repository root so paths like `.circleci/test_milan.py` resolve.

Notes for learning
- Open `config.yml` to see a step-by-step description of what CI does (install, run tests).
- Open `test_milan.py` and `milan_function.py` to see a minimal example of a function and its test.
- If you want to try CircleCI locally, the CircleCI CLI can emulate jobs, but it is optional.

Contributing tips
- Keep tests small and deterministic (no random behaviour).
- Add new test files under `.circleci/` or the repo test folder and update `requirements.txt` if you add dependencies.
- Update `config.yml` if CI needs additional steps (linting, formatting, coverage).

This file is intended as a gentle introduction so you can run and understand the simple CI example in this folder. ````

