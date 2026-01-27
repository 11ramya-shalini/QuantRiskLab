import pandas as pd
import numpy as np
import os

def calculate_returns(csv_path="data/stock_prices.csv"):
    #prices: pd.DataFrame
    # Load stock prices
    prices = pd.read_csv(csv_path, index_col=0, parse_dates=True)

    # daily percentage returns
    daily_returns = prices.pct_change().dropna()
    
    # Log returns
    log_returns = np.log(1 + daily_returns)

    return daily_returns, log_returns

if __name__ == "__main__":
    daily, log = calculate_returns()
    print("Daily Returns (first 5 rows): ")
    print(daily.head())
    print("\nLog Returns (first 5 rows): ")
    print(log.head())