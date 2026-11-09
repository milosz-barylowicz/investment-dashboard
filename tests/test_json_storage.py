#!/usr/bin/env python3

import json
from services.json_storage import save_data

def test_safe_data(tmp_path):
    path = tmp_path / "XTB.json"

    data = {
        "ticker": "XTB",
        "currency": "PLN"
    }

    save_data(path, data)

    assert path.exists()

    with path.open(encoding="utf-8") as file:
        loaded = json.load(file)

    assert loaded == data
