# csv_loader.py



# ------------------------------ LOAD CSVS ------------------------------------

#def get_name(f):
 #       name = f.removeprefix("data/")
  #      name = name.removesuffix(".csv")
   #     return name

#def read_csv(filename, **csv_params):
 #   with open(filename, encoding='utf-8', newline='') as file:
    #    return list(csv.reader(file, **csv_params))

#def get_csvs(filenames):
 #   data = {}
  #  for f in filenames:
   #     name = get_name(f)
    #    csv_file = read_csv(f, delimiter = ",")
     #   data[name] = csv_file
    #return data

#def get_verbs(filename):
 #   dfv = pd.read_csv(filename)
  #  return dfv



#def read_csv(filename, **csv_params):
 #   file_path = pkg_resources.files(data).joinpath(filename)
  #  with open(file_path, encoding="utf-8", newline="") as file:
   #     return list(csv.reader(file, **csv_params))
    
   # csv_loader.py

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd


# Base directory for data files, relative to this module
DATA_DIR = Path(__file__).resolve().parent / "data"


def _normalise_filename(filename: str) -> Path:
    """
    Convert a filename like 'data/adjectives.csv' or 'adjectives.csv'
    into an absolute path inside the package's data directory.

    If an absolute path is passed, it is returned unchanged.
    """
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
    """
    Return a clean name for the CSV (e.g. 'adjectives' from
    'data/adjectives.csv' or 'adjectives.csv').
    """
    return Path(f).stem


def read_csv(filename: str, **csv_params):
    """
    Read a CSV file from the package data directory (or from an absolute path)
    and return a list of rows.
    """
    file_path = _normalise_filename(filename)
    with file_path.open(encoding="utf-8", newline="") as file:
        return list(csv.reader(file, **csv_params))


def get_csvs(filenames):
    """
    Given a list of filenames, return a dict mapping the cleaned name
    (e.g. 'adjectives') to the CSV contents.
    """
    data = {}
    for f in filenames:
        name = get_name(f)
        csv_file = read_csv(f, delimiter=",")
        data[name] = csv_file
    return data

def get_plurals(filename: str):
    name = get_name(filename)
    csv_file = read_csv(filename, delimiter = ",")

file_path = "data/plural_nouns.csv"

def get_verbs(filename: str) -> pd.DataFrame:
    """
    Load a verbs CSV into a pandas DataFrame.
    """
    file_path = _normalise_filename(filename)
    return pd.read_csv(file_path)
    