# Financial Market and Risk Dashboard

A Python-based quantitative finance project designed to download historical market data, calculate core risk-adjusted performance metrics, and visualize asset correlations.

## 🚀 Features
* **Automated Data Retrieval**: Pulls multi-year historical adjusted close prices directly from Yahoo Finance (`yfinance`).
* **Return & Compounding Calculations**: Computes daily percentage returns and cumulative growth using `pandas` and `numpy`.
* **Professional Risk Metrics**: 
  * **Annualised Return & Volatility** (scaled using trading-day math).
  * **Maximum Drawdown** (measuring worst-case peak-to-trough historical losses).
  * **Sharpe Ratio** (evaluating risk-adjusted performance against a baseline risk-free rate).
* **Correlation Analysis**: Generates a Seaborn heatmap matrix to analyze how different asset classes move relative to each other.

---

## 🛠️ Tech Stack
* **Language**: Python 3.10+
* **Libraries**: 
  * `yfinance` (Data acquisition)
  * `pandas` & `numpy` (Data manipulation and vectorised math)
  * `matplotlib` & `seaborn` (Data visualization)

---

## 📂 Project Structure
```text
quant-market-dashboard/
│
├── venv/                 # Virtual environment (ignored by git)
├── app.py                # Main script executing data download and calculations
├── .gitignore            # Excludes temporary cache and venv files
└── README.md             # Project documentation