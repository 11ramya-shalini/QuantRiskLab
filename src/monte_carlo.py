import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def monte_carlo_simulation(
        prices=None,
        csv_path="data/stock_prices.csv",
        stocks=None,
        days=252,
        simulations=1000
):
    if stocks is None:
        stocks = ["AAPL","MSFT","GOOGL"]

    # Load price data
    if prices is None:
        prices = pd.read_csv(csv_path, index_col=0, parse_dates=True)

    # Select stocks
    all_price_paths = {}
    for stock in stocks:
        stock_prices = prices[stock]

        # Calculate log returns
        log_returns = np.log(stock_prices / stock_prices.shift(1)).dropna()

        # Estimate parameters
        mu = log_returns.mean()
        sigma = log_returns.std()

        # Last observed price
        last_price = stock_prices.iloc[-1]

        # Simulate random returns
        random_returns = np.random.normal(
            mu, sigma, (days, simulations)
        )

        # Price paths
        price_paths = np.zeros((days, simulations))
        price_paths[0] = last_price

        for t in range(1, days):
            price_paths[t] = price_paths[t - 1] * np.exp(random_returns[t])

        all_price_paths[stock] = price_paths

    return all_price_paths

if __name__ == "__main__":
    results = monte_carlo_simulation()

    # PLoth simulations
    fig, axes = plt.subplots(len(results), 1, figsize=(10, 8), sharex=True)
    for ax, (stock, paths) in zip(axes, results.items()):
        ax.plot(paths, alpha=0.3)
        ax.set_title(stock)
        ax.set_ylabel("Price")

    axes[-1].set_xlabel("Days")
    plt.tight_layout()
    plt.show()
