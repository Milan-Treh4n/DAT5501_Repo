import os
import pandas as pd
import numpy as np

def test_csv_exists():
    assert os.path.exists("random_data.csv"), "CSV file was not created"

def test_plot_exists():
    assert os.path.exists("fit_plot.png"), "Plot file was not created"

def test_csv_numeric():
    df = pd.read_csv("random_data.csv")
    assert df["x"].apply(np.isreal).all(), "Non-numeric x values found"
    assert df["y"].apply(np.isreal).all(), "Non-numeric y values found"

def test_fit_accuracy():
    df = pd.read_csv("random_data.csv")
    x, y = df["x"], df["y"]
    m_fit, b_fit = np.polyfit(x, y, 1)
    # Expect fitted line close to true line (within tolerance)
    assert np.isclose(m_fit, 2, atol=0.3), f"Slope off: {m_fit}"
    assert np.isclose(b_fit, 5, atol=0.5), f"Intercept off: {b_fit}"
