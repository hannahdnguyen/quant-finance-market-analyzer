import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# stocks to analyze
stocks = ["AAPL", "NVDA", "MSFT", "SPY"]

# download historical stock data
data = yf.download(stocks, start="2020-01-01")["Adj Close"]

# calculate daily returns
returns = data.pct_change().dropna()

# annualized returns and covariance matrix
annual_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252

# number of simulations
num_portfolios = 5000

results = np.zeros((3, num_portfolios))
weights_record = []

for i in range(num_portfolios):

    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)

    weights_record.append(weights)

    portfolio_return = np.sum(weights * annual_returns)

    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    sharpe_ratio = portfolio_return / portfolio_volatility

    results[0,i] = portfolio_return
    results[1,i] = portfolio_volatility
    results[2,i] = sharpe_ratio


# convert results into dataframe
results_frame = pd.DataFrame(results.T, columns=["Return","Volatility","Sharpe"])

# find best portfolio
max_sharpe_port = results_frame.iloc[results_frame["Sharpe"].idxmax()]

print("Best Portfolio Based on Sharpe Ratio")
print(max_sharpe_port)

# plot efficient frontier
plt.figure(figsize=(10,6))
plt.scatter(results_frame.Volatility, results_frame.Return, c=results_frame.Sharpe, cmap="viridis")

plt.colorbar(label="Sharpe Ratio")

plt.xlabel("Volatility")
plt.ylabel("Expected Return")
plt.title("Monte Carlo Efficient Frontier")

plt.scatter(max_sharpe_port.Volatility,
            max_sharpe_port.Return,
            color="red",
            s=100,
            label="Max Sharpe Portfolio")

plt.legend()

plt.show()
