import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск нужного элемента')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not found {locator}')


    @allure.step('Клик по нужному элементу')
    def find_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Элемент не кликабелен: {locator}')

    @allure.step('Ожидание нужного элемента')
    def presence_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((locator)))

    @allure.step('Пролистать до  нужного элемента')
    def scroll_to_view(self, locator, time=20):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

