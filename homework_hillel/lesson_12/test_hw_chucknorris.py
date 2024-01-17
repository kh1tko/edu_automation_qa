import pytest
import requests


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    # перевірити поля "icon_url" чи він не пусти + чи це картинка, - 2 теста
    def test_url_icon(self):
        assert self.response.json().get('icon_url') is not None

    def test_url_icon_format(self):
        icon_url = self.response.json().get('icon_url', '')
        assert icon_url.endswith('png')

    # перевірити чи є ключ "value" і перевірити його значення - 2 теста
    def test_check__key_value(self):
        assert "value" in self.response.json()

    def test_check_value_value(self):
        assert self.response.json().get('value') is not None

    def test_check_year(self):
        assert int(self.response.json()["created_at"][:4]) > 1990, "All our jokes were created until 1990"

    def test_status_code(self):
        assert self.status_code == 200


def test_category():
    URL = "https://api.chucknorris.io/jokes/categories"
    response = requests.request(method="GET", url=URL)
    print(response.json())


@pytest.mark.parametrize("category",
                         requests.request(method="GET", url="https://api.chucknorris.io/jokes/categories").json())
def test_categories(category):
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = requests.request(method="GET", url=URL)
    assert len(response.json()["id"]) == 22

# Зробити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класому фікстуру
# тест на статус код
# тест на кількість жартів
# тест на сам жарт
# + 3 тести
