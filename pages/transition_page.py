import allure

from pages.base_page import BasePage

class SearchQuestionPage(BasePage):
    @allure.step('Поиск нужного вопроса')
    def scroll_question(self, locator):
        self.scroll_to_view(locator)

    @allure.step('Нажимаем на копку  {locator}')
    def find_question(self, locator, time = 20):
        self.scroll_question(locator)
        self.find_element_clickable(locator, time).click()

    @allure.step('Поиск ответа  {locator}')
    def drop_down_text(self, locator, time = 10):
        return self.find_element_located(locator, time)
