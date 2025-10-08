import os
import pandas as pd
import numpy as np

def test_csv_with_outliers_exists():
    assert os.path.exists("random_data_with_outliers.csv"), "CSV file with outliers not found"

def test_plot_with_outliers_exists():
    assert os.path.exists("fit_with_outliers_and_errors.png"), "Plot file with outliers not found"

def test_error_column_exists():
    df = pd.read_csv("random_data_with_outliers.csv")
    assert "error" in df.columns, "Error column missing"

def test_data_is_numeric():
    df = pd.read_csv("random_data_with_outliers.csv")
    assert df.apply(np.isreal).all().all(), "Non-numeric values found in CSV"

def test_fit_is_reasonable():
    df = pd.read_csv("random_data_with_outliers.csv")
    x, y, err = df["x"].values, df["y"].values, df["error"].values
    weights = 1 / (err**2)
    m_fit, b_fit = np.polyfit(x, y, 1, w=weights)
    assert abs(m_fit - 2) < 1.0, f"Slope too far from expected: {m_fit}"
    assert abs(b_fit - 5) < 3.0, f"Intercept too far from expected: {b_fit}"
