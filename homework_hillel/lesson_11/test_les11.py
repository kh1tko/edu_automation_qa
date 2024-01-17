import time
import pytest


def test_delayed_execution_1():
    time.sleep(2)
    assert True
    print("Test 1 executed")


def test_delayed_execution_2():
    time.sleep(2)
    assert not False
    print("Test 2 executed")


def test_delayed_execution_3():
    time.sleep(2)
    assert len('Concatenation') == 13
    print("Test 3 executed")


def test_delayed_execution_4():
    time.sleep(2)
    assert 'Hunter' == 'HUNTER'.title()
    print("Test 4 executed")


@pytest.mark.unique
def test_unique_delayed_execution():
    time.sleep(2)
    assert 3 ** 3 == pow(3, 3)
    print('Test unique 5 executed! ')

# pytest -n 5 -v
# pytest -k unique -v
