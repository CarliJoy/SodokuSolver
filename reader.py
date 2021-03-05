from pathlib import Path
import pandas as pd

def read_excel(filename: Path):
    return pd.read_excel(filename, header=None).to_numpy().astype('float16')
