import streamlit as st
from streamlit_autorefresh import st_autorefresh  # << این را اضافه کن
import yfinance as yf
import mplfinance as mpf
from io import BytesIO

st.set_page_config(page_title="US30 Live Chart", layout="wide")
st.title("📈 US30 (Dow Jones) – Live Chart (Auto Refresh)")

# انتخاب تایم‌فریم و دوره
interval = st.selectbox("تایم‌فریم:", ["1h", "4h", "1d"], index=2)
period = st.selectbox("بازه زمانی:", ["7d", "30d", "90d"], index=1)

# Auto Refresh هر 60 ثانیه
st_autorefresh(interval=60000, limit=None, key="refresh")  # 60s

# دریافت داده
symbol = "^DJI"
data = yf.download(symbol, interval=interval, period=period)

if data.empty:
    st.error("داده‌ای دریافت نشد")
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
    st.image(buf)
