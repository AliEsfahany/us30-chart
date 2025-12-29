import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="US30 Live Chart", layout="wide")
st.title("📈 US30 (Dow Jones) – Live Chart")

# انتخاب تایم‌فریم و دوره
interval = st.selectbox("تایم‌فریم:", ["1h", "4h", "1d"], index=2)
period = st.selectbox("بازه زمانی:", ["7d", "30d", "90d"], index=1)

# دریافت داده
symbol = "^DJI"
data = yf.download(symbol, interval=interval, period=period)

# بررسی ستون‌های مورد نیاز
required_columns = ['Open','High','Low','Close']
if all(col in data.columns for col in required_columns):
    data = data.dropna(subset=required_columns)

    if data.empty:
        st.error("داده‌ای دریافت نشد بعد از حذف NaN")
    else:
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
else:
    st.error(f"ستون‌های مورد نیاز برای رسم چارت موجود نیستند: {required_columns}")
    st.write("ستون‌های دریافت‌شده:", data.columns.tolist())
