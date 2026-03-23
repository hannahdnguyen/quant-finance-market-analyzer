import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# stocks to analyze
stocks = ["AAPL", "NVDA", "MSFT", "SPY"]

# download stock data
data = yf.download(stocks, start="2020-01-01")["Adj Close"]

# calculate daily returns
returns = data.pct_change().dropna()

# calculate annual returns
annual_returns = returns.mean() * 252

print("Average Annual Returns")
print(annual_returns)

# normalize price data for comparison
normalized = data / data.iloc[0]

# plot performance
normalized.plot(figsize=(10,6))
plt.title("Stock Performance vs S&P 500")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.legend(stocks)
plt.show()
