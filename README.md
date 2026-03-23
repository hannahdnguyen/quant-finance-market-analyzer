# Quant Finance Market Analyzer

A Python-based financial analysis tool that evaluates stock performance and portfolio risk using quantitative finance techniques.

This project downloads historical market data, analyzes asset returns, and uses Monte Carlo simulations to construct thousands of potential portfolios. It then identifies the optimal portfolio based on risk-adjusted return and visualizes the Efficient Frontier.

---

## Project Overview

This tool applies concepts from quantitative finance and portfolio management to analyze a set of stocks and evaluate different portfolio allocations.

The program retrieves historical stock prices, calculates returns and risk metrics, and simulates thousands of portfolio combinations to determine which allocation produces the best risk-adjusted performance.

The analysis includes companies such as Apple, Nvidia, and Microsoft, and compares them to the S&P 500 market index.

---

## Features

- Automatic financial market data retrieval
- Daily and annualized return calculations
- Portfolio volatility analysis
- Sharpe ratio calculation
- Monte Carlo portfolio simulation
- Efficient Frontier visualization
- Correlation analysis between assets
- Performance comparison against the S&P 500

---

## Quantitative Finance Methods

This project implements several concepts used in professional asset management and quantitative finance:

### Modern Portfolio Theory
Portfolio construction is based on principles from Modern Portfolio Theory, which balances expected return and portfolio risk.

### Monte Carlo Simulation
The program simulates thousands of randomly generated portfolio allocations to explore the full range of possible investment outcomes.

### Efficient Frontier
The Efficient Frontier shows the set of portfolios that offer the highest expected return for a given level of risk.

### Sharpe Ratio
Risk-adjusted performance is evaluated using the Sharpe Ratio, which measures return relative to volatility.

---

## Technologies Used

Python

Libraries:

- pandas
- numpy
- matplotlib
- yfinance

These tools are commonly used in financial data analysis and quantitative research.

---

## Assets Analyzed

The project analyzes the following assets:

- Apple (AAPL)
- Nvidia (NVDA)
- Microsoft (MSFT)
- S&P 500 ETF (SPY)

These assets were selected to represent large-cap technology companies and the overall U.S. equity market.

---

## Example Output

The program generates:

- Annualized returns for each asset
- Portfolio risk and return statistics
- The optimal portfolio based on Sharpe Ratio
- A visualization of the Efficient Frontier from thousands of simulated portfolios

---

## Installation

Clone the repository and install dependencies.

```bash
pip install -r requirements.txt
