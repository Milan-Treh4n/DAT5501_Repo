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
    
    # Create large enough dataset so ns is never empty
    df = pd.DataFrame({"Close/Last": np.linspace(100, 200, 30)})
    csv_path = tmp_path / "cleaned_apple_data.csv"
    df.to_csv(csv_path, index=False)

    # project root (DAT5501_Repo)
    project_root = Path(__file__).resolve().parents[1]

    # actual script
    script_path = project_root / "Asset price" / "Daily price change" / "daily_price_change.py"
    assert script_path.exists(), f"Script not found at: {script_path}"

    # read
    script_text = script_path.read_text()

    # patch to force local CSV folder
    script_text = script_text.replace(
        "script_dir = os.path.dirname(os.path.abspath(__file__))",
        f"script_dir = r'{tmp_path.as_posix()}'"
    )

    # write patched copy
    script_copy = tmp_path / "script.py"
    script_copy.write_text(script_text)

    # execute patched script
    load_module(script_copy)

    # ensure output image created
    output_plot = tmp_path / "daily_sorting_t_vs_n.png"
    assert output_plot.exists(), "Expected plot was not generated."



