from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

URL = "https://demoqa.com/checkbox"


class CheckboxPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(URL)
        return self

    def expand_folder(self, name):
        expand = self.driver.find_element(By.XPATH,
                                          f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        expand.click()

    def mark_folder(self, name):
        mark = self.driver.find_element(By.XPATH,
                                        f"//label[contains(@for, 'tree-node-{name}')]//*[contains(@class, 'rct-icon-uncheck')]")
        mark.click()

    def get_result_check_folder(self):
        result = self.driver.find_element(By.CSS_SELECTOR, 'span.text-success').text
        return result
