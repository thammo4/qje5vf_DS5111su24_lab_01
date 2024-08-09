"""
f@#$@ you, pylint.
"""

import pytest

def expected_to_fail(func):
    """
    a docstring for a one line function, really?
    what else is there to even say at this point?
    """

    return pytest.mark.xfail(reason="Fails deliberately")(func)
