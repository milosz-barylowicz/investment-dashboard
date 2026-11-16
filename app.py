#!/usr/bin/env python3

import streamlit as st
import yfinance as yf


st.set_page_config(
    page_title="Investment Dashboard",
    page_icon="🌱",
    layout="wide"
)

st.title("Investment Dashboard")
st.caption("Personal Stock Market Dashboard")
st.info("The first version of this application is currently under development.")

stocks = ["XTB", "KRU", "CDPR"]

selected_stock = st.selectbox(
    "Select a stock",
    stocks
)

st.write(f"Selected stock: **{selected_stock}**")

# download one pice of data for one ticker
ticker = yf.Ticker("CDR.WA")
history = ticker.history(
    period="1y",
    interval="1d",
    auto_adjust=False
)

st.write(history.tail())
