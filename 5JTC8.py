zdravo# sample for @pytest.mark.parametrize
import pytest


def add(a, b):
    return a + b


# Parametrize the test function with different sets of arguments
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, -2, -3), (1.5, 2.5, 4.0)])
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected
