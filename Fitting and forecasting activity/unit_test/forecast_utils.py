import numpy as np

def calculate_mae(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length")
    return np.mean(np.abs(y_true - y_pred))

def calculate_rmse(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length")
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

