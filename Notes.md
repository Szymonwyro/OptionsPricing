# Black-Scholes Assumptions

We price under specific, ideal conditions. 
Most work is based around what happens when these conditions are violated
Underlying follows GBM; log-returns are normally distributed (constant drift, vol)
We know this is not true in reality - the volatility smile
No transaction costs, no spread, and fractinal shares traded instantly
Borrowing and lending happens freely at a constant risk-free rate
Underlying pays no dividends
The modelassumes we can hedge continuously

# The Greeks

Delta - option's sensitivity to a $1 move in the underlying, it is also the hedge ratio. If we are short a call with delta 0.6, we hold 0.6 shares to be instantaneously hedged. 

Gamma - rate of change of delta with respect to the underlying. How fast our hedge ration goes stale as price moves. This is why discrete hedging costs money: between rebalancing, gamma causes the hedge to drift out of alignment.

Vega - sensitivity to implied volatility. We will be comparing implied vs. realised volatility so vega tells how much a mismatch between the two costs or earns.

Theta - cost of time decay. For long options this is usually negative (we lose value as time passes), there is a direct relationship between theta and gamma through the BS PDE: the gamma PnL is roughly paid for by theta - core mechanic in gamma scalping. 

Rho - sensitivity to interest rates. Short dated equity options barely move on rate changes anyway.

# Put-call parity

European options on same underlying, strike and expire must obey: C - P = S - Ke^(-rT). Call - put must equal unerlying price - discounted strike. 

Non arbitrage argument necessitates this: 
Portfolio A: C + Ke^(-rT) ie. long call + hold cash
Portfolio B: P + S        ie. long put + long underlying

If anyone one portfolio is priced higher than the opther, we long the overpriced and short the underpriced.

# Distributions in Black-Scholes

Stnadard normal cumulative and its density.
Density used directly in gamma and vega formulae.
Model's log normal assumption:  N(d2) is the risk-neutral probability that the option finishes in the money. N(d2) adjusts for taking an expectation on the price of the underluing. 

Need to know: call delta = N(d1). This is why call delta [0,1] and put delta [-1, 0].

# Reminder on moneyness and other concepts

In the money where S > K
At the money where S ~~ K
Out the money where S < K

Intrinsic option value: payoff at that moment = max(S-K, 0)
Extrinsic (time) value: pricing a move before expiry (decays to 0 at expiry)
