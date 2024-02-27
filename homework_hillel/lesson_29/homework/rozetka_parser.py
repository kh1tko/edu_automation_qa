from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()

driver.get('https://rozetka.com.ua/ua/all-tv/c80037/')


def scrape_and_write_data(driver):
    elements = WebDriverWait(driver, 10).until(
        ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '.goods-tile__inner')))
    with open("output.txt", "a", encoding="utf-8") as file:
        text = []
        for element in elements:
            title = element.find_element(By.CSS_SELECTOR, '.goods-tile__title').text
            price = element.find_element(By.CSS_SELECTOR, '.goods-tile__price-value').text
            text.append(f'{title}: {price}\n')
        file.writelines(text)


def get_url(n):
    scrape_and_write_data(driver)

    for page_num in range(2, n):
        driver.execute_script("window.scrollBy(0, 11000);")
        driver.implicitly_wait(10)
        next_button = driver.find_element(By.CSS_SELECTOR, f'a[href="/ua/all-tv/c80037/page={page_num}/"]')
        next_button.click()
        scrape_and_write_data(driver)


# Количество прогонов страниц (n + 1) можно передать в get_url, столько будет прогонов
n = 5
get_url(n + 1)
driver.quit()
