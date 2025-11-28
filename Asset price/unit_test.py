import os
import importlib.util
import numpy as np
import pandas as pd
from pathlib import Path


def load_module(path):
    """Dynamically load a Python module from any filepath."""
    spec = importlib.util.spec_from_file_location("daily_script", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_script_runs_end_to_end(tmp_path):
    """Test the script runs with a fake CSV."""
    
    # create fake cleaned_apple_data.csv
    df = pd.DataFrame({"Close/Last": [100, 102, 105, 103, 110]})
    csv_path = tmp_path / "cleaned_apple_data.csv"
    df.to_csv(csv_path, index=False)

    # correct root: parent[1] = DAT5501_Repo
    project_root = Path(__file__).resolve().parents[1]

    script_path = project_root / "Asset price" / "Daily price change" / "daily_price_change.py"
    assert script_path.exists(), f"Script not found at: {script_path}"

    # read script
    script_text = script_path.read_text()

    # patch __file__ directory lookup
    script_text = script_text.replace(
        "script_dir = os.path.dirname(os.path.abspath(__file__))",
        f"script_dir = r'{tmp_path.as_posix()}'"
    )

    # write patched copy
    script_copy = tmp_path / "script.py"
    script_copy.write_text(script_text)

    # load patched module
    module = load_module(script_copy)

    # verify plot is created
    output_plot = tmp_path / "daily_sorting_t_vs_n.png"
    assert output_plot.exists(), "Expected plot was not generated."
    print(list(project_root.iterdir()))



