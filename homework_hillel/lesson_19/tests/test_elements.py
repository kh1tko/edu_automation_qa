import pytest
from selenium.webdriver.remote.webelement import WebElement

from pythonProject.homework_hillel.lesson_19.DynamicPropertiesPage import PageDynamicProperties
from pythonProject.homework_hillel.lesson_19.ElementsPage import ElementsPage


class TestElementsPage:

    def test_page(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33

    #  todo перевірити відповіді всіх 33 елементів в елементс
    #  assert elements[2] == "Radio Button"
    @pytest.mark.parametrize('expected_element',
                             ['Text Box', 'Check Box', 'Radio Button', 'Web Tables', 'Buttons', 'Links',
                              'Broken Links - Images', 'Upload and Download', 'Dynamic Properties', '', '', '', '', '',
                              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
    def test_page(self, chrome, expected_element):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert expected_element in elements

    def test_is_button_enabled(self, chrome):
        page = PageDynamicProperties(chrome)
        page.open()
        button: WebElement = page.disable_enable_button()
        button.click()

    def test_is_button_shown(self, chrome):
        page = PageDynamicProperties(chrome).open()  # короткий запис
        button: WebElement = page.button_invisible_visible()
        button.click()
