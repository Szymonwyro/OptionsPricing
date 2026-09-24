import math
from scipy.stats import norm

def _d1_d2(S, K, T, r, sigma):

    d1 = (math.log(S/K) + ((r + 0.5 * sigma**2)) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    return d1, d2
    
def black_scholes_price(S, K, T, r, sigma, option_type):

    if sigma <=0 :
        raise ValueError(f"sigma must be positive, got {sigma}")
    if T <= 0:
        raise ValueError(f"T must be positive, got {T}")

    d1, d2 = _d1_d2(S, K, T, r, sigma)
    
    if option_type == "call":
        return (S * norm.cdf(d1)) - (K * math.exp(-r * T) * norm.cdf(d2))
    elif option_type == "put":
        return (K * math.exp(-r * T) * norm.cdf(-d2)) - (S * norm.cdf(-d1))
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got {option_type}")


def delta(S, K, T, r, sigma, option_type):
    d1, _ = _d1_d2(S, K, T, r, sigma)

    if option_type == "call":
        return norm.cdf(d1)
    elif option_type =="put":
        return norm.cdf(d1) - 1
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got {option_type}")

def gamma(S, K, T, r, sigma, option_type="None"):
    d1, _ = _d1_d2(S, K, T, r, sigma)

    return norm.pdf(d1) / (S * sigma * math.sqrt(T))
        
def vega(S, K, T, r, sigma, option_type="None"):
    d1, _ = _d1_d2(S, K, T, r, sigma)

    return S * norm.pdf(d1) * math.sqrt(T)

def theta(S, K, T, r, sigma, option_type):
    d1, d2 = _d1_d2(S, K, T, r, sigma)

    if option_type == "call":
        return -(S * norm.pdf(d1) * sigma) / (2 * math.sqrt(T)) - r * K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return -(S * norm.pdf(d1) * sigma) / (2 * math.sqrt(T)) + r * K * math.exp(-r * T) * norm.cdf(-d2)
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got {option_type}")


def rho(S, K, T, r, sigma, option_type):
    d1, d2 = _d1_d2(S, K, T, r, sigma)
    
    if option_type == "call":
        return K * T * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return -K * T * math.exp(-r * T) * norm.cdf(-d2)
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got {option_type}")
