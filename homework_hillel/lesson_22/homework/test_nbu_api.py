import pytest
from homework_hillel.lesson_22.homework.NBUapi import CurrencyDataHandler


class TestBase:
    @pytest.fixture
    def currency_data_handler(self):
        return CurrencyDataHandler()

    def test_creation_date_existence(self, currency_data_handler):
        assert currency_data_handler.json_data[0].get('exchangedate', '') != ''

    def test_list_currency_not_empty(self, currency_data_handler):
        assert len(currency_data_handler.json_data) > 0

    def test_currency_data_type(self, currency_data_handler):
        assert isinstance(currency_data_handler.json_data, list)

    def test_numbers_of_currency(self, currency_data_handler):
        assert currency_data_handler.json_data[7].get('txt', '') == 'Індійська рупія'

    def test_overall_sum_of_currency(self, currency_data_handler):
        assert len(currency_data_handler.json_data) == 61

    def test_write_currency_data_to_file(self, currency_data_handler):
        currency_data_handler.write_currency_data_to_file()
        with open('currency.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            assert '[Дата створення запиту]' in content

    def test_write_currency_data_to_file_two(self, currency_data_handler):
        currency_data_handler.write_currency_data_to_file()
        with open('currency.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            assert ' to UAH:' in content
