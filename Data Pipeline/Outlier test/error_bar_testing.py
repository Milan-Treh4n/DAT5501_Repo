def test_error_column_exists():
    df = pd.read_csv("data_with_error.csv")
    assert "error" in df.columns
