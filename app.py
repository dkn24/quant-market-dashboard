import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Download Data (Tech, Energy, Gold, and S&P 500 Benchmark)
tickers = ['AAPL', 'XOM', 'GLD', '^GSPC']
print("Downloading market data...")
data = yf.download(tickers, start='2023-01-01', end='2026-01-01', progress=False)

# Safely extract 'Adj Close' or 'Close' regardless of yfinance version/column format
if 'Adj Close' in data.columns:
    prices = data['Adj Close']
elif isinstance(data.columns, pd.MultiIndex) and 'Adj Close' in data.columns.levels[0]:
    prices = data['Adj Close']
else:
    # Fallback to general close or whatever data is returned
    prices = data['Close'] if 'Close' in data.columns else data

prices = prices.dropna()

# 2. Calculate Returns
daily_returns = prices.pct_change().dropna()
cumulative_returns = (1 + daily_returns).cumprod() - 1

# 3. Calculate Risk Metrics
annualised_vol = daily_returns.std() * np.sqrt(252)
annualised_return = daily_returns.mean() * 252
rolling_max = (1 + daily_returns).cumprod().cummax()
max_drawdown = ((1 + daily_returns).cumprod() / rolling_max - 1).min()

# Assuming a 3% risk-free rate for the Sharpe Ratio
risk_free_rate = 0.03
sharpe_ratio = (annualised_return - risk_free_rate) / annualised_vol

# 4. Compile into a Summary Table
risk_metrics = pd.DataFrame({
    'Annualised Return': annualised_return,
    'Annualised Volatility': annualised_vol,
    'Max Drawdown': max_drawdown,
    'Sharpe Ratio': sharpe_ratio
})

print("\n--- Portfolio Risk Metrics ---")
print(risk_metrics)

# 5. Plotting Cumulative Returns & Correlation Heatmap
plt.figure(figsize=(10, 5))
cumulative_returns.plot(title='Cumulative Returns Dashboard (2023 - 2026)')
plt.xlabel('Date')
plt.ylabel('Growth of $1')
plt.show()

# Correlation Matrix & Heatmap
corr_matrix = daily_returns.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Asset Correlation Matrix')
plt.show()