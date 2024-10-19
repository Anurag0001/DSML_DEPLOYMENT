import streamlit as st
import yfinance as yf
import datetime


ticker_symbol=st.text_input("Please enter the ticker","VEDL.NS")
ticker_data= yf.Ticker(ticker_symbol)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please Enter the starting date", datetime.date(2023, 1, 1))
    

with col2:
    end_date = st.date_input("Please Enter the end date", datetime.date(2024, 10, 1))
   



# get historical market data
ticker_df = ticker_data.history(period="1d",start=start_date ,end=end_date)

st.header("Stock Price Analyser!")
st.write("here is the day wise stock movement: ")
st.text(ticker_symbol)
st.dataframe(ticker_df)


st.header("Price Movement overtime")
st.line_chart(ticker_df['Close'])


st.header("Volume movement Movement overtime")
st.line_chart(ticker_df['Volume'])



