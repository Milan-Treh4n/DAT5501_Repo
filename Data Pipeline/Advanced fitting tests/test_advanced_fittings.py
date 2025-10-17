
import numpy as np
import pandas as pd
import pytest
from scipy.stats import pearsonr

# Configuration

DATA_FILES = [
    "medium_normal_data.csv",
    "large_normal_data.csv",
    "medium_error_data.csv",
    "large_error_data.csv",
]

TRUE_SLOPE = 2.0
TRUE_INTERCEPT = 5.0

# Helper functions
def load_data(filename):
    """
    Load data from a CSV file and return x, y, and error values.
    If no 'error' column exists, default errors are set to 1.
    """
    df = pd.read_csv(filename)
    if "error" in df.columns:
        errors = df["error"].values
    else:
        errors = np.ones(len(df))
    x = df["x"].values
    y = df["y"].values
    return x, y, errors


def fit_line(x, y, weights=None):
    """Fit a straight line (y = m*x + b) and return slope (m) and intercept (b)."""
    if weights is not None:
        m, b = np.polyfit(x, y, 1, w=weights)
    else:
        m, b = np.polyfit(x, y, 1)
    return m, b


def fit_quadratic(x, y):
    """Fit a quadratic curve (y = a*x^2 + b*x + c) and return coefficients a, b, c."""
    a, b, c = np.polyfit(x, y, 2)
    return a, b, c

# Tests
@pytest.mark.parametrize("filename", DATA_FILES)
def test_correlation(filename):
    """
    Verify that x and y are strongly correlated.
    The correlation coefficient (r) should be greater than 0.7
    for a reasonable linear relationship.
    """
    x, y, _ = load_data(filename)
    r, _ = pearsonr(x, y)
    assert abs(r) > 0.7, f"{filename}: correlation too weak (r={r:.3f})"


@pytest.mark.parametrize("filename", DATA_FILES)
def test_chi_squared(filename):
    """
    Evaluate the goodness of fit using the reduced chi-squared statistic.
    A value close to 1 indicates that the fitted line describes the data well.
    Acceptable range: 0.5 ≤ χ² ≤ 2.0.
    """
    x, y, errors = load_data(filename)
    weights = 1.0 / (errors ** 2)

    m, b = fit_line(x, y, weights)
    y_fit = m * x + b

    chi2 = np.sum(((y - y_fit) ** 2) / (errors ** 2))
    dof = len(x) - 2  # degrees of freedom for a linear fit
    reduced_chi2 = chi2 / dof

    assert 0.5 <= reduced_chi2 <= 2.0, f"{filename}: poor fit (reduced χ²={reduced_chi2:.2f})"


@pytest.mark.parametrize("filename", DATA_FILES)
def test_quadratic_fit(filename):
    """
    Fit a quadratic model to the data and compare it with the linear fit.
    For purely linear data, the quadratic coefficient (a) should be close to zero.
    """
    x, y, _ = load_data(filename)
    m, b = fit_line(x, y)
    a2, b2, c2 = fit_quadratic(x, y)

    # For linearly generated data, 'a' should be small
    assert abs(a2) < 0.1, f"{filename}: quadratic curvature too high (a={a2:.3f})"

