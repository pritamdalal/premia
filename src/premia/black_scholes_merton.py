"""
Thin wrappers around py_vollib.black_scholes_merton using clear and explicit
parameter names to reduce user error.

Function signatures:
- option_type: 'c' (call) or 'p' (put)
- spot: underlying spot price S
- strike: strike price K
- ttm: time to maturity in years
- vol: annualized volatility sigma
- risk_free: annualized risk-free rate (continuously compounded)
- dividend: annualized continuous dividend yield q (0.0 for classic Black–Scholes)
"""

from typing import Dict, Iterable, Union
from py_vollib.black_scholes_merton import black_scholes_merton as _price
from py_vollib.black_scholes_merton.greeks.analytical import (
    delta as _delta,
    gamma as _gamma,
    theta as _theta,
    vega as _vega,
    rho as _rho,
)


def price(
    option_type: str,
    spot: float,
    strike: float,
    ttm: float,
    vol: float,
    risk_free: float,
    dividend: float = 0.0,
) -> float:
    option_type = option_type.lower()
    return _price(option_type, spot, strike, ttm, risk_free, vol, dividend)
    

def delta(
    option_type: str,
    spot: float,
    strike: float,
    ttm: float,
    vol: float,
    risk_free: float,
    dividend: float = 0.0,
) -> float:
    option_type = option_type.lower()   
    return _delta(option_type, spot, strike, ttm, risk_free, vol, dividend)


def gamma(
    option_type: str,
    spot: float,
    strike: float,
    ttm: float,
    vol: float,
    risk_free: float,
    dividend: float = 0.0,
) -> float:
    option_type = option_type.lower()
    return _gamma(option_type, spot, strike, ttm, risk_free, vol, dividend)


def theta(
    option_type: str,
    spot: float,
    strike: float,
    ttm: float,
    vol: float,
    risk_free: float,
    dividend: float = 0.0,
) -> float:
    option_type = option_type.lower()
    return _theta(option_type, spot, strike, ttm, risk_free, vol, dividend) * 365


def vega(
    option_type: str,
    spot: float,
    strike: float,
    ttm: float,
    vol: float,
    risk_free: float,
    dividend: float = 0.0,
) -> float:
    option_type = option_type.lower()
    return _vega(option_type, spot, strike, ttm, risk_free, vol, dividend)


def rho(
    option_type: str,
    spot: float,
    strike: float,
    ttm: float,
    vol: float,
    risk_free: float,
    dividend: float = 0.0,
) -> float:
    option_type = option_type.lower()
    return _rho(option_type, spot, strike, ttm, risk_free, vol, dividend)


# Assuming delta, gamma, theta, vega, rho already defined above
_FUNCS = {
    "price": price,
    "delta": delta,
    "gamma": gamma,
    "theta": theta,
    "vega":  vega,
    "rho":   rho,
}

def price_greeks(
    option_type: str,
    spot: float,
    strike: float,
    ttm: float,
    vol: float,
    risk_free: float,
    dividend: float = 0.0,
    which: Union[str, Iterable[str], None] = None,
) -> Dict[str, float]:

    if which is None:
        keys = _FUNCS.keys()
    elif isinstance(which, str):
        keys = [which]
    else:
        keys = list(which)

    return {
        k: _FUNCS[k](option_type, spot, strike, ttm, vol, risk_free, dividend)
        for k in keys
    }


if __name__ == "__main__":
    # option_type = "p"
    # spot = 100
    # strike = 95
    # dividend = 0.05
    # ttm = 0.5
    # risk_free = 0.1
    # vol = 0.2

    option_type = "c"
    spot = 100
    strike = 120
    ttm = 5
    vol = 0.30
    risk_free = 0.01
    dividend = 0


    # just price
    print(price(option_type, spot, strike, ttm, vol, risk_free, dividend))
    
    res_greeks = price_greeks(option_type, spot, strike, ttm, vol, risk_free, dividend)
    for ix_greek, ix_value in res_greeks.items():
        print(f"{ix_greek}: {ix_value}")
