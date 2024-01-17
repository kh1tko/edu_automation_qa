import pytest
from .homework_09 import add_three_numbers


# solution 1
def test_1():
    assert add_three_numbers(3, 4, 5) == 35


def test_2():
    assert add_three_numbers(13, 4, 2) == 34


def test_3():
    assert add_three_numbers(1, 4, 5) == 25


# solution 2
@pytest.mark.parametrize("numb_1, numb_2, numb_3, result", [
    pytest.param(1, 1, 1, 2, id="standard"),
    pytest.param(-1, 2, 1, 1, id="negative and positive"),
    pytest.param(-1, -1, -1, 2, id="three negative")])
def test_set_1(numb_1, numb_2, numb_3, result):
    assert add_three_numbers(numb_1, numb_2, numb_3) == result


# solution 3
list_test = [(3, 4, 7, 49), (3, 3, 3, 18), (-3, -1, -4, 16)]


@pytest.mark.parametrize("numb_1, numb_2,numb_3, result", list_test)
def test_set_2(numb_1, numb_2, numb_3, result):
    assert add_three_numbers(numb_1, numb_2, numb_3) == result
