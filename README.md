# 📈 Quantitative Portfolio Risk Analytics & Optimization Platform

A quantitative finance platform that combines **Monte Carlo simulation, portfolio optimization, risk analytics, and interactive visualization** to evaluate investment portfolios using historical market data.

Built as part of my undergraduate studies, this project applies concepts from **financial mathematics, probability theory, statistics, optimization, and computational finance** to model uncertainty, quantify risk, and identify optimal asset allocations.

---

# 🌐 Live Demo

🚀 **The Dashboard**

[Watch Demo Video](/assets/Live_demo.mp4)

---

# 🎬 Interactive Dashboard Walkthrough

The dashboard enables users to explore portfolio performance, risk characteristics, simulation outcomes, and optimization results through an interactive interface.

---

# 📸 Dashboard Preview

## 📈 Historical Stock Price Analysis

![Stock Prices](/assets/stock_prices.png)

Track historical price movements across selected assets and compare long-term performance trends.

---

## 📉 Daily Return Analysis

![Returns](/assets/daily_returns.png)

Visualize daily percentage returns and analyze short-term market fluctuations.

---

## 🎲 Monte Carlo Simulation

![Monte Carlo](/assets/monte_carlo1.png)
![Monte Carlo](/assets/monte_carlo2.png)

Generate thousands of possible future price paths using stochastic simulations based on historical return distributions.

---

## ⚠️ Portfolio Risk Analytics

The platform evaluates key financial risk metrics:

- Volatility
- Value-at-Risk (VaR)
- Maximum Drawdown

![risk](/assets/risk1.png)
![risk](/assets/risk2.png)
![risk](/assets/risk3.png)

---

## 🧮 Portfolio Optimization

![Portfolio Allocation](/assets/optimal_allo.png)

Determine optimal portfolio weights using risk-adjusted return analysis.

![Portfolio Allocation](/assets/optimal_weight.png)

---

## ⭐ Efficient Frontier

![Efficient Frontier](/assets/frontier1.png)

Explore the risk-return landscape and identify the portfolio with the strongest risk-adjusted performance.

![Efficient Frontier](/assets/frontire2.png)

---

# 🚀 Project Overview

This platform provides an end-to-end workflow for portfolio analysis:

1. Retrieve historical stock market data
2. Calculate return distributions
3. Simulate future price behavior
4. Quantify portfolio risk
5. Optimize asset allocation
6. Visualize the Efficient Frontier
7. Explore results through an interactive dashboard

The goal is to bridge quantitative finance theory with practical implementation using Python.

---

# 🎯 Key Features

## Market Data Collection

- Downloads historical equity data using Yahoo Finance
- Supports multiple assets simultaneously
- Automatically stores and manages datasets

## Return Analysis

- Daily percentage returns
- Logarithmic returns
- Statistical performance evaluation

## Monte Carlo Simulation

- Simulates future stock price trajectories
- Generates 1,000+ possible future outcomes
- Models uncertainty using historical return characteristics

## Risk Analytics

Calculates:

- Portfolio Volatility
- Value-at-Risk (VaR)
- Maximum Drawdown

## Portfolio Optimization

- Generates thousands of candidate portfolios
- Computes expected return and risk
- Maximizes risk-adjusted return
- Produces optimal portfolio allocations

## Efficient Frontier Visualization

- Simulates 5,000 portfolio combinations
- Maps risk-return tradeoffs
- Highlights the optimal portfolio

## Interactive Dashboard

Built using Streamlit for real-time exploration and visualization.

---

# 📌 Key Results

- Simulated 1,000 future price paths per asset
- Generated 5,000 portfolio combinations
- Evaluated downside risk using VaR
- Measured portfolio volatility and drawdowns
- Identified optimal asset allocations
- Constructed and visualized the Efficient Frontier
- Delivered results through an interactive Streamlit dashboard

---

# 🧮 Quantitative Methods Used

## Monte Carlo Simulation

Future asset prices are simulated using stochastic return generation based on historical log-return distributions.

This allows probabilistic forecasting of future market behavior under uncertainty.

---

## Portfolio Return Estimation

Expected portfolio returns are computed using weighted asset returns.

---

## Portfolio Risk Estimation

Portfolio volatility is estimated using the covariance matrix of asset returns and portfolio allocations.

---

## Portfolio Optimization

The optimization engine:

1. Generates random portfolio allocations
2. Calculates portfolio return and risk
3. Evaluates risk-adjusted performance
4. Selects the portfolio with the highest Sharpe Ratio approximation

---

## Value-at-Risk (VaR)

Measures the potential downside loss at a 95% confidence level.

---

## Maximum Drawdown

Measures the largest peak-to-trough decline experienced during the simulation horizon.

---

# 🏗️ Project Architecture

```text
portfolio-risk-optimization/
│
├── dashboard/
│   ├── __init__.py
│   └── app.py
│
├── data/
│   └── stock_prices.csv
│
├── src/
│   ├── __init__.py
│   ├── data_collection.py
│   ├── returns.py
│   ├── monte_carlo.py
│   ├── risk_metrics.py
│   └── optimization.py
│
├── assets/
│   ├── dashboard_demo.gif
│   ├── stock_prices.png
│   ├── returns_analysis.png
│   ├── monte_carlo.png
│   ├── portfolio_weights.png
│   └── efficient_frontier.png
│
├── main.py
├── README.md
└── .gitignore
```

---

# 🔄 Workflow

```text
Historical Market Data
          │
          ▼
   Return Analysis
          │
          ▼
 Monte Carlo Simulation
          │
          ▼
   Risk Evaluation
          │
          ▼
 Portfolio Optimization
          │
          ▼
 Efficient Frontier
          │
          ▼
 Interactive Dashboard
```

---

# 🛠️ Technology Stack

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Data Collection

- yFinance

## Visualization

- Matplotlib

## Dashboard Development

- Streamlit

## Quantitative Finance

- Monte Carlo Simulation
- Portfolio Theory
- Risk Modeling
- Efficient Frontier Analysis
- Value-at-Risk (VaR)
- Maximum Drawdown

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/11ramya-shalini/QuantRiskLab.git
cd QuantRiskLab
```

## Install Dependencies

```bash
pip install pandas numpy matplotlib streamlit yfinance
```

## Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🎓 Academic Context

Developed as part of my undergraduate studies to explore practical applications of:

- Financial Mathematics
- Probability Theory
- Statistical Modeling
- Portfolio Optimization
- Quantitative Risk Management
- Computational Finance

The project demonstrates how quantitative finance concepts can be implemented and visualized using modern Python tools.

---

# 🔮 Future Improvements

- Black-Litterman Portfolio Optimization
- Conditional Value-at-Risk (CVaR)
- Risk Parity Portfolios
- Factor Model Analysis
- Portfolio Backtesting Engine
- Machine Learning Return Forecasting
- Real-Time Market Data Integration
- Advanced Performance Attribution

---

# 👤 Author

**Ramya Shalini**

B.Sc. Mathematics with Computer Applications

**Interests**

Quantitative Finance • Financial Mathematics • Data Science • Machine Learning • Risk Modeling • Quantitative Research

---

⭐ If you found this project interesting, consider giving it a star.