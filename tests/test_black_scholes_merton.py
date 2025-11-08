import pytest
from premia.black_scholes_merton import price
from premia.black_scholes_merton import price_greeks

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

def test_haug_short_dated_call():
    option_type = "c"
    spot = 60
    strike = 65
    ttm = 0.25
    vol = 0.30
    risk_free = 0.08
    dividend = 0

    res_greeks = price_greeks(option_type, spot, strike, ttm, vol, risk_free, dividend)
    assert abs(res_greeks["price"] - 2.1333684449) < 0.000001
    assert abs(res_greeks["delta"] - 0.3724827980) < 0.000001 
    assert abs(res_greeks["gamma"] - 0.0420427558) < 0.000001
    assert abs(res_greeks["theta"] - -8.4281743867) < 0.000001
    assert abs((res_greeks["vega"] * 100) - 11.3515440535) < 0.000001
    assert abs((res_greeks["rho"] * 100) - 5.0538998582) < 0.000001


def test_greeks_r_package_call_values():
    option_type = "c"
    spot = 100
    strike = 120
    ttm = 5
    vol = 0.30
    risk_free = 0.01
    dividend = 0

    res_greeks = price_greeks(option_type, spot, strike, ttm, vol, risk_free, dividend)
    assert abs(res_greeks["price"] - 21.577149923) < 0.000001
    assert abs(res_greeks["delta"] - 0.554941778) < 0.000001 
    assert abs(res_greeks["gamma"] - 0.005890593) < 0.000001
    assert abs(res_greeks["theta"] - -2.989937331) < 0.000001
    assert abs((res_greeks["vega"] * 100) - 88.358901748) < 0.000001
    assert abs((res_greeks["rho"] * 100) - 169.585139380) < 0.000001


def test_odengard_call_values():
    option_type = "c"
    spot = 50
    strike = 50
    ttm = 0.5
    vol = 0.30
    risk_free = 0.1
    dividend = 0

    res_greeks = price_greeks(option_type, spot, strike, ttm, vol, risk_free, dividend)
    assert abs(res_greeks["price"] - 5.4532499260) < 0.000001
    assert abs(res_greeks["delta"] - 0.6337373578) < 0.000001 
    assert abs(res_greeks["gamma"] - 0.0354788717) < 0.000001
    assert abs(res_greeks["theta"] - -6.6147348677) < 0.000001
    assert abs((res_greeks["vega"] * 100) - 13.3045769042) < 0.000001
    assert abs((res_greeks["rho"] * 100) - 13.1168089819) < 0.000001


def test_odengard_put_and_call_values():
    spot = 100
    strike = 100
    ttm = 1
    vol = 0.25
    risk_free = 0.10
    dividend = 0

    call_greeks = price_greeks("c", spot, strike, ttm, vol, risk_free, dividend)
    put_greeks = price_greeks("p", spot, strike, ttm, vol, risk_free, dividend)
    
    # call values
    assert abs(call_greeks["price"] - 14.9757907783) < 0.000001
    assert abs(call_greeks["delta"] - 0.7002084045) < 0.000001 
    assert abs(call_greeks["gamma"] - 0.0139033306) < 0.000001
    assert abs(call_greeks["theta"] - -9.8492957711) < 0.000001
    assert abs((call_greeks["vega"] * 100) - 34.7583264292) < 0.000001
    assert abs((call_greeks["rho"] * 100) - 55.0450496748) < 0.000001

    # put values
    assert abs(put_greeks["price"] - 5.4595325819) < 0.000001
    assert abs(put_greeks["delta"] - -0.2997915955) < 0.000001 
    assert abs(put_greeks["gamma"] - 0.0139033306) < 0.000001
    assert abs(put_greeks["theta"] - -0.8009215908) < 0.000001
    assert abs((put_greeks["vega"] * 100) - 34.7583264292) < 0.000001
    assert abs((put_greeks["rho"] * 100) - -35.4386921288) < 0.000001
