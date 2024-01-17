import pytest
import requests


class ChuckNorrisJokeSearch:
    def __init__(self, query):
        self.query = query
        self.base_url = "https://api.chucknorris.io/jokes/search"

    def search_joke(self):
        url = f"{self.base_url}?query={self.query}"
        response = requests.get(url)
        return response


@pytest.fixture
def joke_search_fixture():
    search_instance = ChuckNorrisJokeSearch(query='iphone')
    return search_instance.search_joke()


def test_search_status_code(joke_search_fixture):
    assert joke_search_fixture.status_code == 200


def test_search_number_of_jokes(joke_search_fixture):
    assert joke_search_fixture.json().get('total') == 8


def test_search_first_joke(joke_search_fixture):
    jokes = joke_search_fixture.json().get('result')
    assert jokes[0].get('value') == ('I just downloaded the new "Roundhouse Kick" app for my iPhone and now my screen '
                                     'is cracked and the phone does not work. Damn you, Chuck Norris.')
