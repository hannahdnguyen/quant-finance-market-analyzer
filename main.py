import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# stocks to analyze
stocks = ["AAPL", "NVDA", "MSFT", "SPY"]

# download historical data
data = yf.download(stocks, start="2020-01-01")["Adj Close"]

# calculate daily returns
returns = data.pct_change().dropna()

# calculate annualized returns
annual_returns = returns.mean() * 252

# covariance matrix
cov_matrix = returns.cov() * 252

# equal portfolio weights
weights = np.array([0.25, 0.25, 0.25, 0.25])

# portfolio return
portfolio_return = np.sum(annual_returns * weights)

# portfolio volatility
portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# sharpe ratio (assuming risk free rate = 2%)
risk_free_rate = 0.02
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

print("Annual Returns")
print(annual_returns)

print("\nPortfolio Return:", portfolio_return)
print("Portfolio Volatility:", portfolio_volatility)
print("Sharpe Ratio:", sharpe_ratio)

# normalize prices for visualization
normalized = data / data.iloc[0]

# performance plot
normalized.plot(figsize=(10,6))
plt.title("Stock Performance vs S&P 500")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.legend(stocks)
plt.show()

# correlation matrix
corr = returns.corr()

print("\nCorrelation Matrix")
print(corr)
