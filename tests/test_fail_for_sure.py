"""
    hiya
"""

import string
from test_base import *

@pytest.mark.xfail(reason="This test is deliberately set to fail")
def test_fail_for_sure():
    """
        sdfasdfqwef
    """
    expect = "Shall we not, like archers who have a mark to aim at, be more likely to hit upon what is right?"
    actual = "If this test is so shamelessly contrieved, have I really tested anything at all?"
    assert actual == expect, f"EXPECTED: '{expect}'. ACTUAL: '{actual}'"
