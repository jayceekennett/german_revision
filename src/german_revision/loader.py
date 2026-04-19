# csv_loader.py
from __future__ import annotations
import csv
from pathlib import Path
import pandas as pd
from typing import Any
import json


# ------------------------------ LOAD CSVS ------------------------------------

# relative base directory
DATA_DIR = Path(__file__).resolve().parent / "data"


def _normalise_filename(filename: str) -> Path:
    p = Path(filename)
    if p.is_absolute():
        return p
    parts = p.parts
    if parts and parts[0] == "data":
        p = Path(*parts[1:])
    return DATA_DIR / p

# ------------------------------ LOAD JSON ------------------------------------

def get_json(filename: str) -> Any:
    file_path = _normalise_filename(filename)
    sentence_bank = json.loads(file_path.read_text(encoding="utf-8"))
    return sentence_bank

# ------------------------------ LOAD CSVS ------------------------------------
def get_name(f: str) -> str:
    return Path(f).stem


def read_csv(filename: str, **csv_params) -> list[Any]:
    file_path = _normalise_filename(filename)
    with file_path.open(encoding="utf-8", newline="") as file:
        return list(csv.reader(file, **csv_params))


def get_csvs(filenames) -> dict[Any]:
    data = {}
    for f in filenames:
        name = get_name(f)
        csv_file = read_csv(f, delimiter=",")
        data[name] = csv_file
    return data

def get_verbs(filename: str) -> pd.DataFrame:
    file_path = _normalise_filename(filename)
    return pd.read_csv(file_path)
    