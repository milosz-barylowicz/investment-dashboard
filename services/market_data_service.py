#!/usr/bin/env python3

import yfinance as yf

class MarketDataService:
    def __init__(self):
        pass

    def fetch_historical_data(self, ticker: str):
        historical_data = yf.Ticker(ticker).history(
            period="1y",
            interval="1d",
            auto_adjust=False
        )

        return historical_data
