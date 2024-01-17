import pytest
from .homework_15 import Calculator
from datetime import datetime


class TestCalculator:
    @classmethod
    def setup_class(cls):
        cls.start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('test_logs.txt', 'a') as file:
            file.write(f'\nStarted testing at {cls.start_time}\n')
        print('Testing started')

    @classmethod
    def teardown_class(cls):
        cls.end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('test_logs.txt', 'a') as file:
            file.write(f'Finished testing at {cls.end_time}\n')
        print('Testing finished')

    @pytest.mark.parametrize('a, b, expected_result', [

        pytest.param(2, 3, 5, id='Standard'),
        pytest.param(-10, 20, 10, id='One number negative'),
        pytest.param(-2, -3, -5, id='Two negative numbers'),
        pytest.param(0, 20, 20, id='add with one 0'),
        pytest.param(0, 0, 0, id='add with two 0')
    ])
    def test_addition(self, a, b, expected_result):
        calc = Calculator('Калькулятор')
        assert calc.addition(a, b) == expected_result

    @pytest.mark.parametrize('a, b, expected_result', [

        pytest.param(10, 2, 5, id='Standard'),
        pytest.param(-100, 20, -5.0, id='One number negative'),
        pytest.param(-99, -3, 33.0, id='Two negative numbers'),
        pytest.param(0, 23, 'Не тупи. На ноль не можна ділити)', id='add with one 0'),
        pytest.param(0, 0, 'Не тупи. На ноль не можна ділити)', id='add with two 0')
    ])
    def test_division(self, a, b, expected_result):
        calc = Calculator('Калькулятор')
        assert calc.division(a, b) == expected_result
