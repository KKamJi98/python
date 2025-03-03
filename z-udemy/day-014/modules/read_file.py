import os
import pandas as pd
from pandas import DataFrame


def read_file(relative_path: str) -> DataFrame:
    current_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if relative_path[0:2] == "./":
        relative_path = relative_path[2:]
    elif relative_path[0] == "/":
        relative_path = relative_path[1:]

    file_path: str = os.path.join(current_dir, relative_path)

    df: DataFrame = pd.read_csv(file_path)

    return df
