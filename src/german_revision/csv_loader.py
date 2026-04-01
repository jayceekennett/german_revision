# csv_loader.py

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd


# Base directory for data files, relative to this module
DATA_DIR = Path(__file__).resolve().parent / "data"


def _normalise_filename(filename: str) -> Path:
    p = Path(filename)

    # If the user gives an absolute path, respect it.
    if p.is_absolute():
        return p

    # Strip a leading "data/" if present (e.g. "data/adjectives.csv")
    parts = p.parts
    if parts and parts[0] == "data":
        p = Path(*parts[1:])  # drop the first part

    # Point to the packaged data directory
    return DATA_DIR / p


# ------------------------------ LOAD CSVS ------------------------------------


def get_name(f: str) -> str:
    return Path(f).stem


def read_csv(filename: str, **csv_params):
    # return list of row from csv file

    file_path = _normalise_filename(filename)
    with file_path.open(encoding="utf-8", newline="") as file:
        return list(csv.reader(file, **csv_params))


def get_csvs(filenames):

    data = {}
    for f in filenames:
        name = get_name(f)
        csv_file = read_csv(f, delimiter=",")
        data[name] = csv_file
    return data


def get_verbs(filename: str) -> pd.DataFrame:
    file_path = _normalise_filename(filename)
    return pd.read_csv(file_path)
    