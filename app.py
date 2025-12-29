import streamlit as st
import yfinance as yf
import mplfinance as mpf
from io import BytesIO
import pandas as pd
import time

st.set_page_config(page_title="US30 Live Chart", layout="wide")
st.title("📈 US30 (Dow Jones) – Live Chart (Auto Refresh)")

# انتخاب تایم‌فریم و دوره
interval = st.selectbox("تایم‌فریم:", ["1h", "4h", "1d"], index=2)
period = st.selectbox("بازه زمانی:", ["7d", "30d", "90d"], index=1)

# Auto Refresh هر 60 ثانیه
st.text("چارت هر 60 ثانیه به‌روز می‌شود")

def get_data():
    symbol = "^DJI"
    data = yf.download(symbol, interval=interval, period=period)
    return data

placeholder = st.empty()

while True:
    data = get_data()
    if data.empty:
        placeholder.error("داده‌ای دریافت نشد")
    else:
        buf = BytesIO()
        mpf.plot(
            data,
            type="candle",
            style="yahoo",
            volume=True,
            tight_layout=True,
            savefig=buf
        )
        placeholder.image(buf)
    time.sleep(60)  # بروزرسانی هر 60 ثانیه
