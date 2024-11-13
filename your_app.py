import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt

# Streamlit web app setup
st.title("Stock Price Viewer with Volatility Insights")

# User input: stock ticker or company name
stock_ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT, TSLA):")

# Time period options for stock data
period = st.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"])

if stock_ticker:
    # Fetch data from yfinance
    try:
        stock = yf.Ticker(stock_ticker)
        df = stock.history(period=period)

        # Plot the Closing Prices
        st.write(f"**Closing Price Chart for {stock_ticker.upper()} ({period})**")
        fig, ax = plt.subplots()
        df['Close'].plot(ax=ax, color='blue', title=f"Closing Prices for {stock_ticker.upper()}")
        ax.set_ylabel("Closing Price (USD)")
        ax.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)

        # Volatility Insight
        st.write("**Volatility Analysis**")
        daily_returns = df['Close'].pct_change().dropna()
        volatility = daily_returns.std()
        st.write(f"Volatility (Standard Deviation of Daily Returns): {volatility:.2%}")

    except Exception as e:
        st.write("An error occurred while fetching data. Please check the stock ticker and try again.")

