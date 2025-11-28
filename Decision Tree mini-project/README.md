# Decision Tree mini-project 

This folder contains a small, beginner-friendly example showing how to train and evaluate a decision tree classifier on the UCI Car Evaluation dataset. It demonstrates loading data, basic categorical encoding, training a classifier with scikit-learn, making predictions and viewing simple evaluation metrics.

What this folder is for
- Learn how to load a dataset and inspect its columns.
- See a simple workflow: encode categorical features, split data, train a DecisionTreeClassifier and evaluate results.
- Run the script and read printed model diagnostics (classification report, confusion matrix).

Concepts
- Dataset: the Car Evaluation dataset (provided in the `car+evaluation/` subfolder).
- Encoding: categorical columns are converted to numeric labels before training.
- Train / test split: data is split so the model is evaluated on unseen examples.
- Evaluation: classification report (precision/recall/f1) and confusion matrix show model performance.

Folder structure and main files
- `decision_tree.py` — main script: loads the dataset (via ucimlrepo), encodes categorical variables, trains a DecisionTreeClassifier, prints performance metrics.
- `car+evaluation/` — UCI dataset files (car.data, car.names, car.c45-names). The script fetches data via ucimlrepo but local files are included as a fallback.

Requirements 
- Python 3.8+
- scikit-learn
- ucimlrepo (used to fetch the dataset)
- pandas (ucimlrepo returns pandas DataFrame)
- matplotlib (optional, used if you add plotting)

Install (macOS, recommended inside a venv)
1. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install required packages:
   ```
   pip install --upgrade pip
   pip install scikit-learn ucimlrepo pandas matplotlib
   ```

How to run 
1. Open Terminal at the project folder:
   ```
   cd "/Users/milansmacbook/University year 2/DAT5501/DAT5501_Repo/Decision Tree mini-project"
   ```
2. Run the script:
   ```
   python decision_tree.py
   ```
3. Inspect the terminal output:
   - Metadata and first rows of the feature table
   - Confirmation messages for encoding and training
   - Classification report (precision, recall, f1) and confusion matrix

Interpreting the outputs (for beginners)
- Classification report: shows per-class precision, recall and F1. Higher values are better.
- Confusion matrix: rows are true classes, columns are predicted classes. Diagonal entries are correct predictions.
- If many off-diagonal values appear, the model is misclassifying between classes and may need different preprocessing or model settings.

Beginner tips and troubleshooting
- ModuleNotFoundError for ucimlrepo or sklearn: ensure your virtual environment is active and packages are installed.
- If ucimlrepo cannot fetch data (no internet), the included `car+evaluation/car.data` can be read directly — you can modify the script to pd.read_csv("car+evaluation/car.data", header=None) if needed.
- Encoding note: the script uses LabelEncoder to convert categorical columns to integers. For some tasks you may prefer one-hot encoding (pandas.get_dummies) or column-specific encoders.
- If the plot_tree display is too cluttered, reduce tree depth in DecisionTreeClassifier (use max_depth) or save the tree to a PNG and zoom in.

Suggested learning path
1. Open `decision_tree.py` and read the printed comments to understand each block (loading, encoding, splitting, training, evaluation).
2. Run the script, review the classification report and confusion matrix.
3. Try small experiments:
   - Set `max_depth=3` in DecisionTreeClassifier and re-run.
   - Replace LabelEncoder with `pd.get_dummies(X)` to try one-hot encoding.
   - Save and view the plotted tree (use matplotlib `plot_tree` and `plt.savefig()`).

Extending the project
- Add a saved PNG visualisation of the trained tree (use plot_tree + savefig).
- Try other classifiers (RandomForestClassifier, LogisticRegression) and compare metrics.
- Add cross-validation (sklearn.model_selection.cross_val_score) to get more robust performance estimates.

This README is intended to help you run the example, understand what the outputs mean, and make small experiments to learn how preprocessing and model settings affect results.