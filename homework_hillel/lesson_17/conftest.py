import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path='C:/code_test_chill/pythonProject/homework_hillel/lesson_17/chromedriver')
    yield driver
    driver.quit()
