# FILE: tests/test_integrate.py
import sys
import os
import string
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest



def test_fail_for_sure():
    expect = "Shall we not, like archers who have a mark to aim at, be more likely to hit upon what is right?";
    actual = "If this test is so shamelessly contrieved, have I really tested anything at all?";
    assert actual == expect, f"EXPECTED: '{expect}'. ACTUAL: '{actual}'";

