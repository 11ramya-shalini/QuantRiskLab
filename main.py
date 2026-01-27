from src.data_collection import fetch_stock_data
from src.returns import calculate_returns
from src.monte_carlo import monte_carlo_simulation
from src.risk_metrics import (
    calculate_volatility,
    calculate_var,
    calculate_max_drawdown
)
from src.optimization import optimize_portfolio


def main():
    stocks = ["AAPL", "MSFT", "GOOGL"]

    print("Fetching stock data...")
    fetch_stock_data(stocks)

    print("\nCalculating returns...")
    daily_returns, log_returns = calculate_returns()

    print("\nRunning Monte Carlo simulations...")
    mc_results = monte_carlo_simulation(stocks=stocks)

    print("\nCalculating risk metrics...")
    for stock, paths in mc_results.items():
        print(f"\n{stock}")
        print("Volatility:", calculate_volatility(paths))
        print("VaR (95%):", calculate_var(paths))
        print("Max Drawdown:", calculate_max_drawdown(paths))

    print("\nOptimizing portfolio...")
    (risk, ret, weights), assets = optimize_portfolio()

    print("\nOptimal Portfolio Allocation:")
    for asset, weight in zip(assets, weights):
        print(f"{asset}: {weight:.2f}")

    print(f"\nExpected Return: {ret:.4f}")
    print(f"Expected Risk: {risk:.4f}")


if __name__ == "__main__":
    main()
