"""
    Set of utility functions to handle json files
    Copy right by Benjamin A. Bernal. JUN2024
"""

# Libraries
import typing as hint
from os import path
import json

def to_dict(file_path:str) -> dict[str, hint.Any]:
    """loads a json file into a dictionary"""
    assert path.exists(file_path), "Either the file or the directory do not exists"

    with open(file_path, "r", encoding="UTF-8") as file:
        return json.load(file)
    
