import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(stocks, period="5y"):
    # Download last 5 years of data
    data = yf.download(stocks,period=period)
    # Extract only closing prices
    close_prices = data["Close"]

    # Ensure data folder exists
    os.makedirs("data",exist_ok=True)

    # Save to csv file
    close_prices.to_csv("data/stock_prices.csv")
    print("Stocks price data saved to data/stock_prices.csv")

if __name__ == "__main__":
    # List of stocks
    stocks = [
        "AAPL","MSFT","GOOGL","AMZN","META",
        "TSLA","NVDA","NFLX","JPM","BAC"]
    fetch_stock_data(stocks)    