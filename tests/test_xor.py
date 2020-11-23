"""Learning about how the xor operation works in python"""
import pytest
import operator


xor_tests = [
    (1, 1, 0),
    (4, 0, 4),
    (7, 0, 7),
    (7, 7, 0),
    (7, 2, 5),
    (7, 3, 4),
]


@pytest.mark.parametrize("buffer1,buffer2,expected", xor_tests)
def test_xor(buffer1, buffer2, expected):
    assert operator.xor(buffer1, buffer2) == expected
