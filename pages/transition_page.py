import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MaimPage

class SearchQuestion(MaimPage):
    @allure.step('Поиск нужного вопроса')
    def scroll_question(self, locator, time=20):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Нажимаем на копку  {locator}')
    def find_question(self, locator):
        self.scroll_question(locator)
        self.find_element_clickable(locator).click()

    @allure.step('Поиск ответа  {locator}')
    def drop_down_text(self, locator, time = 10):
        return self.find_element_located(locator, time)
