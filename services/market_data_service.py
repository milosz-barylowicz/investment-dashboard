#!/usr/bin/env python3

import yfinance as yf
import pandas as pd

class MarketDataService:
    def __init__(self):
        pass

    def fetch_historical_data(self, ticker: str):
        historical_data = yf.Ticker(ticker).history(
            period="1y",
            interval="1d",
            auto_adjust=False
        )

        self.validate_historical_data(historical_data)

        return historical_data


    def validate_historical_data(self, data: pd.DataFrame):
        if data.empty:
            raise ValueError("No historical data available for given ticker")

        required_columns = ["Open", "High", "Low", "Close", "Volume"]
        if not all(column in data.columns for column in required_columns):
            raise ValueError("Historical data is missing required columns")

        for column in required_columns:
            if data[column].isna().any():
                raise ValueError(
                         f"Historical data contains missing values in column: {column}")
        return True
