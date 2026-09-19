import math
from scipy.stats import norm

def main():

    def _d1_d2(S, K, T, r, sigma):

        # maybe unit test these too
        d1 = (math.log(S/K) + ((r + 0.5 * sigma**2)) * T) / (sigma * math.sqrt(T))
        
        d2 = d1 - sigma * math.sqrt(d1)
        
        N_d1 = norm.cdf(d1)
        N_d2 = norm.cdf(d2)
        
        N_neg_d1 = norm.cdf(-d1)
        N_neg_d2 = norm.cdf(-d2)
    
    def black_scholes_price(S, K, T, r, sigma, option_type="call"):

        # unit tests
        if sigma <=0 :
            raise ValueError(f"sigma must be positive, got {sigma}")
        if T <= 0:
            raise ValueError(f"T must be positive, got {T}")
    
        call_price = (S * _d1_d2.N_d1) - (K * math.exp(-r * T) * _d1_d2.N_d2)

        return call_price

    def black_scholes_price(S, K, T, r, sigma, option_type="put"):
    
            # unit tests
            if sigma <=0 :
                raise ValueError(f"sigma must be positive, got {sigma}")
            if T <= 0:
                raise ValueError(f"T must be positive, got {T}")
            if option_type not in ("call", "put"):
                raise ValueError(f"option_type must be 'call' or 'put', got {option_type!r}")
        
            put_price = (K * math.exp(-r * T) * _d1_d2.N_neg_d2) - (S * _d1_d2.N_neg_d1)
    
            return put_price

    def delta(S, K, T, r, sigma, option_type="call"):
        return _d1_d2.N_d1
    def delta(S, K, T, r, sigma, option_type = "put"):
        return _d1_d2.N_d1 - 1

    def gamma(S, K, T, r, sigma, option_type):
        return _d1_d2.N_d1 / (S * sigma * math.sqrt(T))
        

    def vega():

    def theta():

    def rho():

    
