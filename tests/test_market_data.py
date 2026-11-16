#!/usr/bin/env python3

import pandas as pd

from services.market_data_service import MarketDataService


def test_fetch_historical_data():
    service = MarketDataService()

    data = service.fetch_historical_data("CDR.WA")

    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "Close" in data.columns
