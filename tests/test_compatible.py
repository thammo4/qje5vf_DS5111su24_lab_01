import os, sys, platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')));

import pytest
from tokenize_text import tokenize, clean_text
from tests.expected_failure_decorator import expected_to_fail


def test_platform_compatibility():
    """
    Given: test platform
    When: calling lib
    Then: warn platform not supported

    currently only Windows, Ubuntu, and Mac are supported.
    """
    os_ok = ["Windows", "Darwin", "Ubuntu", "Linux"]
    os_no_good = platform.system()

    assert os_no_good in os_ok, f"given os {os_no_good} only {os_ok} supported"


def test_python_version():
    """
    Given: test platform python version
    When: using
    Then: make sure the Python Version is 3.6+

    only Python3 is currently actively supported.
    """
    assert ((sys.version_info.major == 3) and (sys.version_info.minor > 6)), f"Python 3.6+ only [yours: {sys.version}]"



def test_pytest_version():
    """
    Given: calling pytest and build
    When: run pytest
    Then: check if the version is the one in the requirements.txt
    """

    assert pytest.__version__ == '7.4.4', f"pytest {pytest.__version__}  -- expected 7.4.4"
