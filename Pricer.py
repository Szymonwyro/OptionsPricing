import pandas as pd
from BS import black_scholes_price, delta, gamma, vega, theta, rho

data = pd.read_csv("data/USO_prices.csv", skiprows=[1,2], index_col=0, parse_dates = True)

S = data["Close"].iloc[-1]  # Most recent price
K = round(S)                # Arbitrary strike price near the money
T = 30 / 365                # 30 days to expiry, as fraction of year
r = 0.05                    # assumed risk-free rate
sigma = 0.20                # arbitrary value - will become realized vol                   

for option_type in ("call", "put"):
    print(option_type)
    print("price:", black_scholes_price(S, K, T, r, sigma, option_type))
    print("delta:", delta(S, K, T, r, sigma, option_type))
    print("gamma:", gamma(S, K, T, r, sigma))
    print("vega: ", vega(S, K, T, r, sigma))
    print("theta:", theta(S, K, T, r, sigma, option_type))
    print("rho:  ", rho(S, K, T, r, sigma, option_type))