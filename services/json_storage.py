#!/usr/bin/env python3

# service which will deal with json file storage of data

import json
from pathlib import Path

def save_data(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
