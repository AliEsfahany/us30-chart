import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="US30 Live Chart", layout="wide")
st.title("📈 US30 (Dow Jones) – Live Chart")

# انتخاب تایم‌فریم و دوره
interval = st.selectbox("تایم‌فریم:", ["1h", "4h", "1d"], index=2)
period = st.selectbox("بازه زمانی:", ["7d", "30d", "90d"], index=1)

# دریافت داده
symbol = "^DJI"
data = yf.download(symbol, interval=interval, period=period)

if data.empty:
    st.error("داده‌ای دریافت نشد")
else:
    # حذف یا پر کردن NaN
    data = data.dropna(subset=['Open','High','Low','Close'])
    
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        increasing_line_color='green',
        decreasing_line_color='red'
    )])

    fig.update_layout(
        title=f"US30 ({symbol}) - Candlestick Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(fig, use_container_width=True)
