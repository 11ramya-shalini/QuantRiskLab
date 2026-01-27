import numpy as np
import pandas as pd


def optimize_portfolio(returns=None,csv_path="data/stock_prices.csv"):

    if returns is None:
        prices = pd.read_csv(csv_path, index_col=0, parse_dates=True)
        returns = prices.pct_change().dropna()

    # Expected returns and covariance
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    num_assets = len(mean_returns)

    # Random portfolios 
    num_portfolios = 5000
    results = []

    for _ in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)

        portfolio_return = np.dot(weights, mean_returns)
        portfolio_risk = np.sqrt(
            np.dot(weights.T, np.dot(cov_matrix, weights))
        )

        results.append((portfolio_risk, portfolio_return, weights))

    # Choose portfolio with maximum Sharpe ratio (risk-adjusted return)
    results = sorted(
        results, 
        key=lambda x: x[1] / x[0] if x[0] != 0 else -np.inf, 
        reverse=True)
    
    best_portfolio = results[0]

    return best_portfolio, mean_returns.index


if __name__ == "__main__":
    (risk, ret, weights), assets = optimize_portfolio()

    print("Optimal Portfolio Allocation:")
    for asset, weight in zip(assets, weights):
        print(f"{asset}: {weight:.2f}")

    print(f"\nExpected Return: {ret:.4f}")
    print(f"Expected Risk: {risk:.4f}")


def generate_efficient_frontier(returns, num_portfolios=5000):
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    num_assets = len(mean_returns)

    portfolio_returns = []
    portfolio_risks = []
    portfolio_weights = []

    for _ in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)

        ret = np.dot(weights, mean_returns)
        risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

        portfolio_returns.append(ret)
        portfolio_risks.append(risk)
        portfolio_weights.append(weights)

    return (
        np.array(portfolio_risks),
        np.array(portfolio_returns),
        portfolio_weights
    )
