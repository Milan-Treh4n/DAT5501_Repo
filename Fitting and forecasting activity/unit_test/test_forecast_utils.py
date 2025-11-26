import numpy as np
import pytest
from unit_test.forecast_utils import calculate_mae, calculate_rmse

def test_calculate_mae_perfect_predictions():
    assert calculate_mae([1, 2, 3], [1, 2, 3]) == 0

def test_calculate_mae_shifted_predictions():
    result = calculate_mae([1, 2, 3], [2, 2, 2])
    expected = (1 + 0 + 1) / 3
    assert result == pytest.approx(expected)

def test_calculate_rmse_perfect_predictions():
    assert calculate_rmse([5, 5, 5], [5, 5, 5]) == 0

def test_calculate_rmse_shifted_predictions():
    result = calculate_rmse([1, 2], [2, 2])
    expected = np.sqrt(((1-2)**2 + (2-2)**2) / 2)
    assert result == pytest.approx(expected)

def test_length_mismatch():
    with pytest.raises(ValueError):
        calculate_mae([1,2,3], [1,2])

    with pytest.raises(ValueError):
        calculate_rmse([10,20], [10])
