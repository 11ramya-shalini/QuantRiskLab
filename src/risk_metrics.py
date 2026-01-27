import numpy as np
import pandas as pd
from src.monte_carlo import monte_carlo_simulation

def calculate_volatility(price_paths):
    """
    Volatility of final prices across simulations
    """
    final_prices = price_paths[-1]
    returns = (final_prices - price_paths[0]) / price_paths[0]
    return np.std(returns)

def calculate_var(price_paths, confidence_level=0.95):
    """
    Vaule at Risk (VaR)
    """
    final_prices = price_paths[-1]
    returns = (final_prices - price_paths[0]) / price_paths[0]
    var = np.percentile(returns, (1 - confidence_level) * 100)
    return var

def calculate_max_drawdown(price_paths):
    """
    Maximum Drawdown
    """
    cumulative_max = np.maximum.accumulate(price_paths, axis=0)
    drawdowns = (price_paths - cumulative_max) / cumulative_max
    max_drawdown = np.min(drawdowns)
    return max_drawdown

if __name__ == "__main__":
    results = monte_carlo_simulation()

    for stock, paths in results.items():
        vol = calculate_volatility(paths)
        var = calculate_var(paths)
        mdd = calculate_max_drawdown(paths)

        print(f"\nRisk Metrics for {stock}")
        print(f"Volatility: {vol:.4f}")
        print(f"VaR (95%): {var:.4f}")
        print(f"Max Drawdown: {mdd:.4f}")