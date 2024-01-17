import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()
