import pytest

def expected_to_fail(func):
    return pytest.mark.xfail(reason="Fails deliberately")(func)
    # @pytest.mark.xfail(reason="This test is designed to fail")
    # def wrapper(*args, **kwargs):
    #     return func(*args, **kwargs)
    # return wrapper
