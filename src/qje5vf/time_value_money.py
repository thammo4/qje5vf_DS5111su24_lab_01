"""
    Time Value of Money Equations

    These functions compute the present or future value of a specified amount of money which
    accumulates or discounts a particular number of times at a specified interest rate over
    a specified number of years
"""


def present_value(future_value, interest_rate, compound_periods, years):
    if compound_periods == 0:
        return "no compound periods?"
    return future_value / (1 + interest_rate/compound_periods) ** (compound_periods * years)

def future_value(present_value, interest_rate, compound_periods, years):
    if compound_periods == 0:
        return "cant compound zero times"
    return present_value * (1 + interest_rate/compound_periods) ** (compound_periods * years)
