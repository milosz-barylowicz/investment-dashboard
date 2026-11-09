#!/usr/bin/env python3

import streamlit as st


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
