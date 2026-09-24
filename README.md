# Options Pricer

A Black-Scholes options pricer and Greeks calculator built from first principles in Python, feeding into a planned delta-hedging P&L simulator that compares implied vs. realized volatility.

## Motivation

This project extends options theory (put-call parity, Black-Scholes, the Greeks) into working code, validated against reference values and real market data, as groundwork for a delta-hedging simulation: pricing an option, delta-hedging it over time using real historical price data, and decomposing the resulting P&L into its gamma, vega, and hedging-error components.

## Current status

**Pricing engine (`BS.py`)** — complete
- Closed-form Black-Scholes pricing for European calls and puts
- Full Greeks: delta, gamma, vega, theta, rho
- Validated against put-call parity and reference values

**Data pipeline (`data/`)** — in progress
- Historical daily price data pulled via `yfinance`, cached locally as CSV
- Currently working with USO (oil ETF)
- Next: log returns and annualized realized volatility from the price series

**Not yet started**
- Implied volatility (market data or assumed input)
- Delta-hedging simulation loop
- P&L decomposition and analysis (gamma/theta/vega attribution, hedge-frequency sensitivity)
- Planned: move the data pipeline behind a small FastAPI service

## Structure

BS.py # Black-Scholes pricer and Greeks
Pricer.py # script for computing/inspecting price + Greeks on sample inputs
data/ # cached historical price CSVs
USO_prices.csv

## Setup

python3 -m venv venv
source venv/bin/activate
pip install scipy pandas yfinance pytest

## Usage

```python
from BS import black_scholes_price, delta, gamma, vega, theta, rho

price = black_scholes_price(S=100, K=100, T=30/365, r=0.05, sigma=0.20, option_type="call")
```

Note: `theta` and `vega` are returned in their natural units — theta per year, vega per 1.00 (100 percentage points) of volatility — not the "per day" / "per 1%" conventions used in market quoting. Rescale at the point of use if needed.

## Background

Built as part of ongoing quant finance preparation, alongside options fundamentals (put-call parity, implied vs. realized volatility) and market-making theory.