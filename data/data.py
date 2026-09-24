import yfinance as yf

data = yf.download("USO", period = "2y", interval = "1d")
data.to_csv("USO_prices.csv")