import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# =======================
# PATH SETUP
# =======================
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_DIR)
DATA_PATH = os.path.join(PROJECT_DIR, "data", "stock_prices.csv")

# =======================
# IMPORT PROJECT MODULES
# =======================
from src.returns import calculate_returns
from src.monte_carlo import monte_carlo_simulation
from src.risk_metrics import calculate_volatility, calculate_var, calculate_max_drawdown
from src.optimization import optimize_portfolio, generate_efficient_frontier

# =======================
# GLOBAL PLOT STYLE
# =======================
plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "figure.figsize": (10, 5),
    "axes.titlesize": 14,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "lines.linewidth": 1.8,
})

# Page config
st.set_page_config(page_title="Monte Carlo Based Portfolio Risk & Optimization Dashboard", layout="wide")

st.title("📊 Monte Carlo Based Portfolio Risk & Optimization Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH, index_col=0, parse_dates=True)

prices = load_data()

# Sidebar
st.sidebar.header("Settings")
stocks = prices.columns.tolist()
selected_stocks = st.sidebar.multiselect(
    "Select Stocks", prices.columns.tolist(), default=prices.columns.tolist()
)

prices = prices[selected_stocks]
if len(selected_stocks) == 0:
    st.warning("Please select at least one stock")
    st.stop()


# =======================
# STOCK PRICE PLOT
# =======================
st.subheader("📈 Stock Prices Movement")
st.divider()

fig, ax = plt.subplots()
prices.plot(ax=ax, alpha=0.9)
ax.set_title("Stock Prices Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend(frameon=False)
ax.grid(True, linestyle="--", alpha=0.4)
st.pyplot(fig)

# =======================
# RETURNS
# =======================
st.subheader("📉 Daily Returns")
st.divider()

daily_returns, log_returns = calculate_returns(csv_path=DATA_PATH)
daily_returns = daily_returns[selected_stocks]

fig, ax = plt.subplots()
daily_returns.plot(ax=ax, alpha=0.7)
ax.axhline(0, color="black", linewidth=1, alpha=0.6)
ax.set_title("Daily Returns")
ax.set_ylabel("Return")
ax.legend(frameon=False)
ax.grid(True, linestyle="--", alpha=0.4)
st.pyplot(fig)

# =======================
# MONTE CARLO
# =======================
st.subheader("🎲 Monte Carlo Simulation")
st.divider()

stock_for_mc = st.selectbox("Choose stock for simulation", selected_stocks)
# Call Monte Carlo using the CSV and the single stock
simulations_dict = monte_carlo_simulation(csv_path=DATA_PATH, stocks=selected_stocks)
simulations = simulations_dict[stock_for_mc]

fig, ax = plt.subplots()
ax.plot(simulations, color="blue", alpha=0.08)
ax.set_title(f"Monte Carlo Price Simulation – {stock_for_mc}")
ax.set_xlabel("Days")
ax.set_ylabel("Price")
ax.grid(True, linestyle="--", alpha=0.3)
st.pyplot(fig)

# =======================
# RISK METRICS
# =======================
st.subheader("⚠️ Risk Metrics")
st.divider()

for stock in selected_stocks:
    vol = calculate_volatility(daily_returns[stock])
    var = calculate_var(daily_returns[stock])
    mdd = calculate_max_drawdown(prices[stock])

    st.markdown(f"""
    **{stock}**
    - Volatility: `{vol:.4f}`
    - VaR (95%): `{var:.4f}`
    - Max Drawdown: `{mdd:.4f}`
    """)

# =======================
# PORTFOLIO OPTIMIZATION
# =======================
st.subheader("🧮 Optimal Portfolio Allocation")
st.divider()

(best_risk, best_ret, weights), assets = optimize_portfolio(returns=daily_returns)


allocation = pd.DataFrame({
    "Stock": assets,
    "Weight": weights
})

st.dataframe(allocation, use_container_width=True)

# Allocation Bar Chart
fig, ax = plt.subplots()
ax.bar(assets, weights)
ax.set_title("Optimal Portfolio Weights")
ax.set_ylabel("Weight")
ax.grid(axis="y", linestyle="--", alpha=0.4)
st.pyplot(fig)

st.markdown(f"""
**Expected Portfolio Return:** `{best_ret:.4f}`  
**Expected Portfolio Risk:** `{best_risk:.4f}`
""")

# =======================
# EFFICIENT FRONTIER
# =======================
st.subheader("Efficient Frontier")

risks, returns, weights_list = generate_efficient_frontier(daily_returns)

(best_risk, best_ret, best_weights), assets = optimize_portfolio(
    returns=daily_returns
)

fig, ax = plt.subplots(figsize=(8, 6))

# All portfolios
scatter = ax.scatter(
    risks,
    returns,
    c=returns / risks,
    cmap="viridis",
    alpha=0.4
)

# Optimal portfolio (Max Sharpe)
ax.scatter(
    best_risk,
    best_ret,
    color="red",
    marker="*",
    s=250,
    label="Optimal Portfolio"
)

ax.annotate(
    f"Return: {best_ret:.3f}\nRisk: {best_risk:.3f}",
    (best_risk, best_ret),
    textcoords="offset points",
    xytext=(10, 10),
    fontsize=9,
    color="red"
)

ax.set_xlabel("Risk (Volatility)")
ax.set_ylabel("Expected Return")
ax.set_title("Efficient Frontier")
ax.legend()
plt.colorbar(scatter, label="Sharpe Ratio")

st.pyplot(fig)
st.markdown("Optimal Portfolio Details")

st.metric("Expected Return", f"{best_ret:.4f}")
st.metric("Risk (Volatility)", f"{best_risk:.4f}")
st.metric("Sharpe Ratio", f"{best_ret / best_risk:.4f}")
