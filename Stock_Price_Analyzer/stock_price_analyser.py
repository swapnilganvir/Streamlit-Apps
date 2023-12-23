import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

# App heading and description
st.write(
    """
    # Stock Price Analyser

    Shown are the stock prices of Apple.
    """
)


ticker_symbol = st.text_input("Enter Stock Symbol", "AAPL", key="placeholder")
# ticker_symbol = "AAPL"

# horizontal layout
col1, col2 = st.columns(2)

# start date of analysis
with col1:
    start_date = st.date_input("Input Starting Date", datetime.date(2023, 1, 1))

# end date of analysis
with col2:
    end_date = st.date_input("Input Ending Date", datetime.date(2023, 12, 31))

ticker_data = yf.Ticker(ticker_symbol)

# look at the historical data7
ticker_df = ticker_data.history(period="1d", start=f"{start_date}", end=f"{end_date}")

# Show all the data in the dataframe
st.write(f" ### {ticker_symbol}'s EOD prices")
st.dataframe(ticker_df)

# showcasing charts
st.write(
    """
    ## Daily Closing Price Chart
    """
)
st.line_chart(ticker_df.Close)

st.write(
    """
    ## Volume of Shares traded each day
    """
)
st.line_chart(ticker_df.Volume)

# adding my name
c1, c2, c3, c4 = st.columns(4)
with c4:
    st.markdown(
        """
        ---
        **Made by :-** *Swapnil G.*
        """
    )


    