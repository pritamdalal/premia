import pytest
from premia.black_scholes_merton import price

def test_haug_put_value():
    option_type = "p"
    spot = 100
    strike = 95
    ttm = 0.5
    vol = 0.2
    risk_free = 0.1
    dividend = 0.05
    
    value_reference = 2.4648
    value_calc = price(option_type, spot, strike, ttm, vol, risk_free, dividend)
    assert abs(value_reference - value_calc) < 0.0001
        
    
