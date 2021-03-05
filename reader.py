from pathlib import Path
import pandas as pd

from openpyxl import load_workbook

def read_excel(filename: Path):
    return pd.read_excel(filename, header=None).to_numpy()