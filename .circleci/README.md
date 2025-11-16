
This folder contains CircleCI configuration and minimal test code for the DAT5501_Repo. It is intended to run automated tests and any CI checks configured in `config.yml`.

## Contents
- `config.yml` — CircleCI pipeline configuration.
- `milan_function.py` — Example/module under test.
- `requirements.txt` — Python dependencies used by the CI job(s).
- `test_milan.py` — Pytest test file for `milan_function.py`.

## Purpose
- Provide a reproducible CI pipeline (via CircleCI) that installs dependencies and runs the test suite.
- Allow local reproduction of the CI steps for development and debugging.

## Quick start (local)
1. Create and activate a virtual environment (macOS):
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r .circleci/requirements.txt
   ```

3. Run tests:
   ```
   pytest -q .circleci/test_milan.py
   ```

## Running the CircleCI config locally (optional)
If you have the CircleCI CLI installed, you can run the job locally to mirror CI behavior:
```
circleci local execute --config .circleci/config.yml
```
(See CircleCI docs for installation and required Docker runtime.)

## Notes for maintainers
- Keep `requirements.txt` in sync with dependencies used in the rest of the repository.
- Ensure `config.yml` references the correct Python version and paths if project layout changes.
- Tests in `test_milan.py` should remain small, deterministic, and fast so CI stays responsive.

## Troubleshooting
- If tests fail locally but pass on CI, check Python version and installed package versions.
- If CircleCI fails to locate files, confirm the `working_directory` and relative paths in `config.yml`.

## Contributing
- Add new tests alongside `test_milan.py` or add new test files under `.circleci/` if they are specific to CI examples.
- Update `requirements.txt` when adding new runtime/test dependencies.

```// filepath: /Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/.circleci/README.md
# .circleci

This folder contains CircleCI configuration and minimal test code for the DAT5501_Repo. It is intended to run automated tests and any CI checks configured in `config.yml`.

## Contents
- `config.yml` — CircleCI pipeline configuration.
- `milan_function.py` — Example/module under test.
- `requirements.txt` — Python dependencies used by the CI job(s).
- `test_milan.py` — Pytest test file for `milan_function.py`.

## Purpose
- Provide a reproducible CI pipeline (via CircleCI) that installs dependencies and runs the test suite.
- Allow local reproduction of the CI steps for development and debugging.

## Quick start (local)
1. Create and activate a virtual environment (macOS):
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r .circleci/requirements.txt
   ```

3. Run tests:
   ```
   pytest -q .circleci/test_milan.py
   ```

## Running the CircleCI config locally (optional)
If you have the CircleCI CLI installed, you can run the job locally to mirror CI behavior:
```
circleci local execute --config .circleci/config.yml
```
(See CircleCI docs for installation and required Docker runtime.)

## Notes for maintainers
- Keep `requirements.txt` in sync with dependencies used in the rest of the repository.
- Ensure `config.yml` references the correct Python version and paths if project layout changes.
- Tests in `test_milan.py` should remain small, deterministic, and fast so CI stays responsive.

## Troubleshooting
- If tests fail locally but pass on CI, check Python version and installed package versions.
- If CircleCI fails to locate files, confirm the `working_directory` and relative paths in `config.yml`.

## Contributing
- Add new tests alongside `test_milan.py` or add new test files under `.circleci/` if they are specific to CI examples.
- Update `requirements.txt` when adding new runtime/test dependencies.
