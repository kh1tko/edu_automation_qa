import requests


class CurrencyDataHandler:
    def __init__(self, url='https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'):
        self.url = url
        self.json_data = self.get_currency_data()

    def get_currency_data(self):
        response = requests.get(self.url)
        json_data = response.json()
        return json_data

    def write_currency_data_to_file(self):
        creation_date = self.json_data[0].get('exchangedate', '')

        text_to_write = f'[Дата створення запиту]: {creation_date}\n'

        for index, currency_info in enumerate(self.json_data):
            currency_name = currency_info.get('txt', '')
            exchange_rate = currency_info.get('rate', '')
            text_to_write += f'{index + 1}. {currency_name} to UAH: {exchange_rate}\n'
        with open('currency.txt', 'w', encoding='utf-8') as file:
            file.write(text_to_write)


if __name__ == '__main__':
    currency_handler = CurrencyDataHandler()
    currency_handler.write_currency_data_to_file()
